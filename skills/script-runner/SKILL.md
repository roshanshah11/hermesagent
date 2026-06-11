---
name: script-runner
description: Run a named script/backtest via code execution — results + plot file path back to Telegram, every run logged. Never scripts that move money or send anything.
version: 0.1.0
---
# Script Runner

JOB: Roshan names a script ("run the backtest") — run it, hand back the numbers and the plot, so
checking an idea costs him one Telegram message, not a terminal session.

INPUT: script name/path + args, from an allowlisted repo (context/repos.md) or one Roshan points
at explicitly. New or changed script → skim it BEFORE running; any outward call found (orders,
email, posts, paid APIs) = refuse and tell him exactly what you saw.

OUTPUT CONTRACT (Telegram, terse): exit status · headline numbers (the metrics, not a log dump) ·
plot file path(s) if produced · runtime. Failure = the actual error line + best-guess cause —
never summarize a crash as "ran with warnings".

LOG: append every run to memory/script-runs.jsonl (agent data dir): when · script · args · exit ·
artifact paths. The log is the audit trail — no silent runs.

HARD CONSTRAINTS: NEVER run anything that moves money, places/cancels orders, or sends anything
outward (email/messages/posts/uploads) — backtests and analysis only; live-trading scripts are
refused even when asked directly · no secrets on the command line · use the repo's own env, never
pip-install into system · long runs: cap ~10 min, report partial + ask before continuing.

v0 default method (yours to improve): locate script in ~/work/<repo> (box) → skim if new/changed →
execute via code execution with a timeout → collect stdout tail + artifacts (plots usually land
beside the script or in its output/ dir — report the real path) → log → Telegram.
