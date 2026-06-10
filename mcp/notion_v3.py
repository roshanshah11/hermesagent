#!/usr/bin/env python3
"""
notion_v3.py — client for Notion's PRIVATE api/v3 (what the desktop/web app uses).

Unlocks what the official API can't: full row enumeration, bulk ops, column layout,
page format (full-width / font). Auth via NOTION_TOKEN_V2 in ./.env (gitignored).
token_v2 is a live session cookie — rotate when done.

Verified shapes (2026-06-08, this workspace):
  - records double-wrap: recordMap[table][id].value.value = the record
  - queryCollection -> result.reducerResults.collection_group_results.{blockIds,hasMore}
  - writes via saveTransactionsFanout: transactions[].operations[] {pointer,path,command,args}
"""
import json, os, sys, time, uuid, urllib.request, urllib.error

BASE = "https://www.notion.so/api/v3/"


def _load_env(path=None):
    path = path or os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    env = {}
    for line in open(path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


_ENV = _load_env()
TOKEN, SPACE_ID, USER_ID = _ENV["NOTION_TOKEN_V2"], _ENV.get("NOTION_SPACE_ID", ""), _ENV.get("NOTION_USER_ID", "")
TZ = "America/New_York"


def request(endpoint, payload):
    req = urllib.request.Request(BASE + endpoint, data=json.dumps(payload).encode(), method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("cookie", f"token_v2={TOKEN}")
    req.add_header("x-notion-active-user-header", USER_ID)
    req.add_header("notion-audit-log-platform", "web")
    req.add_header("User-Agent", "Mozilla/5.0")
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP {e.code} on {endpoint}: {e.read().decode()[:600]}")


def _rec(table, rid):
    rm = request("syncRecordValuesSpace",
                 {"requests": [{"pointer": {"table": table, "id": rid, "spaceId": SPACE_ID}, "version": -1}]}).get("recordMap", {})
    node = rm.get(table, {}).get(rid, {})
    return (node.get("value", {}) or {}).get("value", {})  # double-unwrap


def inspect_block(block_id):
    return _rec("block", block_id)


def collection_schema(collection_id):
    """Return {prop_id: {'name','type'}} for a collection."""
    return _rec("collection", collection_id).get("schema", {})


def query_collection(collection_id, view_id, limit=2000):
    """One call; returns (blockIds, hasMore, recordMap_blocks)."""
    p = {"source": {"type": "collection", "id": collection_id, "spaceId": SPACE_ID},
         "collectionView": {"id": view_id, "spaceId": SPACE_ID},
         "loader": {"type": "reducer",
                    "reducers": {"collection_group_results": {"type": "results", "limit": limit, "loadContentCover": False}},
                    "searchQuery": "", "sort": [], "userTimeZone": TZ}}
    o = request("queryCollection", p)
    cg = o.get("result", {}).get("reducerResults", {}).get("collection_group_results", {})
    blocks = {bid: (v.get("value", {}) or {}).get("value", {}) for bid, v in o.get("recordMap", {}).get("block", {}).items()}
    return cg.get("blockIds", []), cg.get("hasMore", False), blocks


def dump_rows(collection_id, view_id):
    """All rows with id, title, created_iso, alive."""
    ids, more, blocks = query_collection(collection_id, view_id)
    rows = []
    for bid in ids:
        v = blocks.get(bid, {})
        title = ""
        t = (v.get("properties", {}) or {}).get("title")
        if t and t[0]:
            title = "".join(seg[0] for seg in t if seg)
        ct = v.get("created_time")
        rows.append({"id": bid, "title": title,
                     "created": time.strftime("%Y-%m-%d %H:%M", time.localtime(ct / 1000)) if ct else None,
                     "alive": v.get("alive")})
    return rows, more


# ---- writes ----
def save_transactions(operations):
    txn = {"id": str(uuid.uuid4()), "spaceId": SPACE_ID, "operations": operations}
    return request("saveTransactionsFanout", {"requestId": str(uuid.uuid4()), "transactions": [txn]})


def op(block_id, path, command, args):
    return {"pointer": {"table": "block", "id": block_id, "spaceId": SPACE_ID},
            "path": path, "command": command, "args": args}


def set_page_format(page_id, full_width=None, font=None):
    ops = []
    if full_width is not None:
        ops.append(op(page_id, ["format", "page_full_width"], "set", bool(full_width)))
    if font is not None:
        ops.append(op(page_id, ["format", "page_font"], "set", font))
    return save_transactions(ops) if ops else None


def _cli():
    a = sys.argv
    if len(a) < 2:
        print("usage: whoami | inspect ID | dump COLLID VIEWID | fullwidth PAGEID [0|1] | font PAGEID NAME | raw EP JSON")
        return
    c = a[1]
    if c == "whoami":
        rm = request("loadUserContent", {}).get("recordMap", {})
        print(json.dumps({"spaces": list(rm.get("space", {}).keys()), "user": USER_ID}, indent=2))
    elif c == "inspect":
        b = inspect_block(a[2])
        print(json.dumps({"type": b.get("type"), "collection_id": b.get("collection_id"),
                          "view_ids": b.get("view_ids"), "format": b.get("format"),
                          "content_len": len(b.get("content", [])), "parent": b.get("parent_id")}, indent=2))
    elif c == "dump":
        rows, more = dump_rows(a[2], a[3])
        print(json.dumps({"count": len(rows), "hasMore": more, "rows": rows}, indent=2))
    elif c == "fullwidth":
        val = bool(int(a[3])) if len(a) > 3 else True
        print(json.dumps(set_page_format(a[2], full_width=val), indent=2)[:400])
    elif c == "font":
        print(json.dumps(set_page_format(a[2], font=a[3]), indent=2)[:400])
    elif c == "raw":
        print(json.dumps(request(a[2], json.loads(a[3])), indent=2)[:3000])
    else:
        print("unknown")


if __name__ == "__main__":
    _cli()
