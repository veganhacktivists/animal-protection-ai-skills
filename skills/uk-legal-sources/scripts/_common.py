"""Shared helpers. Standard library only."""
import json, re, sys, time, html
import urllib.request, urllib.parse, urllib.error

UA = "uk-legal-sources-skill (research; contact via user)"
_last = {}

def get(url, delay=0.0, accept=None, timeout=60):
    """GET a URL politely. `delay` = minimum seconds between requests to the same host."""
    host = urllib.parse.urlparse(url).netloc
    wait = _last.get(host, 0) + delay - time.time()
    if wait > 0:
        time.sleep(wait)
    hdrs = {"User-Agent": UA}
    if accept:
        hdrs["Accept"] = accept
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            _last[host] = time.time()
            return r.status, r.headers.get("Content-Type", ""), data
    except urllib.error.HTTPError as e:
        _last[host] = time.time()
        status, ctype, body = e.code, e.headers.get("Content-Type", "") if e.headers else "", e.read()
        if blocked_by_own_network(status, body):
            _warn_network(host, body[:200].decode("utf-8", "ignore"))
        return status, ctype, body
    except (urllib.error.URLError, OSError) as e:
        # No answer from the site at all: usually the AI tool's own network settings.
        reason = str(getattr(e, "reason", e))
        _warn_network(host, reason)
        return 0, "", reason.encode()

def blocked_by_own_network(status, body):
    """True when the block came from the user's own environment (a proxy or allowlist), not the site."""
    t = body[:2000].decode("utf-8", "ignore").lower()
    return status == 0 or (status == 403 and any(w in t for w in ("allowlist", "egress", "proxy")))

def _warn_network(host, reason):
    print(f"NETWORK: could not reach {host} ({reason.strip()[:150]}). If this is one of the data feeds "
          "this skill uses, your AI tool's network settings are probably blocking it. See README.md, "
          "'Letting your AI reach the data feeds'.", file=sys.stderr)

def looks_blocked(status, body):
    t = body[:4000].decode("utf-8", "ignore").lower()
    return status in (403, 429, 503) or "just a moment" in t or "not a bot" in t or "enable javascript and cookies" in t

def strip_tags(s):
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"</(p|div|h\d|li|tr|br)>|<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()

def die(msg, code=1):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)

def out(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))
