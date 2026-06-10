# NIM 200 RPM bump request — ready to file (Plan 14 Task 1 Step 3)

File at: https://forums.developer.nvidia.com → "Access/Accounts" category (same place as the
precedent threads). Free; takes minutes. Until granted: REDUCED crons only (brief + heartbeat),
≥15 min stagger in the 06:00–09:00 window.

---

**Title:** API rate limit increase request — personal agent workload (40 → 200 RPM)

**Body:**

Hi — I'm running a personal AI agent (Hermes Agent, open-source, by Nous Research) on the
build.nvidia.com API, with `nvidia/nemotron-3-super-120b-a12b` as its primary model.

Could my account's rate limit be raised from the default 40 RPM to 200 RPM?

Context: the agent runs scheduled jobs (a morning brief, research digests, and monitoring tasks)
that execute multi-step tool-calling loops — a single job can make 15–30 chat-completion calls in
a few minutes, so several jobs in the same morning window bump into the 40 RPM ceiling even when
total daily volume is modest. Single API key, personal (non-commercial) use.

API key email: [ROSHAN — your build.nvidia.com account email]

Thanks!
