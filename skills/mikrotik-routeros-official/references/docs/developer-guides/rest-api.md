# REST API

> RouterOS REST API: enable HTTPS access with a least-privilege user, read and change the configuration with GET, PUT, PATCH and DELETE, run any console command with POST, work within the 60-second limit and per-user...

# REST API

The REST API gives HTTP access to the RouterOS command line. Every menu is a URL under `/rest`: the `/ip/address` menu is `https://192.168.88.1/rest/ip/address`. JSON requests read, create, change and delete configuration and run any console command. Scripts, monitoring systems, automation tools and web dashboards use it to manage routers without WinBox or SSH.

The REST API is a JSON wrapper of the [API](api): the web server logs in to the API as the authenticated user and runs each request as an API command. The REST API therefore offers the same menus, parameters and permissions as the console, and the [CLI reference](../cli-reference/) describes them. The web server serves the REST API over HTTPS through the `www-ssl` service (`https://<router>/rest`) and over HTTP through the `www` service (`http://<router>/rest`).

A first request with cURL. It uses the `rest-ca.crt` file from [Set up HTTPS](#set-up-https) and asks for the password of the `monitoring` user from [Create a REST user](#create-a-rest-user):

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/system/resource \
    -d .proplist=board-name,cpu-load,free-memory,uptime
```

```json
{"board-name":"hAP ax^2","cpu-load":"7","free-memory":"687116288","uptime":"1d7h44m20s"}
```

Any HTTP client works: cURL, wget, a programming language's HTTP library, and [`/tool/fetch`](../system-information-and-utilities/fetch) on another RouterOS device.

## Enable REST access

A REST client needs three things on the router: a running web service (`www-ssl` for HTTPS, `www` for HTTP), a certificate for HTTPS, and a user whose group allows the REST API.

### Set up HTTPS

The REST API authenticates with [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication): every request carries the username and password. Over HTTP, anyone who can see the traffic can read them. Use HTTP only on a network that no attacker can reach, or inside an encrypted tunnel, and use HTTPS everywhere else.

To serve HTTPS with a certificate authority of your own, create and sign the authority and a server certificate for the router's address, export the authority's certificate, and assign the server certificate to `www-ssl`. Run the commands in a terminal on the router (WinBox Terminal or SSH):

```ros
/certificate/add name=rest-ca common-name=rest-ca \
    key-usage=key-cert-sign,crl-sign days-valid=3650
/certificate/sign rest-ca
:delay 3s
/certificate/add name=rest-https common-name=192.168.88.1 \
    subject-alt-name=IP:192.168.88.1 days-valid=365
/certificate/sign rest-https ca=rest-ca
:delay 3s
/certificate/export-certificate rest-ca file-name=rest-ca
/ip/service/set www-ssl certificate=rest-https disabled=no
```

A signed certificate becomes available to other commands a moment after `sign` reports `done`; the `:delay` lines wait for that. Without them, the next command can fail with `input does not match any value of ca` (or `of certificate`); run it again.

Copy `rest-ca.crt` from the router's files to the client (for example with `scp admin@192.168.88.1:rest-ca.crt .`) and let the client trust it: `--cacert rest-ca.crt` in cURL, `verify="rest-ca.crt"` in Python. Address the router in URLs the way the certificate names it, here `192.168.88.1`; the client refuses a certificate issued for another name or address. The server certificate is valid for a year (`days-valid=365`); create a new one before it expires.

For a router with a public DNS name, you can use a Let's Encrypt certificate instead; see [Certificates](../authentication-authorization-accounting/certificates). For a quick test, `-k` in cURL and `--no-check-certificate` in wget skip the check, and with it the protection that the certificate gives.

`www-ssl` accepts TLS 1.0, 1.1 and 1.2. Set `tls-version=only-1.2` to refuse the older versions. Without a certificate (`certificate=none`), `www-ssl` offers only anonymous ciphers, which browsers and cURL do not accept, so HTTPS requests fail. For all service settings, see [`/ip/service`](../cli-reference/ip/service/).

### Create a REST user

The REST API logs in to the API on behalf of the user, so the user's group needs both the `rest-api` and the `api` policy. It also needs the policies for what the user does: `read` to read, `write` to change the configuration, `test` for `ping`, `ftp` to write files (`export` to a file), `ftp` and `test` to read files with `/file/read`, `sensitive` to see passwords and keys, and `password` to change its own password. The default `read`, `write` and `full` groups include `api` and `rest-api`, but also `reboot`, `sensitive` and the policies for WinBox, SSH and WebFig logins, so create your own groups for REST clients.

Give each client its own user with only the policies it needs. A monitoring system or dashboard only reads:

```ros
/user/group/add name=rest-read policy=read,api,rest-api
/user/add name=monitoring group=rest-read \
    password="use-a-long-random-password"
```

The examples on this page that change the configuration use `admin`. For a script, create a user with the policies of its task, for example `read,write,api,rest-api` to block addresses, or `read,write,ftp,test,api,rest-api` for the configuration backup.

`/user/group/add` revokes every policy it does not list. `/user/group/set` changes only the policies it lists, so revoke a policy with `!`, for example `policy=!write`. For all policies, see [`/user/group`](../cli-reference/user/group) and [User](../authentication-authorization-accounting/user).

### Restrict access

The default firewall drops connections to the router that do not come from the `LAN` interface list, which also keeps the REST API off the internet. Keep it that way: reach remote routers through a VPN such as [WireGuard](../virtual-private-networks/wireguard) instead of opening the web service to the internet. See [Securing your router](../getting-started/securing-your-router). The REST API does not use the `api` service: disabling `api` or limiting its `available-from` does not affect REST.

Limit which clients can use the service (include the addresses of your VPN clients if they use REST), and turn off the REST API over HTTP:

```ros
/ip/service/set www-ssl available-from=192.168.88.0/24
/ip/service/webserver/set rest-plain=no
```

- With `available-from`, the router closes connections from other addresses without serving them. The port stays visible, so use the firewall against untrusted networks. `available-from` applies to every user of the service; to tie one user to one client, set the user's `address` instead, for example `/user/set monitoring address=192.168.88.10/32`. Requests from other addresses then get `401 Unauthorized`.
- `rest-plain=no` turns off the REST API over HTTP (the reply is `403 Forbidden`), and WebFig over HTTP keeps working. To turn off HTTP entirely, disable the `www` service.
- To serve only the REST API over HTTPS, also set `index-secure=no webfig-secure=no graphs-secure=no`. The home page, WebFig, graphs and static files over HTTPS then answer `403 Forbidden`.

For the web server settings, see [`/ip/service/webserver`](../cli-reference/ip/service/webserver).

## Read data

A `GET` request reads a menu, like `print` in the console. The reply is a list of records:

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/ip/address \
    -d .proplist=.id,address,interface
```

```json
[{".id":"*1","address":"192.168.88.1/24","interface":"bridge"}]
```

To read one record, append its ID to the URL. In menus whose records have names, the name works too:

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    "https://192.168.88.1/rest/ip/address/*1" \
    -d .proplist=address,network,interface
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/interface/ether1 \
    -d .proplist=name,type,running,mtu
```

```json
{"address":"192.168.88.1/24","interface":"bridge","network":"192.168.88.0"}
{"mtu":"1500","name":"ether1","running":"false","type":"ether"}
```

- IDs start with `*`. Quote URLs that contain one, so the shell does not expand it. Send the asterisk as it is: the router does not decode `%2A`.
- Encode other reserved characters in names, for example a space as `%20` or the slash of a file in a folder as `%2F` (`/rest/file/flash%2Fbackup.rsc`).
- A menu without records, such as `/system/identity` or `/ip/dns`, returns one object.

Query parameters filter the records. A record must match every parameter, and the values must match exactly. For example, the Ethernet interfaces that have a link (`running=true`, or `yes`):

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/interface \
    -d type=ether -d running=true -d .proplist=name
```

```json
[{".id":"*5","name":"ether2"}]
```

- `.proplist` selects the properties of the reply. A `GET` of a list always includes `.id`.
- When no record matches, the reply is an empty list, `[]`.
- For other conditions (or, not, less than), use `.query` in the body of a `print` command, as in [Select records and properties](#select-records-and-properties). In a URL, `.query` is not a query.

## Change the configuration

The HTTP method selects the console command:

| Method | Console command | Reply on success |
| :-- | :-- | :-- |
| `GET` | `print` | `200 OK` with a record or a list of records |
| `PUT` | `add` | `201 Created` with the new record; the `Location` header holds its URL |
| `PATCH` | `set` | `200 OK` with the changed record |
| `DELETE` | `remove` | `204 No Content`, empty body |
| `POST` | Any command | `200 OK` with the command's reply |

Send the parameters as a JSON object with the `Content-Type: application/json` header. Without the header, the router answers `415 Unsupported Media Type`.

### Create a record

`PUT` to the menu creates one record per request, here an address on `guest`, a bridge for a guest network:

```bash
curl --cacert rest-ca.crt -u admin -X PUT \
    https://192.168.88.1/rest/ip/address \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.99.1/24","interface":"guest"}'
```

```json
{".id":"*18","actual-interface":"guest","address":"192.168.99.1/24","disabled":"false","dynamic":"false","interface":"guest","invalid":"false","network":"192.168.99.0","slave":"false","vrf":"main"}
```

### Change a record

`PATCH` to a record's URL changes the parameters in the body and returns the whole record:

```bash
curl --cacert rest-ca.crt -u admin -X PATCH \
    "https://192.168.88.1/rest/ip/address/*18" \
    -H "Content-Type: application/json" \
    --data '{"comment":"guest network"}'
```

```json
{".id":"*18","actual-interface":"guest","address":"192.168.99.1/24","comment":"guest network","disabled":"false","dynamic":"false","interface":"guest","invalid":"false","network":"192.168.99.0","slave":"false","vrf":"main"}
```

A `PATCH` by a user without the `write` policy fails with `400` and `missing or invalid resource identifier`. To change several records in one request, send `POST` to the menu's `set` command with the IDs separated by commas: `{".id":"*12,*13","comment":"imported"}`.

`PATCH` works only on records. To change a menu without records, such as `/system/identity`, `/ip/dns` or `/ip/service/webserver`, run its `set` command with `POST`. `set` returns an empty list:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/system/identity/set \
    -H "Content-Type: application/json" \
    --data '{"name":"branch-office-1"}'
curl --cacert rest-ca.crt -u monitoring \
    https://192.168.88.1/rest/system/identity
```

```json
[]
{"name":"branch-office-1"}
```

### Delete a record

`DELETE` to a record's URL removes it and returns an empty body. A second `DELETE` of the same ID returns `404`, the only output of these two commands:

```bash
curl --cacert rest-ca.crt -u admin -X DELETE \
    "https://192.168.88.1/rest/ip/address/*18"
curl --cacert rest-ca.crt -u admin -X DELETE \
    "https://192.168.88.1/rest/ip/address/*18"
```

```json
{"error":404,"message":"Not Found"}
```

### Values

- Replies encode every value as a string, also numbers and booleans (`"true"`, `"false"`).
- Requests can send values as strings or as JSON numbers and booleans: `"disabled":"yes"` and `"disabled":true` do the same.
- A command flag without a value, such as `once`, `compact` or `as-string`, takes an empty string: `"once":""`.
- The console's unnamed argument, such as the interface in `/interface/ethernet/monitor ether2`, is `numbers`: `{"numbers":"ether2","once":""}`.

## Run commands

`POST` runs any console command. The URL is the menu path and the command name, and the JSON body holds the command's parameters. For example, to change the authenticated user's own password (the user needs the `password` policy):

```text
POST https://192.168.88.1/rest/password
{"old-password":"old","new-password":"N3w","confirm-new-password":"N3w"}
```

The reply has the same structure as an [API](api) reply:

- A command that returns records (`print`, `ping`, `monitor-traffic`) returns a list of objects, one per record (`!re` sentence).
- A command that returns data in the `!done` sentence returns an object with that data, usually a value in `ret`: the ID of a new record for `add`, the number of records for `print count-only`, the output of `execute` with `as-string`.
- A command that returns nothing returns an empty list, `[]`, or for some commands `[{}]`.
- Commands that report progress (`bandwidth-test`, `fetch`, `check-for-updates`) number their replies in `.section`.

The reply arrives when the command ends: the REST API does not stream output.

### Select records and properties

Two special keys select what a command returns: `.proplist` the properties, for any command that returns records, and `.query` the records, for `print`. `.proplist` is a comma-separated string or a list of strings:

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/ip/address/print \
    -H "Content-Type: application/json" \
    --data '{".proplist":"address,interface"}'
```

```json
[{"address":"192.168.88.1/24","interface":"bridge"}]
```

`.query` is a list of API query words without the leading `?`, evaluated as a stack: `type=ether` matches a value, `<l2mtu=1600` and `>` compare, and `#|!` combines the two previous results with OR and negates the result. For example, `{".query":["type=ether","type=vlan","#|!"]}` is the API sentence:

```text
/interface/print
?type=ether
?type=vlan
?#|!
```

The [API queries](api#queries) section explains the query words and operators. The following request returns the interfaces that are neither Ethernet nor VLAN interfaces:

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/interface/print \
    -H "Content-Type: application/json" \
    --data '{".proplist":"name,type",
        ".query":["type=ether","type=vlan","#|!"]}'
```

```json
[{"name":"bridge","type":"bridge"},{"name":"guest","type":"bridge"},
{"name":"lo","type":"loopback"},{"name":"wifi1","type":"wifi"},
{"name":"wifi2","type":"wifi"}]
```

`count-only` returns the number of records instead:

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/ip/address/print \
    -H "Content-Type: application/json" --data '{"count-only":""}'
```

```json
{"ret":"1"}
```

### Keep commands within 60 seconds

The router ends a request that runs for 60 seconds and answers `400 Bad Request` with the detail `Session closed`. A duration parameter does not extend the limit: a bandwidth test asked to run for an hour still ends after 60 seconds.

Commands that run until you stop them, such as `ping` without `count`, `monitor` commands and `bandwidth-test` without `duration`, always hit the limit:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/ping \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.88.10"}'
```

```json
{"detail":"Session closed","error":400,"message":"Bad Request"}
```

Limit such commands with a parameter. With `count`, `ping` returns one record per echo reply:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/ping \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.88.10","count":"3"}'
```

```json
[{"avg-rtt":"551us","host":"192.168.88.10","max-rtt":"551us","min-rtt":"551us","packet-loss":"0","received":"1","sent":"1","seq":"0","size":"56","time":"551us","ttl":"64"},
{"avg-rtt":"536us","host":"192.168.88.10","max-rtt":"551us","min-rtt":"521us","packet-loss":"0","received":"2","sent":"2","seq":"1","size":"56","time":"521us","ttl":"64"},
{"avg-rtt":"538us","host":"192.168.88.10","max-rtt":"551us","min-rtt":"521us","packet-loss":"0","received":"3","sent":"3","seq":"2","size":"56","time":"542us","ttl":"64"}]
```

A bandwidth test with a `duration` shorter than the limit returns one record per second, with the `status` of the test:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/tool/bandwidth-test \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.88.2","user":"admin",
        "password":"<password>","duration":"3s",
        ".proplist":"status,duration"}'
```

```json
[{".section":"0","status":"connecting"},
{".section":"1","duration":"0s","status":"running"},
{".section":"2","duration":"1s","status":"running"},
{".section":"3","duration":"2s","status":"running"},
{".section":"4","duration":"3s","status":"done testing"}]
```

`monitor` commands take `once` and return a single sample. For example, the current traffic on two interfaces, in bits per second:

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/interface/monitor-traffic \
    -H "Content-Type: application/json" \
    --data '{"interface":"ether1,ether2","once":"",
        ".proplist":"name,rx-bits-per-second,tx-bits-per-second"}'
```

```json
[{"name":"ether1","rx-bits-per-second":"0","tx-bits-per-second":"0"},
{"name":"ether2","rx-bits-per-second":"25128","tx-bits-per-second":"8816"}]
```

To run a task that takes longer than 60 seconds, start it as a background job with `/execute` without `as-string` (see [Run a script and write to the log](#run-a-script-and-write-to-the-log)): the request returns the job ID at once, and the job keeps running. Let the job write its result to the log or to a file.

### Send parallel requests from separate users

The router runs the requests of one user one at a time, in the order they arrive. Requests of different users run in parallel. A long command therefore holds every other request of the same user until it ends.

A request keeps running on the router when the client gives up on it, until the command ends or reaches the 60-second limit. The requests of the same user that wait behind it fail with `Session closed` when it reaches the limit. Give clients that work independently, such as a dashboard and an automation script, separate users.

## Automate common tasks

### Block an address for a day

An intrusion detection system or a log analyzer can add an attacker's address to an address list that the firewall drops. With a `timeout`, the router removes the entry by itself:

```bash
curl --cacert rest-ca.crt -u admin -X PUT \
    https://192.168.88.1/rest/ip/firewall/address-list \
    -H "Content-Type: application/json" \
    --data '{"list":"blocked","address":"203.0.113.45",
        "timeout":"1d","comment":"reported by IDS"}'
```

```json
{".id":"*3C","address":"203.0.113.45","comment":"reported by IDS","creation-time":"2026-09-28 16:48:57","disabled":"false","dynamic":"true","list":"blocked","timeout":"1d"}
```

The router removes the entry when the timeout ends; to unblock the address earlier, `DELETE` the entry's URL (`/rest/ip/firewall/address-list/*3C`). Adding an address that is already in the list fails with `400` and `failure: already have such entry`.

The list blocks nothing by itself: a firewall rule drops its addresses. Add the rule once, in a terminal on the router. A rule in the `raw` table handles packets before connection tracking, so it drops the blocked addresses early, for traffic to the router and through it. `in-interface-list=WAN` limits it to packets from the internet, so a wrong report cannot cut off your LAN:

```ros
/ip/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=blocked \
    comment="drop blocked addresses"
```

A blocked address cannot reach the router or the network behind it from the internet for the whole timeout, so check what the reporting system sends before you automate it. See [Address lists](../firewall-and-quality-of-service/firewall/address-lists).

Another RouterOS device can send such a request with `/tool/fetch`; this one adds an entry without a timeout. The calling router needs `rest-ca.crt` imported (`/certificate/import`) to check the certificate; without it, the fetch fails with `no trusted CA certificate found`:

```ros
/tool/fetch url="https://192.168.88.1/rest/ip/firewall/address-list" \
    http-method=put check-certificate=yes \
    http-header-field="Content-Type: application/json" \
    http-data="{\"list\":\"blocked\",\"address\":\"203.0.113.46\"}" \
    user=admin password="<password>" output=user
```

### Save the configuration to a server

`export` with `file` writes the configuration to a file on the router. `/file/read` returns up to 32768 bytes per request from `offset`, so a backup server can collect the file and delete it from the router. The user needs `read,write,ftp,test,api,rest-api`. In the following commands, `jq` takes the file content out of the JSON reply:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/export \
    -H "Content-Type: application/json" --data '{"file":"backup"}'
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/file/read \
    -H "Content-Type: application/json" \
    --data '{"file":"backup.rsc","chunk-size":"32768","offset":"0"}' \
    | jq -j '.[0].data' > backup.rsc
curl --cacert rest-ca.crt -u admin -X DELETE \
    https://192.168.88.1/rest/file/backup.rsc
```

For a file larger than 32768 bytes, repeat the read with `offset` increased by the number of bytes received, until the reply holds no data (`[{"data":""}]` at the end of the file; an offset past the end fails with `failure: chunk out of file bounds`). See [`/file/read`](../cli-reference/file/read).

The export leaves out passwords and private keys. To include them, add `"show-sensitive":""` and give the user the `sensitive` policy as well; without that policy the file still leaves them out. Keep such a file as safe as the router's password. For a binary backup of the whole configuration, see [Backup](../getting-started/configuration-management/backup).

### Run a script and write to the log

To run a script from `/system/script`, name it (or give its ID) in `.id`:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/system/script/run \
    -H "Content-Type: application/json" --data '{".id":"daily-report"}'
```

`/execute` runs console commands given as a script. Without `as-string`, it starts the script as a job and returns the job ID; with `as-string`, it waits and returns the script's output:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/execute \
    -H "Content-Type: application/json" \
    --data '{"script":"/log/info \"backup job started\""}'
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/execute \
    -H "Content-Type: application/json" \
    --data '{"script":":put [/system/clock/get date]","as-string":""}'
```

```json
{"ret":"*126"}
{"ret":"2026-09-28"}
```

### Check for RouterOS updates

`check-for-updates` asks the update server for the latest version of the router's channel. Without `once`, the reply lists the progress until the check ends, and the last record holds `status` and `latest-version`:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/system/package/update/check-for-updates \
    -H "Content-Type: application/json" --data '{}'
```

### Move a firewall rule

`move` places a rule before another one, like in the console:

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/ip/firewall/nat/move \
    -H "Content-Type: application/json" \
    --data '{".id":"*9","destination":"*C"}'
```

To create a rule at a position, add `place-before` with the ID of the rule that must follow it to the `PUT` body.

### Read SNMP OIDs

`print` with `oid` returns the SNMP OID of each property that has one, instead of its value:

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/system/resource/print \
    -H "Content-Type: application/json" --data '{"oid":""}'
```

```json
[{"build-time":".1.3.6.1.4.1.14988.1.1.7.6.0","cpu-frequency":".1.3.6.1.4.1.14988.1.1.3.14.0","total-memory":".1.3.6.1.2.1.25.2.3.1.5.65536","uptime":".1.3.6.1.2.1.1.3.0"}]
```

### Read interface traffic in Python

The following Python program uses the `requests` library to print the current traffic of every Ethernet interface that has a link. `json=` sends the body as JSON with the `Content-Type` header, and the session reuses one connection for both requests:

```python

ROUTER = "https://192.168.88.1/rest"

session = requests.Session()
session.auth = ("monitoring", "use-a-long-random-password")
session.verify = "rest-ca.crt"

# Names of the Ethernet interfaces that have a link
ports = session.get(
    f"{ROUTER}/interface",
    params={"type": "ether", "running": "true", ".proplist": "name"},
)
ports.raise_for_status()
names = ",".join(port["name"] for port in ports.json())

# One sample of the traffic on these interfaces
traffic = session.post(
    f"{ROUTER}/interface/monitor-traffic",
    json={"interface": names, "once": ""},
)
traffic.raise_for_status()

for port in traffic.json():
    rx = int(port["rx-bits-per-second"]) / 1_000_000
    tx = int(port["tx-bits-per-second"]) / 1_000_000
    print(f"{port['name']}: rx {rx:.1f} Mbit/s, tx {tx:.1f} Mbit/s")
```

```text
ether2: rx 0.1 Mbit/s, tx 0.0 Mbit/s
```

For the binary [API](api), see the [Python 3 example](api/python3-example).

## Build a dashboard or integration

A web dashboard, a status page or an integration with another system can read the router through the REST API, and an AI assistant can write such a tool from this page and the CLI reference: give it the addresses of this page and of the CLI reference pages of the menus the tool uses. Give the assistant, or keep in mind when you write it yourself:

- **A backend for the REST calls.** The router sends no CORS headers and answers `OPTIONS` preflight requests with `503`, so a web page served from another address cannot call the REST API from the browser. Let a small server-side program (the dashboard's backend or a proxy) send the requests. It also keeps the router's password out of the browser.
- **A read-only user.** Create a group with `read,api,rest-api`, as in [Create a REST user](#create-a-rest-user), and a separate user for the dashboard, and set the user's `address` to the address of the backend. A dashboard that only reads cannot change the configuration, even with a mistake in its code.
- **No administrator password for the assistant.** Do not give an AI assistant, or code it writes, the `admin` credentials. Give the generated code the read-only user, and add write access only for the actions the tool really needs.
- **Its own user, and short requests.** Requests of one user run one at a time, so a dashboard that polls many values at once waits for each. Use `monitor` commands with `once`, `ping` with `count`, and `.proplist` to keep replies small.
- **Strings in replies.** Every value arrives as a string: convert numbers before calculating. Traffic rates are in bits per second, memory and disk sizes in bytes, `cpu-load` in percent, and durations such as `uptime` in the RouterOS format, for example `1d7h44m20s`.
- **One connection.** Reuse an HTTP connection (keep-alive) for the polls to save the TCP and TLS setup. The router keeps the user's login for 10 minutes on any connection, so frequent polls do not log in every time.
- **The menus and parameters.** The [CLI reference](../cli-reference/) describes every menu and parameter. The router also describes itself through `/console/inspect`, which lists the commands and parameters of a menu:

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/console/inspect \
    -H "Content-Type: application/json" \
    --data '{"request":"child","path":"ip,address,add",
        ".proplist":"name,node-type"}'
```

```json
[{"name":"add","node-type":"cmd"},{"name":"address","node-type":"arg"},{"name":"broadcast","node-type":"arg"},{"name":"comment","node-type":"arg"},{"name":"copy-from","node-type":"arg"},{"name":"disabled","node-type":"arg"},{"name":"interface","node-type":"arg"},{"name":"netmask","node-type":"arg"},{"name":"network","node-type":"arg"}]
```

Before you run code that an assistant wrote against a production router, test it with the read-only user or on a test router.

## Troubleshoot REST requests

The HTTP status code shows whether a request succeeded. On failure (400 or higher), the body is a JSON object with the code in `error`, its description in `message` and, for most errors, the router's reason in `detail`. For example, `POST /rest/interface/remove` with `{".id":"ether1"}` fails because `/interface` has no `remove` command:

```json
{"detail":"no such command or directory (remove)","error":400,"message":"Bad Request"}
```

| Reply | Cause |
| :-- | :-- |
| `401 Unauthorized` | Wrong username or password, the group has no `rest-api` policy, or the user's `address` does not allow the client. |
| `500`, `std failure: not allowed (9)` | The group has `rest-api` but no `api` policy. |
| `500`, `not enough permissions (9)` | The group lacks the policy for the command, for example `write` for a change or `test` for `ping`. |
| `400`, `missing or invalid resource identifier` | The router could not apply `PATCH` or `DELETE` to a record: no record ID in the URL (for example `PATCH` on a menu without records; use `POST` with `set`), a record that cannot be removed (an Ethernet interface), a value the router refused, or a user without the `write` policy. |
| `400`, `no such command or directory (x)` | The menu, command or record name `x` does not exist. |
| `400`, `no such command` | The command does not exist in the menu, or `GET` was sent to a command. |
| `400`, `no such command prefix` | The URL has a percent-encoded `*` (`%2A`) in an ID. |
| `400`, `unknown parameter x`, `invalid value for argument x`, `missing =x=`, `failure: ...` | The console refused the parameters; the detail is the console's error message. |
| `400`, `Failed to parse json` | The body is not valid JSON, or a number has an exponent. |
| `400`, `Session closed` | The command ran for 60 seconds, or the request waited behind a request of the same user that did. See [Keep commands within 60 seconds](#keep-commands-within-60-seconds). |
| `403 Forbidden` (HTML page) | The REST API is turned off for this protocol (`rest-plain` or `rest-secure` in `/ip/service/webserver`). |
| `404 Not Found` | No record has this ID. |
| `415 Unsupported Media Type` | The request has a body but no `Content-Type: application/json` header. |
| Connection reset | The client address is not in the service's `available-from`. |
| TLS or certificate error | The client does not trust the certificate, the URL names the router differently from the certificate, or `www-ssl` has no certificate. |

The log records REST logins in the `account` topic: `user monitoring logged in from 192.168.88.10 via rest-api`, followed by a login `via api`. A group without the `api` policy logs `login failure for user monitoring via api` after the REST login:

```ros
/log/print where topics~"account"
```

`/user/active` lists each REST login twice: once `via rest-api` with the client address, and once `via api` without an address.

## Technical details

### Sessions

- The REST server logs in to the API with the user's credentials and keeps that login for 10 minutes. Requests in that time use it, whether they come over one HTTP connection or several; the next request after the 10 minutes logs in again.
- A change to the user with `/user/set` (password, `disabled`, `address`) or `/user/remove` applies to the next request. A change to the group's policies applies when the login is renewed, up to 10 minutes later.
- The requests of one user run one at a time; requests of different users run in parallel.

### JSON format

The router broadly follows the ECMA-404 JSON standard:

- Replies encode every value as a string, even when the property holds a number or a boolean.
- A JSON number in a request can be octal (leading `0`, `010` is 8) or hexadecimal (`0x` prefix). A number with an exponent (`2e0`) is refused with `Failed to parse json`.
- A number sent as a string is read the way the console reads it: `"5"` is 5 and `"0x4"` is 4.

### HTTP

- The router uses HTTP/1.1 and keeps connections open (keep-alive), which saves the TCP and TLS setup of the next request.
- A request without credentials gets `401` with `WWW-Authenticate: Basic`.
- `PUT` answers `201 Created` with the new record's URL in the `Location` header, for example `Location: https://192.168.88.1/rest/ip/address/*18`. `DELETE` answers `204 No Content`.
- Error replies of the REST API are JSON objects; a part of the web server turned off in `/ip/service/webserver` answers with an HTML `403` page.
