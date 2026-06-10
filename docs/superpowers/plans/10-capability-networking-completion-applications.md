# Plan 10 — Capability: Networking Completion + Application Library + Review Cadence

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Close the four audited gaps between the charter and the corpus: pre-meeting briefs (chartered as the single best networking feature), the follow-up engine (relationships stop going cold silently), application drafting with a reusable answer library, and the weekly-review-prep cron.

**Depends on:** Plan 01 (agent + skills live), Plan 02 (rubric/trust ledger). All four are L2-or-below; no new access needed.

**Authoring note (per 00-MASTER-PLAN philosophy):** SKILL.md bodies below are intent contracts — output shape + hard constraints; method steps are illustrative v0.

---

### Task 1: `pre-meeting-brief` skill

**Files:** Create: `skills/pre-meeting-brief/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: pre-meeting-brief
description: One-pager on a person before any call/coffee chat — background, recent work, talking points, the ask. Turns every conversation into a prepared one.
version: 0.1.0
---
# Pre-Meeting Brief
TRIGGER: Roshan asks ("brief me on X"), or a Calls DB row / call-type Task row is dated within 48h.
CONTRACT — the brief contains:
- Who: role, firm/group, path (school → roles), school tie if any
- Recent: what they've shipped/posted/been part of lately (cited — this is where deep-research-lite applies)
- Connection: how Roshan knows them / warm path / prior touches (People DB row + past Calls)
- 3 talking points tailored to THEM, not generic
- THE ASK: the one thing Roshan should leave with (suggest it; he decides)
- ≤1 page, Telegram-readable
FILING: attach as the Calls DB sub-page for that call (notion-ops protocol), linked to the person.
HARD RULE: facts about the person must be sourced or marked [unverified] — a wrong "fact" in a live
conversation is worse than a gap.
```

- [ ] **Step 2: Test** — `brief me on <a real person in the People DB>`. Expected: cited one-pager, filed to Calls, Telegram delivery.
- [ ] **Step 3: Commit** — `git add skills/pre-meeting-brief/ && git commit -m "feat(skill): pre-meeting-brief"`

### Task 2: `follow-up-engine` skill + cron

**Files:** Create: `skills/follow-up-engine/SKILL.md` · Modify: `crons/crons.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: follow-up-engine
description: Keeps the network warm — who owes/is owed a reply, who's gone cold, news triggers worth a touch. Surfaces; never sends.
version: 0.1.0
---
# Follow-Up Engine
CONTRACT (weekly + on demand):
1. LAST-TOUCH LEDGER: maintain per-person last-touch date + state (owed-by-them / owed-by-Roshan /
   dormant) in each People DB row's notes (notion-ops protocol). Sources: outreach-draft approvals,
   Calls rows, what Roshan tells you ("met Daniel today").
2. GONE-COLD: active relationships (anyone with outreach/calls in the last 90 days) silent >14 days
   → surface. Dormant-but-valuable (his call list) >45 days → suggest a re-touch angle.
3. NEWS TRIGGERS: light scan for the top ~10 active people — promotion/new role/published/firm news
   = a timely reason to reach out. Cite the trigger.
4. OUTPUT (Telegram, ≤15 lines): 🔴 owed by Roshan · 🟡 gone cold + suggested angle · 📰 triggers.
   "draft N" → outreach-draft takes over (draft-only as always).
HARD RULE: you surface and draft; Roshan sends. No exceptions inherited from outreach-draft.
```

- [ ] **Step 2: Cron** — `crons/crons.md`: `Weekly Fri 16:00 — follow-up-engine → Telegram` (before the weekend, when he has scraps to act). Register.
- [ ] **Step 3: Test** — `/follow-up-engine`. Expected: Daniel/Youti/Yoyo trio appear with correct owed/cold states from their task history; output ≤15 lines.
- [ ] **Step 4: Commit** — `git add skills/follow-up-engine/ crons/crons.md && git commit -m "feat(skill): follow-up-engine + weekly cron"`

### Task 3: Application library + `app-draft` skill

**Files:** Create: `context/answer-library.md`, `skills/app-draft/SKILL.md`

- [ ] **Step 1: Write `context/answer-library.md`** (seeded; grows with every application)

```markdown
# Answer Library (reusable application material — grows with every app he writes/approves)
## Core facts
UChicago transfer ('26) · finance/tech track · IB recruiting + markets/investing · builds: trading
research, Remote Connect, scraping platforms · tabla · golf · Schoolhouse tutoring proof.
## Canonical answers (append per prompt-type as they're written + approved)
### "Walk me through your background" — [to be seeded from his Fin-Markets app essay — ask Roshan
to drop it in context/voice/ or paste it]
### "Why finance/markets" — [seed from first approved draft]
### "Why this program/firm" — pattern: specific program feature → his concrete goal → proof he's
already acting on it. Never generic.
## Rules learned (append like outreach learned.md)
<!-- populated from his edits to app drafts -->
```

- [ ] **Step 2: Write `skills/app-draft/SKILL.md`**

```markdown
---
name: app-draft
description: First-draft applications (programs, fellowships, clubs) from the answer library + his background. He injects the personal take and submits — always.
version: 0.1.0
---
# App Draft
INPUT: the application prompts (he pastes or links) + deadline.
CONTRACT:
1. Pull from context/answer-library.md first — remix, don't regenerate; consistency across apps
   is the point. New prompt-type → draft fresh in his voice (context/voice/), then propose adding
   the approved version to the library.
2. Output per prompt: the draft + [PERSONAL] markers where only he can fill it (a real moment,
   a specific motivation) — never fabricate personal experiences.
3. Create the deadline Task row if none exists (notion-ops; Type=Deadline).
4. DRAFT-ONLY: never submit anything; final text goes to him via Telegram/file.
HARD RULE: no invented facts, activities, or experiences. The library is the truth source for claims.
```

- [ ] **Step 3: Test** — `draft the Contrary Research Fellowship application` (prompts findable; row `…810d-b6b3` exists). Expected: library-consistent drafts with [PERSONAL] markers, no fabrications, deadline row linked.
- [ ] **Step 4: Commit** — `git add context/answer-library.md skills/app-draft/ && git commit -m "feat(skill): app-draft + answer library"`

### Task 4: Weekly-review-prep cron

**Files:** Modify: `crons/crons.md`

- [ ] **Step 1: Add cron** — `Weekly Sun 17:00 — review-prep: assemble (a) what shipped this week (Change Log Source=Hermes + completed Tasks), (b) what slipped (rows that moved or went overdue), (c) next week's known deadlines, (d) proposed research queue for the week (dossiers/sourcing due), (e) the follow-up-engine's open items. ≤20 lines to Telegram BEFORE his weekly review block.` Register.
- [ ] **Step 2: Division-of-labor guard** — the prep FEEDS his review; it does not reschedule anything (calendar reflow belongs to the Notion-project operator). State this line inside the cron definition.
- [ ] **Step 3: Test** — dry-run `/review-prep`-style request once; verify ≤20 lines and no write operations beyond the digest.
- [ ] **Step 4: Commit** — `git add crons/crons.md && git commit -m "feat(cadence): weekly-review-prep cron"`

---

**Self-review:** all four audit gaps closed (pre-meeting briefs ✓ follow-up engine ✓ application drafting + library ✓ review-prep cadence ✓) · no new access surfaces · draft-only inheritance explicit twice · fabrication ban in app-draft (the one place an LLM lying is catastrophic) ✓ · no placeholders ✓
