# Upgrade

> Upgrade RouterOS from the router with check-for-updates and the release channels (long-term, stable, testing, development), upgrade from uploaded package files, automate upgrades with the scheduler, troubleshoot the...

# Upgrade

MikroTik devices are preinstalled with RouterOS, so installation is usually not needed, except in the case of installing RouterOS on a bare metal x86 PC or a virtual machine with CHR images. The upgrade procedure on already installed devices is straightforward.

## Version numbering

RouterOS versions are numbered sequentially, where a period is used to separate sequences; it does *not* represent a decimal point, and the sequences do *not* have positional significance. An identifier of 2.5, for instance, is not "two and a half" or "halfway to version three"; it is the fifth second-level revision of the second first-level revision. Therefore v5.2 is older than v5.18, which is newer.

RouterOS versions are released in several "release chains": Long term, Stable, Testing, and Development. When upgrading RouterOS, you can choose a release chain from which to install the new packages:

- **Long term**: Released rarely, and includes only the most critical fixes. Upgrades within one number branch do not contain new features. When a **Stable** release has been out for a while and seems to be stable enough, it gets promoted into the long-term branch, replacing an older release, which is then moved to the archive. This consecutively adds new features.
- **Stable**: Released every few months, including all tested new features and fixes.
- **Testing**: Released every few weeks, undergoes only basic internal testing, and should not be used in production.
- **Development**: Released when necessary. Includes raw changes and is available for software enthusiasts for testing new features.

![Diagram of the release chains: development (alpha), beta and release candidates, stable and long-term, and how versions move between them](./img/upgrade-01.webp)

## Standard upgrade

The package upgrade feature connects from the router to the MikroTik download server over HTTPS and checks if a newer RouterOS version is available in the selected release channel. This menu can also be used for downgrading by changing the channel to one that offers an older, but more stable release. The feature connects from the router, not your computer, so the router itself needs HTTPS connectivity to the MikroTik server.

After selecting the *Check for Updates* button in QuickSet or in the System → Packages menu, the *Check for Updates* window will open with the current changelog or the latest changelog (if a newer version exists). If a newer version is available, the *Download* and *Download&Install* buttons will appear. Selecting *Download* downloads the newest version (a manual device reboot is required), while selecting *Download&Install* starts the download and automatically reboots the device after a successful download.

From the command line, check for a new version, then install it:

```routeros
/system/package/update/check-for-updates
/system/package/update/install
```

`check-for-updates` shows the installed version and the latest version in the channel, with the status `New version is available`. `install` works like *Download&Install*: it downloads the new packages and reboots the router to install them. To download now and reboot later, use `/system/package/update/download`: the status changes to `Downloaded, please reboot router to upgrade it`, and the router installs the packages at the next reboot. If the router is up to date, the status is
`System is already up to date`. If it cannot reach the server, the status starts with `ERROR:`, for
example `ERROR: IPv4: could not resolve dns name (timeout)` or `ERROR: IPv4: server is not
responding`; see Troubleshooting below.

Make a [backup](../configuration-management/backup) before an upgrade.

The versions offered depend on the selected release channel. The channel offers only its latest version; to install a specific version, upload its package
files. A channel can also offer an older version than the installed one, for example `long-term` on a router that runs the stable release; installing it downgrades the router. On RouterOS 6.49, the `upgrade` channel offers RouterOS v7 and installs it in one step.

If extra packages are installed, the router downloads their new versions too.

### Check for Updates settings

The connection to the MikroTik download server can be fine-tuned in the System → Packages → Check for Updates window, or with the [`/system/package/update/set`](../../cli-reference/system/package/update) command:

- **Channel**: Upgrade channel to use when checking for new versions. The release chains are described in the Version numbering section.
- **Mode**: Protocol for connecting to the MikroTik download server. Use `http` only if your network blocks HTTPS. HTTPS is recommended.
- **IP version**: IP version preference for connecting to the MikroTik download server.
- **Check certificate**: Whether and how to validate the server SSL certificate. Always use `yes` to ensure a secure connection. `yes-without-crl` can be used to skip CRL validation.

```routeros
/system/package/update/set channel=stable mode=https \
    ip-version=auto check-certificate=yes
```

:::warning
On RouterBOARD devices, it is strongly recommended to upgrade the bootloader after RouterOS update. To upgrade the bootloader, execute the [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard/upgrade.md) command in CLI, followed by a reboot. Alternatively, navigate to the GUI System → RouterBOARD menu and select the "Upgrade" button, then reboot the device.
:::

You can **automate** the upgrade process by running a script in the system scheduler. This script asks the MikroTik upgrade server for a new version in the selected channel and, if the status is `New version is available`, installs it. Save it as a script and add a scheduler entry that runs it every week; the script
waits 10 seconds for the server's answer:

```routeros
/system/script/add name=auto-upgrade source={
/system/package/update/check-for-updates
:delay 10s
:local status [/system/package/update/get status]
:if ($status = "New version is available") do={
    /system/package/update/install
}
}
/system/scheduler/add name=auto-upgrade interval=7d \
    start-time=03:00:00 on-event=auto-upgrade
```

The script installs whatever the channel offers. With the `long-term` channel on a router that
runs a newer stable release, it installs the older long-term release.

### Troubleshooting

If the router does not offer a version you expect, check the channel first: a new version is in
the testing or development channel before it reaches stable. If the status shows an `ERROR:`,
verify that the router can resolve and reach the upgrade server, `upgrade.mikrotik.com`.

```routeros
:put [:resolve upgrade.mikrotik.com]
```

