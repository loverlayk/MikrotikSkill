# Log

> RouterOS logs system events in topics; rules in /system/logging send them to memory, a disk, the console, a syslog server (UDP, TCP or TLS; syslog or CEF format), email or a script. Read the log with /log/print.

# Log

RouterOS writes events to the system log: logins and login failures, configuration changes and who made them, interfaces going up and down, DHCP leases, protocol state changes and errors. Each entry has a time, one or more topics that say where it comes from and how important it is (for example `dhcp,info` or `system,error,critical`), and a message.

Two menus decide what is kept and where it goes:

- Rules in `/system/logging` select entries by their topics and pass them to an action.
- Actions in `/system/logging/action` store the entries in memory or in files on a disk, print them on the console, send them to a syslog server or by email, or run a script.

The default configuration has four rules:

| Topics | Action | Result |
| :-- | :-- | :-- |
| `info` | `memory` | Kept in RAM. |
| `error` | `memory` | Kept in RAM. |
| `warning` | `memory` | Kept in RAM. |
| `critical` | `echo` | Printed on open terminals, and at the next login when no terminal is open. |

The `memory` action keeps the newest 1000 entries, and they are lost when the router reboots. Debug messages are not logged by default. To keep the log across reboots, log to a disk or to a syslog server.

For a video introduction, see [Logging basics](https://www.youtube.com/watch?v=E-QAhaWtsnU).

## Read the log

`/log/print` shows the entries kept in memory, oldest first. Filter them with `where`: `topics~` matches a pattern against the topics, `message~` against the message text.

```ros
[admin@MikroTik] > /log/print where topics~"interface|dhcp"
 2026-10-02 17:34:34 interface,info lo link up
 2026-10-02 17:34:42 interface,info ether2 link up (speed 1G, full duplex)
 2026-10-02 17:34:47 dhcp,info bridge on bridge got IP address 192.168.88.36
```

To watch new entries as they arrive, add `follow` (prints the existing entries first) or `follow-only` (new entries only). Press <kbd>Space</kbd> to print a separator line, and <kbd>Control</kbd>+<kbd>C</kbd> to stop. For example, to watch failed logins:

```ros
[admin@MikroTik] > /log/print follow-only where topics~"critical"
 = = =   = = =   = = =      = = =   = = =   = = =      = = =   = = =   = = =
2026-10-02 17:35:45 system,error,critical login failure for user admin from 192.168.88.17 via ssh
2026-10-02 17:35:45 system,error,critical login failure for user root from 192.168.88.17 via ssh
-- Ctrl-C to quit. Space prints separator. New entries will appear at bottom.
```

Login and firewall entries carry extra fields, such as the user, the service and the source address. `with-extra-info` adds them to the line:

```ros
[admin@MikroTik] > /log/print with-extra-info where message~"login failure"
 2026-10-02 17:35:45 system,error,critical login failure for user admin from 192.168.88.17 via ssh app=ssh duser=admin outcome=failure src=192.168.88.17
 2026-10-02 17:35:45 system,error,critical login failure for user root from 192.168.88.17 via ssh app=ssh duser=root outcome=failure src=192.168.88.17
```

`/log/print` also lists the buffers of other memory actions and the newest entries of disk actions, so an entry that several actions store shows once per action. Add `where buffer=memory` to see only the default buffer.

To save the printed entries to a file, add `file=`: `/log/print file=log-before-upgrade` writes `log-before-upgrade.txt`.

### Find what happened at a certain time

Compare `time` with a date and time to see the entries of a period, for example a night:

```ros
/log/print where time>"2026-10-02 01:00:00" and time<"2026-10-02 06:00:00"
```

A lost uplink usually shows as `interface,info ether1 link down` and `link up` entries of the WAN interface, and as DHCP client or PPP entries. When the uplink stays up but the provider stops forwarding traffic, nothing is logged; use [Netwatch](../netwatch) to log such outages. How far back the 1000 entries of the default buffer reach depends on how much the router logs. To keep more, log to a disk or a syslog server.

### Find out who changed the configuration

Each configuration change is logged with the topics `system,info`, who made it (a user and how the user was connected, or a scheduler entry), and the command:

```ros
[admin@MikroTik] > /log/print where topics~"system" and message~" by "
 2026-10-02 17:33:27 system,info static dns entry added by scheduler:add-nas-dns (*2 = /ip dns static add address=192.168.88.20 name=nas.lan)
```

### Write your own entries

Scripts write to the log with `:log info`, `:log warning`, `:log error` and `:log debug`. On the command line, `/log/info`, `/log/warning`, `/log/error` and `/log/debug` do the same. These entries get the topics `script,info`, `script,warning`, and so on. See [Scripting](../../developer-guides/scripting/).

## Log debug messages for one feature

Many features write debug messages, which are logged only when a rule selects them. To troubleshoot one feature, log its `debug` messages into a separate memory buffer, so that they do not push the other entries out of the default buffer. For example, when a client does not get an address from the DHCP server:

```ros
/system/logging/action/add name=dhcpdebug target=memory \
    memory-lines=2000
/system/logging/add topics=dhcp,debug action=dhcpdebug
```

Read the buffer, and empty it between tests:

```ros
/log/print where buffer=dhcpdebug
/system/logging/action/clear action=dhcpdebug
```

A rule matches only entries that have all its topics, so `topics=dhcp,debug` selects DHCP debug messages and nothing else. To leave out the packet dumps that some features add, exclude a topic with `!`, for example `topics=ntp,debug,!packet`.

When you are done, save the buffer to a file, then remove the rule and the action. Removing the rule empties the buffer:

```ros
/log/print where buffer=dhcpdebug file=dhcp-debug
/system/logging/remove [find action=dhcpdebug]
/system/logging/action/remove dhcpdebug
```

:::warning
Debug messages can contain secrets. For example, `ssh,debug` logs the session encryption keys, and `ssh,debug,packet` the content of the sessions. Keep debug messages in a local buffer, and do not send them to a syslog server or by email.
:::

## Keep the log across reboots

The default `disk` action writes to files on the router's storage. Add a rule for each topic you want to keep:

```ros
/system/logging/add topics=info action=disk
/system/logging/add topics=warning action=disk
/system/logging/add topics=error action=disk
/system/logging/add topics=critical action=disk
```

The action writes `log.0.txt` until it holds `disk-lines-per-file` lines (1000 by default). Then the file is renamed to `log.1.txt` and a new `log.0.txt` starts. The action keeps `disk-file-count` files (2 by default) and deletes the oldest. The files are in `/file`:

```ros
[admin@MikroTik] > /file/print where name~"^log"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME       TYPE       SIZE  LAST-MODIFIED
0 log.0.txt  .txt file  1956  2026-10-02 17:32:13
```

The newest entries also show in `/log/print`, under the action's name, so each entry shows twice there; add `where buffer=memory` or `where buffer=disk`. After a reboot, the entries of the current file show again under `buffer=disk`. To read an older file, print its contents, or download it from `/file`:

```ros
:put [/file/get log.1.txt contents]
```

To keep more history, raise both values. To write to a USB drive or another disk, put the disk's folder in front of the file name; the folder must exist:

```ros
/system/logging/action/set disk disk-file-name=usb1/log \
    disk-lines-per-file=5000 disk-file-count=5
```

To limit the writes to the internal flash, log to disk only the topics you need, or use an external disk.

## Send the log to a syslog server

The default `remote` action sends entries to a syslog server over UDP port 514. It has no server address (`remote=0.0.0.0`), and no default rule uses it. Set the server and the format, and add a rule for each topic:

```ros
/system/logging/action/set remote remote=192.0.2.10 \
    remote-log-format=syslog
/system/logging/add topics=info action=remote
/system/logging/add topics=warning action=remote
/system/logging/add topics=error action=remote
/system/logging/add topics=critical action=remote
```

Use separate rules: one rule with `topics=info,warning,error` matches only entries that have all three topics, which is none. To send only logins and logouts, use `topics=account`; failed logins have the topics `system,error,critical`, so they go with `error` or `critical`.

To check that the server receives entries, write one yourself:

```ros
/log/warning "syslog test"
```

`remote-log-format` selects what the server receives (examples in Technical details):

- `default` - The topics and the message, without the time and the host name.
- `syslog` - BSD syslog (RFC 3164), as most syslog servers expect over UDP: a priority, the time and the router's identity (`/system/identity`) in front of the message. The facility is `daemon` and the severity comes from the topics; set `syslog-facility` and `syslog-severity` to change them. The topics are not sent; set `add-topics-string=yes` to add them in front of the message, so that the server can tell, for example, DHCP from firewall entries. RFC 5424 is not supported.
- `cef` - Common Event Format, for security information and event management (SIEM) systems: the extra fields of login and firewall entries (user, service, addresses, interfaces) become CEF fields.

The BSD time has no year and no time zone, so the server takes its own. Set `syslog-time-format=iso8601` (also used by `cef`) when the router and the server are in different time zones, and keep the router's clock correct with [NTP](../../system-information-and-utilities/ntp).

Over UDP, entries are lost while the server is unreachable. With `remote-protocol=tcp` or `tls`, the router keeps up to 1000 entries in memory while the connection is down, for all remote actions together, and sends them when it is back; when the buffer is full, newer entries are dropped, and the buffer is lost at reboot. Over TCP and TLS, use `remote-log-format=cef`: CEF entries end with a delimiter (`cef-event-delimiter`), while `default` and `syslog` entries follow each other in the stream without one, so most servers cannot tell where one ends.

Use `src-address` to choose the source address, and `vrf` when the server is reachable through a [VRF](../../user-guides/routing-and-networking-protocols/vrf).

The following guides set up Elasticsearch to receive and analyze RouterOS logs:

<DocCardList />

### Send the log over TLS

To encrypt the log, use `remote-protocol=tls`. To check the server certificate, import the certificate of the CA that signed it and set `check-certificate=yes`. Without `check-certificate=yes`, the router encrypts the connection but accepts any certificate:

```ros
/certificate/import file-name=syslog-ca.pem name=syslog-ca \
    passphrase="" trusted=yes
/system/logging/action/add name=siem target=remote remote=192.0.2.10 \
    remote-port=6514 remote-protocol=tls remote-log-format=cef \
    check-certificate=yes
/system/logging/add topics=info action=siem
/system/logging/add topics=warning action=siem
/system/logging/add topics=error action=siem
/system/logging/add topics=critical action=siem
```

When the certificate cannot be verified, the router sends nothing, retries, and logs an `ssld,error` entry that ends with `ssl: no trusted CA certificate found`.

`check-certificate=yes` checks that a trusted certificate signed the server certificate. It does not compare the name in the certificate with the server address, so any certificate from a trusted CA passes: trust only the CA of your log servers, or import the server's own certificate. The router does not present a client certificate.

Actions that send to the same server address and port share one connection. Give them the same `remote-protocol` and `check-certificate`.

## Email log messages

The `email` target sends one email for each entry, with the topics and the message as the subject and the text. It uses the server, port, TLS mode and sender of `/tool/e-mail`, so configure that first (see [Email](../../system-information-and-utilities/e-mail)). For example, to get an email for every critical entry, such as a login failure, a reboot by the watchdog or a clock correction:

```ros
/system/logging/action/add name=mail target=email \
    email-to=admin@example.com
/system/logging/add topics=critical action=mail
```

To get an email for failed logins only, add a `regex` that the message must match; `^` means that the message starts with the text:

```ros
/system/logging/add topics=critical regex="^login failure" action=mail
```

`email-cc` adds more recipients. Each email sent is logged as `e-mail,info sent <topics message> to: <address>`. Choose the topics carefully: every entry sends an email, so a password-guessing attack sends hundreds. Stop such attacks with the firewall instead (see [SSH brute-force protection](../../firewall-and-quality-of-service/user-guides/bruteforce-prevention)).

## Run a script on a log message

The `script` target runs a script from `/system/script` for the entries its rule matches. The script gets the entry in two variables: `$topics` (for example `system,error,critical`) and `$message`. Entries that match while the script is still running are skipped, and entries that the script logs itself do not start it again.

For example, to collect the source addresses of failed logins in an address list, for any service (SSH, WinBox, WebFig, API). An address stays in the list for a day after its last failed login:

```ros
/system/script/add name=login-failure source={
    :local at [:find $message " from "]
    :while ([:typeof [:find $message " from " $at]] = "num") do={
        :set at [:find $message " from " $at]
    }
    :local ip [:pick $message ($at + 6) [:find $message " via " $at]]
    /ip/firewall/address-list/remove [find list=login-fail address=$ip]
    /ip/firewall/address-list/add list=login-fail address=$ip timeout=1d
}
/system/logging/action/add name=loginfailure target=script \
    script=login-failure
/system/logging/add topics=critical regex="^login failure" \
    action=loginfailure
```

The rule's `regex` limits the script to entries such as `login failure for user admin from 192.168.88.17 via ssh`. The user name in the message comes from the client and can contain spaces and the word `from`, so the script takes the address after the last ` from `, which the router writes itself. The list does nothing by itself: use it in a firewall rule (see [Address lists](../../firewall-and-quality-of-service/firewall/address-lists)), and exempt your own management addresses, so that a mistyped password cannot lock you out.

## How rules match entries

A rule passes an entry to its action when all of these are true:

- The entry has every topic listed in `topics`, and none of the topics listed with `!`. `topics=script,warning` matches `script,warning` entries, not every `script` entry and every `warning` entry.
- The message matches `regex`, when the rule has one. The regular expression also sees the entry's extra fields after the message, so `$` does not match the end of a login entry's message.
- The rule is enabled.

A rule without `topics` matches every entry, debug messages included.

Every matching rule passes its own copy, so one entry can go to memory, a disk and a syslog server at the same time. When two rules pass the same entry to the same action, the action stores it once.

`prefix` adds text in front of the message for that rule's action: `prefix=core1` stores and sends `core1: <message>`. Use it to tell routers apart on a shared syslog server.

When you change or disable the only rule that uses a memory action, the action's buffer is emptied. Changing the action itself, or one of several rules that use it, keeps the entries.

## Topics

Each entry has one or more topics. Usually one names the feature that wrote the entry and one gives its importance, and some features add more. A login failure has the topics `system,error,critical`; SSH debug messages have `ssh,debug`, and their packet dumps `ssh,debug,packet`.

### Importance topics

| Topic | Entries |
| :-- | :-- |
| `critical` | Events that need attention, such as login failures, reboots by the watchdog and clock corrections. The default rule prints them on the console. |
| `error` | Errors. |
| `warning` | Warnings. |
| `info` | Informational entries, such as logins, configuration changes and link state changes. |
| `debug` | Detailed messages for troubleshooting, logged only when a rule asks for them. |
| `packet` | Contents of a sent or received packet, decoded. |
| `raw` | Raw contents, for example a packet as hex or the AT commands exchanged with an LTE modem. |

### Feature topics

| Topic | Entries |
| :-- | :-- |
| `account` | Logins and logouts of users. |
| `acme-client` | The ACME client that gets certificates. |
| `async` | The command channel of LTE modems. |
| `backup` | Backup creation. |
| `bfd` | BFD. |
| `bgp` | BGP. |
| `bridge` | Bridges. |
| `calc` | Route calculation. |
| `caps` | CAPsMAN and CAPs. |
| `certificate` | Certificates. |
| `clock` | Clock changes, for example by NTP or IP Cloud. |
| `container` | Containers. |
| `ddns` | Dynamic DNS. |
| `dhcp` | DHCP clients, servers and relays. |
| `discover` | Neighbor discovery. |
| `disk` | Disks. |
| `dns` | DNS. |
| `dot1x` | 802.1X authentication. |
| `dude` | The Dude. |
| `e-mail` | The email tool (`/tool/e-mail`). |
| `event` | Events, for example a route installed in the routing table or a message from an LTE modem. |
| `evpn` | EVPN. |
| `fetch` | The fetch tool. |
| `firewall` | Firewall rules with `action=log` or `log=yes`, with their `log-prefix`. |
| `gps` | GPS. |
| `gsm` | GSM modems and the SMS tool. |
| `health` | Health monitoring (voltage, temperature, fans). |
| `hotspot` | HotSpot. |
| `igmp-proxy` | IGMP proxy. |
| `interface` | Interfaces, for example link up and link down. |
| `ipsec` | IPsec. |
| `iscsi` | iSCSI. |
| `isis` | IS-IS. |
| `kvm` | Virtual machines (KVM). |
| `l2tp` | L2TP clients and servers. |
| `ldp` | LDP. |
| `lora` | LoRa. |
| `lte` | LTE and 5G modems. |
| `manager` | User Manager. |
| `mpls` | MPLS. |
| `mqtt` | MQTT. |
| `mvrp` | MVRP. |
| `natpmp` | NAT-PMP. |
| `netwatch` | Netwatch. |
| `ntp` | The NTP client and server. |
| `ospf` | OSPF. |
| `ovpn` | OpenVPN. |
| `pim` | PIM-SM. |
| `poe-in` | PoE-In events, for example LLDP power negotiation when the device itself is powered via PoE. |
| `poe-out` | PoE output. |
| `pon` | PON SFP modules. |
| `ppp` | PPP. |
| `pppoe` | PPPoE clients and servers. |
| `pptp` | PPTP clients and servers. |
| `ptp` | Precision Time Protocol. |
| `queue` | Queues. |
| `radius` | The RADIUS client. |
| `radvd` | IPv6 router advertisements. |
| `rip` | RIP. |
| `route` | Routing. |
| `rpki` | RPKI. |
| `rproxy` | The reverse proxy. |
| `rsvp` | RSVP. |
| `script` | Scripts (`:log`) and the `/log/info` and related commands. |
| `sertcp` | Serial port remote access (`/port/remote-access`). |
| `smb` | The SMB server. |
| `snmp` | SNMP. |
| `socksify` | Socksify. |
| `ssh` | The SSH server and client. |
| `ssld` | TLS connections of RouterOS features, for example a server certificate that cannot be verified. |
| `sstp` | SSTP clients and servers. |
| `stp` | Spanning tree. |
| `system` | System messages, for example reboots and configuration changes. |
| `tftp` | The TFTP server. |
| `timer` | Timers, for example BGP keepalive timers. |
| `tr069` | The TR-069 client. |
| `update` | Package updates. |
| `upnp` | UPnP. |
| `ups` | UPS monitoring. |
| `vpls` | VPLS. |
| `vrrp` | VRRP. |
| `watchdog` | The watchdog. |
| `web-proxy` | The web proxy. |
| `wiliot` | Wiliot. |
| `wireguard` | WireGuard. |
| `wireless` | Wireless interfaces. |
| `zerotier` | ZeroTier. |

The router also lists the topics `amt`, `isdn`, `mme`, `read`, `simulator`, `state`, `store`, `telephony` and `write`, and `netinstall` with the `option` package.

## Troubleshoot

| Problem | Cause and fix |
| :-- | :-- |
| The syslog server receives nothing. | The default `remote` action has `remote=0.0.0.0`; set the server address. Check that a rule passes entries to the action: a rule with several topics needs all of them. Check that the router reaches the server from `src-address` and in `vrf`, and that the server accepts the protocol and port. |
| TLS logging sends nothing. | Look for `ssld,error` entries. `no trusted CA certificate found` means that the CA certificate of the server is not imported or not trusted. |
| The server shows several entries as one. | Over TCP and TLS, `default` and `syslog` entries have no delimiter; use `remote-log-format=cef`. |
| Entries show several times in `/log/print`. | Several actions store them; filter with `where buffer=memory`. |
| The log is empty after a reboot. | Memory actions do not survive a reboot; log to a disk or a syslog server. |
| A memory buffer emptied itself. | The only rule that uses it was changed or disabled. |
| `bad disk file name` | The folder in `disk-file-name` does not exist. |
| `action name can contain only letters and numbers` | Action names cannot contain `-`, `_` or other characters. |

## Technical details

### Message formats

The same login failure, as the server receives it in each `remote-log-format` (with `syslog-time-format=bsd-syslog` and the identity `MikroTik`):

```text
system,error,critical login failure for user guest from 192.168.88.17 via ssh
<27>Oct  2 17:36:35 MikroTik login failure for user guest from 192.168.88.17 via ssh
Oct  2 17:36:35 MikroTik CEF:0|MikroTik|hAP ax^2|7.25beta5|10|system,error,critical|High|dvchost=MikroTik dvc=192.168.88.36 msg=login failure for user guest from 192.168.88.17 via ssh app=ssh duser=guest outcome=failure src=192.168.88.17
```

- The `syslog` format carries no tag field; the message follows the identity.
- With `syslog-severity=auto`, the severity comes from the topics: `debug` 7, `info` 6, `warning` 4, `error` 3. An entry with both `error` and `critical`, as in the example, gets 3, so a server filter for severity `crit` misses login failures. The priority is the facility times 8 plus the severity: `daemon` (3) and `error` (3) give `<27>`.
- The CEF header holds the board name, the RouterOS version, an event class number, the topics and a severity (`Low` for `info` and `debug`, `Medium` for `warning`, `High` for `error`). `dvchost` is the identity, `dvc` an address of the router, `msg` the message, and the extra fields of the entry follow. Firewall entries carry the chain, the log prefix, the interfaces, the addresses and the protocol. `=` and `\` in values are escaped as `\=` and `\\`. Each CEF message ends with `cef-event-delimiter` (`\r\n` by default).

### TCP and TLS

- UDP sends one datagram per entry. TCP and TLS keep one connection per server address and port, shared by all actions that send there.
- While a TCP or TLS server is unreachable, the router keeps the entries in one buffer for all remote actions and retries the connection. The buffer is lost on reboot.
- While the server is unreachable, up to 1000 entries wait in memory; when the buffer is full, newer entries are dropped.
- CEF messages end with the delimiter; `default` and `syslog` messages follow each other in the stream without one.
- `check-certificate=yes` checks the server certificate against the trusted certificates in `/certificate`, not the name in it. The router offers TLS 1.2.

### Disk files

Each line in the files starts with the date in its own format, `Oct/02/2026 16:49:36`, followed by the topics and the message. `/system/logging/action/clear` empties memory actions only; on a disk action, it fails with `cleanup not supported on this target`.

For all parameters, see the [`/system/logging`](../../cli-reference/system/logging/) and [`/system/logging/action`](../../cli-reference/system/logging/action/) CLI reference, and [`/log`](../../cli-reference/log) for the entries.
