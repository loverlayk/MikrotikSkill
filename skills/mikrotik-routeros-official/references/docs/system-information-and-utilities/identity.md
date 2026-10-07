# Identity

> The system identity is the router's name, shown in the CLI prompt, in neighbor discovery, as the SNMP system name and as the DHCP client host name. Set it in the CLI, in WinBox or over SNMP.

# Identity

The system identity is the name of the router. The default is `MikroTik`. Give each router its own name so that you can tell them apart. The identity appears in several places, including:

- In the command-line prompt, for example `[admin@Riga-Office-GW] >`, and in the title of the WinBox connection.
- In [neighbor discovery](neighbor-discovery): neighboring devices list the router under its identity, updated with the next announcement, every 30 seconds by default.
- As the SNMP system name (`sysName`).
- As the host name that the [DHCP client](../network-management/dhcp/client) sends to the DHCP server by default.
- As the default SSID of interfaces of the older `wireless` package ([legacy wireless](../wireless/abgn/wireless-interface)).
- In scripts, as `[/system/identity/get name]`.

The identity can be up to 64 characters long. A longer name is refused with `could not change identity: too long`. Spaces and other characters are allowed, with quotes, for example `name="Riga Office GW"`; because the DHCP host name and DNS names do not allow spaces, a name of letters, digits and hyphens works everywhere.

## Set the identity

A name that says where the router is and what it does helps when you manage several routers, for example `Riga-Office-GW`:

```ros
/system/identity/set name=Riga-Office-GW
/system/identity/print
```

```text
  name: Riga-Office-GW
```

The prompt shows the new name:

```text
[admin@Riga-Office-GW] >
```

## Set the identity in WinBox

In WinBox, open **System > Identity**, enter the router name in **Identity** (callout 1), and select **OK**. Use a name that helps you distinguish the router from other devices, such as `Home-Router`. The name also appears in WinBox's connection title.

![WinBox Identity dialog with a callout around the Identity field](./img/identity-winbox.webp)

## Set the identity over SNMP

A management system can set the identity with an SNMP set request for `sysName.0` (`1.3.6.1.2.1.1.5.0`). This needs an [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp) community with write access; the default community `public` can only read and refuses an SNMPv1 set request with `readOnly`. A community with write access can also change other settings and reboot the router, so give it a name that is hard to guess, because the name works as a password, and limit it to the address of the management system:

```ros
/snmp/community/add name=netadmin-7Qx2 addresses=192.168.88.10/32 \
    write-access=yes
/snmp/set enabled=yes
```

From the management system, for example with `snmpset` on Linux or macOS:

```bash
snmpset -v 1 -c netadmin-7Qx2 192.168.88.1 1.3.6.1.2.1.1.5.0 s Branch-GW
```

```text
SNMPv2-MIB::sysName.0 = STRING: Branch-GW
```

SNMPv1 and SNMPv2c send the community name in clear text. Allow write access only from trusted addresses, or use SNMPv3 with authentication and encryption. The `public` community stays readable from any address unless you limit its addresses too.

For the parameter, see the [`/system/identity` CLI reference](../cli-reference/system/identity).
