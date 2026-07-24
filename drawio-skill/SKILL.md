---
name: drawio-skill
description: Create, edit, normalize, review, and export draw.io / diagrams.net `.drawio` files. Use this whenever the user mentions draw.io, diagrams.net, `.drawio`, 架构图, 流程图, UML, BPMN, 时序图, AWS 架构图, PNG 导出, XML 坐标微调, 多页 drawio, or 压缩 drawio 文件, even if the user does not explicitly ask for a "skill."
compatibility:
  tools:
    - exec_command
    - apply_patch
  dependencies:
    required:
      - python3
    optional:
      - macOS: draw.io.app or diagrams.net.app
      - Windows: draw.io.exe, ideally from Git Bash / MSYS2
      - Linux: drawio CLI in PATH or common install path
---

# drawio-skill

这个 skill 用于高质量地创建、修改、审查和导出 draw.io / diagrams.net 的 `.drawio` 文件。

目标不是"能生成图"，而是生成：

- 准确的图
- 可维护的图
- 连线干净的图
- 视觉上不平庸、不拥挤、不同质化的图
- 有成品感、适合文档与技术文章的图

它明确覆盖 4 类工作：

1. 新建图表
2. 修改已有 `.drawio`
3. 审查或解释图表结构
4. 把 `.drawio` 导出为 PNG，或为后续手工编辑做归一化处理

## 先做什么

先判断用户要的是哪一类任务：

- 新建图：先选图种，再决定是否参考官方样例
- 修改已有图：先检查文件编码模式，再决定是否归一化
- 审查/解释：先输出结构摘要，不要急着改
- 导出/排查问题：先确认运行平台，再确认是否需要 `drawio` CLI

如果用户给的是已有 `.drawio` 文件，第一步默认都是先检查文件，而不是直接改 XML。

如果任务涉及导出、调用 draw.io 可执行文件或安装路径，默认先区分环境：

- `macOS`
- `Windows`
- `Linux`

环境规则见 [platform-environments.md](references/platform-environments.md)。

如果用户说的是"帮我画一个图"，默认你要同时考虑：

- 图种是否选对
- 连线是否会交叉
- 节点是否会遮挡
- 样式是否过于模板化

## 不可跳过的规则

### 1. 不要盲改压缩内容

`.drawio` 的 `<diagram>` 可能是：

- 压缩后的文本内容
- 内联 `<mxGraphModel>`
- 直接写成文本形式的 XML
- 转义后的 XML 文本

官方样例里大多数页都是压缩格式，但也存在直接内联 XML 的文件。不要假设所有 `.drawio` 都能直接用文本补丁修改。

先运行：

```bash
python scripts/drawio_tools.py summary path/to/file.drawio
```

如果不是 `inline_xml`，通常先归一化：

```bash
python scripts/drawio_tools.py normalize path/to/file.drawio --in-place
```

### 2. 修改已有图时，优先局部修补

除非用户明确要求重画，否则：

- 保留现有页面顺序
- 保留 `<diagram id>` 和 `name`
- 尽量保留已有 `mxCell id`
- 只改必要元素、样式、坐标和连接线

不要为了"整理结构"而整体重写整个页面。

### 3. 新建图时，优先输出可编辑的内联 XML

如果是从零创建 `.drawio`，优先写成可读、可补丁的内联 `<mxGraphModel>` 形式，不要主动生成压缩 `<diagram>` 文本。这样后续维护成本更低。

### 4. 多页图必须显式汇报页面影响面

如果改了多页图，在最终答复里说明：

- 修改了哪些 page
- 是否做了归一化
- 是否导出了 PNG

### 5. 需要视觉确认时就导出

以下情况默认应导出 PNG 做校验：

- 布局大改
- 箭头/连线位置调整
- 组框、泳道、时间线、AWS 架构图
- 用户明确提到重叠、错位、溢出、可读性问题

命令：

```bash
bash scripts/convert-drawio-to-png.sh path/to/file.drawio
```

在 macOS 上，优先使用：

```text
/Applications/draw.io.app/Contents/MacOS/draw.io
```

在 Windows 上，优先考虑 Git Bash / MSYS2 风格路径，例如：

```text
/c/Program Files/draw.io/draw.io.exe
/c/Program Files/diagrams.net/draw.io.exe
```

在 Linux 上，优先考虑：

```text
drawio
/usr/bin/drawio
/snap/bin/drawio
/opt/drawio/drawio
```

