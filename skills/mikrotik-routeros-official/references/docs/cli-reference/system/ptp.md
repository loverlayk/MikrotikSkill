# ptp

> RouterOS directory reference for /system/ptp.

-----------

## system/ptp 
**Conditions:** !smips
**Syscap:** ptp
**Type:** Directory
PTP (IEEE 1588-2008, PTPv2) instance configuration. Each entry is one PTP profile instance; ports join it in [`/system/ptp/port`](port). Supported only on specific switch/router hardware (see the [Precision Time Protocol](../../../system-information-and-utilities/precision-time-protocol) guide).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the PTP profile instance</ArgTableRow>
<ArgTableRow arg="priority1" typ="enum (auto) { auto:0 }">First value of the grandmaster election; the lower value wins. With `auto`, the value of the chosen profile applies (802.1AS: 246, other profiles: 128)</ArgTableRow>
<ArgTableRow arg="priority2" typ="enum (auto)">Second value of the grandmaster election, used for ties. With `auto`, the value of the chosen profile applies (802.1AS: 248, other profiles: 128)</ArgTableRow>
<ArgTableRow arg="delay-mode" typ="enum (auto | e2e | p2p)">Delay measurement mechanism: `e2e` (request-response) or `p2p` (peer delay). With `auto`, the profile default applies (802.1AS: p2p, other profiles: e2e)</ArgTableRow>
<ArgTableRow arg="transport" typ="enum (auto | ipv4 | l2-non-forwardable | l2-forwardable)">Transport used for PTP messages: `ipv4` (multicast 224.0.1.129 for PTP primary messages and 224.0.0.107 for peer delay messages), `l2-forwardable` (multicast MAC 01-1B-19-00-00-00, forwarded by PTP-unaware bridges) or `l2-non-forwardable` (01-80-C2-00-00-0E, not forwarded by compliant bridges). With `auto`, the profile default applies (802.1AS and G.8275.1 use `l2-non-forwardable`; AES67, SMPTE and the default profile use `ipv4`)</ArgTableRow>
<ArgTableRow arg="profile" typ="enum (default | 802.1as | g8275.1 | aes67 | smpte-2059)">Operating profile: `default` (plain PTPv2), `802.1as` (AVB/TSN, IEEE 802.1AS-2020), `aes67` (audio over IP), `g8275.1` (telecom frequency and phase), `smpte-2059` (professional broadcast). The profile also presets the auto values of domain, priority1/2, transport and delay-mode</ArgTableRow>
<ArgTableRow arg="domain" typ="enum (auto)">PTP domain number separating independent PTP instances on one network. Allowed ranges differ per profile (0-127 for most, 24-43 for G.8275.1). With `auto`, the profile default applies (default profile/AES67: 0, G.8275.1: 24, SMPTE: 127)</ArgTableRow>
<ArgTableRow arg="ptp-mode" typ="enum (ordinary-clock | transparent-clock)">Clock mode of the instance: an ordinary clock (end device; grandmaster or slave) or a transparent clock (measures and forwards residence time without acting as an end device)</ArgTableRow>
</ArgTable>
