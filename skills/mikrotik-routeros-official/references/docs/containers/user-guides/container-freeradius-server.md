# Container - FreeRADIUS server

> Run a FreeRADIUS server in a RouterOS container, add a RADIUS client and a user, and log in to the router with that user.

# Container - FreeRADIUS server

## Introduction

With containers, RouterOS can run servers that would otherwise need a separate device or machine on your network.

[RADIUS](../../authentication-authorization-accounting/radius.md) (Remote Authentication Dial-In User Service) lets RouterOS check user names and passwords against a central server, for example for [PPP](../../mobile-networking/ppp.md), [PPPoE](../../virtual-private-networks/pppoe/index.md), [L2TP](../../virtual-private-networks/l2tp/index.md), HotSpot and router logins. This guide runs the [FreeRADIUS](https://www.freeradius.org/) server in a container on the router, adds one user, and logs in to the router with it.

The image is [freeradius/freeradius-server on Docker Hub](https://hub.docker.com/r/freeradius/freeradius-server). Check its [tags](https://hub.docker.com/r/freeradius/freeradius-server/tags) for the architectures it is available for; the `alpine` tags are smaller and use other configuration paths than this guide.

## Summary

Read the [container](../) guide first, especially the [disclaimer](../#disclaimer) and the [requirements](../#requirements): the `container` package must be installed and containers enabled in device-mode.

The image takes about 90 MB to download and more after extraction, so this example extracts it to an external disk, `disk1`.

:::warning

This guide shows a basic configuration for testing. See the [FreeRADIUS documentation](https://www.freeradius.org/documentation/) for other options. Before using the server in production, use strong secrets and passwords, and run the server without debug mode.

:::

## Container configuration

### Networking

Add a veth interface for the container:

```routeros
/interface/veth/add name=veth3 address=172.20.0.2/24 gateway=172.20.0.1
```

Create a bridge for the container, give it an address, and add the veth interface to it:

```routeros
/interface/bridge/add name=freeradius
/ip/address/add address=172.20.0.1/24 interface=freeradius
/interface/bridge/port/add bridge=freeradius interface=veth3
```

The router sends its RADIUS requests to the server from the bridge address, `172.20.0.1`.

If the container needs internet access, add NAT for its outgoing traffic:

```routeros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.20.0.0/24
```

### Image

This example downloads the image from Docker Hub (see [Registry](../#registry)); you can also import it from a [.tar](../#option-b-import-image-from-pc) file. Set the directory where the downloaded image is extracted:

```routeros
/container/config/set tmpdir=disk1/pull
```

Add the container:

```routeros
/container/add remote-image=freeradius/freeradius-server:latest \
    interface=veth3 root-dir=disk1/freeradius logging=yes cmd="-X" \
    name=freeradius
```

`cmd="-X"` starts FreeRADIUS in debug mode: it writes every request and its result to the log, which helps while you set up the server.

RouterOS downloads and extracts the image. Check the progress with `/container/print`; when the extraction is done, the container status is `stopped`.

### Start the container

```routeros
/container/start [find where name=freeradius]
```

With container logging enabled, the [log](../../diagnostics-monitoring-and-troubleshooting/log/index.md) shows the server start (`/log/print where topics~"container"`, some lines left out):

```text
2026-11-24 07:11:43 container,info,debug freeradius: FreeRADIUS Version 3.2.10 
 2026-11-24 07:11:44 container,info,debug freeradius: Listening on auth address * port 1812 bound to server default
 2026-11-24 07:11:44 container,info,debug freeradius: Listening on acct address * port 1813 bound to server default
 2026-11-24 07:11:44 container,info,debug freeradius: Ready to process requests
```

## Server configuration

The server's configuration files are in the container's root directory, under `disk1/freeradius/etc/freeradius`. Download them with SFTP (the SSH [service](../../system-information-and-utilities/services.md) must be enabled), edit them, and upload them back. This guide changes two files:

- `clients.conf` - the RADIUS clients (devices such as the router) that may send requests to the server;
- `mods-config/files/authorize` - the users.

Download both files:

```shell
sftp admin@192.168.88.1
sftp> cd disk1/freeradius/etc/freeradius
sftp> ls
README.rst          certs               clients.conf        dictionary          
experimental.conf   hints               huntgroups          mods-available      
mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       
templates.conf      trigger.conf        users               
sftp> get clients.conf
sftp> cd mods-config/files
sftp> get authorize
sftp> exit
```

### Clients

`clients.conf` comes with many commented examples; see the [FreeRADIUS documentation](https://wiki.freeradius.org/config/Configuration-files) for all options. For this example, replace its content with:

```text
client router {
    ipaddr = 172.20.0.1
    secret = Example-secret-1
}
```

- `ipaddr` - the address that the router sends its requests from, the bridge address. The server ignores requests from addresses that are not listed.
- `secret` - the shared secret, which must match the `secret` of the RADIUS entry on the router. Use a long random string.

### Users

In `authorize`, find the commented line for the user `bob`:

```text
#bob	Cleartext-Password := "hello"
```

Remove the `#` and set a password; leave the other lines as they are:

```text
bob	Cleartext-Password := "Example-pass-1"
```

This adds the user `bob`. To add more users, add more lines in the same format.

### Upload the files

Upload both files to the folders that you downloaded them from:

```shell
sftp admin@192.168.88.1
sftp> cd disk1/freeradius/etc/freeradius
sftp> put clients.conf
sftp> cd mods-config/files
sftp> put authorize
sftp> exit
```

Restart the container to load the new configuration:

```routeros
/container/restart [find where name=freeradius]
```

## Log in with a RADIUS user

Add the server to the router's RADIUS client, for router logins, with the secret from `clients.conf`:

```routeros
/radius/add service=login address=172.20.0.2 secret="Example-secret-1"
```

Let router logins use RADIUS:

```routeros
/user/aaa/set use-radius=yes
```

Log in to the router as `bob` with SSH, WinBox or WebFig. To test from the router's own terminal, connect with SSH to one of the router's addresses; the first time, confirm the host key, then enter bob's password:

```routeros
/system/ssh 172.20.0.1 user=bob
```

In bob's session, list the sessions that RADIUS authenticated:

```routeros
/user/active/print proplist=name,via,group where radius
```

```text
Flags: R - RADIUS
Columns: NAME, VIA, GROUP
#   NAME  VIA  GROUP
0 R bob   ssh  read 
```

The `R` flag shows that RADIUS authenticated the session. `bob` has the group `read`, the `default-group` of `/user/aaa`, because the server does not send a group for this user. See [Log in to the router with RADIUS accounts](../../authentication-authorization-accounting/radius.md#log-in-to-the-router-with-radius-accounts) for how to set the group on the server, and what to keep in mind when RADIUS accounts can log in to the router.

The container log shows the request and the answer:

```text
2026-11-24 07:12:37 container,info,debug freeradius: (0) Received Access-Request Id 0 from 172.20.0.1:37287 to 172.20.0.2:1812 length 152
2026-11-24 07:12:37 container,info,debug freeradius: (0) Sent Access-Accept Id 0 from 172.20.0.2:1812 to 172.20.0.1:37287 length 197
```

## Troubleshooting

With `cmd="-X"`, the container log shows why the server rejects or ignores a request.

The router's address is not in `clients.conf`; the server does not answer, and the login fails after the RADIUS timeout:

```text
 2026-11-24 07:22:15 container,info,debug freeradius: Ignoring request to auth address * port 1812 bound to server default from unknown client 172.20.0.1 port 51256 proto udp
```

The `secret` on the router does not match `clients.conf`; the server does not answer, and `/radius/monitor` counts timeouts:

```text
 2026-11-24 07:12:49 container,info,debug freeradius: Dropping packet without response because of error: Received packet from 172.20.0.1 with invalid Message-Authenticator!  (Shared secret is incorrect.) (from client router)
```

The password is wrong; the server rejects the login:

```text
 2026-11-24 07:12:55 container,info,debug freeradius: (7) mschap: ERROR: MS-CHAP2-Response is incorrect
 2026-11-24 07:12:56 container,info,debug freeradius: (7) Sent Access-Reject Id 5 from 172.20.0.2:1812 to 172.20.0.1:52158 length 121
```

For more checks on the router side, see [Check and troubleshoot](../../authentication-authorization-accounting/radius.md#check-and-troubleshoot) on the RADIUS page.

For the commands used in this guide, see [`/container`](../../cli-reference/container/container.md), [`/container/config`](../../cli-reference/container/config), [`/radius`](../../cli-reference/radius/radius.md) and [`/user/aaa`](../../cli-reference/user/aaa).
