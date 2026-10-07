# Console

> The console provides text-based access to MikroTik RouterOS configuration and management features using text terminals, either remotely by using a serial port, telnet, SSH, or console screen within WinBox, or...

# Console

## Overview

The console is used for accessing the MikroTik Router's configuration and management features by using text terminals, either remotely by using a serial port, telnet, SSH, or console screen within [WinBox](./winbox), or directly by using a monitor and keyboard. The console is also used for writing scripts. This manual describes the general console operation principles. Consult the [Scripting Manual](../developer-guides/scripting) on some advanced console commands and on how to write scripts.

## Login Options

Console login options enable or disable various console features like color, terminal detection, and many others.

Additional login parameters can be appended to the login name after the '+' sign.

```
    login_name ::= user_name [ '+' parameters ]
    parameters ::= parameter [ parameters ]
    parameter ::= [ number ] 'a'..'z'
    number ::= '0'..'9' [ number ]
```

If the parameter is not present, then the default value is used. If the number is not present, then the implicit value of the parameter is used.

Example: `admin+ct80w` - disables console colors, disables auto detection, and then sets terminal width to 80.

| Param | Default | Implicit | Description |
| :-- | :-- | :-- | :-- |
| **"w"** | auto | auto | Set terminal width |
| **"h"** | auto | auto | Set terminal height |
| **"c"** | on | off | Disable/enable console colors |
| **"t"** | off | on | Disable auto-detection of terminal capabilities |
| **"e"** | on | off | Enables "dumb" terminal mode |

## Banner and Messages

The login process displays the MikroTik banner and short help after validating the user name and password.

```ros
  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.23.2 (c) 1999-2026       https://www.mikrotik.com/

Press F1 for help
```

After the banner, other important information can be printed, like [`/system/note`](../cli-reference/system/note) set by another admin, the last few critical log messages, demo version upgrade reminder, and default configuration description.

For example, the demo license prompt and the last critical messages are printed:

```ros
UPGRADE NOW FOR FULL SUPPORT
----------------------------
FULL SUPPORT benefits:
- receive technical support
- one year feature support
- one year online upgrades
    (avoid re-installation and re-configuring your router)
To upgrade, register your license "software ID"
on our account server www.mikrotik.com

Current installation "software ID": ABCD-456

Please press "Enter" to continue!

2007-12-10 10:40:06 system,error,critical login failure for user root from 10.0.0.1 via telnet
2007-12-10 10:40:07 system,error,critical login failure for user root from 10.0.0.1 via telnet
2007-12-10 10:40:09 system,error,critical login failure for user test from 10.0.0.1 via telnet
```

## Command Prompt

At the end of the successful login sequence, the login process prints a banner that shows the command prompt, and hands over control to the user.

The default command prompt consists of user name, system identity, and current command path.

For example, change the current path from the root to the interface, then go back to the root:

```ros
  [admin@MikroTik] > interface [enter]
  [admin@MikroTik] /interface> / [enter]
  [admin@MikroTik] >
```

Use <kbd>↑</kbd> to recall previous commands from command history (commands that added sensitive data, like passwords, are not available in the history). If a multiline command is recalled, press <kbd>F8</kbd> to expand it. Use <kbd>Tab</kbd> to autocomplete commands and see available options — pressing <kbd>Tab</kbd> twice shows all possible completions. Press <kbd>Enter</kbd> to execute the command, <kbd>Control</kbd>+<kbd>C</kbd> to interrupt the currently running command and return to the prompt, and <kbd>F1</kbd> to display built-in help.

The easiest way to log out of the console is to press <kbd>Control</kbd>+<kbd>D</kbd> at the command prompt while the command line is empty (you can cancel the current command and get an empty line with **Control-C**, so **Control-C** followed by <kbd>Control</kbd>+<kbd>D</kbd> logs you out in most cases).

It is possible to write commands that consist of multiple lines. When the entered line is not a complete command and more input is expected, the console shows a continuation prompt that lists all open parentheses, braces, brackets, and quotes, and also a trailing backslash if the previous line ended with **backslash**-white-space.

