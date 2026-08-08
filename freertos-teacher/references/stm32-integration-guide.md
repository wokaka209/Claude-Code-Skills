# STM32 + FreeRTOS 集成指南

## CubeMX 配置清单

### 1. SYS 配置（最关键！）

```
System Core → SYS
├── Debug: Serial Wire
└── Timebase Source: TIM6  ← 必须改！不能用 SysTick
```

**为什么不能用 SysTick？**
- FreeRTOS 的 `xTaskIncrementTick()` 需要独占 SysTick
- HAL 库的 `HAL_Delay()` 和 `HAL_IncTick()` 也依赖 SysTick
- 两者冲突会导致系统卡死或行为异常

### 2. FreeRTOS 中间件配置

```
Middleware → FREERTOS
├── Interface: CMSIS_V2  ← 推荐用 V2，API 更清晰
├── Tasks and Queues
│   ├── defaultTask (默认任务，可改名)
│   │   ├── Stack Size: 256 (字)  ← 按需调整
│   │   └── Priority: osPriorityNormal
│   └── + Add 添加更多任务
├── Config Parameters
│   ├── Kernel: 见下方配置表
│   ├── Include parameters: 功能开关
│   └── Memory settings: 堆大小
└── Timers and Semaphores
    ├── + Add 添加信号量/互斥锁/定时器
    └── 设置名称和类型
```

### 3. FreeRTOSConfig.h 关键参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| `configTICK_RATE_HZ` | 1000 | 1ms 一个 tick |
| `configMAX_PRIORITIES` | 56 | STM32 支持的最大优先级数 |
| `configMINIMAL_STACK_SIZE` | 128 | 最小栈大小（字），建议 >= 128 |
| `configTOTAL_HEAP_SIZE` | 10240 | 堆大小（字节），按 RAM 调整 |
| `configUSE_PREEMPTION` | 1 | 抢占式调度 |
| `configUSE_TIME_SLICING` | 1 | 同优先级时间片轮转 |
| `configUSE_MUTEXES` | 1 | 启用互斥锁 |
| `configUSE_COUNTING_SEMAPHORES` | 1 | 启用计数信号量 |
| `configUSE_TASK_NOTIFICATIONS` | 1 | 启用任务通知 |
| `configUSE_TIMERS` | 1 | 启用软件定时器 |
| `configCHECK_FOR_STACK_OVERFLOW` | 2 | 栈溢出检测（调试阶段） |

### 4. 中断优先级配置

```c
// STM32 中断优先级分组：通常配置为 NVIC_PRIORITYGROUP_4
// 即 4 位抢占优先级，0 位子优先级
// 优先级范围：0-15，数值越小优先级越高

// FreeRTOS 只管理优先级 <= configMAX_SYSCALL_INTERRUPT_PRIORITY 的中断
// 这些中断可以调用 FreeRTOS API（xxxFromISR 函数）
// 优先级 > configMAX_SYSCALL_INTERRUPT_PRIORITY 的中断不受 FreeRTOS 管理
// 不能调用任何 FreeRTOS API，但响应最快（不会被 FreeRTOS 延迟）

// 推荐配置：
#define configMAX_SYSCALL_INTERRUPT_PRIORITY  5  // 优先级 0-4 不受管理，5-15 受管理
#define configLIBRARY_LOWEST_INTERRUPT_PRIORITY  15  // 最低中断优先级
#define configLIBRARY_MAX_SYSCALL_INTERRUPT_PRIORITY 5  // 最高可调用 API 的中断优先级
```

**实际影响：**
- 优先级 0-4 的中断：不能调用 FreeRTOS API，但永远不会被 FreeRTOS 关闭
- 优先级 5-15 的中断：可以调用 xxxFromISR API，临界区内会被暂时关闭
- 如果在优先级 0-4 的中断里调用了 FreeRTOS API，会直接导致系统崩溃

## 代码生成后的文件结构

```
Core/
├── Inc/
│   ├── FreeRTOSConfig.h    ← FreeRTOS 配置
│   ├── main.h
│   └── ...
├── Src/
│   ├── main.c              ← 主程序
│   ├── freertos.c          ← FreeRTOS 任务代码（用户代码写在这里）
│   ├── stm32f4xx_it.c      ← 中断处理（不要修改 SysTick_Handler）
│   └── ...
Middlewares/
├── Third_Party/
│   └── FreeRTOS/
│       └── Source/          ← FreeRTOS 内核源码（不要修改）
```

## 用户代码位置

CubeMX 生成的代码中，所有 `/* USER CODE BEGIN */` 和 `/* USER CODE END */` 之间是安全的用户代码区。重新生成代码时这些区域会被保留。

```c
/* USER CODE BEGIN Header */
// 任务函数声明放这里

/* USER CODE END Header */

/* USER CODE BEGIN 4 */
// 任务实现放这里

/* USER CODE END 4 */
```

## 常见问题排查

### 问题 1：系统卡死不运行

**可能原因：**
- SysTick 冲突（Timebase Source 没改成 TIM6）
- 中断优先级配置错误
- 栈溢出

**排查步骤：**
1. 检查 CubeMX 中 SYS → Timebase Source 是否为 TIM6
2. 检查 `configMAX_SYSCALL_INTERRUPT_PRIORITY` 设置
3. 开启 `configCHECK_FOR_STACK_OVERFLOW = 2`

### 问题 2：任务不执行

**可能原因：**
- 任务优先级太低，被高优先级任务饿死
- 任务阻塞在某个 API 上（如 xQueueReceive 等待数据）
- 任务栈溢出

**排查步骤：**
1. 用 `uxTaskGetNumberOfTasks()` 检查任务数
2. 用 `eTaskGetState()` 检查任务状态
3. 检查任务函数中是否有阻塞调用

### 问题 3：HardFault

**可能原因：**
- 栈溢出（最常见）
- 在高优先级中断中调用了 FreeRTOS API
- 内存不足，任务创建失败但没检查返回值

**排查步骤：**
1. 开启栈溢出检测
2. 检查所有中断优先级是否 > configMAX_SYSCALL_INTERRUPT_PRIORITY
3. 检查 `xTaskCreate()` 返回值
4. 用 `xPortGetFreeHeapSize()` 检查剩余堆空间
