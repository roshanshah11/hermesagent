---
name: idea-logging
description: Capture market ideas to the Markets Idea List as Status=Raw — thesis + invalidation criteria. Capture-only; Roshan promotes. Rows are NEVER trade advice to execute.
version: 0.1.0
---
# Idea Logging

JOB: one funnel for market ideas — from Roshan ("log idea: ...") or surfaced by markets-digest /
filing-monitor / earnings-prep — filed to the Markets Idea List so nothing worth tracking is lost.

ROW CONTRACT (every row):
- Title: ticker/theme · one-liner thesis (whose idea + why now)
- INVALIDATION criteria: the observable fact that kills it (Roshan gave none → propose one,
  prefixed "proposed:")
- Source cited (filing/article/conversation) · Status=Raw — always Raw at capture
- Confirm to Telegram in one terse line: what filed + row link

HARD CONSTRAINTS: notion-ops protocol on every write (Control row first, Change Log after,
readback before reporting — a row you can't read back did NOT happen) · capture-only: Roshan
promotes stages, you NEVER move a row past Raw · archive, never delete · rows are research
bookmarks, NEVER trade advice executed or framed as instruction · dupe-check first — same
ticker+thesis = note on the existing row, not a re-file · read the live schema before the first
write; never assume property names.

IDS: Markets Idea List collection id — context/notion-ids.md.
ADD BEFORE FIRST RUN: Markets Idea List VIEW id to context/notion-ids.md (enumerate/dupe-check
needs collection AND view — Sim 6 lesson, hermes-facts Correction 27).

v0 default method (yours to improve): parse ticker/thesis/invalidation from the ask → enumerate
for dupes → create row per notion-ops write recipes → readback → Change Log → one-line confirm.
