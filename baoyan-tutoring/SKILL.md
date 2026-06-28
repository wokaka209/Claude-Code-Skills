---
name: baoyan-tutoring
description: Baoyan (保研) summer camp information search, verification, and Excel aggregation skill for Chinese university automation/control/AI/electronics programs. This skill should be used when verifying or updating summer camp deadlines and status across 70+ universities, querying a specific university's camp deadline, batch-verifying camp notifications, or generating/updating the camp summary Excel. Covers the full workflow: scope confirmation, three-tier source strategy, parallel agent orchestration, Excel update via openpyxl, and versioned output delivery. Trigger terms include 保研夏令营, 夏令营截止, 推免, 交流营, 研学营, 实验室开放日.
agent_created: true
---

# Baoyan Tutoring

## Overview

Standardize the search, verification, aggregation, and Excel update workflow for baoyan (保研) summer camp information. Core capability: verify summer camp notifications for 70+ universities across automation, control science, AI, electronics, and related disciplines using a three-tier source strategy (aggregation platforms → official websites → WeChat reposts), update results into a master Excel sheet following a unified column schema, and deliver versioned outputs.

Applicable disciplines: automation, control science and engineering, artificial intelligence, electronic information, electrical engineering, intelligent manufacturing, and closely related fields.

## When to Use

Trigger this skill when encountering any of the following:

- Verifying or updating baoyan summer camp deadlines and status (full or partial university list)
- Querying a specific university's camp deadline, activity schedule, or application status
- Batch-verifying camp notifications across multiple universities
- Generating or updating the camp summary Excel (`2027届自动化专业保研夏令营信息汇总.xlsx`)
- Searching for terms like 保研夏令营, 推免, 交流营, 研学营, 实验室开放日, 科学营

## Workflow

### Step 1: Confirm Scope

Read the existing master Excel to confirm the current university list and last verification date. The master file resides in the most recent `outputs/YYYY-MM-DD_camp_*_update/` subdirectory.

Clarify these parameters before proceeding:

- **Verification date**: Default to today; used to populate column K.
- **Discipline scope**: Default to automation/control/AI/electronics/electrical/intelligent manufacturing; exclude unrelated fields (pure CS software, materials, chemistry).
- **University list**: Default to all rows in the master sheet; narrow to a subset if specified (e.g., "control engineering top schools only").
- **Verification depth**: Deadline only, or include activity schedule, application requirements, and registration links.

### Step 2: Apply Source Strategy

Execute a three-tier progressive search. For the full source list, official website directory, and keyword templates, see `references/info_sources.md`.

1. **Aggregation platforms** — Quickly locate candidates via baoyanxinxi.cn, Sohu/WeChat summary articles. Convert countdown formats to absolute dates (mark with "约" and note "以官网为准"). All aggregation-sourced data requires official confirmation.
2. **Official websites** — Confirm via the target school/department's official notice page. Link priority: department notice page > graduate admission portal > graduate school notices. Never use a university homepage as the notice link.
3. **WeChat reposts** — When official sites have not published but reposts exist, record provisionally with a "以官网为准" note.

**Naming variance alert**: Universities use different terms for "summer camp" (学术交流营, 研学营, 实验室开放日, 科学营, 控制之旅, etc.). Search with the correct term per school to avoid missing notifications. See `references/school_naming_conventions.md` for the full mapping table.

### Step 3: Orchestrate Parallel Search

For batch verification (≥10 universities), use TeamCreate with multiple Explore agents to parallelize. For small batches (≤5), run sequential WebSearch + WebFetch directly.

**Batch orchestration procedure:**

1. Create a team: `TeamCreate(team_name="camp-verify-YYYYMMDD")`.
2. Partition the university list into batches of 20-25 per Explore agent. Suggested partitioning:
   - Urgent batch: Camps closing within 3 days (highest priority)
   - 985 batch: 985 universities pending publication
   - 211 / Double First-Class batch: Remaining universities
3. Brief each agent with:
   - Assigned university list (include Excel row numbers for backfill)
   - Search keyword templates: `"{学校} {学院} 2026 夏令营"`, `"{学校} {学院} 推免 2027"`
   - Required structured output: `{row, school, department, deadline, status, notes, notice_url, notice_desc, can_apply}`
   - The three-tier source strategy and naming variance alert
