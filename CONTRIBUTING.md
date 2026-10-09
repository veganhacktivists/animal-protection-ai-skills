# Contributing a skill

Thank you. This page covers everything a submission needs, step by step, and how we review it.

Most people will not do this by hand. They will ask their AI agent something like "Submit my catch-up skill to the Animal Protection Skills repo", often for a skill the agent already has installed. The steps under [Submitting a skill](#submitting-a-skill) are written so an agent can follow them from start to finish. If you are doing it yourself, follow the same steps.

If you would rather not use GitHub, email your skill to hello@veganhacktivists.org with "Skill submission" in the subject and we will handle the rest. Step 12 covers what to send.

## What we accept

- Skills only. Not connectors, apps, datasets or general documents. Those belong in the [AI Resource Library](https://github.com/veganhacktivists/ai-resource-library).
- Skills that are useful to people doing animal protection work. General-purpose skills are fine if that audience would use them regularly.
- Skills that work on at least one of: Claude, Codex, Gemini CLI, GitHub Copilot, Microsoft 365 Copilot.
- Skills you have the right to share under the MIT licence.

## What goes in a skill folder

```
skills/
  your-skill-name/
    SKILL.md            required, the instructions the agent follows
    README.md           required, the setup guide for people and their agents
    scripts/            optional, executable code
    references/         optional, extra documentation the agent reads on demand
    assets/             optional, templates and static files
```

The folder name must match the `name` field in `SKILL.md` exactly.

`SKILL.md` is what the agent reads when it uses the skill. `README.md` is the skill's setup guide: what the skill needs, how to install it and how to check it works. GitHub shows it to anyone who opens the skill's folder, so a person or an agent given a link to the folder sees it first. There is a template under [The setup guide](#the-setup-guide-readmemd).

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

A setup skill is not the same thing as a skill's setup guide. Every installable skill has a setup guide (its `README.md`). A setup skill is a different kind of submission, which you send instead of an installable skill.

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
- A `## Requirements` section if the skill needs anything beyond the agent itself. Describe the capability, then how to get it on each platform. For example: "Needs read access to the user's Gmail. In Claude, connect the Gmail connector. In Codex, install a Gmail MCP server. Alternatively install the `gws` command line tool." If the skill needs nothing, say "None. Works with the agent alone."

Keep `SKILL.md` under 500 lines. Move long reference material into `references/`.

Keep it portable:

- Do not name one agent's internal tools (for example `mcp__something__search`). Describe the capability instead: "if your agent can search past conversations, do so; otherwise ask the user to paste the relevant part".
- Do not hard-code file paths from your own machine, your own name, your colleagues' names, or internal board and channel names.
- Do not include API keys, tokens, email addresses or phone numbers.

## The setup guide (README.md)

Every skill folder needs a `README.md` written for the person installing the skill, with a last section for their AI agent. Copy this template. Fill in the parts in angle brackets and keep the install steps as they are, so every skill's guide gives the same instructions.

````markdown
# Setting up <skill-name>

<One or two sentences on what the skill does, in plain words.>

## What you need first

<Everything the skill needs beyond the AI agent: connectors, accounts, command line tools, files. For each one, say how to get it on each platform. If it needs nothing, write "Nothing. It works with the AI agent alone.">

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install <skill-name>@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `<skill-name>` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/<skill-name>`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills <skill-name>`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well: the AI only has the instructions in that one chat or project, and any scripts in this folder will not run.

## Checking it works

Ask your agent: "<a realistic request that runs the skill's main job>"

A good result <what the user should see>.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking.
5. Offer to run the request under "Checking it works".
````

## Submitting a skill

These steps are written so an AI agent can follow them for its user. "You" means whoever is doing the submission, the person or their agent. Where a step says to ask the user, an agent must stop and wait for the answer.

### 1. Find the skill and check whose it is

Find the whole skill folder: `SKILL.md` and everything next to it. A skill the agent has installed is usually in its skills location, for example `~/.claude/skills/<name>/` or a project's `.claude/skills/` in Claude Code, or `~/.agents/skills/` or `~/.codex/skills/` in Codex. If the folder is a link to somewhere else, follow the link. If the skill was uploaded to a website such as claude.ai and you cannot read its files, ask the user to download the skill or paste its files in.

Check that the user wrote the skill, or has the author's permission to share it. A skill installed from somewhere else (a colleague, a team repository, a plugin) belongs to whoever wrote it.

### 2. Check it belongs here

- It is a skill and fits [What we accept](#what-we-accept).
- Read [INDEX.md](INDEX.md). If an existing skill already does the same job, suggest improving that one instead (see [Updating an existing skill](#updating-an-existing-skill)).
- It can work for anyone. If it only works wired to the user's own accounts, channels and tools, submit a [setup skill](#setup-skills-a-different-shape) instead and adapt the rest of these steps to that shape.

### 3. Make a copy to work on

Copy the whole folder somewhere new and make every change to the copy. Never edit or remove the user's installed skill. They keep using their own version.

### 4. Find everything personal or private

Read every file in the copy, including scripts, references, assets and examples. List everything that would not make sense, or should not be seen, outside the user's own setup:

- Names of people: the user, colleagues, clients, donors, anyone in an example.
- Names of the user's organisation's private things: clients and partners, internal boards, channels, folders, drives and project names, prices and rates.
- Email addresses, phone numbers, and links to private documents, calendars or recordings.
- File paths from the user's computer, account IDs and document IDs.
- Passwords, API keys and tokens.
- Tool names that only one agent has, such as `mcp__gmail__search`, and frontmatter fields that only one agent understands, such as `disable-model-invocation`.
- Mentions of other skills or files that will not be published with this one.
- Rules that only make sense for the user, such as how they sign off or which tags they use.

### 5. Make it work for anyone

Rewrite each item on the list so the skill works for any user:

- Replace a specific name with a general description, for example "the user's clients" rather than a list of client names.
- Where the skill needs a fact only its user knows, have the skill ask, for example "If you are not sure which organisations count as clients, ask the user once."
- Replace a tool name with the capability: "If your agent can search the user's email, do so. Otherwise, ask the user to paste the message."
- If the skill depends on another unpublished skill or file, copy in what it needs (into `references/` if it is long), or drop the dependency.

Keep the skill's behaviour and rules the same. Do not add features, and do not drop a rule because it is awkward to make general. If the skill cannot be made general without losing what makes it useful, it should be a setup skill (see step 2).

### 6. Show the user and get their go-ahead

Show the user every change you made in steps 4 and 5 as a numbered list, then the new `SKILL.md` in full. Then ask them three things:

- What name and organisation should be credited? Everything in this repo is public, including the author's name.
- Do they confirm they wrote the skill, or have the author's permission, and are happy to share it under the MIT licence?
- Is anything private left in it?

Do not go further until they say yes. If they want changes, make them and show them again. If you change the skill again later, for example after testing, show them those changes too.

### 7. Name the skill and fill in the frontmatter

Choose the name using the rules under [SKILL.md frontmatter](#skillmd-frontmatter), check that no folder in `skills/` already has it, and rename the copy's folder to match. Fill in the frontmatter with `version` at `1.0.0`. Make sure the body has a `## Requirements` section (see [SKILL.md body](#skillmd-body)).

### 8. Write the setup guide

Add `README.md` to the folder, using the template under [The setup guide](#the-setup-guide-readmemd). "What you need first" should match the `## Requirements` section. For "Checking it works", pick a request that runs the skill's main job. You test it in the next step.

### 9. Test it end to end

Run the new version on at least one agent, in a fresh conversation, with two or three realistic requests, including the one in the setup guide. If installing it would clash with the user's own copy of the same skill, test it without installing: in a fresh conversation, tell the agent to read and follow the new `SKILL.md`. If you cannot start a fresh conversation yourself, ask the user to run the requests and tell you what happened.

Fix anything that breaks. Then set `last-verified` to the date of the test and `verified-on` to the agent or agents you used. Keep the requests and what a good result looked like, because the pull request asks for them.

### 10. Run the checks

From the repo root:

```
python3 tools/validate_skills.py
python3 tools/build_index.py
```

The first checks the frontmatter and the repo rules. It needs PyYAML (`pip install pyyaml`). The second regenerates `INDEX.md` and `index.json`. Never edit those two files by hand. If you cannot run Python, say so in the pull request: the same checks run automatically when it is opened.

The checker does not catch everything. It finds agent-only tool names, file paths from someone's computer and things that look like API keys. It does not find people's names, organisation names or links to private documents. Step 4 is the only check for those.

### 11. Add the skill to the plugin list

`.claude-plugin/marketplace.json` is what lets Claude Code users install one skill with `/plugin install`. Nothing generates it, so edit it by hand. Add an entry for the new skill just above the `all-skills` entry, in the same layout as the others:

```json
    {
      "name": "your-skill-name",
      "description": "One line on what the skill does, with no full stop at the end",
      "source": "./",
      "strict": false,
      "skills": ["./skills/your-skill-name"]
    },
```

Then add `"./skills/your-skill-name"` to the end of the `skills` list in the `all-skills` entry. Setup skills never go in this file.

### 12. Open the pull request, or email the skill

Ask the user before you open the pull request or send the email. Both make the skill visible to other people.

With GitHub:

1. If you do not have write access to this repo (most people don't), fork it. With the GitHub command line tool: `gh repo fork veganhacktivists/animal-protection-ai-skills --clone`.
2. Make a branch called `add-your-skill-name`.
3. Commit only the new skill folder, `INDEX.md`, `index.json` and `.claude-plugin/marketplace.json`.
4. Push the branch and open a pull request against `main` in `veganhacktivists/animal-protection-ai-skills`.
5. Fill in every section of the pull request template, including the test requests from step 9. If an AI agent prepared the submission, say which one, and whether the user has read the final version.

Without GitHub: zip the skill folder and email it to hello@veganhacktivists.org with "Skill submission" in the subject. In the email, give what the pull request template asks for: what the skill does, two or three example requests with what a good result looks like, where it was tested and what it needs. An agent should draft the email and let the user send it.

### 13. After you submit

A member of the Vegan Hacktivists AI Services team reads every line, using the [review checklist](#review-checklist). They may comment or suggest edits. Answer every comment and push any fixes to the same branch. Do not merge the pull request yourself. We merge it once a reviewer has approved it.

### What an AI agent must never do while submitting

- Open a pull request, send an email or post anything without the user's go-ahead for that action.
- Publish anything the user has not seen.
- Edit or remove the user's own installed copy of the skill.
- Approve or merge a pull request.
- Copy secrets, private documents or other people's personal details into the repo, even to test with.

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
- [ ] Nothing is specific to the author's own machine, organisation, clients or colleagues. The checker cannot find names, so read for them.
- [ ] Plain language. No jargon a working advocate would have to look up.

Housekeeping:

- [ ] Folder name matches `name`, and `name` does not start with `vh-` unless the skill is about Vegan Hacktivists.
- [ ] All required metadata fields present, `version` is `1.0.0` for a new skill.
- [ ] `README.md` setup guide present and follows the template. Its "Checking it works" request works.
- [ ] The skill has its own entry in `.claude-plugin/marketplace.json` and is in the `all-skills` list.
- [ ] `tools/validate_skills.py` passes.
- [ ] `INDEX.md` and `index.json` regenerated and committed.
- [ ] Licence is MIT.

## After a pull request is merged

This part is for the Vegan Hacktivists team. Publish a new release so the skill's zip exists for people using claude.ai, Cowork and Microsoft 365 Copilot. Until a release is published, those downloads do not include the new or updated skill.

On the Releases page, draft a new release with the next tag and publish it. Raise the middle number when skills are added (as `v1.1.0` did) and the last number when existing skills are only updated. The release workflow attaches one zip per skill.

## Updating an existing skill

Open a pull request against the skill folder. Bump `version` and update `last-verified`. Say in the pull request what changed and why. The original author stays in `metadata.author`; add yourself to a `## Contributors` section at the bottom of the body if you want credit for the change.

Update the setup guide too if what the skill needs, or how to check it works, has changed. If what the skill does has changed, update its description in `.claude-plugin/marketplace.json`. An agent updating a skill follows steps 4, 6, 9, 10 and 12 to 13 of [Submitting a skill](#submitting-a-skill).

## Reporting a problem with a skill

Open an issue, or email hello@veganhacktivists.org. If you think a skill is doing something it should not, say so in the subject line and we will look the same day.
