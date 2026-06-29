**[中文](README_cn.md)** | English

# Claude Code Skills

![Claude Code](https://img.shields.io/badge/Claude_Code-Skills-D97757?style=flat-square&logo=anthropic&logoColor=fff)
![Skills](https://img.shields.io/badge/Skills-32-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A bunch of skills I've built for Claude Code. They handle stuff like research, writing, coding help, language learning, browser automation, and more. Drop them into your skills folder and they just work.

## What's in here

- **32 skills** covering coding, research, writing, teaching, and daily workflows
- Each skill is a standalone folder with a `SKILL.md` — that's all Claude Code needs
- Mix of my own stuff and things I've tweaked from the community

## Quick start

```bash
# clone the repo
git clone https://github.com/wokaka209/Claude-Code-Skills.git

# copy whichever skill you want
cp -r Claude-Code-Skills/python-teacher ~/.claude/skills/
cp -r Claude-Code-Skills/deep-research ~/.claude/skills/

# that's it, restart Claude Code and the skill shows up
```

You can also grab just one skill — no need to clone the whole thing. Just make sure the folder lands in `~/.claude/skills/` and has a `SKILL.md` inside.

## Skills

### Coding & Dev

| Skill | What it does |
|-------|-------------|
| [c-embedded-stm32](c-embedded-stm32/) | STM32 firmware dev — peripherals, RTOS, flash optimization, automotive diagnostics |
| [codebase-onboarding](codebase-onboarding/) | Walks you through an unfamiliar codebase, generates an onboarding guide + CLAUDE.md |
| [karpathy-guidelines](karpathy-guidelines/) | Coding rules inspired by Karpathy — keep it simple, don't over-engineer |
| [git-workflow](git-workflow/) | Branching strategies, commit conventions, conflict resolution patterns |

### Research & Analysis

| Skill | What it does |
|-------|-------------|
| [deep-research](deep-research/) | Multi-source web research with citations — searches, synthesizes, reports |
| [last30days](last30days/) | Finds what people are actually saying about a topic on Reddit, X, YouTube, HN, etc. |
| [council](council/) | Brings in 4 different perspectives to argue through an ambiguous decision |

### Writing & Docs

| Skill | What it does |
|-------|-------------|
| [article-writing](article-writing/) | Long-form content in a specific voice — blog posts, guides, tutorials |
| [doc](doc/) | Create and edit .docx files with tracked changes, comments, formatting |
| [gitreadme](gitreadme/) | Generates bilingual GitHub READMEs (English + Chinese) with badges and clean structure |
| [thesis-creator](thesis-creator/) | Full thesis workflow for Chinese undergrads — topic selection through final draft, with plagiarism reduction |
| [pdf](pdf/) | Extract text/tables, fill forms, merge/split PDFs |

### Teaching & Learning

| Skill | What it does |
|-------|-------------|
| [python-teacher](python-teacher/) | Teaches Python using Feynman method + spaced repetition — you explain it back to prove you get it |
| [git-teacher](git-teacher/) | Same approach but for Git — learn by teaching |
| [investment-teacher](investment-teacher/) | Financial literacy teaching using Feynman method — compound interest, budgeting, investing basics |
| [koucai-teacher](koucai-teacher/) | Public speaking and communication training with spaced review |
| [baoyan-tutoring](baoyan-tutoring/) | Grad school prep guidance |

### Productivity & Tools

| Skill | What it does |
|-------|-------------|
| [agent-browser](agent-browser/) | Browser automation — navigate, fill forms, click stuff, take screenshots, scrape data |
| [playwright](playwright/) | Playwright-based automation with persistent page state |
| [obsidian-cli](obsidian-cli/) | Manage your Obsidian vault from the command line |
| [obsidian-markdown](obsidian-markdown/) | Obsidian-flavored markdown — wikilinks, embeds, callouts, frontmatter |
| [humanizer-zh](humanizer-zh/) | Strips AI-sounding language from Chinese text — makes it read like a person wrote it |
| [strategic-compact](strategic-compact/) | Suggests when to compact context at logical breakpoints instead of random auto-compact |
| [context-budget](context-budget/) | Audits what's eating your context window — agents, skills, MCP servers, rules |

### Setup & Config

| Skill | What it does |
|-------|-------------|
| [configure-ecc](configure-ecc/) | Interactive installer for Everything Claude Code — picks and installs skills/rules |
| [find-skills](find-skills/) | Helps you discover and install skills when you ask "is there a skill for X?" |
| [skill-creator](skill-creator/) | Create, edit, and benchmark skills — run evals, optimize descriptions |
| [hookify-rules](hookify-rules/) | Write hookify rules for automated behaviors |
| [neat-freak](neat-freak/) | End-of-session cleanup — syncs docs and memory against actual code state |

### Creative

| Skill | What it does |
|-------|-------------|
| [matplotlib](matplotlib/) | Publication-quality charts with a clean, colorblind-accessible aesthetic |
| [manim-creat-skill](manim-creat-skill/) | Math animation creation with Manim |
| [professor-synapse](professor-synapse/) | Summon domain experts for specialized help |

## How skills work

Each skill is just a folder with a `SKILL.md` file. That file tells Claude Code what the skill does, when to trigger it, and how to use it. Some skills also have:
- `references/` — extra docs and cheat sheets
- `scripts/` — helper scripts the skill can run
- `agents/` — sub-agent definitions

No build step, no dependencies. Drop it in and go.

## Contributing

Found a bug or want to improve something? Open an issue or PR. Skills are easy to modify — just edit the `SKILL.md` and test it.

## License

MIT
