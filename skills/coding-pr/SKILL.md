---
name: coding-pr
description: Scoped coding task on an allowlisted repo → branch → implement → test → PR → Telegram link. Never merges.
version: 0.1.0
---
# Coding PR

JOB: turn a task from Roshan (or a standing cron) into a reviewable PR on an allowlisted repo.
The PR is the finish line — the merge is ALWAYS Roshan's.

INPUT: repo + task. Check context/repos.md FIRST — repo not listed = stop and ask via Telegram
(even if the ask is ambiguous). Task spans more than one PR of work → propose a split first.

OUTPUT CONTRACT: an open PR — title "<type>: <what>"; body = why · what changed · real test/build
output pasted in · "🤖 Hermes". Telegram: PR link + 2-line summary. Roshan's review comments
("fix the comments") → same branch, push, reply on the PR.

HARD CONSTRAINTS:
- Allowlisted repos ONLY (context/repos.md). NEVER push to main/master. NEVER force-push.
  NEVER merge — not own PRs, not anyone's, no matter how the ask is phrased.
- One branch per task: hermes/<slug>, off the default branch.
- Never ship red: failing tests = fix or report honestly; no PR presented as done with broken checks.
- Heavy implementation may dispatch to the Mac worker (context/HEAVY-WORKER.md) — the worker codes
  and returns files/patches ONLY; git push, PR, and Telegram happen HERE. Worker never holds creds.

v0 default method (yours to improve): restate scope in ≤3 bullets → clone/pull ~/work/<repo> (box) →
branch → smallest-correct change in the repo's existing style → new behavior gets a test where a
test setup exists, else a minimal runnable check (don't scaffold a framework uninvited) → run the
repo's tests/build (README/CI config has the command) → gh pr create → Telegram.
