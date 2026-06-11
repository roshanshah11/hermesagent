# Plan 02 — Harness: Quality Gate & Trust Dial

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Make "Perplexity-grade or redo" mechanical, and make autonomy expansion a recorded, criteria-based process instead of a vibe.

**Architecture:** A rubric file every research skill must satisfy; a redo loop with a hard escalation limit; a per-skill trust ledger with explicit promotion criteria; a weekly human spot-audit that feeds the ledger.

**Depends on:** Plan 01 (skills exist; deep-research already embeds the gate inline — this plan extracts it into shared, versioned artifacts).

---

### Task 1: The rubric as a versioned artifact

**Files:** Create: `context/quality-rubric.md` · Modify: `skills/deep-research/SKILL.md` (point at it)

- [x] **Step 1: Write `context/quality-rubric.md`**

```markdown
# Quality Rubric (the gate — applied before ANY research deliverable ships)
Score each 0–2. Ship requires ≥9/10 AND no zero.
1. ACTIONABLE: Roshan can act without redoing the research. (0 = he'd have to re-research)
2. SOURCED: ≥3 independent sources; every non-obvious claim cited inline with URL. (0 = uncited claims)
3. NUMBERS: figures cross-checked across 2 sources or flagged [verify]. (0 = unchecked numbers)
4. POINT OF VIEW: a real "what I'd do / what this means", not a summary. (0 = book report)
5. HONESty: uncertainty stated; no confident filler; disagreements between sources surfaced. (0 = smooth slop)
FAIL → redo with the failing dimensions named. Max 2 redos, then deliver WITH a failure banner
("below bar because X — flagged, not hidden") via Telegram. Never silently ship a fail.
```

- [x] **Step 2: Edit `skills/deep-research/SKILL.md`** — replace its inline checklist section with: `## The gate\nApply context/quality-rubric.md verbatim (score all 5; ship ≥9/10, no zeros; max 2 redos then escalate with failure banner).`
- [ ] **Step 3: Test** — `/deep-research <small question>`; ask Hermes to show its rubric scoring. Expected: 5 scores + ship/redo decision visible.
- [x] **Step 4: Commit** — `git add context/quality-rubric.md skills/deep-research/ && git commit -m "feat(harness): quality rubric as versioned artifact"`

### Task 2: Trust-dial ledger

**Files:** Create: `context/trust.md`

- [x] **Step 1: Write `context/trust.md`**

```markdown
# Trust Ledger — autonomy level per skill (Hermes reads this; only Roshan changes levels)
Levels: L0 ask-first · L1 draft/queue for approval · L2 autonomous + Change Log audit · L3 autonomous
| Skill | Level | Since | Promotion criteria |
|---|---|---|---|
| morning-brief | L2 | day1 | L3 after 14 clean days (read-only anyway) |
| deep-research | L2 | day1 | L3 after 4 consecutive spot-audits ≥9/10 |
| research-dossier | L2 | day1 | stays L2 (writes to Notion — audit forever) |
| banker-sourcing | L2 | day1 | stays L2 (People DB writes audited) |
| prof-monitor | L2 | day1 | L3 after 4 clean weeks |
| outreach-draft | L1 | day1 | NEVER above L1 for sending; L1 is terminal by design |
| notion writes (any skill) | L2 | day1 | Control-check + Change Log forever |
| email-send (future) | L0 | — | L1 only after Roshan explicitly flips it here |
| purchases/payments (future) | L0 | — | terminal L0/L1 |
Promotion = Roshan edits this file (or tells Hermes via Telegram → Hermes edits + confirms diff).
Demotion = automatic after any safety violation: drop one level + Telegram alert.
```

- [x] **Step 2: Wire into persona** — append to `context/HERMES.md`: `Before any action, your autonomy level for it is defined in context/trust.md. Below L2 = queue, don't act.`
- [ ] **Step 3: Test** — ask Hermes: `What's your autonomy level for sending outreach? For filing a dossier?` Expected: L1/L2 with correct behavior described.
- [x] **Step 4: Commit** — `git add context/trust.md context/HERMES.md && git commit -m "feat(harness): trust-dial ledger"`

### Task 3: Weekly spot-audit loop

**Files:** Modify: `crons/crons.md`

- [x] **Step 1: Add cron** — `Weekly Sun 18:00 — spot-audit: pick the week's 2 most consequential deliverables (from Change Log Source=Hermes + filed dossiers), send Roshan each with its rubric self-scores and the prompt: "Grade these 1–10. Reply 'audit: N N'."` Register per hermes-facts.md syntax.
- [x] **Step 2: Closing the loop** — append to `crons/crons.md`: on `audit:` reply, Hermes records grades in `context/trust.md` history section and proposes promotions/demotions per criteria.
- [x] **Step 3: Commit** — `git add crons/crons.md && git commit -m "feat(harness): weekly spot-audit cron"`

### Task 4 (v1.1, optional): Second-model judge

- [ ] **Step 1:** When NIM key supports a second cheap model, add to `config/config.template.yaml` a `judge_model` note; deep-research gate then runs the rubric scoring through the judge model instead of self-scoring (self-grading inflates). Record decision in `docs/notes/hermes-facts.md`. Skip if single-model proves sufficient in spot-audits.

---

**Self-review:** rubric = spec's quality bar verbatim ✓ · escalation bounded (max 2 redos, banner) ✓ · ledger covers every v1 skill + future L0 surfaces ✓ · no placeholders ✓
