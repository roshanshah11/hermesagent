# Plan 07 — Capability: Recruiting Deadline Radar + Transfer Onboarding Tracker

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Nothing time-critical silently expires. Sophomore IB/quant openings get tracked in the IB Applications DB the day they appear; UChicago transfer logistics become dated tasks instead of unknown unknowns.

**Depends on:** Plan 01. **Why this matters:** his board has "Recruiting ramp → Oct 1" as ONE row — sophomore programs open absurdly early and a miss is unrecoverable.

---

### Task 1: Sources file

**Files:** Create: `context/recruiting-sources.md`

- [ ] **Step 1: Write the seed list** (Hermes extends it over time via the skill)

```markdown
# Recruiting sources Hermes watches (IB + adjacent; Roshan: skip quant-only unless he flips it)
## Banks — sophomore/insight/diversity programs + early-ID
Goldman Sachs · Morgan Stanley · JPMorgan · BofA · Citi · Evercore · Lazard · PJT · Centerview ·
Moelis · Jefferies · Houlihan Lokey — each firm's careers/students page + program pages.
## Aggregators / lists (cross-check, don't trust alone)
firm careers portals · university handshake board · public recruiting-timeline trackers found via search.
## Programs already known
Contrary Research Fellowship (Q3 cohort — row exists) · UChicago Financial Markets program (submitted).
## Per-run protocol
For each source: find programs open to sophomores (class of his year), capture: program · firm ·
opens · DEADLINE · link · eligibility. New/changed vs IB Applications DB = report + file.
```

- [ ] **Step 2: Commit** — `git add context/recruiting-sources.md && git commit -m "feat(capability): recruiting sources seed"`

### Task 2: `recruiting-radar` skill

**Files:** Create: `skills/recruiting-radar/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: recruiting-radar
description: Weekly watch on IB/finance sophomore recruiting — new openings and deadline changes → IB Applications DB + Telegram. A missed deadline is unrecoverable; precision matters more than volume.
version: 0.1.0
---
# Recruiting Radar
1. Work context/recruiting-sources.md (search + browser; firm pages are truth — aggregators only corroborate).
2. Diff against IB Applications DB (collection ea517e94-9463-44ed-a62c-2a9b9ce9a97c): new program →
   create row (program, firm, deadline, link, status=Researching) via notion-ops protocol; changed
   deadline → update row + flag loudly.
3. Verify every deadline ON THE FIRM'S OWN PAGE before writing it. Unverifiable → [verify] in the row,
   say so in the digest. A wrong deadline is worse than a missing one.
4. Telegram digest: 🆕 new (program · firm · deadline · eligibility · link) · ⏰ approaching
   (≤14 days) · changes. Quiet weeks: one line, no padding.
5. Deadlines ≤14 days out also surface in the morning brief (brief reads the same DB — no extra wiring).
```

- [ ] **Step 2: Cron** — `crons/crons.md`: `Weekly Tue 08:00 — recruiting-radar → Telegram.` Register.
- [ ] **Step 3: Test** — `/recruiting-radar` once. Expected: rows created with firm-page-verified deadlines, digest delivered; spot-check 2 deadlines manually.
- [ ] **Step 4: Commit** — `git add skills/recruiting-radar/ crons/crons.md && git commit -m "feat(skill): recruiting-radar"`

### Task 3: Transfer onboarding tracker (one-time build + weekly watch)

**Files:** Create: `skills/transfer-tracker/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: transfer-tracker
description: UChicago transfer-student onboarding logistics — research once, track weekly until autumn quarter starts. The blind spot: he tracks placement TESTS but not the logistics stack.
version: 0.1.0
---
# Transfer Tracker
SCOPE (deep-research once, then maintain): autumn course registration/bidding window + mechanics ·
transfer-credit evaluation/petition process + deadline · Core requirement mapping for transfers ·
adviser meeting requirement · housing deadlines · immunization/health-form deadline (registration
HOLD risk) · transfer orientation dates · anything else UChicago's transfer pages list.
1. BUILD (first run): research on official UChicago pages ONLY (college.uchicago.edu etc.); for each
   item create (a) a Course Plan DB row (collection 93b93826-79e1-44b5-a0a9-4131c9fbcd0d) and (b) a
   dated Tasks row if there's a deadline (notion-ops; Area=UChicago, Type=Deadline). Cite the page
   on every row; unverifiable dates → [verify] + ask Roshan to confirm against the student portal
   (some dates live behind login).
2. WATCH (weekly until quarter start): re-check pages for date changes; ⚠️ any change.
3. Telegram: the built list once; then weekly only-if-changed.
```

- [ ] **Step 2: Run the build** — `/transfer-tracker`. Expected: dated rows with citations; the ones behind the portal flagged for Roshan.
- [ ] **Step 3: Cron** — `Weekly Wed 08:00 — transfer-tracker watch.` Register.
- [ ] **Step 4: Commit** — `git add skills/transfer-tracker/ crons/crons.md && git commit -m "feat(skill): transfer-tracker"`

---

**Self-review:** firm-page verification rule (wrong deadline > missing) ✓ · feeds existing DBs (IB Apps, Course Plan) not new systems ✓ · portal-gated dates honestly flagged ✓ · no placeholders ✓
