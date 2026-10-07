# send

> Sends one email message through the SMTP server in /tool/e-mail. Parameters given to the command override the server settings for this message. The result shows in last-status of /tool/e-mail. See Email.

-----------

## tool/e-mail/send 
**Type:** Command

Sends one email message through the SMTP server in [`/tool/e-mail`](.). Parameters given to the command override the server settings for this message. The result shows in `last-status` of `/tool/e-mail`. See [Email](../../../system-information-and-utilities/e-mail).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, fqdn: string
 }">SMTP server IP address, IPv6 address, or FQDN. If not specified, the value from the server configuration is used.</ArgTableRow>
<ArgTableRow arg="port" typ="num">SMTP server port. If not specified, the value from the server configuration is used.</ArgTableRow>
<ArgTableRow arg="to" typ="multi { array-id, to: string
 }">Destination email address. Several addresses are allowed, separated by commas; the router sends one message to all of them.</ArgTableRow>
<ArgTableRow arg="cc" typ="multi { array-id, cc: string
 }">Send a copy to listed recipients. Multiple addresses allowed, separated by commas.</ArgTableRow>
<ArgTableRow arg="from" typ="string">Name or email address that will appear as the sender. If not specified, the value from the server configuration is used; when that is empty too, the sender is `<>`, which many servers refuse.</ArgTableRow>
<ArgTableRow arg="subject" typ="string">The subject of the message.</ArgTableRow>
<ArgTableRow arg="body" typ="string">The body text of the email message. `\n` starts a new line.</ArgTableRow>
<ArgTableRow arg="file" typ="multi { array-id, file: file
 }">List of file names to attach to the email, separated by commas. Each file is attached as `application/octet-stream`. A file that does not exist is refused before sending (`input does not match any value of file`).</ArgTableRow>
<ArgTableRow arg="user" typ="string">Username used to authenticate to an SMTP server (AUTH PLAIN; unencrypted without TLS). If not specified, the value from the server configuration is used.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used to authenticate to an SMTP server. If not specified, the value from the server configuration is used.</ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)">
TLS encryption mode. If not specified, the value from the server configuration is used:
- `no` - No TLS. The router does not send STARTTLS, also when the server offers it.
- `yes` - TLS from the start of the connection (implicit TLS, usually port 465).
- `starttls` - Upgrade the connection with STARTTLS (usually port 587). When the server does not offer STARTTLS, the send fails with `TLS not supported by server`; there is no fallback to an unencrypted connection.
</ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">
TLS certificate validation. If not specified, the value from the server configuration is used:
- `no` - The router encrypts the connection but does not check the server's certificate.
- `yes` - Validates the certificate chain against the local certificate store, including the server name. The built-in trust store covers email by default.
- `yes-without-crl` - Validates the certificate without performing a CRL check.
</ArgTableRow>
</ArgTable>
