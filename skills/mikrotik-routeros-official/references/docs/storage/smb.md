# SMB

> RouterOS includes a built-in SMB server for file sharing over SMB/CIFS protocols, supporting SMB2.1, 3.0, and 3.1.1. Users can configure server settings, shares, and user permissions through /ip/smb, /ip/smb/shares,...

# SMB

RouterOS includes a built-in **SMB server** for sharing folders of the router with network clients. In addition, the [Storage package](./) adds an **SMB client** that lets RouterOS mount remote SMB shares as disks.

## SMB server

**Sub-menu:** `/ip/smb` **Packages required:** `system`

SMB server provides file sharing access to configured folders of the router, allowing network clients to browse, read, write, and manage files stored on the router's storage media over the SMB/CIFS protocol. This enables the router to function as a simple network-attached storage (NAS) device for local network sharing of files, backups data, or router configuration backups files.

:::warning
RouterOS only supports SMB2.1, SMB3.0, and SMB3.1.1. SMB1 is not supported due to security vulnerabilities.

SMB is not supported on SMIPS devices.
:::

The server starts on its own once the first share is added (`enabled=auto` is the default; see [`/ip/smb`](../cli-reference/ip/smb/) for the settings), it can also be limited to specific interfaces and renamed.

### Shares

**Sub-menu:** `/ip/smb/shares`

[`/ip/smb/shares`](../cli-reference/ip/smb/shares) configures the share names and directories accessible over SMB. If the directory provided in the configuration does not exist, it will be created automatically. Access can be limited per share with `valid-users` / `invalid-users`, enforced encryption with `require-encryption` (recommended for macOS clients), and read-only access with `read-only`.

### Users

**Sub-menu:** `/ip/smb/users`

[`/ip/smb/users`](../cli-reference/ip/smb/users) sets up the users that can access the router's SMB shares. Each user has a name, a password, and a `read-only` restriction (default: yes) that applies across all shares. A default `guest` user is created automatically and is disabled by default.

### Example

To make the RouterOS folder available through the SMB service follow these steps:

- Create a user.

```ros
/ip/smb/users/add read-only=no name=mtuser password=mtpasswd
```

- add shared folder.

```ros
/ip/smb/shares/add directory=backup name=backup
```

- enable SMB service:

```ros
#this step is optional, as the default is "enabled=auto"
/ip/smb/set enabled=yes
```

Now check for results:

- Check general service settings.

```ros
/ip/smb/print
      enabled: yes
        status: enabled
        domain: MSHOME
       comment: MikrotikSMB
    interfaces: all
```

- SMB user settings

```ros
/ip/smb/users/print
Flags: X - DISABLED; * - DEFAULT; r - READ-ONLY
Columns: NAME, PASSWORD
#     NAME    PASSWORD
0 X*r guest          
1     mtuser  mtpasswd
```

- And finally SMB shares settings.

```ros
/ip/smb/shares/print
Flags: X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION
#    NAME    DIRECTORY  REQUIRE-ENCRYPTION
;;; default share
0 X* pub     /pub       no               
1    backup  backup     no
```

Now, additional configuration changes can be done, like disabling the default user and share, etc.

## SMB client

**Sub-menu:** `/disk` **Packages required:** [Storage package](./)

The Storage package adds an SMB client that mounts a remote SMB share as a local disk on the router. The package currently supports SMB2.1, SMB3.0, and SMB3.1.1 dialects (SMB1 is not supported due to security vulnerabilities).

### Configuration example

```ros
/disk/add smb-address=10.155.145.11 smb-share=share1 smb-user=user smb-password=password type=smb
```

The mounted share then appears as a disk in `/file` and can be managed like any other disk.
