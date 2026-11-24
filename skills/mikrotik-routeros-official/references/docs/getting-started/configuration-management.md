# Configuration Management

> Manage the RouterOS configuration: undo and redo changes, use safe mode to avoid locking yourself out, export the configuration as a script and import it on another router, run scripts automatically after upload, and...

# Configuration Management

RouterOS records every configuration change, so you can undo it, and offers safe mode, which
undoes your changes when the connection to the router is lost. The configuration can be exported
as a script, imported on the same or another router, and reset to the defaults. For a binary copy
of the whole configuration, see [Backup](./backup).

## Undo and redo changes

Every configuration change, made from the CLI, WinBox, WebFig or the API, is recorded in
`/system/history`. The `/undo` and `/redo` commands, or the Undo and Redo buttons in WinBox,
take back the last change or apply it again. Each further `/undo` takes back the change before it. The history keeps the last 100 changes and is cleared when the router reboots.

Add a firewall rule and look at the history:

```routeros
/ip/firewall/filter/add chain=forward action=drop
/system/history/print
```

```text
Flags: U - UNDOABLE
Columns: ACTION, BY, POLICY, TIME
  ACTION              BY     POLICY  TIME
U filter rule added   admin  write   2026-11-23 09:39:35
U user admin changed  admin  write   2026-11-23 09:39:34
                             policy
```

Undo the change. The rule is removed, and the history marks the action as redoable (`R`):

```routeros
/undo
/system/history/print
```

```text
Flags: U - UNDOABLE, R - REDOABLE
Columns: ACTION, BY, POLICY, TIME
  ACTION              BY     POLICY  TIME
R filter rule added   admin  write   2026-11-23 09:39:35
U user admin changed  admin  write   2026-11-23 09:39:34
                             policy
```

`/redo` adds the rule again. The detailed history shows the commands that undo and redo each
action, also for changes made over the API or in the GUI:

```routeros
/redo
/system/history/print detail proplist=action,redo,undo
```

```text
Flags: U - UNDOABLE
U action="filter rule added"
  redo=/ip firewall filter add action=drop chain=forward
  undo=/ip firewall filter remove *1

U action="user admin changed"
```

## Work safely with safe mode

A configuration change can cut your own connection to the router, for example a firewall rule or
a wrong address. Safe mode protects against this: if the session that holds safe mode ends
without releasing it, the router undoes every change made while safe mode was on, including changes made
from other sessions.

- In the CLI, press <kbd>Control</kbd>+<kbd>X</kbd> (or <kbd>F4</kbd>). The router answers
  `Taking Safe Mode session... Success!` and the prompt shows `<SAFE>`, for example
  `[admin@MikroTik] <SAFE>`.
- In WinBox, select **Safe Mode** in the toolbar.

![WinBox window with the Safe Mode button in the toolbar and an open terminal](./img/configuration-management-01.webp)

Changes made in safe mode are listed with the `F` (floating-undo) flag in `/system/history/print`.
How the session ends decides what happens to them:

| Action | Changes |
| :-- | :-- |
| <kbd>Control</kbd>+<kbd>X</kbd> again (`Releasing Safe Mode... Success!`) | Kept. Safe mode ends. |
| <kbd>Control</kbd>+<kbd>D</kbd> | Undone. The session ends. |
| `/quit`, then `y` at `You are in Safe Mode. Quitting will unroll changes. Quit? [y/N]:` | Undone. The session ends. |
| The client closes the connection, for example the terminal window is closed | Undone. |
| The connection is cut without being closed, for example by a firewall rule | Undone when the router detects that the session is gone, which can take about a quarter of an hour. |

If your connection drops and the old session still holds safe mode when you log in again, press <kbd>Control</kbd>+<kbd>X</kbd> and answer `u` to the question that follows to undo its
changes at once.

Pressing <kbd>Control</kbd>+<kbd>X</kbd> twice keeps the changes made so far and starts safe mode
again with an empty list. Change the configuration in small steps: safe mode remembers at most
100 changes. With more, the session leaves safe mode and no changes are undone.

Only one session can hold safe mode. When another session presses <kbd>Control</kbd>+<kbd>X</kbd>, the
router asks:

```text
Safe Mode is taken by current user in another session.
Unroll, release or abort [u/r]?
```

- `u` undoes the changes of the other session and gives safe mode to this session. The other
  session sees `Safe Mode unrolled by another user`.
- `r` keeps the changes of the other session and gives safe mode to this session. The other session
  sees `Safe Mode released by another user`.
- <kbd>Control</kbd>+<kbd>C</kbd> leaves safe mode with the other session.

## Export the configuration

The `export` command prints the configuration as RouterOS commands, which can be imported on the
same or another router. Run it from the root menu for the whole configuration, or from a menu for
that menu and its sub-menus. Export is a CLI command.

