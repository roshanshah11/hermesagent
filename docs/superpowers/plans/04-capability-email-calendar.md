# Plan 04 — Capability: Email Triage + Calendar Proposals

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Checkboxes track steps.

**Goal:** Hermes reads Roshan's inbox (triage + summaries), drafts replies (draft-only), and proposes calendar slots for the chats his sourcing produces. Sending stays L1 (queued) until Roshan flips the trust ledger.

**Depends on:** Plan 01 (agent live), Plan 02 (trust ledger — email-send starts L0/L1).

**Setup-time input (ask Roshan at Task 1):** which account(s) — personal Gmail and/or rashah@uchicago.edu (Outlook/Microsoft 365). Gmail path planned below; if UChicago/Outlook is wanted, repeat the pattern with IMAP host `outlook.office365.com` (app passwords may be disabled by the university — verify; if so, defer that account).

---

### Task 1: Mail access — catalog first, stdlib fallback

- [ ] **Step 1: Check the curated catalog** — `hermes mcp catalog | grep -iE "gmail|google|mail|imap"`. If a reviewed Gmail/IMAP server exists: `hermes mcp install <entry>`, configure creds per its docs, record in `docs/notes/hermes-facts.md`, skip to Task 2.
- [ ] **Step 2 (fallback): App password** — Roshan: Google Account → Security → 2-Step Verification → App passwords → generate for "Mail". Into `.env`: `GMAIL_ADDRESS=...`, `GMAIL_APP_PASSWORD=...` (+ add both to `.env.example` with empty values).
- [ ] **Step 3 (fallback): Author `mcp/mail_mcp.py`** — stdlib-only stdio MCP mirroring `mcp/notion_v3_mcp.py`'s JSON-RPC pattern (read it first; reuse its stdio loop verbatim). Tools — **deliberately no send tool at L1**:

```python
# Tools to implement (imaplib + email + smtplib, stdlib only):
# mail_list_unread(limit=20) -> [{uid, from, subject, date, snippet}]
# mail_read(uid) -> {from, to, subject, date, body_text}            # text/plain part, html-stripped
# mail_search(query, limit=20) -> same shape as list_unread          # IMAP SEARCH
# mail_create_draft(to, subject, body) -> {saved: true, folder: "Drafts"}  # IMAP APPEND to Drafts
# NO mail_send tool exists at L1. When trust.md flips email-send to L1+approved, a send tool may be
# added in a later revision — never silently.
# Connection: imaplib.IMAP4_SSL("imap.gmail.com"); creds from env GMAIL_ADDRESS/GMAIL_APP_PASSWORD.
```

- [ ] **Step 4: Wire into config** — add `mail` server to `~/.hermes/config.yaml` + `config/config.template.yaml` (command python3, args [repo/mcp/mail_mcp.py], env GMAIL_ADDRESS/GMAIL_APP_PASSWORD as `${...}`). `/reload-mcp`.
- [ ] **Step 5: Test** — ask Hermes: `List my unread emails.` Expected: real subjects. `Draft a reply to <uid> saying I'll respond Friday.` Expected: draft appears in Gmail's Drafts folder — nothing sent.
- [ ] **Step 6: Commit** — `git add mcp/mail_mcp.py config/ .env.example && git commit -m "feat(capability): mail MCP — read + drafts, no send tool"`

### Task 2: `email-triage` skill

**Files:** Create: `skills/email-triage/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: email-triage
description: Inbox triage — classify, summarize, surface action items. Read-only; drafts via outreach-draft voice rules.
version: 0.1.0
---
# Email Triage
1. mail_list_unread; classify each: SKIP (promo/noise) · INFO (no action — 1-line summary) ·
   ACTION (needs Roshan: deadline, ask, reply owed) · OPPORTUNITY (recruiting/program/networking —
   cross-check against recruiting-radar + People DB).
2. Deliver to Telegram: `📬 N unread — A action · O opportunities` then ACTION/OPPORTUNITY items
   (from · subject · why it matters · suggested next step). INFO as one collapsed block. Never paste
   full bodies unless asked.
3. If Roshan replies "draft reply to X: <gist>": apply outreach-draft voice rules, mail_create_draft,
   confirm "draft in your Drafts folder" — HE sends from his mail app.
4. NEVER mark read/delete/move messages (read-only), never auto-reply.
```

- [ ] **Step 2: Cron** — add to `crons/crons.md`: `Daily 08:00 + 17:00 — email-triage → Telegram.` Register both.
- [ ] **Step 3: Test** — `/email-triage` with a seeded test email to himself containing a deadline. Expected: classified ACTION with the deadline extracted.
- [ ] **Step 4: Commit** — `git add skills/email-triage/ crons/crons.md && git commit -m "feat(skill): email-triage read-only + drafts"`

### Task 3: `calendar-propose` skill (no calendar write access in v1)

**Files:** Create: `skills/calendar-propose/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: calendar-propose
description: Propose meeting slots for networking calls — no calendar write access; outputs ready-to-send scheduling lines.
version: 0.1.0
---
# Calendar Propose
Roshan's standing rhythm (America/New_York): gym 7:30–9 · deep work 9:30–13:00 (protect) ·
internship Mon/Thu 11:00–11:30 + Wed 12–13 (hard) · family 17:00–20:00 (hard) · open-ish: 13:30–16:00
weekdays, evenings 21:00+, weekend flex block. Networking calls fit best 13:30–16:00.
1. Read today/this-week timed Tasks rows (morning-brief logic) to avoid known conflicts.
2. Propose 3 specific slots ("Tue 6/16 2:00–2:30pm ET") avoiding hard blocks.
3. Output a paste-ready scheduling line for his draft/reply. If he confirms a slot, create the
   Notion task row for the call (notion-ops protocol) linked to the person.
v2 (deferred): real calendar read via Google Calendar MCP when email account is settled.
```

- [ ] **Step 2: Test** — `/calendar-propose 30-min call with an analyst next week.` Expected: 3 slots, none inside deep work/family/internship blocks.
- [ ] **Step 3: Commit** — `git add skills/calendar-propose/ && git commit -m "feat(skill): calendar-propose"`

---

**Self-review:** read+draft only, send tool structurally absent at L1 ✓ · Outlook variant flagged with verify step ✓ · rhythm blocks match operating-model ✓ · no placeholders (fallback server has full tool contract; executor reuses the proven stdio pattern from notion_v3_mcp.py) ✓
