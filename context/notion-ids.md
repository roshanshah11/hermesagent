# Notion IDs Hermes uses (dashed or dashless both work)

- Tasks DB: collection cae4bcc3-c36d-4b78-9653-578fb735fd99 · view f0a2583d-ce2f-4e41-bfad-22aa291d4e18
- People DB: collection 5bb18055-a8c8-4dce-a671-4d7754f388bb · view bc10d6e9-0805-41d7-8685-6bc73784801d
- Change Log DB: collection 6da623fd-465d-41fc-a1c8-a5e1ea19787b · view 8a5f4e2e-f23d-404f-b574-75fe18b12636 (cols: Action title · Timestamp ·
  Source · Entity→Tasks rel · "Before -> After" · Note) — write Source=Hermes
- Control DB row (kill switch): 379b67c2-a997-8188-8db9-d4fa81162937 — if break mode ON, do not write
- Hub (delivery surface): 377b67c2-a997-8103-9b80-d4ebd521db07 · Archive page: 377b67c2-a997-8190-a880-d5244ddeb4a7
- Substack Posts: collection 369fbfdb-941c-497f-8aca-0bd092cbd2cb · view 9408c322-2c6a-4379-9824-02e57df9a538 (Stage: Idea→Research→Model→Thesis→Publish;
  Hermes owns Idea→Research only)
- Research Labs: 067e2e34-d635-45ef-a6cc-7ae9b44f928f · view 36e9d778-613d-4f49-ab60-4737bc3f945a
- Calls: 5fd16c2d-f547-4990-802d-7d7ada0e588b · view 507240eb-d525-4537-8245-3b740c028317
- IB Applications: ea517e94-9463-44ed-a62c-2a9b9ce9a97c · view 79e687f8-6d09-4176-a1fb-c488faa392b0
- Firms: 7a97423f-0c97-4e73-8a1f-9c42a0c475fe · view 52fb44e5-6c86-43e9-ad06-37584e392755
- Club Applications: 4be6eb2a-24e3-49ff-b6da-cbb4ffe8f4d9 · view 13d56c67-15ad-4979-8dce-e931d260f127
- Specialized Programs: 03ce5991-cd92-48e2-8cc2-ff895fc585ab · view 2c9275ea-f7dc-4a09-a30f-3f2188217830
- GTM/Client Acquisition: 33aa7489-78c3-4d3d-8b38-b525efced5d9 · view eda6ace9-1559-4f68-8ba4-3ca548e01d47
- Markets Idea List: 305bffe5-cd5f-4bae-8788-b8e337ded74d · view 8119a63a-962d-45c8-9228-d38bc9cf4d96
- Course Plan DB: collection 93b93826-79e1-44b5-a0a9-4131c9fbcd0d · view 88be2d03-eeef-4162-9769-41906f1438d2
- Tasks schema notes: `When` formula is computed from `Due` (opaque via API — recompute);
  UNIQUE_ID prefix TSK; relation Tasks↔People synced name "Tasks".
