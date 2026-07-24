# drawio-skill

一个面向 draw.io / diagrams.net 的完整技能包，覆盖：

- `.drawio` 新建与编辑
- 压缩页、内联 XML 页、多页文件的检查和归一化
- PNG 导出
- AWS 图标检索
- 官方样例选型

## 目录结构

```text
drawio-skill/
├── SKILL.md
├── README.md
├── evals/
│   └── evals.json
├── references/
│   ├── aws-icons.md
│   ├── connector-routing.md
│   ├── file-format.md
│   ├── layout-guidelines.md
│   ├── official-examples.md
│   ├── platform-environments.md
│   ├── presentation-polish.md
│   ├── review-checklist.md
│   └── visual-systems.md
└── scripts/
    ├── convert-drawio-to-png.sh
    ├── drawio_tools.py
    └── find_aws_icon.py
```

## 常用命令

检查 `.drawio`：

```bash
python scripts/drawio_tools.py summary path/to/file.drawio
```

导出某一页的 XML：

```bash
python scripts/drawio_tools.py dump path/to/file.drawio --page 0
```

把压缩页归一化为内联 XML：

```bash
python scripts/drawio_tools.py normalize path/to/file.drawio --in-place
```

做质量检查：

```bash
python scripts/drawio_tools.py lint path/to/file.drawio
python scripts/drawio_tools.py lint path/to/file.drawio --page 0 --fail-on warn
```

导出 PNG：

```bash
bash scripts/convert-drawio-to-png.sh path/to/file.drawio
bash scripts/convert-drawio-to-png.sh
```

说明：

- 脚本会自动区分 `macOS` / `Windows` / `Linux`
- macOS 下优先走 `/Applications/draw.io.app/Contents/MacOS/draw.io`
- Windows 下优先找 Git Bash / MSYS2 可访问的 `draw.io.exe`
- Linux 下优先找 PATH 中的 `drawio` 或常见安装路径
- 默认先尝试 `--scale 3 --border 20`，失败后回退到默认比例
- 可用环境变量覆盖：`DRAWIO_PLATFORM`、`DRAWIO_BIN`、`DRAWIO_EXPORT_SCALE`、`DRAWIO_EXPORT_BORDER`、`DRAWIO_EXPORT_SLEEP_SECONDS`

环境规则见 [platform-environments.md](/Users/moka/projects/work/project/moka-api-custom/hengli/moka-api-custom/drawio-skill/drawio-skill/references/platform-environments.md)。

## 当前 skill 的增强重点

- 对压缩页、多页、内联 XML 页做统一处理
- 对连线交叉、穿节点、节点重叠做 `lint`
- 对透明背景、默认字体、边标签 offset 做审美 `warn`
- 对视觉系统和去同质化提供明确约束
- 把"先规划通道再布线"写成默认流程
- 吸收旧 `draw-io` skill 里更好的成品感规则，如透明背景、显式字体、字号、容器边距和边标签偏移

搜索 AWS 图标：

```bash
python scripts/find_aws_icon.py ecs
python scripts/find_aws_icon.py route53
```