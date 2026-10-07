# Wi-Fi 5 (802.11ac)

> MikroTik 802.11ac (Wi-Fi 5) ARM devices can be driven two ways: through the new /interface/wifi menu using the wifi-qcom-ac package (WPA3, fast roaming, new CAPsMAN) or through the legacy /interface/wireless menu...

# Wi-Fi 5 (802.11ac)

This section covers MikroTik **802.11ac (Wi-Fi 5)** ARM-based devices. These products are special: the **same hardware can be configured through either of two RouterOS menus**, depending on which driver package is installed. Pick the one that matches the features you need.
:::warning
`wifi-qcom-ac` drivers are very resource-heavy. We suggest using our WiFi 5 (802.11ac) devices with their original `wireless` drivers as they are lightweight.
:::

## Two ways to run an 802.11ac device

| If you need… | Install package | Configure under | Documentation |
| :-- | :-- | :-- | :-- |
| WPA3, fast roaming (802.11r), the new CAPsMAN | `routeros` + `wifi-qcom-ac` | `/interface/wifi` | [Wi-Fi 6 / 7 (802.11ax/be)](../wifi/index.md) — the `/interface/wifi` menu is shared |
| Nstreme, Nv2, WDS, HWMP+ mesh, the old CAPsMAN | `routeros` + `wireless` | `/interface/wireless` | [802.11 a/b/g/n](../abgn/index.md) — the `/interface/wireless` menu is shared |

You cannot use both packages at the same time on the built-in radios — see [Replacing the 'wireless' package](../wifi/index.md) for how to switch.

:::info
The new `/interface/wifi` menu manages **Wi-Fi 5 wave2 and newer** interfaces, so 802.11ac devices running `wifi-qcom-ac` use exactly the same configuration as the 802.11ax/be devices documented under [Wi-Fi 6 / 7 (802.11ax/be)](../wifi/index.md). This section therefore links to that reference rather than duplicating it.
:::

## Devices with a choice of driver

The following 802.11ac ARM models can run either `wifi-qcom-ac` (new `/interface/wifi` menu) or `wireless` (legacy `/interface/wireless` menu):

> Audience, Audience LTE kit, Chateau (all variants of D53), hAP ac², hAP ac³, cAP ac, cAP XL ac, LDF 5 ac, LHG XL 5 ac, LHG XL 52 ac, NetMetal ac², mANTBox 52 15s, wAP ac (RBwAPG-5HacD2HnD), SXTsq 5 ac

:::warning
The `wifi-qcom-ac` driver upgrade is primarily meant for indoor devices. Even though it can also be installed on our outdoor models (LDF 5 ac, LHG XL 5 ac, LHG XL 52 ac, NetMetal ac², mANTBox 52 15s, SXTsq 5 ac), `wifi-qcom-ac` is not tailored for outdoor usage. This is primarily because the drivers do not support the **distance** setting, which is required for links longer than 2 km. We therefore recommend using the `wireless` drivers on all our outdoor boards.
:::

For choosing packages by device type and CAPsMAN scenario, see the decision tables on the [Wireless overview](../index.md).
