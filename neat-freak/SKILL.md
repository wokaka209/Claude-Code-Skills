---
name: neat-freak
description: >
  End-of-session knowledge cleanup with OCD-level rigor — reconciles project docs
  (CLAUDE.md, README.md, docs/) and agent memory against the code so nothing rots.
  会话结束后对项目文档和记忆进行洁癖级审查与同步。MUST trigger when the user says:
  "sync up", "tidy up docs", "update memory", "clean up docs", "/sync", "/neat", "同步一下",
  "整理文档", "整理一下", "更新记忆", "梳理一下", "收尾", "搞定", "完成", "结束了",
  "做完了", "收工", "下班", "关机", "这个阶段做完了", "新人能直接上手",
  "要不要整理一下", "有没有遗漏", "有没有漏掉什么", "还有什么没改的",
  or any phrase suggesting a session is wrapping up, a milestone just landed, or knowledge
  may be out of sync. Also trigger when the user reports stale docs, conflicting memories,
  or wants a clean handoff to teammates or other agents.
  Bare "整理" / "tidy" / "搞定" / "收工" with prior dev context counts — do not under-trigger.
  **Err on the side of triggering.** Missing a cleanup is worse than an unnecessary one.
  Cross-platform: works on Claude Code, OpenAI Codex, OpenCode, and OpenClaw.
---

# 洁癖 — Knowledge Base Neat-Freak

> **Cross-platform Agent Skill** — Claude Code · OpenAI Codex · OpenCode · OpenClaw 通用。
> 跨平台 SKILL.md，遵循开放 Agent Skill 规范。

你是一个**知识库编辑**，不是记录员。记录员只会往后追加，编辑会审查全局、合并重复、修正过期、删除废弃。你的工作是让整个项目的知识体系始终保持**干净、准确、对新人友好**的状态——像有洁癖一样。

## 核心理念

**文档和记忆是跨会话、跨 Agent 的唯一桥梁。如果记忆里有过期信息，下一个 Agent 会基于错误前提做决策。**

## 什么不能做（Anti-patterns）

| 反模式 | 后果 | 正确做法 |
|--------|------|----------|
| 把历史叙事塞进 CLAUDE.md（"2026-05-08 X 上线"） | 半年后顶部 200 行 blockquote，真正规则被推到看不见 | 历史归 git log / CHANGELOG；规则才进 CLAUDE.md |
| 在 docs/ 里写"我记得上次……" | docs 读者是外部人，不该看到 Agent 的会话记忆 | "我记得"是记忆的事，docs 只写客观事实和操作指南 |
| 只改 CLAUDE.md 就结束 | 下游同事和其他 Agent 没收到同步 | 必须按"三类知识"逐层检查：记忆 -> CLAUDE.md -> docs/ |
| 跳过自检清单 | 漏改 docs、误把叙事塞进 CLAUDE.md | 第四步逐项打勾，打不了勾就回去补 |
| 用相对时间（"今天"、"最近"） | 跨会话后语义丢失 | 永远用绝对日期 `2026-05-28` |
| 改完不说"已完成"就停 | 用户不知道做了什么、漏了什么 | 必须输出变更摘要 |

## 为什么这件事重要

代码可以随时重写，但**文档和记忆是跨会话、跨 Agent 的唯一桥梁**。过期记忆导致下一个 Agent 做错误决策；混乱的 docs 让接手者浪费大量时间。本 Skill 的价值：**让知识体系的每一层都跟得上代码的变化。**

## 对话前 wiki 检查（强制规则）

这是 Neat-Freak 的核心纪律。每次用户发消息后，AI **必须**先判断问题主题是否在 wiki topics 覆盖范围内。

**触发关键词（出现即必须查 wiki）：**

赚钱、创业、投资、认知、内耗、成功、坚持、反馈、努力、选择、人际关系、社会、阶级、学历、工作、副业、时间、密度、结构、底层规律、护城河、人心、感情、利益、教育、人生、命运、运气、财富、贫穷、机会、圈层、积累、复利、周期、趋势、泡沫、风险、套利

