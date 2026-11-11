# What the uk-legal-sources skill actually does

A plain account for a researcher who does not take software on trust. It covers what the skill reaches, how, what was tested, and where it will let you down.

## What it is

A skill is a set of instructions and small programs that Claude loads when a task touches UK law or policy. This one does three things:

1. It tells Claude which website holds the answer to which kind of question, so it does not guess or answer from memory.
2. It tells Claude which way of reaching that website works, because many of them refuse automated requests.
3. It supplies six small programs that fetch from the sites that allow it, so Claude does not improvise the fetching each time.

It does not contain any legal text itself. Every answer still depends on fetching a live document and reading it correctly.

## How it identifies itself and behaves

- Every request it makes names itself honestly as `uk-legal-sources-skill (research)`. It never pretends to be a web browser.
- It respects the pace a site asks for. legislation.gov.uk asks for five seconds between requests, and the programs wait that long.
- It never logs in, never enters credentials, and never tries to get round a bot check. Where a site blocks scripts, the skill stops and tells Claude to use a real browser or to tell you it could not reach the source.
- It refuses to fetch from BAILII by script, even though a technical route exists, because BAILII's robots file and terms say no.
- What it fetches goes into Claude's working memory to be read. That means the fetched text is processed by Anthropic's systems, like anything else you paste into Claude. Nothing is stored by the skill itself, and nothing is sent anywhere else.

## How well it was tested

Be clear-eyed about this. Everything in the table below was tested on **4 September 2026**, mostly with **one request per address**, from one computer in the UK. That is enough to know a route worked that day. It is not a track record. Websites change their blocking rules, feeds change their formats, and archives fill in or drop pages. The programs have no automatic retry, so a one-off server hiccup shows up as a failure.

One specific warning: bot-protected sites occasionally let a single request through by chance. Twice during testing a blocked site returned a real page once and then refused the same address on every retry. A single success against a blocked site should not be believed.

The skill includes a checker (`check_access.py`) that tells you, for any address, whether a plain request gets through today. Run it when something seems off.

## The reliability scale used below

- **Solid.** The publisher built a proper machine-readable route with no login. Tested, structured data comes back, and the publisher is a public body with a stated commitment to open data. Expect it to keep working, and expect complete results.
- **Usually fine.** An ordinary web page that fetched without trouble. No structured data, so the program has to pick text out of the page, which can break when the site is redesigned. The site could add bot protection at any time.
- **Patchy.** A side door: an archive copy, a mirror, or a different publisher carrying the same text. Works for some items and not others, may be out of date, and tells you nothing about what is missing.
- **Manual only.** The skill cannot fetch it. Claude can drive a real browser as a person would, which is slow, sees one page at a time, and has been seen stuck on a security check. Or you look yourself.
- **None.** No route at all.

## Every source, how it is reached, and how much to trust the route

