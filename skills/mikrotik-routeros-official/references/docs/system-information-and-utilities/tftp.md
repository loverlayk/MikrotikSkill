# TFTP

> The RouterOS TFTP server: serve boot, firmware and configuration files to devices, accept uploads, match requested file names with access rules and regular expressions, and troubleshoot block sizes, large files and...

# TFTP

RouterOS includes a TFTP server. Trivial File Transfer Protocol (TFTP) is a simple file transfer protocol over UDP, without authentication, that network devices use at startup: IP phones and access points fetch their configuration or firmware with it, network-booting computers load a boot loader, and switches upload configuration backups. The server serves files from the router's storage and accepts uploads when a rule allows them.

The server runs while `/ip/tftp` holds at least one enabled access rule. Each request is checked against the rules in order: the first rule that matches the client address and the requested file name decides, and a request that no rule matches is refused. To download a file from another TFTP server, use [`/tool/fetch`](fetch) with `mode=tftp`.

Devices usually learn the TFTP server and the file name from DHCP. On a RouterOS DHCP server, set `next-server` (the TFTP server address) and `boot-file-name` in [`/ip/dhcp-server/network`](../cli-reference/ip/dhcp-server/network); devices that expect DHCP options 66 or 150 get them from [DHCP options](../network-management/dhcp/server).

:::warning
TFTP has no passwords: every client in a rule's `ip-addresses` can read, and with `read-only=no` write, every name the rule's `req-filename` matches. Limit `ip-addresses` to the devices that need the rule, and write `req-filename` so that it matches only the names you serve: in a rule that serves a folder or the requested name, a pattern such as `.*`, or an empty `req-filename`, also matches names that lead out of the served folder. The examples on this page use `[^/.][^/]*`, a name without a slash that does not start with a dot.
:::

## Serve files to devices

Create a folder, here `tftp`, copy the files into it (see [Files](files)), and serve it to the LAN. A folder as `real-filename` is put in front of the requested name, so a request for `phone.cfg` returns `tftp/phone.cfg`; the pattern accepts names with an optional leading slash, as some clients send it, and no subfolders:

```ros
/file/add name=tftp type=directory
/ip/tftp/add ip-addresses=192.168.88.0/24 \
    req-filename="/\?[^/.][^/]*" real-filename=tftp
```

To configure a rule in WinBox, open **IP > TFTP** and select **New**:

1. Use the **+** control beside **IP Addresses** to enter the allowed client address or subnet, such as `192.168.88.0/24` in the example.
2. Set **Req. Filename** to the requested-name pattern and **Real Filename** to the file or folder on the router. For the folder example, set **Real Filename** to `tftp` and use the pattern from the command.
3. Leave **Allow** and **Read Only** selected to serve files without accepting uploads. Review the address restriction and pattern before selecting **OK**, which creates the enabled rule.

![WinBox new TFTP rule with address, filename, and access settings](./img/tftp-winbox.webp)

The screenshot shows the blank new-rule dialog. Fill in the restrictions before saving it; an unrestricted rule can expose router files. Use **Files** to upload the files you intend to serve.

To give every client the same file whatever it asks for, set `req-filename=".*"` and a file as `real-filename`. Use this only for clients that fetch a single file; a boot loader that fetches more files after the first gets the same file again:

```ros
/ip/tftp/add ip-addresses=192.168.88.0/24 req-filename=".*" \
    real-filename=tftp/boot.img
```

To answer two names with one file:

```ros
/ip/tftp/add ip-addresses=192.168.88.0/24 \
    req-filename="(aaa|bbb)\\.bin" real-filename=tftp/ccc.bin
```

Files on another disk are served by their path, for example `real-filename=usb1/tftp/boot.img`.

## Accept uploads

Rules are read-only by default: an upload gets the error `illegal operation`. To let switches upload their configuration backups into a `backups` folder, allow writing, and overwriting for backups that repeat under the same name. The switches upload to `backups/<name>`, and their own settings decide when:

```ros
/file/add name=backups type=directory
/ip/tftp/add ip-addresses=192.168.88.2-192.168.88.9 \
    req-filename="backups/[^/.][^/]*" read-only=no allow-overwrite=yes
```

- Without `allow-overwrite=yes`, an upload to a name that already exists fails with `file exists`.
- The same rule lets its clients download the uploaded files, which usually contain passwords, so limit `ip-addresses` to the switches.
- Put the upload rule before any read-only rule that also matches `backups/` names, such as a rule with an empty `req-filename` or `.*`; otherwise the read-only rule answers first.
- Uploads fill the router's storage; remove old backups from time to time.

## Refuse some requests

A rule with `allow=no` refuses the requests it matches. Place it before the rule that would allow them, because the first matching rule decides. `req-filename` matches the name the client requests, not the path on the router. For example, to refuse one file of the folder that a broader rule would serve:

```ros
/ip/tftp/add ip-addresses=192.168.88.0/24 \
    req-filename="/\?secret\\.cfg" allow=no \
    place-before=[find real-filename=tftp]
```

Keep files that no client should read outside the served folder.

## Check and troubleshoot

The server listens on UDP port 69 while at least one rule exists, and `hits` counts the requests each rule answered:

