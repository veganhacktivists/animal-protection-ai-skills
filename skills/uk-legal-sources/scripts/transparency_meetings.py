#!/usr/bin/env python3
"""Search a department's published ministerial meetings (GOV.UK transparency returns).

Departments publish, quarterly, a list of every meeting their ministers held with an outside
body: minister, date, who they met, and a one-line purpose. It is open data, no key needed.
This walks the whole published series for a department and searches every row at once.

Usage:
  transparency_meetings.py --org department-for-environment-food-rural-affairs elephant
  transparency_meetings.py --org home-office "asylum|detention" --since 2024-01
  transparency_meetings.py --org cabinet-office --list           # just list the quarterly returns
  transparency_meetings.py --find-org environment                # look up a department's slug
  transparency_meetings.py --collection /government/collections/... elephant   # skip the lookup

The search term is a regular expression, matched case-insensitively across every column, so
"elephant|abta|low.welfare" works. Output: JSON list of
{minister, date, met, purpose, quarter, source} plus a count on stderr.

Three things to know before quoting any of it:
  * Ministers only. Meetings held by officials are not published here at all, and on a stalled
    policy that is usually where the work sits. Use FOI for that layer.
  * The purpose lines are written by hand inside the department. They range from useful to
    meaningless, and are full of typos.
  * It runs late. Returns appear roughly three months after the quarter ends, sometimes much
    later, so expect a six to nine month blind spot at the front. --list shows the real lag.

Never read these files line by line. Purpose fields contain commas and line breaks, so one
meeting can span seventy lines; grep and `wc -l` both give wrong answers. This parses them as
spreadsheets, which is the only way to get the count right.
"""
import argparse, csv, io, json, re, sys, urllib.parse
from _common import get, die, out

SEARCH = "https://www.gov.uk/api/search.json"
CONTENT = "https://www.gov.uk/api/content"


def api(url, delay=0.5):
    status, ctype, body = get(url, delay=delay)
    if status != 200:
        die(f"{url} returned HTTP {status}: {body[:200]!r}")
    return json.loads(body)


def find_org(word):
    """List department slugs matching a word, for use with --org."""
    p = {"q": word, "filter_format": "organisation", "count": 20, "fields": "title,link"}
    d = api(f"{SEARCH}?{urllib.parse.urlencode(p)}")
    return [{"title": r.get("title"), "slug": (r.get("link") or "").rsplit("/", 1)[-1]}
            for r in d.get("results", [])]


def find_collection(org):
    """Find the department's ministerial meetings collection.

    Departments leave dead collections lying about: DCMS has one that stopped in 2014 sitting
    next to the live one. Title words alone pick the wrong one, so shortlist on the title and
    then choose whichever shortlisted collection is still being added to.
    """
    p = {"q": "ministerial gifts hospitality meetings travel external organisations",
         "filter_organisations": org,
         "filter_content_store_document_type": "document_collection",
         "count": 20, "fields": "title,link"}
    d = api(f"{SEARCH}?{urllib.parse.urlencode(p)}")
    hits = d.get("results", [])
    if not hits:
        die(f"no transparency collection found for {org!r}. Try --find-org, or pass --collection.")

    def score(r):
        t = (r.get("title") or "").lower()
        s = 0
        if "minister" in t: s += 3
        if "meeting" in t: s += 3
        if "hospitality" in t or "travel" in t: s += 1
        # Other people's meetings, and collections that are not meetings at all.
        for bad in ("special adviser", "special advisor", "senior official", "board",
                    "workforce", "pipeline", "intergovernmental", "interministerial",
                    "communique", "letters", "publications", "register"):
            if bad in t: s -= 8
        return s

    shortlist = [r for r in sorted(hits, key=score, reverse=True) if score(r) > 0][:3]
    if not shortlist:
        die(f"no likely meetings collection for {org!r}. Pass --collection with the path.")

    best, best_date, best_docs = None, "", None
    for r in shortlist:
        try:
            docs = returns_in(r["link"])
        except SystemExit:
            continue
        newest = docs[0]["published"] if docs else ""
        print(f"#   candidate: {r.get('title')} (newest {newest or 'none'})", file=sys.stderr)
        if newest > best_date:
            best, best_date, best_docs = r, newest, docs
    if best is None:
        die(f"could not read any candidate collection for {org!r}.")
    print(f"# collection: {best.get('title')} ({best.get('link')})", file=sys.stderr)
    return best.get("link"), best_docs


def returns_in(collection_path):
    """Every quarterly return in the collection, newest first."""
    d = api(f"{CONTENT}{collection_path}")
    docs = d.get("links", {}).get("documents", [])
    rows = [{"title": x.get("title"),
             "path": x.get("base_path"),
             "published": (x.get("public_updated_at") or "")[:10]} for x in docs]
    rows.sort(key=lambda r: r["published"], reverse=True)
    return rows


SKIP_TITLE = re.compile(r"special advis|senior official|board member|workforce|"
                        r"business appointment|communique|register of", re.I)
WANT_TITLE = re.compile(r"minister", re.I)


