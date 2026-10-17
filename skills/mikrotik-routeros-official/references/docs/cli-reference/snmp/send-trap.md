# send-trap

> The send-trap command sends one SNMP trap to the configured trap target immediately, which is useful for testing that traps reach the collector. The trap uses the trap-target, trap-community, and trap-version...

-----------

## snmp/send-trap 
**Type:** Command

The `send-trap` command sends one SNMP trap to the configured trap target immediately, which is useful for testing that traps reach the collector. The trap uses the `trap-target`, `trap-community`, and `trap-version` settings of the SNMP service (with `trap-version=1` it is a classic v1 enterprise trap; otherwise it carries the OID and value under the MikroTik trap OID `1.3.6.1.4.1.14988.1.1.9.0.1`). See the [SNMP guide](../../diagnostics-monitoring-and-troubleshooting/snmp) for the trap configuration.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="oid" typ="string">OID of the object the trap reports.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (integer | string | nullobj | obj-id | ip-address | counter32 | timeticks | unsigned) { integer:0x02, string:0x04, nullobj:0x05, obj-id:0x06, ip-address:0x40, counter32:0x41, timeticks:0x43, unsigned:0x47 }">
SNMP type of the value. Accepted values:
- `integer` - A signed integer.
- `string` - An octet string.
- `nullobj` - A NULL value.
- `obj-id` - An object identifier.
- `ip-address` - An IP address.
- `counter32` - A 32-bit counter.
- `timeticks` - A time in hundredths of a second.
- `unsigned` - An unsigned integer.
</ArgTableRow>
<ArgTableRow arg="value" typ="string">Value to send, in the format the selected `type` expects.</ArgTableRow>
</ArgTable>