By default, the export contains only settings that differ from the defaults. Arguments:

- `file` writes the export to a file (`.rsc`) instead of the terminal.
- `verbose` also exports default values.
- `terse` writes every command on one line with its full menu path.
- `show-sensitive` includes passwords, keys and other secrets, which are left out by default (see
  [List of menus with sensitive parameters](./list-of-menus-with-sensitive-parameters)).
- `path` exports only the listed menus. A menu with `!` in front is left out.
- `where` exports only the items that match a condition.
- `compact` is the default and gives the same output as a plain `export`.

Arguments can be combined, for example `/export path=/ip/firewall,!/ip/firewall/nat file=fw`.

Export the addresses to the file `address.rsc`:

```routeros
/ip/address/add address=192.0.2.1/24 interface=ether1
/ip/address/export file=address
/file/print where name=address.rsc
```

```text
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME         TYPE    SIZE  LAST-MODIFIED
0 address.rsc  script   146  2026-11-23 09:39:50
```

Export the whole firewall configuration except NAT:

```routeros
/ip/firewall/address-list/add list=mylist address=198.51.100.1
/ip/firewall/address-list/add list=other address=198.51.100.2
/ip/firewall/nat/add chain=srcnat action=masquerade out-interface=ether1
/export path=/ip/firewall,!/ip/firewall/nat
```

```text
# 2026-11-23 09:40:04 by RouterOS 7.25.1
# system id = aX+jcgZWr+J
#
/ip firewall address-list
add address=198.51.100.1 list=mylist
add address=198.51.100.2 list=other
/ip firewall filter
add action=drop chain=forward
```

Export one address list:

```routeros
/ip/firewall/address-list/export where list=mylist
```

```text
# 2026-11-23 09:40:07 by RouterOS 7.25.1
# system id = aX+jcgZWr+J
#
/ip firewall address-list
add address=198.51.100.1 disabled=no dynamic=no list=mylist
```

If a menu does not answer the export command in time, the export prints
`#error exporting "/<menu>" (timeout)` for it and continues with the next menu.

:::warning
The export does not contain:

- User accounts and their passwords. User groups and SSH public keys (`/user/ssh-keys`) are
  exported, so create the users on the new router before you import.
