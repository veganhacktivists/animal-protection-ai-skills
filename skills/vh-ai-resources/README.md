# Setting up vh-ai-resources

This skill lets your AI agent search the free [Vegan Hacktivists AI Resource Library](https://resources.veganhacktivists.org) for you. Ask it something like "Does VH have anything on writing an AI policy?" It reads the library, opens the best matches, and tells you which few will help with what you're doing, and why. The library has how-tos, prompts, case studies, guides, trainings, tool overviews and FAQs for people doing animal protection work.

You can also set up an optional weekly email: a scheduled task that looks back over your chats, uses this skill to find resources that fit what you worked on, and emails them to you. It needs more from your AI agent. See "Optional: a weekly email of resources" below.

## What you need first

- **An AI agent that can open web pages or search the web.** Most can. If yours has a web search or web access setting, make sure it is on.
- Nothing else. Searching the library needs no account, key or connector.

## Installing it

- **Claude Code and OpenAI Codex:** give your agent the link to this folder, https://github.com/veganhacktivists/animal-protection-ai-skills/tree/main/skills/vh-ai-resources, and ask it to install the skill. It downloads the folder and does the rest.
- **Claude Cowork:** download the `vh-ai-resources` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **ChatGPT Work:** make a skill through ChatGPT's own skill-creation flow, giving it the link to this folder or the contents of `SKILL.md`. Or paste the contents of `SKILL.md` into a Project.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool can't install skills, paste the contents of `SKILL.md` at the start of a chat. This works less well, because the AI only has the instructions in that one chat, and the weekly email won't work.

## Checking it works

Ask your agent: "Find VH resources that would help me write a grant proposal."

A good result names two to five resources from resources.veganhacktivists.org. Each has a working link and a sentence on how it helps with a grant proposal, and the library's grant proposal prompt is one of them. If the agent says it can't open web pages, check its web search or web access setting.

## Optional: a weekly email of resources

Once a week, your agent looks back through your chats, works out what you were working on, and emails you any library resources that would help. Weeks where nothing fits get no email.

It only works if your agent can:

1. **Read your past chats.** Without this, the email has nothing to base its picks on. Some AI tools have a setting for searching or referencing past chats, often with the memory settings.
2. **Run a task on a schedule,** such as a scheduled task in Claude Cowork or ChatGPT Work.
3. **Send you an email,** for example through a Gmail or Outlook connector, or notify you some other way. Some tools can email you themselves when a scheduled task finishes.

You don't need to work this out yourself. After installing the skill, paste this into a chat with your agent. It checks everything before it sets anything up:

```text
Set up the weekly VH resources email from the vh-ai-resources skill. Before you create anything:

1. Check that you can actually read my past chats. Try it: tell me two or three things I worked on in the last week. If you can't, warn me that the weekly email won't really work without that, and don't set it up unless I still want it.
2. Check that I'm happy to receive an email from you, and which address to send it to.
3. Check whether I want it weekly, or more or less often, and on which day and at what time.

Then follow "For AI agents setting up the weekly email" in the skill's setup guide (README.md), including the test run at the end.
```

Before the first email goes out, your agent shows you what it would send. The email only ever goes to you. It names each piece of your work in a few words, so it doesn't copy your chats into your inbox, and it leaves personal topics out completely. You can change or stop it at any time by asking your agent.

## For AI agents installing this skill

1. Read `SKILL.md` and this file. Tell the user in two or three sentences what the skill does.
2. Check that you can reach the library. Try opening https://resources.veganhacktivists.org/llms.txt. If you can't, try a web search for `site:resources.veganhacktivists.org`. If neither works, tell the user the skill needs web access, and how to turn it on in their tool if you know.
3. Install the whole folder in your skills location. Don't change anything outside it without asking.
4. Searching the library needs no setup.
5. Ask the user, in one or two lines, whether they would like the optional weekly email, and say that it works by reading their past chats. If they say yes, follow the next section. Don't create a scheduled task or send anything until its checks are done.
6. Offer to run the request under "Checking it works".

## For AI agents setting up the weekly email

The weekly email is a scheduled task, not part of the skill. The task reads the user's past chats, uses the skill to find resources, and sends the email. You write its instructions in step 5.

Work through these steps in order. If one fails, stop and tell the user why before going further. If the user's message already answered one of the questions, don't ask it again.

1. **Check that you can read the user's past chats.** The whole email depends on this, so don't assume it from your list of tools. Actually try it. Look for the user's chats from the last seven days, and name two or three pieces of work from them so the user can see it works. Read only what you need: the user's own messages are usually enough. Leave personal matters out (health, family, money, relationships, anything that isn't work). Where to look depends on the agent:
   - Some apps have a setting for searching or referencing past chats, often with the memory settings. If it is switched off, tell the user where to turn it on, then try again.
   - Coding agents usually save each session as a file on the user's computer. For example, Claude Code keeps them under `~/.claude/projects/`, and Codex under `~/.codex/sessions/`.

   If you can't read past chats, warn the user plainly. For example: "I can't read your past chats, so a weekly email would have nothing to base its picks on. I don't recommend setting it up." Suggest these instead: ask you for VH resources whenever they start something new, or follow new resources through the library's RSS feed at https://resources.veganhacktivists.org/feed.xml. Only carry on if they still want the email after that warning.

2. **Check that they are happy to get an email.** Tell them what it will contain: an email listing up to five resources, each with a few words saying which piece of their work it fits, and no quotes from their chats. Ask whether they are happy to receive that, and which address to send it to. Only use an address they give you or confirm. If they don't want an email, offer whatever notification your agent can send instead (see step 4), or stop.

3. **Check how often they want it.** Ask whether weekly suits them, or whether they would rather have it more or less often, such as every two weeks or once a month. Ask which day and time, and check their time zone. If they have no preference, suggest Monday morning.

4. **Check that you can run it on a schedule and send it.**
   - You need to be able to create a scheduled task. If you can't, tell the user the weekly email can't run on this agent, and suggest asking you each week instead.
   - Check where scheduled tasks run. A task that runs in the cloud can't read chats saved as files on the user's computer. A task that runs on the user's computer only runs while it is switched on. Tell the user which applies.
   - You need to be able to send the user an email, for example through an email connector. If you can only save drafts, or can't send email at all, say so. Some agents can notify the user themselves when a scheduled task finishes, by push notification or by email. Offer that if it is available.

5. **Create the scheduled task** at the time they chose, with these instructions. Fill in everything in angle brackets, and keep the rest as it is. The task's instructions hold everything about reading chats and sending the email. Don't add any of it to the skill.

   ```text
   Email me resources from the Vegan Hacktivists AI Resource Library that fit what I worked on recently.

   1. Read my chats from the last <7, 14 or 30> days. Read only what you need to tell what I was working on: my own messages are usually enough, so skip tool output and pasted documents. If there are many chats, skim the first few messages of each. Skip scheduled and automated runs, including earlier runs of this task. Leave personal matters out completely: health, family, money, relationships and anything else that isn't work.
   2. If you can't read any of my chats, don't send general resources. Send me two lines saying this run couldn't read my past chats, and stop.
   3. List the pieces of work I was doing, a few words each. Leave out one-off quick questions.
   4. Use the vh-ai-resources skill to find resources for those pieces of work. Keep up to five in total, and only ones that would help with that work. If you can see this task's earlier runs, don't repeat a resource unless I'm still working on the same thing. Don't search my mailbox for this.
   5. If nothing fits, send nothing, and say so in this run's output.
   6. Write the email. Subject: "VH resources for your <week, fortnight or month>" plus one to three topics in general words, for example "VH resources for your week: grant reports and AI policy". Body: one short entry per resource, the title as a link, then one sentence on how it helps, naming the piece of work in a few words ("for the grant report you were drafting"). In the subject and the body: no quotes from my chats, no names of people, donors or partner organisations, and nothing confidential. End with one line saying I can change or stop these emails by asking my AI, and a link to https://resources.veganhacktivists.org.
   7. Send it to <the address the user gave or confirmed> by <email through which connector, or the scheduler's own notification>, and to nobody else.
   8. End this run's output with the titles you sent and any close matches you left out.
   ```

   Don't put these settings in your copy of the skill. Updates replace it, and some apps don't let you edit installed skills.

6. **Test it.** First show the user, in this chat, the email you would send this week, and ask whether it looks right. Then run the scheduled task once straight away, the same way the schedule will run it, and check with the user that the email arrived. This matters because some agents can read past chats in a normal chat but not in a scheduled run. If the test run couldn't read past chats, give the user the same warning as in step 1.

When it is set up, tell the user that weeks where nothing in the library fits get no email, and that they can change or stop it at any time by asking you.