导出脚本内置了实际的回退策略：

- 先尝试高分辨率 `--scale 3 --border 20`
- 失败后回退到默认比例 `--border 20`
- 每个文件之间 `sleep 6`，降低 Electron 连续崩溃概率

如果要改参数，优先通过环境变量，而不是直接改脚本：

```bash
DRAWIO_EXPORT_SCALE=5 DRAWIO_EXPORT_SLEEP_SECONDS=3 bash scripts/convert-drawio-to-png.sh path/to/file.drawio
```

如果平台识别特殊或安装路径不标准，也通过环境变量覆盖：

```bash
DRAWIO_PLATFORM=windows DRAWIO_BIN="/c/Program Files/draw.io/draw.io.exe" bash scripts/convert-drawio-to-png.sh path/to/file.drawio
```

### 6. 连线质量高于装饰

如果连线交叉、穿框、盖字、乱吸附，那么这张图即使颜色和图标很好看，也是不合格的。

按优先级处理问题：

1. 错连 / 漏连
2. 线段交叉
3. 线穿节点或压标题
4. 节点重叠
5. 风格与美观

### 7. 新建图时必须有意识选择视觉系统

不要默认每次都画成"浅色圆角矩形 + 细灰线 + 蓝色标题"的同一张 AI 图。

除非用户已有设计语言，否则你应当先在脑中选择一种视觉系统，再开始画：

- Blueprint
- Operations Board
- Editorial Minimal
- Analytical Contrast
- Product Narrative

选择规则见 [visual-systems.md](references/visual-systems.md)。

### 7.1 吸收旧 `draw-io` skill 的优点

这个 skill 已经吸收旧 `draw-io` skill 里更强的成品感规则。生成图时，默认还要考虑：

- 透明背景
- 更可读的字号
- 显式字体
- 容器内边距
- 边标签偏移
- 箭头后层
- 删除多余装饰

详细规则见 [presentation-polish.md](references/presentation-polish.md)。

### 8. 交付前默认运行 lint

只要图里存在实际节点和连线，就默认运行：

```bash
python scripts/drawio_tools.py lint path/to/file.drawio
```

默认应修复这些问题后再结束：

- `edge_crossing`
- `edge_through_node`
- 明显的 `node_overlap`

如果出于图种限制保留了告警，最终答复里要明确说明原因。

## 推荐工作流

### 场景 A：修改现有 `.drawio`

1. 运行 `summary` 看页面数量、编码模式和基本统计。
2. 如果页面不是 `inline_xml`，先运行 `normalize`。
3. 如果需要导出或预览，先判断平台。
4. 判断问题是结构问题、连线问题、遮挡问题还是风格问题。
5. 按用户任务只改必要页面。
6. 运行 `lint`。
7. 如果牵涉布局，导出 PNG 检查。
8. 汇报：改了哪些 page、是否归一化、运行平台、lint 结果、是否导出。

### 场景 B：新建 `.drawio`

1. 先从 [official-examples.md](references/official-examples.md) 选择最接近的图种。
2. 从 [visual-systems.md](references/visual-systems.md) 选择一个视觉系统，避免默认同质化风格。
3. 参考 [layout-guidelines.md](references/layout-guidelines.md) 决定布局。
4. 参考 [connector-routing.md](references/connector-routing.md) 先规划通道，再画连线。
5. 参考 [presentation-polish.md](references/presentation-polish.md) 应用字体、背景、标签和容器打磨规则。
6. 如果是 AWS 图，查 [aws-icons.md](references/aws-icons.md) 或用脚本搜索图标。
7. 直接输出可编辑的内联 XML 版本。
8. 运行 `lint`。
9. 如用户需要预览或你需要做可视化自检，先判断平台，再导出 PNG。

### 场景 C：审查或解释图表

1. 先运行 `summary`。
2. 如果需要深入分析某页，用 `dump` 导出对应 page 的 `mxGraphModel`。
3. 如问题集中在连线、遮挡或交叉，运行 `lint` 辅助判断。
4. 先指出结构问题、布局风险、图种误用、连线质量问题、风格同质化问题，再给修改建议。

命令：

```bash
python scripts/drawio_tools.py dump path/to/file.drawio --page 0
python scripts/drawio_tools.py lint path/to/file.drawio
```

## 图种选择规则

按用户目标选择，而不是按你最熟的图种选择：

