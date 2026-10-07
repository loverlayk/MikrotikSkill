# S+RJ10 general guidance

> S+RJ10 is a MikroTik 6-speed RJ45 SFP+ module offering 10 Gbps speeds via copper cables, with guidance on its use in MikroTik devices, including recommended placement to prevent overheating when used alongside...

# S+RJ10 general guidance

### Summary

[MikroTik S+RJ10](https://mikrotik.com/product/s_rj10) is a unique 6-speed RJ-45 SFP+ module based on a Marvell 88X3310P transceiver. It offers up to 10 Gbps speeds using twisted-pair copper cables. All the current MikroTik devices with an SFP+ cage support the S+RJ10 module. This article serves as a guideline for S+RJ10 usage in MikroTik devices with both passive and active cooling.

### General Guidance

#### Product specification

The average power consumption of the transceiver is 2.7 W (10GBASE-T, 30 m link) which is relatively high compared with the [S+85DLC03D](https://mikrotik.com/product/Splus85DLC03D) optical module with a maximum 0.8W power consumption. The operating temperature is 0 to +70 C, but the transceiver itself can heat up to 90 C.

#### S+RJ10 Positioning in devices

Due to high operating temperatures, it is recommended to use S+RJ10 transceivers while an optical transceiver or an unused SFP+ interface is in between them. Take a look at the transceivers' capable distance [comparison table](../wired-connections/mikrotik-wired-interface-compatibility.mdx#srj10).

As mentioned, S+RJ10 heat up more than regular transceivers, and keeping them side by side can result in overheating, especially in devices with 4 linear SFP cages. It is recommended to place S+RJ10 in every second interface while keeping an optical transceiver or an empty port in between them.

![](./img/s-plus-rj10-general-guidance-01.webp)

Even when using devices that come with separated SFP+ cages, for example, CRS309-1G-8S+, it is still not recommended to deploy the S+RJ10 transceivers beside each other. Use S+RJ10 in every second interface to avoid transceiver overheating, which may cause unpredictable behavior.

![](./img/s-plus-rj10-general-guidance-02.webp)Recommended S+RJ10 placement![](./img/s-plus-rj10-general-guidance-03.webp)It is not recommended to place transceivers side by side

Devices that come with 4 or 8-block SFP+ cages are not exceptions. It is recommended to use one S+RJ10 transceiver per 4xSFP+ cage block and avoid placing them side by side. Keep at least one vertical row empty (without S+RJ10) after plugging the S+RJ10 transceiver.

![](./img/s-plus-rj10-general-guidance-04.webp)Recommended S+RJ10 placement![](./img/s-plus-rj10-general-guidance-05.webp)We do not recommend placing transceivers side by side

### Using the S+RJ10 Side by Side or with passive cooling devices

There might be situations when it is not possible to use the recommended layout of the transceivers. In such cases where two or more S+RJ10 transceivers are plugged in beside one another or modules are used in passive cooling devices, the network administrator has to ensure additional cooling. The airflow around the device should be increased or the overall ambient temperature should be lowered to keep the temperature of the transceivers within the recommended range.