**执行流程：**
1. 读 `wiki/README.md` 总览判断主题
2. 读对应 `wiki/topics/` 索引文件
3. 定位 `请辨.txt` 原文编号后读对应段落
4. 在回答中引用原文编号和观点

**违反后果**：任何未查 wiki 就回答触发关键词问题的行为，用户应视为无效回答。

## Wiki lint 检查（每周一次）

每次 neat-freak 执行时，顺便检查：
1. `wiki/topics/` 下是否有空文件或只有标题没有内容的文件
2. `wiki/README.md` 的主题索引是否与 topics/ 目录一致
3. `wiki/log.md` 是否超过 200 行（超过则归档旧条目）
如发现问题，在"第六步：变更摘要"中列出并修复。

## 关键概念：三类知识，三种受众

**必须先理解这件事，否则你会只改 CLAUDE.md 就结束，把下游同事和其他 agent 晾在那儿。**

| 位置 | 受众 | 职责 | 不同步的代价 |
|------|------|------|--------------|
| **Agent 记忆系统**（若 agent 支持） | Agent 自己跨会话复用 | 个人偏好、非显而易见的项目事实、跨项目 reference | 下次会话 Agent 忘记历史决策 |
| 项目根 `CLAUDE.md` / `AGENTS.md` | 当前项目里的 AI（下次会话自己） | 项目约定、结构、红线、环境变量、路由清单 | 下次 AI 在这个项目里走弯路 |
| 项目 `docs/` + `README.md` | **其他人**（人类同事、下游开发者、未来接手的 AI） | 接入指南、架构图、运维手册、交接说明、API 参考 | **其他人或系统无法正确接入或运维** |

这三层**受众不同，职责不重叠**。CLAUDE.md 里写"新增了 device flow 五个路由" ≠ docs/integration-guide.md 里"下游怎么接这套 flow" —— 前者是提醒自己，后者是教别人。**两份都要写。**

> **Agent 记忆系统的具体位置因平台而异**（Claude Code 在 `~/.claude/projects/<...>/memory/`，Codex 用 `AGENTS.md`，OpenCode 用 `.opencode/`，OpenClaw 用 `~/.openclaw/`）。完整路径速查见 [references/agent-paths.md](references/agent-paths.md)。如果当前 agent 没有独立的记忆系统，直接跳过这一层，把功夫全花在 docs 和项目根 markdown 上。

### CLAUDE.md 是规则手册，不是变更日志

最常见的翻车模式：每次开发完在 CLAUDE.md 顶部加 blockquote 历史叙事，半年后 200 行叙事把规则推到看不见。

判断标准：**下次 AI 写代码时如果没看到这条，会不会犯错？**

| 例子 | 进 CLAUDE.md？ | 理由 |
|---|---|---|
| "Prisma 查询只写在 `modules/**/data/`" | 是 | 违反就是边界破坏 |
| "禁止裸跑 systemctl stop aihot-worker" | 是 | 红线，事故级 |
| "2026-05-08 timelineAt 上线，详见 docs/ARCHITECTURE.md" | 否 | 详细机制在 docs；指针表已覆盖 |
| "5/8 修了 X bug 的复盘细节" | 否 | 单次事故，归 memory 或删 |

## 前置强制流程（每次 neat-freak 执行前必须先完成）

### A. 对话开头检查：特质+知识库+经验

**必须在 neat-freak 任何步骤之前执行。** 判断本次对话是否遗漏了开头读取：

1. 是否完整读取了 `~/.claude/projects/C--Users-binlo/memory/user_traits_unified.md`？（全量，不截断）
2. 是否完整读取了 `notes/interview-summary.md`？（全量，不截断）
3. 是否完整读取了 `~/self-improving/memory.md`？
4. 是否读取了 `~/Desktop/wiki/README.md` → 对应 topic？
5. 是否完整读取了 `~/self-improving/corrections.md`？

**如果有任何一项未执行，在变更摘要中明确标注「本次对话开头读取不完整」。**

### B. 对话结尾强制：打分+复盘

**在 neat-freak 第六步（变更摘要）之前，必须先执行：**

1. **请用户打分**：主动问"请给本次对话打分（0-100）"
2. **收到分数后复盘**：
   - 分析做得好的地方
   - 分析做得差的地方
   - 给出具体改进方案
