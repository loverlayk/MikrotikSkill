# scan

> PPPoE Scanner allows scanning all active PPPoE servers in the layer2 broadcast domain.

-----------

## interface/pppoe-client/scan 
**Type:** Command

PPPoE Scanner allows scanning all active PPPoE servers in the layer2 broadcast domain.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface to scan for PPPoE servers on.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="service" typ="string">Service name configured on the server.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the detected server.</ArgTableRow>
<ArgTableRow arg="ac-name" typ="string">Name of the Access Concentrator.</ArgTableRow>
</ArgTable>
