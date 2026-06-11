---
name: eod-wrap
description: End-of-day wrap — what got done, what's still open, what needs Roshan's decision tomorrow. Evening cron + on demand ("wrap up the day").
version: 0.1.0
---
# End-of-Day Wrap

JOB: close Roshan's day in one glance — done / open / decisions — so tomorrow starts decided,
not discovered.

OUTPUT CONTRACT (≤15 lines, Telegram voice):
- ✅ Done today: count + the 3 that mattered (from Tasks status changes + today's Change Log rows)
- 🔁 Still open from today: the honest leftovers (Due today, not Done)
- ❓ Needs your decision tomorrow: anything blocked on a choice only Roshan can make
  (drafts awaiting approval, queued jobs, flagged [verify] items)
- One line max of tomorrow preview (first timed row + any deadline inside 48h)

HARD CONSTRAINTS: read-only (no Notion writes, no Change Log entry) · America/New_York day
boundaries · honest zeros ("nothing open" beats invented items) · never re-list what the
morning brief will cover in depth.

v0 default method (yours to improve): enumerate Tasks for today's Due/Status; read today's
Change Log rows (Source=Hermes AND others) for the done-list; scan output/queue/ for pending
dispatches; compose; send.

Cron candidate: daily 21:30 (after the 21:00 preload — keep ≥15 min stagger; see crons/crons.md).
