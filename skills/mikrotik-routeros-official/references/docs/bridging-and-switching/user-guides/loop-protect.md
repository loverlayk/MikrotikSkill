# Loop Protect

> Loop Protect prevents Layer2 loops by detecting and disabling interfaces receiving their own loop-protect packets, with configurable intervals and disable times. It supports Ethernet, VLAN, EoIP, and VxLAN...

# Loop Protect

The loop protect feature can prevent Layer2 loops by sending loop protect protocol packets and shutting down interfaces in case they receive loop protect packets originating from themselves. The feature works by checking the source MAC address of the received loop-protect packet against the MAC addresses of loop-protect enabled interfaces. If the match is found, loop protect disables the interface that received the loop protect packet. A log message warns about this event and the interface is marked with a loop protect comment by the system. The RouterOS loop protect feature can be used on bridged interfaces as well as on Ethernet interfaces which are set for switching in RouterBoard switch chips.

Loop Protect works on Ethernet, VLAN, EoIP, VxLAN interfaces and its packets are encapsulated with EtherType 0x9003.  
The loop protect packet interval and interface disable time can be adjusted. Configuration changes or expiration of disable time resets loop protection on an interface.

On a switch chip that supports ACL rules, loop protect on an Ethernet interface adds a dynamic ACL rule that redirects loop protect packets to the CPU.

Enable loop protect on untrusted access ports, where the connected end devices can create a loop. Examples are unmanaged switches and hosts that bridge their Ethernet and Wi-Fi interfaces. These devices usually do not run STP, so the bridge cannot detect the loop.

:::warning
Even though loop-protect can work on interfaces that are added to a bridge, it is still recommended to use (R/M)STP rather than loop-protect since (R/M)STP is compatible with most switches, and STP variants provide many more configuration options to fine-tune your network.
:::

**Sub-menu:** `/interface/ethernet, /interface/vlan, /interface/eoip, /interface/eoipv6, /interface/vxlan`

| Property | Description |
| :-- | :-- |
| **loop-protect** (*on \| off \| default*; Default: **default**) | Enables or disables loop protect on the selected interface. **default** works as turned off. |
| **loop-protect-send-interval** (*time interval*; Default: **5s**) | Sets how often loop protect packets are sent on the selected interface. |
| **loop-protect-disable-time** (*time interval \| 0*; Default: **5m**) | Sets how long the selected interface is disabled when a loop is detected. **0** - forever. |

### Read-only properties

| Property | Description |
| :-- | :-- |
| **loop-protect-status** (*on \| off \| disabled*) | on - loop-protect feature is turned on, the interface is sending and listening for loop protect packetsoff - loop-protect feature is turned offdisabled - loop-protect feature is turned on, the interface has received a loop protect packet and disabled itself to prevent a loop. |
