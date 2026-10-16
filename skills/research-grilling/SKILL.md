---
name: research-grilling
description: >-
  Interviews the person running a research project, round by round, until every decision about purpose, scope, data, evidence and methods is settled, then writes a research brief plus a list of questions to send the client. Use whenever someone is starting, scoping or kicking off a research project, has just won or been sent a proposal, RFP or project brief, or says "grill me on this project", "research grill", "kick off this project", "what do we need to ask the client", "iron out the methods" or "pin down the methodology", even if they never say "grill". Also use when the client's answers come back and the brief needs updating. For plans that are not research projects, a general grilling skill fits better.
license: MIT
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-10-13"
  verified-on: "Claude Code"
---

# Research grilling

Before a research project starts, interview the person running it until every decision about the research is settled, then write those decisions down as a brief. Questions that only the client can answer go into a separate list to send them. A project pinned down this well can be picked up by a researcher, or an AI agent, who missed every conversation about it.

This adapts Matt Pocock's `grilling` skill ([github.com/mattpocock/skills](https://github.com/mattpocock/skills), MIT licence, see `LICENSE`) for research projects. Three things change from the coding version:

1. Research projects share a known set of decisions, listed under "The branches" below, so the session starts from those instead of from nothing.
2. Some decisions belong to the client, not the team. Those are parked in a list for the client with a recommended answer, so they don't hold the session up.
3. The session usually pauses for days while the client replies, so progress is saved to a file after every round and can be picked up in a new chat.

## Requirements

None. Works with the agent alone.

It works better when the agent can search the web and read the user's files (the proposal, call notes or transcripts, past reports), because it looks facts up instead of asking. In Claude, turn on web search and give it the files or a connector to the drive they are kept in (for example Google Drive or SharePoint). In Codex, Gemini CLI and GitHub Copilot, run it from the project's folder. Agents that can run sub-agents (Claude Code, Claude Cowork) can look facts up while the questions continue.

## Before the first round

Most answers are already written down somewhere, and asking the user for them wastes their time. So gather what exists first:

- **The proposal, RFP or project brief.** If the user hasn't given you one, ask for it, or for a few sentences describing the project if there isn't one. This is the only thing worth asking before round 1.
- **Call notes or transcripts** from conversations with the client, if the user can point you to them. Use the full transcript, not a recorder's summary, where both exist.
- **Anything else the user names:** past related projects, the client's website, data sources.
- **An existing brief from an earlier session.** If one exists, you are resuming (see "Resuming").

Read them, then build the tree of decisions from the branches below. Mark every decision the proposal already settles, and list those at the top of round 1 in one line each ("The proposal says the survey covers the UK and Germany, so I've taken that as settled"). The user can correct any of them.

## The branches

Every research project has to settle these. Each one opens further decisions as answers come in, and a later answer can reopen an earlier branch.

1. **What the research is for.** What decision will the client make with it? Who will read it, and how: in a presentation, on a laptop or on a phone? Will they want to dig into the data themselves?
2. **Scope.** Which countries, time period, species, products or sectors? What must be included and what should be left out? Watch for scope the proposal assumes but never states. For example, if the client works mainly in Latin America but the proposal doesn't say so, do they want the Latin American context or the global one?
3. **Prior work.** Has this been researched before, by the client, by us or by anyone else? What can we build on instead of redoing?
4. **Foundational concepts.** What has to be understood in depth before anything else? A project on how divestment campaigns raise the cost of capital for animal agriculture first needs an estimate of that cost of capital.
5. **Evidence standards.** Which sources count? Unless the project calls for something else, recommend this: peer-reviewed papers and government data first, then think-tank reports, then blogs and news. Back key claims with more than one source, flag sources from the animal agriculture industry, and cite the original report, not coverage of it.
6. **Data.** Good data makes or breaks a project, so grill this branch harder than any other, and go through it for every objective. Most projects that go wrong do so because the data turned out to be missing, late, too coarse or not what everyone assumed.
   - **What answers each objective.** For each research question, which data would answer it? Raise any objective with no data source now, not in week 6.
   - **Whether it exists and who holds it.** Is it public, paid for, held by the client, or something we collect ourselves? Under what licence, and can we publish results from it and hand it over at the end?
   - **Access.** How and when do we get it? Who has to sign what (a data-sharing agreement, data protection paperwork), and how long will that take? Recommend getting a sample of every dataset in week 1, because the problems only show once someone opens the file.
   - **Coverage and detail.** Does it cover the right countries, years, species and products? Is it detailed enough (regional or national, monthly or yearly)? Is it recent enough, and will it be revised partway through the project?
   - **Definitions and units.** Does each source define things the same way across countries and years (what counts as "farmed", tonnes or head counts, which currency and base year)? Where datasets need joining, can they be, and on what?
   - **Quality.** How was it collected, how big is the sample, what is missing, what biases are known, and who paid for it? Flag data from the animal agriculture industry.
   - **Data we collect ourselves.** For a survey: the panel, sample size and what it can detect, quotas and weighting, attention checks, translation, a soft launch, consent and ethics review. For interviews or focus groups: who, how many, how they are recruited and how they are recorded.
   - **Handling.** Where the data is stored, whether it holds personal data, how it is anonymised, and what the client gets at the end (the data, the code, or both).
   - **The fallback.** What happens if the data falls through or turns out worse than expected? If the ideal data doesn't exist, list the proxies that do, with what each gets right and wrong, and let the user choose. Never plan to fill a gap with a number nobody can source.