| Source | What it holds | How the skill reaches it | Reliability | What was tested | Known limits |
|---|---|---|---|---|---|
| legislation.gov.uk | All UK Acts and statutory instruments, current and historic versions | Direct fetch of the site's own machine-readable files (`/data.xml`, `/data.pdf`) and its search feed. Two programs | Solid | Whole Acts, single sections, past-date versions, PDFs, explanatory notes, full-text and title search. Several dozen requests over two days | Search results are not ranked by relevance and carry no in-force marker. Some older SIs have no updated version. The "outstanding changes" warning depends on the site's own metadata flags |
| Hansard (UK Parliament debates) | What was said in the Commons and Lords, 1803 to today | Parliament's open data feed, not the website. One program for search, one for full debates | Solid | Search by term and date, full debate by ID, and a 1998 query to confirm old material is present | The public website itself is blocked to scripts. Citations point at the website, which you may need a browser to open. Feed field names could change |
| Written questions and answers | Parliamentary questions, ministers' written answers, written statements | Parliament's open data feed. One program | Solid | Search, paging through all results, lookup by question number and by internal ID | The same question number is reused every parliament, so a lookup needs a date range. Occasional one-off server errors |
| Bills, members, committees, petitions, statutory instruments, divisions, early day motions, members' interests | Bill progress, MP and peer details, committee metadata, petitions, SI scrutiny, votes, motions | Parliament's open data feeds, called directly with curl. No dedicated programs | Solid | One search call per feed | Committee documents themselves sit on a blocked site; only their metadata comes through the feed |
| Historic Hansard (api.parliament.uk/historic-hansard) | Hansard 1803 to 2005 as web pages | Direct page fetch | Usually fine | Two pages (a sitting and a day's written answers, 1998) | Web pages, not structured data. Coverage ends 2005 |
| publications.parliament.uk | Older Hansard, committee reports, many older parliamentary papers | Not reachable directly. Side door: Wayback Machine copies of specific pages | Patchy | One 2011 written-answers page via the archive | Only pages someone archived. The archive rate-limits. Frozen at capture date |
| House of Commons Library briefings | Neutral research briefings for MPs | Not reachable directly. Web search finds the briefing; Wayback Machine had the briefing page but not its PDF. The open-data catalogue lists briefings by date but its keyword search returns nothing | Patchy | One briefing page via the archive; catalogue keyword search tried with three terms, all empty | Reading the PDF needs a browser. Web search snippets are summaries, not the text |
| Deposited papers register | Documents ministers place in the Libraries, often unpublished elsewhere | Nothing. Every side door tried is closed | Manual only | Old file host (refused), open-data catalogue (empty), Wayback (no copies), direct fetch (blocked) | Browser only. Search-form database with no feed |
| TheyWorkForYou | Charity mirror of Hansard, written answers, votes | Direct page fetch of search results and pages | Usually fine | One search page | Not the official record. Its own data feed needs a free key, which the skill does not hold |
| Find Case Law (National Archives) | Judgments of England and Wales courts from about 2001, UK Supreme Court, Privy Council | The site's own search feed and per-judgment XML. One program | Solid | Search with date and court filters, full judgment fetch and clean-up | No Scotland, NI, House of Lords, Employment Tribunal, magistrates. Bulk analysis across many judgments needs their free licence; the skill does not check whether you hold one. Their robots file bans named AI crawlers |
| Tribunal decisions on GOV.UK | Employment Tribunal (2017 on), Employment Appeal Tribunal, Upper Tribunal, tax and property tribunals | GOV.UK search feed with a document-type filter, called directly | Solid | One call per tribunal type | Each result links to a page carrying a PDF; the PDF still has to be downloaded and converted to text |
| BAILII | Judgments across the UK and Ireland, House of Lords, tribunals, older cases, plus legislation and journals | Not fetched by script, by design. Side door: Wayback Machine copy of a judgment whose address you already have. Web search returns judgments with snippets | Patchy for a known case; Manual only for search | One 2016 judgment via the archive; live site confirmed blocked to browser-like requests | Cannot search BAILII. Archive coverage is hit and miss. BAILII's terms forbid automation, so the skill will not use the technical route that exists |
| judiciary.uk, supremecourt.uk | Newest judgments, sentencing remarks, press summaries | Direct page fetch | Usually fine | One search page and one listing page each; never used in a real task | Web pages only. Not exercised in depth |
| GOV.UK pages and PDFs | Government guidance, consultations and outcomes, codes of practice, statistics | Direct fetch; content and search feeds for structured data; PDFs downloaded and converted to text | Solid | Pages, PDFs, content feed, search feed with DEFRA and consultation filters | Guidance is not law. PDF-to-text conversion can garble layout |
| Scottish Parliament | Official Report, questions, motions, bills, members | Search results page fetches; members, bills and committees feeds fetch. Transcript pages do not | Usually fine for finding; Manual only for reading | Search page, three feeds, one transcript page (which came back without its text) | The transcript text is drawn in by script, so a browser is needed to read what was said |
| Senedd | Record of Proceedings, oral and written questions | Direct fetch of the Record search, which links to meetings and questions | Usually fine | One search | Committee papers site is blocked. Web pages, not structured data |
| Northern Ireland Assembly | Official Report, questions, divisions | The Assembly's open data services, called directly | Solid | Questions by keyword, list of Official Reports, service listings | Older-style web services; method names must be exact |
| Sentencing Council | Sentencing guidelines, including animal cruelty | Direct page fetch | Usually fine | One guideline page, robots file | Their robots file allows reference use and forbids AI training. Fetch for reference only |
| Law Commission | Law reform projects, consultation papers, reports | The site's WordPress search feed and pages | Usually fine | Two feed calls | Feed could be switched off in a redesign |
| Information Commissioner decision notices | FOI refusals upheld or overturned | Not searchable by script; results are drawn in by script. Web search finds individual notices | Manual only for search | One search page (returned no results in the raw page) | Individual notice pages were not tested |
| Local Government Ombudsman | Decisions on council complaints, including licensing enforcement | Category listing pages fetch. Keyword search is behind a CAPTCHA | Usually fine for browsing; Manual only for search | One category page listing ten decisions | You browse by category, not by keyword |
| WhatDoTheyKnow | Archive of Freedom of Information requests and responses | Per-authority feed of the latest 25 requests. Request pages blocked. Web search finds requests | Patchy | One authority feed (25 entries); request pages and site search confirmed blocked | Only the newest requests per body. Reading a request needs a browser |
| EUR-Lex (EU law) | EU regulations, directives, case law | Not the EUR-Lex site. Side door: the EU Publications Office serves the same text to scripts by CELEX number. legislation.gov.uk carries retained EU law | Usually fine for a known instrument; Manual only for browsing | One regulation via the Publications Office (2.4 MB); its data query endpoint answered; legislation.gov.uk retained-law fetch | You need the CELEX number, which is in any EUR-Lex link. Searching EUR-Lex itself needs a browser |
| Regulators and councils (Gambling Commission, Ofcom, council committee systems, licensing registers) | Guidance, policies, committee papers, licence registers | Direct fetch where allowed; a browser-style request got through one council system; registers are often generated on the fly | Usually fine for guidance; Patchy for registers | Gambling Commission pages, Ofcom PDFs, one council committee page, one register that errored | Address slugs change. Registers are timestamped and awkward whatever the route |
| Magistrates' court outcomes | Individual convictions and sentences | No source exists. Press reports, prosecutor releases, FOI | None | Not applicable | The skill points to the Sentencing Council guideline as a proxy for what magistrates apply |

## What the skill does not do

- **It does not judge the law.** It retrieves and quotes. Whether a provision applies to your facts is your call or a lawyer's.
- **It does not guarantee the text is in force.** For legislation it reports the version date the site gives and counts the site's own "changes not yet applied" flags. That is the site's metadata, not an independent check. Repeals that are on the statute book but never commenced are the classic trap, and the skill can only surface what the page says about them.
- **It does not check whether a judgment was later overturned.** Find Case Law and BAILII publish decisions, not their subsequent history.
- **It does not search relevance-ranked.** legislation.gov.uk's search returns results in an order that has nothing to do with importance. The skill's answer to that is to fetch every page of results and hand you the whole list, which is complete but not prioritised.
- **It does not remove the reading risk.** Fetching the right document is half the job. Claude can still misread a subsection or attach the wrong section number. The skill makes Claude print the source address and version date with every fetch precisely so you can check.
- **It does not hold any licence or key.** Find Case Law's computational-analysis licence and TheyWorkForYou's data key are yours to obtain if you need them.
- **It does not cover paid databases.** Westlaw, LexisNexis and the like are outside its scope.

## How to check its work

1. Every fetch prints the exact address it used and, for legislation, the version date. Open that address yourself.
2. Ask Claude which route it used. If the answer is "a search snippet", ask it to fetch the document.
3. If a source seems unreachable, run the checker on the address. If the checker says blocked, that is the site's decision, not a fault you can fix from your side.
4. Treat the "tested" column above as a date-stamped claim. If it matters, re-test before relying on it.
5. Read the "Data sources I used for this answer" list at the end of every answer. It names each source, its link, its date and how it was reached. Anything reached only through a search snippet has not been opened, so do not rely on it.

## Where the evidence came from

The routing and the block list come from about seventeen research sessions run with Claude on 3 and 4 September 2026 for a UK animal law workshop, in which each route was tried on real questions (the Animal Welfare Act, the Pet Animals Act, section 24 of the Animals (Scientific Procedures) Act, zoo licensing, a racecourse gambling licence). The extra sources and side doors were probed on 4 September with single requests.
