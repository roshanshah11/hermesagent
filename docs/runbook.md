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

## Dead-man convention
No heartbeat by 07:30 = box/gateway down. Check: ssh box 'systemctl status hermes-gateway';
journalctl -u hermes-gateway -n 100; power/network. (Mac dry-run: hermes gateway status + launchctl.)

## Incidents
LEAKED SECRET → rotate immediately:
- NOTION_TOKEN_V2: log out that Notion session (Settings → My account → Devices) → grab fresh cookie → .env → ./setup.sh → restart
- NVIDIA_API_KEY: revoke + reissue at build.nvidia.com → .env → ./setup.sh → restart
- TELEGRAM_BOT_TOKEN: @BotFather /revoke → new token → .env → ./setup.sh → restart gateway
- BRAVE_SEARCH_API_KEY: dashboard reissue → .env → ./setup.sh
AGENT MISBEHAVING (bad writes): flip Control row (kill switch) FIRST → review Change Log Source=Hermes
→ rollback from output/snapshots/ → diagnose skill → demote in context/trust.md → fix → re-enable.
PROMPT-INJECTION SUSPECTED (web content steering the agent): kill switch → save the chat/session log
→ offending source goes on the skill's deny-list (persona Hard rule 6 is the standing guard).

## Backups (box)
Weekly: tar czf /tmp/hermes-data-$(date +%F).tgz -C $HOME .hermes --exclude=.hermes/hermes-agent
→ scp to the Mac when awake, else keep last 4 locally (crontab line at deploy). Sessions+memories
are the irreplaceable part; the repo lives on GitHub. Restore drill: untar to temp dir, confirm
sessions/ + memories/ present; full recovery = runbook Recovery + restore tar.

## Update cadence
Weekly: cd hermesagent && git pull (skills update live). Monthly: hermes update; then /skills +
one brief test before walking away. Record any CLI changes in hermes-facts.md.

## Weekly trust audit
Skim Change Log rows (Source=Hermes) — the audit trail IS the trust dial; widen autonomy
per-skill only after clean weeks. (Formalized in Plan 02.)

## Updates
`hermes update` updates the runtime. Run on the box only after it's been quiet on the Mac for a
few days (Plan 03 formalizes cadence + rollback via `hermes checkpoints`).
