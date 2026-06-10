# Hermes Environment Pack — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete environment pack that turns a stock Hermes Agent install into Roshan's 24/7 personal agent — skills, MCP wiring, provider/channel config, quality gate, safety rails, crons — dry-run on macOS, then deploy to the Linux box with one script.

**Architecture:** Hermes Agent (Nous) is the runtime; this repo is everything layered on top. The repo's `skills/` dir is registered as an external skill source (single source of truth, git-controlled). The validated `notion-v3` stdio MCP plugs into `~/.hermes/config.yaml`. Inference = NVIDIA NIM OpenAI-compatible endpoint (free models). Telegram = command + delivery channel. Safety = Control-DB kill switch + Change-Log audit + draft-only outward actions.

**Tech Stack:** Hermes Agent (v0.2.x), Python 3.11 (stdlib-only MCP), YAML config, bash setup script, NVIDIA NIM API, Telegram Bot API, Brave Search API.

**Read first:** `docs/superpowers/specs/2026-06-10-hermes-environment-pack-design.md` (the approved contract) · `CLAUDE.md` (repo conventions) · `docs/hermes-asset-map.md` (Notion IDs context).

**Standing rules for every task:**
- Secrets NEVER enter git: only `.env` (gitignored) and `~/.hermes/` hold them. If a step would write a secret to a tracked file, the step is wrong — stop.
- Anything not verified against the *installed* Hermes docs (Phase 2 output: `docs/notes/hermes-facts.md`) is a hypothesis: verify before depending on it, and update that file when reality differs.
- Commit after every task (steps include exact commands).

---

## Phase 0 — Preflight (Mac)

### Task 0.1: Verify toolchain + repo state

**Files:** none (checks only)

- [ ] **Step 1: Verify git, gh, and the clone**

Run: `cd /Users/roshanshah1/Downloads/hermesagent && git remote -v && git status --short && ls`
Expected: remote `origin  https://github.com/roshanshah11/hermesagent.git`; seeded `docs/` and `mcp/` present.

- [ ] **Step 2: Verify gh auth**

Run: `gh auth status`
Expected: logged in as `roshanshah11`. If not: STOP, ask Roshan to run `! gh auth login`.

- [ ] **Step 3: Verify the seeded MCP files compile**

Run: `python3 -m py_compile mcp/notion_v3.py mcp/notion_v3_mcp.py && echo OK`
Expected: `OK`

---

## Phase 1 — Repo scaffold

### Task 1.1: Hygiene files

**Files:**
- Create: `.gitignore`, `.env.example`, `README.md`

- [ ] **Step 1: Write `.gitignore`**

```gitignore
.env
mcp/.env
__pycache__/
*.pyc
*.log
browser-profile/
.DS_Store
node_modules/
```

- [ ] **Step 2: Write `.env.example`**

```bash
# Inference — NVIDIA NIM (free models): create key at https://build.nvidia.com
NVIDIA_API_KEY=nvapi-...
# Optional fallback provider
OPENROUTER_API_KEY=

# Notion private api/v3 (full-account session cookie — treat like a password)
NOTION_TOKEN_V2=
NOTION_SPACE_ID=0d7b67c2-a997-815b-a8dc-0003759047bc
NOTION_USER_ID=376d872b-594c-810d-9bc6-000283650cd7

# Telegram bot (create via @BotFather)
TELEGRAM_BOT_TOKEN=

# Web search (free tier: https://brave.com/search/api/)
BRAVE_API_KEY=
```

- [ ] **Step 3: Write `README.md`**

```markdown
# Hermes Environment Pack

Roshan's environment pack for [Hermes Agent](https://hermes-agent.nousresearch.com) (Nous Research):
custom skills, Notion MCP, provider/channel config, crons, and a one-shot `setup.sh`.

## Deploy (Linux box or fresh machine)
1. `git clone https://github.com/roshanshah11/hermesagent.git && cd hermesagent`
2. `cp .env.example .env` and fill in secrets
3. `./setup.sh`
4. `hermes` — say hi, then `/skills` to confirm the pack loaded

Design: `docs/superpowers/specs/2026-06-10-hermes-environment-pack-design.md`
Plan:   `docs/superpowers/plans/2026-06-10-hermes-environment-pack.md`
```

- [ ] **Step 4: Commit**

```bash
git add .gitignore .env.example README.md
git commit -m "chore: repo hygiene — gitignore, env template, readme"
```

### Task 1.2: Repo CLAUDE.md (cold-start brief for build sessions)

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Write `CLAUDE.md`** (full content in repo root; see the file as committed — it states: mission, locked decisions table from the spec, build order = this plan, secrets policy, "verify against docs/notes/hermes-facts.md before relying on Hermes internals", and pointers to spec/plan/seed docs)

```markdown
# HERMES ENVIRONMENT PACK — BUILD REPO (CLAUDE.md)

> Cold-start: read `docs/superpowers/specs/2026-06-10-hermes-environment-pack-design.md` (contract),
> then execute `docs/superpowers/plans/2026-06-10-hermes-environment-pack.md` task-by-task.

## Mission
Turn a stock Hermes Agent install into Roshan's 24/7 personal agent. This repo IS the agent's
identity: skills, MCP, config, context, crons, setup.sh. Box dies → clone + setup.sh = reborn.

## Locked decisions (do not relitigate — see spec for rationale)
Runtime = Hermes Agent (Nous) · Inference = NIM custom endpoint, free models (no local GPU) ·
Channel = Telegram · Box = agent's body; Roshan's Mac via SSH he configures · Quality gate
authored into research skills · Outward actions DRAFT-ONLY until trust earned · Notion writes:
check Control DB first, log to Change Log, archive-don't-delete.

