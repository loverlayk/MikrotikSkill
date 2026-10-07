# used

> Menu lists all used IP addresses from IP pools.

-----------

## ip/pool/used 
**Type:** Directory

Menu lists all used IP addresses from IP pools.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="pool" typ="enum">Name of the IP pool.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">IP address that is assigned to a client from the pool.</ArgTableRow>
<ArgTableRow arg="owner" typ="string">Name of the service which acquired this IP address.</ArgTableRow>
<ArgTableRow arg="info" typ="string">Additional info, for example, for DHCP - MAC address from the leases menu and for PPP - connections username of a PPP type client.</ArgTableRow>
</ArgTable>
