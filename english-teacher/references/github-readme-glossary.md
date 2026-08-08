# GitHub / 开源常见技术词汇表

> 按主题分组，优先级从高到低排列。每个词附带：含义、常见用法、例句。

---

## Git / GitHub 核心

| 词汇 | 含义 | 例句 |
|------|------|------|
| repository (repo) | 代码仓库 | "Clone the repository to your local machine." |
| commit | 提交（一次代码变更记录） | "Make a commit with a descriptive message." |
| branch | 分支 | "Create a new feature branch." |
| merge | 合并 | "Merge the pull request into main." |
| pull request (PR) | 拉取请求（代码审查机制） | "Open a pull request for review." |
| fork | 复刻（复制别人的仓库到自己账号） | "Fork the repo and submit a PR." |
| clone | 克隆（下载仓库到本地） | "Clone the repo using HTTPS." |
| push | 推送（上传本地代码到远程） | "Push your changes to the remote." |
| pull | 拉取（下载远程代码到本地） | "Pull the latest changes from main." |
| issue | 问题/议题 | "Open an issue if you find a bug." |
| release | 发布版本 | "Check the latest release for new features." |
| tag | 标签（版本标记） | "This feature was added in tag v2.0." |
| README | 项目说明文件 | "See the README for installation instructions." |
| LICENSE | 许可证 | "This project is under the MIT license." |
| .gitignore | Git 忽略文件配置 | "Add __pycache__ to your .gitignore." |

## 项目结构

| 词汇 | 含义 | 例句 |
|------|------|------|
| dependency | 依赖 | "Install all dependencies with pip." |
| package | 包/软件包 | "This package is available on PyPI." |
| module | 模块 | "Import the module with `import torch`." |
| source (src) | 源代码 | "The source code is in the src/ directory." |
| build | 构建/编译 | "Run the build command to compile." |
| binary | 二进制文件 | "Download the binary for your OS." |
| configuration (config) | 配置 | "Edit the config file to change settings." |
| environment (env) | 环境 | "Set up a virtual environment." |
| scaffold | 脚手架/项目模板 | "Use the CLI to scaffold a new project." |
| boilerplate | 模板代码 | "This template provides boilerplate for React." |
| entry point | 入口点 | "The entry point is main.py." |

## 开发流程

| 词汇 | 含义 | 例句 |
|------|------|------|
| feature | 功能/特性 | "This release includes 3 new features." |
| bug fix | 修复 bug | "Version 2.1 includes several bug fixes." |
| deprecate | 废弃/弃用 | "This function is deprecated. Use `new_func()` instead." |
| refactor | 重构 | "We need to refactor this module for better readability." |
| backward compatible | 向后兼容 | "The API is backward compatible with v1.x." |
| breaking change | 破坏性变更 | "This is a breaking change. See the migration guide." |
| migration | 迁移 | "Follow the migration guide to upgrade from v1 to v2." |
| changelog | 变更日志 | "See the CHANGELOG for a list of all changes." |
| contribution | 贡献 | "See CONTRIBUTING.md for how to contribute." |
| maintain | 维护 | "This project is actively maintained." |
| upstream | 上游（原始仓库） | "Sync with the upstream repository." |
| downstream | 下游（依赖此项目的项目） | "This change may affect downstream packages." |

## 质量与测试

| 词汇 | 含义 | 例句 |
|------|------|------|
| test suite | 测试套件 | "Run the test suite with `pytest`." |
| unit test | 单元测试 | "Write unit tests for each function." |
| integration test | 集成测试 | "Integration tests verify end-to-end behavior." |
| coverage | 覆盖率 | "The test coverage is 95%." |
| CI/CD | 持续集成/持续部署 | "CI/CD is configured with GitHub Actions." |
| lint | 代码风格检查 | "Run the linter before committing." |
| format | 格式化 | "Format your code with Black." |
| code review | 代码审查 | "All PRs require code review before merging." |
| benchmark | 基准测试 | "Run the benchmark to measure performance." |
| regression | 回退/回归（新版本引入的 bug） | "This bug is a regression from v2.0." |

## 安装与使用

