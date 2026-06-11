# Crons (timezone America/New_York — cron expressions run in SYSTEM local time;
# the box is set to America/New_York at deploy. Verify with a one-off test job.)

Rate discipline (Plan 14): NIM free tier = 40 RPM. No two crons start within 15 min of each
other in the 06:00–09:00 window. Until the 200 RPM bump is granted, run REDUCED crons
(brief + heartbeat only).

## v1 jobs — registration commands (syntax verified, hermes-facts.md §Cron)

```bash
# 1. Morning brief — daily 06:30
hermes cron create "30 6 * * *" \
  "Run the morning-brief skill: compose today's brief and deliver it." \
  --name morning-brief --skill morning-brief --skill notion-ops --deliver telegram

# 2. Due-tomorrow pre-load — daily 21:00
hermes cron create "0 21 * * *" \
  "Read tomorrow's Tasks rows (notion-ops conventions). For research-type tasks, pre-stage
materials with a light deep-research pass and file findings to the task. Send a 1-line summary." \
  --name due-tomorrow-preload --skill notion-ops --skill deep-research --deliver telegram

# 3. Professor monitor — weekly Mon 08:00
hermes cron create "0 8 * * 1" \
  "Run the prof-monitor skill and deliver the digest." \
  --name prof-monitor --skill prof-monitor --skill notion-ops --deliver telegram
```

## v1.1 (off by default — do NOT register yet)

```bash
# 4. Markets digest — daily 07:00 (≥15 min after the brief; needs Plan 06)
# hermes cron create "0 7 * * *" "Run the markets-digest skill." \
#   --name markets-digest --skill deep-research --deliver telegram
```

## Notes
- ANY new cron (yours or future plans'): keep ≥15 min from existing starts in 06:00–09:00 ET.
- `--repeat 1` semantics unverified (1 total vs 1+initial) — verify on the fire test and record here.
- Delivery target `telegram` honors TELEGRAM_HOME_CHANNEL (or run /sethome once in the bot chat).
- Cron sessions get fresh agent context; skills attach via --skill (verified).
- Cron sessions cannot create more crons (Hermes anti-runaway, verified).
- List: `hermes cron list` · pause/resume/remove · status: `hermes cron status`.
- Fire test pattern: `hermes cron create "2m" "Run the morning-brief skill." --name test-fire
  --skill morning-brief --deliver telegram --repeat 1` then `hermes cron remove test-fire`.
