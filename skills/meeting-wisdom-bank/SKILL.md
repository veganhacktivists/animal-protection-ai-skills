---
name: meeting-wisdom-bank
description: >-
  After a meeting where I gave advice, reads the full transcript and pulls out what is worth keeping from what I said: my advice and the reasoning behind it, ideas I raised, and short real stories I told that show a principle. Other people's points stay out. Each item is rewritten so a colleague, or a colleague's AI agent, can use it without having been on the call. Then saves the result to my wisdom bank as a Markdown file, Word document, Google Doc or Notion page. Use whenever someone says "add this meeting to my wisdom bank", "extract the wisdom from this call", "save the advice I gave in that meeting", "capture my feedback from today's one-to-ones", "what did I say in that call that my team should keep", or points at a transcript and wants the good advice kept for their team. Not for meeting summaries, minutes or action items.
license: MIT
metadata:
  version: "1.2.1"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-11-08"
  verified-on: "Claude Code"
---

# Meeting wisdom bank

Leaders in small organisations give a lot of good advice in meetings: feedback on a draft, the reason they turned an idea down, a story about what went wrong last time. Most of it is lost once the call ends, so the team keeps coming back to the same person for the same judgement, and everything waits on them. This skill reads a meeting transcript, keeps the user's own advice and judgement worth reusing, and saves it to a wisdom bank. The bank is a set of documents, one per meeting, that the user's team and the team's AI agents can look things up in later ("what would our director say about this draft?").

Each document has three sections:

1. **Wisdom.** Advice, feedback and judgement calls the user gave, with the reasoning behind them. Each is rewritten so a colleague in the same situation could act on it.
2. **Interesting ideas.** Experiments, half-formed plans and things to try that the user raised.
3. **Case studies.** Real stories the user told on the call that show a principle, one paragraph each.

Only the user's own contributions go in. The bank exists so a colleague's AI can answer "what would this person say?". Other people's advice, however good, would answer that question with someone else's judgement.

The readers are the user's colleagues and their AI agents, usually looking at one item at a time. So every item has to make sense on its own, lifted out of the document, to someone who was not on the call.

## Requirements

- **A meeting transcript.** The full transcript, from a meeting recorder (for example Fathom, Otter or Fireflies, or the transcripts Zoom, Google Meet and Microsoft Teams make), from a file, or pasted into the chat. If the agent has a connector to the user's recorder, it fetches the transcript itself.
- **Somewhere to save the bank,** in one of these formats:
  - Markdown files: an agent that can write files on the user's computer, such as Claude Code, Claude Cowork, Codex, Gemini CLI or GitHub Copilot.
  - Word documents: an agent that can create Word files. Coding agents need Pandoc or Python installed.
  - Google Docs: a Google Drive connector that can create files.
  - Notion pages: a Notion connector.
- **Setup.** "Your user's setup" below has to be filled in before the first run. The steps are in `README.md` in this folder.

## Your user's setup

If anything below still says `<not set up yet>`, stop. Tell the user the skill needs setting up first, and offer to follow "For AI agents setting up the wisdom bank" in `README.md`.

- **The user's name:** `<not set up yet>` (the name to use in the bank, plus every other name or email address transcripts use for them)
- **Where transcripts come from:** `<not set up yet>`
- **Document format:** `<not set up yet>` (Markdown file, Word document, Google Doc or Notion page)
- **Where to save it:** `<not set up yet>` (the folder or parent page. Each meeting becomes its own document there.)
- **Who can read the bank:** `<not set up yet>` (only the user, their team, or people outside the organisation too)
- **Always redact:** `<not set up yet>` (kinds of detail to leave out of every document, or "nothing beyond the built-in rules")
- **Meetings to skip:** `<not set up yet>` (kinds of meeting never to add, or "none")
- **Spelling:** `<not set up yet>` (British or American English, or another language)

## Rules that are always on

These are safety rules. Follow them whatever the setup says.

1. **Check with the user about redactions before saving.** Show them the draft and ask whether anything needs redacting, every time, even when the setup already lists things to redact. Save only after they answer. If nobody can answer (for example on a scheduled run), use best judgement and be extra cautious: redact all person and organisation names. The user's own name can stay. See "Running on a schedule".
2. **Leave out anything said off the record.** If someone on the call says something is confidential, off the record or not for sharing, leave out that passage and anything that depends on it.
3. **Leave out personal matters about anyone.** Health, family, pay, performance, job security and disagreements with named colleagues stay out, even when the advice around them is good. If the advice still works without the personal detail, keep the advice and drop the detail. Workload and how a team makes decisions ("every decision waits on one person") are not personal matters, so describe them plainly, without names.
4. **Name nobody except the user.** Everyone else on the call becomes a role: "a new campaigns manager", "a volunteer coordinator", "the other person on the call". People outside the call get the same treatment, unless they are public figures being credited for a published idea. This holds for document titles too.
5. **Never invent or improve on what was said.** Every item must trace back to something someone said in this meeting. See Step 3.
6. **Save only where the setup says.** Never send the document to anyone or put a copy anywhere else.