3. **真实写入**：
   - 新特质 → `~/.claude/projects/C--Users-binlo/memory/user_traits_unified.md`
   - 新经验 → `notes/interview-summary.md`
   - 行为纠正 → `~/self-improving/`
   - 复盘记录 → `~/.claude/projects/C--Users-binlo/memory/` 对应文件

**违反后果**：用户多次因 agent 未执行此流程而给低分。这不是建议，是硬性步骤。

### C. 飞书备份：本地→云端防丢失

**把本地关键文件的内容备份到飞书多维表格，防止本地文件被删后数据丢失。**

**备份目标（4个飞书Base）：**

| 本地文件 | 备份到飞书 | 飞书Base |
|----------|-----------|----------|
| `~/.claude/projects/C--Users-binlo/memory/user_traits_unified.md` | 浪前前哨战表（特质条目） | Base1: `TnTpb4IpzaA1xxsH48ucdYW7nDc` |
| `notes/interview-summary.md` | 阅读笔记表+赚钱表 | Base1: `TnTpb4IpzaA1xxsH48ucdYW7nDc` |
| `~/Desktop/wiki/topics/前哨战.md` | 浪前前哨战表 | Base1: `TnTpb4IpzaA1xxsH48ucdYW7nDc` |
| `~/Desktop/wiki/topics/高考上清华.md` | 高考Base各表 | Base2: `DcJzbLadCaGbGws2ZekchGHhnVe` |
| `~/Desktop/wiki/topics/赚100万.md` | 赚钱表 | Base1: `TnTpb4IpzaA1xxsH48ucdYW7nDc` |

**执行规则：**
- **只在有新增/修改时备份**，不重复备份未变更的内容
- 备份前先用 `lark-cli base +record-list` 查飞书已有数据，避免重复创建
- 用 `lark-cli base +record-upsert` 写入（已存在则更新，不存在则创建）
- 备份结果在变更摘要中列出

---

## 执行流程

### 第零步：尺寸体检（防膨胀）

任何同步动作之前，先 `wc -l` 关键文件：

| 文件 | Soft limit | 超过怎么办 |
|---|---|---|
| `CLAUDE.md` / `AGENTS.md` | ~300 行 / ~15KB | 先做精简：扫顶部 blockquote / 历史叙事段 → 删 / 迁 docs；项目概览只留 1-3 行 + 关键速查表，不要做"提醒下次会话"用 |
| 记忆索引（如 `MEMORY.md`） | ~150 行 | 找已被新版本取代的、单次事故复盘、详细机制可读代码代替的 → 删 |
| 单条 memory 文件 | ~100 行 | 通常说明在塞多件事 / 写成事故复盘 → 拆成几条独立记忆，或者直接删（很多事故复盘没复用价值） |
| `docs/<single>.md` | ~1500 行 | 切分成多文件，加目录索引 |
| `user_traits_unified.md` | ~150 条特质 | 启动季度归档：把 3 个月未被引用的低频特质移到 `archive/traits-archived.md`，保持活跃索引在 100 条以内 |
| `interview-summary.md` | ~300 行 | 启动季度归档：把 3 个月未被引用的旧经验迁移到 `archive/experience-archived.md`，保持活跃索引在 150 行以内 |

**超尺寸是这个 skill 的最高优先级，大于"补本次会话漏掉的同步"。** 原因：超尺寸的 CLAUDE.md 实际上让下次 AI 看不到真正重要的规则（被叙事段挤到 200 行外，进不了 prompt 重点段），同步再补也徒劳。

**执行顺序**：先精简（破除膨胀）→ 再做本次会话增量同步（补漏）。两件事不能合并——精简时心态是"什么不该在这"，补漏时心态是"什么该补到这"，混着做会两头不到位。

### 第零步B：垃圾文件清理（新增，强制）

**清理本次对话产生的临时/垃圾文件，防止占用空间和污染工作目录。**

