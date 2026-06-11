---
name: file-lookup
description: '"Find the thing I wrote about X" — search Roshan''s synced files + Hermes''s own outputs and quote the relevant part back.'
version: 0.1.0
---
# File Lookup

JOB: "find me that thing" — locate where Roshan (or Hermes) wrote about X across his synced
files, Hermes's own outputs, and Notion, and quote the relevant part back.

SCOPE: ~/sync/ (his pushed files) · ~/work/ (repos) · output/ (own artifacts, incl. the
output/research/ mirror) · the agent's notes · Notion read (filed dossiers/pages — IDs in
context/notion-ids.md). Mac over SSH (the key he configured): per-request, read-only, and SAY
SO ("searched your Mac over SSH"); standing crawls/indexing of his Mac only if he explicitly
asks. Anything outside this scope: ask first.

OUTPUT CONTRACT (Telegram, terse):
- file path (or Notion page) · the actual relevant excerpt (quoted) · 1 line of context
- multiple hits → top 3, ranked by relevance/recency
- "Send it to me" → paste full text (small) or describe + path (large)
- honest-empty: "not in my scope — want me to check <next place>?" beats a guessed location

HARD CONSTRAINTS: READ-ONLY — never edit/move/delete his files; copies for processing go to
output/ · quote real text, never paraphrase-as-quote · scope boundaries above are hard.

v0 default method (yours to improve): rg -i across local scope (filenames + contents); Notion
search when the topic smells like a filed dossier; rank; quote.