- 系统边界、云资源、网络与部署：AWS / deployment / architecture
- 业务步骤、审批、流程分支：flowchart / BPMN / activity / workflow
- 对象关系、组件职责：class / component / composite structure
- 时序和交互：sequence
- 状态迁移：state diagram
- 角色与系统能力：use case
- 威胁、攻击路径、信任边界：threat model / DFD / attack tree
- 思维梳理、因果分析、依赖关系：mind map / fishbone / dependency graph / concept map
- 时间节点与阶段演进：timeline

如果不确定，用官方样例清单辅助判断，不要拍脑袋选图。

## 布局与样式原则

详细规则见 [layout-guidelines.md](references/layout-guidelines.md)。执行时重点记住这些：

- 先保证结构正确，再追求美观
- 同级元素对齐，主流程方向保持一致
- 容器内部要留边距，不要把内容贴边
- 连线优先正交线，尽量避免穿字、穿框
- 标签不要悬空，箭头不要盖住标题
- 多页图保持同一套命名、字体和颜色体系

如果图已经正确但仍然"丑"，优先检查这三件事：

1. 是否缺乏留白
2. 是否没有明显视觉层级
3. 是否所有节点都长得一样

样式去同质化规则见 [visual-systems.md](references/visual-systems.md)。
成品感与排版打磨规则见 [presentation-polish.md](references/presentation-polish.md)。

## 连线与遮挡原则

这是这个 skill 的重点约束。

- 线条必须先规划通道，再实际布线
- 主流程边比辅助边更直、更短、更显眼
- 不要接受无意义交叉
- 不要让线从节点主体中穿过
- 不要让线压住标题、标签和图例
- XML 层级上通常应让线在节点下层，标签在边上层

详细规则见 [connector-routing.md](references/connector-routing.md)。

## AWS 专项规则

如果图里有 AWS 元素：

- 优先用 `mxgraph.aws4.*`
- 服务名尽量写正式名称
- 分组边界优先用 AWS Cloud、VPC、Security Group 等 group 图标
- 用户只说"画 AWS 架构图"时，也要先确认是逻辑图、部署图还是数据流图

可以用：

```bash
python scripts/find_aws_icon.py lambda
python scripts/find_aws_icon.py s3
python scripts/find_aws_icon.py vpc
```

## 输出要求

完成任务时，最终答复至少应覆盖这些点：

- 改了或新建了哪个文件
- 影响了哪些页面
- 是否做了归一化
- 运行环境是 `macOS` / `Windows` / `Linux` 中哪一个
- 是否运行了 `lint`
- `lint` 是否还有未消除问题
- 是否做了 PNG 导出或其他验证
- 还有哪些风险或未验证项

如果只是分析/审查，不要假装已经修改文件。

## 常见失败模式

出现以下情况时，要主动纠正：

- 把压缩 `<diagram>` 当普通 XML 直接补丁
- 新建图时无故写成不可读的压缩内容
- 为了小改动而重写整页
- 多页图只改第一页，忽略其他页命名或一致性
- 连接线直接穿过文本或组件
- 为了避免交叉而把边绕成很多无意义拐弯
- 所有图都套用同一套平庸默认风格
- 没有先规划通道就开始随机拉线
- 把 AWS 图标和普通矩形混搭到难以辨识
- 用 `|| true` 吞掉 draw.io 导出失败，再依赖 `$?` 判断成功与否

## 资源导航

- 文件格式和归一化工作流： [file-format.md](references/file-format.md)
- 平台与环境区分： [platform-environments.md](references/platform-environments.md)
- 官方样例清单和适用场景： [official-examples.md](references/official-examples.md)
- 布局与图种规则： [layout-guidelines.md](references/layout-guidelines.md)
- 连线质量与路由规范： [connector-routing.md](references/connector-routing.md)
- 视觉系统与去同质化： [visual-systems.md](references/visual-systems.md)
- 成品感与视觉打磨： [presentation-polish.md](references/presentation-polish.md)
- 最终审查清单： [review-checklist.md](references/review-checklist.md)
- AWS 图标与服务名： [aws-icons.md](references/aws-icons.md)
- `.drawio` 检查/归一化脚本： `scripts/drawio_tools.py`
- AWS 图标检索脚本： `scripts/find_aws_icon.py`
- PNG 导出脚本： `scripts/convert-drawio-to-png.sh`