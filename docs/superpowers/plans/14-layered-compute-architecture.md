# Plan 14 — Layered Compute Architecture (the $0 stack)

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.
> **SUPERSEDES** the single-provider assumption in Plan 01 Phase 3/5 where they conflict. Decision: Roshan, 2026-06-10 — don't pay anyone yet; build the layered free stack; pay later, surgically, only if a real gap hurts.

**Goal:** Hermes runs 24/7 on the Compaq (2GB AMD E-300 — verified constraint) doing the light 80% locally and free; the heavy 20% (Perplexity-grade deep-dives, agentic browsing, sourcing) dispatches over SSH to **Claude Code running headless on the Mac**, best-effort: Mac awake → frontier-grade; Mac asleep → queue or degrade gracefully.

**Architecture:**
```
COMPAQ (always-on orchestrator — light 80%)          MAC (heavy worker — 20%, best-effort)
├─ Hermes Agent + Telegram gateway                   ├─ Claude Code headless (claude -p)
├─ Brain: NIM free tier (Nemotron driver, 40 RPM)    │   └─ WebSearch/WebFetch/agent-browser CLI
├─ Search: ddgs (zero-infra) [+SearXNG if RAM]       │   └─ full skill ecosystem (deep-research…)
├─ Extract ladder: crawl4ai HTTP (T1) →              ├─ Reached via Tailscale SSH
│    Lightpanda CDP (T2, beta, non-SPA, if no-AVX OK) → Mac dispatch (T3)
├─ Notion MCP · crons · queue (SQLite/file)          └─ Awake-policy: pmset/caffeinate (his call)
└─ Jobs: briefs, triage, watchdogs, drafts, digests
```

