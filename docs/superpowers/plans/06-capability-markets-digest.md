# Plan 06 — Capability: Markets Digest + Portfolio Watch + Idea Feeder

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Daily pre-read so Roshan "gets smarter on markets" in 5 minutes instead of an hour: overnight moves on his holdings/watchlist, one worthwhile read, candidate ideas filed to the Markets Idea List DB as Raw.

**Depends on:** Plan 01, Plan 02 (rubric applies to any claim in the digest).

**Setup-time input:** Roshan's holdings + watchlist (he supplies tickers; this is his "start tracking your portfolio" task).

---

### Task 1: Portfolio file

**Files:** Create: `context/portfolio.md`

- [ ] **Step 1: Write the template** (Roshan fills via Telegram: "portfolio: AAPL 10 @ 180, ...")

```markdown
# Portfolio & Watchlist (Roshan edits via Telegram → Hermes updates this file + confirms diff)
## Holdings
| Ticker | Shares | Cost basis | Since |
|---|---|---|---|
## Watchlist (no position — interest only)
| Ticker | Why watching |
|---|---|
```

- [ ] **Step 2: Price source (free, keyless)** — primary: Stooq CSV, e.g. `curl -s "https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv"`. Verify it returns a quote row; record the working pattern (and a fallback found via search if Stooq fails) in `docs/notes/hermes-facts.md`.
- [ ] **Step 3: Commit** — `git add context/portfolio.md && git commit -m "feat(capability): portfolio file + price source"`

### Task 2: `markets-digest` skill

**Files:** Create: `skills/markets-digest/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: markets-digest
description: Daily markets pre-read — holdings/watchlist moves, one worthwhile read, idea capture to Notion. Education-focused; NEVER trade advice presented as instruction.
version: 0.1.0
---
# Markets Digest
1. PRICES: pull holdings + watchlist quotes (price source in hermes-facts.md). Compute day move %
   and vs cost basis.
2. NEWS: search each holding for material overnight news (earnings, guidance, M&A, regulatory) —
   skip noise; cite what you include.
3. ONE READ: pick the single best company/industry piece of the day for his level (learning-focused,
   primary-source preferred). One per day, with 2 lines on why it's worth his time.
4. IDEAS: if research surfaced a candidate worth tracking, file to Markets Idea List
   (collection 305bffe5-cd5f-4bae-8788-b8e337ded74d) as Status=Raw with a one-liner (notion-ops
   protocol). Roshan promotes; you never move stages.
5. DELIVER ≤20 lines to Telegram: 📊 moves table · 📰 material news (cited) · 📖 the read ·
   💡 ideas filed (if any). No advice framing ("you should buy") — information + sources only.
```

- [ ] **Step 2: Cron** — `crons/crons.md`: `Daily 07:00 — markets-digest → Telegram` (after 06:30 brief). Register.
- [ ] **Step 3: Test** — seed 2 tickers in portfolio.md → `/markets-digest`. Expected: real quotes, cited news or honest "nothing material", ≤20 lines.
- [ ] **Step 4: Commit** — `git add skills/markets-digest/ crons/crons.md && git commit -m "feat(skill): markets-digest + idea feeder"`

### Task 3: Dossier hand-off (closes the Substack loop)

- [ ] **Step 1:** Append to `skills/markets-digest/SKILL.md`: `If Roshan replies "deep-dive <ticker>", invoke research-dossier with it — digest is the scout, dossier is the dig.`
- [ ] **Step 2: Test** — reply `deep-dive <ticker>` to a digest. Expected: research-dossier runs, files to Notion, TL;DR back.
- [ ] **Step 3: Commit** — `git add skills/markets-digest/ && git commit -m "feat: digest→dossier handoff"`

---

**Self-review:** matches his "reading + portfolio tracking" tasks ✓ · Idea List feeds his Raw→promote flow, Hermes never promotes ✓ · no-advice framing explicit ✓ · keyless price source with verify step ✓ · no placeholders ✓
