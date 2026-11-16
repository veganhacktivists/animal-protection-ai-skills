# Setup prompt template

Fill in the parts in angle brackets. Keep the section order, and keep the fixed wording wherever it fits: it is what makes the prompt work in ChatGPT, Claude and Codex alike. Rewrite any fixed line that doesn't fit this automation (for example, connector wording for an automation that only touches files on the computer), and cut any section that has nothing in it.

Write it in the first person, as the other person speaking to their own AI ("I want you to set up..."). It reads naturally when they paste it, and their AI treats it as their request.

---

## Skeleton

```
# Set up: <plain name of the automation>

I want you to help me set up an automation that <what it does, in one or two sentences>. It should run <how often, in plain words>, and at the end I get <the result: a message, an updated record, a file>.

A friend built this in <Claude / Codex / ChatGPT> and shared it with me. My tools are probably different from theirs, so don't assume I use the same ones. Work through the steps below in order, and ask me before you set anything up.

## Step 1: Tell me what you can do here

Before anything else, tell me in a few short lines which app you are and whether you can do each of these here:

- run this on a schedule without me starting it each time
- connect to other apps and services through connectors, apps or integrations, and use them during a scheduled run, not only in this chat
<only the abilities it really needs, for example:>
- read and change files on my computer
- use a web browser where I'm signed in to <site>
- run code

If you're not sure, check rather than guess, but don't connect anything yet. If you can't do something, say so plainly and suggest the closest thing that would work, such as a different app, or a reminder for me to run a saved prompt by hand.

## Step 2: Ask me about my tools

This automation needs the jobs below doing. For each one, ask me what I use, then check whether you can reach it.

| Job | What it needs to do | My friend used | What others use |
|---|---|---|---|
| <job> | <read / write, and what exactly> | <product> | <3 to 5 examples> |

If you can't reach the tool I use, suggest options in this order, and tell me what each one means in practice:

1. connect the official connector or integration for it, and tell me how
2. use a different connector that can do the same job
3. a workaround, such as <the realistic workaround for this automation>, and say what it loses <for example: it can read but not write>

If there's no workable option for a job, tell me, and suggest how the automation could work without it.

## Step 3: Ask me the rest

Ask me these, one or two at a time, and wait for my answers:

1. <schedule: when and how often>
2. <scope: what counts, what's in and out>
3. <a personal rule turned into a question, with the friend's choice as the example>
4. <how cautious: propose and wait for my OK, or act on its own once I trust it>
5. <where the result should go>

## What each run does (only after the Step 4 trial)

1. <step, using the job names, not product names>
2. <step>
3. <step>

## Rules, and why

- <lesson as an instruction>, because <reason>.
- <lesson>, because <reason>.

## Never

During a scheduled run:

- <hard safety limit, for example: never delete a record>
- <never send a message to anyone without my OK>

During set-up, you may create only what the automation needs to run (for example its run instructions, any script it needs, a note of when it last ran, and the schedule), and only once I've approved each one.

## Step 4: Test it, then schedule it

1. Do one trial run now, on my real data, without changing anything. Show me what it found and what it would have done.
2. Fix anything I don't like and run the trial again if needed.
3. Write out the instructions each scheduled run will follow, with my answers from Step 3 built in, and show them to me, because a scheduled run won't see this chat. Then set up the schedule. <If it writes or sends:> For the first <two> runs, propose changes and wait for my OK before making them. If you can't pause a scheduled run to wait for me, write the proposals somewhere I'll see them, and make the changes once I approve them, either when I tell you in a chat or on the next run. A run that only proposes changes doesn't count as done, so the next run still covers what it found.
4. Finally, tell me when it will next run, what it needs to keep working (for example the app open, the computer awake, a connector staying signed in, and every permission it needs approved in advance, because nobody is there to approve a prompt), and how to pause or delete it.
```

---

## Filled-in example

This is a made-up automation, shown only to make the pattern concrete. Don't reuse its wording for other automations: write each prompt from what that automation actually does.

```
# Set up: Monday morning "what's slipping" digest

I want you to help me set up an automation that looks at my overdue and due-this-week tasks alongside my calendar, works out which ones I realistically won't get to, and sends me a short list of what to drop, delegate or move. It should run every Monday morning, and at the end I get one short message.

A friend built this in Claude and shared it with me. My tools are probably different from theirs, so don't assume I use the same ones. Work through the steps below in order, and ask me before you set anything up.

## Step 1: Tell me what you can do here

Before anything else, tell me in a few short lines which app you are and whether you can do each of these here:

- run this on a schedule without me starting it each time
- connect to other apps and services through connectors, apps or integrations, and use them during a scheduled run, not only in this chat

If you're not sure, check rather than guess, but don't connect anything yet. If you can't do something, say so plainly and suggest the closest thing that would work, such as a different app, or a reminder for me to run a saved prompt by hand.

## Step 2: Ask me about my tools

This automation needs the jobs below doing. For each one, ask me what I use, then check whether you can reach it.

| Job | What it needs to do | My friend used | What others use |
|---|---|---|---|
| Task manager | read open tasks with due dates (read only) | Todoist | Asana, Trello, Things, Microsoft To Do, Notion |
| Calendar | read this week's events (read only) | Google Calendar | Outlook, Apple Calendar |
| Where the digest goes | send me one message | email to myself | Slack DM, a note, a chat message |

If you can't reach the tool I use, suggest options in this order, and tell me what each one means in practice:

1. connect the official connector or integration for it, and tell me how
2. use a different connector that can do the same job
3. a workaround, such as my calendar's private sharing link or an export of my tasks, and say what it loses (an export goes stale, so the digest is only as fresh as the last export)

If there's no workable option for a job, tell me, and suggest how the automation could work without it.

## Step 3: Ask me the rest

Ask me these, one or two at a time, and wait for my answers:

1. Which day and time should it run?
2. How many hours a week do I really have for tasks, after meetings? (My friend assumes about 60% of free calendar time, because the rest goes on email and interruptions.)
3. Are there tasks it should never suggest dropping? (My friend marks those with a label.)
4. Where should the digest go?

## What each run does (only after the Step 4 trial)

1. Get my open tasks that are overdue or due in the next 7 days, from the task manager.
2. Get this week's calendar and work out roughly how many free hours I have.
3. Compare the two and pick the tasks least likely to get done.
4. Send one short message: what to drop, what to delegate, what to move, with a one-line reason each.

## Rules, and why

- Count all-day events as free time unless they're marked busy, because most all-day events are reminders, not meetings.
- Never suggest dropping more than five tasks, because a long list gets ignored.
- If the task-manager lookup fails or comes back empty, say so at the top of the message, because an empty list looks exactly like a good week.

## Never

During a scheduled run:

- Never change, move or complete a task yourself. Only suggest.

During set-up, you may create only what the automation needs to run (its run instructions and the schedule), and only once I've approved each one.

## Step 4: Test it, then schedule it

1. Do one trial run now, on my real data, without changing anything. Show me what it found and what it would have done.
2. Fix anything I don't like and run the trial again if needed.
3. Write out the instructions each scheduled run will follow, with my answers from Step 3 built in, and show them to me, because a scheduled run won't see this chat. Then set up the schedule.
4. Finally, tell me when it will next run, what it needs to keep working (for example the app open, the computer awake, a connector staying signed in, and every permission it needs approved in advance, because nobody is there to approve a prompt), and how to pause or delete it.
```
