# CHR: Troubleshooting

> This page covers troubleshooting for MikroTik RouterOS CHR, addressing IGMP snooping issues on Linux bridges, VLAN-related data flow problems between guests and the outside world, VLAN tagging requirements in...

# CHR: Troubleshooting

### Using Bridge on Linux

If the Linux bridge has IGMP snooping enabled and you experience issues with IPv6 traffic, disable this feature. IGMP snooping interferes with MLD packets (multicast) and prevents them from passing through the bridge.

```
echo -n 0 > /sys/class/net/vmbr0/bridge/multicast_snooping
```

### Packets Not Passing from Guests

**Problem:** After configuring a software interface (VLAN, EoIP, bridge, etc.) on the guest CHR, the router stops passing data to the outside world.

**Solution:** Check your virtualization management system (VMS) security settings. Verify that:

- Other MAC addresses are allowed to pass
- Packets with VLAN tags are allowed to pass through

Adjust the security settings as needed—for example, enable MAC spoofing or allow a specific MAC address range. For VLAN interfaces, you can typically define allowed VLAN tags or a VLAN tag range.

### Using VLANs on CHR in Various Hypervisors

CHR does not control external VLAN tagging; it only processes VLAN tags received from the virtual network interface.
In some hypervisors, VLAN tagging must be configured on the hypervisor side before it can be used inside the CHR VM.

**Useful articles:**

- Hyper-V VLAN configuration (official Microsoft documentation):
  - https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/configure-virtual-local-area-networks-for-hyper-v

- Hyper-V VLAN trunk configuration with PowerShell:
  - https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmnetworkadaptervlan?view=windowsserver2025-ps

## VMware Integration Notes

CHR does not support VMware Tools or any guest agent integration.

Guest-level automation (such as running scripts inside CHR via VMware Tools, VIX, or vSphere APIs) is not available.

Only basic hypervisor functions such as power management and resource allocation are supported.
