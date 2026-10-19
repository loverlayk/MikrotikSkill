# raw-packet-template

> RouterOS directory reference for /tool/traffic-generator/raw-packet-template.

-----------

## tool/traffic-generator/raw-packet-template 
**Type:** Directory
Builds packet content from a raw header string. Use this when you need low-level packets that the packet-template builder cannot express. See the [Traffic Generator](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the RAW packet template.</ArgTableRow>
<ArgTableRow arg="port" typ="enum">Name of the port (from the port menu) the packets are sent out through.</ArgTableRow>
<ArgTableRow arg="header" typ="string">RAW packet header as a hexadecimal string; it fully defines the header stack.</ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing) { uninitialized:0, random:1, specific-byte:2, incrementing:3 }">How the packet payload (after the header) is filled: uninitialized (not zeroed; fastest), specific-byte (with data-byte), incrementing (bytes 00 01 02 ...), random (random bytes; slowest).</ArgTableRow>
<ArgTableRow arg="data-byte" typ="num">Byte used to fill the payload when data=specific-byte.</ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, offset-and-mask: composite { offset: num [ .. 256]
, mask: num [ .. 255]
 }
 }">Byte offsets in the packet, each with a bit mask, that are filled with random values.</ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { random-range: super { offset: num [ .. 256]
, [width] :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, [range] :range
 }
 }">Fields at given byte offsets that are filled with random values: `width` sets the field size (8, 16 or 32 bits) and `range` the range of the values.</ArgTableRow>
<ArgTableRow arg="ip-header-offset" typ="multi { ip-header-offset: num [ .. 65535]
 }">Byte offset of the IPv4 header within the packet, so the generator can locate and parse it.</ArgTableRow>
<ArgTableRow arg="ipv6-header-offset" typ="multi { ipv6-header-offset: num [ .. 65535]
 }">Byte offset of the IPv6 header within the packet.</ArgTableRow>
<ArgTableRow arg="udp-header-offset" typ="multi { udp-header-offset: num [ .. 65535]
 }">Byte offset of the UDP header within the packet.</ArgTableRow>
<ArgTableRow arg="udp-compute-checksum" typ="multi { udp-compute-checksum: bool
 }">Whether the UDP checksum is computed by the generator.</ArgTableRow>
<ArgTableRow arg="tcp-header-offset" typ="multi { tcp-header-offset: num [ .. 65535]
 }">Byte offset of the TCP header within the packet.</ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool">Whether a special footer is appended to the generated packets.</ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num">Byte offset from which the 2-byte checksum is calculated; for example 14 skips the Ethernet header. no-checksum disables the checksum.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="header-length" typ="num">Total length of the packet header in bytes.</ArgTableRow>
</ArgTable>
