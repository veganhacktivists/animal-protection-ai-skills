#!/usr/bin/env python3
"""Search parliamentary written questions and answers through the open data feed (not bot-blocked).

Usage:
  written_questions.py "reindeer" [--from 2022-01-01] [--to 2023-12-31] [--house Commons|Lords] [--take 100] [--all]
  written_questions.py --uin 61968 [--from 2022-10-01 --to 2022-10-31]   # look up by the public question number
  written_questions.py --id 1521235                                      # by the API's internal id

UINs are reused in every parliament, so --uin may return several questions; add a date range to pin one.
--all pages through every result (100 per page). Output: JSON list of
{uin, date_tabled, date_answered, asked_by, answered_by, department, question, answer, url}.

WARNING, tested 2026-09-22: this feed has no phrase search. A quoted phrase returns HTTP 500.
Unquoted, it matches any word in the term, so "low-welfare activities abroad" comes back with
nearly 14,000 results. Paging deep into a loose result set also throws 500s.

So for "every time Parliament mentioned X", use TheyWorkForYou instead, which does phrase search
properly and covers debates and written answers together:
  https://www.theyworkforyou.com/search/?q=%22your+phrase%22
Then come back here with the UIN for the full text of a specific question and answer.
"""
import argparse, json, sys, urllib.parse
from _common import get, die, out, strip_tags

API = "https://questions-statements-api.parliament.uk/api/writtenquestions/questions"

def row(v):
    return {
        "uin": v.get("uin"),
        "date_tabled": (v.get("dateTabled") or "")[:10],
        "date_answered": (v.get("dateAnswered") or "")[:10],
        "asked_by": (v.get("askingMember") or {}).get("name"),
        "answered_by": (v.get("answeringMember") or {}).get("name"),
        "department": v.get("answeringBodyName"),
        "question": strip_tags(v.get("questionText") or ""),
        "answer": strip_tags(v.get("answerText") or ""),
        "url": f"https://questions-statements.parliament.uk/written-questions/detail/{(v.get('dateTabled') or '')[:10]}/{v.get('uin')}",
    }

def search(term, start, end, house, take, all_pages):
    rows, skip = [], 0
    while True:
        p = {"searchTerm": term, "take": take, "skip": skip, "expandMember": "true"}
        if start: p["tabledWhenFrom"] = start
        if end: p["tabledWhenTo"] = end
        if house: p["house"] = house
        url = API + "?" + urllib.parse.urlencode(p)
        status, ctype, body = get(url, delay=1.0)
        if status != 200:
            die(f"{url} returned HTTP {status}: {body[:200]!r}")
        d = json.loads(body)
        results = d.get("results", [])
        rows += [row(r["value"]) for r in results]
        total = d.get("totalResults", 0)
        print(f"# fetched {len(rows)}/{total}", file=sys.stderr)
        if not all_pages or not results or len(rows) >= total:
            break
        skip += take
    return rows

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("term", nargs="?")
    ap.add_argument("--from", dest="start"); ap.add_argument("--to", dest="end")
    ap.add_argument("--house", choices=["Commons", "Lords"])
    ap.add_argument("--take", type=int, default=100)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--id", help="API internal id for full detail")
    ap.add_argument("--uin", help="public question number (UIN); combine with --from/--to")
    a = ap.parse_args()
    if a.id:
        status, ctype, body = get(f"{API}/{a.id}?expandMember=true")
        if status != 200: die(f"HTTP {status}")
        out(row(json.loads(body)["value"]))
    elif a.uin:
        p = {"uIN": a.uin, "expandMember": "true", "take": 20}
        if a.start: p["tabledWhenFrom"] = a.start
        if a.end: p["tabledWhenTo"] = a.end
        status, ctype, body = get(API + "?" + urllib.parse.urlencode(p))
        if status != 200: die(f"HTTP {status}")
        out([row(r["value"]) for r in json.loads(body).get("results", [])])
    elif a.term:
        out(search(a.term, a.start, a.end, a.house, a.take, a.all))
    else:
        ap.error("give a search term or --id")
