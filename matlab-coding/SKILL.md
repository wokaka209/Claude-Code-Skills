---
name: matlab-coding
description: MATLAB coding standards, CLI invocation patterns, and style guidelines. Use when writing, reviewing, debugging .m files, or automatically running MATLAB scripts via CLI (-batch mode). Covers naming, layout, best practices per MathWorks guidelines, and AI-automated MATLAB execution workflow.
license: MIT
---

# MATLAB 编码规范

基于 MathWorks 官方 [MATLAB Coding Guidelines](https://github.com/mathworks/MATLAB-Coding-Guidelines) 和社区 [matlab/rules](https://github.com/matlab/rules)。

**使用场景：** 编写、审阅或调试 `.m` 文件时触发。适用于脚本、函数、类文件。

---

## 1. 命名规范

### 变量
| 规则 | 示例 |
|------|------|
| **lowerCamelCase**，多词首单词小写后续首字母大写 | `totalPowerLoss`, `gibbsFreeEnergy` |
| 数学表达式/循环迭代器可用单字母 | `i`, `n`, `k`, `x` |
| 不超过 **32 字符** | — |
| 避免缩写，除非领域通行标准 | `freq` → `frequency` |
| **禁止**与 MATLAB 内置函数重名 | 勿用 `sum`, `max`, `sin` 作变量名 |
| 布尔变量用 `is`/`has` 前缀 | `isValid`, `hasConverged` |

### 函数
| 规则 | 示例 |
|------|------|
| **lowerCamelCase** | `calculatePower`, `readData` |
| 动词或动词短语 | `plotResponse`, `saveResults` |
| 转换函数用 `2` 连接 | `struct2table`, `joule2Calorie` |
| 文件名**必须**与主函数名一致 | `myFunc.m` → `function myFunc()` |

### 其他
| 标识符 | 风格 | 示例 |
|--------|------|------|
| 类名 | UpperCamelCase | `PidController`, `MotorModel` |
| 属性/事件 | UpperCamelCase | `LineWidth`, `DataReady` |
| Name-Value 参数 | UpperCamelCase | `'DisplayName'`, `'LineStyle'` |

---

## 2. 格式布局

### 缩进
- **4 空格**（非 Tab）
- 所有控制结构体（`if`, `for`, `while`, `switch`, `try`）必须缩进

### 行宽
- 代码和注释 ≤ **120 字符**
- 长行在逗号、空格或二元运算符后换行

### 空格
```
% 正确
x = a + b;
y = (a > b) && (c < d);
z(i, j) = x .* y;

% 错误
x=a+b;
y=(a>b)&&(c<d);
z(i,j)=x.*y;
```

- 赋值 `=` 和比较运算符两侧各 1 空格
- 逗号和分号后加空格（不在行尾）
- 括号内侧**不**加空格
- 浮点数写前导 0（`0.5` 非 `.5`）

### 空行
- 逻辑段落间用空行分隔
- `%%` 分区前后各 1 空行

---

## 3. 注释与文档

### 文件头
```matlab
%% 简短描述
% 详细说明：输入、输出、副作用
% 使用示例
```

### 函数文档
- 函数声明后紧接 **H1 行**（一行摘要）
- `arguments` 块做输入验证（对外接口函数必须）

### 行内注释
- 注释放在代码**之前**，描述"为什么"而非"是什么"
- `%` 后至少 1 空格
- 对复杂逻辑或隐藏约束加注释

---

## 4. 语句与表达式

### 通用规则
```
% 正确
x = 1;
y = 2;

% 错误（一行多语句）
x = 1; y = 2;
```

- **禁止**在函数/方法内使用命令语法（用函数语法 `()` ）
- 字面常量赋给变量再使用，不硬编码
- 优先用 `"` 字符串（R2017a+）

### 控制流
- 嵌套不超过 **5 层**
- `for` 循环内**不修改**循环变量
- `if-else` 将**常见情况**放 `if` 分支
- `switch` 始终包含 `otherwise`
- 避免 `eval`、`evalin`、`assignin`

### 数组操作
- **预分配**数组，不循环内增长
```matlab
% 正确
y = zeros(n, 1);
for k = 1:n
    y(k) = k^2;
end

% 错误
y = [];
for k = 1:n
    y(end+1) = k^2;
end
```

---

## 5. 函数编写

### 格式
```matlab
function [out1, out2] = myFunction(in1, in2)
    % MYFUNCTION 一行摘要
    % 详细说明
    arguments
        in1 (1,1) double {mustBePositive}
        in2 (1,:) char
    end
    out1 = in1 * 2;
    out2 = upper(in2);
end
```

- 参数不超过 **6 入 / 4 出**
- 用 `arguments` 做输入验证
- 匿名函数保持简洁
- 所有函数以 `end` 结尾

### 错误处理
- 修复 Code Analyzer 全部警告
- `try-catch` 必须有配套的 `catch`
- 用 `MException` 做精细错误恢复
- 避免用 `try-catch` 做正常控制流

---

## 6. 脚本编写（特指 .m 脚本）

```matlab
%% 脚本用途描述
clear; clc; close all;

%% 参数定义
inputFile  = 'data.csv';
nIter      = 100;
tolerance  = 1e-6;

%% 数据处理
data = csvread(inputFile, 1, 0);
% ...

%% 结果可视化
figure('Name', '结果');
plot(data(:,1), data(:,2), 'b-');
xlabel('时间 (s)'); ylabel('幅值'); grid on;
```

- 顶部注释描述用途
- 常量集中定义在脚本开头
- 用 `%%` 做段落分区
- 不用 `global` 变量

---

## 7. 常见陷阱

| ❌ 不要 | ✅ 要 |
|---------|------|
| `eval('x = 1')` | 直接赋值 `x = 1` |
| `a == 0.1`（浮点相等比较） | `abs(a - 0.1) < eps` |
| 循环内不预分配 | 预分配 `zeros(n,1)` |
| 变量名与函数重名（`sum`, `max`） | 用描述性名称 |
| 函数/脚本超过 200 行 | 拆分为多个小函数 |
| 隐藏 `;` 输出 | 赋值语句加分号 |

---

## 8. 与 AI 协作时的特殊要求

生成 MATLAB 代码时，AI 应额外遵守：

1. **不生成死代码** — 不生成示例数据占位、未使用的函数、注释掉的备选实现
2. **名称一致** — 函数名、文件名、调用处的名称必须完全一致
3. **索引从 1 开始** — MATLAB 数组索引从 1 开始（非 0）
4. **向量化优先** — 能用矩阵运算代替循环时，用矩阵运算
5. **`.m` 文件编码** — 使用 UTF-8 编码
6. **行末不写分号测试** — 调试用 `disp()` 而非移除分号
7. **文件路径** — 用 `fullfile` 跨平台拼接路径

---

## 9. MATLAB CLI 调用指南（AI 自动化执行）

当 AI 需要通过命令行自动调用 MATLAB 运行 `.m` 脚本时，遵循以下模式。

### 9.1 基础调用模式

```bash
cmd //c "F:\matlab_2022\bin\matlab.exe" -nosplash -nodesktop \
  -logfile "C:\Users\coolkey\matlab_out.log" \
  -batch "cd('D:/3M_project'); run('script.m'); exit;"
```

| 参数 | 用途 |
|------|------|
| `-nosplash` | 跳过启动画面 |
| `-nodesktop` | 不启动桌面 GUI |
| `-batch` | 非交互模式，执行后自动退出（R2019a+） |
| `-logfile <path>` | **必须**添加，否则输出不可见 |
| `cd('D:/3M_project')` | 切换到项目根目录 |

### 9.2 输出捕获

MATLAB CLI 的输出通过 `-logfile` 写入文件。调用流程：

1. 启动 MATLAB（背景任务，设超时 ≥ 120s）
2. 等待 60-90 秒（首次启动含 JVM 初始化 + 许可证验证）
3. 读取 logfile 获取输出
4. 清理临时 logfile

```matlab
% 在 -batch 中使用 fprintf + disp 输出关键信息
fprintf('RESULT: Kp=%.4f, Ki=%.4f\n', kp, ki);
```

### 9.3 启动时间预算

| 阶段 | 耗时 | 说明 |
|------|------|------|
| JVM 启动 + 许可证 | ~45-60s | 首调用较慢，连续调用可复用许可证缓存 |
| 脚本执行 | 取决于脚本 | 系统辨识 ~30-60s，扫参 ~2-10min |
| 总预算 | 脚本时间 + 90s | 设超时 = 脚本预估时间 + 120s |

### 9.4 图形输出

MATLAB 的 `figure` / `plot` 在 `-batch` 模式下默认不可见。处理方式：

```matlab
f = figure('Visible', 'off');
plot(x, y);
saveas(f, 'output.png');
close(f);
```

### 9.5 调试技巧

- 在脚本末尾加 `fprintf('DONE\n')`，AI 通过搜索 "DONE" 确认正常结束
- 关键中间结果用 `fprintf` 输出，而非依赖 `disp`（某些情况下 disp 被缓冲）
- 通过 `exist` 检查变量后再使用，防止因前次运行残留导致误判
- 错误处理：`-batch` 模式下脚本报错会自动退出并返回非零 exit code
