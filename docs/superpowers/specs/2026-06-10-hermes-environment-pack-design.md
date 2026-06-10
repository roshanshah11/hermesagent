# Hermes Environment Pack — Design (APPROVED 2026-06-10)

> Confirmed through interview with Roshan across 2026-06-09/10. This spec is the contract; the plan corpus in
> `docs/superpowers/plans/` implements it — start at `00-MASTER-PLAN.md`.

## Intent (the restate Roshan approved)

- **Outcome:** A 24/7 self-learning personal agent — **Hermes Agent by Nous Research** running on Roshan's old Linux box, free open models via **NVIDIA NIM custom endpoint** — that owns his repetitive work: deep research, people-sourcing, outreach drafts, monitoring, briefs, coding, errands. Reachable from his phone via **Telegram**.
- **User:** Roshan — so his real hours go to learning (IB technicals/math), building (DCFs, portfolio, code), and relationships.
- **Why now:** Too many things to do; open models finally good enough; the grunt layer of life should be agentic.
- **Success:** Output is deep, cited, and correct enough that he acts on it **without redoing it** — "Perplexity-level, not bullshit AI output." Morning brief lands daily; sourcing sheets fill; drafts queue in his voice.
- **Constraint:** **The harness is the gate** — autonomy widens only as fast as output quality earns trust. Draft-only for anything outward until proven. Free-tier inference.
- **Out of scope:** His learning (technicals, placements, building the DCFs himself), decisions, sends-without-approval (initially), his Mac as the agent's body (box only; SSH he sets up himself), and the live `/daily` reflow loop (stays with Claude Code in the Notion project).

## Capability surface — six control surfaces

1. **Its computer (the Linux box) — full control.** Terminal, filesystem, scripts, processes. The box IS its body; Roshan's Mac stays out of the blast radius (Decision: **A + SSH**, Roshan sets up SSH).
2. **A real browser — agentic browsing** (Perplexity-Comet style): navigate, click, fill, logged-in sessions. Requires a **persistent browser profile** on the box that Roshan logs into once (LinkedIn etc.). Lesson learned: fresh browsers hit login walls; cookies don't port.
3. **Web search + scraping** as distinct tools: search API (key required — no Nous Portal Tool Gateway), scraping for structured extraction, browser for depth.
4. **Workspaces:** Notion full read/write via the validated `notion-v3` MCP (private api/v3); CSV/sheet outputs; knowledge filing.
5. **Communications:** Telegram (command channel + delivery). Email/calendar = phase 2.
6. **Code:** repos, git, PRs (phase 2 for PR automation; terminal git from day 1).

**Cross-cutting:** 24/7 persistence · built-in natural-language cron + ad-hoc commands · native self-learning (auto-generated skills = procedural memory) · subagents · the quality gate · the trust dial.

## Platform facts (verified from official docs, 2026-06-10)

- Install: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` → code `~/.hermes/hermes-agent/`, data `~/.hermes/`, binary `~/.local/bin/hermes`. Auto-installs uv, Python 3.11, Node 22, ripgrep, ffmpeg. Only prereq: git. macOS + Linux + Windows.
- Config: `~/.hermes/config.yaml`. MCP servers under `mcp_servers:` (`command`/`args`/`env` for stdio). Tools exposed as `mcp_<server>_<tool>`. `/reload-mcp` refreshes. Stdio servers receive only explicitly configured env vars.
- Skills: `~/.hermes/skills/<category>/<skill>/SKILL.md` (YAML frontmatter: name, description, version; optional platforms, metadata/activation). agentskills.io standard. **External skill dirs configurable via config.yaml** → our repo's `skills/` can be the source of truth. Agent auto-generates skills via `skill_manage` after complex workflows.
- Models: providers = Nous Portal, OpenRouter, OpenAI, **any custom endpoint** → NIM OpenAI-compatible (`https://integrate.api.nvidia.com/v1`). `hermes setup` configures provider/gateways/tools.
- Cron: built-in natural-language scheduling, delivery to any platform. Channels: 20+ via gateway incl. Telegram.
- Security: command approval, container isolation, exec backends (local/Docker/SSH/Modal), subagents.
- Sources: hermes-agent.nousresearch.com (+ /docs/), github.com/NousResearch/hermes-agent.

## Decisions locked

