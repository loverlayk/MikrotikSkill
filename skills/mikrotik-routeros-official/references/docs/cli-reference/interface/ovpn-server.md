# ovpn-server

> An interface is created for each tunnel established to the specified server. There are two types of interfaces in the OVPN server configuration:

-----------

## interface/ovpn-server 
**Type:** Directory

An interface is created for each tunnel established to the specified server. There are two types of interfaces in the OVPN server configuration:

- Static interfaces are added administratively when you need to reference a specific interface name (for example, in firewall rules or elsewhere) created for a particular user.
- Dynamic interfaces are added to this list automatically when a user connects and their username does not match any existing static entry, or if the matching static entry is already active, since two separate tunnel interfaces cannot use the same name.

Dynamic interfaces appear when a user connects and disappear when the user disconnects. Therefore, it is not possible to reference the tunnel created for that user in router configuration (for example, in firewall rules). If persistent rules are required for a user, create a static entry. Otherwise, dynamic configuration is sufficient.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the server interface was created dynamically.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">Whether hardware encryption is active.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">User name used for authentication.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mtu" typ="num">Current MTU of the connection.</ArgTableRow>
<ArgTableRow arg="client-address" typ="string">IP address of the connected client.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Connection uptime.</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">Encryption encoding used.</ArgTableRow>
</ArgTable>
