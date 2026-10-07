# ssh-exec

> The ssh-exec command is a non-interactive SSH command, allowing you to execute commands remotely on a device through scripts and scheduler.

-----------

## system/ssh-exec 
**Type:** Command

The [`ssh-exec`](../../management-tools/ssh#run-remote-commands-from-scripts) command is a non-interactive SSH command, allowing you to execute commands remotely on a device through scripts and scheduler.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ipv6-address: composite { ip6: ip6Addr
, interface: [ iface_enum]
 }
 }">Remote host IPv4 or IPv6 address.</ArgTableRow>
<ArgTableRow arg="command" typ="string">Remote command to execute.</ArgTableRow>
<ArgTableRow arg="user" typ="string">Username for the remote host.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password for the remote host. You should use SSH PKI authentication instead of plain text passwords.</ArgTableRow>
<ArgTableRow arg="port" typ="num">TCP port the SSH server listens on. Default: 22.</ArgTableRow>
<ArgTableRow arg="known-hosts-ignore" typ="bool">skip host key validation</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">Source address to use when connecting. Supports both IPv4 and IPv6.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF to run the command over; the connection is made inside that routing table.</ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">Write output to file instead of 'output' variable.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="exit-code" typ="num">Exit code reported by the remote command shell; `0` when the command ran. A connection or authentication failure aborts `ssh-exec` itself instead of returning.</ArgTableRow>
<ArgTableRow arg="output" typ="string">Returns the output of the remotely executed command.</ArgTableRow>
</ArgTable>
