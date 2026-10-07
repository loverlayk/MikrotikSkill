# profile

> RouterOS directory reference for /ip/hotspot/profile.

-----------

## ip/hotspot/profile 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="hotspot-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dns-name" typ="string"></ArgTableRow>
<ArgTableRow arg="html-directory" typ="file"></ArgTableRow>
<ArgTableRow arg="html-directory-override" typ="file"></ArgTableRow>
<ArgTableRow arg="install-hotspot-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="http-proxy" typ="composite { address: ipAddr
, port: num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="smtp-server" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="login-by" typ="ubit (mac, cookie, http-chap, https, http-pap, trial, mac-cookie)"></ArgTableRow>
<ArgTableRow arg="mac-auth-mode" typ="enum (mac-as-username | mac-as-username-and-password) { mac-as-username:0, mac-as-username-and-password:1 }"></ArgTableRow>
<ArgTableRow arg="mac-auth-password" typ="string"></ArgTableRow>
<ArgTableRow arg="http-cookie-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="ssl-certificate" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="split-user-domain" typ="bool"></ArgTableRow>
<ArgTableRow arg="trial-uptime-limit" typ="time"></ArgTableRow>
<ArgTableRow arg="trial-uptime-reset" typ="time"></ArgTableRow>
<ArgTableRow arg="trial-user-profile" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="radius-accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="radius-interim-update" typ="alt { symbolic-names: enum (received) { received:0 }
, time-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="nas-port-type" typ="enum (ethernet | cable | wireless-802.11) { ethernet:15, cable:17, wireless-802.11:19 }"></ArgTableRow>
<ArgTableRow arg="radius-default-domain" typ="string"></ArgTableRow>
<ArgTableRow arg="radius-location-id" typ="string"></ArgTableRow>
<ArgTableRow arg="radius-location-name" typ="string"></ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XXXX:XXXX:XXXX | XXXXXX:XXXXXX | XX-XX-XX-XX-XX-XX | XXXXXX-XXXXXX | XXXXXXXXXXXX | XX XX XX XX XX XX) { XX:XX:XX:XX:XX:XX:0, XXXX:XXXX:XXXX:1, XXXXXX:XXXXXX:2, XX-XX-XX-XX-XX-XX:3, XXXXXX-XXXXXX:4, XXXXXXXXXXXX:5, XX XX XX XX XX XX:6 }"></ArgTableRow>
</ArgTable>
