# Verified api/v3 write recipes (derived + readback-verified live, 2026-06-10)

These are the EXACT op shapes that work. Use notion_save_transactions with these; do not improvise
transaction structures ("Invalid ancestor path" = you omitted the parent update op or space_id).

## Create a row in any collection
```json
[
 {"pointer":{"table":"block","id":"<NEW_UUID4>","spaceId":"<SPACE>"},"path":[],"command":"set",
  "args":{"type":"page","id":"<NEW_UUID4>","version":1,"space_id":"<SPACE>"}},
 {"pointer":{"table":"block","id":"<NEW_UUID4>","spaceId":"<SPACE>"},"path":[],"command":"update",
  "args":{"parent_id":"<COLLECTION_ID>","parent_table":"collection","alive":true}},
 {"pointer":{"table":"block","id":"<NEW_UUID4>","spaceId":"<SPACE>"},"path":["properties","title"],
  "command":"set","args":[["<TITLE TEXT>"]]},
 {"pointer":{"table":"block","id":"<NEW_UUID4>","spaceId":"<SPACE>"},"path":["created_time"],
  "command":"set","args":<NOW_EPOCH_MS>}
]
```
Generate the uuid4 yourself. All ops in ONE save_transactions call.

## Property value shapes (path = ["properties", "<PROP_ID>"], command = "set")
- text/title: `[["some text"]]`
- date/datetime (timezone-safe — preferred over offset strings):
  `[["‣",[["d",{"type":"datetime","start_date":"YYYY-MM-DD","start_time":"HH:MM","time_zone":"America/New_York"}]]]]`
  (all-day: `{"type":"date","start_date":"YYYY-MM-DD"}`)
- select: `[["<Option Name>"]]` (must match an existing option value exactly, e.g. "Hermes")
- checkbox: `[["Yes"]]` / `[["No"]]`
- relation: `[["‣",[["p","<TARGET_ROW_ID>","<SPACE>"]]]]`

## Archive a row (NEVER delete)
```json
[{"pointer":{"table":"block","id":"<ROW_ID>","spaceId":"<SPACE>"},"path":[],"command":"update",
  "args":{"alive":false}}]
```

## Change Log row (collection 6da623fd-465d-41fc-a1c8-a5e1ea19787b) — prop ids
title=Action · `;fB:`=Timestamp (date) · `a<nF`=Source (select; write "Hermes") ·
`EETH`=Entity (relation→Tasks) · `AG}\`=Before -> After (text) · `DIBp`=Note (text)

## Tasks DB key prop ids (collection cae4bcc3-c36d-4b78-9653-578fb735fd99)
title=Name · `]Fc}`=Due (date) · `Vy]j`=Status (select) · `?{G|`=Type (select) ·
`>>qF`=Priority (select) · `c:pn`=Area (select) · `bXBv`=Focus (checkbox) · `T{<o`=Notes (text)
(Full map: notion_collection_schema. `When`/`Time` are formulas — never write them.)
