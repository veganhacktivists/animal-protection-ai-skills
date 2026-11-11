---
name: uk-legal-sources
description: Find and quote UK legal, legislative and policy sources by the route that actually works. Use whenever a task involves UK law, Acts, statutory instruments, Hansard, parliamentary debates, written questions, bills, select committees, Commons Library briefings, court judgments, case law, tribunals, sentencing, the devolved parliaments, EU law, FOI requests, or government guidance and consultations, or names a source like legislation.gov.uk, Hansard, Find Case Law, BAILII, TheyWorkForYou, GOV.UK, EUR-Lex or a council licensing register. Also use when someone asks "what does the law say", "is this section in force", "has a minister said", "who did the minister meet about X", "is there a case on", "can AI search X", or wants the full text or PDF of an Act. Routes each question to open data feeds first, page fetches second, and a real browser only where a site blocks scripts, with tested scripts for legislation.gov.uk, Hansard, written questions, ministers' meetings and Find Case Law.
license: MIT
compatibility: Needs Python 3 with internet access to UK government and Parliament data feeds, or a real web browser the agent can drive.
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-11-10"
  verified-on: "Claude Code"
---

# UK legal sources

Every "what does the law say" answer must come from a fetched primary text, never from memory. This skill tells you which source holds the answer, which route reaches it, and gives scripts for the routes that are best done in code.

Tested 4 September 2026. Sites change their blocking rules; if a script starts failing, run `scripts/check_access.py URL` and re-route.

## Rules that apply to every task

1. Fetch, then quote. Give the section number, the exact words, the link, and the version date of the text you fetched.
2. Say which route you used (search snippet, page fetch, browser, data feed). A search snippet is not a source.
3. Check in-force status. Search results never carry it. A repeal shown on the page may not be in force yet (Pet Animals Act 1951 s.2 is the standing example).
4. Keep to the pace the site asks for. legislation.gov.uk wants five seconds between requests; the scripts honour that. Do not disguise a script as a browser to get round a block.
5. Distinguish statute (legislation.gov.uk), what was said in Parliament (Hansard), what a court decided (Find Case Law / BAILII) and government guidance (GOV.UK). Users blur them; you must not.
6. When a source cannot be reached, say so plainly and name the route a person would use. Do not fill the gap.
7. Use the scripts, not the built-in page reader, for any site a script covers: legislation.gov.uk, Hansard, written questions, Find Case Law and the GOV.UK ministers' meetings returns. For other open sites, prefer `curl` in the shell. If the built-in page reader times out on a site, do not try it on that site again in the same task. Switch to the script or `curl`, or tell the user you could not reach it. (In Cowork on 8 October 2026 the page reader hung for three minutes, twice, on legislation.gov.uk pages that the script fetched in seconds.)
8. End every answer with a section headed **Data sources I used for this answer**, so the reader can check every claim. Say once what date you fetched them. Then list each source the answer relies on, one line each: what it is (for example "Pet Animals Act 1951, section 2"), the link, how you reached it (script, data feed, page fetch, browser or search snippet), and the version date or the date of the debate or judgment. After that, list anything you tried but could not reach, and why. Include the section even in short answers, and even when the answer is that nothing was found.

## When your own network settings block the feeds

Two different things can stop a script, and they need different fixes.

- **The site blocks scripts.** The script gets HTTP 403, 429 or 503, or a page saying "Just a moment" or asking it to prove it is not a bot. `check_access.py` prints `BLOCKED (bot check)`. This is the site's decision. Follow the routing table and the side doors below.
- **Your own environment blocks the address.** The script can't connect at all: a proxy or allowlist error (for example "blocked-by-allowlist" or "egress blocked"), a refused connection, or an address that won't resolve. The scripts print a line starting `NETWORK:` and `check_access.py` prints `BLOCKED BY YOUR NETWORK SETTINGS`. The data feeds this skill uses don't bot-block, so a failure like this on one of them means the user's AI tool isn't allowed to reach that address. `check_access.py --feeds` checks all of them at once.

When it is your own environment:

