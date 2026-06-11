---
name: markets-digest
description: Daily markets pre-read — holdings/watchlist moves, material news, one worthwhile read, idea capture. Education-focused; NEVER trade advice presented as instruction.
version: 0.1.0
---
# Markets Digest

⛔ BLOCKED ON ROSHAN INPUT: holdings/watchlist (master plan §setup-time inputs). Targets live in
context/portfolio.md — he supplies tickers via Telegram. Until that file has rows, reply
"portfolio empty — send holdings/watchlist to start the digest" and stop.

JOB: 5-minute daily pre-read so Roshan gets smarter on markets without spending the hour —
overnight moves on his names, the news that actually matters, one read worth his time, candidate
ideas captured before they evaporate.

OUTPUT CONTRACT (≤20 lines, Telegram terse voice):
- 📊 moves: holdings + watchlist, day % and vs cost basis (quotes from the keyless price source
  recorded in docs/notes/hermes-facts.md)
- 📰 material news per name (earnings, guidance, M&A, regulatory — skip noise), every item cited;
  honest "nothing material" beats filler
- 📖 ONE read of the day for his level, primary-source preferred, +2 lines on why it's worth it
- 💡 ideas filed, if any — via idea-logging (Status=Raw; Roshan promotes, you never move stages)

HARD CONSTRAINTS: information + sources only — no advice framing ("you should buy") · any claim in
the digest meets the deep-research quality bar (cited or cut) · Notion writes ONLY through
idea-logging → notion-ops protocol · never invent a price — quote failed = say so.

HANDOFF: if Roshan replies "deep-dive <ticker>", invoke research-dossier with it — digest is the
scout, dossier is the dig (heavy-research dispatch as needed).

v0 default method (yours to improve): read context/portfolio.md → pull quotes (Stooq CSV pattern
in hermes-facts.md) → web_search each name for overnight material news → pick the read → compose,
send. Cron candidate: daily 07:00 (after the 06:30 brief — see crons/crons.md).
