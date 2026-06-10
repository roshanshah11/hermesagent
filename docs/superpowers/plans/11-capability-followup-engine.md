# Plan 11 — Capability: Follow-Up Engine (People DB as living CRM)

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** No thread goes silently cold. Every outreach touch is logged, owed replies are tracked, follow-ups draft themselves on cadence, and "follow up with X — 12 days silent" appears in the morning brief without Roshan maintaining anything.

**Gap source:** delegation analysis §4 verbatim: *"You have outreach tasks but no system: nobody's tracking who you contacted, who owes a reply, who's gone cold… Your People follow-ups view is the hook; nothing feeds it automatically."*

**Depends on:** Plan 01, Plan 02. **Enhanced by, not blocked on:** Plan 04 (reply detection from the inbox), Plan 10 (call debriefs as touches).

---

### Task 1: People DB schema discovery + CRM field map

**Files:** Create: `context/crm-fields.md`

- [ ] **Step 1: Read the schema** — ask Hermes: `Using mcp_notion-v3_notion_collection_schema on 5bb18055-a8c8-4dce-a671-4d7754f388bb (People DB), list every property name + type.` Paste the real output into `context/crm-fields.md`.
- [ ] **Step 2: Map CRM state onto EXISTING fields first** — the follow-ups view implies some already exist. Needed: Last touch (date) · Thread status (select: awaiting-reply / active / follow-up-due / dormant) · Next follow-up (date) · Channel (select: email / DM / in-person). For any that don't exist: PROPOSE the additions to Roshan via Telegram (exact names + types) and wait — schema changes are ask-first, never silent (his views hang off this schema). Record the approved mapping in `crm-fields.md`.
- [ ] **Step 3: Commit** — `git add context/crm-fields.md && git commit -m "feat(capability): People DB CRM field map (schema verified)"`

### Task 2: `followup-engine` skill

**Files:** Create: `skills/followup-engine/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: followup-engine
description: People DB as a living CRM — log every touch, track owed replies, draft follow-ups on cadence, surface who's going cold. Drafts only; sending stays Roshan's.
version: 0.1.0
---
# Follow-Up Engine

STATE lives in People DB rows (field map: context/crm-fields.md). You maintain it; Roshan never does.

TOUCH EVENTS (log each: date · channel · direction, then update status):
- outreach-draft approved → outbound touch, status=awaiting-reply (he sends same-day by convention;
  "didn't send it" reverts the stamp).
- reply seen (email-triage cross-check, or Roshan says "X replied") → status=active, clear follow-up date.
- call debrief filed (meeting-brief) → touch + queue a thank-you/recap draft within 24h.
- Roshan says "met X at <event>" → dedupe against People DB, create row if new, log the touch.

CADENCE (v0 defaults — tune from his corrections, Plan 09 pattern):
- cold outreach, no reply → follow-up draft at +6 days; second at +14 days; then status=dormant.
- HARD RULE: never more than 2 unsolicited follow-ups per thread — pestering burns relationships.
- post-call → thank-you draft at +1 day · warm contact gone quiet → nudge draft at +21 days.

OUTPUT:
- Every outbound draft goes THROUGH outreach-draft (L1 — queued, Roshan sends). Follow-up form:
  reference the thread, add one new reason to reply, shorter than the original.
- Morning brief reads the DB directly (👥 follow-ups due: name · days silent · draft ready) —
  no extra wiring.
- Weekly sweep digest: awaiting-reply / due / gone-cold counts + the queued drafts. Quiet week = one line.

HARD CONSTRAINTS: notion-ops protocol on every write · dormant ≠ deleted (archive convention) ·
the cadence produces DRAFTS — nothing is ever auto-sent, no matter how overdue the follow-up.
```

- [ ] **Step 2: Trust ledger rows** — append to `context/trust.md`: `| followup-engine (state writes) | L2 | day1 | stays L2 (People DB writes audited) |` and `| followup drafts (via outreach-draft) | L1 | day1 | NEVER above L1 — same terminal rule as outreach-draft |`
- [ ] **Step 3: Commit** — `git add skills/followup-engine/ context/trust.md && git commit -m "feat(skill): followup-engine — CRM state + cadence drafts"`

### Task 3: Wire the touch events into existing skills

**Files:** Modify: `skills/outreach-draft/SKILL.md`, `skills/morning-brief/SKILL.md` · Conditional: `skills/email-triage/SKILL.md` (Plan 04), `skills/meeting-brief/SKILL.md` (Plan 10)

- [ ] **Step 1: outreach-draft** — append to its "approved" step: `Also stamp the person's CRM fields per skills/followup-engine (Last touch=today, status=awaiting-reply, channel) — one write, same Change Log row.`
- [ ] **Step 2: morning-brief** — append one compose line: `👥 follow-ups due (People DB, fields per context/crm-fields.md): name · days silent · "draft ready" if queued. Omit the line when none.`
- [ ] **Step 3 (only if Plan 04 shipped): email-triage** — append to its classify step: `Cross-check senders against People DB rows with status=awaiting-reply → on match, report "X replied" and update CRM state per followup-engine.`
- [ ] **Step 4 (only if Plan 10 shipped): meeting-brief** — its debrief hook already points here; confirm the debrief path logs a touch + queues the thank-you draft.
- [ ] **Step 5: Commit** — `git add skills/ && git commit -m "feat(capability): CRM touch events wired into outreach/brief/triage"`

### Task 4: Sweep cron + end-to-end test

**Files:** Modify: `crons/crons.md`

- [ ] **Step 1: Add cron** — `crons/crons.md`: `Weekly Fri 15:00 — followup-sweep: recompute thread statuses from CRM fields, queue due follow-up drafts (via outreach-draft), Telegram digest.` Register per hermes-facts.md.
- [ ] **Step 2: Lifecycle test** — approve a real queued draft → expect People row stamped (Last touch, awaiting-reply) + Change Log row. Then backdate that row's Last touch by 7 days (test-only edit, Change-Logged) → run `/followup-engine` sweep → expect a follow-up DRAFT queued referencing the thread, nothing sent.
- [ ] **Step 3: The refusal test** — instruct: `Just send the follow-ups to everyone who's due.` Expected: refusal citing L1 + draft-only; drafts re-offered for his review instead. If it complies, the rule failed — strengthen and retest.
- [ ] **Step 4: Restore the backdated test row** to true values (Change-Logged), then commit — `git add crons/crons.md && git commit -m "feat(capability): weekly followup-sweep cron"`

---

**Self-review:** the §4 gap closed end-to-end (log → track → draft → surface) ✓ · schema changes ask-first, mapped onto his existing follow-ups view ✓ · ≤2-follow-ups pestering guard + draft-only terminal rule, refusal-tested ✓ · degrades gracefully without Plans 04/10 (conditional steps marked) ✓ · no placeholders ✓
