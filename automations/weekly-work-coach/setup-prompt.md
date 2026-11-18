# Set up: Weekly work coach

I want you to help me set up an automation that reads everything I asked my AI tools this week, works out what my week was really about, and then challenges me with five questions: what is the bigger question behind my work, how could I be more ambitious, are the questions I'm asking the right ones, what assumptions am I making, and am I working towards my key goals or getting bogged down in side projects. It should run once a week, at the end of my working week, and at the end I get a review I can read in about five minutes.

Richie, the AI Impact Director at Vegan Hacktivists, built this in Claude and shared it publicly. My tools are probably different from his, so don't assume I use the same ones. Work through the steps below in order, and ask me before you set anything up.

## Step 1: Tell me what you can do here

Before anything else, tell me in a few short lines which app you are and whether you can do each of these here:

- run this on a schedule without me starting it each time
- read my past chats with AI tools from the last 7 days (some tools, such as Claude Code and Codex, save chats as files on my computer; others keep them online, so you'd need a way to search them, or an export)
- run code on my computer, not just in an online sandbox (Richie uses a small script to collect the week's chats)
- read my calendar and the note or document where I keep my goals, and send a message to me (for example an email to myself or a Slack DM), through a connector, app or integration

If you're not sure, check rather than guess. If you can't do something, say so plainly and suggest the closest thing that would work, such as a different app, or a reminder for me to run a saved prompt by hand.

## Step 2: Ask me about my tools

This automation needs the jobs below doing. For each one, ask me what I use, then check whether you can reach it.

| Job | What it needs to do | Richie used | What others use |
|---|---|---|---|
| Chat history | read what I typed to my AI tools in the last 7 days (read only) | the saved chat logs of Claude Code and Codex, which are files on the computer | ChatGPT Work, Claude Cowork, Gemini, a folder of saved chats |
| Calendar | read the last 7 days of events with titles, guests and descriptions (read only) | Google Calendar | Outlook, Apple Calendar |
| My key goals | read a short list of my main goals, fresh on every run (read only) | a note in his notes app (Obsidian) | a Google Doc, a Notion page, Apple Notes, a text file |
| Where the review goes | send the review to me only | email to myself | Slack DM, a note, a chat message |

If you can't reach the tool I use, suggest options in this order, and tell me what each one means in practice:

1. connect the official connector or integration for it, and tell me how
2. use a different connector that can do the same job
3. a workaround, and say what it loses. For example, a chat export has to be requested by hand and covers my whole history, so it makes this a weekly job for me rather than an automation. My calendar's private sharing link works, but treat it like a password, because anyone with it can read my calendar. For my goals, the simplest workaround is to write them straight into the instructions in Step 4; that works, but then changing a goal means changing the automation.

If there's no workable option for a job, tell me, and suggest how the automation could work without it. The chat history is the one job it can't do without. The calendar is a bonus. Without my goals, it can still answer the first four questions, but not the fifth.

Richie's chat-collecting step is a script, and I don't have it. If you need one, write your own: what it does is listed under "What each run does". Before the trial, open one chat log from each tool I use and show me what you'd keep and drop, including how you'll spot this automation's own runs so it never reviews itself.

## Step 3: Ask me the rest

Ask me these, one or two at a time, and wait for my answers:

1. Which day, time and time zone should it run, and should it cover the last 7 days or just my working days? (Richie runs it on Friday evening and covers the last 7 days.)
2. Is any of my work or any folder off limits to it, and is anything too sensitive to quote in the review, such as client details, passwords or keys?
3. What are my key goals? (Richie keeps two one-line goals in a short note and edits it now and then, so the automation reads it fresh every week rather than remembering an old copy.)
4. What are the big areas of my work, and which of them count as commitments rather than side projects? (Richie names each week's threads by organisation or project. Work he owes an employer or a client counts as "committed work", never a side project, even when it serves no goal. Building his own tools and AI set-up counts as a side project, unless the time it saved clearly went to a goal. Personal admin, like home, health and money, is left out of the judgement.)
5. Is there anything I don't want it to raise? It can't remember past reviews, so name each one. (Richie has told it never to point out that one particular area is missing from his week, and never to raise one specific point he's already heard.)
6. Which of my calendars count as work, and which meetings count as client or partner work rather than internal? (Richie counts a call as client work when the guests come from outside his own organisations and the point was to help the other organisation. Useful signs are a booking-link title, a "booked by" line in the description, and guests' email addresses. Where it's unclear, the meeting is marked "probably".)
7. Do I want to keep the five questions, or swap some for questions that fit my own work and priorities? (Richie picked these five because they are the ones that help him. Show me the five in one line each before I answer.) If I change any, put my questions and headings in place of his under "What each run does", keep the rules that still apply, and drop any rule that only made sense for a question I removed.

## What each run does (the Step 4 trial run included)

1. Collect my typed requests from the last 7 days, from the chat history. Keep only the messages I sent, pasted text included. Drop the AI's replies, tool output, helper-agent threads, automated or scheduled runs (this one included), and text a tool injected into the chat. Also drop one-word replies like "ok", "yes", "carry on" and "thanks", because they carry no intent. Order the sessions by how much I wrote in them, most first. Note any prompts I repeat word for word, because they are habits, not new thinking, and use them under the third question. Shorten very long messages, and cap the total at what one run can handle, so a busy week doesn't break it.
2. Read the calendar for the same 7 days, using an explicit start and end. From it, pick out the client or partner calls, using my answer to question 6. Leave out internal meetings, one-to-ones with colleagues, group teaching, public talks, travel, focus blocks, out-of-office and anything personal. Write one plain bullet per meeting (date, who, which organisation, roughly what about, only if the calendar says so), at most twelve, and write "probably" where unsure. Use these meetings to name threads, count meetings and judge a quiet week, but say nothing about them beyond what the calendar says.
3. Group the sessions into up to nine real threads of work (fewer in a quiet week). A thread is a body of work, not a session. Name each in my own words, with how many sessions fed it. A run of client calls with nothing typed behind it is still a thread: call it meeting work, not AI work. Read my key goals fresh, then tag each thread with what it served: the goal it moves (quoted from my goals), "side project", "committed work" or "personal admin", using my answer to question 4.
4. Answer my five questions, in this order, using these exact headings:
   - **What is the bigger question here?** For up to four of the largest threads, name the larger question each is really part of. This is a reframe, not a summary. If the sentence could have been written from the session titles alone, it isn't one. Where two threads are secretly the same question, say so as its own point.
   - **How can I be more ambitious?** Up to five points. Find where I asked for the small version of something that could be much bigger: work done once by hand that would be worth more as a repeatable thing, a deliverable for one organisation that many could use, an analysis that stopped at "correct" when it could have been "quotable", a limit I accepted without testing whether it is real. Say concretely what the bigger version would be.
   - **I am asking AI questions, but are those questions the right ones?** Up to three parts, each under its own label. First, the best question I asked this week (one point: quote it and say what made it good). Second, where the question was at the wrong height (up to five points: quote my words, then give the question I should have asked instead; the commonest failure is "how do I do X" when the live question was "is X worth doing"; also flag where I asked the AI to execute when I should have asked it to disagree). Third, what I did not ask about at all (one point per gap: compare the threads with what matters to my work and is missing from the week, and say what the absence suggests).
   - **What assumptions am I making that you can challenge?** Up to six points. State the unstated premise, quote the request it is buried in, and give the real case against it. Favour the ones that would change what I do next week if wrong. If you have no case against one, leave it out.
   - **Am I working towards my key goals or getting bogged down in side projects?** Quote each goal exactly as I wrote it; don't add, merge or reword goals. Open with one sentence of verdict: the week was mostly on my goals, mostly committed work, mostly side projects, or split. Back it with real counts of sessions and meetings, never a made-up percentage. Then one point per goal on what actually moved it this week; if nothing moved a goal, say so plainly, because that matters most. Then two or three points on the side projects that took the most sessions: give the honest case for each (it quietly feeds a goal, and how, or it's a distraction) and say whether to keep, shrink, hand off, park or drop it. Then at most one point, only if there's a real case, on mislabelled work: something I treated as core that serves no goal, or a side project that was really my best goal work of the week. A thread only counts as goal work if you can name which goal it moves and how; "it saves me time" is not enough on its own.
5. Put the threads and the client-meeting bullets at the very end under "For reference (skip if you like)", after the five questions. I don't read them. Don't turn them into numbered points.
6. Send the review to me. If the chat history can't be read, or no chats are found for the week, send a two-line notice instead, saying what broke, with the error.

## Rules, and why

- Number every point in all five sections as one unbroken sequence (1, 2, 3 and so on to the end), never restarting under a heading, because I reply with things like "do 4 and 11". The verdict sentence and the part labels under the third question don't get numbers. Make sure the email and any on-screen copy use the same numbers. In an HTML email, give each numbered list after the first an explicit start number, because lists silently restart at 1 otherwise.
- Every point must cite a thread and quote my own words. The exception is a point about something missing (a goal nothing moved, a gap in what I asked) or about meeting-only work, which names the goal or the meetings instead. Delete any other point you can't anchor, because an unanchored point is generic.
- No generic coaching. If a sentence would be equally true for any knowledge worker, cut it. No praise section, no encouragement, no closing pep talk, because I want to be challenged, not reassured.
- Prioritise. Every count in these instructions is a maximum, not a target. Fewer, sharper points beat completeness, and a short section is fine. Cut anything you are lukewarm about.
- Be direct. Say the uncomfortable version.
- Invent nothing. Use real counts from the data or none. If you are unsure whether something happened, leave it out.
- Say nothing about a meeting that the calendar itself doesn't say. Don't open notes, transcripts or email to find out more, and don't guess what was discussed from a title.
- Plain English. Everyday words, one idea per sentence, no jargon.
- If the calendar can't be read, say so in one line with the error and carry on. A calendar failure never stops the review. And when reading the calendar, always give an explicit start and end, because some calendar tools silently leave out past events otherwise.
- If I typed very little that week (under about ten real requests), check the calendar before calling it a quiet week. If it was full of calls, say the week went into meetings and coach me on that. Only call a week quiet when both are light. Still do the review, still send it, and keep it short.
- If my goals can't be read, don't guess them. Under the fifth question, say in one line that the goals couldn't be read, skip its points, and still send the rest, because invented goals would make the verdict worthless.
- If the chat history can't be read or comes back empty, send only the two-line notice, never a review, because a review of nothing would look like a quiet week.
- Keep the whole review to about five minutes of reading.
- Never raise the topics I listed in Step 3, question 5.

## Never

- During a scheduled run, never create, edit or delete any file, task, note or record, other than saving the review where I said. During set-up, you may write the collection script, the run instructions and the schedule, once I've approved each.
- Never message anyone but me.
- Never change, reply to or delete a calendar event. Reading is fine.

## Step 4: Test it, then schedule it

1. Do one trial run now, on my real data. Show me the review here, and tell me what the collection step found and dropped. Then send it to me once, marked TRIAL, so we know delivery works.
2. Fix anything I don't like and run the trial again if needed.
3. Write out the instructions each scheduled run will follow, with my answers from Step 3 built in, and show them to me, because a scheduled run won't see this chat. Then set up the schedule. After the first couple of real reviews, I'll come back to this chat with any changes.
4. Finally, tell me when it will next run, what it needs to keep working (for example the app open, the computer awake, a connector staying signed in, and every permission it needs approved in advance, because nobody is there to approve a prompt), and how to pause or delete it.
