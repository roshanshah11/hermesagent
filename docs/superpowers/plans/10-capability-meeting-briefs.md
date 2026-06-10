# Plan 10 — Capability: Pre-Meeting Briefs

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Roshan never walks into a call cold. Every networking call, internship meeting, or professor chat gets a brief the evening before — who they are, every prior touch, what he wants out of it, and questions worth asking — researched at rubric grade, because a wrong "fact" spoken in a live call is worse than no brief at all.

**Gap source:** delegation analysis §3 — *"Networking RAMP — in-person Chicago, 2–3 calls/wk"* + the Mon/Thu/Wed internship meetings. The calls themselves are human-only by design; walking in prepared is pure agent work the corpus never assigned.

**Depends on:** Plan 01 (agent live), Plan 02 (rubric). **Enhanced by, not blocked on:** Plan 04 (email thread context), Plan 11 (CRM touch history).

---

### Task 1: Where briefs live — Calls surface discovery

**Files:** Modify: `context/notion-ids.md`

- [ ] **Step 1: Check the Calls surface** — ask Hermes: `Using mcp_notion-v3_notion_collection_schema on 5fd16c2d-f547-4990-802d-7d7ada0e588b (Calls, from context/notion-ids.md), list every property name + type. If it's not a collection, read it as a block and describe what it is.` Paste the real answer into `context/notion-ids.md` as a `## Calls surface` note.
- [ ] **Step 2: Pick the filing target** — if Calls is a collection with usable fields (person relation, date): briefs file there as rows/sub-pages. Otherwise fallback: brief files as a sub-page on the person's People DB row (notion-ops protocol either way). Record the decision in the same note.
- [ ] **Step 3: Commit** — `git add context/notion-ids.md && git commit -m "docs: Calls surface verified — meeting-brief filing target"`

### Task 2: `meeting-brief` skill

**Files:** Create: `skills/meeting-brief/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: meeting-brief
description: Pre-meeting brief for tomorrow's (or today's) calls and meetings — who, history, agenda, questions. Cited, never invented; a wrong fact in a live call is worse than a gap.
version: 0.1.0
---
# Meeting Brief

TRIGGER: nightly cron over tomorrow's timed Tasks rows that are calls/meetings with a person or firm
attached; or on demand ("brief me for my 2pm", "brief for the call with <name>").

CONTRACT — for each meeting deliver:
1. WHO: name · role · firm/group · location, plus 2–3 facts that actually matter (recent deal /
   paper / news, school tie) — deep-research light, every fact cited or [verify]-flagged.
   The People DB row is the seed; public sources extend it.
2. HISTORY: every prior touch — outreach thread (People row notes), replies, past calls/debriefs.
   "First contact" is a valid answer; never invent rapport.
3. WHY: what Roshan wants from THIS meeting (task row context; if absent, ask him once via Telegram).
4. ASK: 3–5 specific questions worth asking, tied to THEIR actual work and his goals (IB recruiting,
   markets/quant, research). Generic questions ("tell me about your path") fail the bar.
5. LOGISTICS: time (America/New_York) · duration · format/link if known.

HARD CONSTRAINTS:
- The rubric (context/quality-rubric.md) applies to the WHO facts. NO invented facts about a person,
  ever — uncertain → [verify] or omit. Precision over completeness.
- ≤20 lines per brief to Telegram; full version filed per the Calls-surface decision in
  context/notion-ids.md (notion-ops protocol).
- Read + file only. Never message the counterparty; rescheduling needs = calendar-propose output
  for Roshan to send.

AFTER the call, prompt once: "reply 'debrief: <2 lines>' and I'll file it." File the debrief with
the brief; once Plan 11 lands, the debrief also logs a CRM touch (thank-you draft follows from there).
```

- [ ] **Step 2: Trust ledger row** — append to the `context/trust.md` table: `| meeting-brief | L2 | day1 | stays L2 (Notion filing audited) |`
- [ ] **Step 3: Test (real person, bounded)** — create a test task row "Call with <a real professor from the People DB> tomorrow 2pm" linked to the person → `/meeting-brief`. Expected: cited WHO facts, honest "first contact" history, 3–5 questions specific to their work, ≤20 lines, full brief filed with a Change Log row.
- [ ] **Step 4: The invented-fact test** — run it on a person with a thin public footprint. Expected: [verify] flags and omissions, NOT confident filler. Confident wrong facts = the skill fails; tighten wording and retest.
- [ ] **Step 5: Commit** — `git add skills/meeting-brief/ context/trust.md && git commit -m "feat(skill): meeting-brief — cited pre-call briefs"`

### Task 3: Cron + morning-brief catch

**Files:** Modify: `crons/crons.md`, `skills/morning-brief/SKILL.md`

- [ ] **Step 1: Add cron** — `crons/crons.md`: `Daily 21:15 — meeting-brief: scan tomorrow's timed Tasks rows for calls/meetings → briefs to Telegram (rides behind the 21:00 due-tomorrow pre-load).` Register per hermes-facts.md syntax.
- [ ] **Step 2: Same-day catch** — append one line to `skills/morning-brief/SKILL.md` compose list: `🤝 meetings today: any timed call/meeting row with no brief filed → flag it ("no brief — say 'brief me for X'").`
- [ ] **Step 3: Fire test** — one-off cron "in 2 minutes" with a seeded tomorrow-call row; confirm Telegram delivery; remove test job and test row (archive, not delete).
- [ ] **Step 4: Commit** — `git add crons/crons.md skills/morning-brief/ && git commit -m "feat(capability): nightly meeting-brief cron + morning catch"`

---

**Self-review:** wrong-fact risk treated as the binding constraint (rubric + invented-fact test) ✓ · Calls surface verified before depended on, with honest fallback ✓ · counterparty contact structurally excluded (read + file only) ✓ · debrief hook hands off to Plan 11 without hard dependency ✓ · no placeholders ✓
