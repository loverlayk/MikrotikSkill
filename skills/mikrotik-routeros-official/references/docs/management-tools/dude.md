# Dude

> Dude is a legacy network management tool discontinued by MikroTik, now offered without further updates or enhancements. Users are advised to exercise caution and consider alternative solutions for network management...

# Dude

Please be advised that development of Dude has been officially discontinued, and the software is now classified as legacy. It is provided on an “as-is” basis, and no further updates or enhancements are planned for the foreseeable future. Users are encouraged to exercise their own discretion when utilizing this software.

## Run the Dude server

The Dude server runs on the router and comes in the `dude` extra package (see
[Packages](../getting-started/installation-and-upgrade/packages)). After installing the package,
enable the server and choose the folder for its database:

```routeros
/dude/set enabled=yes data-directory=dude
/dude/print
```

```text
         enabled: yes
  data-directory: dude
          status: running
```

The router creates the folder with the database (`dude.db`) and the default files of the Dude.
While the server runs, RouterOS adds a dynamic `dudes` service on UDP port 514 (see `/ip/service/print`).
On a router with a `flash` folder or an attached disk, choose a folder there, for example
`flash/dude`, so that the database is kept on persistent storage.
