#!/usr/bin/env python3
"""Check every skills/<name>/SKILL.md and setup-skills/*.md against this repo's rules.

Usage: python3 tools/validate_skills.py
Exit code 0 means everything passed.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
SETUP_SKILLS_DIR = ROOT / "setup-skills"
SKILL_SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SETUP_SKILL_FIELDS = {"title", "description", "license", "metadata"}
REQUIRED_METADATA = {"version", "author", "author-org", "last-verified", "verified-on"}
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


def check_metadata_and_body_hygiene(front: dict, body: str, spec_fields: set) -> list[str]:
    """Checks shared by both SKILL.md and setup-skill files: metadata, license, and portability."""
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

    if re.search(r"mcp__[a-z0-9_-]+__", body):
        problems.append("body names an agent-specific MCP tool (mcp__...__); describe the capability instead")
    if re.search(r"/Users/|C:\\\\Users|/home/[a-z]", body + str(front)):
        problems.append("contains a machine-specific file path")
    if re.search(r"(sk-[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{10,}|AKIA[0-9A-Z]{12,})", body):
        problems.append("contains something that looks like an API key")

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

    return [f"{folder.name}: {p}" for p in problems]


def check_setup_skill(path: Path) -> list[str]:
    if not path.name.startswith("skill-setup-") or not path.name.endswith(".md"):
        return [f"{path.name}: setup-skills/ files must be named skill-setup-<name>.md"]
    try:
        front, body = parse_frontmatter(path)
    except ValueError as exc:
        return [f"{path.name}: {exc}"]

    problems = check_metadata_and_body_hygiene(front, body, SETUP_SKILL_FIELDS)

    title = front.get("title")
    if not isinstance(title, str) or not title.strip():
        problems.append("title is missing or empty")

    desc = front.get("description")
    if not isinstance(desc, str) or not desc.strip():
        problems.append("description is missing or empty")
    elif len(desc) > 1024:
        problems.append(f"description is {len(desc)} chars, max 1024")

    if "not follow these steps yourself" not in body and "not to follow these steps" not in body:
        problems.append(
            "body should tell the reading agent to build a bespoke version, not run the steps itself "
            "(setup skills are instructions for building a skill, not a skill to run directly)"
        )

    return [f"{path.name}: {p}" for p in problems]


def main():
    skill_folders = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))
    setup_files = sorted(SETUP_SKILLS_DIR.glob("*.md")) if SETUP_SKILLS_DIR.exists() else []

    if not skill_folders and not setup_files:
        print("no skills found under skills/ or setup-skills/")
        return 1

    all_problems = []
    for folder in skill_folders:
        problems = check_skill(folder)
        print(f"[{'FAIL' if problems else 'ok'}] skills/{folder.name}")
        all_problems.extend(problems)
    for path in setup_files:
        problems = check_setup_skill(path)
        print(f"[{'FAIL' if problems else 'ok'}] setup-skills/{path.name}")
        all_problems.extend(problems)

    for problem in all_problems:
        print("  -", problem)
    print(f"\n{len(skill_folders)} skills and {len(setup_files)} setup skills checked, {len(all_problems)} problems")
    return 1 if all_problems else 0


if __name__ == "__main__":
    sys.exit(main())
