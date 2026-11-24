# Console

> The console provides text-based access to MikroTik RouterOS configuration and management features using text terminals, either remotely by using a serial port, telnet, SSH, or console screen within WinBox, or...

# Console

## Overview

The console is used for accessing the MikroTik Router's configuration and management features by using text terminals, either remotely by using a serial port, telnet, SSH, or console screen within [WinBox](./winbox), or directly by using a monitor and keyboard. The console is also used for writing scripts. This manual describes the general console operation principles. Consult the [Scripting Manual](../developer-guides/scripting) on some advanced console commands and on how to write scripts.

## Login Options

Console login options enable or disable various console features like color, terminal detection, and many others.

Additional login parameters can be appended to the login name after the '+' sign.

```text
    login_name ::= user_name [ '+' parameters ]
    parameters ::= parameter [ parameters ]
    parameter ::= [ number ] 'a'..'z'
    number ::= '0'..'9' [ number ]
```

If the parameter is not present, then the default value is used. If the number is not present, then the implicit value of the parameter is used.

Example: `admin+ct80w` - disables console colors, disables auto detection, and then sets terminal width to 80.
With an SSH client, use the extended name as the user name, for example
`ssh admin+ct@192.168.88.1`.

| Param | Default | Implicit | Description |
| :-- | :-- | :-- | :-- |
| **"w"** | auto | auto | Set terminal width |
| **"h"** | auto | auto | Set terminal height |
| **"c"** | on | off | Disable/enable console colors |
| **"t"** | off | on | Disable auto-detection of terminal capabilities |
| **"e"** | on | off | Enables "dumb" terminal mode |

## Banner and Messages

The login process displays the MikroTik banner and short help after validating the user name and password.

```text
  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.25.2 (c) 1999-2026       https://www.mikrotik.com/

Press F1 for help
```

After the banner, the router can print other information: the
[`/system/note`](../cli-reference/system/note) when it is set to show at login, the most recent
critical log messages, for example `system,error,critical login failure for user admin from
<address> via ssh`, and, on a router with the default configuration, its description. On the
first login after an installation or a configuration reset, the router asks whether to show the
software license and asks for a new password if the account has none.

## Command Prompt

At the end of the successful login sequence, the login process prints a banner that shows the command prompt, and hands over control to the user.

The default command prompt consists of user name, system identity, and current command path.

For example, change the current path from the root to the interface, then go back to the root:

```text
[admin@MikroTik] > interface
[admin@MikroTik] /interface> /
[admin@MikroTik] >
```

Use <kbd>↑</kbd> to recall previous commands from command history (commands that added sensitive data, like passwords, are not available in the history). If a multiline command is recalled, press <kbd>F8</kbd> to expand it. Use <kbd>Tab</kbd> to autocomplete commands and see available options — pressing <kbd>Tab</kbd> twice shows all possible completions. Press <kbd>Enter</kbd> to execute the command, <kbd>Control</kbd>+<kbd>C</kbd> to interrupt the currently running command and return to the prompt, and <kbd>F1</kbd> to display built-in help.

The easiest way to log out of the console is to press <kbd>Control</kbd>+<kbd>D</kbd> at the command prompt while the command line is empty (you can cancel the current command and get an empty line with **Control-C**, so **Control-C** followed by <kbd>Control</kbd>+<kbd>D</kbd> logs you out in most cases).

It is possible to write commands that consist of multiple lines. When the entered line is not a complete command and more input is expected, the console shows a continuation prompt that lists all open parentheses, braces, brackets, and quotes, and also a trailing backslash if the previous line ended with **backslash**-white-space.

```text
[admin@MikroTik] > {
{... :put (\
{(\... 1+2)}
3
```

When you are editing such multiple line entries, the prompt shows the number of current lines and total line count instead of the usual username and system name.

```text
line 2 of 3> :put (\
```

Sometimes commands ask for additional input from the user. For example, the command `/password` asks for the old and the new password. In such cases, the prompt shows the name of the requested value, followed by a colon and a space:

```text
[admin@MikroTik] > /password
old-password:
```

## Hierarchy

The console allows the configuration of the router's settings using text commands. Since there are a lot of available commands, they are split into groups organized into hierarchical menu levels. The name of a menu level reflects the configuration information accessible in the relevant section.

For example, you can issue the `/ip/route/print` command from any menu level. Instead of typing
the `/ip/route` path before each command, the path can be typed only once to move into this branch
of the menu hierarchy, and the commands then run there:

```text
[admin@MikroTik] > /ip/route
[admin@MikroTik] /ip/route> print
```