```ros
    [admin@MikroTik] > {
    {... :put (\
    {(\... 1+2)}
    3
```

When you are editing such multiple line entries, the prompt shows the number of current lines and total line count instead of the usual username and system name.

```
line 2 of 3> :put (\
```

Sometimes commands ask for additional input from the user. For example, the command `/password` asks for old and new passwords. In such cases, the prompt shows the name of the requested value, followed by a colon and a space.

```ros
    [admin@MikroTik] > /password
    old password: ******
    new password: **********
    retype new password: **********
```

## Hierarchy

The console allows the configuration of the router's settings using text commands. Since there are a lot of available commands, they are split into groups organized into hierarchical menu levels. The name of a menu level reflects the configuration information accessible in the relevant section.

For example, you can issue the `/ip/route/print` command:

```ros
[admin@MikroTik] > /ip/route/print 
Flags: X - disabled, A - active, D - dynamic, 
C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 # DST-ADDRESS PREF-SRC G GATEWAY DIS INTE... 
0 A S 0.0.0.0/0 r 10.0.3.1 1 bridge1 
1 ADC 1.0.1.0/24 1.0.1.1 0 bridge1 
2 ADC 1.0.2.0/24 1.0.2.1 0 ether3 
3 ADC 10.0.3.0/24 10.0.3.144 0 bridge1 
4 ADC 10.10.10.0/24 10.10.10.1 0 wlan1 
[admin@MikroTik] >
```

Instead of typing `/ip/route` path before each command, the path can be typed only once to move into this particular branch of the menu hierarchy. Thus, the previous example could also be executed like this:

```ros
[admin@MikroTik] > /ip/route 
[admin@MikroTik] /ip/route> print 
Flags: X - disabled, A - active, D - dynamic, 
C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
 B - blackhole, U - unreachable, P - prohibit # 
DST-ADDRESS PREF-SRC G GATEWAY DIS INTE... 
0 A S 0.0.0.0/0 r 10.0.3.1 1 bridge1 
1 ADC 1.0.1.0/24 1.0.1.1 0 bridge1 
2 ADC 1.0.2.0/24 1.0.2.1 0 ether3 
3 ADC 10.0.3.0/24 10.0.3.144 0 bridge1 
4 ADC 10.10.10.0/24 10.10.10.1 0 wlan1 
[admin@MikroTik] /ip/route>
```

Each word in the path can be separated by a **space** or by `/`.

Notice that the prompt changes to reflect where you are located in the menu hierarchy. To move to the top level again, type `/`

```ros
[admin@MikroTik] > /ip/route 
[admin@MikroTik] /ip/route> /
[admin@MikroTik] >
```

To move up one command level, type `..`

```ros
[admin@MikroTik] /ip/route> .. 
[admin@MikroTik] /ip>
```

You can also use `/` and `..` to execute commands from other menu levels without changing the current level:

```ros
[admin@MikroTik] /ip/route> /ping 10.0.0.1 
10.0.0.1 ping timeout 
2 packets transmitted, 0 packets received, 100% packet loss 
[admin@MikroTik] /ip/firewall/nat> ../service-port/print
Flags: X - disabled, I - invalid 
# NAME PORTS 
0 ftp 21 
1 tftp 69 
2 irc 6667 
3 h323 
4 sip 
5 pptp 
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

You can specify multiple items as targets for some commands. Almost everywhere, where you can write the number of an item, you can also write a list of numbers.

```ros
[admin@MikroTik] > /interface/print 
Flags: X - disabled, D - dynamic, R - running 
# NAME TYPE MTU 
0 R ether1 ether 1500 
1 R ether2 ether 1500 
2 R ether3 ether 1500 
3 R ether4 ether 1500 
[admin@MikroTik] > /interface/set 0,1,2 mtu=1460 
[admin@MikroTik] > /interface/print
 Flags: X - disabled, D - dynamic, R - running 
