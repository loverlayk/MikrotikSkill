# network

> RouterOS directory reference for /app/network.

-----------

## app/network 
**Syscap:** app
**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="e" typ="external">The network is an existing bridge or the LAN bridge.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The network configuration is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Network name. `internal` is the app-created network; external networks use the bridge name and the `lan` alias.</ArgTableRow>
<ArgTableRow arg="allow-outgoing-access" typ="bool">Whether apps on the network can reach destinations outside it. Default: yes.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="network" typ="ipAddr">Network address of the app-created internal network.</ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr">Router IP address on the network.</ArgTableRow>
<ArgTableRow arg="status" typ="string">Current network state, such as `ready`.</ArgTableRow>
<ArgTableRow arg="used-ips" typ="multi { array-id, array-id, ip-and-name: composite { ip: ipAddr
, name: string
 }
 }">IP addresses allocated on the network and the app or host that uses each one.</ArgTableRow>
<ArgTableRow arg="bridge-interface" typ="iface_enum { none }">Bridge interface that carries the network.</ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { cmd: string
 }">Commands that RouterOS used to create the network.</ArgTableRow>
</ArgTable>
