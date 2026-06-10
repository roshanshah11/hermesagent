# Hermes facts — verified from the INSTALLED v0.16.0 (2026-06-10, macOS dry-run host)

> Source of truth for Hermes internals. Extracted from `hermes --help`, `~/.hermes/config.yaml`
> (generated template), and `~/.hermes/hermes-agent/website/docs/`. **Every plan task defers to
> this file over plan assumptions. Update it when reality differs.**

## Version / layout (differs from spec's "0.2.x" assumption)

- `hermes-agent==0.16.0` (2026.6.5), Python 3.11.15 venv, OpenAI SDK 2.24.0. `hermes update` self-updates.
- Code: `~/.hermes/hermes-agent/` · launcher: `~/.local/bin/hermes` (on PATH).
- Data dir `~/.hermes/`: `config.yaml` · `.env` (Hermes's own env file — THE secrets home) · `SOUL.md` ·
  `skills/` (73 bundled synced) · `cron/` · `sessions/` · `logs/` · `memories/` · `hooks/` · `pairing/` ·
  `bin/` (managed uv) · caches.
- Installer auto-installed uv + Python 3.11; found git/node/rg/ffmpeg already present.
- ⚠️ macOS: Playwright Chromium NOT auto-installed. If Hermes-side browsing is ever wanted on the Mac:
  `cd ~/.hermes/hermes-agent && npx playwright install chromium`. (Per Plan 14 the Compaq NEVER gets this.)

## CLI surface (v0.16.0 — much richer than spec assumed)

Top-level: `chat model fallback secrets migrate gateway proxy lsp setup postinstall whatsapp slack send
login logout auth status cron webhook portal kanban hooks doctor security dump debug backup checkpoints
import config pairing skills bundles plugins curator memory tools computer-use mcp sessions insights claw
version update uninstall acp profile completion dashboard desktop gui logs prompt-size`

Key flags: `hermes -z "PROMPT"` = headless one-shot (scriptable smoke tests) · `-m MODEL` · `--provider` ·
`-t TOOLSETS` · `--skills SKILLS` · `--yolo` (auto-approve) · `--resume/--continue`.
Useful ops: `hermes doctor` (config+deps check) · `hermes status` · `hermes backup` / `import` ·
`hermes send` (script→platform message) · `hermes logs` · `hermes config get/set/edit`.

## Provider: NVIDIA NIM is NATIVE (no custom-endpoint wiring needed)

- Provider id `nvidia` — reads `NVIDIA_API_KEY` from `~/.hermes/.env`. Docs' own example is our driver:
  ```yaml
  model:
    provider: "nvidia"
    default: "nvidia/nemotron-3-super-120b-a12b"   # "default" and "model" both work as key name
  ```
- `NVIDIA_BASE_URL` env overrides endpoint (default = build.nvidia.com cloud, OpenAI-compatible).
- Hermes auto-attaches the NIM billing-origin header.
- Fallbacks: top-level `fallback_providers:` list, each `{provider, model}` (custom: + `base_url`,
  `key_env`). Triggers on 429 (after retries), 5xx, timeouts. CLI: `hermes fallback add|list|remove`.
- Nous Portal = optional extra free brain (`hermes setup --portal`; `nvidia/nemotron-3-ultra:free` free
  Jun 4–18 promo). Keep as fallback if configured; never required.
- `agent.api_max_retries` (default 3) — lower to 1 for fast failover when fallbacks configured.

## Config schema (~/.hermes/config.yaml — generated from cli-config.yaml.example)

Top-level keys as shipped: `model terminal browser tool_loop_guardrails compression prompt_caching
memory session_reset max_concurrent_sessions group_sessions_per_user streaming skills agent
platform_toolsets stt code_execution delegation display updates` (+ `mcp_servers`, `fallback_providers`,
`bundles`, `auxiliary` documented). Env vars in `~/.hermes/.env` take precedence over config.yaml.

- `skills.external_dirs:` — list of extra skill dirs (~ and ${VAR} expanded). **Read-only; local
  `~/.hermes/skills/` wins name collisions; skill creation always writes local.** → register repo
  `skills/` here (no symlink needed).
- `skills.creation_nudge_interval: 15` — auto-skill-creation nudge every N tool iterations.
- `agent.max_turns: 60` default · `agent.reasoning_effort: "medium"` · `agent.gateway_timeout` (idle).
- `tool_loop_guardrails:` warnings on by default; `hard_stop_enabled: false` (opt-in circuit breaker
  for cron/autonomous sessions — Plan 03 material).
- `compression:` auto context compression ≥50% of context window (summaries via auxiliary model).
- `platform_toolsets:` per-platform tool control. Defaults: cli=hermes-cli (everything+cron mgmt),
  telegram=hermes-telegram (terminal,file,web,vision,image,tts,browser,skills,todo,cronjob,messaging).
  Custom lists supported, e.g. `telegram: [web, terminal, file, todo]`.
- `auxiliary:` per-task model overrides (web_extract, compression, vision…) — `{provider, model}`.

## MCP (reference/mcp-config-reference.md)

```yaml
mcp_servers:
  <name>:
    command: "..."   # stdio
    args: []
    env: {}          # stdio servers receive ONLY explicitly configured env vars
    # OR url: + headers: for HTTP; auth: oauth supported
    enabled: true
    timeout: 120
    connect_timeout: 60
    supports_parallel_tool_calls: false
    tools: {include: [], exclude: [], resources: true, prompts: true}
```
- `/reload-mcp` reloads from config (works in CLI AND gateway chats). `hermes mcp` CLI exists.
- Tool naming `mcp_<server>_<tool>` (spec fact; re-verify live after wiring notion-v3).

## Skills

- Layout: `~/.hermes/skills/<skill>/SKILL.md` or one category level `<category>/<skill>/SKILL.md`.
- Frontmatter observed (bundled yuanbao): `name, description, version, platforms: [linux, macos,
  windows], metadata: {hermes: {tags: [...], related_skills: []}}`.
- `/reload-skills` re-scans; `/skills` + `hermes skills` = registry search/install/audit/publish;
  `hermes bundles` = multi-skill aliases (`bundles:` config key); `hermes curator` = background skill
  maintenance (status/run/pause/pin).
- Cron jobs attach skills: `--skill NAME` (repeatable).

## Cron (user-guide/features/cron.md)

- `hermes cron create "SCHEDULE" "PROMPT" [--name N] [--deliver TARGET] [--skill S]... [--script
  ~/.hermes/scripts/x.sh] [--no-agent] [--workdir PATH] [--profile P] [--repeat N]`
- SCHEDULE: `30m` · `every 2h` · standard cron expr `0 9 * * *`. TZ: docs silent — ASSUME system local
  time; box gets `timedatectl set-timezone America/New_York` (Phase 11); verify with a test job.
- `--deliver`: `origin | local | telegram | discord | signal | platform:chat_id`. Telegram cron delivery
  honors `TELEGRAM_HOME_CHANNEL` (set via `/sethome` in chat or env).
- `--no-agent --script` = zero-LLM watchdog (stdout delivered verbatim; empty = silent) — heartbeat/
  disk-alert pattern for Plan 03.
- `--workdir` injects that dir's AGENTS.md/CLAUDE.md + uses it as cwd for terminal/file tools.
- Agent manages its own jobs via the `cronjob` tool in chat (natural language works). Cron-run sessions
  CANNOT create more crons (anti-runaway). Jobs run in fresh sessions with the normal tool list.
- Cron jobs use the `hermes model` provider — unattended runs need a non-interactive auth (API key, not
  OAuth-with-expiry; NIM key qualifies).

## Telegram gateway (user-guide/messaging/telegram.md)

- BotFather `/newbot` → token → `TELEGRAM_BOT_TOKEN` in `~/.hermes/.env`.
- `TELEGRAM_ALLOWED_USERS` = comma-separated numeric user IDs. **Default DENY** (`GATEWAY_ALLOW_ALL_USERS=false`)
  → need Roshan's numeric Telegram ID (get from @userinfobot or first-contact log line).
- `TELEGRAM_HOME_CHANNEL` (+ `_NAME`) = default chat for cron delivery; `/sethome` sets it from chat.
- Long-polling default (no public URL needed); webhook mode optional via `TELEGRAM_WEBHOOK_URL`.
- Run: `hermes gateway run` (foreground) · `hermes gateway install` → **launchd (macOS) / systemd (Linux)
  background service** · `start/stop/restart/status/list`. `hermes gateway setup` = interactive platform config.
- Group privacy mode: BotFather default ON (bot sees only /commands + replies + mentions) — fine for DM use.
- Voice notes auto-transcribe (local faster-whisper default, no key).

## Web search + extract (user-guide/features/web-search.md)

- Native model-callable tools: `web_search` + `web_extract`, backend per capability (split allowed).
- Backends: **DDGS — keyless, free, search-only (the Compaq default per Plan 14)** · SearXNG
  (`SEARXNG_URL`, self-hosted, search-only) · Brave free 2k q/mo (env is `BRAVE_SEARCH_API_KEY` — NOT
  `BRAVE_API_KEY` as our .env.example had) · Firecrawl (default extract, 500 credits/mo free) · Tavily
  1k/mo · Exa 1k/mo · Parallel/xAI paid.
- ddgs lazy-installs on first use (`pip install ddgs` to pre-seed).
- ⚠️ `web_extract` >5k chars pipes through the `web_extract` AUXILIARY MODEL (summary ~5k chars; >2M
  refused). Raw extraction needs browser snapshot (Mac) or our own crawl4ai MCP (Compaq) — relevant to
  Plan 14 Task 2 extract ladder.

## Browser

- Engine: agent-browser (Node) — local Chrome default; `AGENT_BROWSER_ENGINE=lightpanda` natively
  supported (auto-retries with Chrome on empty results!) · Browserbase cloud optional · Camofox
  (anti-detection Firefox) via `CAMOFOX_URL`.
- `browser.inactivity_timeout: 120` config; `BROWSER_SESSION_TIMEOUT=300` env.
- Persistent profile dir: no config key found yet in template/env — investigate `browser.md` +
  agent-browser flags WHEN the Mac-side browsing task needs it (Plan 14: browser = Mac side only).

## Memory / sessions / context files

- Memory: `~/.hermes/memories/MEMORY.md` (2,200 chars) + `USER.md` (1,375 chars), injected as frozen
  snapshot at session start; agent edits via `memory` tool. External providers (Honcho) optional.
- Sessions: `~/.hermes/sessions/`; trajectories `~/.hermes/logs/session_*.json`; `--resume/--continue`.
- Context files: **SOUL.md = global identity, ALWAYS loaded (slot #1), lives at `~/.hermes/SOUL.md`,
  loaded fresh each message (no restart)** → setup.sh installs our `context/HERMES.md` content there.
  Project context (first match wins, from CWD/git root): `.hermes.md`/`HERMES.md` → `AGENTS.md` →
  `CLAUDE.md` → `.cursorrules`. Cron `--workdir` triggers same injection.

## Corrections to plan assumptions (running list)

1. Version 0.16.0, not 0.2.x — CLI/config far richer; `hermes setup` optional (we write config directly).
2. NVIDIA NIM = native provider `nvidia`; no custom-endpoint block needed (Plan 01 Task 3.2 simplifies).
3. Secrets home = `~/.hermes/.env` (Hermes reads it natively; env > config.yaml). Repo `.env` stays the
   git-side source; setup.sh merges repo `.env` → `~/.hermes/.env`.
4. Persona home = `~/.hermes/SOUL.md` (not a skills hack) — context/HERMES.md content goes there.
5. External skills via `skills.external_dirs` config key — no symlink needed (plan's fallback unused).
6. Brave env var = `BRAVE_SEARCH_API_KEY` (plan/.env.example said `BRAVE_API_KEY`) — moot while DDGS
   (keyless) is the search backend.
7. DDGS search is NATIVE — Plan 14 Task 2's custom MCP shrinks to extract-only (crawl4ai), if needed at all.
8. Gateway persistence = `hermes gateway install` (launchd/systemd) — Plan 11's hand-rolled systemd unit
   likely unnecessary; verify on the box.
9. Headless testing = `hermes -z "prompt"` — E2E checks scriptable without interactive TUI.
10. Telegram allowlist (numeric ID) required by default — add `TELEGRAM_ALLOWED_USERS` to .env.example.
11. notion-v3 server reads creds from `mcp/.env` BESIDE ITSELF (`_load_env` in notion_v3.py) — the
    `mcp_servers.env:` block is unnecessary for it; setup.sh writes `mcp/.env`. Server validated
    standalone 2026-06-10: initialize ✓ · 7 tools listed ✓ · live enumerate (Tasks) = 209 rows ✓.
12. Telegram gateway needs the `messaging` extra (python-telegram-bot 22.6):
    `cd ~/.hermes/hermes-agent && uv pip install --python ./venv/bin/python '.[messaging]'`
    (installer does NOT include it). setup.sh must do this.
13. Config wants `_config_version: 29` top-level key (else doctor nags "v0 → v29 outdated").
14. `hermes doctor` lints vendor-prefixed model ids on provider=nvidia ("vendor-prefixed slugs belong
    to aggregators") — but providers.md's own NIM example uses `nvidia/nemotron-3-super-120b-a12b`.
    Treat the doctor warning as a false-positive lint until the live /v1/models check at key time.
15. Telegram config.yaml block: NOT needed (env-only). config.yaml `telegram:` exists only for
    proxy/local-bot-api extras; `platforms.telegram.extra` for large-file local server.
16. Extract ladder shipped as `mcp/extract_ladder_mcp.py` (runs under the HERMES VENV python —
    crawl4ai lives there; bare python3 would not see it). Validated on Mac 2026-06-10:
    example.com → tier 1 (165 chars) · docs.crawl4ai.com → tier 1 (13.5k chars) · LinkedIn →
    tier 3 escalate_heavy_research. Tier 2 activates only when LIGHTPANDA_CDP_URL is set
    (box probe at deploy). uv venvs have no pip — all venv installs go through
    `~/.hermes/bin/uv pip install --python <venv-python>`.
17. LIVE BRING-UP (2026-06-10, Mac, key active): /v1/models = 121 models, all three plan IDs exist
    verbatim (nvidia/nemotron-3-super-120b-a12b · deepseek-ai/deepseek-v4-flash · deepseek-ai/
    deepseek-v4-pro). Driver tool-calling VERIFIED raw (proper tool_calls + exact args + finish_reason=
    tool_calls — note: it correctly declines to invent missing required args; give IDs in prompt).
    Through Hermes: `hermes -z` chat ✓ · live MCP read = 209 Tasks rows ✓ · web_search via ddgs ✓.
    `timeout` cmd doesn't exist on macOS (GNU coreutils) — don't use in scripts meant for both hosts.
18. LIVE DEFECT FIXED (2026-06-10): Notion api/v3 throws transient 502 MemcachedCrossCellError
    (observed on syncRecordValuesSpace during the first notion-ops behavior test). notion_v3.py
    request() formerly raised SystemExit on any HTTPError — the MCP dispatcher's BaseException
    catch kept the server alive (by design), but the agent burned the turn. Patched: retry
    502/503/504 ×3 with backoff, then raise NotionHTTPError(Exception). CLI behavior unchanged
    except traceback-on-failure instead of clean exit.
19. FABRICATION INCIDENT + DISCRIMINATOR (2026-06-10): in behavior-test run 2 the agent created the
    task row correctly (recipe worked) but then REPORTED fake Change Log ids and a fake archive.
    Caught by independent readback. Discriminator: syncRecordValuesSpace 502 MemcachedCrossCellError
    that persists across retries = "record does not exist" (a random uuid 502s identically; real rows
    read fine). notion-ops protocol now has step 4: mandatory readback of every write; report only
    round-tripped ids; persistent-502-on-fresh-id = your write failed. Trust dial vindicated — keep
    write autonomy audited until clean weeks.
20. GATEWAY UX + APPROVALS (2026-06-10, live): dangerous-command approvals surface as Telegram
    buttons (once / session / always / deny) and BLOCK the run until tapped — Roshan's first brief
    sat 42 min on one. "always" = approved permanently (inherited by later sessions incl. cron), so
    interactive Phase-10 runs pre-clear the cron path. Feedback config shipped: streaming.enabled
    true (first-token message + progressive edits; final edit MarkdownV2), agent.gateway_notify_interval
    60 (default 180), display.platforms.telegram.cleanup_progress true. hooks_auto_accept relates to
    shell-script hooks only (separate system). subagent_auto_approve exists for subagent prompts.