| 词汇 | 含义 | 例句 |
|------|------|------|
| install | 安装 | "Install with `pip install torch`." |
| setup | 设置/配置 | "Follow the setup guide in the docs." |
| quickstart | 快速入门 | "See the quickstart section below." |
| prerequisites | 前置条件 | "Prerequisites: Python 3.9+, CUDA 11.8." |
| compatible | 兼容 | "Compatible with Python 3.8-3.12." |
| platform | 平台 | "This package supports Linux and macOS platforms." |
| stable | 稳定版 | "Use the stable release for production." |
| nightly | 每夜构建版（实验性） | "Try the nightly build for the latest features." |
| alpha / beta | 内测/公测版 | "This feature is in beta. Use at your own risk." |
| LTS | 长期支持版 | "Ubuntu 22.04 is an LTS release." |
| latest | 最新版 | "Check the latest documentation." |
| deprecated | 已弃用 | "This API is deprecated since v2.0." |

## 常见缩写

| 缩写 | 全称 | 含义 |
|------|------|------|
| PR | Pull Request | 拉取请求 |
| CI | Continuous Integration | 持续集成 |
| CD | Continuous Deployment/Delivery | 持续部署/交付 |
| API | Application Programming Interface | 应用程序接口 |
| SDK | Software Development Kit | 软件开发工具包 |
| CLI | Command Line Interface | 命令行界面 |
| GUI | Graphical User Interface | 图形用户界面 |
| LTS | Long Term Support | 长期支持 |
| EOL | End of Life | 生命周期结束 |
| OSS | Open Source Software | 开源软件 |
| WIP | Work In Progress | 进行中 |
| TL;DR | Too Long; Didn't Read | 太长不看（摘要） |
| IMO/IMHO | In My (Humble) Opinion | 在我（谦虚地）看来 |
| FYI | For Your Information | 供你参考 |
| RTFM | Read The F**king Manual | 去读文档（粗鲁） |
| YMMV | Your Mileage May Vary | 你的体验可能不同 |

## README 常见句型

| 句型 | 含义 | 使用场景 |
|------|------|---------|
| "This project aims to..." | 本项目旨在... | 项目简介 |
| "Feel free to open an issue." | 欢迎提交 issue。 | 贡献指南 |
| "PRs are welcome!" | 欢迎提交 PR！ | 贡献指南 |
| "See the documentation for more details." | 详见文档。 | 指向详细文档 |
| "Getting started" | 入门/开始使用 | 安装章节标题 |
| "Built with" | 使用...构建 | 技术栈说明 |
| "Powered by" | 由...驱动 | 技术栈说明 |
| "Batteries included." | 开箱即用/自带电池。 | 功能丰富 |
| "Production-ready." | 生产就绪/可用于生产环境。 | 稳定性说明 |
| "Lightweight / Zero-dependency" | 轻量/零依赖 | 特性说明 |
| "Drop-in replacement" | 直接替换/无缝替换 | 兼容性说明 |
| "Out of the box" | 开箱即用 | 易用性说明 |
| "Your mileage may vary." | 你的体验可能不同。 | 免责声明 |
| "Contributions are welcome!" | 欢迎贡献！ | 社区参与 |
| "Star this repo if you find it useful!" | 觉得有用就点个 Star！ | 推广 |

## 一词多义（开发者语境）

| 词汇 | 开发者含义 | 日常含义 |
|------|-----------|---------|
| commit | 提交代码 | 承诺 |
| branch | 分支 | 树枝 |
| merge | 合并代码 | 融合 |
| fork | 复刻仓库 | 叉子 |
| pull | 拉取代码 | 拉 |
| push | 推送代码 | 推 |
| clone | 克隆仓库 | 克隆/复制 |
| issue | 议题/问题 | 问题/期刊 |
| release | 发布版本 | 释放 |
| master | 主分支 | 主人/大师 |
| main | 主分支（新命名） | 主要的 |
| origin | 远程仓库默认名 | 起源 |
| head | 当前分支指针 | 头部 |
| tag | 版本标签 | 标签 |
| squash | 压缩提交 | 南瓜/压扁 |
| rebase | 变基 | 重新定基 |
| stash | 暂存更改 | 藏匿 |
| blame | 查看谁修改的 | 责备 |
| cherry-pick | 摘取提交 | 挑选 |
| hook | 钩子（触发器） | 钩子 |
| unique | 独特的（≠唯一） | 独特的 |
| static | 静态的（与dynamic相对） | 静态 |
| scratch | 划痕/起跑线 | 从零开始 |
| lag | 延迟 | 零延迟 |
| overhead | 额外开销 | 最小开销 |
| arbitrarily | 任意地 | 任意改变 |
