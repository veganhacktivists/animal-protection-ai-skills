---
name: assess-relevance
description: >-
  Reads a report, blog post, paper, policy brief, announcement, web page, or
  file and gives a clear verdict on whether it is relevant to the user's
  day-to-day work in animal advocacy — Highly relevant, Possibly relevant, or
  Not relevant — with a plain-language explanation of why. Use this whenever
  the user shares a URL or file and asks anything like "is this relevant to
  me?", "should I read this?", "is this worth my time?", "does this matter for
  my work?", "triage this report", "assess relevance", or
  "/assess-relevance" — even if they just paste a link and say "worth
  reading?". Also use it when the user shares several links or files and wants
  to know which ones to prioritise.
license: MIT
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-09-08"
  verified-on: "Claude Code, Claude Cowork"
---


Animal advocates constantly come across reports, papers, blog posts, and policy briefs that might matter to their work — but the content is long, full of jargon, and it's unclear whether it's actually relevant to *them*. This skill reads the content, learns who the user is from the context available to you, and returns one clear verdict with a plain-language explanation.

The people using this skill are usually non-technical and may be new to Claude. Write for them: plain speech, no jargon, no meta-language about your internal workings. When you do need to name a technical source (like a CLAUDE.md file), briefly explain what it is.

## Step 1: Learn who the user is

Before reading the document, gather what you know about the user's day-to-day work. Check these sources, in this priority order (if they conflict, the higher source wins):

1. **Project custom instructions** — a `CLAUDE.md` or `AGENTS.md` file in the current folder or any folder above it. If the skill is called from inside a project, these usually describe what the project is for. Read them.
2. **Saved memory** — if you have a persistent memory of this user (a memory directory, user preferences, or similar), read the entries that describe who they are, what organisation they work for, and what they work on.
3. **The current conversation** — anything the user has said in this session about their work, role, or current projects.

Keep track of exactly which sources you used and what they said — you will quote them in your answer.

**If you come up light:** if you can find no custom instructions, no memory, and nothing in the conversation that describes what the user actually does day to day, tell the user plainly. Say something like: "I couldn't find much about what you specifically work on — this skill works best when you've saved details about your work to memory, or when you run it from inside a project folder that has custom instructions (a CLAUDE.md or AGENTS.md file) describing the project." Then still give a best-effort verdict: assess relevance to a typical person working at an animal protection non-profit or in the plant-based food sector, and say clearly that this is what you did.

## Step 2: Read the content

The user gives you a URL or a file path (or several — see "Multiple items" below).

- **URLs**: fetch the page with your standard web-fetch tool. Do not rely on any user-specific tools or extensions — this skill must work out of the box for anyone.
- **Files**: read the file directly (PDF, Word document, markdown, plain text — whatever it is).

Two situations need special handling:

- **Paywalled or blocked content**: if the page is behind a paywall or login, do not try to get around it. Tell the user you can't access it and stop. Do not guess at relevance from the URL or headline alone.
- **Very long documents** (roughly 100+ pages, or a web page of similar length): warn the user first that processing it will use a meaningful chunk of their usage, and ask whether to go ahead. Only proceed once they say yes.

Read enough of the document to genuinely understand what it says and what its implications are. For long documents (once the user has approved), prioritise the executive summary, introduction, findings/results, and recommendations sections, and say so if you skipped substantial parts.

## Step 3: Judge relevance — with a high bar

Everyone using this skill works in animal protection. So the fact that a document mentions animals, animal welfare, veganism, or plant-based food does **not** make it relevant — that would make almost everything "relevant" and the skill useless. Judge relevance against **what this specific user does day to day**:

- If called from inside a project, judge relevance to *that project* specifically.
- Otherwise, judge relevance to the user's role, organisation, campaigns, and current work as described in the sources from Step 1.

Expect a wide variety of documents: agriculture policy reports where only one chapter touches animal farming, trade policy papers, scientific studies, funding announcements, corporate news. Ask yourself: *would this change what this person does, inform a decision they face, strengthen an argument they make, or land on their desk anyway?* If the honest answer is "it's vaguely in their universe but wouldn't change anything for them," that is **Not relevant** or at most **Possibly relevant**.

## Step 4: Return the verdict

Give exactly one of three verdicts — no hedged in-betweens, no scores:

- **Highly relevant** — this clearly bears on the user's specific work; they should read it (or the parts you point to).
- **Possibly relevant** — there's a plausible connection to their work, but it's indirect, partial, or depends on something you're unsure about. Say what that something is.
- **Not relevant** — this doesn't bear on their specific work, even if it's about animals or food in general.

### Output format

Use this structure:

```
## Verdict: [Highly relevant / Possibly relevant / Not relevant]

**What this document says:** [2–4 sentences summarising the document in
plain language, with all jargon translated. Always include this, even when
the verdict is Not relevant — the user still deserves to know what the
thing they found actually says.]

**Why:** [A full paragraph explaining the verdict. This paragraph must
reference how you know the user's work — quote the actual source. For
example: "Your project's custom instructions (the CLAUDE.md file, which
describes what this project is about) say you are 'building a campaign to
end the sale of caged eggs in Greek supermarkets', and this report's
third chapter presents new polling on Greek consumer attitudes to cage
eggs — that directly feeds your campaign messaging." Direct quotes do two
jobs: they show the user you genuinely know them, and if your picture of
them is wrong or out of date, the quote makes it easy for them to spot
why you got it wrong.]

**What I based this on:** [One or two sentences naming the context you
used — e.g. "your project's custom instructions (AGENTS.md)", "my saved
memory of your work", "only what you've told me in this conversation".
If you were light on context, repeat the warning from Step 1 here and
note that the verdict is judged against a typical animal protection
non-profit worker instead.]
```

If the verdict is Highly relevant or Possibly relevant, you may add one short sentence at the end pointing to the most useful part ("the section worth your time is chapter 3, pages 40–52").

When you had no sources to quote (the light-on-context case), the "Why" paragraph obviously can't quote anything — instead, name the kinds of roles the document would and wouldn't matter for, so the user can place themselves, and invite them to tell you their role (or save it to memory) for a sharper answer next time.

## Multiple items

If the user gives you several URLs or files at once, run one sub-agent per item, each independently following this skill's steps for its single item, then return every verdict — one full output block per item, in the order given, so the user can triage the whole batch at a glance. If sub-agents aren't available in your environment, process the items one at a time yourself instead.

## Tone

Plain, warm, and direct. The reader may never have used a tool like this before. Never use unexplained technical terms for Claude's features; when you name a source like "custom instructions" or "CLAUDE.md", add a few words of explanation the first time. The explanation of relevance itself must be entirely jargon-free — translate the document's own jargon too.

## Requirements

None. Works with the agent alone. Gives a sharper answer when the agent has some saved context about the user's work (a memory feature, a project's custom instructions, or a `CLAUDE.md`/`AGENTS.md` file) — without that, it falls back to a best-effort verdict for a typical animal protection worker and says so.