Each word in the path can be separated by a **space** or by `/`.

Notice that the prompt changes to reflect where you are located in the menu hierarchy. To move to the top level again, type `/`

```text
[admin@MikroTik] /ip> /
[admin@MikroTik] >
```

To move up one command level, type `..`

```text
[admin@MikroTik] /ip/route> ..
[admin@MikroTik] /ip>
```

You can also use `/` and `..` to run commands from other menu levels without changing the current
level, for example `/ping 192.0.2.1` from any level, or the service ports from the NAT menu:

```text
[admin@MikroTik] /ip/firewall/nat> ../service-port/print
Flags: X - DISABLED, I - INVALID
Columns: NAME, PORTS
#   NAME     PORTS
0   ftp         21
1   tftp        69
2 X irc       6667
3   h323
4   sip       5060
              5061
5   pptp
6 X rtsp       554
7   udplite
8   dccp
9   sctp
[admin@MikroTik] /ip/firewall/nat>
```

## Item Names and Numbers

Many of the command levels operate with arrays of items: interfaces, routes, users, and so on. Such arrays are displayed in similar-looking lists. All items in the list have an item number followed by flags and parameter values.

To change the properties of an item, you have to use the **set** command and specify the name or number of the item.

### Item Names

Some lists have items with specific names assigned to each of them. Examples are `/interface` or `/user` levels. There you can use item names instead of item numbers.

You do not have to use the **print** command before accessing items by their names, which, as opposed to numbers, are not assigned by the console internally, but are properties of the items. Thus, they would not change on their own. However, there are all kinds of obscure situations possible when several users are changing the router's configuration at the same time. Generally, item names are more "stable" than the numbers, and also more informative, so you should prefer them to numbers when writing console scripts.

### Item Numbers

Item numbers are assigned by the print command and are not constant - two successive print commands may order items differently. But the results of the last print commands are memorized and, thus, once assigned, item numbers can be used even after **add**, **remove,** and **move** operations. Item numbers are assigned on a per-session basis; they remain the same until you quit the console or until the next print command is executed. Also, numbers are assigned separately for every item list, so for example, the `/ip/address/print` does not change the numbering of the `/interface` list.

It is possible to use item numbers without running the **print** command. Numbers are assigned just as if the **print** command was executed.

You can specify multiple items as targets for some commands. Almost everywhere, where you can write the number of an item, you can also write a list of numbers or names, for example `/interface/vlan/set vlan10,vlan20 mtu=1400`.

```text
[admin@MikroTik] > /interface/vlan/print
Flags: R - RUNNING
Columns: NAME, MTU, ARP, VLAN-ID, INTERFACE, MAC-ADDRESS
#   NAME     MTU  ARP      VLAN-ID  INTERFACE  MAC-ADDRESS
0 R vlan10  1500  enabled       10  ether1     52:54:00:12:34:56
1 R vlan20  1500  enabled       20  ether1     52:54:00:12:34:56
2 R vlan30  1500  enabled       30  ether1     52:54:00:12:34:56
[admin@MikroTik] > /interface/vlan/set 0,1 mtu=1400
[admin@MikroTik] > /interface/vlan/print
Flags: R - RUNNING
Columns: NAME, MTU, ARP, VLAN-ID, INTERFACE, MAC-ADDRESS
#   NAME     MTU  ARP      VLAN-ID  INTERFACE  MAC-ADDRESS
0 R vlan10  1400  enabled       10  ether1     52:54:00:12:34:56
1 R vlan20  1400  enabled       20  ether1     52:54:00:12:34:56
2 R vlan30  1500  enabled       30  ether1     52:54:00:12:34:56
```

:::warning
Do not use item numbers in scripts. It is not a reliable way to edit items in the **scheduler**, **scripts**, and so on. Instead, use the **find** command. More info in the [scripting documentation](../developer-guides/scripting). Also look at [scripting examples](../developer-guides/scripting/scripting-examples).
:::

## General Commands

