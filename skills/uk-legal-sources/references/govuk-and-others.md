# GOV.UK, regulators, councils, FOI, EU

## GOV.UK

Fully open. Guidance, consultations, responses, codes of practice, statistics. Not law; check statute for the legal position.

- Any page as JSON: `https://www.gov.uk/api/content/{path}` e.g. `/api/content/guidance/animal-welfare`
- Site search as JSON: `https://www.gov.uk/api/search.json?q=animal+welfare&count=20` (add `&filter_organisations=department-for-environment-food-rural-affairs`)
- PDFs at `assets.publishing.service.gov.uk/media/{id}/{name}.pdf` download fine.

PDF pattern for exact wording:
```bash
curl -sL -o doc.pdf "URL" && pdftotext -layout doc.pdf doc.txt && grep -n -i -B3 -A12 "phrase" doc.txt
```
Fallback if pdftotext is missing: `python3 -c "import pypdf,sys; print('\n'.join(p.extract_text() for p in pypdf.PdfReader('doc.pdf').pages))"`.

## Who a minister met: transparency returns

Added 2026-09-22. Every department publishes, quarterly, a list of every meeting its ministers held
with an outside body: minister, date, who they met, and a one-line purpose. Open, no key, back to
about 2019. `scripts/transparency_meetings.py` does the whole chain; the manual route is below,
because it is the same shape for gifts, hospitality, overseas travel, special advisers' meetings and
senior officials' expenses, which are separate collections.

Four steps.

1. Find the collection, filtering search by department and document type:
```bash
curl -s "https://www.gov.uk/api/search.json?q=ministerial%20gifts%20hospitality%20meetings&filter_organisations=home-office&filter_content_store_document_type=document_collection&fields=title,link"
```
2. Read the collection as data. `links.documents` is every return it has ever published:
```bash
curl -s "https://www.gov.uk/api/content/government/collections/home-office-ministers-hospitality-data"
```
3. Read one return as data. `details.attachments` holds the direct spreadsheet addresses. Each
   quarter usually publishes several files; pick the one whose title contains "meeting":
```bash
curl -s "https://www.gov.uk/api/content/government/publications/home-office-ministerial-gifts-hospitality-travel-and-meetings-january-to-march-2026"
```
4. Download and parse as a spreadsheet. **Never grep these line by line.** The purpose column
   contains commas and line breaks, so one meeting can span seventy lines: line-based searching
   misses rows and miscounts totals. One Defra quarter counted 999 lines and held 989 meetings.

Department slugs: `filter_format=organisation` on the search interface finds them, or use
`transparency_meetings.py --find-org <word>`.

Three caveats to state whenever you quote this data:

- **Ministers only.** Officials' meetings are not published here at all. On a stalled policy that is
  usually where the work is, so absence here is a reason to file an FOI, not proof of neglect.
- **The purpose lines are written by hand** inside the department, vary from useful to meaningless,
  and are full of typos. Search loosely and read the raw wording before quoting.
- **It runs late, by a lot, and the lag differs by department.** On 2026-09-22 the Home Office had
  published up to January–March 2026 while Defra's latest was October–December 2025. Always run
  `--list` first and tell the user where the record actually stops.

Column headings drift between departments and quarters ("Name of Individual or Organisation",
"Organisation", "Name of Organisation"), so match headings loosely rather than exactly.

## Tribunal decisions and consultations on GOV.UK
See devolved-and-adjacent.md: `filter_content_store_document_type=employment_tribunal_decision` etc., and `consultation_outcome` with `filter_organisations=department-for-environment-food-rural-affairs`.

## Regulators

- Gambling Commission: guidance pages fetch fine; slugs changed to `gla-part-N-...`, old `part-N-...` 404. Public register: `/public-register/premises/detail/{opaque-id}`, find the id via web search.
- Ofcom: PDFs fetch fine but carry `?v=NNNN` version strings that rotate. Download and keep a copy.
- Companies House officers: `https://find-and-update.company-information.service.gov.uk/company/{number}/officers` (untested here; official API exists with a free key).

## Councils

- ModernGov committee systems (`*.moderngov.co.uk`): 403 to page readers; curl with a desktop browser User-Agent got through. Then strip HTML.
- Licensing registers are often dynamic, timestamped listings; treat as browser-only and expect breakage. Say when a register could not be read.
- Council PDFs (policies, statements) usually download fine; use the PDF pattern.

## FOI

- WhatDoTheyKnow: request pages and JSON endpoints are bot-blocked. The per-authority Atom feed is open: `https://www.whatdotheyknow.com/feed/body/home_office.atom` (latest 25 requests to that body, with links). The search feed `/feed/search/TERM.atom` returned an empty feed. Web search indexes requests well. Read a request in the browser.
- An FOI request itself is not a data-access route; it is asking a person. Flag when that is the only way.

## EU law

- EUR-Lex website returns HTTP 202 with an empty body to scripts (bot protection), including ELI addresses. Browser works. Web search indexes it well.
- Side door that works: the EU Publications Office (Cellar) serves the same text to scripts.
  `curl -sL -H "Accept: application/xhtml+xml" -H "Accept-Language: eng" "http://publications.europa.eu/resource/celex/32005R0001" -o reg.html` (2.4 MB XHTML for Regulation 1/2005). CELEX numbers are in any EUR-Lex link. SPARQL endpoint `https://publications.europa.eu/webapi/rdf/sparql` is open.
- Retained EU law as it applies in the UK is on legislation.gov.uk: `https://www.legislation.gov.uk/eur/2005/1/data.xml`.
- Wayback Machine copies of EUR-Lex pages also fetch.

## Third-party sites in general

Try in this order: page reader → curl with browser User-Agent → real browser. Never enter credentials. If a site's terms or robots say no automation, stop and use the browser as a person would, or tell the user.
