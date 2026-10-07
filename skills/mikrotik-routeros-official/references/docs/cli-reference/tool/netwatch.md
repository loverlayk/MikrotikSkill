# netwatch

> RouterOS directory reference for /tool/netwatch.

-----------

## tool/netwatch 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">The name of the Netwatch probe.</ArgTableRow>
<ArgTableRow arg="host" typ="address (flags=46viD)" mandatory="1">The IP address or domain name of the server to be probed. See [address flags](../../cli-reference/#address-flags)</ArgTableRow>
<ArgTableRow arg="type" typ="enum (simple | icmp | tcp-conn | http-get | https-get | dns)">
Type of the probe (default value: **"simple"**) :
- simple - simplified ICMP probe, with fewer options than "ICMP" type, used for backward compatibility with the older Netwatch version
- icmp - (ping-style) series of ICMP request-response with statistics
- tcp-conn - test TCP connection (3-way handshake) to a server specified by IP and port
- http-get - do an HTTP Get request and test for a range of correct replies
- https-get - do an HTTPS Get request and test for a range of correct replies
- dns - do a specified DNS query for the domain name
</ArgTableRow>
<ArgTableRow arg="src-address" typ="address (flags=46)" unset="1">Source IP address which the Netwatch will try to use in order to reach the host. If the address is not configured on the router or was lost, then the host will be considered as "down". See [address flags](../../cli-reference/#address-flags)</ArgTableRow>
<ArgTableRow arg="interval" typ="time" unset="1">The time interval between probe tests. (default value: **10s**)</ArgTableRow>
<ArgTableRow arg="timeout" typ="time" unset="1">Max time limit to wait for a response. (default value: **3s**)</ArgTableRow>
<ArgTableRow arg="start-delay" typ="time" unset="1">Time to wait before starting the probe. (default value: **3s**) (on add, enable, or system startup in cases when "startup-delay" value is smaller then "start-delay" value)</ArgTableRow>
<ArgTableRow arg="startup-delay" typ="time" unset="1">Time to wait until starting the Netwatch probe after system startup. (default value: **5m**)</ArgTableRow>
<ArgTableRow arg="ignore-initial-up" typ="bool" unset="1">Specifies if "Up" script should be run if the probe state change goes from Unknown to "Up", used to help against false positives after enabling the probe, or after a reboot. "no" means that the change from "Unknown" to "Up" will not be ignored. (default value: **no**)</ArgTableRow>
<ArgTableRow arg="ignore-initial-down" typ="bool" unset="1">Specifies if "Down" script should be run if the probe state change goes from Unknown to "Down". "no" means that the change from "Unknown" to "Down" will not be ignored. (default value: **no**)  **Warning**: Should be used with care, as the first "Down" status won't be executed, and Down script will only be run if the probe goes from "Up" to "Down" state.</ArgTableRow>
<ArgTableRow arg="up-script" typ="alt { script: string
 }" unset="1">Script to execute on the event of probe state change from "Down" to "Up".</ArgTableRow>
<ArgTableRow arg="down-script" typ="alt { script: string
 }" unset="1">Script to execute on the event of probe state change from "Up" to "Down".</ArgTableRow>
<ArgTableRow arg="test-script" typ="alt { script: string
 }" unset="1">Script to execute at the end of every probe test.</ArgTableRow>