def loose_returns(org):
    """Quarterly returns published loose, not gathered into a collection.

    Not every department keeps a live collection. DCMS, for one, has two dead ones lying about
    and publishes the real quarterly returns on their own. So always search the transparency
    publications directly as well, and merge.
    """
    rows, page = [], 0
    while page < 5:
        p = {"q": "ministers meetings hospitality travel",
             "filter_organisations": org,
             "filter_content_store_document_type": "transparency",
             "count": 50, "start": page * 50,
             "order": "-public_timestamp",
             "fields": "title,link,public_timestamp"}
        d = api(f"{SEARCH}?{urllib.parse.urlencode(p)}")
        got = d.get("results", [])
        for r in got:
            t = r.get("title") or ""
            if SKIP_TITLE.search(t) or not WANT_TITLE.search(t):
                continue
            rows.append({"title": t, "path": r.get("link"),
                         "published": (r.get("public_timestamp") or "")[:10]})
        if len(got) < 50:
            break
        page += 1
    return rows


def all_returns(org):
    """Everything findable for a department, from the collection and from loose publications."""
    rows = []
    try:
        _, rows = find_collection(org)
    except SystemExit:
        print("# no usable collection, falling back to a direct search", file=sys.stderr)
    seen = {r["path"] for r in rows}
    extra = [r for r in loose_returns(org) if r["path"] not in seen]
    if extra:
        print(f"# plus {len(extra)} return(s) published outside the collection", file=sys.stderr)
    rows += extra
    rows.sort(key=lambda r: r["published"], reverse=True)
    return rows


def csv_attachments(path, meetings_only=True):
    """Direct spreadsheet addresses on one quarterly return."""
    d = api(f"{CONTENT}{path}")
    found, skipped = [], []
    for a in d.get("details", {}).get("attachments", []):
        title, url = a.get("title") or "", a.get("url") or ""
        if meetings_only and "meeting" not in title.lower():
            continue
        if url.lower().endswith(".csv"):
            found.append({"title": title, "url": url})
        else:
            skipped.append(title)
    for s in skipped:
        print(f"#   not a csv, skipped: {s}", file=sys.stderr)
    return found


def rows_from(url):
    """Parse one spreadsheet. Handles the line breaks inside purpose fields."""
    status, ctype, body = get(url, delay=0.5)
    if status != 200:
        print(f"#   HTTP {status} on {url}", file=sys.stderr)
        return []
    text = body.decode("utf-8-sig", "replace")
    return list(csv.DictReader(io.StringIO(text, newline="")))


def cell_text(row):
    """All of a row's text in one string.

    When a row has more cells than the header, csv puts the extras in a list under the key
    None (one DCMS quarter does this), so flatten lists rather than assuming every value is text.
    """
    parts = []
    for v in row.values():
        if isinstance(v, list):
            parts.extend(x for x in v if x)
        elif v:
            parts.append(v)
    return " ".join(parts)


def pick(row, *names):
    """Column names drift between departments and quarters, so match loosely."""
    for key, val in row.items():
        if not key:
            continue
        k = key.strip().lower()
        if any(n in k for n in names):
            return (val or "").strip()
    return ""


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pattern", nargs="?", help="case-insensitive regular expression")
    ap.add_argument("--org", help="department slug, e.g. department-for-environment-food-rural-affairs")
    ap.add_argument("--collection", help="collection path, skips the lookup")
    ap.add_argument("--find-org", dest="find", help="look up department slugs by word")
    ap.add_argument("--since", help="only returns published on or after this date (YYYY-MM or YYYY-MM-DD)")
    ap.add_argument("--list", action="store_true", help="list the quarterly returns and stop")
    ap.add_argument("--all-files", action="store_true", help="also search travel, gifts and hospitality files")
    a = ap.parse_args()

    if a.find:
        out(find_org(a.find))
        sys.exit(0)
    if not a.collection and not a.org:
        ap.error("give --org (or --collection), or use --find-org to look one up")

    if a.collection:
        rets = returns_in(a.collection)
    else:
        rets = all_returns(a.org)
    if a.since:
        since = a.since if len(a.since) > 7 else a.since + "-01"
        rets = [r for r in rets if r["published"] >= since]
    if a.list:
        out(rets)
        sys.exit(0)
    if not a.pattern:
        ap.error("give a search pattern, or --list")

    term = re.compile(a.pattern, re.I)
    hits, scanned = [], 0
    for r in rets:
        print(f"# {r['published']}  {r['title']}", file=sys.stderr)
        for att in csv_attachments(r["path"], meetings_only=not a.all_files):
            rows = rows_from(att["url"])
            scanned += len(rows)
            for row in rows:
                if term.search(cell_text(row)):
                    hits.append({
                        "minister": pick(row, "minister", "name of minister"),
                        "date": pick(row, "date"),
                        "met": pick(row, "organisation", "individual", "name of"),
                        "purpose": pick(row, "purpose", "reason"),
                        "quarter": r["title"],
                        "source": att["url"],
                    })
    print(f"# scanned {scanned} meetings across {len(rets)} returns, {len(hits)} matched",
          file=sys.stderr)
    out(hits)
