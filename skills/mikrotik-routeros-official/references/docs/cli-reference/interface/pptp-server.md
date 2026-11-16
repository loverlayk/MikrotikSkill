# pptp-server

> PPTP server interfaces exist for each connected or configured client. Dynamic entries (D) are created for connected users; static entries keep a name for firewall rules.

-----------

## interface/pptp-server 
**Type:** Directory

[PPTP](../../../virtual-private-networks/pptp) server interfaces exist for each connected or configured client. Dynamic entries (`D`) are created for connected users; static entries keep a name for firewall rules.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the server interface was created dynamically for a connected user.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running, which means the client is connected.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name. Static entries use this name; dynamic entries are named `<pptp-<username>>`.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">User name used for authentication. The user must exist in `/ppp/secret` or RADIUS; the entry only names the interface.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mtu" typ="num">Negotiated MTU of the connection.</ArgTableRow>
<ArgTableRow arg="mru" typ="num">Negotiated MRU of the connection.</ArgTableRow>
<ArgTableRow arg="client-address" typ="string">IPv4 address of the connected client.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Connection uptime.</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">Encryption encoding used. Empty when the PPP profile does not encrypt.</ArgTableRow>
</ArgTable>
