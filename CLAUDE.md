# HERMES ENVIRONMENT PACK — BUILD REPO (CLAUDE.md)

> Cold-start: read `docs/superpowers/specs/2026-06-10-hermes-environment-pack-design.md` (the approved contract),
> then `docs/superpowers/plans/00-MASTER-PLAN.md` (the plan-of-plans index) and execute the corpus in order,
> starting with `01-core-environment-pack.md` (superpowers:executing-plans or subagent-driven-development).

## Mission
Turn a stock **Hermes Agent** install (Nous Research — hermes-agent.nousresearch.com) into Roshan's
24/7 personal agent. This repo IS the agent's identity: skills, MCP, config, context, crons, setup.sh.
Box dies → `git clone` + `./setup.sh` = reborn.

## Locked decisions (do NOT relitigate — rationale in the spec)
- Runtime = Hermes Agent (not a custom loop, not LangGraph/Goose)
- Inference = NVIDIA NIM custom endpoint (`https://integrate.api.nvidia.com/v1`), free open models; OpenRouter fallback. No local inference (old box, no GPU)
- Channel = Telegram (bot via BotFather)
- The Linux box is the agent's body — full control THERE; Roshan's Mac only via SSH he configures himself
- Quality gate = authored into research skills ("Perplexity-level, not bullshit AI output" — multi-source, cited, synthesized, self-check → redo)
- Outward actions (outreach/email/posting) = DRAFT-ONLY until trust earned; reads/research/Notion-filing autonomous WITH audit
- Notion writes: check Control row FIRST (kill switch), Change Log row AFTER (Source=Hermes), archive-don't-delete, explicit TZ offsets

## Hard rules
- Secrets ONLY in `.env` / `~/.hermes/` — NEVER in tracked files. `.env.example` lists what's needed.
- Hermes internals (config keys, cron syntax, skills layout) — trust `docs/notes/hermes-facts.md`
  (extracted from the INSTALLED docs in plan Phase 2), not memory/assumptions. Update it when reality differs.
- `mcp/notion_v3*.py` are VALIDATED (built+tested 2026-06-08 in the Notion project) — configure, don't rewrite.
- Build + dry-run on this Mac first (Hermes supports macOS); deploy to the box only after Phase 10 acceptance passes.

## Key context
`context/HERMES.md` (agent persona + standing rules — becomes the agent's identity doc) ·
`context/notion-ids.md` (the Notion IDs Hermes needs) · `context/voice/` (Roshan's verbatim words — voice
source for outreach drafts) · `docs/hermes-charter.md` / `hermes-delegation-analysis.md` /
`hermes-asset-map.md` (the why — task analysis + capability charter + asset inventory).

## Who Roshan is (1 line)
19, UChicago transfer (finance/tech), IB/quant track; wants his repetitive layer fully agentic so his
hours go to learning, building, and relationships. Related project: `~/Downloads/Notion` (Life-OS,
separate repo — Claude Code remains the daily schedule operator there; Hermes files work, never reflows).