<ArgTableRow arg="packet-interval" typ="time" unset="1">The time between ICMP-request packet sends. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **50ms**)</ArgTableRow>
<ArgTableRow arg="packet-count" typ="num" unset="1">Total count of ICMP packets to send out within a single test. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **10**)</ArgTableRow>
<ArgTableRow arg="packet-size" typ="num" unset="1">Total size of the IP ICMP packet. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **50**)</ArgTableRow>
<ArgTableRow arg="ttl" typ="num" unset="1">Manually sets the time to live value for the ICMP packet. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **255**)</ArgTableRow>
<ArgTableRow arg="accept-icmp-time-exceeded" typ="bool" unset="1">If the ICMP "time exceeded" message should be considered a valid response. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **no**)</ArgTableRow>
<ArgTableRow arg="early-success-detection" typ="bool" unset="1">Netwatch will not wait for all the packets to be processed to change probe status if it is already known that the host will be considered "Down". This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **no**)</ArgTableRow>
<ArgTableRow arg="early-failure-detection" typ="bool" unset="1">Netwatch will not wait for all the packets to be processed to change probe status if it is already known that the host will be considered "Down". This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **no**)</ArgTableRow>
<ArgTableRow arg="thr-max" typ="time" unset="1">Fail threshold for rtt-max. (a value above thr-max is a probe fail) This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **1s**)</ArgTableRow>
<ArgTableRow arg="thr-avg" typ="time" unset="1">Fail threshold for rtt-avg. (round trip time-avg) This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **100ms**)</ArgTableRow>
<ArgTableRow arg="thr-stdev" typ="time" unset="1">Fail threshold for rtt-stdev. (standard deviation of round trip time) This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **250ms**)</ArgTableRow>
<ArgTableRow arg="thr-jitter" typ="time" unset="1">Fail threshold for rtt-jitter. (jitter ( = max - min) of round trip time) This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **1s**)</ArgTableRow>
<ArgTableRow arg="thr-loss-percent" typ="num" unset="1">Fail threshold for loss-percent. (number of lost packets in percent) This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **85%**)</ArgTableRow>
<ArgTableRow arg="thr-loss-count" typ="num" unset="1">Fail threshold for loss-count. (number of lost packets) This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type. (default value: **4294967295(max)**)</ArgTableRow>
<ArgTableRow arg="port" typ="num" unset="1">TCP port. This parameter is specific to the [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch#tcp-conn-probe) and [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) probe types. (default value: **80** (TCP-conn, HTTP-GET) and  **443** (HTTPS-GET))</ArgTableRow>
<ArgTableRow arg="thr-tcp-conn-time" typ="time" unset="1">Fail threshold for tcp-connect-time, the configuration uses microseconds, if the time unit is not specified (s/m/h), log and status pages display the same value in milliseconds. This parameter is specific to the [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch#tcp-conn-probe) probe type.(default value: **1s**)</ArgTableRow>
<ArgTableRow arg="thr-http-time" typ="time" unset="1">Fail threshold for http-resp-time. This parameter is specific to the [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) probe types. (default value: **10s**)</ArgTableRow>
<ArgTableRow arg="http-codes" typ="multi { http-response-range: range [100 .. 599]
 }" unset="1">Range of HTTP response status codes that are accepted as an "Up" state for the probe. See [mozilla-http-status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) or [RFC7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6). This parameter is specific to the [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) probe types. (default value: **100-299**)</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }" unset="1">Certificate from the local store that should be used for host verification. This parameter is specific to the [**HTTPS-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#https-get-probe) probe type.</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool" unset="1">Enables trust chain validation from the local certificate store. This parameter is specific to the [**HTTPS-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#https-get-probe) probe type. (default value: **no**)</ArgTableRow>
<ArgTableRow arg="record-type" typ="enum (A | AAAA | MX | NS)" unset="1">Record type that will be used for DNS probe. This parameter is specific to the [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) probe type. (default value: **A**)</ArgTableRow>
<ArgTableRow arg="dns-server" typ="address (flags=46)" unset="1">The DNS server that the probe should send its requests to; if not specified, it will use the value from `/ip/dns`. This parameter is specific to the [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) probe type. See [address flags](../../cli-reference/#address-flags)</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (unknown | down | up)" unset="1">Current status of the probe.</ArgTableRow>
<ArgTableRow arg="since" typ="date">Last time the status change happened.</ArgTableRow>
<ArgTableRow arg="done-tests" typ="num">Total number of completed probe tests.</ArgTableRow>
<ArgTableRow arg="failed-tests" typ="num">Total number of failed probe tests.</ArgTableRow>
<ArgTableRow arg="sent-count" typ="num">Amount of ICMP packets sent out during last probe test. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="response-count" typ="num">Amount of ICMP response packets received during last probe test. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="loss-count" typ="num">Amount of lost ICMP response packets during last probe test. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="loss-percent" typ="num">Percent of lost ICMP response packets during last probe test. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="rtt-avg" typ="time">Mean value of round trip time. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="rtt-min" typ="time">Minimal round trip time. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="rtt-max" typ="time">Maximum round trip time. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="rtt-jitter" typ="time">Jitter ( = max - min) of round trip time. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="rtt-stdev" typ="time">Standard deviation of round trip time. This parameter is specific to the [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) probe type.</ArgTableRow>
<ArgTableRow arg="tcp-connect-time" typ="time">Time taken to establish a TCP connection. This parameter is specific to the [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch#tcp-conn-probe) probe type.</ArgTableRow>
<ArgTableRow arg="http-status-code" typ="num">HTTP response status code (200 OK, 404 Not Found, etc.). See [mozilla-http-status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) or [RFC7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6). This parameter is specific to the [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) probe types.</ArgTableRow>
<ArgTableRow arg="http-resp-time" typ="time">Time taken by the HTTP/S server to send a response after receiving a request, typically measured in milliseconds. This parameter is specific to the [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) probe types.</ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr">IPv4 IP address - the result of A record-type probe. This parameter is specific to the [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) probe type.</ArgTableRow>
<ArgTableRow arg="ip6" typ="ip6Addr">IPv6 IP address - the result of AAAA record-type probe. This parameter is specific to the [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) probe type.</ArgTableRow>
<ArgTableRow arg="name-servers" typ="multi { array-id, name-servers: string
 }">Name servers - the result of NS record-type probe. This parameter is specific to the [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) probe type.</ArgTableRow>
<ArgTableRow arg="mail-servers" typ="multi { array-id, mail-servers: string
 }">Mail servers along with their priorities - the result of MX record-type probe. This parameter is specific to the [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) probe type.</ArgTableRow>
</ArgTable>
