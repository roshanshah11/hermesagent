# Hermes Asset Map — what you ALREADY have → what Hermes can do with it

> Survey of the live Notion workspace (all DBs/pages in the ID registry) + every local file in `/Downloads/Notion` (2026-06-10).
> Each asset: **what Hermes does with it — why (one line).**
> Companion to `hermes-charter.md` (capabilities) — this is the *inventory* view: the harness is half-built already.

---

## 1. The two harness gems (you built these for a different reason — they ARE the autonomy harness)

- **🪵 Change Log DB** (`06df62e7…` · cols: Action · Timestamp · Source · Entity→Tasks · "Before -> After" · Note) → **Hermes logs every autonomous write here, before it acts.**
  *Why: "act on its own" is only safe with an audit trail you can review and revert — this DB is exactly that, already wired with a Tasks relation.*
- **🧰 Control DB** (`7ebb75d3…`, break-mode toggle row) → **Hermes checks it before acting — a kill switch / mode flag (run / draft-only / paused).**
  *Why: a 24/7 agent needs an off switch you control from your phone; one select property on this existing row does it.*
- **`hub_content_snapshot.json` + `scaffold_ids.json`** (local) → **generalize the pattern: snapshot before every autonomous bulk write, auto-rollback on bad output.*
  *Why: you already proved this pattern on the cockpit rebuild — it's the harness's undo button.*

## 2. Engine DBs (the spine — Hermes's working memory)

- **✅ Tasks DB** (213 rows, `When`/`Focus`/`Type`/Area, ↔People/Projects/Goals) → **the brief engine + work queue**: read Big 3/Today each morning, write every finished research artifact back as a linked row, pick up rows tagged for it (an `Owner: Hermes` flag).
  *Why: it's your master backlog — Hermes working FROM it and INTO it means zero new systems.*
- **👥 People DB** (Daniel, Youti, Yoyo, 15 profs… ↔Tasks/Calls/IB Apps) → **the CRM**: banker/alumni sourcing rows land here (your "LinkedIn → sheet" ask), enrichment, last-touch tracking, follow-up surfacing.
  *Why: the networking pillar's data home already exists with every relation it needs — your CSV is this DB plus an export.*
