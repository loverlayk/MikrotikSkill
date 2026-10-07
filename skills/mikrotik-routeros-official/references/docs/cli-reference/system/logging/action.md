# action

> Actions that store or send the messages selected by the rules in /system/logging. The default actions are memory (the buffer /log shows), disk (files named log), echo (open terminal sessions) and remote (a syslog...

-----------

## system/logging/action 
**Type:** Directory

Actions that store or send the messages selected by the rules in [`/system/logging`](../). The default actions are `memory` (the buffer `/log` shows), `disk` (files named `log`), `echo` (open terminal sessions) and `remote` (a syslog server, with no address set). Each memory action keeps its own buffer, which [`clear`](clear) empties. See [Log](../../../../diagnostics-monitoring-and-troubleshooting/log/).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">One of the default actions: `memory`, `disk`, `echo` and `remote`.</ArgTableRow>
<ArgTableRow arg="Y" typ="managed"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the action, letters and digits only. Rules refer to the action by this name, and for `target=memory` it is also the buffer name shown in the `buffer` field of [`/log`](../../../log).</ArgTableRow>
<ArgTableRow arg="target" typ="enum (memory | disk | echo | remote | email | script | cmr) { memory:0, disk:1, echo:2, remote:3, email:4, script:5, cmr:6 }" mandatory="1">
Where the messages go:
- `memory` - Keep them in a memory buffer named after the action, shown by `/log/print`. The buffer is empty after a reboot.
- `disk` - Write them to text files (`disk-file-name`).
- `echo` - Print them on open terminal sessions (`remember`).
- `remote` - Send them to a syslog server (`remote`).
- `email` - Send each message as an email (`email-to`).
- `script` - Run a script for each message (`script`).
</ArgTableRow>
<ArgTableRow arg="memory-lines" typ="num">Number of entries the buffer keeps, `1..65535`. When the buffer is full, each new entry drops the oldest one, unless `memory-stop-on-full` is set. Default: 1000.</ArgTableRow>
<ArgTableRow arg="memory-stop-on-full" typ="bool">When `yes`, the buffer keeps its first `memory-lines` entries and drops new ones until it is emptied with [`clear`](clear). Default: no.</ArgTableRow>
<ArgTableRow arg="disk-file-name" typ="string">Name of the log files, without the extension. The action writes to `<name>.0.txt`; when that file is full, it becomes `<name>.1.txt` and a new `<name>.0.txt` starts. To write to another disk or folder, put its name first, for example `usb1/log`. The folder must exist, otherwise the action is refused with `bad disk file name`. Two disk actions cannot use the same file name. Default: log.</ArgTableRow>
<ArgTableRow arg="disk-lines-per-file" typ="num">Number of lines in each file before the action starts a new file, `1..65535`. Default: 1000.</ArgTableRow>
<ArgTableRow arg="disk-file-count" typ="num">Number of files the action keeps, `1..65535`. When a new file starts and the count is reached, the oldest file and its entries are dropped. Default: 2.</ArgTableRow>
<ArgTableRow arg="disk-stop-on-full" typ="bool">Stop writing to this action when the log files are full, instead of dropping the oldest entries. Default: no.</ArgTableRow>
<ArgTableRow arg="remote" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, hostname: string
 }">Address of the syslog server: an IPv4 or IPv6 address or a host name. The default `remote` action has `0.0.0.0` (no server set). Default: 0.0.0.0.</ArgTableRow>