- Certificates. Export and import them separately, see
  [Certificates](../../authentication-authorization-accounting/certificates#export-certificates).
- The databases of [The Dude](../../management-tools/dude) and
  [User Manager](../../authentication-authorization-accounting/user-manager).

Import the file on the same RouterOS version where possible: a command or parameter that does not
exist in the other version stops the import.
:::

### Default entries

Some menus contain built-in default entries, shown with the `*` flag. They cannot be removed, for
example `/ppp/profile/remove default` fails with `can not remove default profile`. The
export lists them only when you change them, with `set`, for example:

```text
/ppp profile
set *0 use-encryption=yes
```

| Menu | Default entries |
| :-- | :-- |
| `/interface/wireless/security-profiles` | default |
| `/ip/hotspot/profile` | default |
| `/ip/hotspot/user/profile` | default |
| `/ip/ipsec/mode-config` | request-only |
| `/ip/ipsec/policy` | the default template policy |
| `/ip/ipsec/policy/group` | default |
| `/ip/ipsec/profile` | default |
| `/ip/ipsec/proposal` | default |
| `/ip/smb/shares` | pub |
| `/ip/smb/users` | guest |
| `/ipv6/nd` | the entry for interface `all` |
| `/ppp/profile` | default, default-encryption |
| `/routing/bgp/template` | default |
| `/queue/type` | default, ethernet-default, wireless-default, synchronous-default, hotspot-default, pcq-upload-default, pcq-download-default, only-hardware-queue, multi-queue-ethernet-default, default-small |
| `/snmp/community` | public |
| `/system/logging` | the rules for info, error, warning and critical |
| `/system/logging/action` | memory, disk, echo, remote |

## Import a configuration

`/import` runs a script file (`.rsc`) line by line. The file can contain any console command,
including scripts.

```routeros
/ip/address/remove [find address="192.0.2.1/24"]
/import address.rsc
```

```text
Script file loaded and executed successfully
```

The import adds to the existing configuration and removes nothing. Firewall rules from the file are
added after the rules that are already there, also when they are the same, and an entry that
already exists, such as an address or an address-list entry, makes the import fail. On a router
with the default configuration, remove or adapt the default items that the file also contains
before you import.

The import stops at the first line that fails and reports it, for example:

```text
Script Error: failure: already have such address (/ip/address/add; line 5) (:import; line 1)
```

`line 5` is the line in the file. The lines before it stay applied. To replace the whole configuration of a router with a file,
export it with `show-sensitive` so that it contains passwords and keys, reset the router and run
the file instead of the default configuration (add `keep-users=yes`, as the file contains no
users):

```routeros
/system/reset-configuration no-defaults=yes keep-users=yes \
    run-after-reset=config.rsc
```

A failing line in such a file is logged as
`error while running run-after-reset script:` followed by the error.

### Check a file before you import it

`verbose=yes` prints each line with its number before it runs, so you can see where an import
stops. With `dry-run`, the router only checks the syntax and changes nothing: it does not find
entries that already exist. `from-line` starts the import at a
line of the file, for example to continue after you fixed the line that failed. `dry-run` and
`from-line` work only together with `verbose=yes`.

```routeros
/import address.rsc verbose=yes dry-run
```

```text
#line 1
# 2026-11-23 09:39:50 by RouterOS 7.25.1
#line 2
# system id = aX+jcgZWr+J
#line 3
#
#line 4
/ip address
#line 5
add address=192.0.2.1/24 interface=ether1 network=192.0.2.0
No syntax errors found in the import file
```

### Import automatically after upload

A file whose name ends in `.auto.rsc` runs as soon as it is uploaded over FTP or SFTP. The router
writes the result to a file with the same name and the `.auto.log` extension, for example
`Script file loaded and executed successfully`, or the script error. Files created on the router
or downloaded with `/tool/fetch` do not run automatically.

### Troubleshoot an import

Before you import an export from another router, check the file for:

- Interface names: renamed interfaces can clash with the default names on the new router. In this
  export, ether6 is renamed to ether2 while ether2 still exists, so the second line fails:

  ```routeros
  /interface/ethernet
  set [ find default-name=ether5 ] auto-negotiation=no name=ether1-gateway
  set [ find default-name=ether6 ] name=ether2
  set [ find default-name=ether7 ] name=ether3
  set [ find default-name=ether8 ] name=ether4
  set [ find default-name=ether1 ] name=ether5
  set [ find default-name=ether2 ] name=ether6
  set [ find default-name=ether3 ] name=ether7
  set [ find default-name=ether4 ] name=ether8
  ```

- Interfaces that do not exist on the new router: a command for a missing interface fails.
- Default entries written with `add` instead of `set` by an older version: change them to `set`.

Then check the syntax with `verbose=yes dry-run`, run the import with `verbose=yes` to find the
line that fails, fix the file, and continue with `from-line` from that line.

#### Startup delay

A script that runs at boot, for example a default configuration script or an import right after a
reset, can start before all interfaces exist. Wait for them before the commands that use them. This
script waits until there are at least 10 interfaces (count them on your router with
`/interface/print count-only`) or 30 seconds, and logs a warning if they did not appear:

```routeros
{
:local i 0
#Number of interfaces. It is necessary to reconfigure this number for each device (/interface/print count-only)
:local x 10
#Max time to wait
:local t 30
while ($i < $t && [:len [/interface/find]] < $x) do={
:put $i
:set $i ($i + 1)
:delay 1
}
if ($i = $t) do={
:log warning message="Could not load all physical interfaces"
} else={
#Rest of your script
}
}
```

## Reset the configuration

`/system/reset-configuration` removes the configuration, reboots the router and applies the default
configuration (see [Default configurations](./default-configurations)). In an interactive session
it asks `Dangerous! Reset anyway? [y/N]:` first. To reset with the button on the router, see
[RouterOS configuration reset](./routeros-configuration-reset).

- Users are removed, and `admin` gets its default password back: none, or the password printed
  on the device sticker. Without a password, the router asks you to set one at the first login.
- Before the reset, the router saves the old configuration to `auto-before-reset.backup`, so a
  reset made by mistake can be undone by [restoring it](./backup#restore-a-backup). Files on the router are kept.
- At the first interactive login after a reset, the router offers to show the software license.
- If a custom default configuration script is installed, for example with Netinstall or TR-069,
  the reset runs that script instead of MikroTik's default configuration.

Arguments change what the reset does, for example:

- `keep-users=yes` keeps users and their passwords.
- `no-defaults=yes` does not apply the default configuration.
- `skip-backup=yes` saves no backup.
- `run-after-reset` runs a script file after the reset instead of the default configuration. A
  script that runs longer than two minutes is stopped, and the log shows
  `error while running run-after-reset script: runtime limit exceeded` (in rare cases
  `std failure: timeout`).
- `caps-mode=yes` runs the CAPs mode script after the reset.
- `shutdown=yes` powers the router off instead of rebooting. It starts with the reset
  configuration when it is powered on.

Reset without the default configuration and without a backup:

```routeros
/system/reset-configuration no-defaults=yes skip-backup=yes
```

The same in WinBox:

![WinBox Reset Configuration dialog with No Default Configuration and Do Not Backup selected](./img/configuration-management-02.webp)

For all arguments, see [`/system/reset-configuration`](../../cli-reference/system/reset-configuration).

## Related topics

<DocCardList />
