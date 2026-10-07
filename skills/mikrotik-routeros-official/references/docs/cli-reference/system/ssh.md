# ssh

> SSH client to connect to remote hosts.

-----------

## system/ssh 
**Type:** Command

[SSH client](../../management-tools/ssh#ssh-client) to connect to remote hosts.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ipv6-address: composite { ip6: ip6Addr
, interface: [ iface_enum]
 }
 }">Remote host IPv4 or IPv6 address.</ArgTableRow>
<ArgTableRow arg="command" typ="string">Remote command to execute.</ArgTableRow>
<ArgTableRow arg="user" typ="string">Username for the remote host. Defaults to the currently logged-in user.</ArgTableRow>
<ArgTableRow arg="port" typ="num">TCP port the SSH server listens on. Default: 22.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">Source address to use when connecting. Supports both IPv4 and IPv6.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF to make the connection in. Matches the remote host only inside that routing table.</ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">Write output to file instead of terminal. Does not accept password input, use key authentication.</ArgTableRow>
</ArgTable>
