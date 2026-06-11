---
name: earnings-prep
description: Pre-earnings brief for Roshan's names — confirmed date, last-quarter setup from the filings, free-sourced expectations, what to watch. Education-focused; never trade advice.
version: 0.1.0
---
# Earnings Prep

JOB: before any holding/watchlist name reports (targets: context/portfolio.md; empty = honest
no-op), Roshan walks in knowing the setup — date confirmed, last quarter's story, what the print
has to show.

OUTPUT CONTRACT (Telegram terse voice, ≤20 lines per name, the evening before it reports):
- 🗓 confirmed date/time + source (company IR / press release preferred)
- 📂 last-quarter setup: revenue/EPS/key segment numbers + the guidance given — pulled from the
  actual 10-Q/8-K press release; EVERY number cites the filing
- 🔮 expectations: free-sourced consensus, cited; none reliable → "[verify] no free consensus"
- 👀 what to watch: 3–5 specifics (guidance, segment, margin) grounded in the last filing
- honest empty: no names reporting soon = silence (cron) / "nothing upcoming" (on demand)

STATE: memory/earnings-prep-state.json — (ticker, event date) already prepped; never re-prep the
same event.

HARD CONSTRAINTS: $0 sources — EDGAR via the extract-ladder MCP tool + web_search; no paid data ·
this is a research output: deep-research gate before delivery · no advice framing — setup and
sources, never positioning · idea spawned → idea-logging (capture-only; Roshan promotes) · deeper
dig on request → research-dossier / heavy-research.

v0 default method (yours to improve): weekly scan for dates ~7 days out (web_search, confirm on
IR) → day before: pull last 10-Q / 8-K results release from EDGAR through the ladder, extract
numbers + guidance, search free consensus, compose, gate, send, update state.
