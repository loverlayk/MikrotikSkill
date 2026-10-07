# Try Before RMA

> A pre-RMA diagnostic checklist for MikroTik hardware. Rule out common power, boot, connectivity, and LTE issues before submitting a warranty request.

# Try Before RMA

Before submitting a device for warranty repair (RMA), work through the checks below. Many apparent hardware issues are caused by power supplies, cables, software versions, or configuration — and can be resolved without sending the device back.

## Power and boot

| Symptom | What to try |
| :-- | :-- |
| Device does not power on | Use a different compatible power supply and/or PoE injector. |
| Device does not boot | Load the backup RouterBOOT: hold the **Reset** button, power on the device, keep holding **Reset** for 2–3 seconds. If the device boots, upgrade the bootloader with `/system/routerboard/upgrade`. If it still fails, reinstall with [Netinstall](../getting-started/installation-and-upgrade/netinstall/index.md). |
| Device reboots under load | Try a different power supply. Upgrade RouterOS to the latest Stable version. Reset the configuration with `/system/reset-configuration`. |
| Device reboots without load | Upgrade RouterOS to the latest Stable version. Reset the configuration with `/system/reset-configuration`. |

## Ethernet and SFP

| Symptom | What to try |
| :-- | :-- |
| Cannot connect to the device | Try a different port — you may be using the WAN port from the default configuration. Verify the cable and port are not physically damaged. |
| Unable to [Netinstall](../getting-started/installation-and-upgrade/netinstall/index.md) | Ensure a direct Ethernet connection, same subnet, and disabled firewalls. Try placing a switch between the PC and the device. See the [Netinstall guide](../getting-started/installation-and-upgrade/netinstall/netinstall-windows.md) for details. |
| Ethernet port not linking | Try a different Ethernet cable. If PoE-in is used, try a different PoE injector. |
| SFP / SFP+ / QSFP port not linking or low throughput | Ensure both ends of the link are compatible. Use the correct optical cable type (single-mode or multimode). Verify the SFP module is supported. |

## LTE

| Symptom | What to try |
| :-- | :-- |
| SIM card not recognized | Try a different SIM card. Check the card orientation and ensure it is fully inserted or clicked into the slot. |
| LTE does not connect | Verify the APN is correct. Check your service provider's documentation for the required APN value. |
| LTE connects but no data passes | Verify the APN is correct. Ensure routing and firewall rules allow traffic. |
| Missing LTE interface | Confirm the device is an LTE Kit variant and that the modem is physically installed. |
| LTE modem not recognized | Install the latest RouterOS Stable version. |

## Other

| Symptom | What to try |
| :-- | :-- |
| LED not working | Install the latest RouterOS Stable version and apply the default configuration. |
| Case is bent or damaged | Inspect the packaging for damage. Shipping damage should be reported to the shipping company. |

:::info
If none of the above steps resolve the issue, contact [MikroTik support](https://mikrotik.com/support) with a description of the problem and a [support output file (`supout.rif`)](../getting-started/supout-rif).
:::
