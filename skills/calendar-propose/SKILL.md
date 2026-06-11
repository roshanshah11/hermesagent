---
name: calendar-propose
description: Propose meeting slots for networking calls — no calendar write access; outputs ready-to-send scheduling lines.
version: 0.1.0
---
⛔ BLOCKED ON ROSHAN INPUT: email account choice (gmail vs uchicago) + app password / calendar source

# Calendar Propose

JOB: when a chat needs scheduling, hand Roshan three concrete conflict-free slots and a
paste-ready line — he never does calendar math. (Banner blocks v2 only; v0 runs calendar-free.)

Standing rhythm (America/New_York): gym 7:30–9 · deep work 9:30–13:00 (protect) · internship
Mon/Thu 11:00–11:30 + Wed 12–13 (hard) · family 17:00–20:00 (hard) · open-ish 13:30–16:00
weekdays · evenings 21:00+ · weekend flex. Networking calls fit best 13:30–16:00.

OUTPUT CONTRACT (Telegram, terse):
- 3 specific slots ("Tue 6/16 2:00–2:30pm ET") — none inside hard blocks or known timed rows
- One paste-ready scheduling line for his draft/reply
- He confirms a slot → create the Notion task row for the call, linked to the person
  (notion-ops protocol)

HARD CONSTRAINTS: NO calendar write access in v1 — you propose, he sends/books · explicit TZ
on every time (ET) · Notion writes only via notion-ops · honest-empty: a genuinely jammed week
gets "no clean slot — loosen which constraint?", never a slot inside a protected block.

v0 default method (yours to improve): read today/this-week timed Tasks rows (morning-brief
logic) for known conflicts → fit against the rhythm above → propose 3.

v2 (deferred, what the banner blocks): real calendar read via Google Calendar MCP once the
email/calendar account is settled.
