# Parliament sources

Pattern across parliament.uk: the human-facing sites sit behind a Cloudflare bot check ("Just a moment...", HTTP 403 to curl and page readers). Most have a matching open data feed at an `-api` address that needs no key. Always prefer the feed.

## Hansard

- Website `hansard.parliament.uk`: blocked to scripts. Browser usually works but has been seen stuck on the check.
- Feed `https://hansard-api.parliament.uk`:
  - Search: `/search.json?queryParameters.searchTerm=TERM&queryParameters.startDate=YYYY-MM-DD&queryParameters.endDate=YYYY-MM-DD&queryParameters.take=N[&queryParameters.house=Commons|Lords]`
    Returns `TotalContributions`, `TotalDebates`, `TotalWrittenAnswers` etc. and `Contributions[]` with `MemberName`, `House`, `SittingDate`, `DebateSection`, `DebateSectionExtId`, `ContributionText`.
  - Full debate: `/debates/debate/{DebateSectionExtId}.json` → `Overview` (Title, House, Date) and `Items[]` (`AttributedTo`, `Value` HTML).
  - Human link to cite: `https://hansard.parliament.uk/{House}/{YYYY-MM-DD}/debates/{DebateSectionExtId}/`
- Pre-2010 Hansard: the data feed above still returns it (1998 test: 20 contributions, 9 written answers). Historic Hansard, 1803-2005, is open: `https://api.parliament.uk/historic-hansard/sittings/1998/mar/03`, `/written_answers/1998/mar/03`, and per-person and per-topic pages. `publications.parliament.uk` itself is blocked; Wayback Machine copies of its pages fetch fine (`https://web.archive.org/web/2024/https://publications.parliament.uk/...`). TheyWorkForYou is also open.

## Written questions and answers

- Website `questions-statements.parliament.uk`: blocked to scripts; browser works.
- Feed `https://questions-statements-api.parliament.uk/api/writtenquestions/questions`
  - `?searchTerm=X&take=100&skip=0&expandMember=true[&tabledWhenFrom=YYYY-MM-DD&tabledWhenTo=...][&house=Commons|Lords]`
  - By public number: `?uIN=61968` (UINs recur each parliament; add dates)
  - By internal id: `/{id}?expandMember=true`
  - Fields: `uin`, `dateTabled`, `dateAnswered`, `askingMember.name`, `answeringMember.name`, `answeringBodyName`, `heading`, `questionText`, `answerText`.
  - Occasional 500 on one query; retry.
- Written statements: `https://questions-statements-api.parliament.uk/api/writtenstatements/statements?searchTerm=X`
- Old host `writtenquestions-api.parliament.uk` redirects; do not use.

## Bills

- Website `bills.parliament.uk`: blocked. Feed open:
  - `https://bills-api.parliament.uk/api/v1/Bills?SearchTerm=animal&Take=20`
  - `https://bills-api.parliament.uk/api/v1/Bills/{id}` and `/Bills/{id}/Stages`, `/Bills/{id}/Publications`

## Members and committees

- `https://members-api.parliament.uk/api/Members/Search?Name=starmer&take=20`
- `https://committees-api.parliament.uk/api/Committees?SearchTerm=environment&Take=20`

### Written evidence to an inquiry

Added 2026-09-22. Badly under-used. An inquiry makes a whole sector write down its position, in
one place, on a date, with a reference number, and it stays public for ever. It is often the only
place a trade body's real view is on the record.

The feed is open; the `committees.parliament.uk` pages are not (403 to scripts and to simple page
readers, though a real browser gets through the bot check after a few seconds).

- One submission, including which inquiry it belongs to and who submitted it:
  `https://committees-api.parliament.uk/api/WrittenEvidence/{id}`
- **Every submission to that inquiry**, which is the useful move:
  `https://committees-api.parliament.uk/api/WrittenEvidence?CommitteeBusinessId={id}&take=100`
  Take the `committeeBusiness.id` from any single submission.
- Inquiries by name: `https://committees-api.parliament.uk/api/CommitteeBusiness?SearchTerm=animal+welfare&take=20`

Quirks: the `SearchTerm` on `WrittenEvidence` returned 0 for plain topic words even where matching
submissions exist, so go in through an inquiry id or a single known submission rather than
searching. The `document.files` entries list the docx, PDF and HTML versions but their `url` fields
are null, so read the text at `https://committees.parliament.uk/writtenevidence/{id}/html/` in a
real browser.

Web search is a good way in: searching a phrase plus the topic often surfaces one submission, and
its inquiry id then gives you all the others.

## Petitions

- `https://petition.parliament.uk/petitions/{id}` fetches fine; `https://petition.parliament.uk/petitions/{id}.json` for data; `/petitions.json?q=animal` to search.

## House of Commons Library

- Briefing pages `commonslibrary.parliament.uk` and PDFs at `researchbriefings.files.parliament.uk`: both 403 to scripts. Browser works. Web search indexes them well.
- Catalogue feed `https://lda.data.parliament.uk/researchbriefings.json?_pageSize=20&_sort=-date` is open and lists briefings with title, date, abstract and identifier, but its `_search=` keyword filter returned zero for every term tried on 2026-09-04, so it is a listing, not a search. Find the briefing by web search instead.
- Wayback Machine had the HTML briefing page (`https://web.archive.org/web/2025/https://commonslibrary.parliament.uk/research-briefings/cbp-9449/`) but not its PDF. Try the archive for the page; use the browser for the PDF.
- Lords Library `lordslibrary.parliament.uk`: also 403 to scripts.

## Deposited papers register

`https://depositedpapers.parliament.uk/` holds documents ministers place in the Libraries, often unpublished elsewhere. Bot-blocked, no feed, web search finds individual entries but not topics. Browser only. Side doors checked and closed: the old file host `data.parliament.uk/DepositedPapers/Files/...` returns 403, `lda.data.parliament.uk/depositedpapers.json` is empty, Wayback has no copies. Search form fields: `Terms`, `DepositedFrom`, `DepositedTo` (DD/MM/YYYY), `House`, `OrderBy=CommitmentDateDesc`, `Expanded=True`, `page`. Once a tab is open, `fetch()` from inside the tab with `credentials:'include'` against that URL pattern pages through results without clicking.

## TheyWorkForYou

Charity mirror of Hansard, written answers and votes. Pages fetch fine: `https://www.theyworkforyou.com/search/?q=animal+welfare`. API `https://www.theyworkforyou.com/api/getDebates?...&key=KEY` needs a free key from theyworkforyou.com/api/key. Cite Hansard, find with TheyWorkForYou.