## Step 1: get the transcript

Work out which meeting the user means. Check its title and attendees against "Meetings to skip". If it matches, stop and tell the user in one line, without reading the transcript.

Then get the **full transcript**, from the source in the setup. If the user pastes one or points to a file, use that.

Read the transcript itself. Never work from the recorder's AI summary. Summaries keep the topics and drop exactly what this skill is after: the story someone tells in passing, the throwaway line that is the best advice in the call, the reason behind a decision. Read every line.

If you cannot find the full transcript, say where you looked and ask the user for it. On a scheduled run, skip that meeting and list it in your report. Don't build the document from a summary, a calendar entry or memory.

## Step 2: work out who said what

Sort out the speakers before you pick anything out. The user may appear under their full name, first name, email address or a speaker number. Transcribers garble names, so check them against the meeting's invite list where you can.

You need this because the bank holds only what the user said. If you get the speakers wrong, the bank fills up with someone else's views under the user's name. If you can't tell which speaker is the user, ask. On a scheduled run, skip the meeting and list it in your report.

Sometimes you can tell who the user is for most of the call but not for every line. For example, a stretch partway through may be labelled "Speaker 3", or two people may share one label. If something worth keeping comes from lines like these, don't guess who said it. Draft the item, add a line under it, `Unsure who said this: <timestamp>`, and ask the user about it in Step 6. On a scheduled run, leave these items out and list them in your report.

## Step 3: pick out the material

**Only what the user said.** Every item must be the user's own: advice they gave, an idea they raised or a story they told. Leave out other people's advice, ideas and stories, however good. Other people's words can appear only as the context the user's point needs, for example the question the user was answering ("Asked whether to delay the launch, ..."). If someone else made a point and the user agreed and gave their own reason, that reason is the user's, so it can go in. A bare "yes" or "good idea" is not enough.

**A pointed question can count as advice.** Some people advise mostly by asking questions. A question from the user counts as their advice when it clearly points to an answer, for example "Have you asked the funder before building it?". Write the item as the view the question points to, and quote the question, so readers can see how the user put it and the item doesn't sound firmer than it was. Open questions that don't point anywhere, such as "What do you think?", don't count.

A call where the user mostly listened, or was the one being advised, will give little or nothing. That is the right result. Don't pad it with other people's points.

**Be choosy, and keep it short.** The bank is a shortlist of what is worth reusing. Don't try to record the whole meeting. An hour-long call that is rich in advice usually gives three to eight pieces of wisdom, up to five ideas and up to five case studies. A status meeting may give nothing. The document for an hour-long call should rarely go past about 1,500 words. For a half-hour call, aim for about half that.

In testing, an hour-long call first produced 14 to 16 pieces of wisdom and about 4,000 words. Most items were true and well written, but a document that long doesn't get read. If a section has more than eight items, merge the ones that make the same point and cut the weakest: the most obvious, or the least likely to change what a colleague does. A thin meeting padded with truisms is worse than an empty section.

**Never invent or improve on what was said.** Rewording is fine. Adding advice of your own, making a claim firmer than the speaker made it, or filling in a detail nobody mentioned is not. If the speaker was unsure, keep the uncertainty.

When someone makes a general claim about what a product can or can't do ("our CRM can't send texts", "the models can handle very long skills"), add "(as of <month year>, unchecked)", using the month of the meeting. These claims go out of date fast, and an AI answering from the bank would otherwise repeat them as fact. Someone describing their own set-up ("mine sends Slack reminders") doesn't need it.

### Wisdom

Advice, feedback and judgement calls that would help a colleague. The test: **would someone who wasn't on this call do something differently after reading it?** If not, leave it out.

**Length:** the heading states the advice in one sentence. Under it, two or three sentences on why it works and how to do it, under about 80 words. If it needs more, it is probably two items, or you are retelling the conversation.

