# push-button

> Using this command device pairing can be performed using physical routerboard/reset button on the client device.

-----------

## cmr/client/push-button 
**Type:** Command

Using this command device pairing can be performed using physical routerboard/reset button on the client device.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }" unset="1">Select inteface or interface list on which to search for CMR server. (default value: **all**)</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="string">State of device pairing.</ArgTableRow>
<ArgTableRow arg="error" typ="string" unset="1">Error information, in case pairing is unsuccessfull.</ArgTableRow>
<ArgTableRow arg="peer" typ="multi { array-id, mac: macAddr
 }" unset="1">CMR server address.</ArgTableRow>
<ArgTableRow arg="peer-id" typ="string" unset="1">CMR server ID.</ArgTableRow>
</ArgTable>
