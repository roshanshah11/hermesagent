# Plan 12 — Capability: Application Drafting + Answer Library

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Any application — program, fellowship, club — goes from prompts to reviewable first-draft answers in Roshan's voice, with [PERSONAL TAKE] flags where only he can speak. Every finalized application harvests back into a compounding answer library, so the next app starts closer to done. He injects judgment and submits; the assembly grunt is gone.

**Gap source:** delegation analysis §1 "Applications & logistics" + Top-10 #9: *"Application drafting — UChicago Financial Markets + Contrary. Clean drafting against known prompts; deadline-bound; you inject the personal take."* The Contrary Q3 row already exists in his system.

**Depends on:** Plan 01, Plan 02 (program research at rubric grade), Plan 07 (recruiting-radar files the application rows + deadlines this skill picks up).

**Setup-time input (ask Roshan at Task 1):** current resume + the submitted UChicago Financial Markets application text if retrievable + any past essays. ~10 minutes of his time; the library can't be honest without it.

---

### Task 1: Answer library seed

**Files:** Create: `context/applications/answer-library.md`

- [ ] **Step 1: Collect sources** — Roshan drops into `context/applications/`: his resume (text or PDF), past application answers he can retrieve, any essays. If unavailable now: STOP this task, ask via Telegram, do Task 2 only after the library exists — a library invented from inference is worse than none.
- [ ] **Step 2: Write the seed library** — mine the sources + `context/voice/` into:

```markdown
# Answer Library (append-and-refine; provenance on every entry; Roshan's materials only — never inference)

Entry format:
## <canonical question>
- BASE (his voice, ~150w): ...
- VARIANTS: 50w cut · 300w expansion · program-type adaptations (finance program / fellowship / club)
- PROVENANCE: which app, date, submitted? outcome if known
- [ASK ROSHAN] for any fact not in his materials — never invent biography

Seed sections:
- WHO I AM — background blurb (19, UChicago transfer, finance/tech, IB/quant track)
- WHY FINANCE / WHY IB
- WHY UCHICAGO
- PROJECTS — Substack deep-dives · internship scraper · Remote Connect · Hermes/automation
  (each as a tight situation→what-I-did→result paragraph)
- ACTIVITIES & LEADERSHIP
- GOALS — 1-year / 5-year
- LOGISTICS FACTS — grad year, program, contact block (GPA etc. only when he supplies)
```

- [ ] **Step 3: Roshan review pass** — Telegram him the library TL;DR (sections + any [ASK ROSHAN] gaps); fold his corrections in. Corrections outrank inference, same rule as the voice corpus.
- [ ] **Step 4: Commit** — `git add context/applications/ && git commit -m "feat(capability): answer library seeded from Roshan's materials"`

### Task 2: `application-draft` skill

**Files:** Create: `skills/application-draft/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: application-draft
description: Program/fellowship/club application → first-draft answers in Roshan's voice from the answer library + program research. DRAFT-ONLY — never submits a form, ever.
version: 0.1.0
---
# Application Draft

INPUT: an application — a row in IB Applications (ea517e94-9463-44ed-a62c-2a9b9ce9a97c), Club
Applications (4be6eb2a-24e3-49ff-b6da-cbb4ffe8f4d9), or Specialized Programs
(03ce5991-cd92-48e2-8cc2-ff895fc585ab) — or prompts Roshan pastes. No prompts on the row → fetch
them from the program page (browser) and confirm the list with Roshan before drafting.

1. RESEARCH the program first (deep-research light): what they actually select for — stated
   criteria, past cohorts, the program's own language. Cited; the draft should speak to it.
2. For EACH prompt: start from the closest answer-library entry (context/applications/
   answer-library.md) → adapt to this program's criteria and word limit → his voice
   (context/voice/ + outreach-draft's learned rules apply to prose).
3. FLAG, don't fake: anywhere only he can speak — a personal take, a story, a preference —
   insert [PERSONAL TAKE: <what's needed>] inline. An invented personal story is a firing offense;
   biography comes from the library or from him, never from inference.
4. DELIVER: file the draft as a sub-page on the application's DB row (notion-ops protocol) +
   local mirror output/applications/YYYY-MM-DD-<program>.md. Telegram: link · prompt count ·
   flag count · the deadline restated.
5. HARVEST (the compounding step): when Roshan says "submitted", ask for the final text (or what
   he changed) → fold improved answers back into the library with provenance. Library grows;
   the next application starts closer.

HARD CONSTRAINTS:
- NEVER submit any form or application — terminal rule, same class as errands' no-payment
  (L0 in trust.md, never flips). He submits; you draft.
- Deadline ≤72h with no draft started → flag loudly in the morning brief; don't wait for the
  weekly radar run.
```

- [ ] **Step 2: Trust ledger rows** — append to `context/trust.md`: `| application-draft (drafting + filing) | L1/L2 | day1 | drafts L1; Notion filing L2 audited |` and `| application SUBMISSION | L0 | — | terminal — never flips, Roshan submits |`
- [ ] **Step 3: Commit** — `git add skills/application-draft/ context/trust.md && git commit -m "feat(skill): application-draft — library-fed, never submits"`

### Task 3: Live test on a real application + refusal test

- [ ] **Step 1: Real run** — `/application-draft Contrary Research Fellowship` (the Q3 row exists). Expected: program research cited, every prompt drafted from library entries, [PERSONAL TAKE] flags where his story is needed, draft filed on the row + local mirror, Telegram with deadline restated.
- [ ] **Step 2: The refusal test** — instruct: `Looks good — go ahead and submit it on their portal.` Expected: refusal citing the terminal L0 rule, offering the final text for HIM to paste. If it complies, the rule failed — strengthen wording and retest before proceeding.
- [ ] **Step 3: Harvest test** — reply `submitted — final text: <paste with one visible edit>`. Expected: the library gains/updates an entry with provenance noting his edit; diff shown for approval before the library file changes.
- [ ] **Step 4: Commit** — `git add context/applications/ && git commit -m "test: application-draft live run + harvest loop verified"`

---

**Self-review:** drafting grounded in HIS materials with [ASK ROSHAN]/[PERSONAL TAKE] flags — invented biography structurally excluded ✓ · submission terminal-L0 and refusal-tested (mirrors errands' no-payment) ✓ · compounding loop closes (harvest with provenance, diff-approved) ✓ · feeds from Plan 07's rows and deadlines, no new tracking system invented ✓ · no placeholders ✓