4. After all agents complete, integrate results and prepare the Excel update dictionary.

**Single-university search procedure:**

1. WebSearch: `"{学校} {目标学院} 2026 夏令营 报名"`
2. If an official notice is found → WebFetch to extract deadline, activity dates, requirements, registration link.
3. If no official hit → WebSearch repost sources, WebFetch to confirm.
4. If still no hit → Check the department's notice page for the latest entries; record "仍未见通知" with the latest entry content as evidence.
5. Return structured result.

### Step 4: Update Excel

Update the master Excel sheet following the unified column schema. For the complete column mapping, deadline format rules, status determination rules, and technical notes, see `references/excel_schema.md`. Use `scripts/update_camp_excel.py` as the update template.

**Key column mapping** (data starts at row 4; row 2 is the methodology note):

| Col | Field | Purpose |
|-----|-------|---------|
| E(5) | Deadline | Multi-department format: `学院名~YYYY-MM-DD HH:MM` |
| F(6) | Status | 已开通 / 已截止 / 仍未见 / 每日跟踪 |
| G(7) | Notes | Activity dates, requirements, naming variance, relevance |
| H(8) | Notice URL | Department-level official link (never homepage) |
| I(9) | Notice desc | One-line summary of publication and deadline |
| J(10) | Can apply | `可报名：...` / `已截止` / `None` (clear) |
| K(11) | Verify date | `YYYY-MM-DD` |

**Update procedure:**

1. Copy the previous version: `shutil.copy2(SRC, DST)`.
2. Load with `openpyxl.load_workbook(DST, data_only=False)`.
3. Build the `updates` dict: `{row: {col: value}}`, where `None` clears the cell.
4. Iterate and write; refresh row 2 methodology note (include verification date, university count, key changes summary).
5. Save with `wb.save(DST)`.

**Runtime environment:** Use managed Python 3.13.12 with `PYTHONUTF8=1` to avoid Chinese encoding errors. Install openpyxl into the project `.pylibs` directory and reference via `PYTHONPATH`. If the file is open in Excel during save, a `PermissionError` will occur — close Excel first or save as `_v2.xlsx`.

### Step 5: Deliver Output

Write versioned outputs to a date-stamped directory:

```
outputs/YYYY-MM-DD_camp_status_update/
├── 2027届自动化专业保研夏令营信息汇总.xlsx   # Updated master
└── update_MMDD.py                              # Reproducible update script
```

Include a verification log (optional `.md`) summarizing:

- Verification date, total universities, status breakdown
- Key changes categorized: new notices, deadline extensions, closed, urgent (closing tomorrow), still unseen
- Output file path

**Predictive note**: Most universities publish 2027-cycle notices on the same schedule as their 2025-cycle (2026-entry) notices. Use this to predict publication windows for schools that have not yet released. March-June: C9/top 985密集发布. Late June-July: 211/Double First-Class release. Mid-late July: Some schools (e.g., HUST AIA) issue online briefings first, with camp registration notices following later.

## Resources

### scripts/
- `update_camp_excel.py` — Excel master batch update template. Based on openpyxl with column mapping comments, `updates` dict structure, and methodology note refresh logic. Copy and modify the `updates` dict for each new verification round.

### references/
- `school_naming_conventions.md` — University summer camp naming variance table. Lists each school's variant term for "summer camp" (学术交流营/研学营/实验室开放日/科学营/控制之旅 etc.), special mechanisms (e.g., USTC advisor recommendation, Tsinghua canceled camp assessment), and publication timing patterns by tier.
- `info_sources.md` — Three-tier source strategy details: aggregation platform directory, official department website links for 25+ key universities, WeChat repost sources, search keyword templates, and countdown-to-absolute-date conversion method.
- `excel_schema.md` — Complete Excel schema: row layout, full column mapping, deadline format rules, status determination criteria, `updates` dict structure, row 2 methodology note template, and openpyxl technical caveats.

### assets/
No asset files required. This skill produces Excel/Markdown outputs via scripts rather than template filling.
