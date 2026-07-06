中文 | **[English](README.md)**

# english-teacher

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=fff)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

给开发者用的英语学习技能。用费曼学习法 + 艾宾浩斯记忆曲线，帮你读懂 GitHub 文档、写好技术英语。

## 目录

- [这是什么](#这是什么)
- [跑起来](#跑起来)
- [怎么用](#怎么用)
- [课程模块](#课程模块)
- [间隔复习](#间隔复习)
- [用到的东西](#用到的东西)
- [参与贡献](#参与贡献)
- [开源协议](#开源协议)

## 这是什么

- **费曼学习法** — 用"教"来学。你读真实文档，我检查你懂没懂
- **间隔复习** — 学完后 1 小时、1 天、3 天、7 天复习，把短期记忆变成长期记忆
- **真实素材** — 所有例句都来自真实的 GitHub README，不是课本英语
- **打分反馈** — 每次练习都有 1-10 分评分 + 具体纠正

## 跑起来

依赖：
- Claude Code CLI
- 英语基础（四级以上）

安装：
```bash
# 复制到你的 skills 目录
cp -r english-teacher ~/.claude/skills/
```

## 怎么用

直接说这些就行：

| 命令 | 效果 |
|------|------|
| `学英语` / `教我英语` | 显示进度，开始今日学习 |
| `教我 README 词汇` | 学习新主题 |
| `看不懂这个 README` | 粘贴 README，手把手带你读 |
| `这段英文什么意思` | 阅读理解练习 |
| `复习` | 间隔复习 |
| `给我出题` | 随机练习 |

## 课程模块

| 模块 | 重点 |
|------|------|
| 01_readme_reading | GitHub README 结构、常见句型、长难句拆解 |
| 02_tech_vocabulary | 500 个开发者高频词、一词多义（branch/commit/merge）、缩写（PR/CI/CD） |
| 03_tech_writing | commit message、PR description、issue 模板 |
| 04_reading_practice | PyTorch/NumPy/Pandas 文档精读、Stack Overflow |

## 间隔复习

基于艾宾浩斯遗忘曲线：

| 轮次 | 间隔 | 方式 |
|------|------|------|
| 1 | 1 小时后 | 不看笔记，口述今日词汇 |
| 2 | 1 天后 | 默写 5 个新词 + 造句 |
| 3 | 3 天后 | 精读新的 README 并翻译 |
| 4 | 7 天后 | 用英语解释一个技术概念 |

## 用到的东西

- [Claude Code](https://claude.ai/code) — AI 编程助手
- [费曼学习法](https://zh.wikipedia.org/wiki/%E8%B2%BB%E6%9B%BC%E6%8A%80%E5%B7%A7) — 用"教"来学
- [艾宾浩斯遗忘曲线](https://zh.wikipedia.org/wiki/%E8%89%BE%E5%AE%BE%E6%B5%A9%E6%96%AF%E9%81%97%E5%BF%98%E6%9B%B2%E7%BA%BF) — 间隔复习科学依据

## 参与贡献

发现 bug 或想改进课程？提 issue 或 PR 都行。

## 开源协议

MIT
