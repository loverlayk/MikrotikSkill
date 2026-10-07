# logging

> Rules that decide which log messages are kept and where they go. Each rule selects messages by their topics, and optionally by a regular expression, and passes them to an action from /system/logging/action. The...

-----------

## system/logging 
**Type:** Directory

Rules that decide which log messages are kept and where they go. Each rule selects messages by their topics, and optionally by a regular expression, and passes them to an action from [`/system/logging/action`](action/). The default rules pass `info`, `error` and `warning` messages to the `memory` action and `critical` messages to `echo`; other messages, for example `debug`, are not logged until a rule asks for them. See [Log](../../../diagnostics-monitoring-and-troubleshooting/log/).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The rule is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The rule is invalid.</ArgTableRow>
<ArgTableRow arg="*" typ="default">One of the four default rules: `info`, `error` and `warning` to `memory`, `critical` to `echo`.</ArgTableRow>
<ArgTableRow arg="Y" typ="managed"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="topics" typ="multi { array-id, array-id, topic: super { !
, topic: enum
 }
 }">
Topics a message must carry to match. A message matches only when it has every topic listed: `topics=dhcp,debug` matches DHCP debug messages, not all DHCP messages and all debug messages. To log several topics, add one rule per topic. A rule without topics matches every message, debug messages included.

`!` before a topic excludes the messages that carry it, for example `topics=ntp,debug,!packet` logs NTP debug messages without the packet dumps. The topics are described on the [Log](../../../diagnostics-monitoring-and-troubleshooting/log/#topics) page. The router accepts: `account`, `acme-client`, `amt`, `async`, `backup`, `bfd`, `bgp`, `bridge`, `calc`, `caps`, `certificate`, `clock`, `container`, `critical`, `ddns`, `debug`, `dhcp`, `discover`, `disk`, `dns`, `dot1x`, `dude`, `e-mail`, `error`, `event`, `evpn`, `fetch`, `firewall`, `gps`, `gsm`, `health`, `hotspot`, `igmp-proxy`, `info`, `interface`, `ipsec`, `iscsi`, `isdn`, `isis`, `kvm`, `l2tp`, `ldp`, `lora`, `lte`, `manager`, `mme`, `mpls`, `mqtt`, `mvrp`, `natpmp`, `netinstall`, `netwatch`, `ntp`, `ospf`, `ovpn`, `packet`, `pim`, `poe-in`, `poe-out`, `pon`, `ppp`, `pppoe`, `pptp`, `ptp`, `queue`, `radius`, `radvd`, `raw`, `read`, `rip`, `route`, `rpki`, `rproxy`, `rsvp`, `script`, `sertcp`, `simulator`, `smb`, `snmp`, `socksify`, `ssh`, `ssld`, `sstp`, `state`, `store`, `stp`, `system`, `telephony`, `tftp`, `timer`, `tr069`, `update`, `upnp`, `ups`, `vpls`, `vrrp`, `warning`, `watchdog`, `web-proxy`, `wiliot`, `wireguard`, `wireless`, `write`, `zerotier`.
</ArgTableRow>
<ArgTableRow arg="prefix" typ="string">Text added in front of every message the rule passes, as `<prefix>: <message>`. The prefix is part of the stored and of the sent message.</ArgTableRow>
<ArgTableRow arg="regex" typ="string">Regular expression matched against the message text, followed by the message's extra fields. When it does not match, the rule does not pass the message, even when the topics match.</ArgTableRow>
<ArgTableRow arg="action" typ="enum">Action from [`/system/logging/action`](action/) that receives the matching messages. Every rule that matches passes the message to its own action; when two rules pass the same message to one action, the action receives it once. Default: memory.</ArgTableRow>
</ArgTable>