| Decision | Choice |
|---|---|
| Runtime/harness | Hermes Agent (Nous) — not custom loop, not LangGraph/Goose |
| Inference | Hosted free open models, NIM custom endpoint; OpenRouter fallback. No local inference (old box, no GPU) |
| Channel | Telegram primary; email delivery later |
| Computer scope | Linux box = its body, full control there; Mac via SSH Roshan configures |
| Source of truth | This repo (`roshanshah11/hermesagent`) = environment pack: skills, MCP, config, context, setup.sh. Box dies → clone + setup.sh = reborn |
| Build flow | Build + dry-run on Mac with Claude Code → `git clone` + `./setup.sh` on box. Claude Code = mechanic; Hermes = operator |
| Quality gate | NOT native — authored into every research skill: multi-source, citations, synthesis with a point of view, self-check rubric, redo loop |
| Trust dial | Draft-only for outward actions (outreach/email); autonomous for read/research/Notion-filing WITH Change Log audit + Control DB kill switch |
| Notion coordination | Hermes writes Change Log rows with `Source=Hermes`; checks Control DB row before write ops; archive-don't-delete; Claude Code (Notion project) remains the daily operator |

## Skills v1 (authored by us; agent grows its own on top)

| Skill | Job | Autonomy |
|---|---|---|
| `notion-ops` | Conventions foundation: tz offsets, recompute `When` from `Due`, archive-don't-delete, Change Log write-before-write, Control DB check, ID registry | n/a (library) |
| `deep-research` | The quality gate as method: multi-source, cited, synthesized, self-check rubric → redo | autonomous |
| `morning-brief` | Tasks DB (Today + deadlines) → Telegram brief | autonomous |
| `banker-sourcing` | Target criteria → browser/web grind → CSV + People DB rows, deduped | autonomous (writes audited) |
| `prof-monitor` | Target profs → new output → outreach hook alert | autonomous |
| `research-dossier` | Company deep-dive (filings/comps/news) → dossier filed to Notion; feeds Roshan's DCF + Substack | autonomous (filing audited) |
| `outreach-draft` | Drafts in Roshan's voice (corpus in `context/voice/`) → queued for approval. **NEVER auto-send** | draft-only, hard rule |

## Crons v1

| Job | Schedule (America/New_York) | Delivery |
|---|---|---|
| morning-brief | daily ~06:30 | Telegram |
| due-tomorrow pre-load | daily ~21:00 | Telegram |
| prof-monitor | weekly Mon ~08:00 | Telegram |
| markets-digest | daily ~07:00 (v1.1, optional) | Telegram |

## Repo layout

```
hermesagent/
├── CLAUDE.md                  # cold-start brief for build sessions
├── README.md
├── .env.example               # NVIDIA_API_KEY, NOTION_TOKEN_V2, NOTION_SPACE_ID, NOTION_USER_ID, TELEGRAM_BOT_TOKEN, BRAVE_API_KEY
├── .gitignore                 # .env, browser-profile/, __pycache__, *.log
├── setup.sh                   # idempotent: install hermes → merge config → register skills dir → prompt secrets
├── skills/<name>/SKILL.md     # the 7 authored skills (+ references/ as needed)
├── mcp/notion_v3.py, notion_v3_mcp.py   # validated, stdlib-only; reads .env beside it
├── config/config.template.yaml # provider + mcp_servers + skill dirs (no secrets)
├── context/                   # HERMES.md persona/rules · notion-ids.md · operating-model excerpt · voice/ corpus
├── crons/crons.md             # jobs to register + exact phrasing
└── docs/                      # charter, delegation analysis, asset map, this spec, the plan
```

## Risks / open setup-time items (not design unknowns)

Telegram bot token (create at BotFather during build) · email account + auth (phase 2) · exact NIM model ID (swappable; plan tests with curl) · search key (Brave free tier at signup) · box RAM (plan includes ≥4GB check) · exact Hermes config keys for external skill dirs/cron syntax (plan Phase 2 extracts verified facts from the installed docs before any dependent task).

## Phase 2 backlog (explicitly deferred)

Email triage MCP + calendar · GitHub PR automation · portfolio tracking (brokerage data) · markets-digest cron · Substack distribution repurposing · $100/day funnel build · family-business research digest · errands automation · warm-intro graph.
