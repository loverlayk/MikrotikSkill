# incoming

> Settings for the Disconnect and Change of Authorization (CoA) requests that RADIUS servers send to the router. See RADIUS for the full guide.

-----------

## radius/incoming 
**Type:** Settings Directory

Settings for the Disconnect and Change of Authorization (CoA) requests that RADIUS servers send to the router. See [RADIUS](../../../authentication-authorization-accounting/radius) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="accept" typ="bool">Whether the router accepts Disconnect and CoA requests. The request must be signed with the shared secret of the first `/radius` entry whose address is the source address of the request. Default: no.</ArgTableRow>
<ArgTableRow arg="port" typ="num">UDP port on which the router listens for the requests. Default: 3799.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF in which the router listens for the requests. Requests that arrive in another VRF are not answered. Default: main.</ArgTableRow>
</ArgTable>
