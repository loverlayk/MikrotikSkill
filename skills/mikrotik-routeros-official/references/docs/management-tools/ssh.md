# SSH

> RouterOS includes a built-in SSH server and client. The server is customizable (ciphers, key types, forwarding, password and public-key authentication) and its host key can be exported, imported and regenerated. The...

# SSH

RouterOS provides an SSH (SSH v2) server for managing the router remotely, and an SSH client for connecting from the router to other devices. It has two client commands: [`/system/ssh`](../cli-reference/system/ssh) for interactive sessions and manual commands, and [`/system/ssh-exec`](../cli-reference/system/ssh-exec) for non-interactive use in scripts and the scheduler.

## SSH server

The SSH server is enabled by default and listens for incoming connections on port TCP/22. You can change the port and disable the server under the [Services](../system-information-and-utilities/services) menu.

See the [`/ip/ssh`](../cli-reference/ip/ssh) CLI reference for parameter descriptions.

### Server host key

The router's SSH host key is generated automatically. Show the fingerprint of the current key with:

```ros
/ip/ssh/print
```

The read-only `host-key-fingerprint` value lets an administrator confirm they are connecting to the right router.

Create a new host key pair, for example after the old key leaked, with:

```ros
/ip/ssh/regenerate-host-key
```

Changing `host-key-type` also regenerates the key immediately. After either change, SSH clients that pinned the old key report a fingerprint mismatch; distribute the new fingerprint (`/ip/ssh/print`) or update the pinned entries.

The default host key type is Ed25519 on new installations; routers upgraded from older RouterOS versions keep their RSA key.

Move the host key to another router (for example when replacing hardware) with [`export-host-key`](../cli-reference/ip/ssh/export-host-key) and [`import-host-key`](../cli-reference/ip/ssh/import-host-key). Exported files are named after `key-file-prefix`, for example `bbu_rsa.pem` and `bbu_rsa_pub.pem` for an RSA key with `key-file-prefix=bbu`.

### Log in with a public key

