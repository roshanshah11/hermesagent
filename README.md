# Hermes Environment Pack

Roshan's environment pack for [Hermes Agent](https://hermes-agent.nousresearch.com) (Nous Research):
custom skills, Notion MCP, provider/channel config, harness (quality gate + safety), crons, and a
one-shot `setup.sh`. The repo IS the agent's identity — box dies → clone + setup = reborn.

## Status
**Planning complete (2026-06-10). Build starts from `docs/superpowers/plans/00-MASTER-PLAN.md`.**

## The plan corpus
| Plan | Delivers |
|---|---|
| `00-MASTER-PLAN.md` | Index, build order, dependency map — **start here** |
| `01-core-environment-pack.md` | Install → NIM provider → Notion MCP → search/browser → Telegram → 7 core skills → crons → setup.sh → Mac E2E → Linux deploy |
| `02-harness-quality-gate.md` | Quality rubric, redo loop, trust-dial ledger, spot-audits |
| `03-harness-safety-ops.md` | Snapshots/undo, heartbeat, incidents, injection guard, backups |
| `04-…` – `08-…` | Capabilities: email/calendar · GitHub PRs · markets digest · recruiting+transfer radar · lead-gen/errands/files |
| `09-self-learning-loop.md` | Auto-skill promotion via PR, voice learning, drift guard |
| `10-…networking-completion…` | Pre-meeting briefs · follow-up engine · application library · review-prep cadence |

Spec (the contract): `docs/superpowers/specs/2026-06-10-hermes-environment-pack-design.md`
Background: `docs/hermes-charter.md` · `docs/hermes-delegation-analysis.md` · `docs/hermes-asset-map.md`

## Deploy (after the build)
1. `git clone https://github.com/roshanshah11/hermesagent.git && cd hermesagent`
2. `cp .env.example .env` and fill secrets
3. `./setup.sh`
4. `hermes` → `/skills` to confirm the pack loaded
