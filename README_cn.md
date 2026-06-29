中文 | **[English](README.md)**

# Claude Code Skills

![Claude Code](https://img.shields.io/badge/Claude_Code-Skills-D97757?style=flat-square&logo=anthropic&logoColor=fff)
![Skills](https://img.shields.io/badge/Skills-32-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

给 Claude Code 写的一堆技能。搞研究、写东西、写代码、学语言、浏览器自动化什么的都有。扔到技能目录里就能用。

## 有什么

- **32 个技能**，覆盖编码、研究、写作、教学、日常工具
- 每个技能就是一个文件夹，里面放个 `SKILL.md` 就行，Claude Code 就能认出来
- 有些是自己写的，有些是从社区拿过来改过的

## 怎么装

```bash
# 克隆仓库
git clone https://github.com/wokaka209/Claude-Code-Skills.git

# 挑你要的技能复制过去
cp -r Claude-Code-Skills/python-teacher ~/.claude/skills/
cp -r Claude-Code-Skills/deep-research ~/.claude/skills/

# 重启 Claude Code 就能用了
```

不用全部克隆，单个拿也行。只要文件夹在 `~/.claude/skills/` 下面，里面有 `SKILL.md` 就可以。

## 技能一览

### 写代码 & 开发

| 技能 | 干嘛的 |
|------|--------|
| [c-embedded-stm32](c-embedded-stm32/) | STM32 固件开发 — 外设驱动、RTOS、Flash 优化、汽车诊断协议 |
| [codebase-onboarding](codebase-onboarding/) | 帮你快速上手一个不熟的代码库，自动生成入门指南和 CLAUDE.md |
| [karpathy-guidelines](karpathy-guidelines/) | Karpathy 风格的编码准则 — 别搞复杂了，能简单就简单 |
| [git-workflow](git-workflow/) | 分支策略、commit 规范、冲突处理 |

### 研究 & 分析

| 技能 | 干嘛的 |
|------|--------|
| [deep-research](deep-research/) | 多来源深度研究，带引用 — 搜、整合、出报告 |
| [last30days](last30days/) | 看看大家最近在 Reddit、X、YouTube、HN 上怎么说某个话题 |
| [council](council/) | 拉 4 个不同视角来辩论一个拿不准的决定 |

### 写作 & 文档

| 技能 | 干嘛的 |
|------|--------|
| [article-writing](article-writing/) | 按照特定风格写长文 — 博客、教程、指南 |
| [doc](doc/) | 创建和编辑 .docx 文件，支持批注、修改痕迹、格式保留 |
| [gitreadme](gitreadme/) | 生成中英双语 GitHub README，带徽章和清晰结构 |
| [thesis-creator](thesis-creator/) | 本科毕业论文全流程 — 从选题到定稿，带降重和 AIGC 降低 |
| [pdf](pdf/) | 提取文字/表格、填写表单、合并拆分 PDF |

### 教学 & 学习

| 技能 | 干嘛的 |
|------|--------|
| [python-teacher](python-teacher/) | 费曼学习法教 Python + 艾宾浩斯复习 — 你得讲给我听才算学会了 |
| [git-teacher](git-teacher/) | 同样的方法教 Git — 教是最好的学 |
| [investment-teacher](investment-teacher/) | 费曼学习法教投资理财 — 复利、预算、投资入门，整合《小狗钱钱》故事框架，适合零资金新手 |
| [koucai-teacher](koucai-teacher/) | 口才和表达训练，带间隔复习 |
| [baoyan-tutoring](baoyan-tutoring/) | 保研相关指导 |

### 效率 & 工具

| 技能 | 干嘛的 |
|------|--------|
| [agent-browser](agent-browser/) | 浏览器自动化 — 导航、填表、点按钮、截图、爬数据 |
| [playwright](playwright/) | 基于 Playwright 的自动化，页面状态保持 |
| [obsidian-cli](obsidian-cli/) | 命令行管理 Obsidian 笔记库 |
| [obsidian-markdown](obsidian-markdown/) | Obsidian 风格 Markdown — wikilinks、嵌入、callout、frontmatter |
| [humanizer-zh](humanizer-zh/) | 去掉中文里的 AI 味，读起来像人写的 |
| [strategic-compact](strategic-compact/) | 在合适的时机压缩上下文，而不是随机自动压缩 |
| [context-budget](context-budget/) | 审计上下文窗口的占用情况 — agent、技能、MCP 服务器、规则 |

### 配置 & 安装

| 技能 | 干嘛的 |
|------|--------|
| [configure-ecc](configure-ecc/) | Everything Claude Code 交互式安装器 — 选技能、装规则 |
| [find-skills](find-skills/) | 问"有没有 X 的技能"的时候帮你找和装 |
| [skill-creator](skill-creator/) | 创建、编辑、测试技能 — 跑评估、优化描述 |
| [hookify-rules](hookify-rules/) | 写 hookify 规则实现自动化行为 |
| [neat-freak](neat-freak/) | 会话结束前的文档和记忆同步清理 |

### 创意

| 技能 | 干嘛的 |
|------|--------|
| [matplotlib](matplotlib/) | 出版级质量的图表，配色对色盲友好 |
| [manim-creat-skill](manim-creat-skill/) | 用 Manim 做数学动画 |
| [professor-synapse](professor-synapse/) | 召唤领域专家来帮忙 |

## 技能怎么运作的

每个技能就是一个文件夹，核心是里面的 `SKILL.md`。这个文件告诉 Claude Code 这个技能干什么、什么时候触发、怎么用。有些技能还有：
- `references/` — 补充文档和速查表
- `scripts/` — 辅助脚本
- `agents/` — 子 agent 定义

不用编译，不用装依赖。扔进去就能跑。

## 参与贡献

发现问题或者想改进？直接提 issue 或者 PR。技能改起来很简单 — 编辑 `SKILL.md` 然后测试一下就行。

## 开源协议

MIT
