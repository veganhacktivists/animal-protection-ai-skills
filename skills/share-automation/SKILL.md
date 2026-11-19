---
name: share-automation
description: >-
  Packages one of the user's automations (a scheduled task, routine or recurring prompt in Claude Cowork, Claude Code, OpenAI Codex, ChatGPT or another AI tool, or one they paste in) into a single setup prompt that someone else pastes into their own AI. That AI checks what it can do, asks which tool they use for each job (which CRM, task manager, email, notes app and so on), suggests another connector or a workaround where it can't reach one, and sets up their own version on a schedule after a trial run that changes nothing. Use whenever someone says "share this automation", "package up my X automation", "make a setup prompt for X", "send my X automation to a colleague / friend / partner organisation", "turn this scheduled task into something someone else can use", "how would someone else set up my X", or names one of their automations and wants another person or organisation to have it. Not for writing a blog post about an automation, and not for building a new automation for the user themselves.
license: MIT
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-11-15"
  verified-on: "Claude Code"
---

# Share an automation

People want to hand their automations to friends, colleagues and partner organisations. The other person might use ChatGPT, Claude, Codex or something else, and almost certainly uses different tools: a different CRM, task manager, notes app or chat app. So copying the instructions across doesn't work. A working automation is full of its owner's accounts, folders, skills and quirks.

This skill turns one automation into **one setup prompt**. The other person pastes it into their own AI. Their AI then:

1. works out what it can do in that app (run on a schedule, reach connectors, read local files, use a browser);
2. interviews them about which tool they use for each job, checks it can reach each one, and suggests another connector or a workaround if not;
3. asks the few questions that tailor it to them;
4. does a trial run that changes nothing, then sets up the schedule.

The skill never sends anything to anyone, and never changes the automation itself.

## Requirements

None. Works with the agent alone: the user can paste the automation in. It works best in an agent that can also list the user's scheduled tasks or automations and their past runs, read files on the computer, save a file, and hand work to a helper agent (a subagent).

## Step 1: Find the automation and everything it depends on

The user names it loosely ("the weekly meetings review", "the downloads renamer"). Find it:

