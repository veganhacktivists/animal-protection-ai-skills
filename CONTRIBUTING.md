# Contributing a skill

Thank you. This page covers what a submission needs to contain and how we review it. If you would rather email your skill than open a pull request, send it to hello@veganhacktivists.org with "Skill submission" in the subject and we will handle the rest.

## What we accept

- Skills only. Not connectors, apps, datasets or general documents. Those belong in the [AI Resource Library](https://github.com/veganhacktivists/ai-resource-library).
- Skills that are useful to people doing animal protection work. General-purpose skills are fine if that audience would use them regularly.
- Skills that work on at least one of: Claude, Codex, Gemini CLI, GitHub Copilot, Microsoft 365 Copilot.
- Skills you have the right to share under the MIT licence.

## Folder layout

```
skills/
  your-skill-name/
    SKILL.md            required
    scripts/            optional, executable code
    references/         optional, extra documentation the agent reads on demand
    assets/             optional, templates and static files
```

The folder name must match the `name` field in `SKILL.md` exactly.

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

Housekeeping:

- [ ] Folder name matches `name`.
- [ ] All required metadata fields present, `version` is `1.0.0` for a new skill.
- [ ] `tools/validate_skills.py` passes.
- [ ] `INDEX.md` and `index.json` regenerated and committed.
- [ ] Licence is MIT.

## Updating an existing skill

Open a pull request against the skill folder. Bump `version` and update `last-verified`. Say in the pull request what changed and why. The original author stays in `metadata.author`; add yourself to a `## Contributors` section at the bottom of the body if you want credit for the change.

## Reporting a problem with a skill

Open an issue, or email hello@veganhacktivists.org. If you think a skill is doing something it should not, say so in the subject line and we will look the same day.
