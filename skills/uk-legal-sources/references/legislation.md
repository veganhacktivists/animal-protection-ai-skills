# legislation.gov.uk

Official text of all UK Acts and statutory instruments, revised with amendments. Fully open to scripts. Robots: `Crawl-delay: 5`, nothing disallowed. Rejects HEAD requests; use GET.

## Address patterns (all tested 2026-09-04)

Base: `https://www.legislation.gov.uk/{type}/{year}/{number}`
Types: `ukpga` Acts, `uksi` UK SIs, `asp` Scottish Acts, `ssi` Scottish SIs, `wsi` Welsh SIs, `nisr` NI rules, `eur` retained EU regs, `ukla` local Acts. Old Acts also have regnal addresses (`ukpga/Geo6/14-15/35`); the year form works too.

| Want | Append |
|---|---|
| Whole text, current, XML | `/data.xml` |
| Whole text, current, PDF | `/data.pdf` |
| Plain HTML | `/data.html` |
| As originally passed | `/enacted/data.xml` (Acts) or `/made/data.xml` (SIs); `/enacted/data.pdf` |
| As it stood on a date | `/2010-01-01/data.xml` |
| One section | `/section/4` (add `/data.xml` for machine text) |
| Explanatory notes | `/notes/data.xml` |
| Contents page | `/contents` |
| Original print PDF (King's Printer) | `/pdfs/ukpga_20060045_en.pdf` style, or `/pdfs/uksi_20180486_en.pdf` |

XML metadata worth reading: `<dc:title>`, `<dct:valid>` or `RestrictStartDate` (version date), `<ukm:UnappliedEffect>` count (changes not yet applied), `RestrictExtent` (E+W+S+N.I.).

## Search feed

`https://www.legislation.gov.uk/all/data.feed?text=...` (body text) or `?title=...`. Replace `all` with a type code to filter. 20 results a page, `&page=N`. `<openSearch:totalResults>` gives the count.

Quirks, all confirmed:
- Not relevance-ranked. Animal Welfare Act 2006 was result 37 of 114 for "unnecessary suffering". Read the whole list.
- Quote phrases. Unquoted multi-word queries degrade badly.
- No stemming. "sentience" (4) and "sentient" (6) differ. Pool several forms.
- No in-force field in results. Open each hit.
- EU-derived regulations dominate title searches; filter by type if you only want UK Acts.

## Traps

- Default text is the revised version, not the enacted one. Sizes differ a lot (AWA 2006: 387 KB enacted vs 605 KB current). Record the version date with every quote.
- Some SIs have no revised version at all (Welfare of Animals at Markets Order 1990). Then fetch the amending SIs too and read them together. The "Changes to legislation" panel on the HTML page lists them.
- "Repealed" annotations can be prospective. Pet Animals Act 1951 s.2 is marked repealed by AWA 2006 Sch 3 but that repeal has never been commenced; the section is live.
- Chapter numbers are easy to confuse: `ukpga/2006/45` is the Animal Welfare Act, `ukpga/2006/46` is the Companies Act.
- Coverage of revised text is weaker for Scottish, Welsh and NI instruments. Caveat cross-nation work.

## Bulk

Sitemaps per type at `https://www.legislation.gov.uk/sitemap-ukpga.xml` etc. A team that repeatedly researches one corner of the law can download that set once (five-second gap), convert to clean text, and run their own full-text or semantic search, which the official search lacks.
