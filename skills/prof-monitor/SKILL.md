---
name: prof-monitor
description: Weekly watch on target professors/labs — new papers, projects, news → outreach hooks.
version: 0.1.0
---
# Professor Monitor

JOB: watch the professors Roshan cares about; surface anything NEW with a hook he could open a
cold email with. Honest "nothing new" beats manufactured news.

TARGETS: People DB rows where Network type = Professor (+ Research Labs DB — IDs in
context/notion-ids.md).

OUTPUT CONTRACT: Telegram digest — prof · what's new · the hook (1–2 lines connecting the new work
to Roshan's interests: markets/AI/quant finance) · link. If Roshan replies "draft N", hand off to
outreach-draft. No outreach without his say-so.

STATE: keep per-prof last-seen items in memory/prof-monitor-state.json (agent data dir) so "new"
means new since last run — never re-alert the same item.

v0 default sources (yours to improve): lab page, Google Scholar/arXiv/SSRN, dept news via search +
extraction; deep checks needing real browsing escalate via heavy-research.
