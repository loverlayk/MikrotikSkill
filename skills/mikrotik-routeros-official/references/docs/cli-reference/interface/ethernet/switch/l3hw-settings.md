# l3hw-settings

> The L3HW Settings menu allows configuring global parameters for the Layer 3 Hardware Offloading driver.

-----------

## interface/ethernet/switch/l3hw-settings 
**Syscap:** rbswitch and crs_prestera
**Type:** Settings Directory

The L3HW Settings menu allows configuring global parameters for the Layer 3 Hardware Offloading driver.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="autorestart" typ="bool" syscap="!prestera-cpss">Automatically restarts L3HW in case of driver failure. If autorestart is not enabled, then `l3-hw-offloading` gets disabled, and the error code is displayed in the [monitor](./monitor). Autorestart does not work for system failures, such as OOM (Out Of Memory).</ArgTableRow>
<ArgTableRow arg="fasttrack-hw" typ="bool" syscap="!prestera-ac3">Enables or disables FastTrack HW Offloading. Keep it enabled unless HW TCAM memory reservation is required, e.g., for dynamic switch ACL rules creation. Not all switch chips support FastTrack HW Offloading (see [`hw-supports-fasttrack`](#hw-supports-fasttrack)).</ArgTableRow>
<ArgTableRow arg="ipv6-hw" typ="bool">IPv6 hardware offloading. IPv6 routes occupy a lot of HW memory, enable this option only if IPv6 traffic is significant enough to benefit from hardware routing.</ArgTableRow>
<ArgTableRow arg="icmp-reply-on-error" typ="bool">Since the hardware cannot send ICMP messages, the packet must be redirected to the CPU to send an ICMP reply in case of an error (e.g., "Time Exceeded", "Fragmentation required", etc.). Enabling helps with network diagnostics but may open potential vulnerabilities for DDoS attacks. Disabling silently drops the packets on the hardware level in case of an error.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-supports-fasttrack" typ="bool">Indicates if the hardware (switch chip) supports FastTrack HW Offloading.</ArgTableRow>
</ArgTable>