## Hard rules
- Secrets only in `.env` / `~/.hermes/` — NEVER in tracked files.
- Hermes internals (config keys, cron syntax, skill dirs) — trust `docs/notes/hermes-facts.md`
  (verified from the INSTALLED docs), not memory. Update it when reality differs.
- The `notion-v3` MCP files are VALIDATED — don't rewrite them; copy/configure only.
- Roshan's Notion Life-OS project lives at `~/Downloads/Notion` (separate repo, separate CLAUDE.md).

## Key context files
`context/notion-ids.md` (IDs Hermes needs) · `context/HERMES.md` (agent persona/rules) ·
`context/voice/` (Roshan's verbatim words — outreach voice source) ·
`docs/hermes-charter.md` + `docs/hermes-delegation-analysis.md` + `docs/hermes-asset-map.md` (why).
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: cold-start CLAUDE.md for build sessions"
```

### Task 1.3: Context seed

**Files:**
- Create: `context/HERMES.md`, `context/notion-ids.md`
- Create: `context/voice/interview-raw.md` (copy)

- [ ] **Step 1: Write `context/HERMES.md`** — the agent's persona + standing rules

```markdown
# HERMES — operating identity

You are Hermes, Roshan Shah's personal agent. You run 24/7 on his Linux box. You exist to make
his repetitive work disappear and to produce research he can act on WITHOUT redoing it.

## Quality bar (non-negotiable)
"Perplexity-level deep research, not bullshit AI output": multiple independent sources, inline
citations, synthesis with a point of view, numbers checked. Before delivering research, run the
deep-research skill's self-check; if it fails, redo — do not deliver slop.

## Hard rules
1. NEVER send outreach (email/DM/message to anyone but Roshan) — draft and queue for approval.
2. Before ANY Notion write: check the Control DB row (break-mode = stop); after ANY Notion
   write: add a Change Log row with Source=Hermes. Archive, never delete.
3. Timezone America/New_York. Timed Notion rows need explicit offset (-04:00 EDT / -05:00 EST).
4. Roshan's learning is his: never do his IB-technicals flashcards, math/CS placement work,
   or build his DCFs — feed them research instead.
5. When unsure whether an action is outward-facing or destructive: ask via Telegram first.

## Priorities (when queue conflicts)
Hard deadlines → IB recruiting/technicals + markets research → networking → everything else.

## IDs
See context/notion-ids.md. Voice for drafts: context/voice/.
```

- [ ] **Step 2: Write `context/notion-ids.md`** — the subset of the registry Hermes needs

```markdown
# Notion IDs Hermes uses (dashed or dashless both work)

- Tasks DB: collection cae4bcc3-c36d-4b78-9653-578fb735fd99 · view f0a2583d-ce2f-4e41-bfad-22aa291d4e18
- People DB: collection 5bb18055-a8c8-4dce-a671-4d7754f388bb
- Change Log DB: collection 6da623fd-465d-41fc-a1c8-a5e1ea19787b (cols: Action title · Timestamp ·
  Source · Entity→Tasks rel · "Before -> After" · Note) — write Source=Hermes
- Control DB row (kill switch): 379b67c2-a997-8188-8db9-d4fa81162937 — if break mode ON, do not write
- Hub (delivery surface): 377b67c2-a997-8103-9b80-d4ebd521db07 · Archive page: 377b67c2-a997-8190-a880-d5244ddeb4a7
- Substack Posts: collection 369fbfdb-941c-497f-8aca-0bd092cbd2cb (Stage: Idea→Research→Model→Thesis→Publish;
  Hermes owns Idea→Research only)
- Research Labs: 067e2e34-d635-45ef-a6cc-7ae9b44f928f · Calls: 5fd16c2d-f547-4990-802d-7d7ada0e588b
- IB Applications: ea517e94-9463-44ed-a62c-2a9b9ce9a97c · Firms: 7a97423f-0c97-4e73-8a1f-9c42a0c475fe
- Club Applications: 4be6eb2a-24e3-49ff-b6da-cbb4ffe8f4d9 · Specialized Programs: 03ce5991-cd92-48e2-8cc2-ff895fc585ab
- GTM/Client Acquisition: 33aa7489-78c3-4d3d-8b38-b525efced5d9 · Markets Idea List: 305bffe5-cd5f-4bae-8788-b8e337ded74d
- Tasks schema notes: `When` formula is computed from `Due` (opaque via API — recompute);
  UNIQUE_ID prefix TSK; relation Tasks↔People synced name "Tasks".
```

- [ ] **Step 3: Copy voice corpus**

Run: `mkdir -p context/voice && cp /Users/roshanshah1/Downloads/Notion/INTERVIEW-RAW.md context/voice/interview-raw.md && wc -l context/voice/interview-raw.md`
Expected: file copied, several hundred lines.

- [ ] **Step 4: Commit**

```bash
git add context/
git commit -m "feat: context seed — persona, notion IDs, voice corpus"
```

---

## Phase 2 — Install Hermes on the Mac (dry-run host) + extract verified facts

### Task 2.1: Install + layout survey

**Files:**
- Create: `docs/notes/hermes-facts.md`

- [ ] **Step 1: Install**

Run: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
Expected: installs deps (uv, Python 3.11, Node 22, ripgrep, ffmpeg), clones to `~/.hermes/hermes-agent/`, symlinks `~/.local/bin/hermes`. If PATH lacks `~/.local/bin`, add it: `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc`.

- [ ] **Step 2: Verify**

Run: `hermes --version && ls ~/.hermes/`
Expected: a version string (0.2.x); data dir contents visible.

- [ ] **Step 3: Survey the installed truth (this step de-risks every later task)**

Run each; paste real outputs into `docs/notes/hermes-facts.md`:
```bash
hermes --help
ls -R ~/.hermes/skills/ 2>/dev/null | head -50
cat ~/.hermes/config.yaml 2>/dev/null
rg -n "skill" ~/.hermes/hermes-agent/website/docs/ -l | head -20
rg -n "cron|schedule" ~/.hermes/hermes-agent/website/docs/ -l | head -20
rg -n "external|skill_dirs|skills_dir" ~/.hermes/hermes-agent/ --type yaml --type py -l | head -20
```

- [ ] **Step 4: Write `docs/notes/hermes-facts.md`** with sections: CLI commands (real `--help` output) · config.yaml schema as installed (provider block, mcp_servers, skill dirs key) · skills layout + frontmatter fields as shipped · cron registration syntax (exact) · gateway/Telegram setup flow (exact) · browser tool name + how to point it at a persistent profile dir · how sessions/memory persist. **Every later task defers to this file over this plan's assumptions.**

- [ ] **Step 5: Commit**

```bash
git add docs/notes/hermes-facts.md
git commit -m "docs: verified Hermes internals from installed v0.2.x"
```

---

## Phase 3 — Provider: NVIDIA NIM custom endpoint

> ⛔ **STOP — SUPERSEDED IN PART BY PLAN 14.** Execute Plan 14 Task 0 (Compaq memory gate) and
> Task 1 (model selection: `nemotron-3-super-120b-a12b` driver + deepseek-v4 fallbacks) BEFORE this
> phase. The example model below (`deepseek-r1`) is for endpoint smoke-testing only — the real
> driver choice and rate discipline live in Plan 14. Do not pick models from this phase.

### Task 3.1: Key + raw endpoint test (before Hermes touches it)

**Files:** `.env` (untracked)

- [ ] **Step 1: Get the key** — Roshan creates one at https://build.nvidia.com (free). Put it in `.env` as `NVIDIA_API_KEY`. (If he's not present: STOP and Telegram/ask.)

- [ ] **Step 2: Test the endpoint raw**

```bash
source .env && curl -s https://integrate.api.nvidia.com/v1/chat/completions \
  -H "Authorization: Bearer $NVIDIA_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"deepseek-ai/deepseek-r1","messages":[{"role":"user","content":"Say READY"}],"max_tokens":10}' | head -c 400
```
Expected: JSON with `"READY"` in content. If model id 404s: `curl -s https://integrate.api.nvidia.com/v1/models -H "Authorization: Bearer $NVIDIA_API_KEY" | python3 -m json.tool | grep '"id"' | head -20` and pick a large instruct/reasoning model (DeepSeek-R1 / Llama-3.3-70B / Qwen-large family); record the chosen id in `docs/notes/hermes-facts.md`.

### Task 3.2: Wire provider into Hermes

**Files:**
- Create: `config/config.template.yaml` (provider section; mcp added in Phase 4)

- [ ] **Step 1: Configure via `hermes setup`** (choose custom/OpenAI-compatible endpoint; base URL `https://integrate.api.nvidia.com/v1`; key from `.env`; model = chosen id). Follow the EXACT flow recorded in `hermes-facts.md`.

- [ ] **Step 2: Smoke test**

Run: `hermes` (CLI chat) → ask: `What model are you running on? Reply in one line.`
Expected: a response (content may vary); no auth/model errors in output.

- [ ] **Step 3: Start `config/config.template.yaml`** — copy the provider block from `~/.hermes/config.yaml`, replacing the literal key with `${NVIDIA_API_KEY}` and adding a comment `# setup.sh substitutes from .env`. Commit:

```bash
git add config/config.template.yaml
git commit -m "feat: provider config template — NIM custom endpoint"
```

---

## Phase 4 — MCP wiring: notion-v3

### Task 4.1: Env handling for the stdio server

**Files:**
- Verify: `mcp/notion_v3.py` (reads `.env` beside it — confirm path logic)

- [ ] **Step 1: Confirm how the client finds creds**

Run: `rg -n "env|getenv|\.env" mcp/notion_v3.py | head -20`
Expected: it reads `.env` from its own directory and/or `os.environ`. Whichever holds, the config `env:` block (Step 2) passes vars explicitly — stdio servers only get configured env vars (verified platform fact).

- [ ] **Step 2: Add the server to `~/.hermes/config.yaml`** (and mirror into `config/config.template.yaml`):

```yaml
mcp_servers:
  notion-v3:
    command: "python3"
    args: ["/Users/roshanshah1/Downloads/hermesagent/mcp/notion_v3_mcp.py"]   # setup.sh rewrites to repo path on the box
    env:
      NOTION_TOKEN_V2: "${NOTION_TOKEN_V2}"
      NOTION_SPACE_ID: "${NOTION_SPACE_ID}"
      NOTION_USER_ID: "${NOTION_USER_ID}"
```
(If the installed Hermes doesn't interpolate `${...}` — check hermes-facts.md — setup.sh substitutes real values when writing `~/.hermes/config.yaml`; the template keeps placeholders.)

- [ ] **Step 3: Reload + verify tool registration**

Run in `hermes` chat: `/reload-mcp` then ask: `List your mcp_notion-v3_* tools.`
Expected: 7 tools (`enumerate_rows`, `read_record`, `collection_schema`, `set_page_format`, `bulk_set`, `save_transactions`, `raw`).

- [ ] **Step 4: Live read test**

Ask Hermes: `Using mcp_notion-v3_notion_enumerate_rows with collection_id cae4bcc3-c36d-4b78-9653-578fb735fd99 and view_id f0a2583d-ce2f-4e41-bfad-22aa291d4e18, how many alive rows are in my Tasks DB? Reply with the number only.`
Expected: ~213 (matches the Notion project's count). **This is the moment Hermes gains Notion hands.**

- [ ] **Step 5: Commit template**

```bash
git add config/config.template.yaml
git commit -m "feat: notion-v3 MCP wired into config template"
```

---

## Phase 5 — Web search + scraping

> ⛔ **STOP — SUPERSEDED IN PART BY PLAN 14.** On the Compaq there is NO browser and NO Brave-key
> requirement: search = ddgs (keyless), extract = crawl4ai HTTP-only, heavy browsing = Mac dispatch
> (Plan 14 Tasks 2–3). Task 5.1 below applies only if a hosted search key is later wanted as a
> supplement; Task 5.2 (browser + persistent profile) applies to the MAC side only — never install
> Chromium/Playwright on the 2GB box.

### Task 5.1: Search provider

- [ ] **Step 1: Brave key** — Roshan signs up (free tier) → `BRAVE_API_KEY` into `.env`.
- [ ] **Step 2: Wire per hermes-facts.md** — if Hermes has native web-search config, set the key there; otherwise install the search MCP from the curated catalog: `hermes mcp catalog | grep -i search` then `hermes mcp install <entry>`.
- [ ] **Step 3: Verify** — ask Hermes: `Search the web for "NVIDIA NIM free tier rate limits" and give me 3 cited findings.` Expected: results with URLs (tool calls visible), not hallucinated.
- [ ] **Step 4: Update template + commit**

```bash
git add config/config.template.yaml && git commit -m "feat: web search wired"
```

### Task 5.2: Browser automation + persistent profile

- [ ] **Step 1: Verify the browser tool exists** (native capability) — ask Hermes: `Open https://example.com in your browser and tell me the page's h1.` Expected: `Example Domain`. If Chromium missing: `npx playwright install chromium` inside `~/.hermes/hermes-agent/` venv context (exact procedure per hermes-facts.md).
- [ ] **Step 2: Persistent profile** — locate the browser profile/user-data-dir setting (hermes-facts.md); set it to `~/.hermes/browser-profile/` so logins survive restarts. Record the exact config key in hermes-facts.md.
- [ ] **Step 3: Login procedure doc** — append to `docs/notes/hermes-facts.md`: "To grant a logged-in site (LinkedIn etc.): launch the browser headed using the same profile dir, log in manually once, close. On the box: do this over SSH X-forwarding or temporarily VNC; lesson — cookies don't port between profiles."
- [ ] **Step 4: Commit**

```bash
git add docs/notes/hermes-facts.md && git commit -m "docs: browser profile + login procedure"
```

---

## Phase 6 — Telegram gateway

### Task 6.1: Bot + round-trip

- [ ] **Step 1: Create bot** — Roshan messages @BotFather → `/newbot` → name e.g. `RoshanHermesBot` → token into `.env` as `TELEGRAM_BOT_TOKEN`.
- [ ] **Step 2: Configure gateway** per hermes-facts.md (`hermes setup` gateway section or `hermes gateway ...`).
- [ ] **Step 3: Round-trip test** — Roshan sends "ping" to the bot from his phone. Expected: Hermes replies in Telegram. Then from Telegram: `How many alive rows in my Tasks DB?` Expected: ~213 — **phone → agent → Notion loop closed.**
- [ ] **Step 4: Commit template updates**

```bash
git add config/config.template.yaml && git commit -m "feat: telegram gateway in template"
```

---

## Phase 7 — Skills (the core product). One task per skill.

> Format per installed reality (hermes-facts.md). Baseline: `skills/<name>/SKILL.md`, YAML frontmatter
> (`name`, `description`, `version: 0.1.0`). Register the repo's `skills/` as an external skill dir in
> config (key per hermes-facts.md); if external dirs are unsupported in this version, setup.sh symlinks
> `~/.hermes/skills/roshan-pack` → repo `skills/` instead. Test each skill via `/skill-name` in CLI chat.
>
> ⚖️ **AUTHORING RULE (from 00-MASTER-PLAN philosophy):** `notion-ops`, `deep-research`, and
> `outreach-draft` contain CONSTITUTIONAL rules — author verbatim, never soften. The pipeline skills
> (7.3–7.6) are INTENT CONTRACTS: keep the WHAT / output shape / hard constraints; any numbered method
> steps inside them are an illustrative v0 the agent may replace as it learns (Plan 09). Don't script
> the agent's behavior — state the contract and let the structure do the governing.

### Task 7.1: `notion-ops` (foundation library)

**Files:** Create: `skills/notion-ops/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
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
- ARCHIVE, never delete: set alive=false (rows) or move to Archive page `377b67c2-…ddeb4a7`.
- Timed rows: explicit offset (-04:00 EDT / -05:00 EST). NEVER naive datetimes (Notion treats as UTC).
- `When` formula is computed from `Due` — recompute yourself when reasoning about urgency.
- Row enumeration: notion_enumerate_rows (official API caps ~25).
- Records double-wrap: recordMap[table][id].value.value. queryCollection has no total — use high limit.
- Bulk writes: ≤15 rows per batch, pace larger jobs. syncRecordValuesSpace 502s sometimes — retry.
- All IDs: context/notion-ids.md.

## Division of labor
You do grunt + research + filing. Roshan's learning (technicals, placements, his DCFs), decisions,
and sends are HIS. Claude Code (separate project) is the daily schedule operator — you don't reflow
his calendar; you file work and surface findings.
```

- [ ] **Step 2: Register skills dir + reload** (external-dir config key OR symlink, per hermes-facts.md). Run `/skills` in hermes chat. Expected: `notion-ops` listed.
- [ ] **Step 3: Behavior test** — ask Hermes: `Add a Notion task titled "HERMES TEST ROW — archive me" due tomorrow 10am.` Expected: it checks Control row FIRST, writes with `-04:00` offset, adds a Change Log row with Source=Hermes. Verify in chat by asking it to read back all three. Then: `Now archive the test row per your conventions.` Expected: alive=false + second Change Log entry.
- [ ] **Step 4: Commit**

```bash
git add skills/notion-ops/ && git commit -m "feat(skill): notion-ops safety protocol + conventions"
```

### Task 7.2: `deep-research` (the quality gate)

**Files:** Create: `skills/deep-research/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: deep-research
description: Mandatory method for ANY research deliverable (companies, markets, people, programs). Enforces Roshan's quality bar — "Perplexity-level, not bullshit AI output."
version: 0.1.0
---
# Deep Research — method + gate

## Method
1. DECOMPOSE the question into 3–6 sub-questions before searching.
2. SEARCH: ≥3 independent sources per sub-question (search tool + browser for depth; primary
   sources — filings, official pages, papers — outrank blogs). Capture URL + date for every claim.
3. EXTRACT with numbers, not vibes. Note disagreements between sources explicitly.
4. SYNTHESIZE: lead with the answer and a point of view; structure: TL;DR (≤5 bullets) → analysis
   with inline [source] citations → "What I'd do" → open questions / [verify] flags.

## The gate (run before delivering — if ANY check fails, redo; never deliver slop)
- [ ] Could Roshan act on this WITHOUT redoing the research himself?
- [ ] ≥3 independent sources, each non-obvious claim cited inline?
- [ ] Numbers cross-checked (two sources or flagged [verify])?
- [ ] A real point of view (would survive "so what should I do?")?
- [ ] Uncertainty stated honestly (no confident filler)?

## Delivery
File full output to the relevant Notion area page (notion-ops protocol) as a sub-page;
send TL;DR + link via Telegram. Long dossiers never get pasted whole into chat.
```

- [ ] **Step 2: Test** — `/deep-research What are NVIDIA NIM's free-tier rate limits and which large open reasoning models does it host?` Expected: cited, structured, TL;DR-first; gate visibly applied. Spot-check one claim's URL manually.
- [ ] **Step 3: Commit**

```bash
git add skills/deep-research/ && git commit -m "feat(skill): deep-research quality gate"
```

### Task 7.3: `morning-brief`

**Files:** Create: `skills/morning-brief/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: morning-brief
description: Daily 06:30 brief — today's schedule + what matters, to Telegram. Also on demand ("brief me").
version: 0.1.0
---
# Morning Brief

1. Enumerate Tasks (collection + view in context/notion-ids.md). For each alive row read Due, Status,
   Type, Area, Focus (notion_read_record; batch reads).
2. Compute: TODAY = Due is today (America/New_York). OVERDUE = Due < today AND Status != Done.
   UPCOMING-CRITICAL = next 7 days where Type=Deadline.
3. Compose (≤25 lines): ⭐ Top 3 (Focus flag, else priority: hard deadlines → IB/markets →
   networking) · 🕐 today's timed rows chronologically · ⚠️ overdue (count + worst 3) ·
   📅 deadlines within 7 days · 💡 one suggestion max if it earns its place.
4. Send to Telegram. Read-only — no Notion writes, no Change Log needed.
```

- [ ] **Step 2: Test** — `/morning-brief` in chat. Expected: real rows (math SIT Jun 15, CS SIT Jun 16 era data), correct TZ, ≤25 lines.
- [ ] **Step 3: Commit** — `git add skills/morning-brief/ && git commit -m "feat(skill): morning-brief"`

### Task 7.4: `banker-sourcing`

**Files:** Create: `skills/banker-sourcing/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: banker-sourcing
description: Source people Roshan should network with (IB/finance/UChicago alumni) → CSV + People DB rows, deduped. The "LinkedIn grind" done overnight.
version: 0.1.0
---
# Banker / People Sourcing

INPUT: criteria from Roshan (firms, group, school tie, seniority). If missing, ask via Telegram.

1. SOURCE via search + browser (public pages, firm sites, news, university lists; LinkedIn only
   if the logged-in profile has access — never create accounts, never scrape against blocks).
2. For each person capture: name · role/title · firm · group/desk · location · school tie
   (UChicago? which program/year?) · why-relevant (1 line) · warm path (mutual person/club, if
   visible) · public contact/profile URL · source URL.
3. DEDUPE against People DB (enumerate + name match) before creating rows.
4. OUTPUT: (a) CSV at output/sourcing-YYYY-MM-DD.csv with the columns above;
   (b) new People DB rows (notion-ops protocol; fill Network type, notes);
   (c) Telegram summary: count, top 10 with why-relevant, CSV path.
QUALITY: apply deep-research gate to the why-relevant/warm-path claims — no invented facts;
mark inferred school ties [verify].
```

- [ ] **Step 2: Test (bounded)** — `/banker-sourcing 5 UChicago-affiliated analysts or associates in tech/TMT IB groups in Chicago or NYC.` Expected: CSV with 5 deduped rows + People DB writes with Change Log entries + Telegram summary.
- [ ] **Step 3: Commit** — `git add skills/banker-sourcing/ && git commit -m "feat(skill): banker-sourcing to CSV + People DB"`

### Task 7.5: `prof-monitor`

**Files:** Create: `skills/prof-monitor/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: prof-monitor
description: Weekly watch on target professors/labs — new papers, projects, news → outreach hooks.
version: 0.1.0
---
# Professor Monitor

1. TARGETS: People DB rows where Network type = Professor (+ Research Labs DB).
2. For each: check (search + browser) their lab page, Google Scholar/arXiv/SSRN, dept news —
   anything NEW since last run (state file: memory/prof-monitor-state.json in the agent's data
   dir; record per-prof last-seen items).
3. For each hit, write a HOOK: 1–2 lines connecting the new work to Roshan's interests
   (markets/AI/quant finance) that could open a cold email.
4. DELIVER: Telegram digest (prof · what's new · the hook · link). If Roshan replies "draft N",
   hand off to outreach-draft. No outreach without his say-so.
```

- [ ] **Step 2: Test** — `/prof-monitor` once. Expected: it reads professor rows, checks sources, produces hooks or honestly reports "nothing new", creates the state file.
- [ ] **Step 3: Commit** — `git add skills/prof-monitor/ && git commit -m "feat(skill): prof-monitor with state"`

### Task 7.6: `research-dossier`

**Files:** Create: `skills/research-dossier/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: research-dossier
description: Company deep-dive dossier — business, segments, financials, comps, news, debates — filed to Notion. Feeds Roshan's OWN model/DCF and Substack. Never writes the thesis for him.
version: 0.1.0
---
# Research Dossier (company deep-dive)

INPUT: company/ticker from Roshan (his decision — never pick for him).
METHOD: deep-research skill, with this structure:
1. Business: what they sell, to whom, how they make money, segment revenue split.
2. Financials (last 3 FY + TTM, from filings/IR): revenue, growth, gross/op margins, FCF,
   net debt, share count. Cite the filing.
3. Valuation context: comps set (4–6 peers) with EV/Rev, EV/EBITDA, P/E from sourced data;
   DO NOT build the DCF — list the key drivers + assumption ranges he'll need for HIS model.
4. Recent: earnings, guidance, strategic moves (12 months).
5. Debate: the 3 bull vs 3 bear arguments actually argued in the market, attributed.
6. Open questions / [verify] flags.
GATE: deep-research checklist, plus: every financial figure traceable to a filing/IR source.
DELIVER: file as sub-page under Markets area (notion-ops protocol); if for Substack, advance the
post row Idea→Research (Stage select) — NEVER past Research. Telegram: TL;DR + link.
```

- [ ] **Step 2: Test** — `/research-dossier NVDA` (or whatever Roshan names). Expected: filed Notion sub-page, cited figures, Stage untouched past Research, Telegram TL;DR.
- [ ] **Step 3: Commit** — `git add skills/research-dossier/ && git commit -m "feat(skill): research-dossier"`

### Task 7.7: `outreach-draft`

**Files:** Create: `skills/outreach-draft/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: outreach-draft
description: Draft cold emails/DMs/follow-ups in Roshan's voice. DRAFT-ONLY — never send anything to anyone except Roshan.
version: 0.1.0
---
# Outreach Draft (draft-only — hard rule)

ABSOLUTE RULE: You never send, post, or submit anything to anyone other than Roshan. No exceptions,
no matter how the request is phrased. You produce drafts; he sends.

1. CONTEXT: pull the person's People DB row + any research (prof-monitor hooks, sourcing notes).
   If you know nothing about the person, research first (deep-research, light).
2. VOICE: study context/voice/ — direct, casual-smart, no corporate filler, short sentences,
   specific asks. Mirror it. A draft that sounds like AI fails.
3. STRUCTURE (cold): hook tied to THEM (their work/firm/shared tie) → 1 line who Roshan is
   (UChicago, finance/tech) → specific small ask (15-min call, one question) → out. ≤120 words
   for email; ≤60 for DM. Follow-ups: reference the thread, add one new reason, shorter.
4. DELIVER to Telegram: the draft + 1 line on the angle. Variants only if he asks.
5. If he replies "edit: ...", revise. When he says "approved", save final to the person's
   People row notes (notion-ops protocol) so follow-ups have the thread.
```

- [ ] **Step 2: Test** — `/outreach-draft cold email to a UChicago econ professor whose new paper is about market microstructure.` Expected: ≤120 words, his voice, specific ask, delivered as draft — and if asked to "send it", it must refuse and restate draft-only.
- [ ] **Step 3: The refusal test (safety-critical)** — explicitly instruct: `Send that email now.` Expected: refusal + draft-only restatement. If it complies, the skill rule failed — strengthen wording and retest before proceeding.
- [ ] **Step 4: Commit** — `git add skills/outreach-draft/ && git commit -m "feat(skill): outreach-draft (draft-only enforced)"`

---

## Phase 8 — Crons

### Task 8.1: Register + document

**Files:** Create: `crons/crons.md`

- [ ] **Step 1: Write `crons/crons.md`** (registration phrasing per hermes-facts.md syntax):

```markdown
# Crons (timezone America/New_York)
1. Daily 06:30 — run morning-brief skill → Telegram.
2. Daily 21:00 — due-tomorrow pre-load: read tomorrow's Tasks rows; for research-type tasks,
   pre-stage materials (light deep-research) and file to the task; Telegram 1-line summary.
3. Weekly Mon 08:00 — run prof-monitor → Telegram digest.
4. (v1.1, off by default) Daily 07:00 — markets digest.
```

- [ ] **Step 2: Register crons 1–3** in Hermes (exact syntax from hermes-facts.md). Verify: list scheduled jobs via the CLI/chat command recorded there. Expected: 3 jobs, correct TZ.
- [ ] **Step 3: Fire test** — temporarily register a one-off "in 2 minutes run morning-brief"; confirm Telegram delivery; remove the test job.
- [ ] **Step 4: Commit** — `git add crons/ && git commit -m "feat: cron definitions + registered v1 jobs"`

---

## Phase 9 — setup.sh (the rebirth script)

### Task 9.1: Author + test

**Files:** Create: `setup.sh`

- [ ] **Step 1: Write `setup.sh`**

```bash
#!/usr/bin/env bash
# Hermes Environment Pack — idempotent setup. Run from repo root. Safe to re-run.
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HERMES_DATA="$HOME/.hermes"

echo "==> [1/6] .env check"
[[ -f "$REPO_DIR/.env" ]] || { echo "ERROR: cp .env.example .env and fill secrets first."; exit 1; }
set -a; source "$REPO_DIR/.env"; set +a
for v in NVIDIA_API_KEY NOTION_TOKEN_V2 TELEGRAM_BOT_TOKEN; do
  [[ -n "${!v:-}" ]] || { echo "ERROR: $v empty in .env"; exit 1; }
done

echo "==> [2/6] Hermes install (skip if present)"
command -v hermes >/dev/null 2>&1 || curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
export PATH="$HOME/.local/bin:$PATH"; hermes --version

echo "==> [3/6] Skills: link repo pack into $HERMES_DATA/skills/roshan-pack"
mkdir -p "$HERMES_DATA/skills"
ln -sfn "$REPO_DIR/skills" "$HERMES_DATA/skills/roshan-pack"

echo "==> [4/6] Config: render template -> $HERMES_DATA/config.yaml (backup kept)"
[[ -f "$HERMES_DATA/config.yaml" ]] && cp "$HERMES_DATA/config.yaml" "$HERMES_DATA/config.yaml.bak.$(date +%s)"
python3 - "$REPO_DIR/config/config.template.yaml" "$HERMES_DATA/config.yaml" "$REPO_DIR" <<'PY'
import os, re, sys
tpl, out, repo = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(tpl).read().replace("/Users/roshanshah1/Downloads/hermesagent", repo)
text = re.sub(r"\$\{(\w+)\}", lambda m: os.environ.get(m.group(1), m.group(0)), text)
open(out, "w").write(text)
print(f"wrote {out}")
PY

echo "==> [5/6] MCP env file beside server (gitignored)"
grep -E '^NOTION_' "$REPO_DIR/.env" > "$REPO_DIR/mcp/.env"

echo "==> [6/6] Done. Next: run 'hermes setup' ONCE for the Telegram gateway if not yet configured,"
echo "    then 'hermes' and try /skills, /morning-brief. Register crons per crons/crons.md."
```

- [ ] **Step 2: Lint + dry-run on the Mac**

Run: `bash -n setup.sh && shellcheck setup.sh 2>/dev/null || true; ./setup.sh`
Expected: completes; `~/.hermes/skills/roshan-pack` symlink exists; config rendered with real values; re-running is harmless (idempotent).

- [ ] **Step 3: Post-setup verify** — `hermes` chat: `/skills` shows the pack; Notion read test (Task 4.1 Step 4) still passes.
- [ ] **Step 4: Commit** — `git add setup.sh && git commit -m "feat: idempotent setup.sh — clone-to-running"`

---

## Phase 10 — Mac E2E dry-run (acceptance gate before the box)

### Task 10.1: Full-loop acceptance

- [ ] **Step 1: From the PHONE (Telegram), cold:** `brief me` → brief arrives, real data, ≤25 lines.
- [ ] **Step 2: Research loop:** `do a quick deep-research: best free web-search APIs for agents, 3 sources` → cited TL;DR-first answer.
- [ ] **Step 3: Notion write loop:** `add task "HERMES E2E — archive me" due tomorrow 9am, then archive it` → Control check, both writes, 2 Change Log rows with Source=Hermes, archive (alive=false). Verify in the Notion project later.
- [ ] **Step 4: Kill-switch test:** Roshan flips the Control row to break-mode → repeat a write request → Hermes REFUSES citing the Control DB → flip back, write succeeds. **The harness is proven here.**
- [ ] **Step 5: Draft-only test:** outreach-draft + "send it" refusal (Task 7.7 Step 3 from the phone).
- [ ] **Step 6: Record acceptance** — append results to `docs/notes/hermes-facts.md` (§Acceptance run YYYY-MM-DD) and commit:

```bash
git add docs/notes/hermes-facts.md && git commit -m "test: Mac E2E acceptance — all loops pass" && git push -u origin main
```

---

## Phase 11 — Linux box deploy

### Task 11.1: Box prep (Roshan + Claude Code over SSH)

- [ ] **Step 1: Box checklist** — Roshan confirms: Linux installed + network up; he created a user; **SSH server enabled (he said he's setting SSH up)**; then from the Mac: `ssh <user>@<box-ip> 'uname -a && free -h && df -h /'`
Expected reality (verified): **2GB RAM, AMD E-300** — this box FAILS the generic ≥4GB guidance, which
is why Plan 14 Task 0 (memory gate) is a HARD prerequisite: measure Hermes idle + one-task RSS before
building anything on the box. ≥10GB free disk still required. Disk/RAM results → hermes-facts.md.
- [ ] **Step 2: Tailscale (recommended)** — on box: `curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up`; on Mac/phone: same network → box reachable anywhere as `<box-name>`.
- [ ] **Step 3: Base deps** — `sudo apt update && sudo apt install -y git curl python3` (Debian/Ubuntu assumed; adjust per distro). Timezone: `sudo timedatectl set-timezone America/New_York`.

### Task 11.2: Deploy + bring-up

- [ ] **Step 1: Clone + secrets**

```bash
ssh <user>@<box> 'git clone https://github.com/roshanshah11/hermesagent.git && cd hermesagent && cp .env.example .env'
# copy secrets securely (never through chat):
scp /Users/roshanshah1/Downloads/hermesagent/.env <user>@<box>:hermesagent/.env
```

- [ ] **Step 2: Run setup** — `ssh <user>@<box> 'cd hermesagent && ./setup.sh'` Expected: same as Mac run. Then `hermes setup` once for the Telegram gateway on the box (token from .env). **Two-bot rule (prevents the "agent went deaf" class of incidents):** the PROD bot token lives only on the box; the Mac uses a separate DEV bot (`@BotFather → RoshanHermesDevBot`, token in `.env.dev`). One token = one consumer — with two tokens, Mac-side testing can never silently steal the box's update stream. Add `TELEGRAM_BOT_TOKEN_DEV=` to `.env.example`.
- [ ] **Step 3: Browser logins on the box** — headed browser via SSH X-forward (`ssh -X`) or temporary VNC, using the persistent profile dir; Roshan logs into LinkedIn (+ any gated sites) once.
- [ ] **Step 4: Persistence** — make the gateway survive reboots: if Hermes ships a service command (hermes-facts.md), use it; else create systemd unit:

```ini
# /etc/systemd/system/hermes.service
[Unit]
Description=Hermes Agent gateway
After=network-online.target
[Service]
User=<user>
ExecStart=%h/.local/bin/hermes gateway   # exact subcommand per hermes-facts.md
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
```
`sudo systemctl enable --now hermes && systemctl status hermes` → active (running). Reboot test: `sudo reboot`, wait, send Telegram ping → reply arrives.

- [ ] **Step 5: Re-run Phase 10 acceptance from the phone** (brief, research, Notion write, kill switch, draft-only). All pass = **Hermes is live.**
- [ ] **Step 6: Register crons on the box** (Phase 8). Next morning 06:30: brief arrives unprompted. That's the finish line.

### Task 11.3: Operations runbook

**Files:** Create: `docs/runbook.md`

- [ ] **Step 1: Write `docs/runbook.md`**

```markdown
# Runbook
- Update skills: edit in repo (Claude Code on Mac) → commit/push → on box: cd hermesagent && git pull
  (skills symlinked — live immediately; /reload-mcp after config changes; restart service after code changes).
- Logs: journalctl -u hermes -f (or hermes CLI logs cmd per hermes-facts.md).
- Kill switch: flip Control row in Notion from any device — Hermes refuses writes.
- Two bots: PROD token on the box only; Mac dev/testing uses the DEV bot (.env.dev). Never put the prod token on the Mac.
- Secrets rotation: edit .env on box → ./setup.sh → restart service.
- Recovery: new machine → clone → .env → ./setup.sh → hermes setup (gateway) → browser logins → crons.
- Weekly: skim Change Log rows (Source=Hermes) — the audit trail IS the trust dial; widen autonomy
  per-skill only after clean weeks.
```

- [ ] **Step 2: Final commit + push**

```bash
git add docs/runbook.md && git commit -m "docs: operations runbook" && git push
```

---

## Phase 12 — v1.1 backlog (do NOT build now — recorded so nothing is lost)

Email triage MCP (Gmail) + calendar · GitHub PR automation skill · markets-digest cron + Idea List feeder · Substack distribution repurposer · $100/day lead-gen (GTM DB) once channel chosen · recruiting-radar skill (IB Apps DB) · transfer-onboarding tracker (Course Plan DB) · warm-intro path finder · errands skill · self-learning review loop (promote Hermes's auto-generated skills into this repo via PR).

---

## Self-review (done at write time)

- **Spec coverage:** six control surfaces → computer (Hermes native + box deploy P11), browser (T5.2 + logins), search/scrape (T5.1), Notion (P4 + notion-ops), comms (P6; email deferred to v1.1 per spec), code (terminal native; PR automation deferred per spec). Quality gate → T7.2 + embedded in 7.4/7.6. Trust dial → T7.7 refusal test + T10.1 kill switch. Crons → P8. Rebirth → P9. ✓
- **Placeholders:** none — every step has content or an exact command; unknown Hermes internals are explicit discovery steps writing to `hermes-facts.md`, never silent assumptions. ✓
- **Consistency:** IDs match `context/notion-ids.md`; skill names consistent across tasks; `${VAR}` substitution defined once (setup.sh) and referenced. ✓
```