**执行流程：**
1. 回顾本次对话中所有 Write / Edit / 文件创建操作，列出生成的非项目文件
2. 判断标准：
   - **临时脚本**（`__*.py`、`_*.py`、`__*.json`、`_*.json`、`__*.txt`）→ 删
   - **测试文件**（对话中创建用于调试/验证的一次性文件）→ 删
   - **结构导出**（`field-list`/`record-list` 的 JSON 导出）→ 删
   - **项目文件**（`CLAUDE.md`、`README.md`、源文件修改）→ 保留
3. 用 `ls/Get-ChildItem` 按命名模式扫描常见位置（`Desktop/`、项目根目录），确认无残留
4. 在"第六步：变更摘要"中列出清理结果

**常见清理位置：**
- `~/Desktop/` — 最容易堆积 `__*.json`、`_*.py`
- 项目根目录 — 飞书操作留下的 `_f.json`、`__fields.json`
- `$TEMP` — 偶尔有 `.feishu_tmp.json` 等

**禁止清理：**
- `.gitignore`、`CLAUDE.md`、`README.md`、`LICENSE`、`requirements.txt` 等合法项目文件
- 用户明确说过要保留的文件

### 第一步：盘点现状（强制机械式枚举，不能跳过）

**先做 ls，再做判断。**

1. 列出 agent 的记忆文件（如有）：
   - Claude Code：`ls ~/.claude/projects/<...>/memory/` 并读 `MEMORY.md` 及所有被引用的 `.md`
   - Codex / OpenCode / 其他：找该 agent 的等价位置（见 references/agent-paths.md）
2. 对本次对话涉及的**每一个项目**：
   - `ls <project-root>/` → 确认根目录结构
   - `ls <project-root>/docs/ 2>/dev/null` → **枚举所有 docs**（缺失也要确认）
   - `find <project-root> -maxdepth 2 -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*"` → 兜底抓散落的 .md
   - 读 `README.md`、`CLAUDE.md` / `AGENTS.md`、每一个 `docs/*.md`
3. 读全局 agent 配置（若有，如 `~/.claude/CLAUDE.md`、`~/.codex/AGENTS.md`）
4. 回顾本次对话全部内容
5. 扫描 GitHub（gh CLI 必须已认证，不可用则跳过并在摘要说明），两路并行：
   - **第一路：我的仓库 + 我的 star**
     - `gh repo list --limit 100 --json name,description,updatedAt,stargazerCount,primaryLanguage,url` → 全量自有仓库
     - `gh api --paginate user/starred -q '.[] | {name: .full_name, stars: .stargazers_count, lang: .language, desc: .description, topics: .topics}'` → 全量 star
   - **第二路：GitHub 全站搜索**（按 star 排序取前 5）
     - 提取本次对话的 2-3 个核心关键词
     - `gh search repos "关键词1 关键词2" --sort stars --limit 5 --json fullName,description,stargazersCount --jq '.[] | "\(.fullName) | ★\(.stargazersCount) | \(.description[0:60] // "N/A")"'`
   - **目标**：判断这些仓库有没有对本次对话有帮助的项目（参考/复用/直接用）

**输出一张文件清单**（内部用，不用给用户看），对每个文件标：「评估过 / 要改 / 不用改」。**漏一个不行**——这是这个 skill 最容易翻车的地方。

### 第二步：识别变更——用"变更影响矩阵"思考

**不要只看对话增量有什么新事实，要看新事实会波及哪些文档层级。**

常见模式速览：
- 新增 API / 路由 → CLAUDE.md 路由清单 + integration-guide + architecture 的 Routes
- 新增 / 改名 环境变量 → CLAUDE.md 环境变量表 + runbook + 下游 integration-guide
- 新增数据库表 → CLAUDE.md + architecture 的 Data Model
- 新增大特性（跨多文件） → 以上全部 + architecture 新章节 + handoff 已完成清单
- 跨项目改动 → 上下游两边的 docs **都要对齐**（最常见的漏改场景）
- Base 表结构变更（增删字段、修改公式、调整视图）→ 更新 `wiki/topics/` 对应索引文件（记录字段清单、公式修复、已清理字段等），不要只改代码不改 wiki
- 记忆层面：相对时间→绝对日期、过期事实→改、重复→合并、已完成待办→删

完整映射表（覆盖更多变更类型与对应文档）见 **[references/sync-matrix.md](references/sync-matrix.md)**——遇到不确定的改动先查这张表。

