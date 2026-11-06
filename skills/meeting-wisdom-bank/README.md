# Setting up meeting-wisdom-bank

After a meeting where you give advice, this skill reads the transcript and pulls out your own advice, judgement calls, ideas and stories worth keeping. Other people's points stay out, so the bank holds only your judgement. It checks with you about anything that needs redacting, then saves them to your wisdom bank: a set of documents, one per meeting, that your team and their AI agents can look things up in. Over time the bank holds your judgement, so colleagues can ask their AI "what would you say about this?" instead of waiting for you.

## What you need first

- **Meeting transcripts.** A meeting recorder that makes full transcripts, such as Fathom, Otter or Fireflies, or the transcripts Zoom, Google Meet and Microsoft Teams make. If your AI agent can connect to your recorder, it fetches transcripts itself. In Claude or ChatGPT, add your recorder's connector if it has one. Otherwise, download the transcript or paste it into the chat.
- **Somewhere for the bank,** in the format you choose during setup:
  - Markdown files: an agent that can write to a folder on your computer, such as Claude Code, Claude Cowork or Codex.
  - Word documents: an agent that can create Word files. In the Claude app, turn on file creation. Coding agents such as Claude Code or Codex need Pandoc or Python installed.
  - Google Docs: a Google Drive connector that can create files. In Claude, connect Google Drive.
  - Notion pages: a Notion connector. In Claude, connect Notion.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install meeting-wisdom-bank@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `meeting-wisdom-bank` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat, and fill in its "Your user's setup" section by hand. This works less well: the AI only has the instructions in that one chat or project.

## What the setup asks you

When your agent installs the skill, it asks you a few questions and writes your answers into its copy of the skill. It helps to have answers in mind:

1. What form each document should take: a Markdown file on your computer, a Word document, a Google Doc or a Notion page. Pick whatever your team already reads, so they can find it.
2. Where to save it (a folder or a parent page), and who can open that place.
3. What kinds of things, if any, should always be redacted. For example donor or funder names, details of investigations, legal matters, partner organisations' confidential plans, unreleased campaigns, or figures about money or staff.
4. Kinds of meeting that should never go in the bank at all, such as HR conversations or board meetings.
5. Where your transcripts come from, how your name appears in them, and which name the bank should use for you.

When you run the skill yourself, it also shows you the draft and asks whether anything else needs redacting. Nothing is saved until you answer. When it runs on a schedule it can't ask you, so it is extra cautious: it removes every person's and organisation's name except yours, and leaves out anything it is unsure about. Some rules are always on and can't be switched off: nobody except you is named, personal matters (health, pay, performance, conflicts) stay out, anything said off the record is left out, and it only saves where you told it to.

## Checking it works

Pick a meeting where you were clearly the one giving advice, such as a feedback session, a mentoring one-to-one or a one-to-one with someone you manage. A call where you mostly listened gives a short or empty document. That is the right result, but it won't show you much.

Ask your agent: "Add my last meeting to my wisdom bank", or paste in a transcript and ask "Extract the wisdom from this call for my wisdom bank".

A good result is a short draft with three sections (Wisdom, Interesting ideas, Case studies). Every item is something you said. Each has its own heading and makes sense to someone who wasn't on the call, and nobody is named except you. The agent lists anything it left out or blurred, then asks whether anything else needs redacting before it saves.

## How your team uses the bank

Your colleagues point their AI agent at the bank's folder or page and ask things like "What would our director say about this draft?" or "What has our director said about writing to funders?". Answers get better as more meetings go in. Every month or so, someone can also ask their AI to turn the bank into a shared skill (for example "Ask <your name>"), so everyone's AI applies it without being pointed at the folder.

Answers from the bank are an AI's reading of what you said. Ask your team to treat them as a first opinion, and to check with you before acting on anything important.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking. Creating the bank's folder or page, and the scheduled task in step 8, are the only exceptions, and only once the user has asked for them.
5. **Look before you ask.** Work these out yourself first, then report what you found:
   - Which meeting recorders you can reach. Check your own tools first, and only ask about a recorder you can't see.
   - Which places you can save to: a folder on the user's computer, Google Drive, Notion, or none of these.
   - Whether you can create Word documents.
   - The user's name, from your account details or their recent transcripts, and how it appears in those transcripts.
   - Which spelling they use (British or American English, or another language), from their own writing. Don't ask them about it.
6. **Ask.** Cover these, adapting the wording but keeping the intent. Recommend an answer wherever you can.
   - What form should each document take: a local Markdown file, a Word document, a Google Doc or a Notion page? Only offer the ones you can actually create. If they are unsure, recommend the one their team already uses.
   - Where should it be saved, and who can open that place: only them, their team, or people outside their organisation too? Each meeting becomes its own document there. If the folder or page doesn't exist yet, offer to create it.
   - What kinds of things, if any, would they want redacted from every document? Suggest examples that fit their work, such as donor or funder names, details of investigations, legal matters, partner or member organisations' confidential plans, unreleased campaigns, or figures about money or staff. "Nothing beyond the built-in rules" is a fine answer.
   - Are there kinds of meeting that should never go in the bank, such as HR conversations, board meetings or calls with funders?
   - Where do their transcripts come from, if you couldn't tell? Does their name appear in them any other way, and which name should the bank use for them?

   Don't ask whether to check with them before saving, or about the other rules under "Rules that are always on". Those are safety rules and are already built into the skill.
7. Fill in every line of "Your user's setup" in your installed copy of `SKILL.md` with their answers.
8. If they want it to run by itself after meetings, create a scheduled task that follows "Running on a schedule" in `SKILL.md`. Once a day in the early evening usually works. Tell them a scheduled run can't check with them, so it saves straight to the bank after removing every person's and organisation's name except theirs, and leaves out anything it is unsure about.
9. Offer to run the request under "Checking it works" on a recent meeting where they were clearly the one giving advice.
