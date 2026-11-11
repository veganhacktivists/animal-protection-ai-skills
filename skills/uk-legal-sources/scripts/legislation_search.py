#!/usr/bin/env python3
"""Search legislation.gov.uk by title or full text and return the COMPLETE result list.

The site's search feed is not relevance-ranked, so this fetches every page (20 per page)
and honours the site's requested 5-second gap between requests.

Usage:
  legislation_search.py --text '"unnecessary suffering"' [--text sentience ...]
  legislation_search.py --title "animal welfare"
  legislation_search.py --text docking --type ukpga      # limit to Acts (ukpga, uksi, asp, wsi, nisr, eur...)
  legislation_search.py --text X --max-pages 3            # cap pages while exploring

Output: JSON list of {title, url, year, number, type, query}. Duplicates across queries are merged.
Quote multi-word phrases: unquoted phrases give poor results. Results carry NO in-force status;
open each hit (legislation_fetch.py) to check for repeal/revocation.
"""
import argparse, sys, urllib.parse, xml.etree.ElementTree as ET
from _common import get, die, out, looks_blocked

A = "{http://www.w3.org/2005/Atom}"
OS = "{http://a9.com/-/spec/opensearch/1.1/}"
UKM = "{http://www.legislation.gov.uk/namespaces/metadata}"
DELAY = 5.0

def search(param, value, typ, max_pages):
    base = f"https://www.legislation.gov.uk/{typ or 'all'}/data.feed"
    page, total, items = 1, None, []
    while True:
        url = base + "?" + urllib.parse.urlencode({param: value, "page": page})
        status, ctype, body = get(url, delay=DELAY)
        if looks_blocked(status, body) or status != 200:
            die(f"{url} returned HTTP {status}")
        root = ET.fromstring(body)
        if total is None:
            t = root.find(OS + "totalResults")
            total = int(t.text) if t is not None and t.text else 0
        entries = root.findall(A + "entry")
        for e in entries:
            link = e.find(A + "link")
            title = (e.findtext(A + "title") or "").strip()
            items.append({
                "title": title,
                "url": (link.get("href") if link is not None else "").replace("/id/", "/"),
                "year": e.find(UKM + "Year").get("Value") if e.find(UKM + "Year") is not None else None,
                "number": e.find(UKM + "Number").get("Value") if e.find(UKM + "Number") is not None else None,
                "type": e.find(UKM + "DocumentMainType").get("Value") if e.find(UKM + "DocumentMainType") is not None else None,
                "query": f"{param}={value}",
            })
        if not entries or len(items) >= total or (max_pages and page >= max_pages):
            break
        page += 1
    return total, items

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--text", action="append", default=[], help="full-text query (repeatable; quote phrases)")
    ap.add_argument("--title", action="append", default=[], help="title query (repeatable)")
    ap.add_argument("--type", default=None, help="legislation type code, e.g. ukpga, uksi, asp, wsi, nisr, eur")
    ap.add_argument("--max-pages", type=int, default=0, help="stop after N pages (0 = all)")
    args = ap.parse_args()
    if not args.text and not args.title:
        ap.error("give at least one --text or --title")
    merged, totals = {}, {}
    for q in args.text:
        total, items = search("text", q, args.type, args.max_pages)
        totals[f"text={q}"] = total
        for it in items: merged.setdefault(it["url"], it)
    for q in args.title:
        total, items = search("title", q, args.type, args.max_pages)
        totals[f"title={q}"] = total
        for it in items: merged.setdefault(it["url"], it)
    print(f"# totals per query: {totals}  | unique results: {len(merged)}", file=sys.stderr)
    out(list(merged.values()))
