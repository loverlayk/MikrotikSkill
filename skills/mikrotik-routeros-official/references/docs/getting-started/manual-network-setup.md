# Manual Network Setup (No Default Configuration)

> How to manually set up a MikroTik router that has no default configuration: reset to a clean state, create a bridge, assign a LAN IP address, and configure a DHCP server using CLI or WinBox/WebFig.

# Manual Network Setup (No Default Configuration)

Most MikroTik routers ship with a [default configuration](./configuration-management/default-configurations) that already provides a bridge, a LAN IP address, a DHCP server, and a basic firewall. If you keep the default configuration, you can skip this page.

Follow the steps below only if your device has **no default configuration**, or if you have reset it to a clean state.

## Start from a clean configuration

1. Connect the Internet cable to the router's **ether1** port.
2. Connect your computer to any other **Ethernet** port.
3. Open WinBox and locate the router using Neighbor Discovery. For detailed instructions, see the [WinBox article](../management-tools/winbox).
4. Select the router's MAC address and click **Connect**.

To start with a completely clean configuration, run the following command:

```ros
/system/reset-configuration no-defaults=yes skip-backup=yes
```

The router will reboot without any default settings, firewall rules, or services configured.

Or from WinBox:

![](./img/reset-config-to-default_01.png)

## Create a bridge and assign an IP address

Since a MAC connection can sometimes be unreliable, the first step is to enable IP connectivity. This involves three main tasks:

- Create a bridge interface and assign bridge ports
- Assign an IP address to the bridge interface
- Configure a DHCP server

<Tabs>
<TabItem value="cli" label="CLI" default>

Create a bridge interface, add the desired Ethernet port as a bridge port, and assign the IP address to the bridge:

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add interface=ether2 bridge=bridge1
/ip/address/add address=192.168.88.1/24 interface=bridge1
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

1. Open the **Bridge** window, ensuring the **Bridge** tab is selected.
   - Click the <kbd>**New**</kbd> or <kbd>**+**</kbd> button to open a new dialog box. You can either enter a custom bridge name or retain the default **bridge1**, then click <kbd>**OK**</kbd> to proceed.

     ![](./img/add_bridge.png)
2. Switch to the **Ports** tab and click the <kbd>**New**</kbd> or <kbd>**+**</kbd> button to open another dialog box.
   - Select **ether2** as the interface and **bridge1** as the bridge, then click <kbd>**OK**</kbd>. Repeat this step for each additional port that you want to add to the bridge.

     ![](./img/add_bridge_port.png)
   - You may close the bridge dialog.
3. Access the **IP** menu and navigate to the **Address** dialog.
   - Click the <kbd>**New**</kbd> or <kbd>**+**</kbd> button to open a new dialog box.
   - Enter IP address **`192.168.88.1/24`** and select interface **bridge1** from the dropdown list.

     ![](./img/ip_addr_add.png)
   - Click <kbd>**OK**</kbd> to confirm the settings.

</TabItem>
</Tabs>

## Set up a DHCP server

<Tabs>
<TabItem value="cli" label="CLI" default>

To simplify and expedite this process, run the setup command. Most of the configuration options are automatically determined, so you simply need to press <kbd>Enter</kbd> to accept each value:

```ros
[admin@MikroTik] > ip dhcp-server/ setup [enter]
Select interface to run DHCP server on 

dhcp server interface: bridge1 [enter]
Select network for DHCP addresses 

dhcp address space: 192.168.88.0/24 [enter]
Select gateway for given network 

gateway for dhcp network: 192.168.88.1 [enter]
Select pool of ip addresses given out by DHCP server 

addresses to give out: 192.168.88.2-192.168.88.254 [enter]
Select DNS servers 

dns servers: 192.168.88.1 [enter]               
Select lease time 

lease time: 1800 [enter]
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

The DHCP Server Setup wizard is also available in [WinBox](../management-tools/winbox) and [WebFig](../management-tools/webfig):

- Navigate to the **IP → DHCP Server** window, ensuring the **DHCP** tab is selected.
- Click the <kbd>**DHCP Setup**</kbd> button to open a new dialog.

  ![](./img/dhcp_setup_01.png)

- Select **bridge1** as the **DHCP Server Interface** and click <kbd>**Next**</kbd>.
- Follow the wizard to complete the setup.

</TabItem>
</Tabs>

Following these steps, the connected PC should obtain a dynamic IP address automatically. You can then close WinBox and reconnect to the router using the IP address **`192.168.88.1`**.

When IP connectivity is working, continue with [Configuring the internet connection](./first-time-configuration.md#configuring-the-internet-connection-wan) and the rest of the first-time guide.