# NAME TYPE MTU 
0 R ether1 ether 1460 
1 R ether2 ether 1460 
2 R ether3 ether 1460 
3 R ether4 ether 1500 
[admin@MikroTik] >
```

:::warning
Do not use item numbers in scripts. It is not a reliable way to edit items in the **scheduler**, **scripts**, and so on. Instead, use the **find** command. More info in the [scripting documentation](../developer-guides/scripting). Also look at [scripting examples](../developer-guides/scripting/scripting-examples).
:::

## General Commands

Some commands are common to nearly all menu levels, namely: **add**, **edit**, **find**, **move**, **print**, **remove**, **set**, **reset**, **export**, **get**, **enable**, **disable**, and **comment**. These commands have similar behavior throughout different menu levels. For detailed descriptions and parameters, see the [Scripting Commands](../developer-guides/scripting#commands) reference.

:::info
You can combine commands. Here are two variants of the same command that place a new firewall filter entry, by looking up the comment:

```ros
/ip/firewall/filter/add chain=forward place-before=[find where comment=CommentX]
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
- **Hot-lock mode** - indicated by an additional yellow >. Autocompletes commands.

### Safe Mode

It is sometimes possible to change the router configuration in a way that makes the router inaccessible (except from the local console). Usually, this is done by accident, but there is no way to undo the last change when the connection to the router is already cut. Safe mode can be used to minimize such risk.

The **"Safe Mode"** button in the WinBox GUI allows you to enter Safe Mode, while in the CLI, you can access it by either using the keyboard shortcut <kbd>F4</kbd> or pressing <kbd>Control</kbd>+<kbd>X</kbd>. To exit without saving the changes made in CLI, hit <kbd>Control</kbd>+<kbd>D</kbd>.

```ros
[admin@MikroTik] /ip/route>[CTRL]+[X] 
[Safe Mode taken] 
[admin@MikroTik] /ip/route<SAFE>
```

![](./img/safe-mode-cli.png)

Message **Safe Mode taken** is displayed and the prompt changes to reflect that session is now in safe mode. All configuration changes that are made (also from other login sessions), while the router is in safe mode, are automatically undone if the safe mode session terminates abnormally. You can see all such changes that are automatically undone, tagged with an **F** flag in the system history:

```ros
[admin@MikroTik] /ip/route> 
[Safe Mode taken]
[admin@MikroTik] /ip/route<SAFE>/add
[admin@MikroTik] /ip/route<SAFE> /system/history/print
Flags: U, F - FLOATING-UNDO
Columns: ACTION, BY, POLICY
  ACTION                 BY     POLICY
F route 0.0.0.0/0 added  admin  write
```

Now, if the telnet connection (or WinBox terminal) is cut, then after a while (TCP timeout is **9** minutes) all changes that were made while in safe mode are undone. Exiting the session by <kbd>Control</kbd>+<kbd>D</kbd> also undoes all safe mode changes, while **/quit** does not.

If another user tries to enter safe mode, they are given the following message:

```ros
[admin@MikroTik] > 
Hijacking Safe Mode from someone - unroll/release/don't take it [u/r/d]:
```

- [u] - undoes all safe mode changes, and puts the current session in safe mode.
- [r] - keeps all current safe mode changes, and puts the current session in safe mode. The previous owner of safe mode is notified about this:

```ros
[admin@MikroTik] /ip/firewall/rule/input 
[Safe mode released by another user]
```

- [d] - leaves everything as-is.

If too many changes are made while in safe mode, and there's no room in history to hold them all (currently history keeps up to the 100 most recent actions), then the session is automatically put out of safe mode, and no changes are automatically undone. Thus, it is best to change the configuration in small steps, while in safe mode. Pressing <kbd>Control</kbd>+<kbd>X</kbd> twice is an easy way to empty the safe mode action list.

:::warning
As "Safe Mode" operates within the user's session and stores configuration changes, it is ignored for commands requiring a reboot, such as resetting configuration or restoring from a backup.
:::

### HotLock Mode

When HotLock mode is enabled, commands are auto-completed.

