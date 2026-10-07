# lte

> RouterOS directory reference for /interface/lte.

-----------

## interface/lte 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="master" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
<ArgTableRow arg="apn-profiles" typ="enum" deprecated="1"></ArgTableRow>
<ArgTableRow arg="apn-profile" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="modem-init" typ="string">string to send upon modem initialization</ArgTableRow>
<ArgTableRow arg="operator" typ="string">operator locking, use numeric value: mccmnc</ArgTableRow>
<ArgTableRow arg="allow-roaming" typ="bool"></ArgTableRow>
<ArgTableRow arg="sms-read" typ="bool">This setting is ignored if any interface is enabled in /tool/sms</ArgTableRow>
<ArgTableRow arg="sms-protocol" typ="enum (mbim | at | qmi | auto)"></ArgTableRow>
<ArgTableRow arg="network-mode" typ="multi { array-id, network: enum
 }"></ArgTableRow>
<ArgTableRow arg="band" typ="multi { array-id, band: enum
 }">LTE band</ArgTableRow>
<ArgTableRow arg="nr-band" typ="multi { array-id, nr-band: enum
 }">NR band</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="advertised-mtu" typ="num"></ArgTableRow>
</ArgTable>
