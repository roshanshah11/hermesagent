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

## Dependency shape

```
01 core ──► 02 quality gate ──► 04 email · 06 markets · 08 leadgen
   │                 │
   ├──► 03 safety/ops└──► 09 self-learning (continuous)
   └──► 05 github · 07 radar
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
for 08 · SSH to the box (he's setting up) · one-time browser logins (LinkedIn etc.) on the box.

## Definition of DONE for the whole project
From his phone, unprompted: 06:30 brief arrives daily · sourcing CSVs + People rows appear on request ·
dossiers file themselves with citations that survive spot-checks · drafts queue in his voice ·
kill switch verified weekly · Change Log shows every write · the agent's own skills grow and get
promoted through review. Roshan's hours go to learning, building, relationships — the grunt is gone.
