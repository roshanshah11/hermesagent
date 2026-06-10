---
name: banker-sourcing
description: Source people Roshan should network with (IB/finance/UChicago alumni) → CSV + People DB rows, deduped. The "LinkedIn grind" done overnight.
version: 0.1.0
---
# Banker / People Sourcing

INPUT: criteria from Roshan (firms, group, school tie, seniority). If missing, ask via Telegram.

OUTPUT CONTRACT:
(a) CSV at output/sourcing-YYYY-MM-DD.csv — columns: name · role/title · firm · group/desk ·
    location · school tie (UChicago? program/year?) · why-relevant (1 line) · warm path (mutual
    person/club, if visible) · public contact/profile URL · source URL;
(b) new People DB rows, deduped against existing (notion-ops protocol; fill Network type, notes);
(c) Telegram summary: count, top 10 with why-relevant, CSV path.

HARD CONSTRAINTS:
- Public pages, firm sites, news, university lists. LinkedIn and anything needing real browsing
  runs through the heavy-research skill (Mac dispatch) — this box has no browser. Never create
  accounts; never scrape against blocks.
- DEDUPE against People DB (enumerate + name match) BEFORE creating rows.
- Quality gate (deep-research) applies to why-relevant/warm-path claims — no invented facts;
  inferred school ties marked [verify].