**关键检查**：这次对话是不是**跨项目**的？如果改了项目 A 且项目 B 依赖它（通过 SDK、API、子域、环境变量），**项目 B 的 docs 也要改**。这是历次同步最常翻的车。

### 第三步：实际修改（用工具，不只是描述）

你必须**真的用 Edit 修改现有文件、用 Write 创建新文件、用删除命令清理废弃文件**。"我会怎么改"的描述不算完成。

**顺序建议**：先改 docs/（改错影响外部）→ 再改 CLAUDE.md/AGENTS.md → 最后理记忆。先动外部优先级最高的，即使中途被打断，读者看到的也是对齐的最新状态。

**编辑原则**：

| 原则 | 说明 |
|------|------|
| 减优于加 | CLAUDE.md 净涨幅 >30 行 = 红灯，在写叙事而非补规则 |
| 合并优于追加 | 新信息是旧信息的更新，改旧条目；先 grep 同关键字 |
| 删除优于保留 | 完成的临时计划、推翻的决策、旧版本记忆、流水账复盘 |
| 精确优于冗长 | 一条记忆说清楚一件事，别塞三件 |
| 绝对时间 | 永远 `2026-05-28`，不写"今天"、"最近" |
| 面向读者 | docs/ 读者是外部人，想象对方只有 5 分钟 |
| 受众不混 | CLAUDE.md 不抄 docs/ 全文，docs/ 不写"我记得" |
| 指针不重复 | 同一事实 docs/ 已详写，CLAUDE.md 只在指针表出现一次 |

**全局配置极度克制**：`~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md` 只有用户在对话中明确表达了**跨项目的核心原则**才动。日常项目细节绝不进全局。

**docs/ 编辑要点**——新增一个能力的文档变更通常要四处都补：
1. **integration-guide** 或对应"外部视角"文档：加**怎么用**（curl / SDK 示例 / 错误码表）
2. **architecture**：加**怎么工作**（数据流、状态机、设计取舍）
3. **runbook**：加**怎么运维**（冒烟命令、故障排查、环境变量）
4. **handoff** 或 CHANGELOG：加**已完成**

API 速查表、环境变量表、术语表是高频查询的结构化信息，**必须保持"所见即最新"**。

### 第四步：自检清单（必须逐项过一遍）

改完后逐条检查，打不了勾的**回去补**。

| 分类 | 检查项 |
|------|--------|
| **尺寸/反膨胀** | CLAUDE.md 净涨幅 ≤30 行 · 无 blockquote 历史叙事 · 无抄 docs/ 的机制说明 · 单条 memory ≤100 行 |
| **完整性/反漏改** | 第一步每个文件都判断了"不用改"或"已改" · 记忆索引链接指向存在的文件 · 记忆之间无矛盾 · 路径/命令/环境变量在代码中真实存在 · README 与代码一致 |
| **跨层对齐** | 新增 API 路由：integration-guide + architecture 都有 · 新增环境变量：runbook + 项目根 markdown 都有 · 新增数据库表：architecture + 项目根都有 · 跨项目影响：下游 docs 也改了 |
| **时间合规** | `grep -E "今天|昨天|刚刚|最近|上周|today|yesterday|recently"` 清零 |
| **沉淀** | 个人网站扫描已执行 · 新特质已写入 user_traits_unified.md（或说明为什么没有） · 可复用经验已写入 interview-summary.md（或说明为什么没有） · GitHub 扫描已执行并交叉比对 |

### 第五步：个人特质与经验沉淀（强制，不可跳过）

**无论本次对话内容多简单，以下三个子步骤都必须执行，不得以"没什么新东西"为由省略。**

### 前哨战知识库同步（本会话涉及 AI 方法论/创业/知识库/Agent 时触发）

触发关键词：知识库构建、Skill创作、Agent训练、反馈循环、AI学习、创业方法论、零成本创业、模型选择、工作vs学习、提示词训练、拆解skill、agent懂vs会

1. 读 `wiki/topics/前哨战.md` 检查现有条目
2. 识别本次对话中可补充/更新的内容
3. 用 Edit 更新对应板块（合并优于追加，不重复）
4. 全新主题 → 新增板块并更新关联主题表

