# HERMES — MASTER PLAN (plan of plans)

> **Start here tomorrow.** This indexes the full planning corpus. Execute plans in order; each is
> self-contained per superpowers:executing-plans / subagent-driven-development.
> Spec (the contract): `../specs/2026-06-10-hermes-environment-pack-design.md`

## The corpus

| # | Plan | What it delivers | Depends on | When |
|---|------|------------------|------------|------|
| 01 | `01-core-environment-pack.md` | The working agent: install, NIM provider, Notion MCP, search+browser, Telegram, **7 core skills**, crons, setup.sh, Mac E2E acceptance, Linux deploy, runbook | — | **Day 1 (tomorrow)** |
| 02 | `02-harness-quality-gate.md` | The trust machine: quality rubric file, judge/redo mechanics, trust-dial ledger, weekly spot-audit | 01 | Day 1–2 (rubric ships with 01's skills; ledger after) |
| 03 | `03-harness-safety-ops.md` | Safety + operations hardening: secrets/incidents, snapshot-before-bulk, heartbeat/dead-man, backups, update cadence | 01 | Day 2 |
| 04 | `04-capability-email-calendar.md` | Email triage (read) + drafts (draft-only) + calendar proposals | 01, 02 | Week 1 |
| 05 | `05-capability-github-coding.md` | Coding agent: repo work → branch → tests → PR → Telegram link (internship scraper = first target) | 01 | Week 1 |
| 06 | `06-capability-markets-digest.md` | Daily markets digest + portfolio watch + Idea List feeder | 01, 02 | Week 1 |
| 07 | `07-capability-recruiting-transfer-radar.md` | Recruiting deadline radar (IB Apps DB) + UChicago transfer-onboarding tracker (Course Plan DB) | 01 | Week 1–2 |
| 08 | `08-capability-leadgen-errands.md` | $100/day lead-gen (GTM DB; blocked on Roshan's channel call) + errands + file-lookup + knowledge filing | 01, 02 | Week 2 / when unblocked |
| 09 | `09-self-learning-loop.md` | The growth engine: auto-generated-skill review → promote to repo, voice refinement, pattern memory | 01, 02 | Week 2, then continuous |
| 10 | `10-capability-meeting-briefs.md` | Pre-meeting briefs: tomorrow's calls/meetings → who · history · agenda · questions, cited (wrong fact in a live call > no brief) | 01, 02 (+04/11 enrich) | Week 2 |
| 11 | `11-capability-followup-engine.md` | People DB as living CRM: touch log, owed replies, cadence follow-up drafts (≤2, draft-only), gone-cold surfacing in the brief | 01, 02 (+04/10 enrich) | Week 2 |
| 12 | `12-capability-application-drafting.md` | Application drafting + compounding answer library (Contrary, FM program, clubs) — flags personal takes, NEVER submits | 01, 02, 07 | Week 1–2 (Contrary Q3 deadline-driven) |
| 13 | `13-cron-weekly-review-prep.md` | Sunday pre-filled weekly-review doc — slipped · week-ahead · relationships · research queue · Hermes's week | 01 (+02/06/07/11 light up sections) | Week 2 |
| 14 | `14-layered-compute-architecture.md` | **The $0 stack (ARCH — read with 01):** NIM Nemotron driver on the Compaq · ddgs + crawl4ai HTTP-only local search/extract (NO browser on the 2GB box) · heavy 20% dispatches via SSH to Claude Code on the Mac, best-effort with queue/degrade | 01 | Day 1–2, alongside 01 |

> Plans 10–13 added 2026-06-10 (same day, second pass): they close the four delegation-analysis §2/§4
> gaps — pre-meeting briefs, follow-up engine, application drafting + answer library, weekly-review prep.

> **Executor note:** the "REQUIRED SUB-SKILL: superpowers:executing-plans" header on every plan means
> *execute task-by-task with checkbox tracking and review gates* — that's the contract. Any equivalent
> plan-executor harness satisfies it (superpowers:subagent-driven-development, ecc:plan-orchestrate,
> claude-mem:do, ecc:prp-implement). Pick per session; don't mix executors mid-plan.

## Dependency shape

```
01 core ──► 02 quality gate ──► 04 email · 06 markets · 08 leadgen · 10 briefs · 11 follow-up · 12 applications
   │                 │
   ├──► 03 safety/ops└──► 09 self-learning (continuous)
   ├──► 05 github · 07 radar ──► 12 applications (radar feeds the rows it drafts against)
   └──► 13 weekly-review-prep (richer as 02/06/07/11 land)
soft edges: 04 ⇢ enriches 10+11 (email context/replies) · 10 debriefs ⇢ feed 11 · 11 state ⇢ feeds 13
```

## ⚖️ Skill-authoring philosophy (GOVERNS every plan in this corpus)

Three layers — author them differently:
1. **Harness (structural):** brain/provider, tools/MCP, browser, files/SSH, channels, scheduler,
   memory, and HOW skills+identity are governed (this repo = source of truth; trust ledger; drift
   guard). Build exactly as planned — this is the product.
2. **Rules (constitutional — fully prescriptive):** Control-DB check, Change Log, draft-only outward,
   quality rubric, injection guard, allowlists, payment gates. Never soften; never let the agent
   "optimize" these away.
3. **Task skills (intent contracts — deliberately light):** the pipeline SKILL.md bodies in these
   plans state WHAT the job is, the OUTPUT shape, and the HARD CONSTRAINTS. Where they enumerate
   numbered steps, those are an illustrative v0 default, NOT a locked procedure — the agent owns the
   HOW, may do it differently, and is expected to evolve its methods through Plan 09 (its own
   procedural memory). When authoring, trim any step that is method rather than contract.

Roshan's directive (2026-06-10): don't script the agent's behavior — build the structure that lets it
control its brain, its skills, its files, its everything, safely.

## Build order rationale
01 first because nothing exists without the runtime+hands. 02/03 immediately after because **autonomy
widens only as fast as the harness earns trust** (the spec's binding constraint) — the gate and the
audit must exist before capabilities multiply. Capabilities (04–08) are independent of each other —
parallelizable across sessions. 09 runs forever.

## Roshan's setup-time inputs (collected as plans hit them — none block planning)
NVIDIA key (build.nvidia.com) · Telegram bot token (@BotFather) · Brave search key · which email
account for 04 (gmail vs uchicago) + auth · holdings list for 06 · $100/day channel+pricing decision
for 08 · SSH to the box (he's setting up) · one-time browser logins (LinkedIn etc.) on the box ·
resume + past application text for 12's answer library (~10 min) · weekly-review slot for 13
(default Sun 16:00) · approval for any People DB schema additions 11 proposes.

## Definition of DONE for the whole project
From his phone, unprompted: 06:30 brief arrives daily · sourcing CSVs + People rows appear on request ·
dossiers file themselves with citations that survive spot-checks · drafts queue in his voice ·
kill switch verified weekly · Change Log shows every write · the agent's own skills grow and get
promoted through review. And the gap layer (10–13): every call comes pre-briefed the night before ·
no thread goes silently cold — follow-ups draft themselves on cadence · applications start from the
answer library, never from blank · Sunday's review doc is waiting before he sits down. Roshan's hours
go to learning, building, relationships — the grunt is gone.
