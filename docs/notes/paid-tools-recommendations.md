# Paid APIs & tools — where $0 holds, where money buys something real (2026-06-10)

Verdict up front: **the $0 stack survived a full build-and-test night.** Nothing below is required.
Ranked by leverage-per-dollar if you ever want to spend.

## $0 moves first (do these regardless)
1. **NIM 200 RPM bump — FREE, highest impact.** The drafted request is at
   docs/notes/nim-rpm-bump-request.md; file it at forums.developer.nvidia.com (2 min). The 40 RPM
   ceiling is the single biggest speed constraint we observed all night.
2. **Email = free**: Gmail app password (or UChicago SMTP) into EMAIL_* vars — unblocks email-triage
   with zero spend. Same for calendar v1 (calendar-propose runs calendar-free off Notion rhythm).
3. **Tavily or Exa free tiers (1k/mo each, key signup)** if web_extract quality ever hurts —
   ddgs+crawl4ai covered everything tonight.

## Where money buys real capability (ranked)
1. **~$5–10/mo OpenRouter credit — the resilience buy.** NIM is a free PREVIEW endpoint: we logged
   ReadTimeouts, broken pipes, and 150s stream walls all night. One OpenRouter key =
   (a) instant fallback brain when NIM flakes (fallback_providers slot exists),
   (b) Gemini Flash for auxiliary tasks (compression summaries, web_extract) off the NIM budget.
   If you spend on exactly one thing, this is it.
2. **Compaq insurance, $0–60 hardware.** The 2GB memory gate (Plan 14 Task 0) is untested and is
   the deploy's biggest risk. If it fails: a 4–8GB DDR3 stick (~$15–25 used) or a used mini-PC
   (~$50–80, e.g. older NUC/ThinkCentre) beats every software workaround. Decide only AFTER the
   gate measurement — don't pre-spend.
3. **Market data, only when Excel/comps gets serious.** Free EDGAR + yfinance carries filing-monitor,
   earnings-prep, digest v1. If comps tables need clean fundamentals at scale: Financial Modeling
   Prep (~$15/mo) or Polygon (~$30/mo). Skip until the Excel workflow exists and hurts.
4. **Anthropic API key (pay-per-use) — only if the Mac-asleep gap bites.** Heavy research currently
   rides your existing Claude Code (already paid) when the Mac is awake; the queue/degrade path
   covers sleep. If overnight deep-dives become daily, ~$5–20/mo of API in a headless worker closes
   it. Browserbase NOT recommended — the Mac + agent-browser already covers real browsing.
5. **Never needed**: paid Telegram (free covers everything) · Notion API tiers (private api/v3 is
   free) · paid cron/hosting (the Compaq IS the host) · search beyond free tiers at current volume.

## Decision rule
Spend only where a measured failure exists (NIM flake-rate, memory gate, extract quality) — every
line above maps to one. No measured failure → stay $0.
