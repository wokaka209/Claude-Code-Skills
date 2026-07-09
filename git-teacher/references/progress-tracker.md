# Git 学习进度追踪

## 当前学习进度

| 模块 | 状态 | 内容 |
|------|------|------|
| 01_basics | ✅ 完成 | init, add, commit, status, log |
| 02_branching | ✅ 完成 | branch, checkout, switch, merge |
| 03_remote | ✅ 完成 | remote, push, pull, fetch, clone |
| 04_undoing | ✅ 完成 | restore, reset, revert, stash |
| 05_collab | ✅ 完成 | PR, code review, conflict resolution |
| 06_advanced | 🔄 进行中 | rebase, cherry-pick, bisect, worktree |

---

## 复习记录

<!-- 格式：| 命令/概念 | 学习日期 | 复习1 | 复习2 | 复习3 | 复习4 | -->

| 命令/概念 | 学习日期 | 1h后 | 1天后 | 3天后 | 7天后 |
|----------|---------|------|------|------|------|
| git init, add, commit | 2026-07-02 | ⏳ | ⏳ | ⏳ | ⏳ |
| git status, log | 2026-07-02 | ⏳ | ⏳ | ⏳ | ⏳ |
| git branch, switch, merge | 2026-07-02 | ⏳ | ⏳ | ⏳ | ⏳ |
| git remote, push, pull | 2026-07-02 | ⏳ | ⏳ | ⏳ | ⏳ |
| git restore, reset | 2026-07-02 | ⏳ | ⏳ | ⏳ | ⏳ |
| PR, code review | 2026-07-02 | ⏳ | ⏳ | ⏳ | ⏳ |

---

## 学习笔记

### 2026-07-02 学习内容

**模块 01-05 完成：**
- `git init` = 初始化仓库（租店面）
- `git add` = 暂存文件（放收银台）
- `git commit` = 保存存档（贴标签）
- `git branch` = 创建分支（平行宇宙）
- `git switch` = 切换分支（穿越宇宙）
- `git merge` = 合并分支（带回成果）
- `git remote` = 关联远程仓库（设置云端地址）
- `git push` = 推送到远程（上传存档）
- `git pull` = 拉取远程更新（下载存档）
- `git restore` = 撤销工作区修改（橡皮擦）
- `git reset` = 撤回提交（时光倒流）
- `gh pr create` = 创建 PR（提交合并申请）
- `gh pr merge --squash` = 合并 PR（压缩合并）

**费曼检验平均得分：7/10**
- 理解基本准确，但细节需要补充
- 特别是 `git reset` 的三种模式和 `squash` 的作用

**待复习：**
- `git reset --soft/--mixed/--hard` 的区别
- `git rebase` 与 `git merge` 的区别
- 分支 + PR 的工作流

---

## 下次学习计划

**模块 06：高级操作**
- `git rebase` — 重写历史
- `git cherry-pick` — 摘取特定提交
- `git bisect` — 二分查找 bug
- `git worktree` — 多工作目录
