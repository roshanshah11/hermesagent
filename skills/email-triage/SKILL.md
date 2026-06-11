---
name: email-triage
description: Inbox triage — classify, summarize, surface action items. Read-only; drafts via outreach-draft voice rules.
version: 0.1.0
---
⛔ BLOCKED ON ROSHAN INPUT: email account choice (gmail vs uchicago) + app password / calendar source

# Email Triage

JOB: read the inbox so Roshan doesn't — classify every unread, surface only what needs him,
bury the noise. Read-only; v1 has NO send path.

Classes: SKIP (promo/noise) · INFO (no action) · ACTION (deadline, ask, reply owed) ·
OPPORTUNITY (recruiting/program/networking — cross-check recruiting radar + People DB).

OUTPUT CONTRACT (Telegram, terse):
- Header: `📬 N unread — A action · O opportunities`
- Each ACTION/OPPORTUNITY: from · subject · why it matters · suggested next step (1 line)
- INFO: one collapsed block of 1-line summaries · SKIP: count only
- Honest-empty: "📬 inbox clear — nothing needs you" beats manufactured urgency
- Never paste full bodies unless asked

HARD CONSTRAINTS: READ-ONLY — never mark read/delete/move/archive, never auto-reply · NO send
capability at L1; adding one is an explicit trust.md flip + skill revision, never silent ·
reply drafts ONLY on Roshan's ask ("draft reply to X: <gist>"), in outreach-draft voice, saved
to his Drafts folder — HE sends from his mail app · anything filed to Notion → notion-ops
protocol.

v0 default method (yours to improve): Hermes-native email tools (IMAP, creds = EMAIL_* in
~/.hermes/.env — native support supersedes Plan 04's custom mail-MCP fallback) → list unread →
classify → compose → Telegram. Draft requests → outreach-draft rules → confirm "draft is in
your Drafts folder".

Cron candidate: daily 08:00 + 17:00 → Telegram (register in crons/crons.md once unblocked).
