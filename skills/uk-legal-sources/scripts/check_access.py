#!/usr/bin/env python3
"""Quick check of which route a URL will accept: plain fetch, or does it need a real browser?

Usage:  check_access.py URL [URL ...]
        check_access.py --feeds     (checks every data feed this skill's scripts use)
Prints one line per URL: OK / BLOCKED BY YOUR NETWORK SETTINGS / BLOCKED (bot check) / HTTP nnn,
plus the suggested route.
"""
import sys
from _common import get, looks_blocked, blocked_by_own_network

FEEDS = [
    "https://questions-statements-api.parliament.uk/api/writtenquestions/questions?take=1",
    "https://hansard-api.parliament.uk/search.json?queryParameters.searchTerm=animal&queryParameters.take=1",
    "https://members-api.parliament.uk/api/Members/Search?Name=smith&take=1",
    "https://committees-api.parliament.uk/api/Committees?take=1",
    "https://bills-api.parliament.uk/api/v1/Bills?take=1",
    "https://www.legislation.gov.uk/ukpga/2006/45/contents/data.xml",
    "https://caselaw.nationalarchives.gov.uk/atom.xml?query=animal",
    "https://www.gov.uk/api/content/government/organisations/department-for-environment-food-rural-affairs",
]

HINTS = {
    "hansard.parliament.uk": "use scripts/hansard_search.py (hansard-api) instead",
    "bills.parliament.uk": "use https://bills-api.parliament.uk/api/v1/Bills?SearchTerm=... instead",
    "questions-statements.parliament.uk": "use scripts/written_questions.py instead",
    "publications.parliament.uk": "try api.parliament.uk/historic-hansard (1803-2005), hansard_search.py, or a Wayback Machine copy; else real browser",
    "commonslibrary.parliament.uk": "try a Wayback Machine copy of the page (web.archive.org/web/2025/URL); else real browser",
    "researchbriefings.files.parliament.uk": "real browser only (PDFs were not in Wayback)",
    "committees.parliament.uk": "metadata via committees-api.parliament.uk; the document file needs the real browser",
    "depositedpapers.parliament.uk": "real browser only; no side door exists",
    "ico.org.uk": "search results render by script: real browser for search; individual notices should fetch",
    "lgo.org.uk": "keyword search is CAPTCHA-protected: browse category pages by curl or use the browser",
    "parliament.scot": "search pages fetch; transcript text renders by script, so read it in the browser",
    "bailii.org": "do NOT script this site: robots.txt disallows all case paths and the terms forbid automated access. Read it in a real browser as a person would; try Find Case Law first (scripts/caselaw_search.py)",
    "whatdotheyknow.com": "per-body Atom feed is open (/feed/body/{slug}.atom); request pages need the real browser",
    "eur-lex.europa.eu": "fetch the text from Cellar instead: curl -H 'Accept: application/xhtml+xml' -H 'Accept-Language: eng' http://publications.europa.eu/resource/celex/{CELEX}",
}

args = sys.argv[1:]
if not args or args[0] in ("-h", "--help"):
    print(__doc__.strip())
    sys.exit(0 if args else 2)
if args == ["--feeds"]:
    args = FEEDS

for url in args:
    status, ctype, body = get(url, timeout=30)
    host = url.split("/")[2].removeprefix("www.")
    if blocked_by_own_network(status, body):
        verdict = "BLOCKED BY YOUR NETWORK SETTINGS"
        print(f"{verdict:45} {url}\n{'':45} -> allow this address in your AI tool's network settings (README.md), or read it in a real browser")
        continue
    if looks_blocked(status, body) or (status == 202 and not body):
        verdict = f"BLOCKED (HTTP {status}, bot check)"
    elif status == 200:
        verdict = f"OK (HTTP 200, {len(body)} bytes, {ctype.split(';')[0]})"
    else:
        verdict = f"HTTP {status}"
    hint = next((h for k, h in HINTS.items() if host.endswith(k)), "")
    show = hint and (not verdict.startswith("OK") or host.endswith("bailii.org"))
    print(f"{verdict:45} {url}" + (f"\n{'':45} -> {hint}" if show else ""))
