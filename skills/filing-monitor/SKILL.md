---
name: filing-monitor
description: Watch SEC EDGAR for new 8-K/10-Q/10-K filings on Roshan's names — dedup, summarize, cite the filing. $0 sources only; honest empty when nothing filed.
version: 0.1.0
---
# Filing Monitor

JOB: Roshan never learns about a filing late. Watch his holdings + watchlist
(context/portfolio.md; empty file = honest no-op) for NEW EDGAR filings and say what each one
actually contains.

OUTPUT CONTRACT (Telegram terse voice, per new filing):
- ticker · form type · filed date · 2–4 line summary of what's IN it (8-K: the item that matters,
  not boilerplate; 10-Q/10-K: the deltas)
- citation = direct EDGAR document link + accession number — the summary cites the filing, always
- honest empty: nothing new = silence (cron) / "no new filings" (on demand) — never manufacture
- a filing worth tracking as a thesis → file via idea-logging (Status=Raw; Roshan promotes)

STATE: memory/filing-monitor-state.json — last-seen accession numbers per ticker. "New" means new
since last run; never re-alert the same accession.

HARD CONSTRAINTS: $0 sources only — EDGAR RSS/Atom + full-text search are keyless (send the SEC
fair-access User-Agent, respect rate limits) · summarize from the filing text itself via the
extract-ladder MCP tool, not from headlines (web_search = surrounding context only) · no advice
framing · analysis beyond the summary = deep-research gate; real depth → research-dossier /
heavy-research.

v0 default method (yours to improve): per ticker, pull EDGAR's per-company Atom feed (or
data.sec.gov submissions JSON) through the extract ladder → diff accessions vs state → fetch new
docs (ladder tier 1; escalate per ladder) → summarize, cite, send → update state.
Cron candidate: market days 08:00 + 17:30 (filings cluster pre-open and after the close).
