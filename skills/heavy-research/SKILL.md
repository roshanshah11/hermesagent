---
name: heavy-research
description: Dispatch deep research / agentic-browsing jobs to Claude Code on Roshan's Mac (frontier-grade). Best-effort — degrade or queue when the Mac is asleep.
version: 0.1.0
---
# Heavy Research (dispatch)

WHEN: research-dossier, banker-sourcing, any job needing real browsing or more depth than local
search + HTTP extraction can honestly deliver.

1. PROBE: ssh -o ConnectTimeout=5 mac 'echo up'
2. UP → dispatch per context/HEAVY-WORKER.md (in the environment-pack repo); retrieve; apply the
   deep-research gate to the RESULT (the gate is ours, not the worker's); file + deliver normally,
   noting "researched on Mac worker".
3. DOWN → tell Roshan: "Mac asleep — queued <job>. Run now in degraded local mode instead? (ddgs +
   HTTP extract, shallower)". Queue = output/queue/<job-id>.json; retry on next heartbeat + when any
   cron fires; deliver when done. Deadline-critical jobs (≤24h) auto-degrade rather than wait.

HARD RULE: the Mac worker is read-only on the world (research + local files only). All sends,
Notion writes, and deliveries happen from Hermes after the gate.