To enter/exit HotLock mode press <kbd>F7</kbd>.

```ros
[admin@MikroTik] /ip/address> [F7]
[admin@MikroTik] /ip/address>>

```

Double `>>` is an indication that HotLock mode is enabled. For example, if you type "`/in et"`, it is auto-completed to:

```ros
[admin@MikroTik] /ip/address>> /interface/ethernet/
```

### Lock Mode

The **:lock** command locks the screen.

```ros
[admin@MikroTik] > :lock
...
  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.16rc1 (c) 1999-2024       https://www.mikrotik.com/

Session is locked       (Ctrl-D to Quit)

 password for admin: 
```

## Quick Typing

Two features in the console help entering commands much quicker and easier - the <kbd>Tab</kbd> key completions, and abbreviations of command names. Completions work similarly to the bash shell in UNIX. If you press the <kbd>Tab</kbd> key after a part of a word, the console tries to find the command within the current context that begins with this word. If there is only one match, it is automatically appended, followed by a space:

`/inte` <kbd>Tab</kbd> becomes `/interface/`

If there is more than one match, but they all have a common beginning, which is longer than that of what you have typed, then the word is completed to this common part, and no space is appended:

`/interface/set e` <kbd>Tab</kbd> becomes `/interface/set ether`

If you've typed just the common part, pressing <kbd>Tab</kbd> once has no effect. However, pressing it for the second time shows all possible completions in compact form:

```ros
[admin@MikroTik] > /interface/set e[Tab]_ 
[admin@MikroTik] > /interface/set ether[Tab]_ 
[admin@MikroTik] > /interface/set ether[Tab]_ 
ether1 ether5 
[admin@MikroTik] > interface set ether_
```

The <kbd>Tab</kbd> key can be used in almost any context where the console might have a clue about possible values - command names, argument names, arguments that have only several possible values (like names of items in some lists or names of protocols in firewall and NAT rules). You cannot complete numbers, IP addresses, and similar values.

Another way to press fewer keys while typing is to abbreviate command and argument names. You can type only the beginning of the command name, and, if it is not ambiguous, the console accepts it as a full name. So typing:

```ros
[admin@MikroTik] > pin 10.1 c 3 si 100
```

equals:

```ros
[admin@MikroTik] > ping 10.0.0.1 count 3 size 100
```

It is possible to complete not only the beginning, but also any distinctive substring of a name: if there is no exact match, the console starts looking for words that have the string being completed as the first letters of a multiple-word name, or that simply contain letters of this string in the same order. If a single such word is found, it is completed at the cursor position. For example:

```ros
[admin@MikroTik] > /interface/x[TAB][TAB]_ 
dot1x  vxlan  export
[admin@MikroTik] > /interface/mt[TAB]_
[admin@MikroTik] > /interface/monitor-traffic _

```

## Console Search

Console search allows performing keyword search through the list of RouterOS menus and the history. The search prompt is accessible with the <kbd>Control</kbd>+<kbd>R</kbd> shortcut.

## Internal Chat System

RouterOS console has a built-in internal chat system. This allows remotely located admins to talk to each other directly in RouterOS CLI. To start the conversation, prefix the intended message with the # symbol. Anyone who is logged in at the time of sending the message sees it.

```ros
[admin@MikroTik] > # ready to break internet?
[admin@MikroTik] > 
fake_admin: i was born ready
[admin@MikroTik] > 
```

```ros
[fake_admin@MikroTik] > 
admin: ready to break internet?
[fake_admin@MikroTik] > # i was born ready
[fake_admin@MikroTik] > 
```

## Settings

In the [`/console/settings`](../cli-reference/console/settings) menu, it is possible to enable an option for replacing reserved characters with underscores for file names.

## Built-in Help

The console has built-in help. Press <kbd>F1</kbd> for general console usage help. The general rule is that help shows what you can type in a position where <kbd>F1</kbd> was pressed (similarly to pressing <kbd>Tab</kbd> key twice, but in verbose form and with explanations).

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
