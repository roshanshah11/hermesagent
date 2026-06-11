---
name: repo-monitor
description: Poll Roshan's allowlisted repos via gh CLI — failing CI, new issues, stale branches → Telegram digest. Read-only; honest-empty.
version: 0.1.0
---
# Repo Monitor

JOB: watch the repos in context/repos.md so Roshan never discovers a red CI run, an unanswered
issue, or an aging branch by accident. Honest "all green, nothing new" beats manufactured alerts.

OUTPUT CONTRACT (Telegram, ≤10 lines): per repo, only what CHANGED since last run — ❌ failing CI
(workflow · branch · link) · 🆕 new issues (title · link) · 🥀 stale branches (no commits >14d;
flag hermes/* with a PR still awaiting his review). Nothing new anywhere = one line, done.
Roshan replies "fix N" → hand off to coding-pr (its allowlist rules apply).

STATE: memory/repo-monitor-state.json (agent data dir) — last-seen run/issue/branch ids per repo,
so "new" means new since last run; never re-alert the same item.

HARD CONSTRAINTS: READ-ONLY — gh list/view only; no issue comments, no workflow re-runs, no branch
deletes, no writes of any kind to any repo · scope = context/repos.md, nothing else until Roshan
names more · every claim carries its link · no Notion writes, no Change Log entry.

v0 default method (yours to improve): per repo — gh run list (latest per workflow, flag failures) ·
gh issue list --state open (diff vs state) · branch last-commit ages via gh api (cross-check
gh pr list for orphaned hermes/* branches) → diff vs state → compose → send → save state.

Cron candidate: daily 18:00 (respect the ≥15-min stagger rule; see crons/crons.md).
