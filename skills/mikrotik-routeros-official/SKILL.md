---
name: mikrotik-routeros-official
description: Official MikroTik RouterOS documentation, CLI reference, configuration syntax, and version-specific behavior.
version: 1.1.0
author: AroCore
license: MIT
metadata:
  hermes:
    tags: [mikrotik, routeros, routeros7, networking, cli, firewall, routing, vpn, scripting, containers]
    category: networking
---

# MikroTik RouterOS Official Manual

Use this skill for detailed RouterOS questions. The official MikroTik Manual is
the authoritative source.

## Progressive disclosure

Do not load the whole manual into context. Identify the RouterOS topic/version
first, then load only the relevant files from `references/`.

Preserve exact command paths, properties, types, defaults, examples,
prerequisites, and version-specific behavior. Never invent undocumented
commands or properties.

## Official sources

- https://manual.mikrotik.com/docs/introduction/
- https://manual.mikrotik.com/llms.txt
- https://manual.mikrotik.com/llms-full.txt

## Updating

Manual synchronization is performed by:

    python3 scripts/sync_mikrotik_manual.py

The synchronizer tracks page hashes and only rewrites changed pages. It also
removes local reference files for pages no longer present in the official
index.

For a full rebuild:

    python3 scripts/sync_mikrotik_manual.py --clean

For a test:

    python3 scripts/sync_mikrotik_manual.py --limit 10

Third-party RouterOS skills remain separate from this official documentation
skill.
