# User

> RouterOS user management: local user database, user groups and policies, password complexity and expiry, session inactivity handling, SSH key authentication, and RADIUS authentication and accounting for management...

# User

The router user facility in `/user` manages the accounts that access the router with management tools: WinBox, WebFig, the console over SSH or Telnet, the API and the REST API. RouterOS authenticates users against the local user database or a RADIUS server. Each user belongs to exactly one user group, and the group's policies define what the user can do on the router. For hardening recommendations (per-administrator accounts, key login, service restrictions), see [Securing your router](../getting-started/securing-your-router).

## Create a user

The default configuration has one user, `admin`, in the `full` group. Create a group with the policies the users need, then add the users:

```ros
/user/group/add name=managers policy=ssh,read,write,password
/user/add name=john group=managers password="StrongPass123!"
```

```ros
[admin@MikroTik] > /user/group/print where name=managers
4  name="managers"
   policy=ssh,read,write,password,!local,!telnet,!ftp,!reboot,!policy,!test,
      !winbox,!web,!sniff,!sensitive,!api,!romon,!rest-api skin=default
```

Policies that are not listed are revoked from the group. Passwords accept any characters, including spaces and UTF-8. When you add a user, the password argument is mandatory; an explicitly empty password (`password=""`) allows logging in with a blank password.

Set `address` to an IP prefix to allow the user to log in only from matching source addresses:

```ros
/user/set john address=192.168.88.0/24
```

User names accept letters, digits and the characters `_` `.` `#` `-` `@`, must end with a letter or a digit, and cannot start with `.` or `-`.

For all user properties, see [`/user`](../cli-reference/user/) in the CLI reference.

## Change a password

Users change their own password with the `/password` command, in interactive mode or in one line:

```ros
/password old-password=StrongPass123! new-password=NewStrongPass456 confirm-new-password=NewStrongPass456
```

The user's group must include the `password` policy, otherwise the command fails with "not enough permissions".

An administrator changes another user's password with `/user/set`:

```ros
/user/set john password="NewStrongPass456"
```

To force a user to set a new password at the next login, expire the current password:

```ros
/user/expire-password john
```

```ros
[admin@MikroTik] > /user/print where name=john
Flags: E - EXPIRED
Columns: NAME, GROUP, ADDRESS, INACTIVITY-POLICY
#   NAME  GROUP     ADDRESS          INACTIVITY-POLICY
2 E john  managers  192.168.88.0/24  none
```

At the next interactive login the router asks the user for a new password; a new password set by an administrator also clears the `E` flag.

Require stronger passwords with the complexity settings in [`/user/settings`](../cli-reference/user/settings): `minimum-password-length` and `minimum-categories` (how many of the groups digits, lowercase letters, uppercase letters and symbols the password must contain).

## User groups

Groups assign access rights to users. The full list of policies and what each one grants is in [`/user/group`](../cli-reference/user/group).

RouterOS has three default groups which cannot be deleted:

```ros
[admin@MikroTik] > /user/group/print
0  name="read"
   policy=local,telnet,ssh,reboot,read,test,winbox,password,web,sniff,
      sensitive,api,romon,rest-api,!ftp,!write,!policy skin=default

1  name="write"
   policy=local,telnet,ssh,reboot,read,write,test,winbox,password,web,sniff,
      sensitive,api,romon,rest-api,!ftp,!policy skin=default

2  name="full"
   policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,
      web,sniff,sensitive,api,romon,rest-api
```

:::warning
Even the `read` group includes the `reboot` and `sensitive` policies. Do not give it to untrusted users; create a custom group with only the policies they need instead.
:::

The exclamation mark `!` in front of a policy revokes it from the group.

## Lock or close inactive sessions

Set `inactivity-timeout` (range 1 minute to 24 hours) and `inactivity-policy` on a user to handle idle console sessions:

- `logout` closes the idle session with the message "`<name>` was logged out due to inactivity".
- `lockscreen` locks the session and asks for the user's password to resume it; <kbd>Control</kbd>+<kbd>D</kbd> closes the locked session.

## SSH keys

The `/user/ssh-keys` menu stores public SSH keys assigned to users, and `/user/ssh-keys/private` stores the private keys that identify the router itself when it connects to other devices with SSH, for example with `/system/ssh` or `/tool/fetch`.

:::warning
When a user has an SSH key assigned, SSH no longer accepts password authentication for that user. See the [SSH](../management-tools/ssh) page for the supported configurations.
:::

Upload the key file to the router and import it for a user:

```ros
/user/ssh-keys/import public-key-file=mykey.pub user=john info="john laptop"
```

