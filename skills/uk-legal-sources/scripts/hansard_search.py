#!/usr/bin/env python3
"""Search Hansard (Commons and Lords debates) through Parliament's open data feed, which is not bot-blocked.

Usage:
  hansard_search.py "animal welfare" --from 2022-01-01 --to 2022-12-31 [--house Commons|Lords] [--take 50]
  hansard_search.py --debate E7D8AF2F-9BB3-4475-86D6-39091FB54AC4      # full text of one debate by ID

Search output: JSON with total counts and a list of matching contributions
{member, house, date, debate_title, debate_id, snippet, url}. `url` is the human Hansard page (needs a browser);
`debate_id` feeds back into --debate for the full text without a browser.
"""
import argparse, json, re, sys, urllib.parse
from _common import get, die, out, strip_tags, looks_blocked

API = "https://hansard-api.parliament.uk"

def search(term, start, end, house, take):
    p = {"queryParameters.searchTerm": term, "queryParameters.take": take}
    if start: p["queryParameters.startDate"] = start
    if end: p["queryParameters.endDate"] = end
    if house: p["queryParameters.house"] = house
    url = f"{API}/search.json?" + urllib.parse.urlencode(p)
    status, ctype, body = get(url)
    if status != 200 or looks_blocked(status, body):
        die(f"{url} returned HTTP {status}")
    d = json.loads(body)
    rows = []
    for c in d.get("Contributions", []):
        rows.append({
            "member": c.get("MemberName"),
            "house": c.get("House"),
            "date": (c.get("SittingDate") or "")[:10],
            "debate_title": c.get("DebateSection"),
            "debate_id": c.get("DebateSectionExtId"),
            "snippet": strip_tags(c.get("ContributionText") or "")[:400],
            "url": f"https://hansard.parliament.uk/{c.get('House')}/{(c.get('SittingDate') or '')[:10]}/debates/{c.get('DebateSectionExtId')}/",
        })
    return {
        "totals": {k: d.get(k) for k in ("TotalContributions", "TotalDebates", "TotalWrittenStatements", "TotalWrittenAnswers", "TotalMembers")},
        "returned": len(rows),
        "contributions": rows,
    }

def debate(debate_id):
    url = f"{API}/debates/debate/{debate_id}.json"
    status, ctype, body = get(url)
    if status != 200:
        die(f"{url} returned HTTP {status}")
    d = json.loads(body)
    lines = [f"# {d.get('Overview', {}).get('Title')} — {d.get('Overview', {}).get('House')} — {(d.get('Overview', {}).get('Date') or '')[:10]}",
             f"# source: https://hansard.parliament.uk/{d.get('Overview', {}).get('House')}/{(d.get('Overview', {}).get('Date') or '')[:10]}/debates/{debate_id}/", ""]
    for it in d.get("Items", []):
        who = it.get("AttributedTo") or it.get("MemberName") or ""
        txt = strip_tags(it.get("Value") or "")
        if txt:
            lines.append(f"**{who}**: {txt}" if who else txt)
            lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("term", nargs="?")
    ap.add_argument("--from", dest="start")
    ap.add_argument("--to", dest="end")
    ap.add_argument("--house", choices=["Commons", "Lords"])
    ap.add_argument("--take", type=int, default=50)
    ap.add_argument("--debate", help="debate ID to fetch in full")
    a = ap.parse_args()
    if a.debate:
        print(debate(a.debate))
    elif a.term:
        out(search(a.term, a.start, a.end, a.house, a.take))
    else:
        ap.error("give a search term or --debate ID")
