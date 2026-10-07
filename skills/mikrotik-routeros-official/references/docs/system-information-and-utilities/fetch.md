# Fetch

> Fetch transfers files over HTTP, HTTPS, FTP, TFTP and SFTP and makes HTTP requests from the console or scripts: downloads, uploads, POST data and webhooks, certificate checks, redirects, result variables and VRF support.

# Fetch

Fetch downloads and uploads files over HTTP, HTTPS, FTP, TFTP and SFTP, and makes HTTP requests (GET, POST, PUT and others) to remote servers. It runs in the console and in scripts, prints a live status and either saves the result to a file or returns it to a script variable.

In WinBox, select **New Terminal** in the left menu to run the commands on this page. The terminal displays the transfer status; open **Files** to find a downloaded file when the command saves its result to the router.

## Download and upload files

Copy a file from another RouterOS device over FTP. The device needs the FTP service enabled (`/ip/service`) and an account with a password:

```ros
/tool/fetch mode=ftp address=192.168.88.2 user=admin \
    password=mypassword src-path=conf.rsc dst-path=backup.rsc
```

To upload a file instead, set `upload=yes` and swap the paths: `src-path` is the file on the local router, `dst-path` is the name on the remote device:

```ros
/tool/fetch mode=ftp address=192.168.88.2 user=admin \
    password=mypassword src-path=backup.rsc dst-path=conf.rsc upload=yes
```

The same transfers work with `mode=sftp` on port 22. SFTP uses the SSH service of the remote device, which RouterOS enables by default. Uploads (`upload=yes`) work in the `ftp` and `sftp` modes only; to send data to a web server, use an HTTP request with `http-data`. Without `user`, FTP logs in as `anonymous`.

You can put the address, credentials and path into a single URL; the mode is then detected from the scheme:

```ros
/tool/fetch url="ftp://admin:mypassword@192.168.88.2/conf.rsc" \
    dst-path=backup.rsc
```

`mode=tftp` downloads from a TFTP server, for example [`/ip/tftp`](../cli-reference/ip/tftp/) on another router:

```ros
/tool/fetch address=192.168.88.2 mode=tftp src-path=conf.rsc \
    dst-path=backup.rsc
```

:::note
SFTP host key validation is enabled on new installations and kept disabled on upgraded routers (the `known-hosts-validation` setting in [`/ip/ssh`](../cli-reference/ip/ssh/)). With validation enabled, a fetch to a server whose key is not in [`/ip/ssh/known-hosts`](../cli-reference/ip/ssh/known-hosts) fails with `host key not trusted`; `sftp-known-hosts-ignore=yes` bypasses this for a single transfer, and `known-hosts-trusted-subnets` skips the check for whole subnets.
:::

## Make HTTP requests

With the `url` parameter, fetch detects the protocol from the scheme and saves the file with the name from the URL unless `dst-path` overrides it:

```ros
[admin@MikroTik] > /tool/fetch check-certificate=yes \
    url="https://download.mikrotik.com/routeros/7.19/CHANGELOG"
  status: connecting

      status: finished
        code: 200
  downloaded: 18KiB
       total: 18KiB
    duration: 1s
```

Fetch does not validate TLS certificates by default: without `check-certificate`, it connects even to a server with an expired or self-signed certificate. Set `check-certificate=yes` for HTTPS downloads you rely on, and always before you import or run what you download. RouterOS includes a builtin trust store with public root certificates (`builtin-trust-store` in `/certificate/settings`), so public sites work without extra imports. For a server with a certificate from your own authority, import the authority's certificate with `/certificate/import`; see [Certificates](../authentication-authorization-accounting/certificates). The check also verifies the host name in the URL, and it compares the certificate dates with the router's clock, so set the clock (for example with the [NTP client](ntp)) before you rely on it. An invalid certificate fails the fetch:

```text
failure: SSL: ssl: cert not valid (after: Sun Apr 12 23:59:59 2015 < now: Tue Sep 29 06:51:00 2026) - "OU=PositiveSSL Wildcard, CN=*.badssl.com" (6)
```

For servers with HTTP authentication, set `user` and `password`. Basic authentication is the default and sends the credentials with the first request; set `http-auth-scheme=digest` for digest authentication.

HTTP redirects are followed automatically. `http-max-redirect-count` limits how many redirects fetch follows: with the default of 2, a chain of two redirects is followed, and a third fails the request with the redirect status, for example `failure: Status 302, Found (Location: "https://mikrotik.com/download")`.

### Send data to a server

Use `http-method`, `http-header-field` and `http-data` for API endpoints:

```ros
/tool/fetch url="https://192.0.2.10/collector" http-method=post \
    http-header-field="Content-Type: application/json" \
    http-data="{\"lat\":\"56.12\",\"lon\":\"25.12\"}"
```

Without a `Content-Type` in `http-header-field`, the body is sent as `application/x-www-form-urlencoded`. Separate several header fields with commas (`"X-One: a,X-Two: b"`). With `http-content-encoding=gzip` (or `deflate`), a POST or PUT body is sent compressed with a matching `Content-Encoding` header.

To send generated content, store it in a file, read the file into a variable and pass the variable as `http-data`. Keep the commands in one block, because a `:local` variable exists only inside its block, and find the file with `find`:

```ros
{
    /export file=export.rsc
    :local data [/file/get [find name=export.rsc] contents]
    /tool/fetch url="https://192.0.2.10/collector" http-method=put \
        http-data=$data
}
```

