# Capability map — Roshan's asks (2026-06-10) × plan corpus

Legend: ✅ live tonight · 📋 planned (plan #) · 🆕 new — needs a plan home · 🧪 sim-tested
> 2026-06-10 23:15 UPDATE: lanes A-F authored + merged 15 more skills (26 total in the pack, all
> registered). Every 📋 row below now has its SKILL.md shipped — remaining work per capability =
> its plan's discovery/wiring/test tasks + Roshan's ⛔ inputs. Sim suite 8/8.

## Daily rhythm
| Ask | Status | Home |
|---|---|---|
| Morning brief (news+calendar+due+priorities → Telegram pre-wake) | ✅🧪 (243s sim) — news/calendar enrich 📋 | live skill; enrich via 04 (calendar) + 06 (news) |
| Markets digest (moves, watchlist, filings, 2-3 ideas → Idea List) | 📋 | Plan 06 (needs his holdings/watchlist input) |
| End-of-day wrap (done/open/decisions) | ✅ shipped tonight (untested) | skills/eod-wrap; cron candidate 21:30 |
| Email triage pass | 📋 | Plan 04 (account+auth = his input) |
| Calendar prep (tomorrow's meetings, who/what/why) | 📋 | Plan 04 + Plan 10 |

## IB / finance recruiting
| Ask | Status | Home |
|---|---|---|
| Recruiting radar (careers pages, postings, deadline changes) | 📋 | Plan 07 |
| Application tracker maintenance (IB Apps DB, no dupes) | 📋 | Plan 07 |
| Application drafting (cover letters / why-this-firm) | 📋 | Plan 12 (needs his resume+past answers, ~10 min) |
| Deadline countdown + nudge | 📋 | Plan 07 (radar feeds it) |
| Networking/lead-gen (bankers/alumni, Mac-dispatched) | ✅ skill (banker-sourcing) — untested heavy path | live + Plan 08 widening |
| Cold outreach drafting (draft-only) | ✅🧪 (29s refusal PASS) | live skill |
| Follow-up engine (who/when, "5 days since X") | 📋 | Plan 11 |
| Coffee-chat prep brief | 📋 | Plan 10 |

## Markets / investing
| Ask | Status | Home |
|---|---|---|
| Single-name deep-dive (→ Mac/Claude heavy) | ✅ skills (research-dossier + heavy-research) — dispatch path untested until box | live; E2E at deploy |
| Filing monitor (8-K/10-Q watch, dedup, summarize) | 🆕 | propose Plan 06 addendum (EDGAR RSS poll, $0) |
| Earnings prep (expectations + last Q setup) | 🆕 | propose Plan 06 addendum |
| Idea logging (thesis → Idea List + invalidation) | 📋 | Plan 06 |
| Comps / model assist (build/update Excel comps or model tab) | 🆕 | needs design: openpyxl in venv (pre-seeded tonight) → agent writes output/*.xlsx from pulled data; NEVER touches his master models — separate proposal at brainstorm |

## Transfer / academic
| Ask | Status | Home |
|---|---|---|
| Transfer tracker (deadlines/requirements, flag changes) | 📋 | Plan 07 |
| Course planning (Course Plan DB, prereqs/conflicts) | 📋 | Plan 07 |
| Professor/opportunity monitor | ✅ skill (prof-monitor) 🧪 sim running | live |

## Coding / builder
| Ask | Status | Home |
|---|---|---|
| Coding PR (ticket → branch → PR, Mac-dispatched) | 📋 | Plan 05 |
| Repo monitor (CI fails, issues, stale branches) | 🆕 | propose Plan 05 addendum (gh CLI poll) |
| Build/script runner (backtest → results+plot) | 🆕 | propose Plan 05 addendum (code_execution + matplotlib) |

## Knowledge & self-management
| Ask | Status | Home |
|---|---|---|
| Research dossier (any topic → sourced one-pager) | ✅ skill 🧪 (research method PASS 175s) | live |
| File/info lookup (Notion + local) | 📋 | Plan 08 |
| Meeting briefs (person+company+context) | 📋 | Plan 10 |
| Errand handling (draft/stage, never submit) | 📋 | Plan 08 |
| Weekly review prep | 📋 | Plan 13 |
| Self-learning loop (notice ask → propose skill/cron) | 📋 — first live event already curated (agent-proposals/) | Plan 09 |

## Cross-cutting shipped tonight
- Telegram voice law (text-chat replies, no walls) → SOUL.md
- Response-time stack: reasoning low, compression discipline, hard stops, max_turns 40
- notion_raw excluded from agent toolset (endpoint-freelance guardrail)

## Brainstorm agenda (when Roshan returns — /interview-me + /brainstorming)
1. Excel/comps assist: scope v1 (which data sources, comps set shape, where files live, master-model
   boundary) — biggest genuinely-new build
2. Filing monitor + earnings prep: fold into Plan 06 or separate plan?
3. EOD wrap cron time (21:30 default) + what "needs your decision" should include
4. Repo monitor + script runner: which repos, which scripts
5. Markets digest inputs: holdings list, watchlist, idea-flow taste
6. Plan 02/03 scheduling (trust ledger + safety ops — next per master plan)
