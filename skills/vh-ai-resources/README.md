# Setting up vh-ai-resources

This skill lets your AI agent search the free [Vegan Hacktivists AI Resource Library](https://resources.veganhacktivists.org) for you. Ask it something like "Does VH have anything on writing an AI policy?" It reads the library, opens the best matches, and tells you which few will help with what you're doing, and why. The library has how-tos, prompts, case studies, guides, trainings, tool overviews and FAQs for people doing animal protection work.

It can also send you a weekly email of resources that fit what you worked on that week. That part is optional and needs more from your AI agent. See "Optional: a weekly email of resources" below.

## What you need first

- **An AI agent that can open web pages or search the web.** Most can. If yours has a web search or web access setting, make sure it is on.
- Nothing else. Searching the library needs no account, key or connector.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install vh-ai-resources@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and the Claude app:** download the `vh-ai-resources` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool can't install skills, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well, because the AI only has the instructions in that one chat or project, and the weekly email won't work.

## Checking it works

Ask your agent: "Find VH resources that would help me write a grant proposal."

A good result names two to five resources from resources.veganhacktivists.org. Each has a working link and a sentence on how it helps with a grant proposal, and the library's grant proposal prompt is one of them. If the agent says it can't open web pages, check its web search or web access setting.

## Optional: a weekly email of resources

Once a week, your agent looks back through your chats, works out what you were working on, and emails you any library resources that would help. Weeks where nothing fits get no email.

It only works if your agent can do three things:

1. **Read your past chats.** Without this, the email has nothing to base its picks on. Some AI tools have a setting for searching or referencing past chats, often with the memory settings. Coding agents such as Claude Code and Codex save past sessions as files on your computer, which they can read. Some tools can read past chats in a normal chat but not in a scheduled task.
2. **Run a task on a schedule,** such as a scheduled task in Claude Cowork or ChatGPT. If the task runs in the cloud, it can't read chats saved on your computer. If it runs on your computer, it only runs while your computer is on.
3. **Send you an email,** for example through a Gmail or Outlook connector, or notify you some other way. Some tools can email you themselves when a scheduled task finishes.

You don't need to work this out yourself. After installing the skill, paste this into a chat with your agent. It checks everything before it sets anything up:

```text
Set up the weekly VH resources email from the vh-ai-resources skill. Before you create anything:

1. Check that you can actually read my past chats. Try it: tell me two or three things I worked on in the last week. If you can't, warn me that the weekly email won't really work without that, and don't set it up unless I still want it.
2. Check that I'm happy to receive an email from you, and which address to send it to.
3. Check whether I want it weekly, or more or less often, and on which day and at what time.

Then follow "Setting it up" under "The weekly email" in the skill, including the test run at the end.
```

Before the first email goes out, your agent shows you what it would send. The email only ever goes to you. It names each piece of your work in a few words, so it doesn't copy your chats into your inbox, and it leaves personal topics out completely. You can change or stop it at any time by asking your agent.

## For AI agents installing this skill

1. Read `SKILL.md` and this file. Tell the user in two or three sentences what the skill does.
2. Check that you can reach the library. Try opening https://resources.veganhacktivists.org/llms.txt. If you can't, try a web search for `site:resources.veganhacktivists.org`. If neither works, tell the user the skill needs web access, and how to turn it on in their tool if you know.
3. Install the whole folder in your skills location. Don't change anything outside it without asking.
4. Searching the library needs no setup.
5. Ask the user, in one or two lines, whether they would like the optional weekly email, and say that it works by reading their past chats. If they say yes, follow "Setting it up" in `SKILL.md`. It starts by checking that you can read their past chats, then checks that they are happy to get an email and how often they want it. Don't create a scheduled task or send anything until those checks are done.
6. Offer to run the request under "Checking it works".
