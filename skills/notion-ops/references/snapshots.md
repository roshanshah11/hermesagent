# Snapshot protocol (before any bulk write: >5 rows OR any archive sweep)
1. Enumerate the target collection (notion_enumerate_rows) and read each affected record.
2. Dump JSON to output/snapshots/YYYY-MM-DD-HHMM-<collection>-<action>.json (gitignored dir).
3. Proceed with the write. Note the snapshot filename in the Change Log row's Note field.
ROLLBACK: read the snapshot, restore prior values via save_transactions (alive flags, properties).
Precedent: hub_content_snapshot.json saved the cockpit rebuild in the Notion project.
