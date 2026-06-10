# Heavy-worker dispatch contract (Compaq → Mac)

INVOKE: ssh mac 'mkdir -p ~/work/dispatch/out && cd ~/work/dispatch && claude -p "<TASK>" \
  --output-format json \
  --allowedTools "WebSearch,WebFetch,Bash(agent-browser *),Read,Write" --max-turns 30'

TASK template: role (deep researcher) + the question + quality bar (the deep-research gate,
inline) + output contract (markdown dossier w/ inline citations) + "write the result to
~/work/dispatch/out/<job-id>.md".

RETRIEVE: scp mac:~/work/dispatch/out/<job-id>.md back; Hermes files it per the normal filing
convention (notion-ops) and delivers the TL;DR.

RULES:
- One job at a time; 30-min timeout; job-id = <skill>-<YYYYMMDD-HHMMSS>.
- The Mac worker NEVER gets Notion/Telegram/mail creds — it researches and writes files;
  Hermes does ALL delivery and ALL workspace writes.
- The quality gate runs on the RESULT here (the gate is ours, not the worker's).
- Path convention: ~/work/dispatch lives on the MAC (this contract); ~/work/<repo> on the BOX
  (Plan 05 coding) — same convention, different machines.
