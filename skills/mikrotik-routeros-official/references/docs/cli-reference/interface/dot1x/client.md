# client

> Ports where the router is an 802.1X supplicant and authenticates to the network.

-----------

## interface/dot1x/client 
**Conditions:** !smips
**Type:** Directory

Ports where the router is an 802.1X supplicant and authenticates to the network.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Ethernet interface of the client.</ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { method: enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2) { eap-tls:13, eap-ttls:21, eap-peap:25, eap-mschapv2:26 }
 }" mandatory="1">EAP methods of the client: `eap-mschapv2`, `eap-peap`, `eap-ttls`, `eap-tls`. Several methods can be listed.</ArgTableRow>
<ArgTableRow arg="identity" typ="string" mandatory="1">User name of the client.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password of the client. Not used with `eap-tls`.</ArgTableRow>
<ArgTableRow arg="anon-identity" typ="string">Name for the outer authentication of `eap-peap` and `eap-ttls`. When empty, `identity` is used.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">Client certificate with a private key, for `eap-tls`. Default: `none`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">
- `authenticated` - the authentication succeeded.
- `authenticating` - the authenticator is reached and the authentication is in progress.
- `rejected` - the server refused the client.
- `disabled` - the client is disabled.
- `interface is down` - the interface is not running.
- `error` - an internal error.
</ArgTableRow>
</ArgTable>