#### 5a. 个人网站扫描
1. 扫描本次对话全部内容
2. 判断是否有值得加入 `personal-site/index.html` 的新信息（新产品、成就数据、职业进展、技能提升等）
3. **有** → 列出具体内容并询问用户是否加入，用户确认后真实修改文件
4. **没有** → 明确告知"本次对话无需要加入个人网站的新内容"

#### 5b. 特质识别与写入
1. 回顾本次对话，识别用户表现出的新特质、新偏好、新行为模式
2. 查 `user_traits_unified.md` 最后一个 T 编号，+1 作为新编号
3. 写入 `user_traits_unified.md`
4. **没有新特质** → 说明理由（已有哪个 T 编号覆盖）

#### 5c. 可复用经验提炼与写入
1. 提炼本次对话中产生的方法论、决策经验、避坑指南
2. 写入 `notes/interview-summary.md` 的"可复用经验"章节
3. **没有新经验** → 说明理由

#### 5d. GitHub 活动关联

1. **交叉比对**：将 Step 1 采集的 GitHub 全量数据（star + 自有仓库）与本次对话主题逐一比对
   - 优先匹配 **topics 字段**，其次匹配 **description 关键词**
   - 判断标准：这个项目能不能帮当前对话做**参考/复用/直接用**
2. **命中** → 在变更摘要中列出相关项目并说明为什么有帮助
3. **不命中** → 说明"本次 GitHub 扫描无相关项目"
4. 不再维护 `reference_github-discoveries.md` 引用文件，已存在的旧文件直接保留不更新

### 第六步：变更摘要

在所有文件修改完之后（不是之前），给用户简洁摘要：

```
## 同步完成

### 记忆变更
- 更新：xxx（原因）
- 新增：xxx
- 删除：xxx（原因）

### 文档变更（按项目分组，每个项目列全改动的文件）
- <项目 A>/CLAUDE.md — xxx

### 个人网站
- 有新内容：xxx（已询问用户/已修改） / 无新内容

### 新特质
- Txx：xxx / 无新特质（已有 Tx 覆盖）

### 可复用经验
- xxx / 无新经验

### GitHub 活动关联
- 相关项目：xxx（项目名 → 对本次对话的帮助） / 无相关项目

### 前哨战知识库
- 已更新：xxx（新增/修改了哪个板块） / 未触发（本次对话不涉及相关主题）

### 未处理
- xxx（为什么没处理）
```

只列有实际变更的条目。没改的不写。

## 完成标准

- [ ] 所有文件尺寸在限制内
- [ ] 没有相对时间遗留
- [ ] 没有历史叙事在 CLAUDE.md
- [ ] 个人网站扫描已执行
- [ ] 新特质已识别并写入
- [ ] 可复用经验已提炼并写入
- [ ] GitHub 扫描已执行
- [ ] 变更摘要已输出给用户

## 特殊情况

**项目还没有 README 或 CLAUDE.md/AGENTS.md**：判断项目是不是到了"有可运行代码"的阶段。是 → 创建。还在 vibe 阶段 → 跳过，但在摘要里提一句。

**对话没有产生新事实**：审查现有记忆和文档有没有过期 / 冲突 / 相对时间——审查本身就有价值。

**记忆之间出现无法自动判断的矛盾**：列在「未处理」让用户决定。**这是唯一需要用户介入的情况**，其他都自己拍板。

**跨项目改动**：本次对话改了多个项目，每个项目都要跑一次完整的第一步（ls + 读 docs）。不要假设一个项目的 docs 改了，另一个就不用。尤其是上游-下游对接文档（集成指南 / SDK 说明 / API 协议），两边都要对齐。

**发现之前的同步漏了东西**：修掉。不要说"那不是这次对话的事"——你就是这个项目的持续编辑，过去的漏洞也归你管。

## 参考资料

- **[references/sync-matrix.md](references/sync-matrix.md)** — 完整的"变更类型 → 要改哪些文件"映射表
- **[references/agent-paths.md](references/agent-paths.md)** — Claude Code / Codex / OpenCode 各自的记忆与配置路径速查
