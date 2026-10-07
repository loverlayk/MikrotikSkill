# fetch

> Download and upload files and make HTTP requests from the console or scripts. See the Fetch guide.

-----------

## tool/fetch 
**Type:** Command

Download and upload files and make HTTP requests from the console or scripts. See the [Fetch](../../system-information-and-utilities/fetch) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="url" typ="string">Full URL of the resource, for example https://download.mikrotik.com/routeros/7.19/CHANGELOG or ftp://user:password@192.168.88.2/conf.rsc. The scheme selects the mode, and ftp/sftp URLs may carry the credentials. Can replace the separate address and src-path parameters. A VRF cannot be given inside the URL: in http://192.168.88.2@vrf1/ the part after @ is treated as the host name. Use the address parameter for VRF.</ArgTableRow>
<ArgTableRow arg="output" typ="enum (none | file | user | user-with-headers)">
Determines where the fetched data is stored.
- `none` - Do not store downloaded data.
- `file` (default) - Store downloaded data in a file (`dst-path`; with `url` and no `dst-path`, the file is named after the last part of the URL path).
- `user` - Store downloaded data in the `data` value of `as-value`, at most 64512 bytes (63 KiB); a longer body is cut without an error.
- `user-with-headers` - Store downloaded data in `data` (at most 20480 bytes, 20 KiB) and the response headers in `http-headers` (up to 44 KB).
</ArgTableRow>
<ArgTableRow arg="http-method" typ="enum (get | post | put | delete | head | patch)">
HTTP method of the request. PUT and PATCH without `http-data` send an empty body.
- `get` (default) - Request the resource.
- `post` - Send `http-data` to the resource.
- `put` - Send `http-data` as the new content of the resource.
- `delete` - Delete the resource.
- `head` - Request only the response headers.
- `patch` - Send `http-data` as a partial change of the resource.
</ArgTableRow>
<ArgTableRow arg="http-auth-scheme" typ="enum (basic | digest)">HTTP authentication scheme for `user` and `password`. With `basic`, the credentials are sent with the first request, without waiting for a challenge. Default: basic.</ArgTableRow>
<ArgTableRow arg="http-data" typ="string">Request body for POST, PUT and PATCH. Maximum data limit is 64 KB. Without a `Content-Type` in `http-header-field`, the body is sent as `application/x-www-form-urlencoded`.</ArgTableRow>
<ArgTableRow arg="http-header-field" typ="multi { array-id, header-field: string
 }">HTTP header fields and values, in the form of "h1:fff,h2:yyy": a comma starts the next header. To keep a comma inside one header value, escape it with two backslashes, e.g. "h:fff\\,yyy" sends `h: fff,yyy`. Fetch always sends `User-Agent: RouterOS <version>` and `Accept-Encoding: deflate, gzip`.</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (no | yes | yes-without-crl)">
TLS certificate validation for HTTPS.
- `no` (default) - Do not validate: fetch connects even to a server with an expired or self-signed certificate.
- `yes` - Validate the trust chain against the local certificate store, which includes a builtin trust store with public root certificates. An invalid certificate fails the fetch, for example with `failure: SSL: ssl: cert not valid (after: ... < now: ...)`.
- `yes-without-crl` - Validate the certificate without a CRL check.
</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum">Certificate from the certificate store used for server verification in HTTPS mode. Applicable only when `check-certificate` is enabled.</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address: address (flags=46vi)
, address: ipAddr
 }">IP address or host name of the target device. Append @vrf_name to run the fetch operation within a specific VRF, or set only address=@vrf_name and let the url parameter supply the address.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">Source IP address for establishing the connection. Applicable to HTTP, HTTPS, and SFTP modes only.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Port used for the connection. Default: the port of the mode (80 for `http`, 443 for `https`, 21 for `ftp`, 22 for `sftp`, 69 for `tftp`), or the port given in `url`.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (http | https | ftp | tftp | sftp)">
