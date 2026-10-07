# 802.11 a/b/g/n

> MikroTik 802.11 a/b/g/n devices use the legacy /interface/wireless menu provided by the wireless package. This section covers the wireless interface, MikroTik-proprietary protocols (Nstreme, Nv2), HWMP+ mesh,...

# 802.11 a/b/g/n

This section covers MikroTik **802.11 a/b/g/n** devices (and any 802.11ac device running the `wireless` package), configured through the **`/interface/wireless`** menu (the **`wireless`** driver package) — the only option on MIPS-based devices.

This menu is also where the MikroTik-specific, throughput-oriented features live — **Nstreme** and **Nv2** (TDMA), **WDS**, and **HWMP+ mesh** — as well as the original **[CAPsMAN](./capsman/ap-controller-capsman.md)** (`/caps-man`) controller.

:::info
Some 802.11ac devices can instead run the new `/interface/wifi` menu via the `wifi-qcom-ac` package — see [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) to choose. WPA3 and fast roaming are only available through the new menu.
:::

<DocCardList />
