#!/usr/bin/env python3
"""Search Find Case Law (The National Archives) and fetch judgments. Not bot-blocked; no key needed.

Usage:
  caselaw_search.py "Animal Welfare Act 2006" [--from 2020-01-01] [--to 2026-12-31] [--court ewca/crim] [--max-pages 3]
  caselaw_search.py --judgment https://caselaw.nationalarchives.gov.uk/ewhc/admin/2025/1383   # full text

Search output: JSON list of {name, citation, court, date, url}. Judgment output: clean text to stdout.

Licence note: reading and quoting individual judgments is fine under the standard licence. Running this
across many judgments to extract or classify information counts as "computational analysis" and needs
The National Archives' free licence: https://caselaw.nationalarchives.gov.uk/about-this-service
Coverage is England & Wales plus UKSC/Privy Council, mostly 2001 onwards. For Scotland, NI, older cases,
the House of Lords or tribunals not covered, use BAILII in a real browser.
"""
import argparse, re, sys, urllib.parse, xml.etree.ElementTree as ET
from _common import get, die, out, strip_tags, looks_blocked

A = "{http://www.w3.org/2005/Atom}"
TNA = "{https://caselaw.nationalarchives.gov.uk}"
BASE = "https://caselaw.nationalarchives.gov.uk"

def search(q, start, end, court, max_pages):
    rows, page = [], 1
    while True:
        p = {"query": q, "page": page, "order": "-date"}
        if start: p["from_date_0"], p["from_date_1"], p["from_date_2"] = start.split("-")[::-1]
        if end: p["to_date_0"], p["to_date_1"], p["to_date_2"] = end.split("-")[::-1]
        if court: p["court"] = court
        url = f"{BASE}/atom.xml?" + urllib.parse.urlencode(p)
        status, ctype, body = get(url, delay=1.0)
        if status != 200 or looks_blocked(status, body):
            die(f"{url} returned HTTP {status}")
        root = ET.fromstring(body)
        entries = root.findall(A + "entry")
        for e in entries:
            link = next((l.get("href") for l in e.findall(A + "link") if l.get("rel") in (None, "alternate")), None)
            rows.append({
                "name": (e.findtext(A + "title") or "").strip(),
                "citation": (e.findtext(TNA + "identifier") or e.findtext(A + "id") or "").strip(),
                "court": (e.findtext(A + "author/" + A + "name") or "").strip(),
                "date": (e.findtext(A + "published") or e.findtext(A + "updated") or "")[:10],
                "url": link,
            })
        nxt = any(l.get("rel") == "next" for l in root.findall(A + "link"))
        if not entries or not nxt or (max_pages and page >= max_pages):
            break
        page += 1
    return rows

def judgment(url):
    url = re.sub(r"/(data\.xml|data\.pdf)?/?$", "", url.strip()) + "/data.xml"
    status, ctype, body = get(url)
    if status != 200 or looks_blocked(status, body):
        die(f"{url} returned HTTP {status}")
    x = body.decode("utf-8", "ignore")
    x = re.sub(r"<meta>.*?</meta>", "", x, flags=re.S)  # identifiers, CSS and other metadata
    x = re.sub(r"</(p|paragraph|heading|num|judge|party|docTitle|neutralCitation|date|level|content)>", "\n", x)
    print(f"# source: {url}", file=sys.stderr)
    return strip_tags(x)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?")
    ap.add_argument("--from", dest="start"); ap.add_argument("--to", dest="end")
    ap.add_argument("--court", help="court code, e.g. ewca/crim, ewhc/admin, uksc")
    ap.add_argument("--max-pages", type=int, default=3)
    ap.add_argument("--judgment", help="judgment URL to fetch in full")
    a = ap.parse_args()
    if a.judgment:
        print(judgment(a.judgment))
    elif a.query:
        out(search(a.query, a.start, a.end, a.court, a.max_pages))
    else:
        ap.error("give a query or --judgment URL")
