# DLNA Media Server

> The DLNA media server shares video, music and picture files from a disk folder with TVs, phones and players on one interface. It covers limiting a server to one device, the servers that disk sharing creates, and how...

# DLNA Media Server

DLNA (Digital Living Network Alliance) is a set of network protocols that devices use to share digital media such as videos, photos and music. DLNA is built on UPnP (Universal Plug and Play), which gives devices discovery and control: devices find each other with SSDP (Simple Service Discovery Protocol), exchange control messages with SOAP (Simple Object Access Protocol), and describe themselves and their services in XML.

The RouterOS media server shares the media files of a folder on a disk, for example a USB disk, another disk or a [tmpfs](tmpfs) folder, with TVs, phones and player applications such as VLC. Each server runs on one interface. Players on that interface find the server by its name and play the files from the router. The router serves the files as they are and does not convert them, so the player must support the file format.

:::info
The media server is not available on SMIPS devices, the small MIPS-based devices whose `architecture-name` in `/system/resource/print` is `smips`.
:::

## Share a USB disk with the TVs on the LAN

Add a server for the `media` folder of the USB disk on the LAN bridge:

```ros
/ip/media/add friendly-name="Office media" interface=bridge \
    path=usb1/media
```

```ros
[admin@MikroTik] > /ip/media/print
Columns: INTERFACE, FRIENDLY-NAME, PATH, ALLOWED-IP, STATUS
# INTERFACE  FRIENDLY-NAME  PATH        ALLOWED-IP  STATUS
0 bridge     Office media   usb1/media  0.0.0.0     Running
```

Players on the LAN list the server as `Office media`. Devices on Wi-Fi interfaces that are ports of the bridge are on the `bridge` too. The folders under `usb1/media` show as folders.

`path` can also be the root folder of a disk, for example `path=usb1`. Always set `path`: a server without it shares the whole file list of the router, with all its disks and folders.

The server lists video, music and picture files, such as `.mp4`, `.mkv`, `.mp3`, `.flac` and `.jpg` files; other files, such as `.txt` files, are not listed. It recognises a media file only by a lower-case extension, so rename files with upper-case extensions such as `.MP4` or `.JPG`, which cameras often write. An `.srt` file with the same name as a video, for example `holiday.srt` next to `holiday.mp4`, is offered with the video as its subtitles. A file you copy to the folder later appears the next time a player opens the folder.

## Limit a server to one device

On routers where automatic media sharing is on, for example with the default configuration of the hAP ax², the disk already has a dynamic server that every device on the bridge can use (described in the section on servers created for disks automatically). A dynamic server cannot be changed (`failure: can't edit dynamic object`), so turn it off before you add limited servers:

```ros
/disk/set usb1 media-sharing=no
```

By default, every device on the interface can use a server. To limit a server to one device, set one of these:

