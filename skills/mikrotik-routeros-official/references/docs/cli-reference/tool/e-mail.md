# e-mail

> Settings of the SMTP server the router sends email through: the server and port, the TLS mode, certificate verification, the sender and the login. /tool/e-mail/send uses them for every message unless the command...

-----------

## tool/e-mail 
**Type:** Settings Directory

Settings of the SMTP server the router sends email through: the server and port, the TLS mode, certificate verification, the sender and the login. `/tool/e-mail/send` uses them for every message unless the command overrides them. See [Email](../../../system-information-and-utilities/e-mail).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, fqdn: string
 }">SMTP server IP address, IPv6 address, or FQDN. With a name, `last-address` shows the address the router connected to. Default: 0.0.0.0.</ArgTableRow>
<ArgTableRow arg="port" typ="num">SMTP server port. Default: 25.</ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)">
TLS encryption mode:
- `no` (default) - No TLS. The router does not send STARTTLS, also when the server offers it.
- `yes` - TLS from the start of the connection (implicit TLS, usually port 465).
- `starttls` - Upgrade the connection with STARTTLS (usually port 587). When the server does not offer STARTTLS, the send fails with `TLS not supported by server`; there is no fallback to an unencrypted connection.
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF on which the service creates outgoing connections. Default: main.</ArgTableRow>
<ArgTableRow arg="from" typ="string">Name or email address that will be shown as the sender. When it is empty, the router sends the message with an empty sender (`<>`), which many servers refuse. Default: &lt;&gt;.</ArgTableRow>
<ArgTableRow arg="user" typ="string">Username used for authenticating to an SMTP server. The router logs in with AUTH PLAIN; without TLS, the user name and password cross the network unencrypted. Default: "".</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used for authenticating to an SMTP server. Default: "".</ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">
TLS certificate validation:
- `no` (default) - The router encrypts the connection but does not check the server's certificate.
- `yes` - Validates the certificate chain against the local certificate store, including the server name. The built-in trust store covers email by default.
- `yes-without-crl` - Validates the certificate without performing a CRL check.
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-status" typ="enum (none | resolving-dns | in-progress | failed | succeeded)">Status of the last email send attempt: `succeeded` or `failed` when it has ended.</ArgTableRow>
<ArgTableRow arg="last-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">IP address of the last used SMTP server.</ArgTableRow>
</ArgTable>
