# SMB

> RouterOS includes a built-in SMB server for file sharing over SMB/CIFS protocols, supporting SMB2.1, 3.0, and 3.1.1. Users can configure server settings, shares, and user permissions through /ip/smb, /ip/smb/shares,...

# SMB

RouterOS includes an **SMB server** for sharing folders of the router with network clients, and an **SMB client** that mounts remote SMB shares as disks. Both are part of the base system; the [Storage package](./) is not needed.

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

[`/ip/smb/users`](../cli-reference/ip/smb/users) sets up the users that can access the router's SMB shares. Each user has a name, a password, and a `read-only` restriction (default: yes) that applies across all shares. A default `guest` user is created automatically; it has read-only access to the shares without a password. Disable it unless anyone in the network may read the shares.

### Example

To make a folder of the router available through SMB:

1. Create a user:

   ```routeros
   /ip/smb/users/add read-only=no name=mtuser password=mtpasswd
   ```

2. Create the folder and the share. When the folder exists, clients can open the share:

   ```routeros
   /file/add name=backup type=directory
   /ip/smb/shares/add directory=backup name=backup
   ```

3. Disable the `guest` user, so that only `mtuser` can open the share:

   ```routeros
   /ip/smb/users/disable guest
   ```

The server starts when the first share is added (`enabled=auto`); `/ip/smb/set enabled=yes` starts it in any case. Check the settings:

```text
/ip/smb/print
     enabled: auto       
      status: enabled    
      domain: MSHOME     
     comment: MikrotikSMB
  interfaces: all
```

```text
/ip/smb/users/print
Flags: X - DISABLED; * - DEFAULT; r - READ-ONLY
Columns: NAME
#     NAME  
0 X*r guest 
1     mtuser
```

The default share `pub` is disabled:

```text
/ip/smb/shares/print
Flags: X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION
#    NAME    DIRECTORY  REQUIRE-ENCRYPTION
0 X* pub     /pub       no                
1    backup  /backup    no
```

A Linux client connects with, for example, `smbclient //192.168.88.1/backup -U mtuser`. SMB1 clients cannot connect.

## SMB client

**Sub-menu:** `/disk`

The SMB client mounts a remote SMB share as a disk on the router. It supports the SMB2.1, SMB3.0, and SMB3.1.1 dialects; SMB1 is not supported.

### Configuration example

```routeros
/disk/add type=smb smb-address=10.0.2.2 smb-share=share1 \
    smb-user=smbu smb-password=<password>
```

The share is mounted as `smb-<address>-<share>`, here `smb-10-0-2-2-share1`, and its files appear in `/file` like the files of any other disk.
