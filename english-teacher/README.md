**[中文](README_cn.md)** | English

# english-teacher

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=fff)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

English learning skill for developers. Uses Feynman technique + Ebbinghaus spaced repetition to help you read GitHub docs and write technical English.

## Table of Contents

- [What is this](#what-is-this)
- [Getting started](#getting-started)
- [How to use](#how-to-use)
- [Course modules](#course-modules)
- [Spaced repetition](#spaced-repetition)
- [Built with](#built-with)
- [Contributing](#contributing)
- [License](#license)

## What is this

- **Feynman method** — learn by explaining. You read real docs, I check your understanding
- **Spaced repetition** — review at 1h, 1d, 3d, 7d intervals to lock in memory
- **Real-world material** — all examples come from actual GitHub READMEs, not textbook English
- **Scored feedback** — every exercise gets a 1-10 score with specific corrections

## Getting started

Requirements:
- Claude Code CLI
- Basic English (CET-4 level or above)

Install:
```bash
# Copy to your skills directory
cp -r english-teacher ~/.claude/skills/
```

## How to use

Just say any of these:

| Command | What it does |
|---------|--------------|
| `学英语` / `教我英语` | Show progress, start today's lesson |
| `教我 README 词汇` | Learn new topic |
| `看不懂这个 README` | Paste a README, get guided reading |
| `这段英文什么意思` | Reading comprehension practice |
| `复习` | Spaced repetition review |
| `给我出题` | Random exercise |

## Course modules

| Module | Focus |
|--------|-------|
| 01_readme_reading | GitHub README structure, common patterns, long sentences |
| 02_tech_vocabulary | 500 dev高频词, polysemy (branch/commit/merge), abbreviations (PR/CI/CD) |
| 03_tech_writing | Commit messages, PR descriptions, issue templates |
| 04_reading_practice | PyTorch/NumPy/Pandas docs, Stack Overflow |

## Spaced repetition

Based on Ebbinghaus forgetting curve:

| Round | Interval | Method |
|-------|----------|--------|
| 1 | 1 hour | Recite today's vocabulary from memory |
| 2 | 1 day | Write 5 new words + make sentences |
| 3 | 3 days | Read a new README and translate |
| 4 | 7 days | Explain a technical concept in English |

## Built with

- [Claude Code](https://claude.ai/code) — AI coding assistant
- [Feynman Technique](https://en.wikipedia.org/wiki/Feynman_Technique) — learn by teaching
- [Ebbinghaus Forgetting Curve](https://en.wikipedia.org/wiki/Forgetting_curve) — spaced repetition science

## Contributing

Found a bug or want to improve the course? Open an issue or PR.

## License

MIT
