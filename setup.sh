#!/usr/bin/env bash
# Hermes Environment Pack — idempotent setup. Run from repo root. Safe to re-run.
#
# Usage: ./setup.sh [--dev]
#   --dev  Mac dry-run mode: use TELEGRAM_BOT_TOKEN_DEV (two-bot rule — the PROD
#          token lives ONLY on the box; Mac testing must never steal its updates).
#
# Verified against installed Hermes v0.16.0 — see docs/notes/hermes-facts.md:
#   secrets home = ~/.hermes/.env (upserted, not clobbered) · persona = ~/.hermes/SOUL.md ·
#   skills via skills.external_dirs (template) · telegram needs the [messaging] extra.
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HERMES_HOME="$HOME/.hermes"
DEV_MODE=0
[[ "${1:-}" == "--dev" ]] && DEV_MODE=1

echo "==> [1/8] repo .env check"
[[ -f "$REPO_DIR/.env" ]] || { echo "ERROR: cp .env.example .env and fill secrets first."; exit 1; }
set -a; source "$REPO_DIR/.env"; set +a
[[ -n "${NOTION_TOKEN_V2:-}" ]] || { echo "ERROR: NOTION_TOKEN_V2 empty in .env (MCP is dead without it)"; exit 1; }
[[ -n "${NVIDIA_API_KEY:-}" && "${NVIDIA_API_KEY}" != "nvapi-..." ]] || echo "WARN: NVIDIA_API_KEY empty — brain offline until set"
if [[ $DEV_MODE -eq 1 ]]; then
  TELEGRAM_TOKEN_EFFECTIVE="${TELEGRAM_BOT_TOKEN_DEV:-}"
  [[ -n "$TELEGRAM_TOKEN_EFFECTIVE" ]] || echo "WARN: --dev but TELEGRAM_BOT_TOKEN_DEV empty — gateway offline"
else
  TELEGRAM_TOKEN_EFFECTIVE="${TELEGRAM_BOT_TOKEN:-}"
  [[ -n "$TELEGRAM_TOKEN_EFFECTIVE" ]] || echo "WARN: TELEGRAM_BOT_TOKEN empty — gateway offline"
fi

echo "==> [2/8] Hermes install (skip if present)"
export PATH="$HOME/.local/bin:$PATH"
command -v hermes >/dev/null 2>&1 || curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes --version | head -1

echo "==> [3/8] Config: render template -> $HERMES_HOME/config.yaml (backup kept)"
[[ -f "$HERMES_HOME/config.yaml" ]] && cp "$HERMES_HOME/config.yaml" "$HERMES_HOME/config.yaml.bak.$(date +%s)"
python3 - "$REPO_DIR/config/config.template.yaml" "$HERMES_HOME/config.yaml" "$REPO_DIR" <<'PY'
import sys
tpl, out, repo = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(tpl).read().replace("/Users/roshanshah1/Downloads/hermesagent", repo)
open(out, "w").write(text)
print(f"    wrote {out}")
PY

echo "==> [4/8] Secrets: upsert into $HERMES_HOME/.env (never printed, never tracked)"
python3 - "$HERMES_HOME/.env" "$TELEGRAM_TOKEN_EFFECTIVE" <<'PY'
import os, sys
path, tg_token = sys.argv[1], sys.argv[2]
keys = {
    "NVIDIA_API_KEY": os.environ.get("NVIDIA_API_KEY", ""),
    "TELEGRAM_BOT_TOKEN": tg_token,
    "TELEGRAM_ALLOWED_USERS": os.environ.get("TELEGRAM_ALLOWED_USERS", ""),
    "TELEGRAM_HOME_CHANNEL": os.environ.get("TELEGRAM_HOME_CHANNEL", ""),
    "BRAVE_SEARCH_API_KEY": os.environ.get("BRAVE_SEARCH_API_KEY", ""),
    "OPENROUTER_API_KEY": os.environ.get("OPENROUTER_API_KEY", ""),
}
keys = {k: v for k, v in keys.items() if v and v != "nvapi-..."}
lines = open(path).readlines() if os.path.exists(path) else []
seen = set()
for i, line in enumerate(lines):
    for k, v in keys.items():
        if line.startswith(f"{k}=") or line.startswith(f"# {k}="):
            lines[i] = f"{k}={v}\n"; seen.add(k)
for k, v in keys.items():
    if k not in seen:
        lines.append(f"{k}={v}\n")
open(path, "w").write("".join(lines))
os.chmod(path, 0o600)
print(f"    upserted {sorted(keys)} -> {path}")
PY

echo "==> [5/8] MCP creds: write mcp/.env beside the server (gitignored)"
grep -E '^NOTION_' "$REPO_DIR/.env" > "$REPO_DIR/mcp/.env"
chmod 600 "$REPO_DIR/mcp/.env"

echo "==> [6/8] Telegram support: install [messaging] extra into the Hermes venv (idempotent)"
if [[ -d "$HERMES_HOME/hermes-agent" ]]; then
  "$HERMES_HOME/bin/uv" pip install --python "$HERMES_HOME/hermes-agent/venv/bin/python" -q \
    --directory "$HERMES_HOME/hermes-agent" '.[messaging]' \
    || "$HERMES_HOME/hermes-agent/venv/bin/python" -m pip install -q "python-telegram-bot[webhooks]==22.6"
  "$HERMES_HOME/hermes-agent/venv/bin/python" -c "import telegram" 2>/dev/null \
    && echo "    python-telegram-bot OK" || echo "    WARN: telegram lib missing"
fi

echo "==> [7/8] Persona: install context/HERMES.md -> $HERMES_HOME/SOUL.md (+ repo pointer)"
{ cat "$REPO_DIR/context/HERMES.md"; echo; echo "## Environment pack"; \
  echo "Your skills/config/context live in this git repo: $REPO_DIR"; \
  echo "(skills/ · context/notion-ids.md · context/voice/ · crons/crons.md). Repo is source of truth."; } \
  > "$HERMES_HOME/SOUL.md"

echo "==> [8/8] Pre-seed ddgs (search backend) in the Hermes venv"
# uv-created venvs ship without pip — use the managed uv against the venv python.
"$HERMES_HOME/bin/uv" pip install --python "$HERMES_HOME/hermes-agent/venv/bin/python" -q ddgs \
  && echo "    ddgs OK" || echo "    WARN: ddgs install failed (lazy-install will retry on first use)"

echo
echo "DONE. Next steps:"
echo "  1. hermes doctor                        # config + key sanity"
echo "  2. hermes gateway install && hermes gateway start   # background service (launchd/systemd)"
echo "  3. Message the bot, run /sethome in the chat        # cron delivery target"
echo "  4. Register crons: see crons/crons.md"
