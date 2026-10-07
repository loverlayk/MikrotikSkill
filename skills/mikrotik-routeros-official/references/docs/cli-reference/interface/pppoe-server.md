# pppoe-server

> There are two types of interface (tunnel) items in PPPoE server configuration - static users and dynamic connections. An interface is created for each tunnel established to the given server. Static interfaces are...

-----------

## interface/pppoe-server 
**Type:** Directory

There are two types of interface (tunnel) items in PPPoE server configuration - static users and dynamic connections. An interface is created for each tunnel established to the given server. Static interfaces are added administratively if there is a need to reference the particular interface name (in firewall rules or elsewhere) created for the particular user. Dynamic interfaces are added to this list automatically whenever a user is connected and the user's username does not match any existing static entry (or in case the entry is active already, as there can not be two separate tunnel interfaces referenced by the same name - set the *one-session-per-host* value if this is a problem). Dynamic interfaces appear when a user connects and disappear once the user disconnects, so it is impossible to reference the tunnel created for that user in the router configuration (for example, in firewall), so if you need a persistent rule for that user, create a static entry for him/her. Otherwise, it is safe to use a dynamic configuration.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the server interface was created dynamically.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">Username used for authentication.</ArgTableRow>
<ArgTableRow arg="service" typ="string" mandatory="1">PPPoE service name.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mtu" typ="num">Current MTU of the connection.</ArgTableRow>
<ArgTableRow arg="mru" typ="num">Current MRU of the connection.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="string">Remote IP address of the connection.</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">Encryption encoding used.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Connection uptime.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Interface the client is connected through.</ArgTableRow>
<ArgTableRow arg="vid" typ="num">VLAN ID of the connection.</ArgTableRow>
</ArgTable>
