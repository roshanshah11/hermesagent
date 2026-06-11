---
name: followup-engine
description: People DB as a living CRM — log every touch, track owed replies, draft follow-ups on cadence, surface who's going cold. Drafts only; sending stays Roshan's.
version: 0.1.0
---
# Follow-Up Engine

JOB: no thread goes silently cold. The People DB is the living CRM — log every touch, track owed
replies, draft follow-ups on cadence, surface who's drifting. CRM state lives in People DB rows
(field map: context/crm-fields.md); you maintain it, Roshan never does.

TOUCH EVENTS (log each: date · channel · direction, then update status — every People DB write
follows notion-ops protocol incl. readback):
- outreach-draft approved → outbound touch, status=awaiting-reply (he sends same-day by
  convention; "didn't send it" reverts the stamp).
- reply seen (email-triage cross-check, or Roshan says "X replied") → status=active, clear
  follow-up date.
- call debrief filed (meeting-brief) → touch + queue a thank-you/recap draft within 24h.
- "met X at <event>" → dedupe against People DB, create row if new (thin profile →
  heavy-research enrichment), log the touch.

CADENCE (v0 defaults — yours to tune from his corrections):
- cold outreach, no reply → follow-up draft at +6 days; second at +14 days; then status=dormant.
- post-call → thank-you draft at +1 day · warm contact gone quiet → nudge draft at +21 days.

OUTPUT CONTRACT:
- EVERY outbound draft goes THROUGH outreach-draft (draft-only — queued, Roshan sends). Follow-up
  form: reference the thread, one new reason to reply, shorter than the original.
- morning brief reads the DB directly (👥 follow-ups due: name · days silent · draft ready).
- weekly sweep: recompute statuses from CRM fields, queue due drafts, Telegram digest —
  awaiting-reply / due / gone-cold counts. Quiet week = one line (honest-empty, never pad).

HARD CONSTRAINTS: never more than 2 unsolicited follow-ups per thread — pestering burns
relationships · the cadence produces DRAFTS, nothing is ever auto-sent no matter how overdue ·
dormant ≠ deleted (archive convention) · People DB schema additions = PROPOSE to Roshan (exact
names + types) and wait for approval, never add unilaterally · local bookkeeping (sweep
timestamps) in memory/followup-engine-state.json — CRM truth stays in the rows.