To enable PKI authentication for incoming connections, import the public key of the connecting user. Generate the key pair on the connecting device first (see [Log in with an SSH key](#log-in-with-an-ssh-key)), upload the public key file to the router, and import it for the user:

```ros
/user/ssh-keys/import public-key-file=id_rsa.pub user=admin
```

When at least one key is assigned to a user, password login is refused for that user (with the default `password-authentication=yes-if-no-key`). More about supported key formats in the [User SSH keys](../authentication-authorization-accounting/user#ssh-keys) section.

## SSH client

The interactive [`/system/ssh`](../cli-reference/system/ssh) command connects the router to a remote host over SSH. It is used from the console; for scripts and the scheduler, use [`ssh-exec`](#run-remote-commands-from-scripts).

### Log in to a remote host

Connect to a remote host and initiate an SSH session. The address works with IPv4 and IPv6:

```ros
/system/ssh 192.168.88.3
/system/ssh 2001:db8:add:1337::beef
```

The command passes the username of the router account you are logged in as. Use `user=<username>` to log in as a different user:

```ros
/system/ssh 192.168.88.3 user=noc
/system/ssh 2001:db8:add:1337::beef user=noc
```

### Log in from a specific address of the router

To log in to a host from a specific source address (for example for firewall rules or testing), use the `src-address=<ip address>` argument. The address works with IPv4 and IPv6:

```ros
/system/ssh 192.168.88.3 src-address=192.168.89.2
/system/ssh 2001:db8:add:1337::beef src-address=2001:db8:bad:1000::2
```

In this case, the SSH client binds to the specified address and then initiates the SSH connection to the remote host.

### Log in with an SSH key

RouterOS cannot generate user key pairs on its own, so the key pair has to come from elsewhere. Either generate an RSA or Ed25519 key pair on your management device, or reuse the router's own host key pair: export it with [`/ip/ssh/export-host-key`](../cli-reference/ip/ssh/export-host-key) and import the exported private key file.

Upload the private key file to the router (with the Files menu in WinBox or over SFTP) and import it for the user that makes the outgoing connection:

```ros
/user/ssh-keys/private/import user=admin private-key-file=id_rsa
```

Only a user with full rights on the router can change the `user` attribute value under `/user/ssh-keys/private`.

The key file must be in PEM format (PKCS#1, PKCS#8, or encrypted PKCS#8). Keys in the OpenSSH private key format ("BEGIN OPENSSH PRIVATE KEY") are rejected; generate the key with `ssh-keygen -m PEM` or convert an existing one with `ssh-keygen -p -m PEM`.

The corresponding public key must be installed on the SSH server side (for RouterOS servers, see [Log in with a public key](#log-in-with-a-public-key)). With the private key imported, SSH sessions log in without a password:

```ros
/system/ssh 192.168.88.3
```

Watch how to log in with an [RSA key](http://youtube.com/watch?v=8tt7fSvdFRM) or [Ed25519 key](http://youtube.com/watch?v=be-pBwhjRWA).

### Verify remote host keys

Without verification, the SSH client accepts any host key, which makes the connection vulnerable to an on-path attacker. Client host key verification is controlled by `known-hosts-validation` in [`/ip/ssh`](../cli-reference/ip/ssh/): it is enabled by default on new installations; routers upgraded from older RouterOS versions keep the previous setting, so validation stays off there until you enable it.

Trusted server keys are kept in [`/ip/ssh/known-hosts`](../cli-reference/ip/ssh/known-hosts).

With validation enabled, the interactive client asks on the first connection to a new server and pins the key on confirmation:

```text
host key not trusted: SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
do you want to trust this host key? <y/n>
```

When a server later presents a different key than the pinned one, the client does not proceed silently and asks whether to update the stored key:

```text
host key mismatch for 192.168.88.3
old fingerprint: SHA256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
new fingerprint: SHA256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
do you want to update the host key? <y/n>
```

Non-interactive commands cannot ask: `ssh-exec` (and fetch over SFTP) fails with `host key not trusted` for an unknown or mismatched server. For scripted connections, pin the server key in advance, pass `known-hosts-ignore=yes` to skip validation for that one command, or set `known-hosts-trusted-subnets` to skip validation for whole subnets, for example a management network.

Pin a server's key in advance with its public key — get the OpenSSH-format key line (`<type> <base64>`) from the server's administrator or from a workstation with `ssh-keyscan 192.168.88.3`, and add it:

```ros
/ip/ssh/known-hosts/add host=192.168.88.3 key="ssh-ed25519 AAAA..." \
    comment="backup server"
```

Answering `y` to the interactive client's trust prompt pins the key the same way, so a scripted `ssh-exec` that failed with `host key not trusted` works after one interactive `/system/ssh` login where you confirm the key.

With validation disabled, no host key is asked about or stored, and any key is accepted.

### Run a command on a remote host

To execute a remote command, supply it at the end of the log-in line:

```ros
/system/ssh 192.168.88.3 "/ip/address/print"
/system/ssh 192.168.88.3 command="/ip/address/print"
/system/ssh 2001:db8:add:1337::beef "/ip/address/print"
/system/ssh 2001:db8:add:1337::beef command="/ip/address/print"
```

:::note
The MikroTik SSH server does not provide pseudo-tty (the `ssh -T` mode in OpenSSH). Multiline commands, for example `"/ip/address \n add address=1.1.1.1/24"`, fail on older RouterOS versions; RouterOS 7.25 and later execute them.
:::

If you wish to execute remote commands through **scripts** or **scheduler**, use the [`ssh-exec`](../cli-reference/system/ssh-exec) command.

## Run remote commands from scripts

The `ssh-exec` command is a non-interactive SSH command, allowing you to execute commands on a remote device through scripts and the scheduler. See the [`ssh-exec`](../cli-reference/system/ssh-exec) CLI reference for parameter descriptions.

### Retrieve information

The command returns two values:

- **exit-code**: the exit code reported by the remote command shell — `0` when the command ran; a command that `exit`s sets that code. Failures of RouterOS commands instead come back as error text in `output`
- **output**: returns the output of the remotely executed command, including error messages like `input does not match any value...` when the remote command fails

**Example:** The following code retrieves the link status of ether1 from device 10.10.10.1 and outputs the result to "Log". The example assumes the user `remote` is set up for public-key authentication (no `password=` on the command line) and that the server's host key is pinned, as required by [host key verification](#verify-remote-host-keys) on new installations:

```ros
:local res ([/system/ssh-exec address=10.10.10.1 user=remote \
    command=":put ([/interface ethernet monitor ether1 once as-value]->\"status\")" \
    as-value])
:log info ($res->"output")
```

:::warning
Do not put a plain-text password in the `password` parameter on the command line; it ends up in scripts and command history. Use SSH PKI authentication for users on both sides instead.

The user group and script policy executing the command require **test** permission.
:::

Watch how to [execute commands through SSH](http://youtube.com/watch?v=JfGfPSicTzs).

See the [`/ip/ssh`](../cli-reference/ip/ssh/), [`/system/ssh`](../cli-reference/system/ssh) and [`/system/ssh-exec`](../cli-reference/system/ssh-exec) CLI references for all parameters.