- `allowed-ip` - the IP address of the device. It takes one address; a subnet is refused. Give the device a static DHCP lease, so that its address does not change (see [Leases](../network-management/dhcp/server#leases)).
- `allowed-hostname` - the host name of the device's DHCP lease on this router's DHCP server. The name must match exactly, including upper and lower case.

A server takes only one of the two: setting both fails with `failure: can't set both allowed IP and allowed hostname`. The server refuses other devices, so they do not see its files.

For example, give the TV in the children's room only the children's films, and the living room TV the rest. Each TV gets its own server:

```ros
/ip/media/add friendly-name=adults interface=bridge \
    path=usb1/media/adults allowed-hostname=Living-Room-TV
/ip/media/add friendly-name=kids interface=bridge \
    path=usb1/media/kids allowed-hostname=Kids-Room-TV
```

```ros
[admin@MikroTik] > /ip/media/print
Columns: INTERFACE, FRIENDLY-NAME, PATH, ALLOWED-IP, ALLOWED-HOSTNAME, STATUS
# INTERFACE  FRIENDLY-NAME  PATH               ALLOWED-IP  ALLOWED-HOSTNAME  STATUS
0 bridge     adults         usb1/media/adults  0.0.0.0     Living-Room-TV    Running
1 bridge     kids           usb1/media/kids    0.0.0.0     Kids-Room-TV      Running
```

To find the host name of a device, look at the `HOST-NAME` column of its lease:

```ros
/ip/dhcp-server/lease/print
```

A device that sends no host name in its DHCP request has an empty `HOST-NAME` and cannot match `allowed-hostname`. Limit such a device with `allowed-ip` and a static lease instead.

:::note
`allowed-ip` and `allowed-hostname` are not access control. They check only the source address of a request or the host name a device sends in DHCP. The server asks for no password, and the files go over plain HTTP, so any device on the network can take another device's address or host name. To keep files from some devices, put them on a separate network with its own server, or share them over [SMB](smb) with users and passwords.
:::

## Servers created for disks automatically

RouterOS also adds media servers by itself:

- For a disk with `media-sharing=yes` in `/disk`.
- For every new disk and [tmpfs](tmpfs#check-what-the-folder-shares) folder when `/disk/settings` has `auto-media-sharing=yes`. The default configuration of the hAP ax², for example, sets `auto-media-sharing=yes` and `auto-media-interface=bridge`.

Such a server is a dynamic entry (flag `D`) on the interface from `media-interface` (or `auto-media-interface`), named after the router identity and the disk slot, for example `MikroTik usb1 media`. Its `allowed-ip` is `0.0.0.0`, so every device on that interface can read the disk's media files. A dynamic server cannot be edited or removed. To limit it, stop the media sharing of the disk and add a static server.

To stop the server of one disk:

```ros
/disk/set usb1 media-sharing=no
```

To stop the automatic servers for disks you add later:

```ros
/disk/settings/set auto-media-sharing=no
```

The same settings also share disks over SMB, to the `guest` user without a password (see [Tmpfs](tmpfs#check-what-the-folder-shares)). To stop that for one disk, and for disks you add later:

```ros
/disk/set usb1 smb-sharing=no
/disk/settings/set auto-smb-sharing=no
```

## Check and troubleshoot

First check that a server exists and runs. `/ip/media/print` shows the state of each server in `STATUS`:

- `Running` - the server announces itself and serves files.
- `Error, can't find directory` - the folder in `path` does not exist. Check the disk slot and the folder name in `/file/print`.

While a server runs, `/ip/service/print` shows its dynamic `upnp` listeners on UDP port 1900 and TCP port 2828. To test the server from a computer, use a player such as VLC, which lists UPnP media servers in its local network section.

When a player does not list the server:

- The player must be on the server's `interface`. Players in another subnet or VLAN cannot discover the server, because the SSDP discovery messages stay in one network. Add a second server with the same `path` on that interface.
- The firewall of the router must accept UDP port 1900 and TCP port 2828 from the players. The default firewall accepts all traffic from the LAN.
- `allowed-ip` or `allowed-hostname` must match the player. A device they do not match sees nothing.
- Open the player's list of servers again, or restart the player, so that it searches for servers again.

When a file is missing from the list, check that it is a video, music or picture file with a lower-case extension. Other files are not listed.

## Technical details

### Discovery

The server announces itself with SSDP `NOTIFY` messages to the UPnP multicast group `239.255.255.250:1900`, as a `urn:schemas-upnp-org:device:MediaServer:1` device with the `ContentDirectory:1` and `ConnectionManager:1` services. It also answers the `M-SEARCH` requests players send to find servers. The messages carry `CACHE-CONTROL: max-age=3600` and the address of the server description, for example `LOCATION: http://192.168.88.1:2828/mediaserver_description-1.xml`. The number in the file name differs for each server entry.

### Content

Players browse the folders through the ContentDirectory service and download the files over HTTP from TCP port 2828. Each folder is a container, and each media file an item with its media type, for example `video/mp4`, `audio/mpeg` or `image/jpeg`. A subtitle file is an extra `text/srt` resource of its video.

### Thumbnails

`/ip/media/settings` sets the cover pictures of folders:

```ros
/ip/media/settings/set thumbnails=folder.jpg
```

A file named `folder.jpg` is then no longer listed as a picture, and becomes the cover picture of the other files in its folder. `thumbnails` takes a comma-separated list of file names.

### Interface binding

A server serves requests that arrive on its interface, also from devices in another subnet whose traffic is routed to the router through that interface. The listeners accept connections on every interface, but a request for the server that arrives on another interface gets an HTTP 404 error, whichever router address it uses. The firewall is what keeps the WAN out: the default firewall drops input from the WAN.

For all parameters, see the CLI reference for [`/ip/media`](../cli-reference/ip/media/) and [`/ip/media/settings`](../cli-reference/ip/media/settings).
