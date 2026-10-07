# sms

> RouterOS settings reference for /tool/sms.

-----------

## tool/sms 
**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="receive-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { serial: enum
, interface: iface_enum { none }
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
<ArgTableRow arg="allowed-number" typ="multi { array-id, number: string
 }"></ArgTableRow>
<ArgTableRow arg="sim-pin" typ="string"></ArgTableRow>
<ArgTableRow arg="sms-storage" typ="enum (modem | sim)">Memory for reading, writing, sending and receiving operations (`<mem1>`, `<mem2>` and `<mem3>` in ETSI TS 127 005), will be used in further +CPMS commands (setting effective when using AT commands only)</ArgTableRow>
<ArgTableRow arg="polling" typ="bool">Poll new SMS every 5s. It's recommended to enable polling only when there are problems with receiving new SMS otherwise.</ArgTableRow>
<ArgTableRow arg="remove-sent-sms-after-send" typ="bool">Useful when modem automatically stores sent SMS</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (off | running)"></ArgTableRow>
<ArgTableRow arg="last-ussd" typ="string"></ArgTableRow>
</ArgTable>