```ros
/ip/service/print where name=tftpd
/ip/tftp/print
```

The router logs refused and failed transfers in the `tftp` topic, for example `ERROR code:0 string:permission denied!`. To see every request with its client, file name and result, and transfers that time out, log the `tftp,debug` topic as well:

```ros
/system/logging/add topics=tftp,debug
/log/print where topics~"tftp"
```

The debug lines show, for example, `requested (binary) file: phone.cfg access: allowed` and `connection timeout`.

The client receives the same TFTP error:

| Error | Cause |
| :-- | :-- |
| `permission denied!` (code 0) | No rule matches the client address and file name, or the first matching rule has `allow=no`. |
| `file not found` (code 1) | A rule matches, but the file it points to does not exist. Check `real-filename` and the path of the file. |
| `illegal operation` (code 4) | An upload to a read-only rule, or a transfer of more than 65535 blocks without `allow-rollover=yes`. |
| `file exists` (code 6) | An upload to an existing file without `allow-overwrite=yes`. |
| No answer | The router has no enabled TFTP rule, or the firewall drops UDP port 69: the default firewall accepts it only from interfaces in the `LAN` interface list. |

:::tip
If the router receives the requests but the client runs into a timeout during the transfer, check the block size: some embedded clients request a large block size and then fail to handle fragmented packets. Set the client's block size to the smallest MTU on the path minus 32 bytes (20 bytes for the IP header, 8 for UDP and 4 for TFTP), less if the network uses IP options: 1468 bytes for a 1500-byte MTU. On the router, set `max-block-size` to the next lower value it offers, for example `/ip/tftp/settings/set max-block-size=1454`, or `512`, which also fits IPv6 and tunnels. A smaller block size lowers the largest file a transfer can carry; see [Large files](#large-files).
:::

## How rules match

- `ip-addresses` lists the clients: IPv4 addresses, ranges (`192.168.88.2-192.168.88.9`) or prefixes, or IPv6 prefixes. Empty means any client.
- `req-filename` is the requested file name as a regular expression, case-sensitive. Empty matches any name.
- `real-filename` decides what is served. Empty serves the requested name itself, a file serves that file, and a folder is put in front of the requested name. The value is used as it is written: references such as `\1` to parts of `req-filename` are not supported.

A `req-filename` must match the whole requested name: `phone\.cfg` matches only `phone.cfg`, and `.*\.cfg` matches every name that ends in `.cfg`. RouterOS adds the anchors around the whole value, so put alternatives in a group: `(aaa|bbb)\.bin` matches `aaa.bin` and `bbb.bin`, but `(aaa.bin)|(bbb.bin)` matches every name that starts with `aaa.bin` or ends with `bbb.bin`. A value that starts with `^` is used as it is written, so `^boot` matches every name that starts with `boot` unless you end it with `$`.

The regular expression elements:

| Element | Meaning | Example |
| :-- | :-- | :-- |
| `.` | Any one character | `boo.` matches `boot` and `boox` |
| `*` | The previous element zero or more times | `.*\.bin` matches every `.bin` name |
| `+` | The previous element one or more times | `bo+t` matches `bot` and `boot` |
| `?` | The previous element once or not at all | `x?boot` matches `boot` and `xboot` |
| `[ ]` | One of the listed characters | `boo[tx]` matches `boot` and `boox` |
| `( \| )` | A group and alternatives | `(aaa\|bbb)\.bin` matches `aaa.bin` and `bbb.bin` |
| `\` | Takes the next character literally | `\.` matches a dot |
| `^`, `$` | The start and the end of the name | `^boot` matches names that start with `boot` |

In the terminal, a value in double quotes needs two backslashes for one (`"(aaa|bbb)\\.bin"`), `\$` for a dollar sign and `\?` for a question mark, because the console treats `\`, `$` and `?` itself (`?` shows help).

## Technical details

### Transfers

- By default, the client and the server exchange one data block at a time, and each block is acknowledged before the next one is sent.
- Clients can ask for a larger block size (`blksize`); the router agrees up to `max-block-size` in `/ip/tftp/settings`: `512`, `1454`, `4096` (the default) or `8192`. The router also answers the transfer size option (`tsize`). It does not negotiate a window size (`windowsize`).
- With `reading-window-size=pipelining` on a rule, the router sends several blocks of a download before it waits for acknowledgements, which speeds up downloads. The default is `none`.
- The server listens in the VRF set with `vrf` in `/ip/tftp/settings` (default `main`).

### Large files

TFTP numbers the blocks of a transfer with 16 bits, so a transfer ends at 65535 blocks: about 32 MiB with 512-byte blocks, 90 MiB with 1454-byte blocks and 256 MiB with 4096-byte blocks. With `allow-rollover=yes`, the router continues after block 65535 with block 0 and completes larger files; the client must support such a rollover. Without it, the transfer fails at the limit with `illegal operation`. To allow it on the folder rule:

```ros
/ip/tftp/set [find real-filename=tftp] allow-rollover=yes
```

For all properties, see [`/ip/tftp`](../cli-reference/ip/tftp/) and [`/ip/tftp/settings`](../cli-reference/ip/tftp/settings) in the CLI reference.
