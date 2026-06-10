# Plan 13 — Cron: Weekly-Review-Prep

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** His weekly review becomes *reviewing*, not assembling: by Sunday afternoon a pre-filled review doc is waiting — what slipped, the week ahead, relationship state, a proposed research queue, and what Hermes shipped — so his review block starts at the judgment layer.

**Gap source:** delegation analysis §2 verbatim: *"Week-ahead prep. Reconcile what slipped, pre-draft next week's research queue, refresh the outreach/follow-up list (who's gone cold). A pre-filled weekly-review doc so his review is reviewing, not assembling."*

**Depends on:** Plan 01. **Sections light up as their plans ship:** 02 (audit grades), 06 (Idea List), 07 (deadline DBs), 11 (follow-up state) — the skill renders what exists and says what's missing; it never fakes a section.

---

### Task 1: `weekly-review-prep` skill

**Files:** Create: `skills/weekly-review-prep/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: weekly-review-prep
description: Sunday pre-fill of Roshan's weekly review — slipped / week-ahead / relationships / research queue / Hermes's week — filed to Notion + TL;DR to Telegram. Assembles the facts; the review judgments stay his.
version: 0.1.0
---
# Weekly Review Prep

OUTPUT: one doc, filed "YYYY-MM-DD — Weekly Review Prep" as a sub-page under the Hub
(context/notion-ids.md; notion-ops protocol) + local mirror output/review/YYYY-MM-DD.md.
Telegram TL;DR ≤15 lines with the link. Sections — render only what's live, name what's missing:

1. ⏪ SLIPPED — overdue + not-done from the week (Tasks DB). Name patterns, not blame
   ("technicals block slipped 3rd week running"), so the review can fix the system.
2. ⏩ WEEK AHEAD — deadlines ≤14 days across Tasks · IB Applications · Club Applications ·
   Course Plan; timed commitments; test sits. Anything ≤72h flagged loud.
3. 👥 RELATIONSHIPS — awaiting-reply · follow-ups due · gone-cold (followup-engine state,
   context/crm-fields.md). Queued drafts get linked, not re-described.
4. 🔬 RESEARCH QUEUE (proposal only) — 2–3 Substack deep-dive candidates from Markets Idea List
   Raw rows (305bffe5-cd5f-4bae-8788-b8e337ded74d), one line each on why now — HE picks, you never
   do (his decision, per charter). Plus research debt: anything he asked for that isn't delivered.
5. 🤖 HERMES'S WEEK — what shipped (Change Log Source=Hermes: count + 3 highlights), failures and
   redos stated honestly. Spot-audit grading stays with its own 18:00 cron — link, don't duplicate.
6. 📝 PROPOSALS — cron/skill/priority changes you'd suggest, proposal-only (drift guard, HERMES.md
   rule 7).

HARD CONSTRAINTS: assemble and propose, never decide — no auto-picking deep-dives, no reflowing his
calendar (the Notion project's operator owns that), no padding quiet sections to look busy.
```

- [ ] **Step 2: Trust ledger row** — append to `context/trust.md`: `| weekly-review-prep | L2 | day1 | stays L2 (filing audited; content is proposals) |`
- [ ] **Step 3: Commit** — `git add skills/weekly-review-prep/ context/trust.md && git commit -m "feat(skill): weekly-review-prep — assembled facts, his judgments"`

### Task 2: Cron — the Sunday ops window

**Files:** Modify: `crons/crons.md`

- [ ] **Step 1: Confirm his review slot** — check the Tasks DB for his recurring Weekly Review row (time/day). Default if unscheduled: deliver Sun 16:00 (before the 17:00–20:00 family block; doc waits whenever he reviews).
- [ ] **Step 2: Add cron + document the window** — `crons/crons.md`: `Weekly Sun 16:00 — weekly-review-prep → Notion + Telegram TL;DR.` Add a note block: `## Sunday ops window — order matters: 16:00 weekly-review-prep (assembles the week) → 18:00 spot-audit (grades samples, Plan 02) → 19:00 skill-review (proposes growth, Plan 09).` Register per hermes-facts.md.
- [ ] **Step 3: Fire test** — one-off "in 2 minutes" run. Expected with current data: real slipped rows, deadlines including the Jun 15/16 sits, an honest "followup-engine not live yet" if Plan 11 hasn't shipped, TL;DR ≤15 lines, doc filed with Change Log row.
- [ ] **Step 4: Commit** — `git add crons/crons.md && git commit -m "feat(cron): weekly-review-prep + Sunday ops window ordering"`

---

**Self-review:** the §2 gap closed (slipped / queue / follow-up refresh all present) ✓ · decisions stay his — research queue is proposal-only, deep-dive pick never automated (charter §3) ✓ · degrades honestly when Plans 02/06/07/11 haven't shipped ✓ · Sunday window sequenced against existing 18:00/19:00 crons, no collisions ✓ · no calendar reflow (Notion-project boundary held) ✓ · no placeholders ✓
