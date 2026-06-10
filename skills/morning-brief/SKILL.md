---
name: morning-brief
description: Daily 06:30 brief — today's schedule + what matters, to Telegram. Also on demand ("brief me").
version: 0.1.0
---
# Morning Brief

JOB: every morning (and on demand) Roshan gets one Telegram message that tells him what today
actually is — without opening Notion.

OUTPUT CONTRACT (≤25 lines, Telegram):
- ⭐ Top 3 (Focus flag first; else priority: hard deadlines → IB/markets → networking)
- 🕐 today's timed rows, chronological
- ⚠️ overdue: count + worst 3
- 📅 deadlines within 7 days (Type=Deadline)
- 💡 at most one suggestion, only if it earns its place

HARD CONSTRAINTS: read-only (no Notion writes, no Change Log needed) · America/New_York for all
"today" math (`When` is computed from `Due` — recompute, don't trust stale formula reads).

v0 default method (yours to improve): enumerate Tasks (collection + view in context/notion-ids.md),
read Due/Status/Type/Area/Focus per alive row (batch reads), compute TODAY / OVERDUE /
UPCOMING-CRITICAL, compose, send.