```ros
[admin@MikroTik] > /user/ssh-keys/print where user=john
Columns: USER, KEY-TYPE, BITS, INFO
#  USER  KEY-TYPE  BITS  INFO
1  john  ed25519    256  john laptop
```

Public key import accepts OpenSSH one-line, PKCS#1 PEM (`BEGIN RSA PUBLIC KEY`) and PKCS#8/SPKI PEM (`BEGIN PUBLIC KEY`) files. You can also paste an OpenSSH-format key directly with `/user/ssh-keys/add key="ssh-ed25519 AAAA..." user=john`; a comment at the end of the key string becomes the key's `info`.

Private key import accepts PKCS#1 PEM (`BEGIN RSA PRIVATE KEY`) and PKCS#8 files, plain (`BEGIN PRIVATE KEY`) and encrypted (`BEGIN ENCRYPTED PRIVATE KEY`, requires the `passphrase` argument):

```ros
/user/ssh-keys/private/import private-key-file=routerkey.pem user=john passphrase=keypass
```

OpenSSH-format private keys (`BEGIN OPENSSH PRIVATE KEY`) are not accepted. For all properties, see [`/user/ssh-keys`](../cli-reference/user/ssh-keys/) and [`/user/ssh-keys/private`](../cli-reference/user/ssh-keys/private/) in the CLI reference.

## RADIUS authentication

Router user remote AAA authenticates management logins against a RADIUS server and sends it accounting records. Configure the RADIUS client first: add a [`/radius`](../cli-reference/radius/) entry with `service=login`, then enable [`/user/aaa`](../cli-reference/user/aaa). For the RADIUS server, any RouterOS with the [User Manager](user-manager) package works:

```ros
# on the RADIUS server
/user-manager/set enabled=yes
/user-manager/router/add name=main address=192.168.88.24 shared-secret=radiusSecret
/user-manager/user/add name=john-remote password=JohnPass456

# on the router the users log in to
/radius/add service=login address=192.168.88.36 secret=radiusSecret
/user/aaa/set use-radius=yes
```

User Manager allows one concurrent login per user by default (`shared-users`); a second login with the same name is refused while the first session is active.

RADIUS is consulted only for user names that do not exist in the local user database; a local user with the same name always takes precedence. RADIUS-authenticated users get `default-group` (`read` by default), unless the server sends a `Mikrotik-Group` attribute naming a different local group (in User Manager, set it on the user with `attributes="Mikrotik-Group:full"`). Groups listed in `exclude-groups` are never accepted from the server and the user gets `default-group` instead.

Active RADIUS-authenticated sessions show the `R` (radius) flag in `/user/active/print`.

## Monitor active sessions

`/user/active/print` shows the connected management sessions:

```ros
[admin@MikroTik] > /user/active/print
Flags: R - RADIUS
Columns: WHEN, NAME, ADDRESS, VIA
#   WHEN                 NAME         ADDRESS        VIA
0 R 2026-09-25 09:32:20  john-remote  192.168.88.17  ssh
```

Close a session with `/user/active/remove`:

```ros
/user/active/remove [find name=john-remote]
```

For the session properties, including the `M` (by-romon) flag and the full `via` list, see [`/user/active`](../cli-reference/user/active).

## Technical details

### Expired password flow

`/user/expire-password` sets the `E` flag on the user. At the next interactive login the router prints "Change your password (Ctrl-C to skip)", then asks for "new password" and "repeat new password"; a mismatch prints "New passwords do not match!" and the prompt repeats. Pressing <kbd>Control</kbd>+<kbd>C</kbd> skips the change. Non-interactive sessions (command execution over SSH) are not prompted. Setting a new password for the user clears the flag.

### RADIUS authentication and accounting

- Password logins forwarded to RADIUS are authenticated with MS-CHAPv2 (the Access-Request carries `MS-CHAP-Challenge` and `MS-CHAP2-Response`).
- With `accounting=yes` the router sends an Accounting-Request (Start) at login and (Stop) at logout; `interim-update` sets the interval for Interim-Update messages while a session is active. Management session accounting carries no bandwidth counters.
- The `radius` log topic shows the exact attributes exchanged: `/system/logging/add topics=radius`.

## Read more

- [`/user`](../cli-reference/user/), [`/user/settings`](../cli-reference/user/settings), [`/user/group`](../cli-reference/user/group), [`/user/active`](../cli-reference/user/active), [`/user/aaa`](../cli-reference/user/aaa), [`/user/ssh-keys`](../cli-reference/user/ssh-keys/) in the CLI reference
- [RADIUS client](radius)
- [User Manager](user-manager)
- [SSH](../management-tools/ssh)
