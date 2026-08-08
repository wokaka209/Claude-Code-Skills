# FreeRTOS 同步与通信机制选择指南

## 快速选择表

| 需求 | 推荐机制 | 替代方案 |
|------|---------|---------|
| 任务 A 通知任务 B "某件事发生了" | 二值信号量 | 任务通知 |
| 中断通知任务 "数据准备好了" | 二值信号量 | 任务通知（更快） |
| N 个相同资源可用（如缓冲区槽位） | 计数信号量 | — |
| 多个任务共享一个外设（如 UART） | 互斥锁 | — |
| 任务间传递数据（如传感器读数） | 队列 | — |
| 等待多个条件中的任意一个/全部满足 | 事件组 | — |
| 快速、轻量的任务间通知（无数据） | 任务通知 | 二值信号量 |

## 各机制对比

### 1. 队列（Queue）

**用途：** 任务间传递**数据**

```c
// 场景：传感器任务采集数据，处理任务消费
QueueHandle_t xDataQueue = xQueueCreate(10, sizeof(SensorData_t));

// 传感器任务
void SensorTask(void *param) {
    SensorData_t data;
    for (;;) {
        data = ReadSensor();
        xQueueSend(xDataQueue, &data, portMAX_DELAY);  // 满了会阻塞
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

// 处理任务
void ProcessTask(void *param) {
    SensorData_t data;
    for (;;) {
        xQueueReceive(xDataQueue, &data, portMAX_DELAY);  // 空了会阻塞
        ProcessData(&data);
    }
}
```

**特点：**
- 可以传递任意大小的数据（创建时指定）
- 深度可配置（队列长度）
- 满/空时可阻塞、超时或立即返回
- ISR 版本：`xQueueSendFromISR`、`xQueueReceiveFromISR`

### 2. 二值信号量（Binary Semaphore）

**用途：** 任务间/中断与任务间**同步**（不含数据）

```c
// 场景：按键中断通知任务处理
SemaphoreHandle_t xButtonSem = xSemaphoreCreateBinary();

// 按键中断回调
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) {
    if (GPIO_Pin == BUTTON_Pin) {
        BaseType_t xHigherPriorityTaskWoken = pdFALSE;
        xSemaphoreGiveFromISR(xButtonSem, &xHigherPriorityTaskWoken);
        portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
    }
}

// 处理任务
void ButtonTask(void *param) {
    for (;;) {
        xSemaphoreTake(xButtonSem, portMAX_DELAY);  // 等待信号
        HandleButtonPress();
    }
}
```

**特点：**
- 只有 "有/无" 两种状态
- 不传递数据，只传递"事件"
- 创建时初始状态为"无"（与互斥锁不同）
- ISR 中只能 Give，不能 Take

### 3. 计数信号量（Counting Semaphore）

**用途：** 管理**多个相同资源**的访问

```c
// 场景：3 个缓冲区槽位，多个任务竞争使用
SemaphoreHandle_t xBufferSem = xSemaphoreCreateCounting(3, 3);

void WorkerTask(void *param) {
    for (;;) {
        // 等待缓冲区可用（计数 > 0 才能 Take）
        xSemaphoreTake(xBufferSem, portMAX_DELAY);

        UseBuffer();  // 使用缓冲区

        xSemaphoreGive(xBufferSem);  // 归还缓冲区
    }
}
```

**特点：**
- 计数范围 0 ~ MaxCount
- 每次 Take 计数减 1，每次 Give 计数加 1
- 计数为 0 时 Take 会阻塞

### 4. 互斥锁（Mutex）

**用途：** 保护**共享资源**，防止多任务同时访问

```c
// 场景：两个任务共用 UART 打印
SemaphoreHandle_t xUartMutex = xSemaphoreCreateMutex();

void TaskA(void *param) {
    for (;;) {
        xSemaphoreTake(xUartMutex, portMAX_DELAY);  // 加锁
        printf("TaskA: data = %d\n", GetData());     // 临界区
        xSemaphoreGive(xUartMutex);                   // 解锁
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

void TaskB(void *param) {
    for (;;) {
        xSemaphoreTake(xUartMutex, portMAX_DELAY);
        printf("TaskB: status = %d\n", GetStatus());
        xSemaphoreGive(xUartMutex);
        vTaskDelay(pdMS_TO_TICKS(150));
    }
}
```

**特点：**
- 有**优先级继承**机制：低优先级任务持有锁时，会被提升到等待锁的最高优先级
- 防止优先级反转问题
- 只有持有者能释放（与信号量不同）
- ISR 中不能使用

### 5. 事件组（Event Group）

**用途：** 等待**多个条件**的组合

```c
// 场景：等待 WiFi 连接 AND 传感器就绪 才开始工作
EventGroupHandle_t xEvents = xEventGroupCreate();

#define WIFI_CONNECTED_BIT  (1 << 0)
#define SENSOR_READY_BIT    (1 << 1)

// WiFi 任务
void WifiTask(void *param) {
    ConnectWifi();
    xEventGroupSetBits(xEvents, WIFI_CONNECTED_BIT);
}

// 传感器任务
void SensorTask(void *param) {
    InitSensor();
    xEventGroupSetBits(xEvents, SENSOR_READY_BIT);
}

// 主任务：等待两个条件都满足
void MainTask(void *param) {
    xEventGroupWaitBits(xEvents,
                        WIFI_CONNECTED_BIT | SENSOR_READY_BIT,
                        pdTRUE,   // 满足后清除
                        pdTRUE,   // AND 逻辑
                        portMAX_DELAY);
    StartOperation();
}
```

**特点：**
- 每个事件占 1 bit（最多 24 个事件，取决于 `configUSE_16_BIT_TICKS`）
- 支持 AND（等待所有）和 OR（等待任意）
- 可以在满足后自动清除

### 6. 任务通知（Task Notification）

**用途：** 最轻量的**任务间通知**机制

```c
// 场景：ISR 通知任务处理数据（替代二值信号量，更快）
void DMA_IRQHandler(void) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    vTaskNotifyGiveFromISR(DataTaskHandle, &xHigherPriorityTaskWoken);
    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}

void DataTask(void *param) {
    for (;;) {
        ulTaskNotifyTake(pdTRUE, portMAX_DELAY);  // 等待通知
        ProcessData();
    }
}
```

**特点：**
- 比信号量快（不经过队列机制）
- 每个任务只有一个通知值（32 位）
- 可以用作二值信号量（Give/Take）或传递数值
- 不能用于多个任务等待同一个通知（一对一）

## 选择决策树

```
需要传递数据？
├── 是 → 队列（Queue）
└── 否 → 需要保护共享资源？
    ├── 是 → 互斥锁（Mutex）
    └── 否 → 需要计数？
        ├── 是 → 计数信号量（Counting Semaphore）
        └── 否 → 需要等待多个条件？
            ├── 是 → 事件组（Event Group）
            └── 否 → 简单的事件通知？
                ├── 是 → 任务通知（最快） 或 二值信号量
                └── 否 → 重新审视需求
```

## 性能对比

| 机制 | 创建开销 | 操作耗时 | RAM 占用 |
|------|---------|---------|---------|
| 任务通知 | 无（已内置于 TCB） | 最快 ~0.5us | 0（额外） |
| 二值信号量 | 中等 | 较快 ~1us | 较少 |
| 计数信号量 | 中等 | 较快 ~1us | 较少 |
| 互斥锁 | 中等 | 较快 ~1us | 较少 |
| 队列 | 中等 | 中等 ~1.5us | 较多（含数据缓冲区） |
| 事件组 | 中等 | 较慢 ~2us | 较少 |
