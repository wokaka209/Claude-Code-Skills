---
name: gitreadme
description: Generate bilingual GitHub README files (English + Chinese) with badges, table of contents, and a direct practical tone. Use when the user asks to create a README, write project documentation, generate bilingual docs, update README, or needs GitHub-ready documentation. Also use when setting up a new repo, onboarding docs, or when the user says "写个README", "生成readme", "帮我写文档", "create a readme", or any variation.
---

# GitREADME — Bilingual GitHub README Generator

Generate two README files for any project: `README.md` (English) and `README_cn.md` (Chinese), following a clean, direct, badge-heavy GitHub style.

## Core Style Rules

The tone is **casual, direct, and practical** — like explaining your project to a smart friend, not writing a corporate doc.

**English example**: "throw in text, get audio" (not "input text to obtain audio output")
**Chinese example**: "直接扔文本进去，出来就是语音" (not "将文本输入即可获得语音输出")

**What to avoid**:
- Corporate jargon ("leverage", "utilize", "empower", "赋能", "助力", "一站式")
- Passive voice when active works
- Redundant filler ("In this section, we will discuss...", "本节将介绍...")
- Over-explaining things that code examples already show

## File Structure

Always generate TWO files:
- `README.md` — English version
- `README_cn.md` — Chinese version

Each file starts with a language switcher:
```markdown
<!-- English README -->
**[中文](README_cn.md)** | English

<!-- Chinese README -->
中文 | **[English](README.md)**
```

## README Template

Follow this structure. Adapt section names and content to the project, but keep the ordering and format consistent.

### 1. Language Switcher + Title

```markdown
**[中文](README_cn.md)** | English

# project-name
```

### 2. Badges

Pick badges relevant to the project's tech stack. Always use `flat-square` style with `logo` and `logoColor=fff` where applicable.

Common badge patterns:
```markdown
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=fff)
![Node](https://img.shields.io/badge/Node.js-20-339933?style=flat-square&logo=node.js&logoColor=fff)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=flat-square&logo=typescript&logoColor=fff)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react&logoColor=000)
![PyTorch](https://img.shields.io/badge/PyTorch-2.6-EE4C2C?style=flat-square&logo=pytorch&logoColor=fff)
![CUDA](https://img.shields.io/badge/CUDA-12.4-76B900?style=flat-square&logo=nvidia&logoColor=fff)
![License](https://img.shields.io/badge/License-Apache_2.0-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
```

Choose badges based on what the project actually uses. Don't add irrelevant ones.

### 3. One-liner Description

One sentence, right after badges. What does this project do, in plain language.

English: "TTS workspace using VoxCPM2. Text-to-speech, voice design, voice cloning — 48kHz output."
Chinese: "用 VoxCPM2 做语音合成。支持文本转语音、音色设计、声音克隆，输出 48kHz 高质量音频。"

### 4. Table of Contents

Use Chinese anchor links for the Chinese version. Keep section names short.

English:
```markdown
## Table of Contents
- [What is this](#what-is-this)
- [Getting started](#getting-started)
- [How to use](#how-to-use)
- [Built with](#built-with)
```

Chinese:
```markdown
## 目录
- [这是什么](#这是什么)
- [跑起来](#跑起来)
- [怎么用](#怎么用)
- [用到的东西](#用到的东西)
```

### 5. Main Content Sections

Adapt sections to the project. Common patterns:

**"What is this" / "这是什么"** — 2-4 bullet points of what the project does. Use bold for feature names, em dash for descriptions.

**"Getting started" / "跑起来"** — Prerequisites + install commands + quick test. Code blocks with bash.

**"How to use" / "怎么用"** — Code examples showing different use cases. Each example in its own code block with a bold label.

**"Built with" / "用到的东西"** — Links to dependencies with short descriptions.

### 6. Section Naming Reference

| English | Chinese | Use for |
|---------|---------|---------|
| What is this | 这是什么 | Project overview |
| Getting started | 跑起来 | Setup instructions |
| How to use | 怎么用 / 配音脚本怎么用 | Usage examples |
| Model download | 模型下载 | Large file downloads |
| Configuration | 配置 | Config options |
| API | 接口 | API reference |
| Built with | 用到的东西 | Dependencies |
| Contributing | 参与贡献 | Contribution guide |
| License | 开源协议 | License info |

## Workflow

When the user asks for a README:

1. **Explore the project** — Read key files (package.json, setup.py, pyproject.toml, requirements.txt, existing scripts, CLAUDE.md) to understand what the project does, its tech stack, and how to use it.

2. **Ask clarifying questions** if needed — What's the project about? Any specific sections they want? What language should be primary?

3. **Generate README.md** (English) first.

4. **Generate README_cn.md** (Chinese) — translate naturally, don't literally translate. The Chinese version should read like it was originally written in Chinese.

5. **Verify** — Make sure badges render, anchor links work, code examples are accurate.

## Badge Quick Reference

Format: `![label](https://img.shields.io/badge/TEXT-VERSION-COLOR?style=flat-square&logo=LOGO&logoColor=fff)`

Popular logos: `python`, `node.js`, `typescript`, `react`, `vue`, `rust`, `go`, `docker`, `kubernetes`, `aws`, `pytorch`, `tensorflow`, `nvidia`, `linux`, `github`

Popular colors: Python `3776AB`, Node `339933`, TypeScript `3178C6`, React `61DAFB`, Rust `000`, Go `00ADD8`, Docker `2496ED`, PyTorch `EE4C2C`, CUDA `76B900`, MIT `blue`, Apache `green`
