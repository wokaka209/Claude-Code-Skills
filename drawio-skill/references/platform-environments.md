# 平台与环境区分

`drawio-skill` 必须区分运行环境。

至少要区分：

- macOS
- Windows
- Linux

原因很直接：

- draw.io 可执行文件路径不同
- Shell 语法和路径写法不同
- 导出 PNG 的稳定性和可调用方式不同

## 1. 总原则

不要假设所有机器都能用同一条命令。

生成或导出 `.drawio` 时，默认流程应是：

1. 先识别平台
2. 再决定 draw.io 可执行文件路径
3. 再决定是否需要用户显式提供 `DRAWIO_BIN`

如果平台不明确，不要直接硬编码 macOS 路径。

## 2. macOS

最常见的安装方式是 App bundle：

```text
/Applications/draw.io.app/Contents/MacOS/draw.io
```

有些用户会安装成：

```text
/Applications/diagrams.net.app/Contents/MacOS/draw.io
```

建议：

- 优先尝试 App bundle 路径
- 其次再尝试 `drawio` 在 PATH 中的命令
- Electron 崩溃时，保留 sleep 间隔

## 3. Windows

Windows 环境要先分清你是在什么 shell 中运行：

- Git Bash / MSYS2 / Cygwin
- PowerShell
- CMD

当前 skill 内置导出脚本主要面向 Bash 风格环境，因此更适合：

- Git Bash
- MSYS2
- Cygwin

常见安装位置：

```text
C:\Program Files\draw.io\draw.io.exe
C:\Program Files\diagrams.net\draw.io.exe
```

在 Bash 风格 shell 中通常会表现为：

```text
/c/Program Files/draw.io/draw.io.exe
/c/Program Files/diagrams.net/draw.io.exe
```

建议：

- Windows 下优先建议用户在 Git Bash 里运行脚本
- 如果装在非标准路径，显式设置 `DRAWIO_BIN`

## 4. Linux

Linux 更常见的是 PATH 安装或包管理器安装。

常见位置：

```text
/usr/bin/drawio
/usr/local/bin/drawio
/snap/bin/drawio
/opt/drawio/drawio
```

建议：

- 先尝试 PATH 中的 `drawio`
- 再尝试常见安装路径
- 如是容器或远程环境，确认图形依赖是否满足 CLI 导出

## 5. WSL 与特殊环境

WSL 在技术上属于 Linux，但很多用户实际想调用 Windows 的 draw.io。

这种环境不要自动假设一定可行。

如果是 WSL：

- 最稳妥的方式是用户手动设置 `DRAWIO_BIN`
- skill 里要明确告诉用户这是"特殊环境"

## 6. 推荐环境变量

导出脚本支持这些变量：

- `DRAWIO_PLATFORM`
- `DRAWIO_BIN`
- `DRAWIO_EXPORT_SCALE`
- `DRAWIO_EXPORT_BORDER`
- `DRAWIO_EXPORT_SLEEP_SECONDS`