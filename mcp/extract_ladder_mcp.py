#!/usr/bin/env python3
"""
extract_ladder_mcp.py — stdio MCP server: the Compaq extraction ladder (Plan 14).

Tier 1: crawl4ai HTTP-only (no browser, no Playwright launch) -> markdown
Tier 2: Lightpanda over CDP (ONLY if LIGHTPANDA_CDP_URL env is set AND playwright
        client importable; JS-needing but non-SPA pages; empty DOM = MISS)
Tier 3: structured escalate signal -> the agent routes to the heavy-research skill
        (Claude Code on the Mac). A miss NEVER silently fails a task.

Stdlib-only protocol (same newline-delimited JSON-RPC pattern as notion_v3_mcp.py);
heavy deps (crawl4ai, playwright) are lazy-imported and fully optional — the tool
degrades honestly and reports which tiers exist via extract_status.
"""
import asyncio
import json
import os
import re
import sys

SERVER_NAME = "extract-ladder"
SERVER_VERSION = "1.0.0"
DEFAULT_PROTOCOL_VERSION = "2024-11-05"

# Login-walled / SPA domains: Tier 1/2 are structurally blind here — straight to Tier 3.
SPA_BLOCKLIST = (
    "linkedin.com", "x.com", "twitter.com", "instagram.com", "facebook.com",
    "reddit.com", "tiktok.com", "notion.so", "docs.google.com",
)
MIN_USEFUL_CHARS = 80  # below this, a fetch is a MISS (JS shells are <50 chars); short real pages still pass


def log(msg):
    sys.stderr.write("[extract-ladder-mcp] " + str(msg) + "\n")
    sys.stderr.flush()


def _domain_blocked(url):
    m = re.match(r"https?://([^/]+)", url or "")
    host = (m.group(1) if m else "").lower()
    return any(host == d or host.endswith("." + d) for d in SPA_BLOCKLIST)


def _escalate(url, reason):
    return {
        "tier": 3,
        "url": url,
        "action": "escalate_heavy_research",
        "reason": reason,
        "note": "Dispatch via the heavy-research skill (Mac worker). Do NOT retry tiers 1-2.",
    }


# ---------------------------------------------------------------- Tier 1
def _tier1_crawl4ai(url):
    """crawl4ai with the HTTP-only strategy. Returns markdown or None on miss."""
    try:
        from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
        from crawl4ai.async_crawler_strategy import AsyncHTTPCrawlerStrategy
    except Exception as e:  # noqa: BLE001 — any import failure = tier unavailable
        log(f"tier1 unavailable (crawl4ai import: {e})")
        return None

    async def run():
        async with AsyncWebCrawler(crawler_strategy=AsyncHTTPCrawlerStrategy()) as crawler:
            res = await crawler.arun(url=url, config=CrawlerRunConfig(verbose=False))
            md = getattr(res, "markdown", None)
            return str(md) if md else None

    try:
        return asyncio.run(run())
    except Exception as e:  # noqa: BLE001
        log(f"tier1 fetch failed: {e}")
        return None


def _tier1_stdlib(url):
    """Degraded fallback when crawl4ai is absent: stdlib fetch + tag-strip."""
    import html
    import urllib.request

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read(2_000_000).decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        log(f"tier1-degraded fetch failed: {e}")
        return None
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    text = re.sub(r"(?s)<[^>]+>", " ", raw)
    text = html.unescape(re.sub(r"[ \t]+", " ", text))
    text = "\n".join(ln.strip() for ln in text.splitlines() if ln.strip())
    return text or None


# ---------------------------------------------------------------- Tier 2
def _tier2_lightpanda(url):
    """Lightpanda via CDP. Only if LIGHTPANDA_CDP_URL set; empty DOM = miss (None)."""
    cdp = os.environ.get("LIGHTPANDA_CDP_URL", "").strip()
    if not cdp:
        return None
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:  # noqa: BLE001
        log(f"tier2 unavailable (playwright import: {e})")
        return None
    try:
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(cdp)
            page = browser.new_page()
            page.goto(url, timeout=30_000)
            text = page.evaluate("() => document.body ? document.body.innerText : ''")
            browser.close()
            return text or None
    except Exception as e:  # noqa: BLE001
        log(f"tier2 failed: {e}")
        return None


