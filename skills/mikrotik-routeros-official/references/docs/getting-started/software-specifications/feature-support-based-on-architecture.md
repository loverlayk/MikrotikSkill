# Feature support based on architecture

> This page outlines feature support differences across MikroTik RouterOS architectures, listing which features are unsupported or exclusively available for each platform like ARM, MIPS, and PPC. It also references...

# Feature support based on architecture

## Feature Support by Architecture

Most feature support is consistent across all device architectures, with only a few exceptions. The table below shows which features are not supported or are exclusively supported for each architecture:

| Architecture | Not Supported | Exclusively Supported |
| :-- | :-- | :-- |
| **ARM (ARM32)** | — | ZeroTier, Container, BTH |
| **ARM64** | — | ZeroTier, Container, BTH |
| **MIPSBE** | ZeroTier, Dude Server | — |
| **MMIPS** | ZeroTier | — |
| **SMIPS** | ZeroTier, DOT1X, BGP, MPLS, PIMSM, Dude Server, User Manager, Reverse Proxy | — |
| **TILE** | ZeroTier | BTH |
| **PPC** | ZeroTier, Dude Server | — |
| **x86 PC** | ZeroTier, Cloud | Container |
| **CHR (Cloud Hosted Router)** | — | Container |

In addition to feature differences, hardware capabilities vary by device model. For more information, see the following resources:

- **WiFi** — New driver implementation for 802.11ax devices and supported older devices
- **L3 Hardware Offloading** — Device support details
- **PTP (Precision Time Protocol)** — Overview and configuration
- **Switch Chip Features** — Capabilities and limitations
