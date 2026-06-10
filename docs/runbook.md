# Runbook (mechanics verified against Hermes v0.16.0 — hermes-facts.md)

## Update skills / config
Edit in repo (Claude Code on Mac) → commit/push → on box: `cd ~/hermesagent && git pull`.
- Skills: live immediately (external_dirs reads the repo); `/reload-skills` if mid-session.
- MCP changes: `/reload-mcp` (works in CLI and Telegram chats).
- config.template.yaml changes: `./setup.sh && hermes gateway restart`.

## Service (gateway = Telegram + cron scheduler)
- `hermes gateway status|start|stop|restart` · installed as systemd/launchd via `hermes gateway install`.
- Logs: `hermes logs` · trajectories in `~/.hermes/logs/session_*.json` · `journalctl -u` the unit on Linux.
- Health: `hermes doctor` · `hermes status`.

## Kill switch
Flip the Control row in Notion (any device) — notion-ops protocol makes Hermes refuse writes.
Verify weekly that it still refuses (Phase 10 Step 4 pattern).

## Two-bot rule
PROD bot token lives ONLY on the box. Mac dev/testing uses the DEV bot (`./setup.sh --dev` reads
TELEGRAM_BOT_TOKEN_DEV). Never run the prod token on two machines — the second consumer silently
steals the update stream ("agent went deaf").

## Secrets rotation
Edit repo `.env` on the box → `./setup.sh` (upserts `~/.hermes/.env` + `mcp/.env`) →
`hermes gateway restart`. NOTION_TOKEN_V2 is a session cookie — re-grab from browser devtools
when it dies; MCP errors with HTTP 401 are the symptom.

## Recovery (box dies)
New machine → clone repo → `cp .env.example .env` + fill (or restore from password manager) →
`./setup.sh` → `hermes gateway install && hermes gateway start` → message bot, `/sethome` →
register crons (crons/crons.md) → re-run Phase 10 acceptance. `hermes backup` zips `~/.hermes/`
(sessions/memories) — repo restores everything else.

## Weekly trust audit
Skim Change Log rows (Source=Hermes) — the audit trail IS the trust dial; widen autonomy
per-skill only after clean weeks. (Formalized in Plan 02.)

## Updates
`hermes update` updates the runtime. Run on the box only after it's been quiet on the Mac for a
few days (Plan 03 formalizes cadence + rollback via `hermes checkpoints`).
