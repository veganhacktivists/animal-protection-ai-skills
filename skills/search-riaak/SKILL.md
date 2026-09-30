---
name: search-riaak
description: >-
  Searches RIAAK (riaak.netlify.app), a free public knowledge base of animal
  advocacy research, and answers using only the notes it finds, with a
  clickable link to every source. RIAAK holds summaries of academic papers,
  NGO and think tank reports, and practitioner notes on factory farming,
  alternative proteins, diet change, messaging, policy, farmed fish and
  animal welfare. Use this whenever the user wants evidence or sources on an
  animal advocacy topic, asks "what does the research say about...", "find me
  studies on...", "is there evidence that...", "search RIAAK", "check RIAAK",
  or wants links to reports they can read themselves. Do not use it for
  general web searches or for topics outside animal advocacy, food systems
  and alternative proteins.
license: MIT
compatibility: Needs internet access and a way to make an HTTPS request with a custom header, such as running curl.
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-09-30"
  verified-on: "Claude Code"
---

# Search RIAAK

RIAAK (https://riaak.netlify.app) is a free, public knowledge base of animal advocacy research: summaries of academic papers and NGO reports, plus practitioner notes, on factory farming, alternative proteins, diet change, messaging, policy and more. This skill runs a search over it and answers the user's question using **only** the notes that come back, with a **clickable link to every source**, so the user can read the originals.

The search understands meaning, not just keywords: it turns the question into numbers that represent its meaning, finds the notes closest to it, re-ranks them for relevance, and returns the best passage from each note.

## Strict knowledge boundaries

- **No outside knowledge.** If the returned notes don't answer the question, say so. Do not fill gaps from your own training.
- **No invention.** Never make up authors, dates, statistics, findings or context. Every claim must trace back to a returned passage.
- Stay within what the passages actually say. Paraphrase rather than copy.

## Step 1: Turn the question into a short search query

Use the key ideas, not a full sentence. For example "cultivated meat consumer acceptance naturalness", not "what do people think about lab grown meat and is it natural".

## Step 2: Call the search

Run this, putting the query where it says `YOUR QUERY HERE`:

```bash
curl -s --get "https://riaak.vercel.app/api/search" \
  -H "X-Api-Key: riaak_0a5b497c3423538c06c6fb5c123a1ec4126c2b9e" \
  --data-urlencode "q=YOUR QUERY HERE" \
  --data-urlencode "top_k=8"
```

About that `X-Api-Key` value: it is a public, shared value, not a password. The same value is sent by the RIAAK website's own search box, so anyone visiting the site already has it. Its only job is to stop random bots running searches. It is not tied to anyone's account and does not unlock anything beyond RIAAK's public search. Never ask the user for a key.

- `top_k` (1 to 15, default 8) is how many different notes come back. Use 12 to 15 for broad questions and 3 to 5 for narrow ones.
- The first search after a quiet spell can take up to about 15 seconds while the search service wakes up. Wait for it rather than giving up.

The reply is JSON, one entry per note:

```json
{"results": [
  {
    "score": 0.63,
    "text": "…the most relevant passage from the note…",
    "url": "/citations/szejda-et-al-2021/",
    "file_path": "Citations/Szejda et al., 2021.md",
    "title": "Szejda et al., 2021",
    "tags": ["Alternative_Proteins/Cultivated_Meat", "Consumer_Research"]
  }
]}
```

If the reply is an error instead (for example `{"error": "Unauthorized"}`), tell the user the RIAAK search isn't available right now, point them to https://riaak.netlify.app to search in the browser, and stop.

## Step 3: Decide which results are genuinely relevant

The search always returns something, even for an off-topic question, so getting results does not mean you found an answer. Judge each result by whether its `text` actually bears on the question.

- `score` is a rough similarity signal: around 0.5 or above is usually a solid match, and 0.35 or below is usually weak. Treat it as a hint, not a verdict. The results are already in relevance order.
- Keep the passages that address the question and drop the rest.
- If nothing is genuinely relevant, reply exactly:

  > I could not find information on that specific topic in the RIAAK knowledge base.

  Then point the user to https://riaak.netlify.app to browse. Do not make up an answer.

RIAAK only contains notes its editor has published, so a missing topic may simply not be covered yet.

## Step 4: Build a link for every source you use

- **Link text:** the `title` field.
- **Link address:** `https://riaak.netlify.app` followed by the `url` field (which always starts with `/`).

Example: `title` = `Szejda et al., 2021` and `url` = `/citations/szejda-et-al-2021/` gives
`[Szejda et al., 2021](https://riaak.netlify.app/citations/szejda-et-al-2021/)`

## Step 5: Write a short answer with inline links

- Give a brief, synthesised answer drawn only from the relevant passages.
- End every specific claim with its source link, for example:
  > South African consumers were very open to plant-based and cultivated meat ([Szejda et al., 2021](https://riaak.netlify.app/citations/szejda-et-al-2021/)).
- If several notes support one point, link them all.
- Keep direct quotes short and still link them.
- Tone: helpful, careful and neutral. The aim is to answer briefly and hand the user the sources to read for themselves.

## Step 6: List the sources

After the answer, add a list headed **Sources in RIAAK**: one link per note you used, with its tags, if any, as a short hint.

**Sources in RIAAK**
- [Szejda et al., 2021](https://riaak.netlify.app/citations/szejda-et-al-2021/): cultivated meat, consumer research

Finish with:

> Browse the full knowledge base at https://riaak.netlify.app

## Example

User: "Is there evidence that shrimp suffer at slaughter?"

Good: search `shrimp welfare slaughter`, keep the passages from the notes on shrimp welfare that talk about slaughter and pre-slaughter conditions, write two or three sentences that say only what those passages say, link each claim, then list the sources.

Bad: adding facts about shrimp nervous systems that are not in any returned passage, or listing every result including ones about fish or chickens that don't mention shrimp.

## Requirements

Needs internet access and a way to make an HTTPS request with a custom header.

- **Claude Code, OpenAI Codex, Gemini CLI, GitHub Copilot:** the agent runs the `curl` command above. Nothing to set up.
- **Claude.ai, Claude Cowork, ChatGPT and other chat apps:** the agent needs a tool that can make web requests with a custom header, such as code execution with internet access turned on. A plain web-browsing tool usually can't add the header, so the search will fail. If your agent can't make the request, search at https://riaak.netlify.app instead.

No account or sign-in is needed.
