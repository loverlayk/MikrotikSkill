---
name: mikrotik-routeros-official
description: Official MikroTik RouterOS documentation, CLI reference, configuration syntax, and version-specific behavior.
version: 1.1.1
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

Do not load the whole manual into context.

For every RouterOS question:

1. Identify the RouterOS version if provided by the user.
2. Read `references/_manifest.md` first.
3. Use the manifest to identify the smallest set of relevant documentation files.
4. Load only the relevant reference files.
5. Prefer version-specific documentation when available.
6. Preserve exact RouterOS command paths, properties, types, defaults,
   examples, prerequisites, and version-specific behavior.
7. Never invent undocumented commands, properties, or behavior.
8. If the official documentation does not provide enough information,
   explicitly say so instead of guessing.

## Language policy

- Default response language: Persian (fa-IR) when the user asks in Persian.
- Explain RouterOS concepts in clear Persian.
- Preserve all RouterOS commands, paths, properties, configuration snippets,
  error messages, and code in their original form.
- Keep important English technical terms in parentheses when useful.
- If the user explicitly requests English, answer in English.

## Source priority

Use sources in this order:

1. Official MikroTik documentation in `references/`.
2. The official machine-readable MikroTik Manual sources listed below.
3. Local Persian guidance included by this skill, when available.
4. Never invent undocumented RouterOS behavior.

## Official sources

- https://manual.mikrotik.com/docs/introduction/
- https://manual.mikrotik.com/llms.txt
- https://manual.mikrotik.com/llms-full.txt

## Updating

Manual synchronization is performed by:

    python3 scripts/sync_mikrotik_manual.py

The synchronizer tracks page hashes and only rewrites changed pages. It also
removes local reference files for pages no longer listed in the official
index.

For a full rebuild:

    python3 scripts/sync_mikrotik_manual.py --clean

For a test:

    python3 scripts/sync_mikrotik_manual.py --limit 10

If any documentation page fails to download, the sync exits with a non-zero
status so GitHub Actions cannot incorrectly report a successful sync.

Third-party RouterOS skills remain separate from this official documentation
skill.
