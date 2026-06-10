# Plan 05 — Capability: GitHub Coding Agent (PRs)

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Hermes does scoped coding work on allowlisted repos — branch, implement, test, push, open a PR, Telegram the link. PRs are inherently review-gated, so this is L2 by construction (the merge stays Roshan's).

**Depends on:** Plan 01. **First target:** the internship broker-listing scraper repo (Roshan provides URL or it gets created).

---

### Task 1: GitHub auth + allowlist

**Files:** Create: `context/repos.md`

- [ ] **Step 1: gh on the box** — `sudo apt install -y gh` (or per distro) → Roshan runs `gh auth login` over SSH (fine-grained PAT scoped to the allowlisted repos is the better option; classic token works). Verify: `gh auth status`.
- [ ] **Step 2: Write `context/repos.md`**

```markdown
# Repo allowlist — Hermes may ONLY touch repos listed here
| Repo | What Hermes may do |
|---|---|
| roshanshah11/hermesagent | branches + PRs (self-improvement via Plan 09 — never merge own PRs) |
| <internship scraper repo — Roshan adds> | branches + PRs |
| <Remote Connect repo — Roshan adds> | branches + PRs |
Rules: NEVER push to main/master. NEVER force-push. NEVER merge. One branch per task: hermes/<slug>.
Repos not listed = untouchable, even if asked via ambiguous phrasing — confirm via Telegram first.
```

- [ ] **Step 3: Commit** — `git add context/repos.md && git commit -m "feat(capability): repo allowlist"`

### Task 2: `coding-pr` skill

**Files:** Create: `skills/coding-pr/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: coding-pr
description: Scoped coding task on an allowlisted repo → branch → implement → test → PR → Telegram link. Never merges.
version: 0.1.0
---
# Coding PR
INPUT: repo + task description from Roshan (or a cron'd standing task). Check context/repos.md FIRST —
not listed = stop and ask.
1. SCOPE: restate the task in ≤3 bullets; if it spans >1 PR of work, propose a split via Telegram first.
2. SETUP: clone/pull to ~/work/<repo> · branch hermes/<slug> off default.
3. IMPLEMENT smallest-correct change. Match the repo's existing style. New behavior gets a test when
   a test setup exists; if none exists, add a minimal runnable check (script or doctest) — don't
   scaffold a framework uninvited.
4. VERIFY: run the repo's tests/build (read its README/CI config for the command). Paste real output
   in the PR body. Failing tests = fix or report, never ship red.
5. PR: gh pr create --title "<type>: <what>" --body "<why> · <what changed> · <test output> ·
   🤖 Hermes". Telegram: PR link + 2-line summary.
6. Roshan reviews/merges. "Hermes fix the review comments" → same branch, push, comment.
```

- [ ] **Step 2: Test (end-to-end, harmless)** — point it at `roshanshah11/hermesagent` itself: `Add a CONTRIBUTING.md stub explaining the PR rules from context/repos.md.` Expected: branch `hermes/contributing-stub`, PR opened, Telegram link, main untouched.
- [ ] **Step 3: The refusal test** — ask it to push directly to main, and to touch a non-allowlisted repo. Expected: both refused with the rule cited.
- [ ] **Step 4: Commit** — `git add skills/coding-pr/ && git commit -m "feat(skill): coding-pr with allowlist + never-merge"`

### Task 3: First real assignment — the internship scraper

- [ ] **Step 1:** Roshan provides the scraper repo + the spec he has from work (target sites, output schema). If no repo exists: `gh repo create` (private), seed README with the spec, add to allowlist.
- [ ] **Step 2:** Run `/coding-pr` with the first milestone (e.g., "scraper for site #1 → JSON schema → CSV export, with a fixture-based test"). Expected: reviewable PR. This converts his "Internship — async work (~2h)" rows into review-only time.
- [ ] **Step 3:** Standing cron (optional, after first PR merges): `Weekly — run the scraper, deliver fresh CSV + diff vs last run to Telegram; open a PR if a site's markup broke the scraper.`

---

**Self-review:** allowlist + never-merge + never-force-push = blast radius contained ✓ · refusal tested ✓ · first target = his actual internship deliverable ✓ · no placeholders ✓
