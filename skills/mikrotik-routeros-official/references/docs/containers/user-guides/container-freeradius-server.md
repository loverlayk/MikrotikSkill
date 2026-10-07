# Container - freeradius server

> This page introduces the container feature in MikroTik RouterOS for running servers like RADIUS within the router, detailing setup steps including container mode activation, networking configuration, and image...

# Container - freeradius server

## Introduction

The introduction of the container feature into RouterOS made it possible to run all kinds of servers for all sorts of tasks inside the router. This is especially relevant for people who want to reduce the number of devices in their network. Instead of running a server on a separate device/machine, why not run it inside the router?

[Radius](../../authentication-authorization-accounting/radius.md) is short for Remote Authentication Dial-In User Service. RouterOS has a RADIUS client feature that can authenticate for HotSpot, [PPP](../../mobile-networking/ppp.md), [PPPoE](../../virtual-private-networks/pppoe/index.md), [PPTP](../../virtual-private-networks/pptp.md), [L2TP](../../virtual-private-networks/l2tp/index.md), and ISDN connections. Basically, this feature allows you to connect RouterOS to a Radius Server, and then, utilize the user database from the server for client authentication.

In our example, we will showcase the **[freeradius/freeradius-server](https://hub.docker.com/r/freeradius/freeradius-server/tags)** image installation.

## Summary

**Sub-menu:** `/container`

***Note**:* The **container** package is required.

Make sure to study our [container](../) guide before proceeding with the configuration. Make sure to check the [disclaimer](../#disclaimer) and [requirements](../#requirements) sections to understand all the risks and necessary steps you might be required to do.

At the time when the guide was published, the image was available for Linux/**amd64** OS/architecture **only** (usable by CHR and x86 devices). For arm64 devices you will need to make your own container from the [FreeRADIUS source](https://github.com/FreeRADIUS/freeradius-server). For both arm64 and arm32 devices, you can also use **[freeradius/freeradius-server-dev](https://hub.docker.com/r/freeradius/freeradius-dev)** image **at your own risk** (as it is an "experimental/development" version of the image).

To help you set up a CHR in a [Virtual Box](https://www.virtualbox.org/), please check our [YouTube tutorial](https://www.youtube.com/watch?v=oHXkaHkSVVo), or [Make your own x86 router](https://www.youtube.com/watch?v=JpccW9tYOkQ).

:::warning
This guide demonstrates a basic example! The tests were performed in a local environment! This guide is meant for basic RADIUS "testing" purposes! Not all "freeradius" feature were tested!
:::

## Configuration

### Container mode

Enable container mode:

```ros
/system/device-mode/update container=yes
```

You will need to confirm the device-mode with a cold reboot if using the container on X86.

### Networking

Add veth interface for the container:

```ros
/interface/veth/add name=veth3 address=172.17.0.2/24 gateway=172.17.0.1
```

Create a bridge for the container, assign an IP network to it, and add veth to the bridge:

```ros
/interface/bridge/add name=dockerfreeradius
/ip/address/add address=172.17.0.1/24 interface=dockerfreeradius
/interface/bridge/port/add bridge=dockerfreeradius interface=veth3
```

Setup NAT for outgoing traffic if required:

```ros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
```

### Getting image

To simplify the configuration, we will get the image from an external library, but you can also import it via the [.tar](../#option-b-import-image-from-pc) file.

Make sure that you have "Registry URL" set accordingly, limit RAM usage (if necessary), and set up a directory for the image:

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull
```

Pull the image with the help of the command:

```ros
/container/add remote-image=freeradius/freeradius-server:latest interface=veth3 root-dir=freeradius logging=yes cmd="-X"
```

where `cmd="-X"` enables debug logging (per the "freeradius" documentation).

After running the command, RouterOS should start "extracting" the package. Check "File System" for newly created folders and monitor container status with the command `/container/print`.

### Starting the container

After you make sure that the container has been added and the status has changed to `status=stopped` after using `/container/print`, you can initiate it:

```ros
/container/start 0
```

### Altering the server's configuration files

To access the server's configuration files (**clients.conf** and **authorize**), we will need to use the SFTP (file transfer over SSH) protocol, so make sure that SSH [service](../../system-information-and-utilities/services.md) is enabled.

Open your command terminal ("CMD", as Administrator, for Windows users, or "Linux Shell or Command Terminal" for Linux users) and navigate to the directory where you want to download the configuration files. For example, to the "radius" folder on your "Desktop":

```powershell
C:\WINDOWS\system32>cd C:\Users\Administrator\Desktop\radius
 
C:\Users\Administrator\Desktop\radius>
```

Initiate SFTP to the device's IP address:

```powershell
C:\Users\Administrator\Desktop\radius>sftp admin@10.55.8.53
admin@10.55.8.53's password:
Connected to 10.55.8.53.
sftp>
```

Go to the server's configuration file folder (use the `dir` or `ls` command to see the content of the folder you are in and the `cd` command to go to the folder of our choice).

The first file, "clients.conf", allows you to define RADIUS clients. Per the "freeradius" documentation, it should be under the `/etc/freeradius` directory...so, navigate there and use the `get` command to download it:

```powershell
sftp> dir
freeradius          pub                     pull                    skins                   
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> get clients.conf
Fetching /freeradius/etc/freeradius/clients.conf to clients.conf
/freeradius/etc/freeradius/clients.conf                                               100% 8323     1.2MB/s   00:00
```

Open "**clients.conf**" via your preferred text editor (Notepad or any other). You can study the file to see all the options that you have (additionally, check [freeradius.org](https://wiki.freeradius.org/config/Configuration-files)). This example shows a basic setup, so we will just overwrite the whole file with the lines shown below:

```text
client new {
    ipaddr = 0.0.0.0/0
    secret = client_password
}
```

where we indicate that our radius client can connect using any possible IP address (**ipaddr=0.0.0.0/0** ensures that, but you also can change it to the actual ip address/mask of your radius client if you need to do so) and that our secret is "client\_password" (you can change it to any other secret).

Save the file/overwrite it.

The second file, "authorize", allows you to set up users. Per the "freeradius" documentation, it should be under `/etc/freeradius/mods-config/files`. Go there and `get` the file:

```powershell
sftp> dir
freeradius          pub                     pull                    skins                    
sftp> cd freeradius/etc/freeradius/mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> get authorize
Fetching /freeradius/etc/freeradius/mods-config/files/authorize to authorize
/freeradius/etc/freeradius/mods-config/files/authorize                                100% 6594     1.1MB/s   00:00
```

Open "**authorize**" via your preferred text editor (notepad or any other). This example shows a basic setup, so we will just uncomment (remove the "#" symbol from) the line shown below (leave the rest of the configuration/lines as they are):

```text
bob	Cleartext-Password := "hello"
```

which creates a username "bob" and sets the password to "hello" (you can change the username and password).

Save the file/overwrite it.

Upload both files back to overwrite the default files with the help of the `put` command:

```powershell
sftp> dir
freeradius          pub                     pull                    skins      
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> put clients.conf
Uploading clients.conf to /freeradius/etc/freeradius/clients.conf
clients.conf                                                                          100%   67    22.3KB/s   00:00
sftp> cd mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> put authorize
Uploading authorize to /freeradius/etc/freeradius/mods-config/files/authorize
authorize                                                                             100% 6626     1.6MB/s   00:00
```

Restart the container:

```ros
/container/stop 0
/container/start 0
```

Make sure to wait for the container to stop (`status=stopped` should be shown after using the `/container/print` command) before initiating it again.

## Result verification

In RouterOS, add a new RADIUS client configuration:

```ros
/radius/add service=login address=172.17.0.2 secret="client_password"
```

, where the `address` is the IP address of the veth3 interface, `secret` is the secret that we configured in the **clients.conf** file and `service` is the allowed service that you wish to use.

Allow "login" with RADIUS users via the command:

```ros
/user/aaa/set use-radius=yes
```

We have allowed the "login" service for RADIUS and we can test it using an ssh/winbox/webfig connection. For the SSH test, issue the command (where you need to indicate the device's management IP and input bob's password "hello" after):

```ros
/system/ssh 10.55.8.53 user=bob
```

You should be able to verify that the terminal user changed from "admin@MikroTik" to "bob@MikroTik":

```ros
[admin@MikroTik] > /system/ssh 10.55.8.53 user=bob
password:hello                                                                                                                                                                 
 

  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.8alpha173 (c) 1999-2023       https://www.mikrotik.com/

Press F1 for help
  
[bob@MikroTik] > 
```

If you issue the command `/user/active/print`:

```ros
/user/active/print
Flags: R - RADIUS
Columns: WHEN, NAME, ADDRESS, VIA
#   WHEN                  NAME   ADDRESS     VIA    
0   2023-02-16 16:31:21  admin  xx.xx.xx.xx  winbox 
1   2023-02-16 16:38:46  admin  xx.xx.xx.xx  console
2 R 2023-02-16 16:38:53  bob    10.55.8.53  ssh  
```

you will be able to verify that a new user "bob" is "active" and has a flag "R" assigned, which indicates it is a RADIUS user.
