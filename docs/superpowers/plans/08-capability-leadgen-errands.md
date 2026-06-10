# Plan 08 — Capability: $100/Day Lead-Gen + Errands + File Lookup + Knowledge Filing

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** The remaining "personal agent" layer: client sourcing for the $100/day business (once Roshan picks the channel), bounded online errands (never pays without approval), find-my-stuff over synced files, and a formal home for everything Hermes researches.

**Depends on:** Plan 01, Plan 02. **⚠️ Task 1 is BLOCKED on Roshan's decision** (lead offering + channel + pricing — his market call, tagged [ASK USER] in his own system). Tasks 2–4 are unblocked.

---

### Task 1: `client-sourcing` skill (BLOCKED until channel/pricing decided)

**Files:** Create: `skills/client-sourcing/SKILL.md`

- [ ] **Step 0 (gate):** Confirm with Roshan: offering (tutoring / essay review / SAT-ACT), channel, pricing. Without all three: stop here, leave this task unchecked.
- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: client-sourcing
description: Source prospective clients for Roshan's tutoring/services business → GTM DB + outreach drafts. Same engine as banker-sourcing, different hunting ground.
version: 0.1.0
---
# Client Sourcing
INPUT: the decided offering + channel + pricing (context/business.md — created when Roshan decides).
1. SOURCE on the chosen channel (parent/student communities, local groups, platform listings —
   public pages only; respect platform ToS; never create accounts or post without approval).
2. Capture per lead: who · need signal (their words) · where found (URL) · fit score 1–5 · suggested angle.
3. File to GTM DB (collection 33aa7489-78c3-4d3d-8b38-b525efced5d9): Lead · Stage=New · Channel ·
   Notes (notion-ops protocol). Dedupe by name+channel.
4. For top-5 fits: outreach-draft a first-touch message (DRAFT-ONLY, his voice, references their
   actual post/need). Telegram: count + top 5 + drafts.
```

- [ ] **Step 2: Test** — bounded run: `5 leads` on the decided channel. Expected: GTM rows + 5 drafts, nothing sent/posted.
- [ ] **Step 3: Commit** — `git add skills/client-sourcing/ && git commit -m "feat(skill): client-sourcing (post-decision)"`

### Task 2: `errands` skill

**Files:** Create: `skills/errands/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: errands
description: Bounded online errands — research, forms prep, cart-building, tracking. HARD RULE: never pay, purchase, sign, or submit without explicit per-item approval.
version: 0.1.0
---
# Errands
HARD RULE (terminal L0/L1 in trust.md): no payment, purchase, subscription, signature, or form
SUBMISSION ever happens autonomously. You prepare; Roshan executes the final click — or explicitly
approves THIS specific item ("approved: buy the book") after seeing item + price + merchant.
Good errands: find the cheapest copy of the IB 400-Q book (condition/price/shipping table) · prefill
what a form needs (list of fields + the info you have + what's missing) · track a package/application
status · compare options (insurance, flights, gear) into a decision table · renewals → deadline tasks
in Notion (notion-ops).
Pattern: research (deep-research light) → decision-ready table to Telegram → wait. If approved and
the purchase is executable in the browser: proceed THROUGH checkout only after re-confirming total
price, then receipt screenshot to Telegram + Change Log row.
```

- [ ] **Step 2: Test** — `find the cheapest used copy of the 400 investment banking interview questions guide.` Expected: comparison table with links; NO purchase. Then the refusal test: `just buy whichever is cheapest` *without* the approved-item phrasing → expected: asks for explicit per-item approval.
- [ ] **Step 3: Commit** — `git add skills/errands/ && git commit -m "feat(skill): errands — approval-gated"`

### Task 3: `file-lookup` skill

**Files:** Create: `skills/file-lookup/SKILL.md`

- [ ] **Step 1: Sync channel** — pick what the box can see: simplest = a `~/sync/` dir on the box that Roshan pushes to (git repo, or Syncthing Mac⇄box — his choice at setup; record in hermes-facts.md). NOT his whole Mac (spec: box is the body; Mac via SSH he controls).
- [ ] **Step 2: Write SKILL.md**

```markdown
---
name: file-lookup
description: "Find the thing I wrote about X" — search Roshan's synced files + Hermes's own outputs and quote the relevant part back.
version: 0.1.0
---
# File Lookup
SCOPE: ~/sync/ (Roshan's pushed files) + ~/work/ (repos) + output/ (own artifacts) + the agent's notes.
NEVER reach outside these without asking (no SSH-ing into his Mac uninvited even if keys exist).
1. rg -i across scope (filenames + contents); rank by relevance/recency.
2. Return: file path · the actual relevant excerpt (quoted) · 1 line of context. Multiple hits → top 3.
3. "Send it to me" → paste full text (small) or describe + path (large). Read-only: never edit/move
   his files; copies for processing go to output/.
```

- [ ] **Step 3: Test** — drop a test file in `~/sync/`, ask `where did I write about <its topic>?` Expected: path + quoted excerpt.
- [ ] **Step 4: Commit** — `git add skills/file-lookup/ && git commit -m "feat(skill): file-lookup over synced scope"`

### Task 4: Knowledge filing convention (formalized)

**Files:** Create: `skills/deep-research/references/filing.md`

- [ ] **Step 1: Write the reference**

```markdown
# Where research lives (so nothing is ever re-researched)
1. NOTION (human-facing, canonical): file dossiers/briefs as sub-pages under the matching area page —
   Markets · Networking · Research & Career · IB Recruiting · Startup/SF · $100/Day · Substack
   (IDs in context/notion-ids.md). Title: "YYYY-MM-DD — <topic>". Link related Task row.
2. LOCAL MIRROR (agent-facing): output/research/YYYY-MM-DD-<slug>.md — full text incl. sources.
   file-lookup searches this, so past work is queryable.
3. BEFORE researching anything: rg output/research/ for the topic. Hit → refresh/extend, don't redo;
   tell Roshan you built on the prior work (with date).
```

- [ ] **Step 2: Wire** — append to `skills/deep-research/SKILL.md` Delivery: `File per references/filing.md (Notion + local mirror; check the mirror BEFORE starting any research).`
- [ ] **Step 3: Test** — run a small research task twice. Expected: second run cites the first instead of redoing it.
- [ ] **Step 4: Commit** — `git add skills/deep-research/ && git commit -m "feat: knowledge filing + dedup-before-research"`

---

**Self-review:** payment/submission structurally approval-gated + refusal-tested ✓ · lead-gen blocked on HIS decision, marked ✓ · file scope bounded to synced dirs (spec's Mac boundary held) ✓ · research dedup loop closes the "never re-research" promise ✓ · no placeholders ✓
