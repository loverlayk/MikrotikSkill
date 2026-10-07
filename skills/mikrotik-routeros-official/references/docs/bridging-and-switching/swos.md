# SwOS

> SwOS is a lightweight operating system built exclusively for the administration of MikroTik switching hardware. It delivers maximum wire-speed Layer 2 forwarding capability across all standard Ethernet frames,...

# Introduction to SwOS

SwOS is a lightweight operating system built exclusively for the administration of MikroTik switching hardware. It delivers maximum wire-speed Layer 2 forwarding capability across all standard Ethernet frames, handling IPv4, IPv6, and non-IP traffic seamlessly.

### Core & Advanced Features

Beyond standard managed switch capabilities, SwOS offers a robust suite of networking features:

* **VLAN Management:** Full configuration support for complex VLAN setups, including access and trunking ports.
* **Traffic Control:** Advanced broadcast storm control, bandwidth limiting, and port-to-port forwarding settings.
* **Monitoring & Mirroring:** Ingress/egress traffic mirroring along with real-time port-level statistics.
* **Security & Filtering:** A granular Access Control List (ACL) engine capable of matching traffic by MAC, IP, and port-level rules.
* **Hardware Offloading:** Direct hardware-driven manipulation of specific MAC and IP header fields on supported device models.

:::note Management Limitation
SwOS is configured exclusively through a standard web browser (HTTP) over IPv4. It does not support command-line interface (CLI) access via serial console/SSH, API access, WinBox, or other alternative management protocols.
:::

<DocCardList />
