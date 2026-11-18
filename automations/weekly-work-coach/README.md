---
title: Weekly work coach
description: "Once a week, your AI reads everything you asked it that week, works out what your week was really about, and challenges you with five questions: what is the bigger question behind your work, how could you be more ambitious, are you asking the right questions, what are you assuming, and are you working towards your key goals or getting bogged down in side projects. You get a review you can read in about five minutes. Only works for people who do most of their work inside an AI app."
license: MIT
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-11-14"
  verified-on: "Claude Code"
---

# Weekly work coach

Most weeks go on the work in front of us, with no time to step back and ask whether it is the right work. This automation does that step for you. Once a week, your AI reads what you asked it that week and sends you a short, blunt review that challenges how you are thinking.

It was built by Richie, the AI Impact Director at Vegan Hacktivists, who runs it on his own work every week.

## Who it's for

It only works if you do most of your work inside an AI app, such as Claude Cowork, Claude Code, OpenAI Codex or ChatGPT Work. The coach can only see what you asked your AI. If most of your work happens somewhere else, it sees a thin slice of your week, and the review will be about that slice.

## What it does each week

1. Collects the messages you typed to your AI tools in the last 7 days. It keeps only your own words and drops the AI's replies.
2. Reads your calendar for the same week, if you let it, so a week of calls doesn't look empty.
3. Reads your key goals, if you keep them somewhere it can reach.
4. Groups the week into the real threads of work you did.
5. Answers five questions about your week, quoting your own words:
   - What is the bigger question here?
   - How can I be more ambitious?
   - I am asking AI questions, but are those questions the right ones?
   - What assumptions am I making that you can challenge?
   - Am I working towards my key goals or getting bogged down in side projects?
6. Sends the review to you, and only you.

## Change the questions to suit you

These are the five questions that help Richie. Your work and your priorities are different, so change them. The setup asks whether you want to keep them or swap some, and builds your questions in instead.

## What you need first

- **An AI tool that can run on a schedule and read your past chats.** Claude Code and OpenAI Codex are the easiest, because they save your chats as files on your computer. The setup checks what your tool can do before anything else, and suggests the closest thing that works if it can't.
- **Somewhere to send the review**, such as an email to yourself or a Slack message to yourself.
- **Optional:** your calendar, and a short note or document with your key goals.

## Setting it up

1. Open [`setup-prompt.md`](setup-prompt.md) and copy the whole file. On GitHub, the copy button is at the top right of the file.
2. Paste it into a new chat in the AI tool you do most of your work in.
3. Answer its questions. It asks about your tools, your goals, what is off limits and whether to change the five questions.

Or give your agent the link to this folder, https://github.com/veganhacktivists/animal-protection-ai-skills/tree/main/automations/weekly-work-coach, and ask it to set up the weekly work coach for you.

Either way, it does a trial run first and shows you the review. It asks before it sets anything up.

## Checking it works

By the end of setup you should have one review marked TRIAL, sent wherever you chose, and your AI should tell you when the first real one will arrive. If that one doesn't arrive, go back to the chat where you set it up and ask what the scheduled run did.

Give it two or three weeks. Then tell your AI what was useful and what wasn't, so it can sharpen the questions.

## Privacy

The review quotes your own messages, so it can contain sensitive work. It only ever goes to you. During setup, it asks which work or folders are off limits and what is too sensitive to quote. Each weekly run only reads and then sends you the review. It never edits your files or messages anyone else.

## For AI agents setting up this automation

1. This is an automation, not a skill. Don't install it into your skills folder.
2. Download `setup-prompt.md` exactly as it is, from https://raw.githubusercontent.com/veganhacktivists/animal-protection-ai-skills/main/automations/weekly-work-coach/setup-prompt.md. Don't work from a summary of the page.
3. Read it in full, then tell your user in two or three sentences what it will set up and what it needs.
4. Follow it step by step with your user, as if they had pasted it to you. Ask before you set anything up, and do the trial run before you schedule anything.