- **Keep the reasoning.** A rule on its own only covers the cases it names. The reason behind it lets a colleague, or an AI reading the bank, work out what the user would say about a case nobody has raised yet. So "Lead funder updates with what changed since the last report" is weaker than the same advice plus the reason the user gave for it.
- **Generalise it.** Advice given to one person about their situation becomes advice for anyone in that situation. Feedback on one draft becomes the standard behind it. An adviser telling a mentee "get your CEO to show the team something they built with AI" becomes "Leaders showing their own AI use gives staff permission to try it. Ask the most senior person to share one thing they did with AI at each all-staff meeting."
- **Keep the specifics.** Numbers, tool names, steps and the reasons behind them are what make an item useful. "AI adoption takes time" is a truism. "Expect a new automation to need tuning for its first few days, and tell people that up front, or they'll give up when day one goes slightly wrong" is wisdom.
- **Keep memorable phrasing.** When the user puts something memorably, quote it (under about 25 words). Their own labels for things are worth keeping exactly.
- **Keep the user's side of a disagreement.** If the user disagreed with someone and the disagreement is useful, give the other view in a few words, only so the user's position makes sense. The item is the user's position and their reasons.
- **Leave out descriptions that aren't advice.** "The director plans the week every Monday morning" describes a habit. It only counts as wisdom if it was offered as something others should do.

### Interesting ideas

Speculation, "what if we...", experiments to run, tools someone could build and predictions, when the user raised them. This is the half-formed material. In two or three sentences (under about 70 words), say what the idea is, why the user thought it might work and what is still open. If anyone on the call agreed to try it, say who, describing them by role as usual.

### Case studies

Whenever the user tells a real story that shows a principle: their own experience, or one they heard from another organisation. Stories that other people on the call tell stay out.

- **One paragraph, roughly 60 to 120 words:** the situation, what happened, how it turned out, and the principle it shows. Keep only the details the lesson needs.
- **The principle is one closing sentence**, no broader than this one story can support. It is your summary, so keep it modest.
- **Only real events.** "Imagine an organisation that..." is a hypothetical. If it is useful, it belongs under wisdom or ideas.
- **Don't fill gaps.** If the call didn't say how it turned out, say so ("It was still unresolved at the time of the call") rather than inventing an ending.
- **Something the user did on the call counts,** such as a live demo they gave that changed someone's mind. Credit it "Happened on the call".
- **One story per case study.** Don't merge two.

**Don't say the same thing twice.** If a case study's closing principle already states a piece of advice, don't also write that advice up as a wisdom item. Keep the case study, because a story is harder to come by than advice. Write a separate wisdom item only if it adds something the story doesn't, such as the steps to follow.

**If nothing passes these tests, stop.** Save nothing, and tell the user in one line why the meeting had nothing worth keeping.

## Step 4: redact

First apply the rules that are always on, then everything under "Always redact" in the setup. Then:

- **Organisations.** If only the user's own team can read the bank, the organisation they work for can be named (or organisations, if they work for several). If people outside it can read the bank, describe it by kind instead. Describe every other organisation by kind, including former employers: "a member company", "a partner sanctuary", "a funder". The user can tell you in Step 6 that one can be named.
- **Roles that point to one person.** In a bank only the team reads, "the colleague who approves every article" is as good as a name. That's fine for a harmless or positive story. If the person might mind, mark it "Check before saving".
- **Blur numbers that identify, keep numbers that teach.** "Eight hours a week logging donations by hand" carries the lesson, so keep it. An exact budget, staff count or city can point to one organisation or person, so round it or drop it.
- **Watch for details that identify in combination.** "The volunteer who joined in March and runs the Saturday stall" names nobody but points to one person. Describe people only as much as the lesson needs.
- **Watch for things the person would mind seeing.** If they would recognise themselves and be upset, blur it further or leave it out.
- **Mark anything you are unsure about.** Keep it in the draft and add a line under the item: `Check before saving: <why>`. The user decides in Step 6. Do the same for any item that sits right next to a passage the transcript says was removed, because the removed part may have been context the item needs.

If the transcript says a passage was removed, mention that once in the opening line of the document, and don't guess what was in it.

## Step 5: check the bank

If you can read the bank, check two things before you show the user anything:

- **An earlier document from this meeting.** If there is one, add the new items to it rather than making a second document, and tell the user in Step 6.
- **Advice the user has given before.** Look for items that repeat advice from earlier meetings, and add "Also said in <document name>." under each one. Advice someone gives again and again is usually central to their judgement, so readers should know it was repeated.

If you can't read the bank, skip this step and say so in your report.

## Step 6: check with the user

Always do this step when the user can answer. On a scheduled run, follow "Running on a schedule" instead. Show the user:

- the draft document
- a numbered list of anything you left out or blurred in Step 4, so they can put back anything that was fine
- every item marked "Check before saving"
- every item marked "Unsure who said this". Ask whether each one was the user's, and offer to leave them all out instead, so the user can skip checking them. Keep only the ones they confirm.
- one line naming anything you cut in Step 3 that they might expect to see, so they can ask for it back. If most of the advice on the call came from someone else, say so in that line, so the user knows why the document is short. Don't offer to put other people's points back in.

