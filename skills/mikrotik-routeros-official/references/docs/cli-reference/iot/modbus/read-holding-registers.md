# read-holding-registers

> RouterOS command reference for /iot/modbus/read-holding-registers.

-----------

## iot/modbus/read-holding-registers 
**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="slave-id" typ="num"></ArgTableRow>
<ArgTableRow arg="reg-addr" typ="num"></ArgTableRow>
<ArgTableRow arg="num-regs" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="values" typ="multi { array-id, value: num
 }"></ArgTableRow>
</ArgTable>