**Verified facts (2026-06-10):** NIM free tier = 40 RPM default, 200 RPM on request, 100+ models free incl. Nemotron 3 Super 120B / DeepSeek / Qwen / Kimi ([limits guide](https://decodethefuture.org/en/nvidia-nim-api-pricing-limits-guide/), [forums](https://forums.developer.nvidia.com/t/clarity-on-nim-api-free-tier-rate-limit-increases/369624)) · SearXNG runs in 256–512MB, ~300MB disk ([specs discussion](https://github.com/searxng/searxng/discussions/3884)) · crawl4ai ships an HTTP-only crawler strategy (no Playwright) + text/light modes ([docs](https://docs.crawl4ai.com/)) · packaged skills exist: [crawl4ai-skill](https://skills.sh/lancelin111/crawl4ai-skill/crawl4ai-skill) (489 installs), [browser-automation](https://skills.sh/claude-office-skills/skills/browser-automation) (3.1K).

---

### Task 0: ⛔ THE MEMORY GATE — can the E-300 even run Hermes? (single biggest unvalidated assumption; run FIRST)

- [ ] **Step 1: Measure.** On the Compaq, after `hermes setup` but with no jobs running:
  `free -h && ps -o rss=,comm= -p $(pgrep -d, -f hermes) | sort -rn` — record Hermes idle RSS.
  Then run ONE morning-brief-class task and re-measure peak (`watch -n2 free -h` during the run,
  or systemd-cgtop if under systemd). Record both in `docs/notes/hermes-facts.md`.
- [ ] **Step 2: Decide by threshold (usable RAM ≈ 1.6GB after OS):**
  - Idle ≤700MB and one-task peak ≤1.2GB → **proceed as planned** (light tier local).
  - Idle >1GB → **the Compaq is a gateway-only relay**: Telegram gateway + crons + queue live here;
    EVERYTHING (even the light tier) dispatches to the Mac via the heavy-research path. Skip Task 2's
    crawl4ai/SearXNG installs entirely; ddgs only if it fits. Amend the routing table accordingly and
    note the demotion in hermes-facts.md — do NOT build seven skills on an assumption this gate refuted.
  - Between → proceed, but add 512MB+ swap (`fallocate -l 1G /swapfile…`), zram if available, and
    re-measure under a markets-digest run before trusting crons unattended.

### Task 1: Brain — NIM Nemotron driver on the Compaq

- [ ] **Step 1: Model selection (decided 2026-06-10 from the live catalog — 76 free endpoint models).**
  Three roles, three models:
  - **DRIVER (default for everything): `nemotron-3-super-120b-a12b`.** Why: the Nemotron line is
    NVIDIA's explicitly agentic family — strong tool/function calling, which is THE make-or-break
    capability for the orchestrator (every MCP call, search, and dispatch is a tool call); MoE with
    ~12B active params = fast despite 120B class (the driver runs dozens of small jobs daily —
    latency > peak depth, since depth lives on the Mac); NVIDIA's own flagship on NVIDIA's own
    service = best-supported, least likely to vanish from the preview catalog.
  - **FAST FALLBACK (429s/flakes): `deepseek-v4-flash`** — same OpenAI-compatible call, one config
    line to swap when the driver rate-limits or the preview endpoint flakes.
  - **DEEP ESCALATION (Mac asleep, deadline forces local depth): `deepseek-v4-pro`** — strongest
    reasoner on the free catalog for one-off degraded deep jobs.
  - Skipped deliberately: kimi/qwen3.5/glm/minimax (fine, don't beat the picks for these jobs);
    cosmos/content-safety/voicechat/pii/video models (wrong modality).
  ⚠️ Catalog display names ≠ API ids. Get exact strings first:
  `curl -s https://integrate.api.nvidia.com/v1/models -H "Authorization: Bearer $NVIDIA_API_KEY" | python3 -m json.tool | grep '"id"' | grep -iE "nemotron-3-super|deepseek-v4"`
  (expect e.g. `nvidia/nemotron-3-super-120b-a12b`, `deepseek-ai/deepseek-v4-flash`). Then execute
  Plan 01 Task 3.1/3.2 with the driver id — and the smoke test MUST include a tool-call check, not
  just chat (a driver that fumbles function calling is disqualified regardless of benchmarks).
  Record ids + observed rate behavior in `docs/notes/hermes-facts.md`.
- [x] **Step 2: Rate-limit discipline** — add to `config/config.template.yaml` comments + `context/HERMES.md`: `Brain = 40 RPM free tier. Crons must not stampede: stagger schedules ≥5 min apart; on 429, back off 60s and retry ≤3.` If Portal quick-setup was already completed on the box, keep it as fallback provider — two free brains beat one.
- [ ] **Step 3: Apply for the 200 RPM bump — DAY-1 BLOCKER, not "file it early."** The morning window
  (06:30 brief → 07:05 heartbeat → 07:30 markets → 08:15 email → 08:45 radar) fires multi-call agent
  loops against a 40 RPM ceiling; the bump is what makes the cron schedule viable. File the request
  (free, NVIDIA developer forums) before registering the full cron set; until granted, run REDUCED
  crons (brief + heartbeat only) and enforce: **no two crons start within 15 min of each other in the
  06:00–09:00 window.** Record outcome in hermes-facts.md.
- [ ] **Step 4: Commit** — `git add config/ context/ docs/notes/ && git commit -m "feat(arch): NIM Nemotron driver + rate discipline"`

### Task 2: Light search/extract on the Compaq (no browser, no keys)

- [ ] **Step 1: ddgs (primary, zero-infra)** — `pip install ddgs` in Hermes's venv; smoke test: 3-result query from Python. This is the default search for ALL Compaq-local jobs.
- [ ] **Step 2: crawl4ai HTTP-only (extract)** — `pip install crawl4ai` configured with the **HTTPCrawlerStrategy** (no Playwright install on the Compaq — 2GB cannot hold Chromium; enforce by NOT running `crawl4ai-setup` browser step). Use for static-page extraction → markdown. Optionally install the packaged skill for reference: `npx skills add lancelin111/crawl4ai-skill -g -y`.
- [ ] **Step 3: Lightpanda probe (Tier-2 — PROBABLY DEAD on this box; spend 2 minutes, not an hour).**
  The AMD E-300 has no AVX and Lightpanda is V8-based — expect `illegal instruction`. Probe ONLY:
  `curl -fsSL https://pkg.lightpanda.io/install.sh | bash && lightpanda version`. If it crashes (the
  likely outcome): Tier 2 does not exist on this hardware — the ladder is **Tier 1 → Mac, period**;
  record in hermes-facts.md, delete the binary, write NO systemd unit, NO CDP wiring, NO Tier-2
  routing logic. Only if it runs cleanly: wire serve mode (`lightpanda serve --host 127.0.0.1 --port
  9222`, Playwright `connect_over_cdp`) for JS-needing-but-NOT-SPA pages — beta, empty DOM = miss,
  never LinkedIn/SPAs.
- [ ] **Step 4: SearXNG (optional, only if free RAM >700MB measured)** — `docker compose` per [selfhosting guide](https://selfhosting.sh/apps/searxng/); 256–512MB budget; if RAM is tight, SKIP — ddgs suffices.
- [ ] **Step 5: Wire as tools** per hermes-facts.md (Hermes native search config or a 30-line stdio MCP wrapping ddgs+crawl4ai+Lightpanda, same pattern as notion_v3_mcp.py). Encode the extraction ladder in the tool itself: **Tier 1 crawl4ai-HTTP (default) → Tier 2 Lightpanda CDP (only if installed; JS-needing, non-SPA) → Tier 3 escalate to heavy-research (Mac)**. A Lightpanda result that is empty/near-empty DOM = a MISS, not an answer → auto-fall through to Tier 3 (or queue). Never let a Tier-2 miss fail a task silently.
- [ ] **Step 6: Test the ladder** — Compaq-local: (a) static page → Tier 1 answers, no browser process; (b) a JS-rendered non-SPA page → Tier 2 returns DOM; (c) a LinkedIn URL → tool refuses Tier 2 and routes Tier 3; (d) kill Lightpanda mid-run → Tier 2 miss degrades to Tier 3/queue, task still completes or queues cleanly. RAM stays <80% throughout.
- [ ] **Step 7: Commit** — `git add mcp/ config/ && git commit -m "feat(arch): Compaq extraction ladder — HTTP -> Lightpanda -> Mac dispatch"`

### Task 3: `heavy_research` dispatch — SSH → Claude Code on the Mac

**Files:** Create: `skills/heavy-research/SKILL.md`, `context/HEAVY-WORKER.md`

- [ ] **Step 1: Mac-side prep — HARD GATE, not a checklist item.** SSH key from Compaq authorized on
  the Mac (System Settings → Sharing → Remote Login; he set up SSH already). Then from the Compaq:
  `ssh mac 'claude --version && agent-browser --help | head -3'` — **BOTH must succeed before any
  skill that routes Tier-3 ships.** If `agent-browser` is missing, install it on the Mac first —
  without it, banker-sourcing has NO browser path at all (the routing table treats Mac browsing as
  guaranteed; this gate is what makes that true).
  **Awake policy (decide now, not after the first thin 6:30 brief):** the Compaq's highest-value jobs
  all dispatch here — the always-on agent is only as capable as the Mac's sleep schedule. Recommended:
  `sudo pmset repeat wakeorpoweron MTWRFSU 06:00:00` + evening availability (his usage windows
  06:00–08:00 + 21:00–01:30), or accept best-effort with eyes open.
  **Path convention note:** `~/work/dispatch` lives on the MAC (this plan); `~/work/<repo>` lives on
  the BOX (Plan 05 coding-pr). Same convention, different machines — don't conflate.
- [x] **Step 2: Write `context/HEAVY-WORKER.md`** — the dispatch contract:

```markdown
# Heavy-worker dispatch contract (Compaq → Mac)
INVOKE: ssh mac 'cd ~/work/dispatch && claude -p "<TASK>" --output-format json \
  --allowedTools "WebSearch,WebFetch,Bash(agent-browser *),Read,Write" --max-turns 30'
TASK template: role (deep researcher) + the question + quality bar (context/quality-rubric.md inline)
+ output contract (markdown dossier w/ inline citations) + write result to ~/work/dispatch/out/<job-id>.md
RETRIEVE: scp the output file back; Hermes files it per the normal filing convention.
RULES: one job at a time; 30-min timeout; the Mac worker NEVER gets Notion/Telegram/mail creds —
it researches and writes files, Hermes does all delivery and all workspace writes.
```

- [x] **Step 3: Write `skills/heavy-research/SKILL.md`**

```markdown
---
name: heavy-research
description: Dispatch deep research / agentic-browsing jobs to Claude Code on Roshan's Mac (frontier-grade). Best-effort — degrade or queue when the Mac is asleep.
version: 0.1.0
---
# Heavy Research (dispatch)
WHEN: research-dossier, banker-sourcing, any job needing real browsing or >light depth.
1. PROBE: ssh -o ConnectTimeout=5 mac 'echo up'. 
2. UP → dispatch per context/HEAVY-WORKER.md; retrieve; apply quality rubric to the RESULT
   (the gate is ours, not the worker's); file + deliver normally, noting "researched on Mac worker".
3. DOWN → tell Roshan: "Mac asleep — queued <job>. Run now in degraded local mode instead? (ddgs +
   HTTP extract, shallower)". Queue = output/queue/<job-id>.json; retry on next heartbeat + when any
   cron fires; deliver when done. Deadline-critical jobs (≤24h) auto-degrade rather than wait.
HARD RULE: the Mac worker is read-only on the world (research + local files). All sends, Notion
writes, and deliveries happen from Hermes after the gate.
```

- [ ] **Step 4: E2E test** — from Telegram: a dossier request → verify dispatch path (Mac awake), then `sudo pmset sleepnow` on Mac → same request → verify queue + degrade offer.
- [x] **Step 5: Commit** — `git add skills/heavy-research/ context/HEAVY-WORKER.md && git commit -m "feat(arch): heavy-research SSH dispatch to Claude Code"`

### Task 4: Routing table (which jobs run where)

- [x] **Step 1:** Append to `context/HERMES.md`:

```markdown
## Compute routing
COMPAQ-LOCAL (light 80%): morning-brief · due-tomorrow preload · email-triage · markets-digest
(quotes+ddgs news) · follow-up-engine · recruiting/transfer radar checks · outreach drafts ·
calendar-propose · errands research · file-lookup · all Notion ops.
MAC-DISPATCH (heavy 20%, via heavy-research): research-dossier · banker-sourcing (browser grind) ·
pre-meeting-brief enrichment when the person is thin on ddgs · prof-monitor deep checks · any job
you judge needs agentic browsing or frontier depth. When in doubt: try local first; escalate if the
rubric fails on local output.
EXTRACTION LADDER (within any Compaq-local job): Tier 1 crawl4ai-HTTP (default) → Tier 2 Lightpanda
CDP (beta; JS-needing, non-SPA ONLY — never LinkedIn/SPAs; empty DOM = miss) → Tier 3 Mac dispatch.
Misses fall through; they never silently fail a task.
```

- [x] **Step 2: Commit + update master plan row + spec decision table** (inference row → "Layered: NIM Nemotron (Compaq) + Claude Code heavy worker (Mac, best-effort)"; browser row → "Mac side via agent-browser/Claude Code; Compaq runs NO browser").

---

**Self-review:** 2GB constraint respected (no Chromium/Playwright on Compaq, ddgs+HTTP-only) ✓ · best-effort semantics explicit (probe → dispatch/queue/degrade, deadline auto-degrade) ✓ · privilege separation (Mac worker researches; Hermes alone touches Notion/Telegram/mail) ✓ · $0 (NIM free, ddgs free, Claude plan already paid) ✓ · rate discipline for 40 RPM ✓ · no placeholders ✓