1. Tell the user once, in a sentence or two, that their AI tool's network settings are blocking the address, name the address, and say the fix is to allow it. Point them to "Letting your AI reach the data feeds" in this skill's `README.md`. Don't repeat this on every request.
2. Setting changes usually only reach a new session or chat. If the user changes them, tell them to start a new one and ask again.
3. Meanwhile, or if they can't change the setting: if you can drive a real web browser on the user's computer, open the same feed address in it. The browser uses the user's own internet connection, not your environment's, and the feeds return plain data that reads as text. Use the same addresses and parameters as the scripts (`references/parliament.md` lists them).
   - The written questions list (`/api/writtenquestions/questions?...`) cuts each answer short. Open `/api/writtenquestions/questions/{id}?expandMember=true` for the full question, answer and member names.
   - Open one address at a time, at a person's pace, and say in your sources that you used the browser.
4. If you have no browser either, say which sources you couldn't reach and give the user the exact address to open themselves and paste back.

Don't try other ways round your environment's block, such as a proxy.

## Routing table

| The question is about | Go to | Route | Script |
|---|---|---|---|
| Text of an Act or SI, a section, a past version, explanatory notes, PDF | legislation.gov.uk | Fetch (fully open) | `legislation_fetch.py` |
| Which law covers X | legislation.gov.uk search feed | Fetch, read the whole list | `legislation_search.py` |
| What a minister or MP said in a debate | Hansard | Data feed (website is bot-blocked) | `hansard_search.py` |
| Written parliamentary questions and answers | questions-statements-api | Data feed (website is bot-blocked). **Cannot do phrase search**, see below | `written_questions.py` |
| An exact phrase in written questions, e.g. one Act's name | TheyWorkForYou search | Fetch. The feed above cannot do this | none |
| Who a minister met about X, and when | That department's quarterly transparency returns on GOV.UK | Fetch, open data, no key | `transparency_meetings.py` |
| Progress of a bill | bills-api.parliament.uk | Data feed, no key | curl, see references/parliament.md |
| Select committee, MP or peer details, petitions | committees-api / members-api / petition.parliament.uk | Data feed, no key | see references/parliament.md |
| What an industry or campaign group told Parliament | Select committee written evidence | Data feed for the list, browser for the text | see references/parliament.md |
| Pre-2010 Hansard | api.parliament.uk/historic-hansard (1803-2005, open) or `hansard_search.py` with old dates | Fetch | `hansard_search.py` |
| Old committee reports, other publications.parliament.uk pages | Wayback Machine copy, else real browser | Fetch archive, else browser | see references/parliament.md |
| Commons Library briefing | Web search to find it; Wayback Machine copy or real browser to read it | Search, then archive or browser | see references/parliament.md |
| Documents ministers deposited in the Library | depositedpapers.parliament.uk | Real browser only, no feed, no side door found | none |
| What was said in the Scottish Parliament, Senedd or NI Assembly | Their own records, not Hansard | Fetch (search pages and NI data services open; Scottish transcripts need browser) | see references/devolved-and-adjacent.md |
| Court judgment, England & Wales 2001+, UKSC | Find Case Law | Fetch / feed (fully open) | `caselaw_search.py` |
| Employment Tribunal, EAT, Upper Tribunal decision | GOV.UK search feed first, then BAILII | Fetch | see references/devolved-and-adjacent.md |
| Judgment from Scotland, NI, Ireland, House of Lords, pre-2001 | BAILII | Wayback Machine copy for a known URL; otherwise real browser, one-off lookups. Never script the live site | none |
| Sentencing practice, especially where magistrates' outcomes are unpublished | Sentencing Council guidelines | Fetch (reference use only) | curl |
| Law reform proposals | Law Commission | Fetch, WordPress API | see references/devolved-and-adjacent.md |
| FOI refusal overturned or upheld | ICO decision notices | Web search to find; browser to search the site | see references/devolved-and-adjacent.md |
| Council maladministration, e.g. licensing enforcement | Local Government Ombudsman decisions | Fetch category pages; browser for keyword search | see references/devolved-and-adjacent.md |
| Sentencing remarks, newest judgments | judiciary.uk, supremecourt.uk | Fetch | curl |
| Government guidance, consultations and outcomes (DEFRA etc.), codes | GOV.UK | Fetch, plus content and search APIs | see references/govuk-and-others.md |
| A government PDF | assets.publishing.service.gov.uk | Fetch, then `pdftotext`, then grep | see references/govuk-and-others.md |
| Regulator guidance, council papers, licensing registers | varies | Fetch first; curl with browser UA if 403; browser last | `check_access.py` |
| Freedom of Information responses | WhatDoTheyKnow | Per-authority Atom feed is open; request pages need the browser | see references/govuk-and-others.md |
| EU law | EUR-Lex text via the EU Publications Office (Cellar), or legislation.gov.uk for retained EU law | Fetch | see references/govuk-and-others.md |

