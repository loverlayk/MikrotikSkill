# user-manager

> General settings of User Manager, the RADIUS server of RouterOS.

-----------

## user-manager 
**Package:** userman-5
**Type:** Settings Directory

General settings of User Manager, the RADIUS server of RouterOS.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Enables User Manager. Default: `no`.</ArgTableRow>
<ArgTableRow arg="authentication-port" typ="num">UDP port for authentication requests. Default: 1812.</ArgTableRow>
<ArgTableRow arg="accounting-port" typ="num">UDP port for accounting requests. Default: 1813.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">Server certificate for the EAP methods that use TLS (EAP-TLS, EAP-TTLS, EAP-PEAP). Default: `none`.</ArgTableRow>
<ArgTableRow arg="radsec-certificate" typ="enum (none)">Server certificate for routers that connect with RadSec. Default: `none`.</ArgTableRow>
<ArgTableRow arg="use-profiles" typ="bool">Uses profiles and limitations. With `yes`, a user without a valid profile is refused. With `no`, a user needs only a name and a password. Default: `no`.</ArgTableRow>
<ArgTableRow arg="require-message-auth" typ="enum (no | yes-access-request)">Whether an Access-Request must have the Message-Authenticator attribute: `yes-access-request` or `no`. Default: `yes-access-request`.</ArgTableRow>
</ArgTable>
