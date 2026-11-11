# Devolved legislatures and adjacent sources

Added 2026-09-04 after probing. "Curl OK" means a plainly named script got real content that day.

## Devolved legislatures (Hansard is UK Parliament only)

Animal welfare is largely devolved. What a Scottish, Welsh or NI minister said is NOT in Hansard.

### Scottish Parliament
- Official Report search page is server-rendered and curl OK:
  `https://www.parliament.scot/chamber-and-committees/official-report/search-what-was-said-in-parliament?keywords=animal+welfare`
  Result links look like `.../meeting-of-parliament-DD-MM-YYYY?meeting=NNNNN&iob=NNNNNN`.
- The transcript pages themselves load their text by script: curl returned the shell with no debate text. Read them in the browser, or look for the PDF/print link on the page.
- Open data: `https://data.parliament.scot/api/members`, `/api/bills`, `/api/committees` curl OK (JSON). `/api/motionsquestionsanswersquestions?year=2024` returned 14 MB of questions and answers on one call, then timed out on a repeat; use the year filter and expect it to be slow. No official-report endpoint.

### Senedd (Welsh Parliament)
- The Record search is server-rendered and curl OK: `https://record.senedd.wales/Search/?query=animal+welfare`
  Result links: `/Meeting/{id}?#C{contribution}`, `/OralQuestion/{id}`, `/WrittenQuestion/{id}`, `/QNR/{id}`. Prefix with `https://record.senedd.wales`.
- `business.senedd.wales` (committee papers, ModernGov) returned 403 to scripts; browser.

### Northern Ireland Assembly
- Open data web services at `http://data.niassembly.gov.uk/` (services: hansard, members, organisations, plenary, questions). JSON variants end `_JSON`. Curl OK:
  - Questions by keyword: `http://data.niassembly.gov.uk/questions.asmx/GetQuestionsBySearchText_JSON?searchText=animal%20welfare`
  - Written answer text: `questions.asmx/GetWrittenAnswerHtml?documentId=...`
  - List of Official Reports: `hansard.asmx/GetAllHansardReports_JSON` → `ReportDocId`, then `hansard.asmx/GetHansardComponentsByReportId_JSON?reportId=...`
  - Divisions: `plenary.asmx/GetDivisionResult_JSON`, `GetVotesOnDivision_JSON`
- AIMS portal (`aims.niassembly.gov.uk`) pages also curl OK.

## Tribunal decisions on GOV.UK (not on Find Case Law)

GOV.UK search feed, no key. Filter by document type:
`https://www.gov.uk/api/search.json?q=animal&filter_content_store_document_type=TYPE&count=20`
Types confirmed with results: `employment_tribunal_decision` (2017 onwards), `employment_appeal_tribunal_decision`, `utaac_decision` (Upper Tribunal Administrative Appeals, includes information-rights appeals), `tax_tribunal_decision`, `residential_property_tribunal_decision`. Each result has `link` to the GOV.UK page, which carries the decision PDF.
Route rule: for an Employment Tribunal or Upper Tribunal question, try GOV.UK first, then BAILII in the browser.

## Government consultations and outcomes

Same GOV.UK feed: `filter_content_store_document_type=consultation_outcome` (or `open_consultation`, `closed_consultation`), add `&filter_organisations=department-for-environment-food-rural-affairs` for DEFRA, `&order=-public_timestamp` for newest first. Curl OK, 500+ DEFRA outcomes. DEFRA's consultation hub `consult.defra.gov.uk` also curl OK.

## Sentencing Council
`https://www.sentencingcouncil.org.uk/` pages curl OK, e.g. the magistrates' animal cruelty guideline at `/offences/magistrates-court/item/animal-cruelty/`. This is what magistrates apply, so it is the best proxy where magistrates' outcomes are unpublished. Robots: allows `*` with `Content-Signal: search=yes, ai-train=no, use=reference`; bans ClaudeBot and several AI crawlers by name. Fetch for reference, do not harvest. Site search: `/?s=animal` (WordPress REST API is not enabled).

## Law Commission
`https://lawcom.gov.uk/` curl OK, and its WordPress REST API works:
- `https://lawcom.gov.uk/wp-json/wp/v2/search?search=animal&per_page=10`
- `https://lawcom.gov.uk/wp-json/wp/v2/project?search=animal&per_page=10` (projects with status and documents)
Use for reform proposals, consultation papers and reports.

## Information Commissioner decision notices
`https://ico.org.uk/action-weve-taken/decision-notices/` is where FOI refusals are upheld or overturned. The search results are rendered by script: curl gets the page shell with no results. Use the browser for search. Web search indexes individual notices well, and an individual notice page should fetch once you have its address (not tested in bulk).

## Local Government and Social Care Ombudsman
`https://www.lgo.org.uk/decisions` keyword search is a form protected by a CAPTCHA, so browser only. But the category browse pages are server-rendered and curl OK, e.g. `https://www.lgo.org.uk/decisions/environment-and-regulation/licensing` lists decisions as `/decisions/environment-and-regulation/licensing/YY-NNN-NNN`. Individual decision pages fetch fine. Useful for council failures on animal licensing enforcement.

## Also confirmed open (curl OK, no key), not yet scripted
- Statutory instruments with scrutiny status: `https://statutoryinstruments-api.parliament.uk/api/v2/StatutoryInstrument?Name=animal&Take=20`
- Commons divisions: `https://commonsvotes-api.parliament.uk/data/divisions.json/search?queryParameters.searchTerm=animal`
- Lords divisions: `https://lordsvotes-api.parliament.uk/data/Divisions/search?SearchTerm=animal`
- Early day motions: `https://oralquestionsandmotions-api.parliament.uk/EarlyDayMotions/list?parameters.searchTerm=animal`
- Committee publications metadata: `https://committees-api.parliament.uk/api/Publications?SearchTerm=animal+welfare` (the document download itself sits on committees.parliament.uk, which is bot-blocked; browser for the file)
- Members' interests: `https://interests-api.parliament.uk/api/v1/Interests?SearchTerm=animal`
- Court of Justice of the EU search page `curia.europa.eu` curl OK. European Court of Human Rights HUDOC did not respond to a plain request; browser.

## Blocked or dead, for the record
Incorporated Council of Law Reporting (403), Casemine (403), Local Government Association (bot check), CPS legal guidance index (moved, 404), Scottish courts judgment search address tried (404, needs a fresh look).