## Using the scripts

All scripts are standard-library Python, no installs. Run them from this folder or by full path. Each prints JSON to stdout and progress or warnings to stderr. `--help` on any script shows the options.

```bash
S=path/to/uk-legal-sources/scripts   # the scripts folder next to this SKILL.md, wherever the skill is installed
python3 $S/legislation_search.py --text '"unnecessary suffering"' --text sentience     # pooled, complete list
python3 $S/legislation_fetch.py ukpga/2006/45                                          # whole Act as clean text
python3 $S/legislation_fetch.py ukpga/2006/45 --section 4                              # one section
python3 $S/legislation_fetch.py ukpga/2006/45 --version 2010-01-01                     # as it stood on a date
python3 $S/legislation_fetch.py ukpga/2006/45 --format pdf -o act.pdf                  # PDF
python3 $S/hansard_search.py "section 24" --from 2022-01-01 --to 2022-12-31            # who said what, when
python3 $S/hansard_search.py --debate E7D8AF2F-9BB3-4475-86D6-39091FB54AC4            # full debate text
python3 $S/written_questions.py reindeer --from 2022-01-01 --all                       # every matching WQ
python3 $S/written_questions.py --uin 61968 --from 2022-10-01 --to 2022-10-31          # one WQ by number
python3 $S/caselaw_search.py "Animal Welfare Act 2006" --from 2020-01-01               # judgments, newest first
python3 $S/caselaw_search.py --judgment https://caselaw.nationalarchives.gov.uk/ewhc/admin/2025/1383
python3 $S/transparency_meetings.py --org home-office "asylum|detention" --since 2024-01  # who a minister met
python3 $S/transparency_meetings.py --find-org environment                              # a department's slug
python3 $S/transparency_meetings.py --org cabinet-office --list                          # returns + the real lag
python3 $S/check_access.py https://example.gov.uk/page                                 # which route will work?
python3 $S/check_access.py --feeds                                                     # can I reach every data feed?
```

### The written questions feed cannot do phrase search

Tested 2026-09-22. `searchTerm` with a quoted phrase returns HTTP 500. Without quotes it matches
any word, so `"low-welfare activities abroad"` comes back with nearly 14,000 results, nearly all
noise. There is no phrase operator.

So for "every time Parliament mentioned X", search TheyWorkForYou instead, which does phrase
search properly and covers debates and written answers together:
`https://www.theyworkforyou.com/search/?q=%22your+phrase%22`. It gives dates, askers and links
to each item, and the individual pages fetch fine. Use `written_questions.py` once you know the
UIN or a single distinctive word, and for pulling a specific question and its full answer.

The standard research loop:

1. `legislation_search.py` with several phrasings, quoted. Read the whole list; it is not ranked. Pick candidates by title and year.
2. `legislation_fetch.py` each candidate. Note the "version in force from" line and any "outstanding changes" warning on stderr.
3. If the question is about what government said or intends, `hansard_search.py` and `written_questions.py` for the same terms and period, plus TheyWorkForYou for the exact phrase.
3a. If it is about who government listened to, `transparency_meetings.py` on the responsible department. Say plainly that this covers ministers only, not officials, and name the blind spot at the front caused by the publication lag.
4. If a court has interpreted the provision, `caselaw_search.py` with the Act's name or the phrase. If nothing there and the case might be older, Scottish, NI or a tribunal, tell the user to look on BAILII in a browser, or use the browser tool for a one-off lookup.
5. Quote with section numbers, links and version dates. Finish with the **Data sources I used for this answer** section (rule 8), including anything you could not reach.

## Side doors into the bot-blocked sites

Checked 2026-09-04. Claude's built-in page reader is blocked on all six, same as curl.

