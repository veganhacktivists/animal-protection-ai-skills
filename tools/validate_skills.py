#!/usr/bin/env python3
"""Check every skills/<name>/SKILL.md and its README.md setup guide against this repo's rules.

Usage: python3 tools/validate_skills.py
Exit code 0 means everything passed.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
SKILL_SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
REQUIRED_METADATA = {"version", "author", "author-org", "last-verified", "verified-on"}
SETUP_GUIDE_SECTIONS = [
    "## What you need first",
    "## Installing it",
    "## Checking it works",
    "## For AI agents installing this skill",
]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("no YAML frontmatter block at the top of the file")
    front = yaml.safe_load(match.group(1)) or {}
    if not isinstance(front, dict):
        raise ValueError("frontmatter is not a mapping")
    return front, match.group(2)


# Kept as an alias: build_index.py imports this name for skills/<name>/SKILL.md files.
parse_skill = parse_frontmatter


def check_portability(text: str) -> list[str]:
    """Problems that stop a file working for anyone but its author. Used for SKILL.md and README.md."""
    problems = []
    if re.search(r"mcp__[a-z0-9_-]+__", text):
        problems.append("names an agent-specific MCP tool (mcp__...__); describe the capability instead")
    if re.search(r"/Users/|C:\\\\Users|/home/[a-z]", text):
        problems.append("contains a machine-specific file path")
    if re.search(r"(sk-[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{10,}|AKIA[0-9A-Z]{12,})", text):
        problems.append("contains something that looks like an API key")
    return problems


def check_metadata_and_body_hygiene(front: dict, body: str, spec_fields: set) -> list[str]:
    """Frontmatter metadata, license, and portability checks for a SKILL.md."""
    problems = []

    unknown = set(front) - spec_fields
    if unknown:
        problems.append(f"non-spec frontmatter fields (break other agents): {sorted(unknown)}")

    if front.get("license") != "MIT":
        problems.append("license must be MIT in this repo")

    meta = front.get("metadata")
    if not isinstance(meta, dict):
        problems.append("metadata block is missing")
    else:
        missing = REQUIRED_METADATA - set(meta)
        if missing:
            problems.append(f"metadata missing required keys: {sorted(missing)}")
        for key, value in meta.items():
            if not isinstance(value, str):
                problems.append(f"metadata.{key} must be a string (quote it), got {type(value).__name__}")
        version = meta.get("version")
        if isinstance(version, str) and not VERSION_RE.match(version):
            problems.append(f"metadata.version {version!r} must look like 1.2.3")
        verified = meta.get("last-verified")
        if isinstance(verified, str) and not DATE_RE.match(verified):
            problems.append(f"metadata.last-verified {verified!r} must be YYYY-MM-DD")

    problems += [f"body {p}" for p in check_portability(body)]
    if re.search(r"/Users/|C:\\\\Users|/home/[a-z]", str(front)):
        problems.append("frontmatter contains a machine-specific file path")

    return problems


def check_skill(folder: Path) -> list[str]:
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return [f"{folder.name}: missing SKILL.md"]
    try:
        front, body = parse_frontmatter(skill_md)
    except ValueError as exc:
        return [f"{folder.name}: {exc}"]

    problems = check_metadata_and_body_hygiene(front, body, SKILL_SPEC_FIELDS)

    name = front.get("name")
    if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
        problems.append(f"name {name!r} must be 1-64 chars, lowercase letters/numbers/single hyphens")
    elif name != folder.name:
        problems.append(f"name {name!r} does not match folder name {folder.name!r}")

    desc = front.get("description")
    if not isinstance(desc, str) or not desc.strip():
        problems.append("description is missing or empty")
    elif len(desc) > 1024:
        problems.append(f"description is {len(desc)} chars, max 1024")

    compat = front.get("compatibility")
    if compat is not None and (not isinstance(compat, str) or not 1 <= len(compat) <= 500):
        problems.append("compatibility must be a string of 1-500 chars if present")

    if body.count("\n") > 500:
        problems.append(f"SKILL.md body is {body.count(chr(10))} lines, keep it under 500")
    if "## Requirements" not in body:
        problems.append("body has no '## Requirements' section")

    readme = folder / "README.md"
    if not readme.exists():
        problems.append("missing README.md setup guide (see 'The setup guide' in CONTRIBUTING.md)")
    else:
        guide = readme.read_text(encoding="utf-8")
        missing_sections = [h for h in SETUP_GUIDE_SECTIONS if h not in guide]
        if missing_sections:
            problems.append(f"README.md setup guide is missing sections: {missing_sections}")
        problems += [f"README.md {p}" for p in check_portability(guide)]

    return [f"{folder.name}: {p}" for p in problems]


def main():
    skill_folders = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))

    if not skill_folders:
        print("no skills found under skills/")
        return 1

    all_problems = []
    for folder in skill_folders:
        problems = check_skill(folder)
        print(f"[{'FAIL' if problems else 'ok'}] skills/{folder.name}")
        all_problems.extend(problems)

    for problem in all_problems:
        print("  -", problem)
    print(f"\n{len(skill_folders)} skills checked, {len(all_problems)} problems")
    return 1 if all_problems else 0


if __name__ == "__main__":
    sys.exit(main())
