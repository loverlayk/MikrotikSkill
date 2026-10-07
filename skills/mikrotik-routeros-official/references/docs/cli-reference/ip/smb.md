# smb

> RouterOS settings reference for /ip/smb.

-----------

## ip/smb 
**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (no | auto | yes)">
Whether the built-in SMB server runs:
- `no` - the server is disabled.
- `auto` (default) - the server starts automatically when the first non-disabled share is configured in [`shares`](shares).
- `yes` - the server is enabled.
</ArgTableRow>
<ArgTableRow arg="domain" typ="string">Name of the Windows workgroup the SMB server belongs to. Default: MSHOME.</ArgTableRow>
<ArgTableRow arg="comment" typ="string">Comment of the SMB server. Default: MikrotikSMB.</ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum { all:0 }
 }">Interfaces on which the SMB service listens. Default: all.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">Actual state of the SMB server, for example `enabled`.</ArgTableRow>
</ArgTable>
