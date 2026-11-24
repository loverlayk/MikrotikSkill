# tr069-client

> Settings of the TR-069 (CWMP) client, which connects the router to an Auto Configuration Server (ACS). The menu is available when the tr069-client package is installed. See TR-069 for setup and the RPCs the router...

-----------

## tr069-client 
**Package:** tr069-client
**Type:** Settings Directory

Settings of the TR-069 (CWMP) client, which connects the router to an Auto Configuration Server (ACS). The menu is available when the `tr069-client` package is installed. See [TR-069](../../management-tools/tr-069) for setup and the RPCs the router supports.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (yes | no)">Enables the CWMP client. When enabled with an `acs-url`, the client starts a session with the ACS. Default: `no`.</ArgTableRow>
<ArgTableRow arg="acs-url" typ="string">URL of the ACS, `http://` or `https://`, for example `https://acs.example.com:7547/`. For HTTPS with `check-certificate=yes`, the certificate store must contain the CA certificate that signed the ACS certificate. Changing the URL makes the next Inform carry the `0 BOOTSTRAP` event, so the new ACS treats the router as a new device. Maps to `Device.ManagementServer.URL`.</ArgTableRow>
<ArgTableRow arg="username" typ="string">Username the router sends to the ACS for HTTP authentication. Over HTTP the router sends the credentials after the ACS asks for them (HTTP 401); over HTTPS it sends them with the first request.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password the router sends to the ACS for HTTP authentication. It is a sensitive value: `/export` leaves it out unless `show-sensitive` is given. Changing it does not start a session; the next scheduled or retried session uses it.</ArgTableRow>
<ArgTableRow arg="periodic-inform-enabled" typ="bool">Starts a session with the ACS every `periodic-inform-interval`. The Inform of such a session carries the `2 PERIODIC` event. Maps to `Device.ManagementServer.PeriodicInformEnable`. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="periodic-inform-interval" typ="time">Interval between periodic sessions, counted from the end of the last successful session. The ACS can change it through `Device.ManagementServer.PeriodicInformInterval` (in seconds). Minimum `1s`. Default: `1d`.</ArgTableRow>
<ArgTableRow arg="connection-request-username" typ="string">Username the ACS must use for Connection Requests, the HTTP requests with which the ACS asks the router to start a session. The router accepts only HTTP Digest authentication. Set a username and password: with both empty, the router accepts a Digest request with empty credentials.</ArgTableRow>
<ArgTableRow arg="connection-request-password" typ="string">Password the ACS must use for Connection Requests (HTTP Digest authentication).</ArgTableRow>
<ArgTableRow arg="connection-request-port" typ="num">TCP port on which the router listens for Connection Requests. The router reports the full URL, `http://<address>:<port>/<random path>`, to the ACS as `Device.ManagementServer.ConnectionRequestURL` in every Inform. The firewall must accept connections to this port from the ACS; the client adds no firewall rule. Default: `7547`.</ArgTableRow>
<ArgTableRow arg="provisioning-code" typ="string">Free-form code that the router sends to the ACS in every Inform as `Device.DeviceInfo.ProvisioningCode`. An ACS can use it to group devices, for example by service plan or region.</ArgTableRow>
<ArgTableRow arg="client-certificate" typ="enum (none)">Certificate (with its private key) from the certificate store that the router presents in the TLS handshake when the ACS asks for a client certificate. Default: `none`.</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (yes | no)">Verifies the HTTPS certificate of the ACS: it must be signed by a CA in the certificate store, and its name must match the host in `acs-url`. With `no`, the router connects to any HTTPS server at that URL and sends it the `username` and `password`. Default: `yes`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (disabled | initializing | error | waiting-url | running)">
State of the client:
- `disabled` - `enabled=no`.
- `waiting-url` - enabled, but `acs-url` is empty.
- `running` - enabled with an ACS URL. The status stays `running` while sessions fail; check `last-session-error` and `retry-count`.
- `initializing`, `error` - other states the client reports.
</ArgTableRow>
<ArgTableRow arg="last-session-error" typ="string">Reason the last session failed, for example `Connection refused`, `resolving error`, `Network unreachable`, `HTTP error code: 500`, `HTTP authentication error. Wrong username/password.` or an `SSL:` certificate error. Empty after a successful session.</ArgTableRow>
<ArgTableRow arg="retry-count" typ="num">Number of failed sessions in a row. The client retries with a growing delay (seconds at first, then minutes) and sends the count to the ACS in the Inform `RetryCount`. Resets to 0 after a successful session, when the client is disabled, and after a reboot.</ArgTableRow>
</ArgTable>