7. **Methods.** The analysis approach, and every choice where reasonable analysts could disagree: which control variables, how to handle outliers and missing data, which definitions to use, what counts as a meaningful result. When AI does part of the analysis, any choice left open gets made without anyone noticing, and differently each time. Scott Cunningham ran 15 Claude Code sessions on the same dataset and question and [got noticeably different results](https://causalinf.substack.com/p/claude-code-28-multiple-agents-auditing).
8. **Constraints.** Deadline, budget or days available, who on the team does what, and what the client provides (data access, introductions, sign-off). The proposal usually settles these, so confirm them instead of asking afresh.
9. **The finished product.** Format, length, graphs, interim drafts, who signs off. If the project went well, what would the press release say?
10. **What could go wrong.** Imagine the project has failed and ask why. Each plausible reason is either a risk to plan for or a decision still missing from the tree. Ask about the data first: what happens if it arrives late, is patchier than promised, or doesn't say what everyone assumed?

Spend the most rounds on data and methods. Expect the data branch alone to take more than one round.

## Three kinds of question

Sort every unsettled decision before you ask it, because each kind is handled differently.

- **Facts** can be looked up: whether research on the topic already exists, what data is available and how detailed it is, what the client has published, what one of your organisation's past reports found. Finding facts is your job, never the user's. If you can run sub-agents, send one per fact and carry on asking the questions that don't depend on it. Otherwise, look facts up between rounds. Check the user's organisation's past reports too, if you can reach the drive or folder they are kept in. Otherwise, search the web. Data is where looking things up pays off most: open each source and check its years, countries, variables, units and licence yourself, and download a sample where you can, instead of trusting someone's description of it. Some facts live only in the user's head, such as what the costing assumed or what was said on an unrecorded call. Look first, and ask only when nothing written down has the answer.
- **Team decisions** are choices the research team can make, mostly about data, methods, evidence and constraints. Put these to the user in rounds.
- **Client decisions** are choices only the client can make: what the research is for, scope, audience, what the finished product looks like, and access to any data the client holds (what they can share, in what form, and by when). Don't ask the user to guess these. Park each one in the client list with your recommended answer, and carry on using that answer as a flagged working assumption, so the rest of the tree isn't blocked. The user can move any parked question back ("we can decide that ourselves"), and can send any question to the client list by answering "ask the client".

## Rounds

Work the tree in rounds. The frontier is every unsettled team decision whose prerequisites are already settled or assumed: the questions you can ask now without guessing at answers you haven't heard yet. A question that depends on another question in the same round belongs to a later round.

Ask the whole frontier in one round. If it holds more than about ten questions, ask the ones that unblock the most first and say how many are waiting.

Format each round like this:

```
❓ **Q1** - **<question title>**: <the question, with the options where there is a real choice>

➡️ <your recommended answer, and the reason in one sentence>

---

❓ **Q2** - **<question title>**: ...

➡️ ...
```

Word each question so that "yes" accepts your recommendation. Base recommendations on the proposal, the facts you have found and the defaults above, and say when one is a guess.

Keep each question to two or three sentences and each recommendation to one or two. A round of ten long questions gets skimmed, and skimmed answers settle nothing. Put the facts you found in a short list before the questions, so the questions themselves can stay short.

Number questions continuously across rounds (if round 1 ends at Q6, round 2 starts at Q7), so the user can answer anything by its number.

End every round with:

- **Parked for the client:** numbered, one line each, with the working assumption.
- **Still looking up:** any facts that sub-agents are still finding.

Then wait for the user's answers. When they arrive, update the brief file with what was settled (see "Finishing" for the file), so nothing is lost if the chat stops. Recompute the frontier and ask the next round.

## Finishing

The session is done when no team decisions are left on the frontier: every branch is settled, parked for the client, or waiting on a fact. Say so, sum up the main decisions in a few lines, and ask the user to confirm you have reached a shared understanding. Don't start the research itself until they do.

Before writing anything up, check the numbers and facts the decisions rest on: that each dataset covers what the brief says it covers, sample sizes and what they can detect, costs against the budget, and what the law or earlier research already says. People make slips under time pressure, and a brief built on a wrong number sends the whole project the wrong way. If a check changes a decision, don't quietly fix it in the brief. Write the brief with that decision marked "Open", and put it to the user as a new round.

Then write two files in the project's folder, or the current folder if there isn't one:

1. `<project name> - research brief.md`, following `references/brief-template.md`.
2. `<project name> - questions for the client.md`, following `references/client-questions-template.md`.

Tell the user where they are. Offer to turn the client questions into a Google Doc or an email draft if a tool for that is connected. Never send anything to the client yourself.

## Resuming

The client's answers usually come back days later, in a new chat. When the user says the client has replied, or pastes their answers, find and read the brief, then apply each answer:

- **It matches the working assumption:** mark it confirmed.
- **It differs:** change the decision, then follow it down the tree. A change of scope or purpose can reopen methods decisions, so run new rounds on whatever it unsettles.
- **The client didn't answer it:** keep the working assumption, and say in the brief that it was never confirmed.

Then rewrite both files and tell the user what changed.

## Writing

Write in plain British English, with no em dashes. The brief is for the team: be specific, and record each judgement call with the reason for it. The client questions go to the client: keep them short, warm and free of jargon, and leave out internal notes.

Write the brief so that someone who missed every conversation (a new researcher, or an AI agent asked to draft part of the work) could start from it alone.