Some commands are common to nearly all menu levels, namely: **add**, **edit**, **find**, **move**, **print**, **remove**, **set**, **reset**, **export**, **get**, **enable**, **disable**, and **comment**. These commands have similar behavior throughout different menu levels. For detailed descriptions and parameters, see the [Scripting Commands](../developer-guides/scripting#commands) reference.

:::info
You can combine commands. Here are two variants of the same command that place a new firewall filter entry, by looking up the comment:

```routeros
/ip/firewall/filter/add chain=forward \
    place-before=[find where comment=CommentX]
/ip/firewall/filter/add chain=forward place-before="CommentX"
```

:::

## Edit Modes

The console line editor works either in multiline mode or in single-line mode.

In multiline mode, the line editor displays the complete input line, even if it is longer than a single terminal line. It also uses a full-screen editor for editing large text values, such as scripts.

In single-line mode, only one terminal line is used for line editing, and long lines are shown truncated around the cursor. A full-screen editor is not used in this mode.

The choice of modes depends on detected terminal capabilities.

## Input Modes

It is possible to switch between several input modes:

- **Normal mode** - indicated by a normal command prompt.
- **Safe mode** - indicated by the word SAFE after the command prompt.
- **Hot-lock mode** - indicated by an additional `>` in the prompt. Autocompletes commands.

### Safe Mode

Safe mode undoes every configuration change made while it is on, including changes from other
sessions, if the session that holds it ends without releasing it, for example when a change cuts
your own connection to the router. Press <kbd>Control</kbd>+<kbd>X</kbd> (or
<kbd>F4</kbd>) to take it. The router answers `Taking Safe Mode session... Success!`, and the prompt
shows `<SAFE>`:

```text
[admin@MikroTik] <SAFE>
```

Press <kbd>Control</kbd>+<kbd>X</kbd> again to release safe mode and keep the changes. <kbd>Control</kbd>+<kbd>D</kbd>,
or `/quit` answered with `y`, ends the session and undoes them; answering `n` keeps the session in
safe mode. Safe mode remembers at most 100 changes: with more, the session leaves safe mode and no
changes are undone, so change the configuration in small steps. For what happens when the
connection is lost and when another session asks for safe mode, see
[Work safely with safe mode](../getting-started/configuration-management/#work-safely-with-safe-mode).

:::warning
As "Safe Mode" operates within the user's session and stores configuration changes, it is ignored for commands requiring a reboot, such as resetting configuration or restoring from a backup.
:::

### HotLock Mode

When HotLock mode is enabled, commands are auto-completed.

To enter/exit HotLock mode press <kbd>F7</kbd>.

```text
[admin@MikroTik] >>
```

Double `>>` is an indication that HotLock mode is enabled. For example, typing `/i` completes to
`/interface/`, and then typing `e` completes to `/interface/ethernet/`:

```text
[admin@MikroTik] >> /interface/ethernet/
```

### Lock Mode

The `:lock` command locks the session: the router clears the screen and shows the version line with
`Session is locked (Ctrl-D to Quit)` and a password prompt. Enter the password of the logged-in
user to continue the session, or press <kbd>Control</kbd>+<kbd>D</kbd> to log out:

```text
Session is locked       (Ctrl-D to Quit)
 password for admin:
```

## Quick Typing

Two features in the console help entering commands much quicker and easier - the <kbd>Tab</kbd> key completions, and abbreviations of command names. Completions work similarly to the bash shell in UNIX. If you press the <kbd>Tab</kbd> key after a part of a word, the console tries to find the command within the current context that begins with this word. If there is only one match, it is automatically appended, followed by a space:

`/inte` <kbd>Tab</kbd> becomes `/interface/`

If there is more than one match, but they all have a common beginning, which is longer than that of what you have typed, then the word is completed to this common part, and no space is appended:

`/interface/set e` <kbd>Tab</kbd> becomes `/interface/set ether`

If you've typed just the common part, pressing <kbd>Tab</kbd> once has no effect. However, pressing it for the second time shows all possible completions in compact form:

```text
[admin@MikroTik] > /interface/set e[Tab]_
[admin@MikroTik] > /interface/set ether[Tab]_
[admin@MikroTik] > /interface/set ether[Tab]_
ether1 ether5
[admin@MikroTik] > /interface/set ether_
```

The <kbd>Tab</kbd> key can be used in almost any context where the console might have a clue about possible values - command names, argument names, arguments that have only several possible values (like names of items in some lists or names of protocols in firewall and NAT rules). You cannot complete numbers, IP addresses, and similar values.

Another way to press fewer keys while typing is to abbreviate command and argument names. You can type only the beginning of the command name, and, if it is not ambiguous, the console accepts it as a full name. So typing:

```routeros
pin 10.1 c 3 si 100
```

equals:

```routeros
ping 10.0.0.1 count 3 size 100
```

(`10.1` is the short form of the address `10.0.0.1`.)

It is possible to complete not only the beginning, but also any distinctive substring of a name: if there is no exact match, the console starts looking for words that have the string being completed as the first letters of a multiple-word name, or that simply contain letters of this string in the same order. If a single such word is found, it is completed at the cursor position. For example, `/interface/mt` <kbd>Tab</kbd> becomes `/interface/monitor-traffic`.

## Console Search

Console search allows performing keyword search through the list of RouterOS menus and the history. Press <kbd>Control</kbd>+<kbd>R</kbd>: the prompt changes to `[admin@MikroTik] []>`, and the text you type between the brackets selects the matching earlier commands.

## Internal Chat System

RouterOS console has a built-in internal chat system. This allows remotely located admins to talk to each other directly in RouterOS CLI. To start the conversation, type the message at the command prompt with the # symbol in front. The other console sessions that are open at that moment see it. In scripts, # starts a comment.

```text
[admin@MikroTik] > # ready to upgrade?
```

Another console session of the same user shows:

```text
[admin@MikroTik] > admin: ready to upgrade?
```

## Settings

In the [`/console/settings`](../cli-reference/console/settings) menu:

- `sanitize-names` replaces reserved characters (`\ / : * ? |`) with underscores in file and script names. Default: `no`.
- `log-script-errors` writes errors of scripts that run in the background to the log. Default: `yes`.
- `tab-width` sets the tab width in the full-screen editor. Default: `4`.

## Built-in Help

The console has built-in help. The general rule is that help shows what you can type in a position where <kbd>F1</kbd> was pressed (similarly to pressing <kbd>Tab</kbd> key twice, but in verbose form and with explanations). For example, <kbd>F1</kbd> after `/ip/address/` lists the commands of the menu with a short description, and ends with `Press F1 for general console usage help`.

The same data is available to scripts and external tools through [Console inspect](../developer-guides/scripting/console-inspect).

## List of Keys

| Key | Description |
| :-- | :-- |
| <kbd>F1</kbd> | Show context-sensitive help |
| <kbd>F3</kbd> or <kbd>Control</kbd>+<kbd>R</kbd> | Search command history |
| <kbd>F4</kbd> or <kbd>Control</kbd>+<kbd>X</kbd> | Toggle safe mode |
| <kbd>F5</kbd> or <kbd>Control</kbd>+<kbd>L</kbd> | Reset terminal and repaint screen |
| <kbd>F7</kbd> | Toggle hot-lock mode |
| <kbd>F8</kbd> | Print entire multiline input |
| <kbd>Tab</kbd> | Perform line completion. When pressed a second time, show possible completions. |
| <kbd>Control</kbd>+<kbd>C</kbd> | Interrupt current action |
| <kbd>Control</kbd>+<kbd>D</kbd> | Terminate session (on empty prompt) |
| <kbd>Control</kbd>+<kbd>K</kbd> | Delete to the end of the line |
| <kbd>Control</kbd>+<kbd>U</kbd> | Delete to the beginning of the line |
| <kbd>Control</kbd>+<kbd>T</kbd> | Switch to a background task |
| <kbd>Control</kbd>+<kbd>\\</kbd> | Split line at cursor. Insert newline at the cursor position. |
| <kbd>Control</kbd>+<kbd>B</kbd> or <kbd>←</kbd> | Move cursor backward one character |
| <kbd>Control</kbd>+<kbd>F</kbd> or <kbd>→</kbd> | Move cursor forward one character |
| <kbd>Control</kbd>+<kbd>P</kbd> or <kbd>↑</kbd> | Go to the previous line. If this is the first line of input, recall previous input from history. |
| <kbd>Control</kbd>+<kbd>N</kbd> or <kbd>↓</kbd> | Go to the next line. If this is the last line of input, recall the next input from history. |
| <kbd>Control</kbd>+<kbd>A</kbd> or <kbd>Home</kbd> | Move the cursor to the beginning of the line. If the cursor is already at the beginning, go to the beginning of the first line of the current input. |
| <kbd>Control</kbd>+<kbd>E</kbd> or <kbd>End</kbd> | Move the cursor to the end of the line. If the cursor is already at the end, move it to the end of the last line of the current input. |
| <kbd>Delete</kbd> | Remove character at the cursor |
| <kbd>Control</kbd>+<kbd>H</kbd> or <kbd>Backspace</kbd> | Remove character before cursor and move the cursor back one position |
| <kbd>#</kbd> | Send a message to the internal chat system |
| **/** | Move up to base level |
| **..** | Move up one level |
| **/command** | Use command at the base level |

<kbd>Up</kbd>, <kbd>Down</kbd> and split keys leave the cursor at the end of the line.
