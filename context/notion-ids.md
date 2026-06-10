# Notion IDs Hermes uses (dashed or dashless both work)

- Tasks DB: collection cae4bcc3-c36d-4b78-9653-578fb735fd99 · view f0a2583d-ce2f-4e41-bfad-22aa291d4e18
- People DB: collection 5bb18055-a8c8-4dce-a671-4d7754f388bb
- Change Log DB: collection 6da623fd-465d-41fc-a1c8-a5e1ea19787b (cols: Action title · Timestamp ·
  Source · Entity→Tasks rel · "Before -> After" · Note) — write Source=Hermes
- Control DB row (kill switch): 379b67c2-a997-8188-8db9-d4fa81162937 — if break mode ON, do not write
- Hub (delivery surface): 377b67c2-a997-8103-9b80-d4ebd521db07 · Archive page: 377b67c2-a997-8190-a880-d5244ddeb4a7
- Substack Posts: collection 369fbfdb-941c-497f-8aca-0bd092cbd2cb (Stage: Idea→Research→Model→Thesis→Publish;
  Hermes owns Idea→Research only)
- Research Labs: 067e2e34-d635-45ef-a6cc-7ae9b44f928f · Calls: 5fd16c2d-f547-4990-802d-7d7ada0e588b
- IB Applications: ea517e94-9463-44ed-a62c-2a9b9ce9a97c · Firms: 7a97423f-0c97-4e73-8a1f-9c42a0c475fe
- Club Applications: 4be6eb2a-24e3-49ff-b6da-cbb4ffe8f4d9 · Specialized Programs: 03ce5991-cd92-48e2-8cc2-ff895fc585ab
- GTM/Client Acquisition: 33aa7489-78c3-4d3d-8b38-b525efced5d9 · Markets Idea List: 305bffe5-cd5f-4bae-8788-b8e337ded74d
- Tasks schema notes: `When` formula is computed from `Due` (opaque via API — recompute);
  UNIQUE_ID prefix TSK; relation Tasks↔People synced name "Tasks".