The result should be `159.148.147.251`. If the address does not resolve or resolves to a different IP, review your DNS settings. See the [DNS](../../network-management/dns) article for more information.

Once DNS resolution is confirmed, verify that the device can reach the server:

```routeros
/tool/ping address=159.148.147.251
```

If the ping fails, check your firewall rules, routing, or upstream connectivity. A failed ping alone
does not prove that the server is unreachable: continue with the next check.

Once the IP connectivity is confirmed working, verify that TCP port 443 is reachable. The
router prints `Connected to 159.148.147.251` if it is; press <kbd>Control</kbd>+<kbd>C</kbd> to close
the connection:

```routeros
/system/telnet 159.148.147.251 port=443
```

## Manual upgrade

You can upgrade RouterOS in the following ways:

- WinBox – drag and drop files to the Files menu.
- WebFig - upload files from the Files menu.
- FTP or SFTP - upload files to the root directory.

:::warning
On RouterBOARD devices, it is strongly recommended to upgrade the bootloader after upgrading RouterOS. To upgrade the bootloader, execute the [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard/upgrade.md) command in CLI, followed by a reboot. Alternatively, navigate to the GUI System → RouterBOARD menu and select the "Upgrade" button, then reboot the device.

**Warning:** RouterOS cannot be upgraded through a serial cable. Only [RouterBOOT](./routerboot.md#simple-upgrade) is upgradeable with this method.
:::

### Manual upgrade process

- Open the [MikroTik download page](https://mikrotik.com/download) and choose the architecture of the router (System → Resources, or `architecture-name` in `/system/resource/print`).
- Download the **routeros** package and the extra packages that are installed on the router. File names are listed on the [Packages](./packages) page.
- Upload packages to the device with one of the methods listed above.

If you need to skip some specific package upgrade or a package file is no longer available, then use [`/system/package/update/install ignore-missing`](../../cli-reference/system/package/update/install.md) to skip missing packages.

#### Using WinBox

Choose your system type and download the upgrade package. Connect to your router with WinBox. Select the downloaded file with your mouse and drag it to the Files menu. If some files are already present, make sure to put the package in the root menu, not inside the hotspot folder! The upload will start.

![WinBox File List with a RouterOS package upload in progress](./img/upgrade-02.webp)

After it finishes, reboot the device. The new version number will be seen in the WinBox title and in the Packages menu.

#### Using S/FTP

- Open an S/FTP client, select the package, and upload it to your router.
- You can check if the file is successfully transferred onto the router (optional).

```routeros
/file/print where type=package
```

```text
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME                 TYPE     SIZE      LAST-MODIFIED
0 iot-7.25.1.npk       package  576.1KiB  2026-11-23 09:55:33
1 routeros-7.25.1.npk  package  19.9MiB   2026-11-23 09:55:32
```

- Reboot the device for the upgrade to begin.

```routeros
/system/reboot
```

- After the reboot, check the installed packages and the log:

```routeros
/system/package/print
/log/print where message~"install"
```

```text
Columns: NAME, VERSION, BUILD-TIME, SIZE
# NAME      VERSION  BUILD-TIME           SIZE
0 iot       7.25.1   2026-11-02 12:39:53  576.1KiB
1 routeros  7.25.1   2026-11-02 12:39:53  19.9MiB

 2026-11-23 09:56:17 system,info installed system-7.25.1
 2026-11-23 09:56:17 system,info installed iot-7.25.1
```

If a package was not installed, the log says why, for example `omitting package system-<version>:
newer package system-<version> is already installed` when the uploaded package is older than the
installed one (to install an older version, see [Packages](./packages)). The uploaded files are
removed after the reboot.

## RouterOS local upgrade

You can upgrade one or multiple MikroTik routers within your local network by using [`/system/package/local-update`](../../cli-reference/system/package/local-update/local-update.md) tool on one device which has all needed packages. Here is a simple example with 3 routers (the same method works on networks with any number of routers):

- Place needed packages under the Files menu, on your main router:

![WinBox Files menu on the main router with the RouterOS packages](./img/upgrade-03.webp)

**Optional:** you can set a mirror device between the main ones. If not needed, skip this step:

- Choose Local Package Sources and enable Mirror device. Set Primary Server (10.155.136.50) where the packages are located. The Check Interval **minimum** setting can be set to 00:07:12, at which the device will connect by using WinBox to a main device and check for packages.  
  If new packages are available, it will begin to download. The download process is slow and may require some time when many files are used. In case of some failures, download will resume on next Check.

![WinBox Local Package Sources tab with the Upgrade Mirror dialog: enabled, primary server, check interval, user and password](./img/upgrade-04.webp)

- A new `packs` folder is created, where the mirror device will store packages:

![WinBox Files menu of the mirror device with the packs folder](./img/upgrade-05.webp)

- Add a new package source on the device which will be updated, in this example we use mirror device 10.155.136.71:

![WinBox Package Source dialog with the address, user and password of the mirror device](./img/upgrade-06.webp)

- When you select **Refresh** in the Local Update packages tab, the device in WinBox will connect to the source and check if there are new packages.

![WinBox Local Update Packages tab after Refresh, listing the packages of the source](./img/upgrade-07.webp)

- Choose packages and select **Download**. After download completes, reboot the device.

![WinBox Local Update Packages tab with packages selected for download](./img/upgrade-08.webp)

- Use `/system/package/local-update/refresh` to automate this in your scripts. The Fetch tool can be used to download packages from our web page, for example:

```routeros
/tool/fetch url=https://download.mikrotik.com/routeros/7.25.2/routeros-7.25.2-arm.npk
```
