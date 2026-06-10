---
name: notion-ops
description: REQUIRED foundation for ANY write to Roshan's Notion — safety protocol, conventions, IDs. Load before any notion-v3 write tool call.
version: 0.1.0
---
# Notion Ops — conventions for Roshan's workspace

## Before ANY write (hard protocol)
1. Read Control row `379b67c2-a997-8188-8db9-d4fa81162937` (mcp_notion-v3_notion_read_record,
   table=block). If break-mode/paused is set: STOP, tell Roshan via Telegram, do nothing.
2. Make the write (bulk_set / save_transactions).
3. Append a Change Log row (collection 6da623fd-465d-41fc-a1c8-a5e1ea19787b): Action=what you did,
   Source="Hermes", Entity=related Task if any, "Before -> After"=old→new values, Note=why.

## Conventions (violations corrupt his system)
- ARCHIVE, never delete: set alive=false (rows) or move to Archive page `377b67c2-a997-8190-a880-d5244ddeb4a7`.
- Timed rows: explicit offset (-04:00 EDT / -05:00 EST). NEVER naive datetimes (Notion treats as UTC).
- `When` formula is computed from `Due` — recompute yourself when reasoning about urgency.
- Row enumeration: notion_enumerate_rows (official API caps ~25).
- Records double-wrap: recordMap[table][id].value.value. queryCollection has no total — use high limit.
- Bulk writes: ≤15 rows per batch, pace larger jobs. syncRecordValuesSpace 502s sometimes — retry.
- All IDs: context/notion-ids.md in the environment-pack repo.

## Division of labor
You do grunt + research + filing. Roshan's learning (technicals, placements, his DCFs), decisions,
and sends are HIS. Claude Code (separate project) is the daily schedule operator — you don't reflow
his calendar; you file work and surface findings.
