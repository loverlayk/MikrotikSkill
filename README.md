# MikroTik RouterOS Official — Hermes Skill

An unofficial Hermes Agent skill built around the official machine-readable
MikroTik RouterOS Manual.

## Features

- Real Hermes `SKILL.md`
- Progressive-disclosure reference corpus
- Incremental synchronization using SHA-256 page hashes
- Detects new and changed pages
- Removes pages no longer listed by MikroTik
- Generates a sync manifest
- GitHub Actions automation
- Optional automatic GitHub Releases when the official manual changes

## Install

Clone the repository and place the skill under:

```text
~/.hermes/skills/mikrotik-routeros-official/
```

Then:

```bash
cd ~/.hermes/skills/mikrotik-routeros-official
python3 -m pip install requests
python3 scripts/sync_mikrotik_manual.py
```

## Automatic updates

GitHub Actions runs the synchronization on a schedule. If the official
MikroTik Manual changes, the workflow commits the changed references and
creates a GitHub Release.

You can also run it manually from:

`Actions → Sync MikroTik Manual → Run workflow`

The workflow supports:

- normal incremental sync
- clean rebuild
- test/limited sync

## Source

Official MikroTik documentation:

https://manual.mikrotik.com/docs/introduction/

Machine-readable index:

https://manual.mikrotik.com/llms.txt

Full corpus:

https://manual.mikrotik.com/llms-full.txt

## Attribution

MikroTik and RouterOS are trademarks of MikroTik. MikroTik documentation
remains the property of MikroTik. This repository is an unofficial community
project and does not claim ownership of the documentation.

The MIT license applies to the original code and Skill scaffolding in this
repository, not to third-party MikroTik documentation.

## Third-party skills

This official documentation skill is intentionally separate from projects
such as `tikoci/routeros-skills`.
