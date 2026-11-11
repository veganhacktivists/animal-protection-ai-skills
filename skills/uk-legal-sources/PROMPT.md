# Prompt block for people using any AI tool

Paste this at the top of a research request in ChatGPT, Gemini, Copilot or Claude. It needs no code and no special tools. It works best in a tool that can open web pages; in one that can only search, it still improves what comes back.

---

I am researching UK law and policy. Follow these rules for the whole conversation.

1. Never tell me what a law says from memory. Open the text and quote it. Every legal statement must come with a link to legislation.gov.uk, Hansard, Find Case Law (caselaw.nationalarchives.gov.uk) or GOV.UK. If you cannot open the source, say so rather than summarising a search snippet.

2. For legislation, use legislation.gov.uk. To read a whole Act in one go, add /data.xml to its address, for example https://www.legislation.gov.uk/ukpga/2006/45/data.xml. Add /enacted/ before data.xml for the version as originally passed, or a date such as /2010-01-01/ for the law as it stood then. Give me section numbers, the exact wording, and the date of the version you read. Tell me whether each provision is in force, and check for repeals or amendments that are not yet in force.

3. For what ministers or MPs said, use Hansard. If you cannot open hansard.parliament.uk, use the data feed at hansard-api.parliament.uk or the mirror at theyworkforyou.com, and give me the Hansard link to cite.

4. For court decisions, check Find Case Law first. Only mention BAILII if the case is Scottish, Northern Irish, older than 2001, or from a tribunal Find Case Law does not carry, and tell me you could not open BAILII yourself.

5. For government guidance and consultations, use GOV.UK, and label it as guidance, not law.

6. If you run a search on legislation.gov.uk, put quotation marks around phrases, try several wordings, and report the complete list of results with the total count. The results are not ranked by relevance and do not show whether a law is still in force.

7. Separate clearly: what the statute says, what a court has decided, what a minister said, and what guidance recommends. Do not blend them.

8. End every answer with a section headed "Data sources I used for this answer". List each source you relied on, with its link, how you reached it (opened the page yourself, or only saw a search snippet), and the version date or the date of the debate or judgment. Then list anything you could not reach and how a person could get it.

---

Why these rules: AI tools invent plausible section numbers and case names when left to memory. Making them fetch and quote is the single most effective fix. The address tricks in rule 2 exist because the legislation.gov.uk website shows one section at a time, which makes AI tools give up on long Acts.
