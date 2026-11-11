# Case law

## Find Case Law (The National Archives) — use first

`https://caselaw.nationalarchives.gov.uk`. Official publisher of judgments for England & Wales, UK Supreme Court and Privy Council. Open to scripts; robots allows `*` but bans named AI crawlers (GPTBot, ClaudeBot, anthropic-ai, PerplexityBot and others).

- Search page: `/judgments/search?query=...`
- Atom feed: `/atom.xml?query=animal+welfare&order=-date&page=N` (also `court=ewca/crim`, `from_date_0/1/2` = D/M/Y, `to_date_0/1/2`). Entry has `title`, `link rel=alternate` (HTML), a second link `type=application/akn+xml` (XML), `author/name` (court), `published`, `tna:identifier type=ukncn` (neutral citation), PDF link.
- Judgment XML: judgment URL + `/data.xml` (Akoma Ntoso). Strip the `<meta>` block; body is `<judgmentBody>` with `<paragraph><num>` and `<p>`.
- Docs: https://nationalarchives.github.io/ds-find-caselaw-docs/public

Licence: standard licence covers reading and quoting. "Computational analysis" (software across many judgments to extract, classify, summarise at scale) needs their free licence; apply before bulk work. Coverage: most series from 2001 or 2003; no House of Lords, no Employment Tribunal (EAT only from 2021), no Scotland/NI/Ireland, essentially no magistrates' courts.

## BAILII — browser only, one case at a time

`https://www.bailii.org`. Charity library covering what Find Case Law does not: Scotland (Court of Session, High Court of Justiciary, Sheriff Courts), Northern Ireland, Republic of Ireland, Jersey, House of Lords (5,071 decisions), Employment Tribunal (66k), immigration tribunals, IPO, Competition Appeal Tribunal, ECHR and CJEU, plus legislation, Law Commission reports, journals.

Access: bot check (Anubis) on browser-like requests; robots.txt disallows `/uk /ew /scot /nie /ie /eu ...` to all agents; terms forbid spidering, scraping and bulk download. Do not script it, even though an honestly named script may get a 200. Use the browser tool for a one-off lookup. Direct search URL: `/cgi-bin/search_preprocess.cgi?mode=case&phrase=X&sort=date`; parameters `all`, `any`, `titleall`, `citation`, `boolean`, `datelow`, `datehigh`, `sort=date|title|jurisdiction|relevance` (relevance shows NaN%). Pressing Return in the form does not submit. Web search does surface BAILII judgments with snippets because they were indexed before the block; the AI cannot then open the page.

Wayback Machine copies work for individual judgments too when you already have the BAILII address, e.g. `https://web.archive.org/web/2024/https://www.bailii.org/ew/cases/EWHC/Admin/2016/2531.html` returned the full judgment. Check the capture date. The archive rate-limits, so one page at a time. Static BAILII pages (database lists, coverage tables) were readable the same way.

Tribunals: Employment Tribunal (2017 on), EAT and Upper Tribunal decisions are on GOV.UK with an open search feed; try there before BAILII. See devolved-and-adjacent.md.

## judiciary.uk and supremecourt.uk

Both fetch fine with curl (checked 2026-09-04, not exercised in depth). judiciary.uk: newest judgments, sentencing remarks as PDFs under `/wp-content/uploads/`, `?s=` site search works. supremecourt.uk: case pages `/cases/uksc-2025-0165`, judgment PDFs under `/uploads/`, press summaries. No APIs.

## Magistrates' courts

Not systematically published anywhere. Press reports, prosecutor press releases (RSPCA, CPS) and FOI are the routes. Deep-research style web search is the right tool; say clearly that coverage is partial.
