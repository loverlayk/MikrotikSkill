# Default Configuration Passwords

> Find the default login credentials for MikroTik RouterOS devices fresh from the factory or after a full reset.

MikroTik devices ship from the factory with a default configuration that includes a preset password. The same password is re-applied whenever you perform a standard system reset. Knowing how to locate this password is essential for initial device access.

:::tip[Watch our official explainer]
[Default passwords: WHY?!](https://www.youtube.com/watch?v=mq7nIIILrVc) — a short overview of why MikroTik devices now ship with unique factory passwords.
:::

Earlier MikroTik models typically used the username `admin` with no password — type `admin` for the login and press **Enter** when prompted. Later models are manufactured with a unique default password per device.

:::note[Custom-branded units]
Custom-branded or OEM units may have a different default password. If you cannot locate a standard sticker, the device can still be reset with the **[Netinstall utility](../installation-and-upgrade/netinstall)**.
:::

## Where to Find the Password

The default password is printed in several physical locations:

- On the device itself, on the serial number sticker
- On the device packaging, also on the serial number sticker
- On the printed Quick Guide sheet included inside the product box

Some MikroTik [indoor wireless](https://mikrotik.com/products/indoor-wireless) devices (such as the [hAP ac³](https://mikrotik.com/product/hap_ac3) and [hAP ax³](https://mikrotik.com/product/hap_ax3)) have a dedicated **product information compartment** — a small panel on the underside of the device that houses the sticker with default credentials. Look for a compartment near the Ethernet ports or under an RF connector cover. Open the panel to reveal the serial number and default password printed on the sticker inside.

:::warning

Always check for these stickers before contacting support. The password is printed only on physical materials — it is not stored digitally in any online system.

:::

## If You Cannot Find the Password

If the stickers are missing or illegible, contact the MikroTik distributor that supplied the device. Provide the device serial number and the name of the seller or shop where you purchased the unit. Distributors maintain a password database and can retrieve the default password from the serial number.

:::tip

Watch our video guide: [Secret CSV password file for seamless configuration](https://www.youtube.com/watch?v=q9F871KkGBw) — learn how to use a CSV password file for automated device setup.

:::

If you cannot reach the distributor or the password is not retrievable, you can still regain access by **reinstalling RouterOS** with **[Netinstall](../installation-and-upgrade/netinstall)** or performing a **[full configuration reset](./routeros-configuration-reset)**.

:::tip[Mass-configuration with Flashfig]

For deploying multiple devices at scale, use the Flashfig tool:

- [Mass-config MikroTik with flashfig](https://www.youtube.com/watch?v=gticPeOdN54) (Windows)
- [Mass-config MikroTik with flashfig from Linux](https://www.youtube.com/watch?v=xasM81Qc11g) (Linux)

:::