Then ask, in one short question, whether anything else needs redacting before you save it. Make the changes they ask for. If the changes were big, show the changed items again. Save only once they say it is fine, and remove the "Check before saving" and "Unsure who said this" lines before you do.

If the user asks you to redact the same kind of thing that they would want gone from every meeting, offer to add it to "Always redact" in "Your user's setup".

## Step 7: save it

Save the document in the format and place given in the setup:

- **Markdown:** a `.md` file in the chosen folder.
- **Word:** a `.docx` file in the chosen folder. Use Word's heading styles (Heading 1, 2 and 3) so the structure survives.
- **Google Doc:** a new Google Doc in the chosen Drive folder, with real headings. If your connector can only upload files, upload the document as HTML and have it converted to a Google Doc, then check the headings came through.
- **Notion:** a new page under the chosen parent page, with real headings.

Title it `Wisdom from <short meeting description> <YYYY-MM-DD>`, for example `Wisdom from weekly comms one-to-one 2026-11-03`. No names except the user's. For files, leave out characters some systems reject: `: / \ # ^ [ ] | ? *`.

## Document template

```markdown
# Wisdom from <short meeting description> <YYYY-MM-DD>

<One line: what kind of meeting, the date and roughly how long, with no names except the user's. Say if part of the transcript was removed. For example: "Weekly one-to-one with a new campaigns manager, 3 November 2026, about 45 minutes.">

Source: <where the transcript is, or "pasted into chat on <date>">

## Wisdom

### <The advice as one plain sentence>

<Two or three sentences, under about 80 words: why it works and how to do it.>

> "<Optional short quote, if the user put it memorably or advised by asking a question>"

*<The user's name>, <timestamp>*

Also said in <earlier document>.

## Interesting ideas

### <The idea in a few words>

<Two or three sentences, under about 70 words: what it is, why the user thought it might work, and what is still open.>

*Raised by <the user's name>, <timestamp>. <Only if someone agreed to try it: who, for example "The other person on the call agreed to try it.">*

## Case studies

### <Short name for the story>

<One paragraph, 60 to 120 words, ending on the principle it shows.>

*Told by <the user's name>, <timestamp>*
```

- Include the "Source" line only if just the user can read the bank. Otherwise leave it out, because a link or recording title usually shows who was on the call.
- Keep all three section headings even when one is empty, and write "Nothing from this meeting." under it, so readers can see it was checked.
- Each item gets its own heading, so a reader can link to or quote one item.
- Under each item the extra lines go in this order, and only when they apply: the quote, who said it and when, then "Also said in".
- Give the timestamp where the point starts, as plain text in the transcript's own format. Leave timestamps out if the transcript has none.

## Writing rules

- Use the spelling in the setup, and plain, everyday words. Quotes follow the setup's spelling too, because the spelling in a transcript comes from the transcriber.
- Each item must make sense on its own to someone who wasn't on the call. Explain any jargon or acronym the speakers took for granted. Explaining a term is not the same as adding to what was said.
- Fix obvious mis-transcriptions silently, inside quotes too, when the meaning is certain. Where you can't tell what was meant, write `[unclear in transcript]` rather than guessing.
- Avoid em dashes, semicolons and the other habits that make writing read as AI-written.

## Running on a schedule

Some people want this to run by itself after their meetings. Nobody can answer Step 6 on a scheduled run, so use your best judgement and be extra cautious:

1. Do Steps 1 to 5 for each meeting since the last run.
2. In place of Step 6, redact every person's and organisation's name, including the user's own organisation. The user's own name can stay. Leave out every item you would have marked "Check before saving" or "Unsure who said this".
3. Save each document to the bank, following Step 7.
4. Tell the user what was saved, if the agent has a way to (for example a notification, or an email or message to the user alone). List what you left out, so they can ask for it back the next time they are in a chat with you.

## Several meetings at once

For requests like "this week's one-to-ones" or "all my calls in September":

1. List the meetings in the range as a numbered list, each with a one-line guess at whether it is worth mining. Status meetings, logistics calls and calls where the user was the one being advised usually aren't. Leave out anything that matches "Meetings to skip". If there are more than five, ask the user to confirm the list before you start, because each transcript is long and costly to read.
2. If your agent can run sub-agents, give each meeting to its own sub-agent with this skill and that one meeting, so the transcripts don't crowd your context. Ask each to do Steps 1 to 5 and hand back its draft without saving anything. Otherwise do them one at a time.
3. Read every draft and check it against Steps 3 and 4. Then do Step 6 once for the whole batch: show all the drafts and ask one question about redactions, plus one about any items marked "Unsure who said this".

## Report back

After saving, tell the user briefly where the document is (with a link if there is one), how many items are in each section, and anything you couldn't do, such as a missing transcript.