- If you can list the user's scheduled tasks, automations or routines, do so, and match their words against names, titles and descriptions. Check every kind you can reach: for example scheduled tasks in this app, routines that run in the cloud, and automations from another AI app whose files you can read on this computer. Say in the report which kinds you couldn't check.
- If you can't list them, or can't find a match, ask the user to paste the automation's instructions and tell you how often it runs.
- If the user pastes an automation in (say a ChatGPT task, or a colleague's prompt), work from what they pasted, with no need to search as well, and ask about anything it leaves out.

If a line could mean two things, and the choice changes what the automation does, ask. If you can't ask, turn it into a question in the setup prompt rather than guess, and list it in the report.

**Some scheduled tasks run several jobs**, each from its own instructions, and an older task may have been folded into one of these and deleted. So if the name doesn't match a task, search inside the tasks' instructions too. If the user names one job of a task like this, package only that job, and say in the report which other jobs share the task and were left out.

If two match, ask which one. If none match, list the closest names and ask.

**Then read everything the automation points to.** The other person has none of these files, so the setup prompt has to carry the substance of all of it:

- skills it loads (the whole skill, not only its description);
- the job's own instructions, if it's one job of a larger task;
- scripts it runs (read what they do, not just their names);
- any memory or notes the user or their agent keeps about it, if you can read them.

A loaded skill can be long. Carry over what would change how the other person's version behaves: the steps, the definitions, the lessons, the safety limits. Leave out record IDs, column names and other wiring for the user's own tools.

**Then look at how it has actually behaved,** if you can see its past runs. The run history is where the lessons are, and lessons are what a fresh AI would get wrong. Reading it is also the most expensive part of this skill: ten full run transcripts can cost a couple of hundred thousand tokens. So:

- start from each run's final report or summary, not its full transcript;
- open a full run only when the report shows a failure, a surprise or a fix;
- if you can hand work to a helper agent, give it this job and ask it to return only a short list of lessons, each with the date and what happened.

Up to the last 10 runs is plenty. If the job used to be its own task, its older runs may sit under the old task's name. If you can't see any runs, ask the user what has gone wrong or surprised them, and say in the report that you had no run history.

**The chat where it was built is optional.** If you can search the user's past conversations, one or two searches can explain why a rule exists. If they find nothing, or you can't search, move on, and say in the report which reasons you had to infer.

If a file you read changes while you work (scheduled tasks get edited often), read it again before you write the prompt.

## Step 2: Break it into jobs, rules and plumbing

This is the heart of the skill. Sort everything you learned into four piles.

### Pile 1: Jobs (the tools it needs)

Every specific product becomes a **job**, described by what the automation needs from it. For example:

| The user's tool | The job | What it needs to do |
|---|---|---|
| a monday.com board of client meetings | CRM | read existing entries for this week; add new entries after approval |
| Google Calendar | calendar | read last week's meetings with attendees |
| Todoist | task manager | list tasks completed in the last 7 days |
| an Obsidian vault | notes app | find and edit notes |

Be specific about **read or write**, because it changes which workarounds are acceptable. A CRM the AI only reads can be swapped for a weekly spreadsheet export. A CRM it must write to can't.

For each job, list a few common alternatives so the other person recognises the job straight away. Examples only, not a recommendation: CRM (HubSpot, Salesforce, Pipedrive, Airtable, Notion, a spreadsheet), task manager (Todoist, Asana, Trello, Things, Microsoft To Do), notes (Obsidian, Notion, Google Docs, Apple Notes), email (Gmail, Outlook), calendar (Google Calendar, Outlook), team chat (Slack, Teams, Discord, WhatsApp), files (Google Drive, OneDrive, Dropbox, a folder on their computer).

Also note any **abilities** it needs beyond connectors: running on a schedule, reading or writing files on the computer, a browser where the person is signed in, searching the web, running code or a command-line tool. Name only the ones it really needs, because each one narrows which apps can run it. For example, an automation that renames files in a Downloads folder needs local file access, which an app that runs in the cloud can't give it.

### Pile 2: Rules that travel

Lessons and safety limits that would help anyone. Keep these, each as an instruction with its reason:

- "Check what is already in the CRM before proposing anything, because otherwise it logs the same meeting twice."
- "If the task-manager lookup fails, say so at the top and label the review calendar-only, so a missing half never looks like a quiet week."

You may soften a rule that would misfire for someone else. For example, an automation that treats an unanswered invite as a meeting that didn't happen works for internal meetings, but outside partners often don't reply to invites. List every rule you changed in the report, so the user can check it.

### Pile 3: Rules that are the user's (or their organisation's) preferences

Rules that are right for the user but might not be for the other person. Don't keep these as rules and don't drop them. **Turn each one into a question, with the user's rule as the example answer.** For example, "planning meetings for a workshop are not billable" becomes:

> Are there kinds of work you never count? (My friend leaves out meetings that only plan a workshop. The workshop itself counts once it's delivered.)

This is where most of the tailoring comes from. It tells the other person's AI the kind of rule that matters, without forcing the user's choices on them. Refer to the user as "my friend" throughout, without a pronoun, and never by name.

### Pile 4: Plumbing (drop it)

Things that only exist because of the user's own setup: folder paths, sign-in renewals for a command-line tool, quirks of a messaging bridge, which of their skills to load, account names, time zone, workarounds for a connector that broke on their machine. Leave all of it out. If a piece of plumbing hides a lesson that travels (for example "the connector sometimes returns nothing without an error, so check the count"), move that lesson to Pile 2.

## Step 3: Make it safe to share

The test for every fact about a person or organisation:

> **If the person this fact is about read this, would they be annoyed that it was public?**

If yes, make it generic ("a partner organisation", "a colleague") or leave it out. Some things always come out, whatever the test says:

- names of real people and organisations from the user's examples or run history, and places or local groups that would identify them, unless the user says the recipient already knows them;
- email addresses, phone numbers, home addresses;
- API keys, tokens, passwords, account numbers, private calendar links;
- anything the user keeps off-limits to AI, such as a mail label or folder they've told AI not to read;
- details of partners, supporters or investigations that aren't already public;
- the user's own money, travel, health and personal documents, including real file names from the runs (a bank statement, a boarding pass);
- other people's health, money or private lives.

Product names, the kind of work, and the shape of the process are fine. Note every judgement call so you can list it in the report.

The same care applies to what the automation will handle, not only to what the prompt says. If its trial runs, reports or summaries would show sensitive details (children's names, health, money, supporters' or investigation details), add a rule to the prompt that keeps them out, with the reason.

## Step 4: Write the setup prompt

Use the skeleton in `references/setup-prompt-template.md`. Read it now. It gives the section order, the wording that makes the prompt work across ChatGPT, Claude and Codex, and a filled-in example.

The skeleton is a starting point, not a form. Keep its order and what each section does: check abilities, ask about tools with a way out for each, ask the rest, say what each run does, give the rules and limits, then test before scheduling. Rewrite any line that doesn't fit. For an automation that only touches files on the computer, for instance, the jobs table can shrink to a short list, and the connector options become "a folder you can reach".

Things that make or break the prompt:

- **Don't tell their AI what its app can or can't do.** The apps change month to month, and their AI knows its own app better than you do. Ask it to check and report instead. The template's first step does this.
- **Keep it neutral even when the user names the recipient's app or tools.** People switch apps and pass prompts on, and their AI asks anyway. Put what the user told you into the report instead: for example, "it needs files on the computer, so if they use ChatGPT in a browser, Step 1 will probably send them to a desktop app."
- **It must stand alone.** Their AI has never heard of the user, their skills or their files. Anything the automation gets from a skill or script has to be in the prompt, in plain words. If a script does something too fiddly to describe, say what it does and ask their AI to write its own version, or tell the user that the script needs sending as well.
- **Every connector question offers a way out.** For each job: ask what they use, check whether it can be reached, and if not, suggest options in this order: connect the official connector, use a different connector that can do the same job, or a workaround. Say plainly what each workaround loses (for example, "a weekly CSV export means it can read your CRM but not add to it").
- **A trial run that changes nothing comes first.** Anything that writes, sends, deletes or moves things proposes its changes and waits for an OK on the first runs. Keep any approval step the original has. If their app can't pause a scheduled run to wait for them, the run should write its proposals where they'll see them, and the changes are made once they approve, either in a chat or on the next run.
- **The limits are for scheduled runs, not set-up.** A blanket "never create a file" stops their AI from writing the script, run instructions and schedule it needs, so it can't follow the prompt at all. Put the hard limits under "During a scheduled run", and let set-up create only what the automation needs, each with their OK.
- **The scheduled run won't see the setup chat.** Their answers to the interview live only in that chat. So before scheduling, their AI must write the standing instructions with the answers built in and show them. The template's last step does this.
- **Runs don't remember each other either.** If the automation handles "everything since last time", set-up must create a note of when it last made its changes. A run that only proposes changes must leave that note alone, so nothing is lost if they haven't approved before the next run.
- **Their AI is capable.** Don't explain how to make a schedule, call a connector or write a loop. Spend the words on what it wouldn't know: the jobs, the lessons, the safety limits and the questions.
- **Keep the interview short.** Beyond the job questions, ask 3 to 6 questions that really change how it's set up. Tell their AI to ask one or two at a time and wait.
- **Length.** The fixed wording alone is about 500 words, so most prompts land between 700 and 1,500. One with several jobs that write, or with safeguarding rules, can run longer. Stay at the low end when you can, but don't cut a lesson or a safety limit to save words.
- **Plain English.** It will be read by the other person as well as their AI. No jargon without a short explanation. No em dashes, because many readers take them as a sign of AI writing.

Then check it against this list and fix anything that fails:

1. Would it make sense pasted cold into ChatGPT, Claude or Codex, by someone who has never met the user?
2. Does every product name appear only as an example of a job, never as an assumption?
3. Does every job ask what they use, check it can be reached, and offer an alternative?
4. Did every personal rule become a question rather than a rule?
5. Are the hard-won lessons in, each with its reason?
6. Does it test before scheduling, and ask before writing, sending or deleting anything?
7. Does it have their AI write out the standing instructions before scheduling?
8. Does it end by telling them when it will run, what keeps it working, and how to pause or delete it?
9. Is anything from Step 3 still in it?

## Step 5: Cold-read check

If you can hand work to a helper agent, paste the **full text of the setup prompt** into its brief. Don't give it a file path, because a real recipient only ever sees the text. Brief it like this: "Someone has just pasted the text below into a chat app. Answer three times: as ChatGPT, as Claude, and as Codex. Each time, without doing anything, list what you'd ask them first, anything you couldn't work out, any instructions that contradict each other, and anything that assumes tools or knowledge you don't have." Fix what it finds, including the template's fixed wording where that is the problem. It isn't the same as watching a real person use the prompt, but it catches contradictions and missing context. It costs about as much as reading a few full runs (one check took about 100,000 tokens), so skip it for a very short automation, or if you can't hand work to a helper.

## Step 6: Save it and report back

If you can save files, save the prompt as a Markdown file named `<Plain name> - setup prompt.md`, in the folder the user asks for. If they haven't said, suggest a folder (for example a `Shared automations` folder in their documents) and check before creating it. Never overwrite an existing file: if the name is taken, add the date. At the top of the file, above the prompt, add one line saying what it is and how to use it ("Paste everything in the box below into ChatGPT, Claude or Codex and answer its questions."). Put the prompt itself in a fenced code block so it copies cleanly.

If your app can send or attach files to the user, send the file too. Always paste the prompt into the reply as well, in a code block, so it can be copied from a phone. If you can't save files, the reply is the only copy, so say so.

If it should be shared more widely than one person, there are two other homes for it:

- **For the movement:** submit it as an automation to the public [animal-protection-ai-skills](https://github.com/veganhacktivists/animal-protection-ai-skills) library, as a folder at `automations/<name>/` holding the prompt as `setup-prompt.md` and a `README.md` guide for the person setting it up. Follow the "Automations" section of that library's `CONTRIBUTING.md`. It asks for frontmatter in the README, and for scheduled runs that only read, apart from delivering the result, so an automation that writes or sends things may need changing first.
- **For the user's own team:** if their organisation keeps a shared library of skills or prompts, it can go there, following that library's rules.

Then report, using the user's own report format if they have one. Number every item in one unbroken sequence, so they can reply "change 3 and 7". Cover:

- each privacy judgement call (what you made generic or left out, and why);
- each personal rule you turned into a question, and each rule you softened;
- anything that can't travel, or that only works with certain abilities (for example "needs files on their computer, so it won't run in an app that runs in the cloud");
- for a task that runs several jobs, the other jobs you left out;
- anything you couldn't find or check (no run history, no build chat, a script you couldn't read, kinds of automation you couldn't list);
- whether you did the cold-read check and what it changed.

Never send the prompt to the recipient yourself. If the user wants a covering message, draft it in their voice and wait for them to say send.
