#!/usr/bin/env python3
"""
notion_v3_mcp.py — stdio MCP server wrapping the private Notion api/v3 client (notion_v3.py).

Gives Claude Code native tools for the full-power Notion surface the OFFICIAL API can't reach:
row enumeration, double-unwrapped record reads, bulk prop/alive writes, page format, and raw
api/v3 escape hatches.

WHY STDLIB-ONLY (no `mcp` SDK):
  `.mcp.json` launches this with the bare `command: "python3"`. We cannot control which
  interpreter that PATH-resolves to (system 3.9 vs Homebrew 3.14). A dependency-free server
  written to the 3.9 baseline runs under *every* interpreter and needs zero `pip install`.
  So the "which python3" question stops mattering — that is the durability this needs.

PROTOCOL (MCP over stdio = newline-delimited JSON-RPC 2.0, NOT LSP Content-Length framing):
  - one JSON object per line on stdin; reply one JSON object per line on stdout.
  - stdout carries ONLY protocol messages. ALL logging goes to stderr.
  - requests have an `id` and get a response; notifications have no `id` and get NO response.
  - `initialize` echoes the client's protocolVersion, advertises tools capability + serverInfo.

SECURITY: the token lives in ./.env (gitignored), read at runtime by notion_v3._load_env.
  Nothing secret is hard-coded here. token_v2 is a live session cookie — rotate when done.
"""
import json
import os
import sys
import traceback

# Make `import notion_v3` work no matter the launch cwd (Claude Code may spawn from elsewhere).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import notion_v3  # noqa: E402

SERVER_NAME = "notion-v3"
SERVER_VERSION = "1.0.0"
DEFAULT_PROTOCOL_VERSION = "2024-11-05"


def log(msg):
    """All logging -> stderr. stdout is reserved for JSON-RPC frames."""
    sys.stderr.write("[notion-v3-mcp] " + str(msg) + "\n")
    sys.stderr.flush()


# ---------------------------------------------------------------------------
# Tool implementations — thin wrappers over notion_v3. Each returns a
# JSON-serializable Python object; the dispatcher renders it to text content.
# ---------------------------------------------------------------------------

def t_enumerate_rows(collection_id, view_id):
    """Enumerate ALL rows of a collection via a view (the official-API-can't move)."""
    rows, has_more = notion_v3.dump_rows(collection_id, view_id)
    return {"count": len(rows), "hasMore": has_more, "rows": rows}


def t_read_record(table, id):
    """Full record, double-unwrapped (recordMap[table][id].value.value)."""
    rec = notion_v3._rec(table, id)
    return {"table": table, "id": id, "record": rec}


def t_collection_schema(collection_id):
    """Map prop_id -> {name, type} for a collection."""
    return {"collection_id": collection_id, "schema": notion_v3.collection_schema(collection_id)}


def t_set_page_format(page_id, full_width=None, font=None):
    """Set full-width and/or font on a page. Returns the saveTransactions result (or null if no-op)."""
    if full_width is None and font is None:
        return {"error": "supply at least one of full_width or font"}
    return {"result": notion_v3.set_page_format(page_id, full_width=full_width, font=font)}


def t_bulk_set(block_ids, path, value):
    """
    Set a single prop/path to `value` on MANY blocks in ONE transaction.
    e.g. bulk-archive: path=["alive"], value=false.
    `value` is polymorphic (bool for ["alive"], string/array elsewhere) — passed through as-is.
    """
    ops = [notion_v3.op(bid, path, "set", value) for bid in block_ids]
    res = notion_v3.save_transactions(ops)
    return {"updated_blocks": len(block_ids), "path": path, "result": res}


def t_save_transactions(operations):
    """Raw saveTransactionsFanout escape hatch — caller supplies the operations[] array."""
    return {"result": notion_v3.save_transactions(operations)}


def t_raw(endpoint, payload):
    """Raw api/v3 escape hatch: POST `payload` to `endpoint`, return the parsed JSON."""
    return {"result": notion_v3.request(endpoint, payload)}


