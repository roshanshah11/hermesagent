---
name: meeting-brief
description: Pre-meeting brief for tomorrow's (or today's) calls and meetings — who, history, agenda, questions. Cited, never invented; a wrong fact in a live call is worse than a gap.
version: 0.1.0
---
# Meeting Brief

JOB: Roshan never walks into a call cold. Nightly, scan tomorrow's timed Tasks rows that are
calls/meetings with a person or firm attached; also on demand ("brief me for my 2pm", "brief for
the call with <name>"). One brief per meeting, the evening before.

OUTPUT CONTRACT (per meeting — ≤20 lines to Telegram; full version filed per the Calls-surface
decision in context/notion-ids.md, notion-ops protocol incl. readback):
1. WHO: name · role · firm/group · location + 2–3 facts that actually matter (recent deal /
   paper / news, school tie). People DB row is the seed; public sources extend it (deep-research,
   light). Thin public footprint → dispatch heavy-research before settling for gaps.
2. HISTORY: every prior touch — outreach thread (People-row notes), replies, past calls/debriefs.
   "First contact" is a valid answer; never invent rapport.
3. WHY: what Roshan wants from THIS meeting (task-row context; if absent, ask him once via Telegram).
4. ASK: 3–5 questions tied to THEIR actual work and his goals (IB recruiting, markets/quant,
   research). Generic ("tell me about your path") fails the bar.
5. LOGISTICS: time (America/New_York) · duration · format/link if known.

HARD CONSTRAINTS:
- THE GATE: a wrong fact in a live call is worse than no brief. Every WHO fact cited or
  [verify]-flagged (deep-research gate); uncertain → [verify] or omit. Precision over completeness.
- Read + file only. Never message the counterparty; rescheduling needs = calendar-propose output
  for Roshan to send.
- Honest-empty: no qualifying meetings → no message (on demand: say so, one line).

AFTER the call, prompt once: "reply 'debrief: <2 lines>' and I'll file it." File the debrief with
the brief and log a CRM touch via followup-engine (thank-you draft follows from there).

v0 default method (yours to improve): enumerate tomorrow's timed Tasks rows → person/firm via the
Tasks↔People relation → research → compose → file → Telegram. Track briefed rows in
memory/meeting-brief-state.json so unbriefed same-day meetings can be flagged.
