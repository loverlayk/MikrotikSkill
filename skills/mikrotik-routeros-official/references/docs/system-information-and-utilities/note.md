# Note

> The system note is a text that RouterOS shows to administrators at login: the router's purpose, contacts or a warning. Set it in the CLI, in WinBox or from a sys-note.txt file, and show it before the Telnet login prompt.

# Note

The system note is a text that RouterOS shows to every administrator who logs in: in the command line right after the banner, and in WinBox in a window after login. Use it to say what the router does, whom to contact, or what not to do, for example during a maintenance window. The note is empty by default.

## Set a note

Set the text with `note`. In a double-quoted string, `\n` starts a new line:

```ros
/system/note/set \
    note="Office gateway. IT: +371 0000000\nNo reboots 08:00-18:00"
```

At the next interactive login, for example over SSH or MAC Telnet, the note follows the banner:

```text
  MikroTik RouterOS 7.25beta5 (c) 1999-2026       https://www.mikrotik.com/

Press F1 for help

Office gateway. IT: +371 0000000
No reboots 08:00-18:00
```

A command run over SSH without an interactive session, such as `ssh admin@router '/system/resource/print'`, does not show the note. For longer text, `/system/note/edit note` opens the note in the built-in editor. To stop showing the note without deleting it, set `show-at-login=no`.

## Configure the note in WinBox

Open **System > Note**:

1. Choose when the note appears with **Show At Login** and **Show At CLI Login**. **Show At Login** displays it after login; **Show At CLI Login** also displays it before the Telnet login prompt.
2. Enter the message in **Note**, then select **OK**. For example, record the router's purpose and the maintenance contact. The text area accepts multiple lines.

![WinBox System Note dialog with login display options and the Note text area](./img/note-winbox.webp)

## Show the note before login

With `show-at-cli-login=yes`, the router also prints the note before the Telnet login prompt, here seen from another router with `/system/telnet 192.168.88.1`:

```text
Connecting to 192.168.88.1
Connected to 192.168.88.1
Office gateway. IT: +371 0000000
No reboots 08:00-18:00
Login:
```

This works independently of `show-at-login`. Anyone who connects to the Telnet port sees this text without logging in, so keep information meant only for administrators out of the note. Telnet is enabled by default; see [Services](services). SSH does not show the note before login, and MAC Telnet asks for the user name and password before it connects, so it shows the note only after login.

## Set the note from a file

A plain text file named `sys-note.txt` in the root of the router's file storage replaces the note at the next startup, and the router then removes the file. To set the note on a new router this way, upload the file, for example over SFTP or FTP, and reboot the router.

For the parameters, see the [`/system/note` CLI reference](../cli-reference/system/note).