# ---------------------------------------------------------------------------
# Tool registry: name -> (handler, inputSchema, description)
# ---------------------------------------------------------------------------
TOOLS = [
    {
        "name": "notion_enumerate_rows",
        "description": (
            "Enumerate ALL rows of a Notion collection (database) through a view, returning each "
            "row's id, title, created timestamp, and alive flag. This is the enumeration the "
            "OFFICIAL Notion API cannot do. Needs the collection_id and a view_id of that collection."
        ),
        "handler": t_enumerate_rows,
        "inputSchema": {
            "type": "object",
            "properties": {
                "collection_id": {"type": "string", "description": "Collection (data source) id."},
                "view_id": {"type": "string", "description": "A view id belonging to that collection."},
            },
            "required": ["collection_id", "view_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "notion_read_record",
        "description": (
            "Read a full Notion record by table + id, double-unwrapped "
            "(recordMap[table][id].value.value). table is e.g. 'block', 'collection', "
            "'collection_view', 'space', 'notion_user'. Returns the raw record object."
        ),
        "handler": t_read_record,
        "inputSchema": {
            "type": "object",
            "properties": {
                "table": {"type": "string", "description": "Record table, e.g. 'block' or 'collection'."},
                "id": {"type": "string", "description": "The record id (dashed or dashless)."},
            },
            "required": ["table", "id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "notion_collection_schema",
        "description": (
            "Return a collection's schema as a map of prop_id -> {name, type}. Use this to learn "
            "the internal property ids needed for bulk_set / save_transactions writes."
        ),
        "handler": t_collection_schema,
        "inputSchema": {
            "type": "object",
            "properties": {
                "collection_id": {"type": "string", "description": "Collection (data source) id."},
            },
            "required": ["collection_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "notion_set_page_format",
        "description": (
            "Set page-level format on a Notion page: full_width (bool) and/or font (string, e.g. "
            "'default', 'serif', 'mono'). These cannot be set via the official API. Supply at least one."
        ),
        "handler": t_set_page_format,
        "inputSchema": {
            "type": "object",
            "properties": {
                "page_id": {"type": "string", "description": "The page (block) id to format."},
                "full_width": {"type": "boolean", "description": "Enable/disable full-width layout."},
                "font": {"type": "string", "description": "Page font name, e.g. 'default', 'serif', 'mono'."},
            },
            "required": ["page_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "notion_bulk_set",
        "description": (
            "Set ONE property/path to a value on MANY blocks in a single transaction. "
            "Classic use: bulk-archive rows with path=[\"alive\"] and value=false. "
            "`value` is polymorphic (bool for [\"alive\"], string/array for other paths) and is "
            "passed through unchanged. `path` is the array of keys into the block record."
        ),
        "handler": t_bulk_set,
        "inputSchema": {
            "type": "object",
            "properties": {
                "block_ids": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Block ids to update.",
                },
                "path": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Path into the block record, e.g. [\"alive\"] or [\"properties\",\"<propId>\"].",
                },
                "value": {
                    "description": "Value to set. Polymorphic: bool for [\"alive\"], else string/array/object.",
                },
            },
            "required": ["block_ids", "path", "value"],
            "additionalProperties": False,
        },
    },
    {
        "name": "notion_save_transactions",
        "description": (
            "Raw saveTransactionsFanout escape hatch. Supply the `operations` array directly "
            "(each op: {pointer:{table,id,spaceId}, path, command, args}). Use notion_raw + "
            "the op helper's shape when bulk_set isn't expressive enough."
        ),
        "handler": t_save_transactions,
        "inputSchema": {
            "type": "object",
            "properties": {
                "operations": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "Array of saveTransactions operation objects.",
                },
            },
            "required": ["operations"],
            "additionalProperties": False,
        },
    },
    {
        "name": "notion_raw",
        "description": (
            "Raw Notion api/v3 escape hatch: POST `payload` to api/v3 `endpoint` (e.g. "
            "'queryCollection', 'loadUserContent', 'syncRecordValuesSpace') and return the parsed "
            "JSON response. Full power — use when no higher-level tool fits."
        ),
        "handler": t_raw,
        "inputSchema": {
            "type": "object",
            "properties": {
                "endpoint": {"type": "string", "description": "api/v3 endpoint name (no leading slash)."},
                "payload": {"type": "object", "description": "JSON request body."},
            },
            "required": ["endpoint", "payload"],
            "additionalProperties": False,
        },
    },
]

TOOLS_BY_NAME = dict((tool["name"], tool) for tool in TOOLS)


def tools_list_payload():
    return [
        {"name": t["name"], "description": t["description"], "inputSchema": t["inputSchema"]}
        for t in TOOLS
    ]


# ---------------------------------------------------------------------------
# JSON-RPC plumbing
# ---------------------------------------------------------------------------

def send(message):
    """Write one JSON-RPC frame (newline-delimited) to stdout."""
    sys.stdout.write(json.dumps(message) + "\n")
    sys.stdout.flush()


def make_result(req_id, result):
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def make_error(req_id, code, message):
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


def handle_initialize(params):
    client_proto = (params or {}).get("protocolVersion") or DEFAULT_PROTOCOL_VERSION
    return {
        "protocolVersion": client_proto,
        "capabilities": {"tools": {}},
        "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
    }


def handle_tools_call(params):
    """Returns an MCP tools/call result dict: {content:[...], isError:bool}."""
    name = (params or {}).get("name")
    arguments = (params or {}).get("arguments") or {}
    tool = TOOLS_BY_NAME.get(name)
    if tool is None:
        return {
            "content": [{"type": "text", "text": "Unknown tool: " + str(name)}],
            "isError": True,
        }
    # CRITICAL: notion_v3.request raises SystemExit (a BaseException, NOT Exception) on any
    # HTTP error. A bare `except Exception` would let it kill the server on the first live
    # error. Catch BaseException so the server survives and reports the failure as tool output.
    try:
        result = tool["handler"](**arguments)
        text = json.dumps(result, indent=2, default=str)
        return {"content": [{"type": "text", "text": text}], "isError": False}
    except BaseException as exc:  # noqa: BLE001 — intentional; see note above.
        tb = traceback.format_exc()
        log("tool '" + str(name) + "' failed: " + repr(exc) + "\n" + tb)
        return {
            "content": [{"type": "text", "text": "Tool '" + str(name) + "' error: " + repr(exc)}],
            "isError": True,
        }


def dispatch(message):
    """
    Process one parsed JSON-RPC message. Returns a response dict, or None for
    notifications (no `id`) and post-shutdown signals.
    """
    method = message.get("method")
    req_id = message.get("id")
    params = message.get("params") or {}
    is_notification = "id" not in message

    # Notifications (incl. notifications/initialized, notifications/cancelled) get NO response.
    if is_notification:
        return None

    if method == "initialize":
        return make_result(req_id, handle_initialize(params))
    if method == "ping":
        return make_result(req_id, {})
    if method == "tools/list":
        return make_result(req_id, {"tools": tools_list_payload()})
    if method == "tools/call":
        return make_result(req_id, handle_tools_call(params))

    # Methods we don't implement (resources/list, prompts/list, etc.) — proper JSON-RPC error.
    return make_error(req_id, -32601, "Method not found: " + str(method))


def main():
    log("starting; %d tools; python %s" % (len(TOOLS), sys.version.split()[0]))
    # Synchronous line loop — no asyncio, 3.9-safe.
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except ValueError:
            # Can't recover an id from unparseable input; per JSON-RPC use null id.
            send(make_error(None, -32700, "Parse error"))
            continue
        try:
            response = dispatch(message)
        except BaseException as exc:  # never let a handler bug kill the loop
            log("dispatch error: " + repr(exc) + "\n" + traceback.format_exc())
            response = make_error(message.get("id"), -32603, "Internal error: " + repr(exc))
        if response is not None:
            send(response)
    log("stdin closed; exiting")


if __name__ == "__main__":
    main()