| Site | Side door that worked | Still needs the browser for |
|---|---|---|
| BAILII | Wayback Machine copy of a known judgment URL (`https://web.archive.org/web/2024/https://www.bailii.org/...`). Web search snippets. Find Case Law or the court's own site often has the same judgment | Searching BAILII; anything not archived |
| publications.parliament.uk | Historic Hansard `https://api.parliament.uk/historic-hansard/sittings/1998/mar/03` and `/written_answers/1998/mar/03` (1803-2005). The Hansard data feed also returns 1990s material. Wayback copies of specific pages | Committee reports and other documents not archived |
| Commons Library | Web search finds the briefing. Wayback Machine had the briefing HTML page. The open-data catalogue lists briefings by date but its keyword search returns nothing | The PDF itself (not in Wayback for the one tried) |
| Deposited papers | None found. The old file host returns 403, the catalogue is empty, Wayback has nothing | Everything |
| WhatDoTheyKnow | Per-authority Atom feed, e.g. `https://www.whatdotheyknow.com/feed/body/home_office.atom` (25 latest requests). Web search finds requests | Reading a request page; site search |
| EUR-Lex | EU Publications Office serves the full text: `curl -H "Accept: application/xhtml+xml" -H "Accept-Language: eng" http://publications.europa.eu/resource/celex/32005R0001`. SPARQL endpoint open. legislation.gov.uk holds retained EU law at `/eur/2005/1/data.xml`. Wayback copies | Browsing EUR-Lex itself |

A one-off success against a bot-blocked site proves nothing: the Cloudflare check let two single requests through on 2026-09-04 and refused the same addresses on every retry. Do not build on it.

Wayback Machine manners: it rate-limits (a 429 came back on the availability check). One page at a time, and check the snapshot date, since an archived page is frozen at capture.

## Where the browser is the only route

Hansard's website, publications.parliament.uk, the Commons Library site and PDFs, the deposited papers register, BAILII, WhatDoTheyKnow and EUR-Lex all block scripts with a bot check. For Hansard and written questions the data feeds above are better anyway. For the rest, use the real browser tool as a person would: load the page, use the site's own search form, read the result. One useful trick on the deposited papers register: once the page is open in the browser, the site's own search URL can be called from inside the tab with the session cookies, which lets you page through results without clicking.

BAILII specifically: its robots file disallows every case directory and its terms forbid automated access. Its bot check happens to let honestly named scripts through, but do not use that. Read BAILII in the browser for individual cases, and check Find Case Law first. Direct search URL pattern for the browser:
`https://www.bailii.org/cgi-bin/search_preprocess.cgi?mode=case&phrase=YOUR+PHRASE&sort=date` (swap `phrase` for `all`, `any`, `titleall`, `citation`; sort by date, relevance is broken).

## Licences and manners

- Find Case Law: reading and quoting individual judgments is fine. Running software across many judgments to extract or classify is "computational analysis" and needs their free licence. Their robots file bans named AI crawlers, so do not bulk-harvest.
- legislation.gov.uk: open, five-second gap. Sitemaps exist if a team wants a local corpus for one area of law.
- TheyWorkForYou API needs a free key; the pages themselves fetch fine.

## References

- `references/legislation.md`: address patterns, version logic, search-feed quirks, known traps.
- `references/parliament.md`: every parliament.uk data feed with tested example calls, plus the Library and deposited papers.
- `references/caselaw.md`: Find Case Law coverage, feed fields, licence; BAILII coverage differences; judiciary and Supreme Court sites.
- `references/govuk-and-others.md`: GOV.UK APIs, the PDF pattern, regulators, councils, FOI, EU.
- `references/devolved-and-adjacent.md`: Scottish Parliament, Senedd, NI Assembly; tribunal decisions on GOV.UK; consultation outcomes; Sentencing Council; Law Commission; ICO and Ombudsman decisions; the extra parliament.uk feeds (SIs, divisions, EDMs, committee publications, interests).
- `WHAT-THIS-SKILL-DOES.md`: the plain, sceptic's account of every source, route, test and limitation. Point researchers at it.
- `PROMPT.md`: a short, tool-agnostic prompt block to give to people using ChatGPT, Gemini or Claude without code.
- `README.md`: the setup guide, including which addresses to allow and how to check the feeds are reachable.

## Requirements

- Python 3 (standard library only) that you can run, with internet access to the data feeds listed in `README.md`.
- Where your network settings block those feeds and the user can't change them: a real web browser you can drive on the user's computer.
- With neither, you can still route the question and tell the user which address to open. `PROMPT.md` works in any AI tool.

If the user asks to set this skill up, follow `README.md` in this folder.
