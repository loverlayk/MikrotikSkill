# state

> State of each Dot1X server port.

-----------

## interface/dot1x/server/state 
**Conditions:** !smips
**Type:** Directory

State of each Dot1X server port.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Port.</ArgTableRow>
<ArgTableRow arg="status" typ="string">
- `authorized` - the port passes traffic.
- `un-authorized` - no device is authenticated, the port passes only EAPOL frames.
- `rejected-holding` - the RADIUS server rejected the device.
- `iface-down` - the interface is not running.
</ArgTableRow>
</ArgTable>