This works for files up to 60000 bytes, within the 64 KB limit of `http-data`. Upload larger files with FTP or SFTP instead. To call the REST API of another RouterOS device, see [REST API](../developer-guides/rest-api).

## Automate common tasks

### Upload a backup to a server

Save an encrypted backup and upload it to an SFTP server. `/system/backup/save` finishes before the next command runs. Run the commands from a [scheduler](scheduler) script to keep a nightly copy off the router:

```ros
/system/backup/save name=nightly password="backup-file-password"
/tool/fetch url="sftp://192.168.88.2/nightly.backup" upload=yes \
    src-path=nightly.backup user=backup password="server-password"
```

For what a backup contains and how to restore it, see [Backup](../getting-started/configuration-management/backup).

### Download and run a script

Fetch a configuration script from your server and import it. `check-certificate=yes` makes sure that the file comes from your server; `/import` runs every command in the file, so fetch scripts only from a server you control. In one block, a failed download stops the block, so an older copy of the file is not imported:

```ros
{
    /tool/fetch url="https://config.example.com/branch.rsc" \
        check-certificate=yes dst-path=branch.rsc
    /import file-name=branch.rsc
}
```

### Send a notification to a webhook

Chat services, monitoring and automation tools accept JSON messages on a webhook URL; the field names depend on the service, so check its webhook documentation. `$[...]` inserts the output of a command into the message, here the router's name. The inserted text is not escaped: a quote or backslash in it breaks the JSON.

```ros
/tool/fetch url="https://hooks.example.com/notify" http-method=post \
    http-header-field="Content-Type: application/json" \
    check-certificate=yes output=none \
    http-data="{\"text\":\"$[/system/identity/get name]: backup done\"}"
```

With the identity `branch-office-1`, the server receives `{"text":"branch-office-1: backup done"}`. `output=none` discards the reply.

## Use fetch in scripts

With `as-value`, fetch returns an array instead of printing to the console. For `:local` variables, `{ }` blocks and `:onerror`, see [Scripting](../developer-guides/scripting/). `output` decides where the response body goes:

- `file` (default) - A file, `dst-path` or the name from the URL.
- `none` - Nowhere.
- `user` - The `data` key, at most 64512 bytes (63 KiB).
- `user-with-headers` - The `data` key, at most 20480 bytes (20 KiB), and the response headers in `http-headers`.

A longer body is cut without an error: when `[:len ($result->"data")]` equals the limit, the body was probably longer.

The following script disables `ether5` when a web page starts with `0`, and enables it otherwise. `:pick` takes the first character, because a text file usually ends with a newline. A failed fetch raises an error, which `:onerror` catches and logs, leaving the port as it is:

```ros
{
    :local url "http://192.0.2.10/state.txt"
    :onerror e in={
        :local result [/tool/fetch url=$url as-value output=user]
        :if ([:pick ($result->"data") 0 1] = "0") do={
            /interface/ethernet/set [find name=ether5] disabled=yes
        } else={
            /interface/ethernet/set [find name=ether5] disabled=no
        }
    } do={:log warning "state check failed: $e"}
}
```

`:onerror` puts the error message in the first variable; for an HTTP error, the second one holds the status `code` and the returned `http-headers`:

```ros
:onerror err,attr in={
    /tool/fetch url=http://192.168.88.2/nonexistent as-value
} do={
    :put $err; :put ($attr->"code"); :put ($attr->"http-headers")
}
```

```text
failure: Status 404, Not Found (/tool/fetch; line 2)
404
Cache-Control: no-store;Connection: Keep-Alive;Content-Length: 99;Content-Type: text/html;Date: Tue, 29 Sep 2026 07:05:39 GMT;Expires: 0;Pragma: no-cache;X-Frame-Options: sameorigin
```

## Run fetch in a VRF

To make fetch use a [VRF](../user-guides/routing-and-networking-protocols/vrf), append the VRF name to the `address` parameter after an `@`. Both forms work:

```ros
/tool/fetch url="ftp://admin:mypassword@192.168.88.2/conf.rsc" \
    address=@vrf1 dst-path=backup.rsc
/tool/fetch mode=ftp address=192.168.88.2@vrf1 user=admin \
    password=mypassword src-path=conf.rsc dst-path=backup.rsc
```

The VRF cannot be written into the URL itself: in `url="http://192.168.88.2@vrf1/…"` everything after `@` is treated as the host name, and the request fails with a resolving error.

## Technical details

- Fetch prints interim status lines such as `status: connecting` or `status: requesting`, and a summary with `status`, `code`, transfer sizes and `duration` when done. The sizes are shown in KiB, rounded down and at least 1 when data arrived, and the `as-value` fields `downloaded`, `uploaded` and `total` contain the same values.
- Every HTTP request carries `User-Agent: RouterOS <version>` and `Accept-Encoding: deflate, gzip`.
- For HTTPS on ARM64 and x86/CHR devices, `http-version=http2` is available; HTTP/2 responses present their headers with HTTP/2 pseudo headers such as `:status`.
- When a script combines `as-value` with `address=` and `src-path=`, fetch fails with `Conflicting remote paths provided in URI and parameter`. Use the `url` form, or drop `as-value`.

For all properties, see [`/tool/fetch`](../cli-reference/tool/fetch) in the CLI reference.