- **🏢 Firms DB** (# Apps + # People rollups) → **target-firm map**: Hermes enriches each firm, attaches sourced people, exposes warm paths per firm.
  *Why: the rollups already count people-per-firm — that IS coverage tracking for banker outreach.*
- **💼 IB Applications DB** (APP- IDs, ↔People referral) → **recruiting deadline radar**: Hermes creates a row per opening it finds (sophomore programs, early-ID, OAs) with deadlines + status.
  *Why: a miss here is unrecoverable, and the tracker is already built — it just needs a researcher feeding it.*
- **🎯 Goals / 📁 Projects DBs** → **weekly-review prep**: roll up what moved per goal/project, flag stalled ones.
  *Why: relations to Tasks already exist, so "what did this week actually advance" is a query, not a chore.*
- **🪵 Calendar page + Week/Month/Timeline views** → **morning brief + due-tomorrow pre-load source.**
  *Why: the brief is a read over views you already maintain.*

## 3. Workstream DBs (each one is a Hermes pipeline waiting for a worker)

- **✍️ Substack Posts** (Stage: Idea→Research→Model→Thesis→Publish) → **the biweekly research drop**: Hermes moves a post Idea→Research by attaching the deep-dive dossier; you take it Model→Thesis (your DCF, your take).
  *Why: the Stage select is literally a pipeline state machine — Hermes owns the first two stages, you own the rest.*
- **💡 Markets Idea List** (Raw/Exploring/Promising/Parked/Promoted) → **digest feeder**: daily markets digest files candidate ideas as Raw with a one-liner; you promote.
  *Why: matches your "reading to get smarter + portfolio" track — ideas get captured instead of evaporating.*
- **🔬 Research Labs DB + profs in People** (15 profs, 5 labs, cited) → **prof monitoring**: watch each target's publications/news, ping you with a timely outreach hook, draft the email.
  *Why: the target list research is DONE — monitoring it is pure recurring agent work.*
- **🏛️ Club Applications DB** (Function · Takes sophomores? · Process · Deadline · Status) → **club radar**: fill from discovery research, watch deadlines through the Oct recruiting ramp.
  *Why: schema already has every column the research produces.*
- **⭐ Specialized Programs DB** → **opportunity radar home**: Contrary Q3 + every fellowship/program Hermes finds gets a row with deadline.
  *Why: "things that appear and vanish" need a watched table, and this is it.*
- **📘 Course Plan DB** → **transfer-onboarding tracker**: registration windows, transfer-credit petitions, Core mapping, holds — researched and dated by Hermes.
  *Why: the biggest latent blind spot from the charter gets a home that already exists.*
- **☎️ Calls DB** (↔People) → **pre-meeting briefs**: before any call, Hermes attaches a one-pager (background, recent work, talking points, the ask) as the call page.
  *Why: the DB structurally links person↔call already — the brief just fills the page.*
- **🆕 GTM / Client Acquisition DB** (Lead · Stage · Channel · Notes) → **$100/day lead-gen**: same sourcing-to-rows pattern as bankers, pointed at tutoring/essay clients once you pick the channel.
  *Why: you already built a lead pipeline DB — it's empty because no one's been doing the sourcing; that's Hermes.*
- **Tutoring / Business Setup / SAT-ACT DBs** → **funnel build executor** post-decision (profiles, listings, setup steps).
  *Why: setup is checklist work — agent-grade once the pricing/channel call (yours) is made.*
- **🚀 Startup Ideas DB** (Problem/Who for/Why me/Tech-AI angle/Stage) → **idea pressure-tester**: for each captured idea, Hermes researches market/competitors/feasibility before Jul 25 (YC Startup School).
  *Why: the schema's fields ARE a validation brief template — Hermes fills them with evidence, you make the call.*
- **🏠 SF Housing DB** → **booking pipeline**: refresh hacker-house/lodging options with prices and apps, ready-to-book before Jul 24–26.
  *Why: dated, structured, external-web research — the easiest full delegation on the board.*
- **📗 Technicals DB** → **sequence tracking only** — Hermes tracks what's covered/next, but materials and flashcards stay yours.
  *Why: your explicit call — building the deck is the learning.*
- **Calc Study Plan + Practice Tests DBs** → **hands off.**
  *Why: your call — math/CS placement is you.*

## 4. Pages (the knowledge base already has a skeleton)

- **Area pages** (Networking · Research & Career · IB Recruiting · Markets · Substack · $100/Day · Startup/SF) → **research dossiers file here as sub-pages, by area.**
  *Why: the "research knowledge base" gap needs a filing tree — it exists; nothing's been filing into it.*
- **🏠 Hub cockpit** (Big 3/Today/Overdue/This Week/Inbox/Follow-ups views) → **the delivery surface**: morning brief lands here; Hermes also keeps it clean (sweep stale rows — your standing rule).
  *Why: you glance at one place; everything Hermes produces should surface there, not in some new app.*
- **🗄 Archive page** → **Hermes's trash can**: everything it supersedes gets archived (reversible), never deleted.
  *Why: matches the no-stale-rows rule and keeps autonomous cleanup safe.*

## 5. Local files (Hermes's boot disk, hands, and voice)

- **`notion_v3.py` + `notion_v3_mcp.py` + `.mcp.json` + `.env`** → **Hermes's hands** — full enumerate/read/bulk-write surface beyond the official API, already validated.
  *Why: the hardest integration problem (full read/write on your workspace) is solved and tested; Hermes inherits it day 1.*
- **`CLAUDE.md` (ID registry + conventions + API gotchas)** → **boot context** — Hermes cold-starts from it exactly like I do.
  *Why: every ID, timezone rule, and write-gotcha an agent needs is already documented from real scar tissue.*
- **`docs/intent/operating-model.md`** → **the scheduling + self-learning brain**: your rhythm, priority order, daily template, and the standing "continuously learn his patterns" directive.
  *Why: you asked for a self-learning agent — the directive AND the pattern log it learns into already exist.*
- **Memory dir** (`~/.claude/projects/…/memory/`) → **the learning substrate**: Hermes writes observed patterns/corrections there, exactly as I do.
  *Why: self-learning needs persistent memory; the mechanism is live.*
- **`/daily` · `/reflow` · `/eod` commands** (`.claude/commands/`) → **Hermes runs the unattended halves** (brief assembly, due-tomorrow pre-load, EOD reconcile draft); live reflow stays a conversation with you.
  *Why: the operator loop is already written down — splitting it into attended/unattended is the cron spec.*
- **`INTERVIEW-LOG.md` + `INTERVIEW-RAW.md` + `INTAKE.md`** (~90KB of your verbatim words) → **voice corpus**: Hermes learns to draft outreach/applications in YOUR voice from these.
  *Why: "drafts in his voice" needs samples — you already produced a large one without trying.*
- **`PRODUCT.md` + `AGENT.md`** → **capability contract + operator manual** — Hermes's job description seed.
  *Why: they define how an agent is supposed to behave in this workspace.*
- **`docs/hermes-delegation-analysis.md` + `hermes-charter.md`** → **the spec inputs** (this file is the third leg).
- **`schedule-q3.md`, `TASK_BREAKDOWN_PLAN.md`, `plans/`** → **planning corpus** for how you like work decomposed.
- 🧹 **Cleanup flag:** stray `--full-page` file (334KB, Jun 10 00:19) in the project root — looks like an accidental page dump; archive or delete.

## 6. Explicitly out (your calls, restated once)

IB-technicals materials/flashcards · math + CS placement prep and sitting · your DCF builds (Hermes feeds research only) · decisions (channel, company, offering, idea, clubs, profs) · live reflow conversations · gym/tabla/golf/family blocks.

---

### Bottom line
You don't need to build Hermes a workspace — **you already built it.** Every pillar in the charter has a live DB waiting for a worker (People/Firms/Calls = networking; Substack Posts/Idea List = markets; IB Apps/Clubs/Programs/Course Plan = radar; GTM = lead-gen), the v3 client is its hands, the Change Log + Control DB are its accountability and kill switch, the snapshot pattern is its undo, the interview corpus is its voice, and the memory dir is its self-learning. What's missing is only: the runner (cron/loop), the quality gate ("Perplexity-grade or redo"), and the per-pipeline prompts.
