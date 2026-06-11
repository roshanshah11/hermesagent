---
name: transfer-tracker
description: UChicago transfer-student onboarding logistics — research once, track weekly until autumn quarter starts. The blind spot: he tracks placement TESTS but not the logistics stack.
version: 0.1.0
---
# Transfer Tracker

JOB: turn UChicago transfer-onboarding logistics from unknown unknowns into dated, cited rows —
deep-research the stack ONCE, then watch weekly for date changes until autumn quarter starts.

SCOPE (the contract of coverage): autumn course registration/bidding window + mechanics ·
transfer-credit evaluation/petition process + deadline · Core requirement mapping for transfers ·
adviser meeting requirement · housing deadlines · immunization/health-form deadline (registration
HOLD risk) · transfer orientation dates · anything else UChicago's transfer pages list.

OUTPUT CONTRACT:
- BUILD (first run): one Course Plan DB row per item + a dated Tasks row (Area=UChicago,
  Type=Deadline) wherever there's a deadline; the source page cited on EVERY row; the built
  list sent once to Telegram.
- WATCH (weekly): re-check pages; ⚠️ only what changed — no-change week = silent or one line.

HARD CONSTRAINTS: official UChicago pages ONLY (college.uchicago.edu etc.) · dates behind the
student portal → [verify] on the row + ask Roshan to confirm against the portal — never guess
login-walled dates · all writes via the notion-ops protocol (Control check → write → Change Log
→ readback) · heavy/JS pages escalate via heavy-research · honest-empty beats invention.

ids: Course Plan collection 93b93826-79e1-44b5-a0a9-4131c9fbcd0d (per Plan 07); Tasks ids in
context/notion-ids.md — ADD Course Plan DB entry + view id BEFORE FIRST RUN (enumerate needs
collection + view).

v0 default method (yours to improve): first run = deep research across the SCOPE list on official
pages, file rows via notion-ops, send the list; weekly = re-fetch tracked pages, diff against
memory/transfer-tracker-state.json, update rows + ⚠️ changes only.

Cron candidate: weekly Wed 08:00, until autumn quarter starts (crons/crons.md).
