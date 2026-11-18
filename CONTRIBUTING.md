# Contributing a skill or automation

Thank you. This page covers what a submission needs to contain and how we review it. If you would rather email your skill or automation than open a pull request, send it to hello@veganhacktivists.org with "Skill submission" in the subject and we will handle the rest.

## What we accept

- Skills and automations only. Not connectors, apps, datasets or general documents. Those belong in the [AI Resource Library](https://github.com/veganhacktivists/ai-resource-library). See "Automations" below for what counts as one.
- Skills that are useful to people doing animal protection work. General-purpose skills are fine if that audience would use them regularly.
- Skills that work on at least one of: Claude Code, Claude Cowork, OpenAI Codex, ChatGPT Work, Gemini CLI, GitHub Copilot, Microsoft 365 Copilot.
- Skills you have the right to share under the MIT licence.

## Folder layout

```
skills/
  your-skill-name/
    SKILL.md            required
    README.md           the setup guide, see "README.md: the setup guide" below
    scripts/            optional, executable code
    references/         optional, extra documentation the agent reads on demand
    assets/             optional, templates and static files
```

The folder name must match the `name` field in `SKILL.md` exactly.

## Setup skills: a different shape

Some capabilities only work wired to one person's own accounts, channels, and tools. Sharing a copy of someone else's version produces noise, or copies their setup assumptions along with it. For those, submit a **setup skill** instead: a single markdown file written for an AI agent, telling it how to interview its own user and build them a bespoke version. The reusable part is the process and the judgement calls, not a copy-pasteable file.

```
setup-skills/
  skill-setup-your-topic.md
```

- Name it `skill-setup-<topic>.md`. No `SKILL.md`, no folder: it is one flat file.
- Frontmatter uses `title`, `description`, `license`, and the same `metadata` block as a normal skill (`version`, `author`, `author-org`, `last-verified`, `verified-on`). No `name` or `compatibility` field.
- The body should tell the reading agent, explicitly, not to run the steps itself but to build a personalised version for its user. Say what is being built and why it is not a shared skill, what the agent should discover before asking anything, the questions to ask, the core logic to build in, and what is a safety constraint rather than a preference. Keep specific tools out of the logic itself, describing "their task system" rather than naming one product.
- It never gets installed or zipped, and does not appear in `.claude-plugin/marketplace.json`. It is read on request, not auto-triggered.

The same review checklist below applies, and `tools/validate_skills.py` checks these too.

## Automations

An automation is a job someone's AI does on a schedule, such as a weekly review of their work or a daily summary of their inbox. It isn't shared as a skill to install, because each person has to wire it to their own tools. It is shared as a setup prompt: a prompt the person pastes into their AI tool, which then sets the automation up with them.

```
automations/
  your-automation-name/
    README.md           required: frontmatter and the guide for the person
    setup-prompt.md     required: the prompt they paste into their AI
```

The folder name uses lowercase letters, numbers and single hyphens.

### README.md

Start it with this frontmatter. The fields follow the same rules as a skill's (see "SKILL.md frontmatter" below), except that it has a `title` in place of `name`.

```yaml
---
title: Your automation's name
description: What it does, what the person gets and how often, and who it suits. Max 1024 characters.
license: MIT
metadata:
  version: "1.0.0"
  author: Your Name
  author-org: Your Organisation
  last-verified: "2026-09-07"
  verified-on: "Claude Code"
---
```

Then write it for the person setting it up:

1. What it does, in two or three sentences.
2. **Who it's for.** Say plainly who it won't work for.
3. **What it does each run**, in a short numbered list.
4. **What you need first.** The kind of AI tool it needs, such as one that can run on a schedule, and any connectors.
5. **Setting it up.** Copy `setup-prompt.md` into a new chat, or give your agent the link to the folder.
6. **Checking it works.** What they should have at the end of setup, and what to do if the first real run doesn't arrive.
7. **Privacy**, if it reads anything sensitive. Say what it reads, who sees the results, and what it never does.
8. **For AI agents setting up this automation.** Numbered steps for the person's agent: download `setup-prompt.md` exactly, read it in full, then follow it with the person. The validator checks this section is there.

See [`automations/weekly-work-coach/README.md`](automations/weekly-work-coach/README.md) for an example.

### setup-prompt.md

The person pastes the whole file into their AI, so it has no frontmatter. Write it in the first person, as the person talking to their own AI. A good setup prompt:

- Says in its first paragraph what the automation does and how often.
- Asks the AI to say first what it can do in that app: run on a schedule, read what the automation needs, run code, send a message. If it can't do something, the AI says so and suggests the closest thing that works.
- Lists each job the automation needs done, what you used for it, and what other people commonly use, so the AI asks which tool the person uses rather than assuming yours.
- Says what to do when a tool can't be reached: the official connector first, then another connector, then a workaround that says what it loses.
- Spells out exactly what each run does, and the rules, with the reason for each rule.
- Keeps the run as safe as the job allows. Scheduled runs only read, apart from delivering the result to the person. The result only goes to the person, unless sending it to others is the point of the automation.
- Ends with a trial run on the person's real data before anything is scheduled, then tells them when it next runs, what it needs to keep working, and how to pause or delete it.

The same portability rules as skills apply: no tool names from one agent, no machine file paths, no keys. Naming the tools you used as examples is fine.

## SKILL.md frontmatter

Copy this and fill it in. Every field shown is required in this repo except `compatibility`.

```yaml
---
name: your-skill-name
description: What the skill does and when the agent should use it. Include the phrases a user might say. Max 1024 characters.
license: MIT
compatibility: Only if the skill needs something specific, e.g. "Requires Python 3.11+ and access to the internet". Leave out otherwise.
metadata:
  version: "1.0.0"
  author: Your Name
  author-org: Your Organisation
  last-verified: "2026-09-07"
  verified-on: "Claude Code"
---
```

Rules for the fields:

- `name`: lowercase letters, numbers and single hyphens only. Max 64 characters. Do not start with `vh-` unless the skill is specifically about Vegan Hacktivists.
- `description`: this is the only thing the agent sees before deciding whether to load the skill, so it carries the triggering. Say what it does, then when to use it, with example phrases. Say when not to use it if there is an obvious confusion.
- `metadata.version`: start at `1.0.0`. Bump the last number for wording fixes, the middle for new behaviour, the first for changes that break how people already use it.
- `metadata.author` and `metadata.author-org`: this is how you get credit. Use whatever name you want shown publicly.
- `metadata.last-verified`: the date you last ran the skill end to end and it did what it should. Format `YYYY-MM-DD`.
- `metadata.verified-on`: the agent or agents you tested it on, comma separated.

Only use frontmatter fields from the [Agent Skills specification](https://agentskills.io/specification): `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Agent-specific fields (for example Claude Code's `disable-model-invocation`) break the skill on other agents, so leave them out.

## SKILL.md body

Write for the agent, not for a human reader. Plain, direct instructions. A good skill usually has:

- A short statement of the job and the standard it is held to.
- Step by step instructions.
- What to leave out or never do.
- An example of good and bad output where that helps.
- A `## Requirements` section if the skill needs anything beyond the agent itself. Describe the capability only, for example "Needs read access to the user's Gmail." How to get it on each agent is setup, so it goes in the README. If the skill needs nothing, say "None. Works with the agent alone."

Leave setup out of `SKILL.md`. The agent reads `SKILL.md` every time it runs the skill, so setup steps there are wasted reading once the skill is set up. They go in the README. A one-line pointer is fine, such as "If the user asks to set this up, follow `README.md` in this folder." If a run needs settings from its user, such as which folder to save to, `SKILL.md` can list them as values. The steps for filling them in still go in the README.

Keep `SKILL.md` under 500 lines. Move long reference material into `references/`.

Keep it portable:

- Do not name one agent's internal tools (for example `mcp__something__search`). Describe the capability instead: "if your agent can search past conversations, do so; otherwise ask the user to paste the relevant part".
- Do not hard-code file paths from your own machine, your own name, your colleagues' names, or internal board and channel names.
- Do not include API keys, tokens, email addresses or phone numbers.

## README.md: the setup guide

Everything about setting the skill up goes in a `README.md` next to `SKILL.md`. GitHub shows it on the skill's folder page, so a person or an agent who opens the folder link sees it first. Write it for the person installing the skill, with sections for their AI agent at the end:

1. What the skill does, in two or three sentences.
2. **What you need first.** What the skill needs, and how to get it on each agent, for example "In Claude Cowork, connect Google Drive."
3. **Installing it.** Copy the block below and put in your skill's name.
4. **Checking it works.** One request to try, and what a good result looks like.
5. **For AI agents installing this skill.** Numbered steps for the person's agent: read the skill, check what it needs, install the whole folder, and offer to run the request under "Checking it works". In the install step, link to https://raw.githubusercontent.com/veganhacktivists/animal-protection-ai-skills/main/FOR-AI-AGENTS.md for how to download the folder and where skills go. Don't repeat those steps in your README.
6. **For AI agents setting up ...** Only if the skill needs settings from its user, or has an optional extra such as a scheduled run. Say what the agent should find out for itself, what to ask, where the answers go and how to test it.

The install block:

```markdown
## Installing it

- **Claude Code and OpenAI Codex:** give your agent the link to this folder, https://github.com/veganhacktivists/animal-protection-ai-skills/tree/main/skills/<skill-name>, and ask it to install the skill. It downloads the folder and does the rest.
- **Claude Cowork:** download the `<skill-name>` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **ChatGPT Work:** make a skill through ChatGPT's own skill-creation flow, giving it the link to this folder or the contents of `SKILL.md`. Or paste the contents of `SKILL.md` into a Project.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool can't install skills, paste the contents of `SKILL.md` at the start of a chat. This works less well, because the AI only has the instructions in that one chat.
```

Three rules for install steps:

- For Claude Code and Codex, don't give `/plugin` commands or folder paths to copy the skill into. The agent knows where its own skills go.
- Always include ChatGPT Work.
- Name Claude Cowork. Don't write "the Claude app", "claude.ai" or "Claude chat", because Claude's chat and Cowork have merged.

See [`skills/meeting-wisdom-bank/README.md`](skills/meeting-wisdom-bank/README.md) for a setup guide with a "For AI agents setting up ..." section.

## Before you open the pull request

1. Run the checks locally:
   ```
   python3 tools/validate_skills.py
   python3 tools/build_index.py
   ```
   The first one checks your frontmatter. The second regenerates `INDEX.md` and `index.json`. Commit the regenerated index files with your skill.
2. Run the skill end to end on at least one agent and set `last-verified` to today.
3. Fill in the pull request template. It asks for two or three example prompts and what a good result looks like. Reviewers use these to test.

## Review checklist

This is what a reviewer does with every submission. Nothing is merged until every box is ticked by a Vegan Hacktivists AI Services team member.

Safety:

- [ ] Read every line of `SKILL.md` and every file in the folder. No exceptions for long files.
- [ ] No instructions are fetched from a URL at run time. Links to documentation for the human are fine. Instructions the agent is told to download and follow are not.
- [ ] No hidden, encoded, zero-width, white-on-white or otherwise obscured text.
- [ ] No script we have not read in full. Scripts are checked for network calls, file deletion and anything touching credentials.
- [ ] Nothing asks for, stores or transmits passwords, API keys or tokens.
- [ ] Nothing sends the user's data anywhere the user did not ask for.
- [ ] Nothing tells the agent to ignore its own safety rules, the user's instructions or this checklist.

Quality:

- [ ] The `description` accurately says what the skill does. It does not claim more than the body delivers.
- [ ] The skill does one job and does it well. It is not three skills in one folder.
- [ ] The example prompts in the pull request work. A reviewer has run at least one.
- [ ] Nothing is specific to the author's own machine, organisation or colleagues.
- [ ] Plain language. No jargon a working advocate would have to look up.
- [ ] Setup steps are in `README.md`, not `SKILL.md`. The install steps follow the block in "README.md: the setup guide".

Automations, as well as the checks above:

- [ ] Read `setup-prompt.md` as the person's AI would. It asks before setting anything up and does a trial run before it schedules anything.
- [ ] Scheduled runs only read, apart from delivering the result, and the result only goes to the person unless sharing it is the point.
- [ ] It works for people whose tools differ from the author's. It asks which tool they use for each job.

Housekeeping:

- [ ] Folder name matches `name`.
- [ ] All required metadata fields present, `version` is `1.0.0` for a new skill.
- [ ] `tools/validate_skills.py` passes.
- [ ] `INDEX.md` and `index.json` regenerated and committed.
- [ ] Licence is MIT.

## Updating an existing skill

Open a pull request against the skill folder. Bump `version` and update `last-verified`. Say in the pull request what changed and why. If what the skill needs, or how to set it up, has changed, update its README too. The original author stays in `metadata.author`; add yourself to a `## Contributors` section at the bottom of the body if you want credit for the change.

## Reporting a problem with a skill

Open an issue, or email hello@veganhacktivists.org. If you think a skill is doing something it should not, say so in the subject line and we will look the same day.
