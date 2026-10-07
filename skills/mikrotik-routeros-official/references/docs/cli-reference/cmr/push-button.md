# push-button

> Using this command device pairing can be performed using physical routerboard/reset button on the server device.

-----------

## cmr/push-button 
**Type:** Command

Using this command device pairing can be performed using physical routerboard/reset button on the server device.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }" unset="1">Select interface or interface list on which to search for CMR client. Default: all.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="string">State of device pairing.</ArgTableRow>
<ArgTableRow arg="error" typ="string" unset="1">Error information, in case pairing is unsuccessful.</ArgTableRow>
<ArgTableRow arg="peer" typ="multi { array-id, mac: macAddr
 }" unset="1">Peer address.</ArgTableRow>
<ArgTableRow arg="peer-id" typ="string" unset="1">Peer ID.</ArgTableRow>
</ArgTable>
