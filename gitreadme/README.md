# gitreadme

Claude Code skill for generating bilingual GitHub README files (English + Chinese).

## What it does

- Generates `README.md` (English) + `README_cn.md` (Chinese) with language switcher
- Auto-detects project tech stack and adds relevant badges (flat-square style)
- Casual, direct tone — no corporate jargon
- Table of contents with Chinese anchor links

## Install

Copy `SKILL.md` to your Claude Code skills directory:

```bash
# User-level (available in all projects)
cp SKILL.md ~/.claude/skills/gitreadme/SKILL.md

# Project-level (project only)
cp SKILL.md .claude/skills/gitreadme/SKILL.md
```

## Usage

Just ask Claude to create a README:

- "帮我写个 README"
- "create a readme for this project"
- "生成双语文档"

Claude will read your project files, detect the tech stack, and generate both `README.md` and `README_cn.md`.
