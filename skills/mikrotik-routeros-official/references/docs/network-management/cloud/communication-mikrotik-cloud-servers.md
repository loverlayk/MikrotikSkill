# Communication with MikroTik Cloud Services

> Every connection RouterOS makes to MikroTik servers: the menu that starts it, the server, whether it runs by default, and how to turn it off.

# Communication with MikroTik Cloud Services

RouterOS connects to MikroTik servers only for the services in the following table. By default, the router asks the cloud server for the time and time zone when it starts, and a Cloud Hosted Router (CHR) checks its license. Everything else runs only after you enable it or run the command.

| Menu | Server | On by default | How to turn it off |
| :-- | :-- | :-- | :-- |
| `/system/clock` `time-zone-autodetect` | `cloud2.mikrotik.com` | Yes | `/system/clock/set time-zone-autodetect=no` (see [Clock](../../system-information-and-utilities/clock)) |
| `/ip/cloud` `update-time` | `cloud2.mikrotik.com` | Yes | `/ip/cloud/set update-time=no` (see [Time update](./#time-update)) |
| `/ip/cloud` `ddns-enabled` | `cloud2.mikrotik.com` | No | `/ip/cloud/set ddns-enabled=auto`, with Back To Home off (see [DDNS](./#ddns)) |
| `/ip/cloud` `back-to-home-vpn` | `cloud2.mikrotik.com` and relay servers | No | `/ip/cloud/set back-to-home-vpn=revoked-and-disabled` (see [Back To Home](./back-to-home)) |
| `/ip/cloud/back-to-home-file` | `cloud2.mikrotik.com` and relay servers | No | Remove all file shares (see [File Share](./file-share)) |
| `/system/backup/cloud` | `cloud2.mikrotik.com` | No | Runs only for the `print`, `upload-file`, `download-file` and `remove-file` commands (see [Cloud backup](./cloud-backup)) |
| `/system/license` | `licence.mikrotik.com` | Only on CHR | Cannot be turned off on CHR (see [CHR licensing](../../getting-started/routeros-licensing/chr/chr-licensing)) |
| `/interface/lte` `firmware-upgrade` | `upgrade.mikrotik.com` | No | Runs only for the `firmware-upgrade` command (see [LTE firmware upgrade](../../mobile-networking/lte-5g#modem-firmware-upgrade-command)) |
| `/interface/detect-internet` | `cloud.mikrotik.com` | No | `/interface/detect-internet/set detect-interface-list=none` (see [Detect Internet](../../diagnostics-monitoring-and-troubleshooting/detect-internet)) |
| `/system/package/update` | `upgrade.mikrotik.com` | No | Runs only for the `check-for-updates` command and package downloads (see [Packages](../../getting-started/installation-and-upgrade/packages)) |
| `/system/swos` `upgrade` | `upgrade.mikrotik.com` | No | Runs only for the `upgrade` command (see [SwOS upgrade](../../bridging-and-switching/marvell-prestera-switch-chip-features#configuring-swos-using-routeros)) |

## Technical details

The router uses the following ports:

- `cloud2.mikrotik.com`: UDP port 15252 for DDNS and TCP port 15252 for cloud backup. The name resolves to more than one address, and the router tries another one when a server does not answer.
- `cloud.mikrotik.com`: UDP port 30000 for Detect Internet.
