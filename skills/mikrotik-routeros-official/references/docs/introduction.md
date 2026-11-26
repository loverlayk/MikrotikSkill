# Introduction

> MikroTik RouterOS is a powerful network operating system for MikroTik devices, offering routing, firewalling, VPN, wireless management, QoS, automation, and monitoring tools in one platform for network building and...

# Introduction

MikroTik RouterOS is the network operating system that powers MikroTik routers, switches, and wireless devices. It brings together routing, firewalling, VPN, wireless management, quality of service, automation, and monitoring tools in a single platform for building and operating networks of all sizes.

## How the documentation is organized

The sidebar on the left is the map of the manual. Categories are ordered to take you from general knowledge toward specific features, so a reader who works through them top to bottom moves from first contact with a device to advanced configuration.

The flow is:

- **Getting Started** covers how to reach a new device, first-time configuration, installation, licensing, upgrades, and basic security.
- The topic sections that follow each focus on one area of the system: management tools, system information and utilities, diagnostics and monitoring, hardware, wired and wireless connectivity, mobile networking, bridging and switching, network services, routing protocols, firewall and quality of service, virtual private networks, user management, high availability, the Internet of Things, storage, and containers.
- **Developer Guides** cover scripting and the programming interfaces for people who automate RouterOS.
- **CLI Reference** sits at the end as a lookup section rather than a reading section.

Start in Getting Started if a device is new to you. Move to the topic section that matches your task once the base system is in place. Treat the CLI Reference as a dictionary you consult while you work, not a chapter you read front to back.

## Finding information

You have several ways to locate content:

- **Search.** The search box indexes the full text of every page. It is the fastest route when you know a keyword, a command, or a property name.
- **Sidebar and breadcrumbs.** Browse the sidebar to explore a topic, and read the breadcrumb trail at the top of each page to see where you are in the structure.
- **In-page contents.** The list on the right side of a page links to the headings on that page, so you can jump straight to the part you need on longer articles.
- **Version selector.** The version dropdown in the top navigation lets you choose which release of the documentation to read when more than one version is published.

## The CLI Reference

The [CLI Reference](./cli-reference/) documents RouterOS command menus and properties by console path. Look up a feature by its menu, for example `/ip/address` or `/routing/bgp`, to find the available commands, the configuration objects, and every property with its type and default.

This section is generated automatically from the RouterOS system itself rather than written by hand. The menus, commands, and argument types are extracted from the software, so the reference tracks what the system actually exposes. Each parameter lists an argument type, and the legend that explains those types is on the CLI Reference start page. Because the section is generated, look things up by console path and rely on search instead of expecting a hand-edited article for every topic.

## Release notes and documentation updates

Two separate sections track how things change over time:

- **[Docs Changes](/changelog)** — dated summaries of what changed in the manual, with links to the affected pages. Check here to see what was added, corrected, or reorganized since your last visit.
- **[Product news](/blog)** — MikroTik product announcements and newsletters.

## Getting support

MikroTik handles help requests in a set order, from self-service resources to a ticket with the support team. Work through the steps until the problem is solved.

1. **Contact the seller.** If you did not buy the device directly from MikroTik, ask your distributor first. The distributor provides support and handles warranty claims for the hardware it sells.
2. **Check the documentation.** Most questions about a menu, a property, or a working configuration are already answered in this manual, including the [CLI Reference](./cli-reference/) and the configuration examples in each topic section.
3. **Search the community.** The [MikroTik forum](https://forum.mikrotik.com/) often describes the same problem and its solution.
4. **Update RouterOS.** Reproduce the problem on the latest RouterOS version before you open a ticket. The issue may already be corrected.
5. **Describe the setup and capture diagnostics.** Write a short description of the network setup and the steps to reproduce the problem. Create a [support output file](./getting-started/supout-rif) (`supout.rif`) while the problem is present. The file holds the configuration, logs, process state, and crash data the support team needs.
6. **Submit the request.** Open a ticket in the [MikroTik support system](https://help.mikrotik.com/servicedesk/servicedesk), or send the description and the `supout.rif` to [support@mikrotik.com](mailto:support@mikrotik.com). Sign up for a support system account to keep a history of your requests. If you have already exchanged email with support, use the password recovery on the login page to claim the account.

[MikroTik Certified Consultants](https://mikrotik.com/consultants) provide immediate personal help with design and troubleshooting. They are independent specialists, not MikroTik employees, and their services are paid.

For a suspected hardware fault, run the checks in [Try before RMA](./hardware/try-before-rma) first. If the device still fails, start a warranty claim through your seller or the RMA system in your [mikrotik.com](https://mikrotik.com) account, and send the `supout.rif` with the request. Report security vulnerabilities through `security@mikrotik.com`, not the ordinary support flow.

If you find an error, an outdated instruction, or a gap in a page, tell us. Send an email to [support@mikrotik.com](mailto:support@mikrotik.com) with the address of the page and a short description of the problem. Include the exact wording you expected to see when you can, because it makes the correction faster. Clear reports about a single page are the most effective way to improve the manual for everyone.

## Machine-readable access for AI tools

The whole manual is published in plain formats so it can be read by retrieval pipelines, assistants, and other automated tools, not only in a browser.

The available endpoints are:

| Endpoint | Purpose |
| --- | --- |
| [`/llms.txt`](pathname:///llms.txt) | An index of every page, with a short description and a link for each. It follows the [llms.txt convention](https://llmstxt.org) and is meant as an entry point a tool reads first to discover what exists. |
| [`/llms-full.txt`](pathname:///llms-full.txt) | The entire manual concatenated into one plain-text file, intended for bulk ingestion or loading a full local copy. |
| Per-page Markdown | The raw source of any page. Append `.md` to a documentation address, for example [`/docs/introduction.md`](pathname:///docs/introduction.md), to fetch the Markdown behind it. |
| [`/sitemap.xml`](pathname:///sitemap.xml) | A standard sitemap that lists every page for crawlers and indexers. The site `robots.txt` permits standard and AI crawlers. |

A common pattern is to read `/llms.txt` first to find the relevant pages, then fetch the individual `.md` pages you need for detail. When you want the complete corpus in one piece, load `/llms-full.txt` instead. These files are regenerated on every build, so they stay in step with the published pages.
