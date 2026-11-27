# profile

> The /ip/hotspot/profile menu lists the server profiles. A profile holds the settings that HotSpot servers share: the address and DNS name of the login page, the login methods, the HTML directory, and the RADIUS...

-----------

## ip/hotspot/profile 
**Type:** Directory

The `/ip/hotspot/profile` menu lists the server profiles. A profile holds the settings that HotSpot servers share: the address and DNS name of the login page, the login methods, the HTML directory, and the RADIUS settings. See the [HotSpot](../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">The default profile. It cannot be removed.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the profile.</ArgTableRow>
<ArgTableRow arg="hotspot-address" typ="ipAddr">IP address of the HotSpot service, which is the address of the login page.</ArgTableRow>
<ArgTableRow arg="dns-name" typ="string">DNS name of the login page. The router resolves this name to the HotSpot address for the clients. Empty - the login page uses the IP address.</ArgTableRow>
<ArgTableRow arg="html-directory" typ="file">Directory with the HotSpot pages. Default: `hotspot`, or `flash/hotspot` on a router that has a `flash` folder in its file list.</ArgTableRow>
<ArgTableRow arg="html-directory-override" typ="file">Directory with your own HotSpot pages. If it is set and exists, it is used instead of `html-directory`. On a router that has a `flash` folder in its file list, keep the directory in `flash` and set the path with the folder, for example `flash/hs-custom`: files outside `flash` are lost on reboot.</ArgTableRow>
<ArgTableRow arg="install-hotspot-queue" typ="bool">Whether to create a dynamic simple queue for the HotSpot interface of each server with this profile. The queue uses the `hotspot-default` queue type. Default: `no`.</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">Rate limit in the form `rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]]`. `rx` is what the router receives from the user (upload), `tx` is what it sends to the user (download). For example, `512k/2M` limits upload to 512 kbps and download to 2 Mbps. The limit applies to all users of the servers with this profile together.</ArgTableRow>
<ArgTableRow arg="http-proxy" typ="composite { address: ipAddr
, port: num [0 .. 65535]
 }">Address and port of a proxy server for the HTTP requests of the clients. `0.0.0.0:0` - no proxy.</ArgTableRow>
<ArgTableRow arg="smtp-server" typ="ipAddr">Server to which the SMTP connections (TCP port 25) of the clients are redirected. `0.0.0.0` - no redirect.</ArgTableRow>
<ArgTableRow arg="login-by" typ="ubit (mac, cookie, http-chap, https, http-pap, trial, mac-cookie)">
Login methods that the servers with this profile accept. Default: `cookie,http-chap`.
- `http-chap` - user name and password on the login page; the password is sent as an MD5 hash with a challenge
- `http-pap` - user name and password on the login page; the password is sent as plain text
- `https` - user name and password on the login page over HTTPS; needs `ssl-certificate`
- `cookie` - automatic login with a browser cookie from an earlier login
- `mac` - automatic login when a user with the MAC address of the device as its name exists
- `mac-cookie` - automatic login by the MAC address of a device that has logged in before
- `trial` - login without an account for a limited time
</ArgTableRow>
<ArgTableRow arg="mac-auth-mode" typ="enum (mac-as-username | mac-as-username-and-password) { mac-as-username:0, mac-as-username-and-password:1 }">What is sent for a `mac` login: `mac-as-username` - the MAC address as the user name, with `mac-auth-password` as the password; `mac-as-username-and-password` - the MAC address as both.</ArgTableRow>
<ArgTableRow arg="mac-auth-password" typ="string">Password for `mac` logins. Use it when the RADIUS server rejects users with an empty password.</ArgTableRow>
<ArgTableRow arg="http-cookie-lifetime" typ="time">Time for which the cookie of the `cookie` login method is valid. Default: `3d`.</ArgTableRow>
<ArgTableRow arg="ssl-certificate" typ="enum (none) { none:0 }">Certificate for the `https` login method. It has to be valid for the `dns-name` of the profile. Default: `none`.</ArgTableRow>
<ArgTableRow arg="split-user-domain" typ="bool">Whether to split a user name given as `user@domain` or `domain\user` into the user name and the domain. Default: `no`.</ArgTableRow>
<ArgTableRow arg="trial-uptime-limit" typ="time">Time for which a trial user has access. Default: `30m`.</ArgTableRow>
<ArgTableRow arg="trial-uptime-reset" typ="time">Time after which a device can use the trial again. Default: `1d`.</ArgTableRow>
<ArgTableRow arg="trial-user-profile" typ="enum ()">User profile from `/ip/hotspot/user/profile` for trial users. Default: `default`.</ArgTableRow>
<ArgTableRow arg="use-radius" typ="bool">Whether to authenticate users that are not in `/ip/hotspot/user` on a RADIUS server. The server is set in `/radius` with `service=hotspot`. Default: `no`.</ArgTableRow>
<ArgTableRow arg="radius-accounting" typ="bool">Whether to send accounting records for the sessions to the RADIUS server. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="radius-interim-update" typ="alt { symbolic-names: enum (received) { received:0 }
, time-interval: time
 }">Interval of the accounting updates. `received` - the interval that the RADIUS server sends is used.</ArgTableRow>
<ArgTableRow arg="nas-port-type" typ="enum (ethernet | cable | wireless-802.11) { ethernet:15, cable:17, wireless-802.11:19 }">Value of the NAS-Port-Type attribute sent to the RADIUS server. Default: `wireless-802.11`.</ArgTableRow>
<ArgTableRow arg="radius-default-domain" typ="string">Domain for the RADIUS requests of this profile. Set the same value as `domain` of a server in `/radius` to use a separate RADIUS server for the profile. All logins of the profile go to that server, also names with another domain. The name is sent as the user typed it, and the domain is in the MS-CHAP-Domain and Mikrotik-Realm attributes.</ArgTableRow>
<ArgTableRow arg="radius-location-id" typ="string">Value of the WISPr-Location-ID attribute sent to the RADIUS server.</ArgTableRow>
<ArgTableRow arg="radius-location-name" typ="string">Value of the WISPr-Location-Name attribute sent to the RADIUS server.</ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XXXX:XXXX:XXXX | XXXXXX:XXXXXX | XX-XX-XX-XX-XX-XX | XXXXXX-XXXXXX | XXXXXXXXXXXX | XX XX XX XX XX XX) { XX:XX:XX:XX:XX:XX:0, XXXX:XXXX:XXXX:1, XXXXXX:XXXXXX:2, XX-XX-XX-XX-XX-XX:3, XXXXXX-XXXXXX:4, XXXXXXXXXXXX:5, XX XX XX XX XX XX:6 }">Format of the MAC address of the client in the RADIUS requests. Default: `XX:XX:XX:XX:XX:XX`.</ArgTableRow>
</ArgTable>
