# SSH

> RouterOS includes a built-in SSH server with customizable settings such as cipher configurations, key types, and forwarding options. It supports password and public-key authentication, with commands to export/import...

# SSH

## SSH Server

RouterOS has a built-in SSH (SSH v2) server that is enabled by default and listens for incoming connections on port TCP/22. You can change the port and disable the server under the [Services](../system-information-and-utilities/services) menu.

See the [`/ip/ssh`](../cli-reference/ip/ssh) CLI reference for parameter descriptions.

### Enabling PKI authentication

Example of importing a public key for user **admin**:

[Get the SSH key pair on the client device](#log-in-by-using-an-ssh-key) (the device you connect from). Upload the public SSH key to the router and import it.

More information about supported SSH keys can be found in [User SSH keys](../authentication-authorization-accounting/user#ssh-keys) section.

```ros
/user/ssh-keys/import public-key-file=id_rsa.pub user=admin
```

### SSH key pair generation

RouterOS does not support direct SSH key generation, which is available on Linux systems.

To obtain an SSH key pair (an SSH key pair is automatically generated on the first SSH connection), the device's SSH host key must be exported by using the [`export-host-key`](../cli-reference/ip/ssh/export-host-key) command.

## SSH Client

### Log in to a remote host

Connect to a remote host and initiate an SSH session. The IP address supports both IPv4 and IPv6.

```ros
/system/ssh 192.168.88.1
/system/ssh 2001:db8:add:1337::beef
```

In this case the username provided to the remote host is the one that has logged into the router. If another value is required, use `user=<username>`.

```ros
/system/ssh 192.168.88.1 user=lala
/system/ssh 2001:db8:add:1337::beef user=lala
```

### Log in from a specific IP address of the router

For testing or security reasons you may need to log in to another host by using a specific source address. Use the `src-address=<ip address>` argument. The IP address supports both IPv4 and IPv6.

```ros
/system/ssh 192.168.88.1 src-address=192.168.89.2
/system/ssh 2001:db8:add:1337::beef src-address=2001:db8:bad:1000::2
```

In this case, the SSH client binds to the specified address and then initiates an SSH connection to the remote host.

### Log in by using an SSH key

Example of importing an RSA private key for user *admin.*

First, export the SSH keys to a file:

```ros
/ip/ssh/export-host-key key-file-prefix=admin
```

Two files *admin\_rsa* and *admin\_rsa.pub* are generated. The pub file needs to be trusted on the SSH server side ([how to enable SSH PKI on RouterOS](./ssh#enabling-pki-authentication)). The private key must be added for the particular user.

```ros
/user/ssh-keys/private/import user=admin private-key-file=admin_rsa
```

:::danger
Only a user with full rights on the router can change the 'user' attribute value under `/user/ssh-keys/private`
:::

After the public key is installed and trusted on the SSH server, a PKI SSH session can be created.

```ros
/system/ssh 192.168.1.1
```

Watch how to log in with an [RSA key](http://youtube.com/watch?v=8tt7fSvdFRM) or [Ed25519 key](http://youtube.com/watch?v=be-pBwhjRWA).

### Executing remote commands

To execute a remote command, supply it at the end of the log-in line:

```ros
/system/ssh 192.168.88.1 "/ip/address/print"
/system/ssh 192.168.88.1 command="/ip/address/print"
/system/ssh 2001:db8:add:1337::beef "/ip/address/print"
/system/ssh 2001:db8:add:1337::beef command="/ip/address/print"
```

:::danger
If the server does not support pseudo-tty (ssh -T or ssh host command), like the MikroTik SSH server, you cannot send multiline commands through SSH.
:::

For example, sending a command `"/ip/address \n add address=1.1.1.1/24"` to a MikroTik router fails.

:::warning
If you wish to execute remote commands through **scripts** or **scheduler**, use the [`ssh-exec`](../cli-reference/system/ssh-exec) command.
:::

## SSH exec

The `ssh-exec` command is a non-interactive SSH command, allowing you to execute commands remotely on a device through scripts and scheduler. See the [`ssh-exec`](../cli-reference/system/ssh-exec) CLI reference for parameter descriptions.

### Retrieve information

The command returns two values:

- **exit-code**: returns 0 if the command execution succeeded
- **output**: returns the output of the remotely executed command

**Example:** The following code retrieves the interface status of ether1 from device 10.10.10.1 and outputs the result to "Log"

```ros
:local Status ([/system/ssh-exec address=10.10.10.1 user=remote command=":put ([/interface/ethernet/monitor [find where name=ether1] once as-value]->\"status\")" as-value]->"output")
:log info $Status
```

:::warning
For security reasons you should not use a plain text password with the "password" parameter specified in the command line. To ensure safe execution of the command remotely, you should use SSH PKI authentication for users on both sides.

The user group and script policy executing the command require **test** permission.
:::

Watch how to [execute commands through SSH](http://youtube.com/watch?v=JfGfPSicTzs).
