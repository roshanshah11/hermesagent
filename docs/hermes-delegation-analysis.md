# Hermes Delegation Analysis — Roshan's Summer Task List

> One lens only: **what can an always-on autonomous agent (Hermes) take off Roshan's plate.**
> Source: live Tasks DB enumeration (213 rows, 2026-06-09). Tasks referenced are real, not generic.
> Governing rule throughout: **research is automatable; the decision, the send, the sitting, and the learning are human.**
> Scope boundary: Hermes owns **unattended heads-down production** (research, drafts, data pulls, monitoring, scheduling) and surfaces it for Roshan's decision/send. It does **not** replace the interactive `/daily` `/reflow` `/eod` operator loop — that one needs Roshan in the room (chores, last-minute items, judgment reflows).

---

## 1. Automatable now — Hermes can fully or mostly DO these

Each item: **the task · what "done" looks like · what Hermes needs (inputs/access).**

### Markets / Substack (strongest cluster)
- **Substack biweekly deep-dive — research + outline + first model pass.** Real tasks: *"Substack — deep-dive research + outline," "build model / DCF," "draft thesis (flexible block)," "biweekly deep-dives continue."*
  - **Done:** a research dossier on the chosen company (business, segment economics, comps set, recent filings/news), a first-pass DCF/EV model with assumptions flagged, and a draft thesis skeleton with the open questions marked for Roshan to take a view on.
  - **Needs:** the ticker/company (Roshan's call — see §3), SEC filings access (EdgarTools/XBRL-class), a market-data source for prices/multiples, and write access to a working doc or the Substack draft.
- **Markets reading — "get smarter" company/industry read + portfolio tracking.** Real tasks: *"Markets — reading: get smarter (company/industry read)," "reading + start tracking your portfolio."*
  - **Done:** a standing industry/company reading digest (what moved, what's worth his time, 3–5 annotated links) and a maintained portfolio sheet with positions, P&L, and notable events on his holdings.
  - **Needs:** his holdings list, a price/news feed, and a sheet/DB to write into.

### IB technicals (prep is automatable; the learning is not)
- **Technicals study materials — flashcards, Q&A drills, 400-Q bank.** Real tasks: *"EV/equity review + flashcards," "consolidate Comps/Precedents/DCF/LBO," "LBO (review + Q&A drill)," "finish + 400-Q grind," "book order + 400-question grind," "line up tomorrow's technicals topic + make flashcards."*
  - **Done:** per-topic flashcard decks, a graded Q&A drill set with answer keys, and a consolidated 400-question bank organized by topic and difficulty — ready for him to drill.
  - **Needs:** the topic list (already implied by his rows: EV/equity → Comps → Precedents → DCF → LBO), a reference source (his book once ordered, or standard IB guides), and a deck/doc to populate.

### Placement-test prep (build the materials; he sits the test)
- **Math placement — topic pull + practice-exam build + grading.** Real tasks: *"Math — Perplexity: pull all placement topics (pre-calc → Calc 2) + build practice exam," "take the practice exam (timed)," "grade exam + list topics to review."*
  - **Done:** the full topic map (pre-calc → Calc 2), a timed practice exam with answer key, and — after he sits it — a graded breakdown with weak-topic list driving the next review block.
  - **Needs:** UChicago's placement scope (he provides), and the exam doc.
- **CS placement — problem sets + timed mock exam.** Real tasks: *"CS Setup," "Programming Basics + Warm-up: Parking," "Recursion + Trees," "FULL timed practice exam (120-min)."* (Note: CS sit Jun 16 may be skipped — pending Roshan.)
  - **Done:** Python warm-up problems per topic with auto-checkable solutions, plus a 120-min mock exam mirroring the real format.
  - **Needs:** the CS exam content/topic-by-day (his own task *"Provide CS exam content"* is the blocker — once supplied, Hermes runs).

### Internship deliverables (the actual near-term work, regardless of priority)
- **AI broker-listing scraping platform + industry research.** Real tasks: *"🏢 Internship — work (1h MAX: scraping + research)," "Internship — async work (~2h)" ×many, "~10h async work."*
  - **Done:** a working scraper that pulls broker listings into a defined schema, plus the industry-research write-up that accompanies it. This is the cleanest "agent does the whole thing" item on the list — it *is* scraping + research.
  - **Needs:** target sites, the output schema/fields, a storage target (sheet/DB/file), and any auth for gated sources.

### Personal coding
- **Remote Connect build (+ other personal projects).** Real tasks: *"Personal coding project — Remote Connect (build)," "Coding — personal projects (Remote Connect + others)."*
  - **Done:** implemented features per spec with tests, on a branch for his review. Longer-horizon, so scope it per-feature rather than "build the app."
  - **Needs:** the repo, the spec/next feature, and run/test access.

### Research & outreach prep (source + draft; he sends)
- **Professor research outreach — target list + reusable template + personalized drafts.** Real tasks: *"Perplexity: build UChicago professor target list (econ/eng/tech/AI)," "Draft reusable cold-email template for professors," "Research — Perplexity prof sourcing + cold emails," "prof cold-outreach follow-ups."*
  - **Done:** a ranked professor/lab target list with research interests, a reusable cold-email template, and a personalized draft per target — queued for his one-click send.
  - **Needs:** his background blurb + ask, a voice/template sample, and contact info (lab pages / directory). Draft scope, not send scope.
- **Networking sourcing — UChicago-alumni / people list.** Real tasks: *"Networking — light Perplexity sourcing / UChicago-alumni list," "Networking — light Perplexity sourcing."*
  - **Done:** a maintained, deduped contact list (name, role, firm, why-relevant, warm-path note) feeding the People DB.
  - **Needs:** target criteria (UChicago + finance/tech), LinkedIn/public sources, and the People DB.
- **Outreach message drafts — Daniel / Youti / Yoyo.** Real tasks: *"Email Daniel," "Text Youti," "DM Yoyo."*
  - **Done:** a tailored draft for each, in his voice, with context pulled on the person — ready to review and send.
  - **Needs:** the relationship context (he has it) + a voice sample. **Send stays human (§3).**

### Market-decision research (research = Hermes; the call = §3)
- **$100/day market research.** Real tasks: *"Perplexity deep-dive: $100/day — what to offer, who actually buys, willingness-to-pay + pricing, best channels," "Define tutoring offering + positioning (Schoolhouse proof)," "Validate online essay-review service."*
  - **Done:** a decision-ready brief — offering options, buyer personas, WTP/pricing benchmarks, channel comparison with effort/CAC notes.
  - **Needs:** web research access; output to a doc. (The *choice* of offering/channel is his — §3.)
- **HF-vs-IB recruiting requirements.** Real task: *"Perplexity: what does hedge-fund recruiting actually require vs IB … define prep."*
  - **Done:** a comparison brief that converts into a concrete prep plan (what to study, in what order).
  - **Needs:** web research; his target firm types.

### Applications & logistics
- **Application drafting — UChicago Financial Markets program + Contrary Fellowship.** Real tasks: *"🎓 UChicago Financial Markets program — APPLICATION," "Contrary Research Fellowship — apply (Q3 cohort)," "UChicago Financial Markets app — work session."*
  - **Done:** first-draft answers to every prompt, built from his background + the program's criteria, flagged where he needs to inject a personal take.
  - **Needs:** the application prompts, his resume/background, and the draft doc.
- **SF logistics research — hacker houses + Startup School lodging.** Real tasks: *"Research SF hacker houses + housing options / applications," "Sort out SF lodging for YC Startup School (Jul 24–26)."*
  - **Done:** a shortlist with prices, locations, dates, links, and application requirements — ready for him to book.
  - **Needs:** dates (Jul 24–26), budget, web access.
- **Club discovery.** Real task: *"Perplexity: discover UChicago target clubs (skip quant)."*
  - **Done:** a researched club list (function, whether they take sophomores, process, deadlines) into the Club Applications DB. (Which to *apply* to = his call.)
  - **Needs:** UChicago club sources; the Club Applications DB.

---

## 2. Recurring / cron-able — the heart of an always-on agent

These run unattended on a schedule and hand back a product. Roshan's own *"Look-ahead"* tasks are the literal seed: he wrote *"each morning, glance at what's due tomorrow and pre-load it,"* *"line up tomorrow's technicals topic + make flashcards,"* *"pick the company for the next Substack deep-dive."* That's a cron spec in disguise — Hermes should own it.

| Cadence | Job | Delivery |
|---|---|---|
| **Daily, ~6–7am** | **Morning brief.** Pull Big 3 + Today from the Tasks DB, surface what's due, flag deadline proximity (Math SIT Jun 15, CS SIT Jun 16). | A single brief waiting when he wakes — today's schedule + the 1–3 things that actually matter. |
| **Daily, evening** | **"Due-tomorrow" pre-load.** Look at tomorrow's blocks and pre-stage the materials: tomorrow's technicals topic + a fresh flashcard/drill set; tomorrow's study block's problem set. | Tomorrow's deep-work materials sitting ready, so he opens the doc and goes — his exact *"pre-load it"* task, automated. |
| **Daily** | **Markets digest.** Company/industry read + overnight moves on his holdings. | A short annotated digest + updated portfolio sheet. |
| **Weekly (his existing Weekly Review block)** | **Week-ahead prep.** Reconcile what slipped, pre-draft next week's research queue, refresh the outreach/follow-up list (who's gone cold). | A pre-filled weekly-review doc so his review is *reviewing*, not assembling. |
| **Biweekly** | **Substack deep-dive research drop.** On the cadence of *"biweekly deep-dives continue"* — once he names the company, Hermes delivers the dossier + first model pass ahead of his writing block. | Research + model in the draft before he sits down to write. |
| **Weekly / event-driven** | **Deadline & opportunity scan.** Watch application windows (Contrary Q3, club recruiting → Oct 1, fellowships, research postings) and surface new ones. | A "deadlines moving" alert in the brief — nothing silently expires. |
| **Daily/weekly during internship** | **Scraper run + freshness check.** Once the broker-listing scraper exists, run it on schedule and report deltas/breakage. | Fresh data + a flag if a target site changed and broke the scrape. |

---

## 3. Human-only — keep this honest so you don't automate the wrong things

**Decisions (research feeds them, but the call is yours).** Each of these appears in your list explicitly as a decision; pair it with the Hermes research from §1 — Hermes briefs, you decide:
- *"Choose client-acquisition channel [ASK USER — don't pick]"* — you literally tagged this human.
- *"Decide first company to deep-dive"* / *"pick the company for the next Substack deep-dive."*
- *"Decide lead $100/day offering after research."*
- *"Idea-gen sprint — land a candidate idea before Jul 25"* — Hermes can generate and pressure-test options; landing the idea is you.
- Which clubs to actually apply to; which professors are worth the relationship.

**Relationships & sends.** Hermes drafts; you send and you own the relationship:
- *Email Daniel, Text Youti, DM Yoyo* — the send and the rapport.
- *"Networking RAMP — in-person Chicago, 2–3 calls/wk,"* *"Research — UChicago labs/profs (in person)"* — calls and in-person are you.

**Learning & sitting.** The reason placement/technicals prep splits cleanly: Hermes builds the materials, but the knowledge has to land in *your* head:
- Math/CS **placement tests — SIT** (Jun 15 / Jun 16). Non-delegable by definition.
- Actually *learning* IB technicals, doing the reps, the timed practice exams.

**Presence / life blocks.** Not tasks to automate — Gym, Tabla, Golf, *Household/family (5–8pm blocked)*, the Mon/Thu/Wed internship meetings. Leave them on the calendar; don't let an agent "optimize" them.

**Final judgment on your own system.** The interactive reflow — "to do X I need Y first, adjust everything" — stays a live conversation. Hermes feeds it; it doesn't run it.

---

## 4. Gaps — things that *should* be on your list given your goals, that an agent could own

- **Trading systems / quant research — your biggest gap.** You said you want to be *"building out trading models"* and it got swallowed into Substack scope. There are no structured tasks for: signal research, backtesting, walk-forward validation, data pulls, or a strategy journal. This is the single cleanest agent-ownable domain that exists — it's all data + code + measurement, almost no human-judgment bottleneck until the "go live" decision. **Recommend: stand up a trading-systems workstream and let Hermes own the backtest/data/validation loop.** (This class of work — PIT fundamentals, EDGAR pulls, walk-forward, cost models — is demonstrably tractable for an agent.)
- **Family business — named in your ask, entirely absent from the list.** Be honest about the split: the relationship, the strategic calls, and family dynamics are *you*. But the agent-ownable slices are real and missing — market/competitor research, process/ops automation, data cleanup, a recurring "what's happening in our market" digest. Worth deciding if any of it belongs in the system at all; right now it's a blind spot.
- **Networking CRM / follow-up engine.** You have outreach *tasks* but no *system*: nobody's tracking who you contacted, who owes a reply, who's gone cold. An always-on agent should maintain the People DB as a living CRM and surface "follow up with X — 10 days silent" in the morning brief. (Your People follow-ups view is the hook; nothing feeds it automatically.)
- **Application/deadline monitoring as a standing job** (not one-off tasks). Contrary Q3, club recruiting → Oct 1, research postings, fellowships — these should be *watched*, not remembered.
- **Substack distribution & growth.** You have produce-the-content tasks but nothing on getting it read — repurposing each deep-dive into X/LinkedIn posts, building a distribution loop. Pure agent work once a piece ships.
- **A research-knowledge base.** Every Perplexity/research task produces output that currently has no home. Hermes should file findings into a searchable store so you stop re-researching.

---

## 5. Top 10 highest-leverage delegations

Ranked by **time saved × how cleanly an agent can do it.** A clean medium-time task outranks a messy big one. Anything needing your judgment is excluded by design (it's in §3).

1. **Substack deep-dive: research dossier + first DCF/model pass.** Highest time, very clean — data + filings + drafting, zero judgment until you write the thesis. Recurs biweekly, so the leverage compounds.
2. **Internship broker-listing scraper + industry research.** It *is* a scraping-and-research deliverable — the textbook "agent does the whole thing." High hours, fully specifiable.
3. **Trading-systems backtest/data/validation loop (gap → add it).** Not on your list yet, but the cleanest agent domain you have and tied to a real goal — would be #1 the moment it's a workstream.
4. **IB technicals materials — flashcards + Q&A drills + 400-Q bank.** Daily prep you currently do by hand; clean to generate, frees your blocks for actual reps.
5. **Math placement: topic map + timed practice exams + grading.** Bounded, clean, deadline-driven (Jun 15) — Hermes builds, you sit.
6. **Daily morning brief + "due-tomorrow" pre-load.** Pure cron, zero judgment, every single day — your own look-ahead task, automated. Small per-run, enormous over a summer.
7. **Professor/research outreach pipeline — target list + personalized drafts.** Research + draft is clean and high-volume; you only send. Directly serves the research-at-UChicago goal.
8. **$100/day market-research brief (offer / buyer / WTP / channels).** One clean research push that unblocks a decision you keep deferring — high leverage because it's currently *stuck*.
9. **Application drafting — UChicago Financial Markets + Contrary.** Clean drafting against known prompts; deadline-bound; you inject the personal take.
10. **Markets daily digest + portfolio tracking.** Low time per run but daily and clean — monitoring is exactly what an always-on agent is *for*.

---

*Honest bottom line:* your list is ~40% recurring life/calendar blocks (don't touch), ~25% learning/sitting (you, with Hermes building the materials), and ~35% research/draft/code/monitor — and that last third is almost entirely delegable today. The fastest win isn't a new tool; it's wiring the **morning brief + biweekly Substack research drop + the internship scraper** into Hermes first, then opening the **trading-systems** workstream that's been missing.