<ArgTableRow arg="remote-port" typ="num">Port of the syslog server. Default: 514.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">Source address of the packets sent to the syslog server. `0.0.0.0` leaves the choice to the router. Default: 0.0.0.0.</ArgTableRow>
<ArgTableRow arg="remote-log-format" typ="enum (default | syslog | cef)">
Format of the messages sent to the syslog server:
- `default` (default) - The topics and the message, `<topics> <message>`, without time or host name.
- `syslog` - BSD syslog (RFC 3164): `<PRI>` (facility and severity), the time, the router's identity and the message. `syslog-facility`, `syslog-severity`, `syslog-time-format` and `add-topics-string` apply to it.
- `cef` - Common Event Format: the time and the router's identity, then `CEF:0|MikroTik|<model>|<version>|` with the topics, a severity (`Low`, `Medium`, `High`) and the fields `dvchost`, `dvc` and `msg`, followed by the message's extra fields. Each message ends with `cef-event-delimiter`.
</ArgTableRow>
<ArgTableRow arg="remote-protocol" typ="enum (udp | tcp | tls)">
Transport to the syslog server. Every format works with every transport, and actions that send to the same address and port share one connection.
- `udp` (default) - One datagram per message. Messages sent while the server is unreachable are lost.
- `tcp` - A TCP connection. Up to 1000 messages logged while the server is unreachable, for all remote actions together, are kept in memory and sent when the connection is back; newer ones are dropped when the buffer is full. `default` and `syslog` messages have no delimiter in the stream; use `cef` over TCP.
- `tls` - The same as `tcp`, encrypted with TLS (`check-certificate`).
</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool">For `remote-protocol=tls`: whether to verify the server certificate against the trusted certificates in [`/certificate`](../../../certificate/). When the verification fails, the router does not send, logs `ssld,error client session, logging, remote IP: <address>, ssl: no trusted CA certificate found` and tries again later. The name in the certificate is not compared with the server address, so trust only the CA of your log servers. Default: no.</ArgTableRow>
<ArgTableRow arg="cef-event-delimiter" typ="string">Characters added at the end of every `cef` message, also over UDP. Default: `\r\n`.</ArgTableRow>
<ArgTableRow arg="syslog-time-format" typ="enum (bsd-syslog | iso8601)">
Time format of `syslog` messages:
- `bsd-syslog` (default) - `Oct  2 16:51:21`, the router's local time without the year.
- `iso8601` - `2026-10-02T16:51:21.726+03:00`, with milliseconds and the time zone offset.
</ArgTableRow>
<ArgTableRow arg="syslog-facility" typ="enum (kern | user | mail | daemon | auth | syslog | lpr | news | uucp | cron | authpriv | ftp | ntp | local0 | local1 | local2 | local3 | local4 | local5 | local6 | local7) { kern:0, user:1, mail:2, daemon:3, auth:4, syslog:5, lpr:6, news:7, uucp:8, cron:9, authpriv:10, ftp:11, ntp:12, local0:16, local1:17, local2:18, local3:19, local4:20, local5:21, local6:22, local7:23 }">
Facility in the `<PRI>` of `syslog` messages, with its code:
- `kern` (0)
- `user` (1)
- `mail` (2)
- `daemon` (3) (default)
- `auth` (4)
- `syslog` (5)
- `lpr` (6)
- `news` (7)
- `uucp` (8)
- `cron` (9)
- `authpriv` (10)
- `ftp` (11)
- `ntp` (12)
- `local0` to `local7` (16 to 23)
</ArgTableRow>
<ArgTableRow arg="syslog-severity" typ="enum (auto | emergency | alert | critical | error | warning | notice | info | debug) { auto:0xffffffff, emergency:0, alert:1, critical:2, error:3, warning:4, notice:5, info:6, debug:7 }">
Severity in the `<PRI>` of `syslog` messages. A value other than `auto` sends every message with that severity.
- `auto` (default) - Take the severity from the message topics: `debug` 7, `info` 6, `warning` 4, `error` 3. A message with both `error` and `critical` gets 3.
- `emergency` (0) - System is unusable.
- `alert` (1) - Action must be taken immediately.
- `critical` (2) - Critical conditions.
- `error` (3) - Error conditions.
- `warning` (4) - Warning conditions.
- `notice` (5) - Significant condition.
- `info` (6) - Informational message.
- `debug` (7) - Debug message.
</ArgTableRow>
<ArgTableRow arg="email-to" typ="string">Address the email action sends to. Each matching message is sent as its own email, with `<topics> <message>` as the subject and the body, through the SMTP server, port, TLS mode and sender set in [`/tool/e-mail`](../../../tool/e-mail/). See [Email](../../../../system-information-and-utilities/e-mail).</ArgTableRow>
<ArgTableRow arg="email-cc" typ="multi { array-id, cc: string
 }">Additional recipients of the email action, in the CC header. Several addresses are allowed.</ArgTableRow>
<ArgTableRow arg="email-start-tls" typ="bool">Not used by the email action: STARTTLS follows the `tls` setting in [`/tool/e-mail`](../../../tool/e-mail/). Default: no.</ArgTableRow>
<ArgTableRow arg="remember" typ="bool">For `target=echo`: keep the messages logged while no terminal session is open and print them at the next login, once. Default: yes.</ArgTableRow>
<ArgTableRow arg="add-topics-string" typ="bool">For `remote-log-format=syslog`: put the topics in front of the message, `<PRI><time> <identity> <topics> <message>`. The `default` format always contains the topics. Default: no.</ArgTableRow>
<ArgTableRow arg="script" typ="enum ()">For `target=script`: the script from [`/system/script`](../../script/) to run for each matching message. The script gets the variables `$topics` (the topics as text, for example `system,error,critical`) and `$message`. Messages that match while the script is still running are skipped, and a message the script logs itself does not run it again.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum ()">VRF the remote action connects from. Default: main.</ArgTableRow>
</ArgTable>