# ---------------------------------------------------------------- tools
def t_extract_url(url, max_chars=12000):
    if not re.match(r"^https?://", url or ""):
        return {"error": f"not an http(s) url: {url!r}"}
    if _domain_blocked(url):
        return _escalate(url, "login-walled/SPA domain — tiers 1-2 structurally blind here")

    md = _tier1_crawl4ai(url)
    tier_label = 1
    if md is None:
        md = _tier1_stdlib(url)
        tier_label = "1-degraded" if md else 1
    if md and len(md.strip()) >= MIN_USEFUL_CHARS:
        out = md.strip()
        return {"tier": tier_label, "url": url, "chars": len(out),
                "truncated": len(out) > max_chars, "markdown": out[:max_chars]}

    dom = _tier2_lightpanda(url)
    if dom and len(dom.strip()) >= MIN_USEFUL_CHARS:
        out = dom.strip()
        return {"tier": 2, "url": url, "chars": len(out),
                "truncated": len(out) > max_chars, "markdown": out[:max_chars]}

    return _escalate(url, "tier 1 thin/failed"
                     + ("; tier 2 miss (empty/near-empty DOM)" if dom is not None
                        else "; tier 2 not available"))


def t_extract_status():
    status = {"tier1_crawl4ai": False, "tier1_degraded_stdlib": True,
              "tier2_lightpanda_cdp": False, "tier3_escalation": "always available (heavy-research)"}
    try:
        import crawl4ai  # noqa: F401
        status["tier1_crawl4ai"] = True
    except Exception:  # noqa: BLE001
        pass
    cdp = os.environ.get("LIGHTPANDA_CDP_URL", "").strip()
    if cdp:
        try:
            import playwright  # noqa: F401
            status["tier2_lightpanda_cdp"] = cdp
        except Exception:  # noqa: BLE001
            pass
    status["spa_blocklist"] = list(SPA_BLOCKLIST)
    return status


TOOLS = [
    {
        "name": "extract_url",
        "description": (
            "Extract readable content from a URL via the Compaq extraction ladder: "
            "Tier 1 crawl4ai HTTP-only (default) -> Tier 2 Lightpanda CDP (only if configured; "
            "non-SPA JS pages) -> Tier 3 escalate. SPA/login-walled domains (LinkedIn etc.) and "
            "all misses return action=escalate_heavy_research — then USE THE heavy-research SKILL; "
            "never treat an escalation as a failure and never retry lower tiers."
        ),
        "handler": lambda url, max_chars=12000: t_extract_url(url, max_chars),
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "http(s) URL to extract"},
                "max_chars": {"type": "integer", "description": "cap on returned markdown (default 12000)"},
            },
            "required": ["url"],
            "additionalProperties": False,
        },
    },
    {
        "name": "extract_status",
        "description": "Report which extraction tiers are available on this host (crawl4ai / Lightpanda CDP / escalation).",
        "handler": lambda: t_extract_status(),
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
]


# ------------------------------------------------------- JSON-RPC plumbing
def _resp(rid, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": rid}
    if error is not None:
        msg["error"] = error
    else:
        msg["result"] = result
    return msg


def handle(req):
    method, rid, params = req.get("method"), req.get("id"), req.get("params") or {}
    if method == "initialize":
        return _resp(rid, {
            "protocolVersion": params.get("protocolVersion", DEFAULT_PROTOCOL_VERSION),
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })
    if method in ("notifications/initialized", "notifications/cancelled"):
        return None
    if method == "tools/list":
        return _resp(rid, {"tools": [
            {"name": t["name"], "description": t["description"], "inputSchema": t["inputSchema"]}
            for t in TOOLS]})
    if method == "tools/call":
        name, args = params.get("name"), params.get("arguments") or {}
        tool = next((t for t in TOOLS if t["name"] == name), None)
        if tool is None:
            return _resp(rid, error={"code": -32602, "message": f"unknown tool {name!r}"})
        try:
            out = tool["handler"](**args)
            return _resp(rid, {"content": [{"type": "text", "text": json.dumps(out, ensure_ascii=False)}]})
        except Exception as e:  # noqa: BLE001
            log(f"tool {name} crashed: {e}")
            return _resp(rid, {"content": [{"type": "text", "text": json.dumps({"error": str(e)})}],
                               "isError": True})
    if rid is not None:
        return _resp(rid, error={"code": -32601, "message": f"method {method!r} not supported"})
    return None


def main():
    log("ready")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError as e:
            log(f"bad json: {e}")
            continue
        out = handle(req)
        if out is not None:
            sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
