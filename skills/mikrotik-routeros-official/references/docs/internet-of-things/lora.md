# Lora

> This page introduces MikroTik RouterOS LoRa and LoRaWAN configuration, covering gateway setup, general properties, server integration, and non-LoRaWAN payload forwarding with MQTT/HTTP. It details supported hardware,...

# Lora

This section covers LoRa and LoRaWAN features in RouterOS. Use it to configure LoRa gateways, general properties, and integrations with supported LoRaWAN networks.

<DocCardList />

Available settings:

- ## [General Properties](./general-properties.md)

Gateway initial steps and different LoRaWAN setup examples:

- ## [User Guides](./user-guides/index.md)

The term "LoRa" represents the "radio" itself ("LoRa payloads" are packets broadcasted by the nodes using the LoRa frequencies), while the term "LoRaWAN" represents a logical/link layer on top that enables the communication between "LoRa" devices. In other words, "LoRaWAN" is how the "LoRa" radio devices communicate.

**R11e-LR8** (operates in 863-870 MHz frequency), **R11e-LR9** (operates in 902-928 MHz frequency) and **R11e-LR2** (operates using 2.4 GHz frequencies) are concentrator Gateway cards for LoRa® technology in the mini PCIe form factor based on a Semtech chipset. They enable LoRa® connectivity for any MikroTik product that has an mPCIe slot with connected USB lines.

A typical LoRaWAN topology consists of 3 main elements → the server, the node and the gateway. The gateway's job is to simply forward received LoRa packets that are broadcasted by the nodes (within the same supported frequency spectrum) to the server.

MikroTik LoRaWAN gateways are devices that have an R11e-LR**x** miniPCIe card and have the "iot" [package](../../getting-started/installation-and-upgrade/packages.md) (which enables LoRa drivers) installed.

The primary design for the MikroTik gateway devices is to operate as LoRaWAN devices. To achieve this, simply configure/select a correct server in the LoRa interface settings. A few examples can be found in the [user guides section](./user-guides/index.md).

#### Non-LoRaWAN setup

However, if you do not wish to use a LoRaWAN network/topology, and you wish to forward "raw LoRa" payloads to your own server, you have an option to do so. You can use [MQTT](../mqtt/index.md) or [HTTP post](../../system-information-and-utilities/fetch.md) to forward received payloads to your MQTT/HTTP server, but it will require additional [scripting](../../developer-guides/scripting/index.md). The script will have to collect information (payloads) from the `IoT>LoRa>Traffic` tab, store those payloads as variables, structure an MQTT/HTTP message out of the variables and post it.

:::info
Please note that if the payloads broadcasted by the node are encrypted, and you wish to forward them to your own MQTT/HTTP server (without using LoRaWAN), you will need to decipher the payloads on the server-side. The gateway does not have the built-in functionality to decipher the node's data. Servers are responsible for this task.

Also, there is no option to "relay" downlink MQTT/HTTP messages back from the MQTT/HTTP server to the LoRa node (only "uplink" payloads from the nodes can be "forwarded" to the server), primarily because there is no way to "make" LR cards "broadcast" custom payloads (there is no way to pass the content of the MQTT/HTTP downlink message into the LoRa chip).
:::