Protocol used for the connection. With `url`, the protocol comes from the URL scheme.
- `http` (default) - HTTP.
- `https` - HTTP over TLS.
- `ftp` - FTP; download and upload.
- `tftp` - TFTP; download from a TFTP server, for example `/ip/tftp` on another router.
- `sftp` - SFTP over SSH; download and upload.
</ArgTableRow>
<ArgTableRow arg="http-content-encoding" typ="enum (deflate | gzip)">Compresses `http-data` with gzip or deflate and adds a matching `Content-Encoding` header. Only applicable to POST and PUT methods.</ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (any | ipv4 | ipv6)">
IP family preference when resolving domain names.
- `any` (default) - Use IPv4 or IPv6.
- `ipv4` - Use IPv4 only.
- `ipv6` - Use IPv6 only.
</ArgTableRow>
<ArgTableRow arg="src-path" typ="file">Path of the remote file; with `upload=yes`, the local file to upload.</ArgTableRow>
<ArgTableRow arg="dst-path" typ="file">Destination path where the fetched file is saved; with `upload=yes`, the file name on the remote device. Without `dst-path`, a download is named after the last part of the URL path.</ArgTableRow>
<ArgTableRow arg="user" typ="string">Username for authentication on the remote device. Without `user`, FTP logs in as `anonymous` and HTTP sends no credentials.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password for `user`. With `user` and no `password`, HTTP sends an empty password.</ArgTableRow>
<ArgTableRow arg="host" typ="string">Hostname or virtual hostname of the remote web server. Useful when the same IP serves multiple virtual hosts. For example, `address=manual.mikrotik.com host=forum.mikrotik.com`.</ArgTableRow>
<ArgTableRow arg="ascii" typ="bool">Enables ASCII mode for FTP/TFTP transfers. Default: no.</ArgTableRow>
<ArgTableRow arg="upload" typ="bool">Enables upload mode for FTP and SFTP transfers: `src-path` is the local file, and `dst-path` (or the path in `url`) the name on the remote device. HTTP uploads are not supported; use `http-method=put` with `http-data`. Default: no.</ArgTableRow>
<ArgTableRow arg="sftp-known-hosts-ignore" typ="bool">Skip SSH host key validation for this SFTP transfer. Has an effect when known-hosts-validation in /ip/ssh is enabled; without validation enabled, any host key is accepted. Default: no.</ArgTableRow>
<ArgTableRow arg="keep-result" typ="bool">Deprecated, use the output argument instead.</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="alt { idle-timeout: time [1 .. 604800]
, idle-timeout: enum (none) { none:0 }
 }">Idle timeout since last read/write action. Default: 10s.</ArgTableRow>
<ArgTableRow arg="http-max-redirect-count" typ="num">Maximum number of HTTP redirects that fetch follows. With the default of 2, a chain of two redirects is followed and a third fails the fetch with the received 3xx status. Default: 2.</ArgTableRow>
<ArgTableRow arg="http-percent-encoding" typ="bool">Percent-encodes every character in the request path except alphanumeric and `-._~/?^=:`. Default: no.</ArgTableRow>
<ArgTableRow arg="http-version" typ="enum (http1_1 | http2 | http2-forced)">HTTP protocol version. HTTP2 is supported only on ARM64 and x86/CHR devices. Default: http1_1.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (none | connecting | requesting | downloading | uploading | finished | failed)">Current status of the fetch operation.</ArgTableRow>
<ArgTableRow arg="code" typ="num">HTTP status code returned by the server.</ArgTableRow>
<ArgTableRow arg="downloaded" typ="num">Amount downloaded, in KiB, rounded down and at least 1 when data arrived (7 bytes and 2047 bytes both show 1). With `output=user`, the amount stored in `data`; compare `[:len ($r->"data")]` with the limit to detect a cut body.</ArgTableRow>
<ArgTableRow arg="uploaded" typ="num">Amount uploaded, in KiB, rounded down.</ArgTableRow>
<ArgTableRow arg="total" typ="num">Total size of the transfer, in KiB, rounded down.</ArgTableRow>
<ArgTableRow arg="duration" typ="time">The total duration of the fetch operation.</ArgTableRow>
<ArgTableRow arg="data" typ="string">Fetched data when `output` is `user` (at most 64512 bytes) or `user-with-headers` (at most 20480 bytes). A longer body is cut without an error.</ArgTableRow>
<ArgTableRow arg="http-headers" typ="object { http-header: super { key: string
, [value] : string
 }
 }">HTTP headers returned by the server.</ArgTableRow>
</ArgTable>
