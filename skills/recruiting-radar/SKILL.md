---
name: recruiting-radar
description: Weekly watch on IB/finance sophomore recruiting — new openings and deadline changes → IB Applications DB + Telegram. A missed deadline is unrecoverable; precision matters more than volume.
version: 0.1.0
---
# Recruiting Radar

JOB: weekly watch on sophomore IB/finance recruiting — new programs and deadline changes land in
the IB Applications DB and one Telegram digest. A missed deadline is unrecoverable; a WRONG
deadline is worse than a missing one.

OUTPUT CONTRACT (Telegram digest, terse text-chat voice):
- 🆕 new: program · firm · deadline · eligibility · link (one line each)
- ⏰ approaching: anything ≤14 days out
- ✏️ deadline changes — flagged loudly
- quiet week = one line, no padding (honest-empty beats invention)

HARD CONSTRAINTS: every deadline VERIFIED on the firm's OWN page before it's written — aggregators
corroborate, never source; unverifiable → [verify] in the row + said in the digest · all DB writes
via the notion-ops protocol (Control check → write → Change Log → readback) · diff before create —
no dupe rows · track/file only: application drafting is Plan 12's skill, submitting is Roshan's,
always · JS-walled or login-gated careers pages escalate via heavy-research — never guess.

ids: IB Applications collection ea517e94-9463-44ed-a62c-2a9b9ce9a97c (context/notion-ids.md) —
ADD IB Applications view id BEFORE FIRST RUN (notion_enumerate_rows needs collection + view).
sources: context/recruiting-sources.md (Plan 07 Task 1 — must exist before first run).

v0 default method (yours to improve): work the sources file (search + extract; firm pages are
truth) → enumerate IB Apps DB → diff → new program = create row (program, firm, deadline, link,
status=Researching); changed deadline = update row + flag → per-source last-checked state in
memory/recruiting-radar-state.json → compose digest, send. Deadlines ≤14 days out surface in the
morning brief automatically (it reads the same DB — no extra wiring).

Cron candidate: weekly Tue 08:00 (crons/crons.md).
