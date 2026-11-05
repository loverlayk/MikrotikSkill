# Configuring EasyMesh

> Configure a Wi-Fi EasyMesh network in RouterOS: set up the controller and agents, create fronthaul and backhaul configurations, onboard agents with WPS, and monitor the mesh.

# Configuring EasyMesh

**Package:** `wifi-qcom`, `wifi-qcom-ac`

:::warning

- EasyMesh is available in CLI (no GUI support yet).
- At this moment, it works on `wifi-qcom` and `wifi-qcom-ac` only.
- When onboarding an agent over Wi-Fi, configure the fronthaul with `wpa2-psk` or `wpa2-psk,wpa3-psk`. WPS onboarding uses the fronthaul configuration, while the agent's backhaul credentials are delivered over the backhaul link. WPS does not support WPA3-only (SAE).
- DPP (Wi-Fi Easy Connect) onboarding is not implemented. To onboard an agent, use the WPS push-button or connect the agent over Ethernet.

:::

EasyMesh is a Wi-Fi Alliance standard for managing Wi-Fi APs and wireless extenders from different vendors as one coordinated network. A controller distributes fronthaul (client SSID) and backhaul (agent SSID) settings to managed APs (agents), which bridge their fronthaul interfaces to a wireless or Ethernet backhaul interface via Layer 2, preserving client MAC addresses during client traffic forwarding. The result is one Layer 2 network under a single controller. For all settings, see the [EasyMesh CLI reference](../../cli-reference/interface/wifi/easymesh/).

[CAPsMAN](./capsman) provides similar centralized management for MikroTik devices, but it is primarily intended for access points connected to the network with Ethernet. It does not provide the standardized wireless backhaul and WPS onboarding. EasyMesh certification allows a controller to manage certified agents from different vendors. Interoperability still depends on the devices, so test the controller and agent combination before deployment.

## Topology

An EasyMesh network has one controller and one or more agents. The controller and agents must be in the same Layer 2 network. Agents connect to the controller over a wired Ethernet connection or a wireless backhaul link. The backhaul (wired and wireless) carries EasyMesh management traffic and the client traffic of each agent.

A device performs one of three EasyMesh roles:

- `controller` - manages the EasyMesh network. It provides the fronthaul and backhaul configurations and coordinates the agents. Use it on a device that only performs controller duties.
- `agent` - joins the EasyMesh network and receives its configuration from the controller. It broadcasts the configured fronthaul networks and connects to the controller over a wireless backhaul link or a wired Ethernet connection. Use it on additional access points.
- `controller-and-agent` - performs both roles on the same device. A single Wi-Fi device can manage the EasyMesh network and also serve clients as an agent. Use it on the main router or access point with Wi-Fi radios.

Only the controller manages the network. An agent receives and applies configuration (it does not manage other agents, but it can relay controller traffic over the backhaul).

In most setups, the main router uses `controller-and-agent` and additional access points use `agent`.

The radios on these devices can perform the following roles:

- Fronthaul AP - broadcasts the client networks. Client devices connect to these BSSes.
- Backhaul AP - broadcasts the backhaul network. Agents use it to connect to the controller. Client devices do not use this network.
- Backhaul station - connects an agent to the controller's backhaul AP. It is used only for a wireless backhaul.

The same radio can provide both fronthaul and backhaul BSSes. Fronthaul interfaces stay dedicated to clients and are bridged to the backhaul.

The controller and agents exchange EasyMesh control messages with the IEEE 1905.1 standard (EtherType `0x893A`). It carries Wi-Fi Alliance Multi-AP Control Message Data Units (CMDUs) and TLVs over the Layer 2 backhaul. WPS onboarding uses 802.11/EAP-WSC.

## Controller configuration

### Set the radio manager

Set the EasyMesh manager on every radio that EasyMesh should control:

```ros
/interface/wifi
set [find default-name=wifi1] configuration.manager=easymesh
set [find default-name=wifi2] configuration.manager=easymesh
```

Adjust the interface names to match your device.

### Create the Wi-Fi configurations

Create a fronthaul configuration for clients and a backhaul configuration for wireless agents:

```ros
/interface/wifi/configuration
add name=em_fh ssid=em_fh security.authentication-types=wpa2-psk security.passphrase=fronthaul-password
add name=em_bh ssid=em_bh security.authentication-types=wpa2-psk security.passphrase=backhaul-password
```

- `em_fh` is the client network, broadcast by agents for client devices.
- `em_bh` is the backhaul network, broadcast by agents for other agents to connect to. Use a separate SSID and password from the client network.

### Enable the controller

```ros
/interface/wifi/easymesh
set enabled=yes role=controller-and-agent bridge=bridge bhaul-configuration=em_bh fhaul-configurations=em_fh dpp-onboarding=no
```

- `role=controller-and-agent` makes the device manage the network and provide Wi-Fi. Use `role=controller` if the device only manages the network.
- `bridge=bridge` is the bridge that connects the controller to the agents. Use the existing LAN bridge.
- `bhaul-configuration=em_bh` selects the backhaul configuration.
- `fhaul-configurations=em_fh` selects the client network. Add more configuration names to broadcast more networks.

The backhaul SSID and security come from the `em_bh` configuration. Wireless agents receive these credentials during onboarding.

## Agent configuration

### Prepare the access point

Configure the agent as a bridged access point. Set the EasyMesh manager on every radio:

```ros
/interface/wifi
set [find default-name=wifi1] configuration.manager=easymesh
set [find default-name=wifi2] configuration.manager=easymesh
```

Configure the bridge and the management IP address as described in [Configuring standalone access point](./configuring-standalone-access-point). The bridge must include the Ethernet port used for a wired backhaul.

### Enable the agent

```ros
/interface/wifi/easymesh
set enabled=yes role=agent bridge=bridge dpp-onboarding=no
```

EasyMesh adds its Wi-Fi interfaces to the bridge specified in the `bridge` setting. Do not set `bhaul-configuration` or `fhaul-configurations` on the agent. The controller provides them during onboarding.

## Onboarding

### Wired backhaul

Connect an agent Ethernet port to the controller's LAN. WPS is not required. When the agent is in the same Layer 2 network, the controller discovers it and applies the configuration automatically.

### Wireless backhaul

A wireless backhaul is used when an agent has no Ethernet connection to the controller. The controller provides a backhaul network through its `bhaul-configuration`. A backhaul AP broadcasts it, and the agent's backhaul station connects to it using the credentials received during onboarding.

Onboard the agent with WPS push-button:

```ros
/interface/wifi/easymesh/wps-push-button
```

Run the command on the controller first, then on the agent. The agent connects to the controller's backhaul network and receives the backhaul and fronthaul configuration.

After onboarding, `agent-state` will change to `wifi-backhaul-connected`:

```ros
[admin@hAP] > /interface/wifi/easymesh/print
                     enabled: yes
                        role: agent
                      bridge: bridge
                  bhaul-ssid: em_bh
            bhaul-passphrase: backhaul-password
  bhaul-authentication-types: wpa2-psk
            bhaul-encryption: ccmp
                              gcmp
              dpp-onboarding: no
                 agent-state: wifi-backhaul-connected
```

:::tip
Keep the agent close to the controller during onboarding. Move it to its final location after the backhaul link is established.
:::

## Verify the setup

Run the following commands to see the EasyMesh state:

```ros
/interface/wifi/easymesh/print
/interface/wifi/easymesh/topology/print
/interface/wifi/easymesh/bss/print
/interface/wifi/easymesh/sta/print
```

- `print` shows the global EasyMesh settings, the agent state, and the topology tree with the controller, agents, radios, and BSSes.
- `topology/print` lists connected agents by their AL MAC addresses.
- `bss/print` lists all BSSes with their fronthaul/backhaul role, channel, utilization, and client count.
- `sta/print` lists connected clients and backhaul stations.

:::info
The AL MAC is the IEEE 1905.1 abstraction layer MAC address. EasyMesh uses it as the device identity in control messages and topology, independent of the interface that carries the traffic.
:::

The `print` output shows the global settings, the agent state, and the topology tree:

```ros
[admin@cAP] > /interface/wifi/easymesh/print
               enabled: yes
                  role: controller-and-agent
                bridge: bridge
   bhaul-configuration: em_bh
  fhaul-configurations: em_fh
        dpp-onboarding: no
           agent-state: wired-backhaul-connected
               network: CONTROLLER: AL-MAC: 48:XX:XX:XX:XX:74
                            ETHERNET: mac: 48:XX:XX:XX:XX:74
                                AGENT: AL-MAC: D0:XX:XX:XX:XX:D3 via mac: D0:XX:XX:XX:XX:D3
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D3
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D4
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D5
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D6
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D7
                                    RADIO: mac: D0:XX:XX:XX:XX:D9
                                        bVAP[0]: bssid: D0:XX:XX:XX:XX:D9, ssid: em_bh, bw: 160 MHz, ccfi1: 50
                                        fVAP[1]: bssid: D2:XX:XX:XX:XX:DA, ssid: em_fh, bw: 160 MHz, ccfi1: 50
                                    RADIO: mac: D0:XX:XX:XX:XX:D8
                                        bVAP[0]: bssid: D2:XX:XX:XX:XX:D8, ssid: em_bh, bw: 40 MHz, ccfi1: 11
                                        fVAP[1]: bssid: D2:XX:XX:XX:XX:D9, ssid: em_fh, bw: 40 MHz, ccfi1: 11
                            ETHERNET: mac: 48:XX:XX:XX:XX:75
                            RADIO: mac: 48:XX:XX:XX:XX:77
                                bVAP[0]: bssid: 48:XX:XX:XX:XX:77, ssid: em_bh, bw: 40 MHz, ccfi1: 5
                                fVAP[1]: bssid: 4A:XX:XX:XX:XX:77, ssid: em_fh, bw: 40 MHz, ccfi1: 5
                            RADIO: mac: 48:XX:XX:XX:XX:76
                                bVAP[0]: bssid: 48:XX:XX:XX:XX:76, ssid: em_bh, bw: 80 MHz, ccfi1: 58
                                fVAP[1]: bssid: 4A:XX:XX:XX:XX:76, ssid: em_fh, bw: 80 MHz, ccfi1: 58
```

The topology table lists connected agents:

```ros
[admin@cAP] > /interface/wifi/easymesh/topology/print
Columns: ALMAC
#  ALMAC
0  D0:XX:XX:XX:XX:D3
```

The BSS table lists the fronthaul and backhaul BSSes on the controller and the agent:

```ros
[admin@cAP] > /interface/wifi/easymesh/bss/print
Flags: A - ACTIVE
Columns: ALMAC, RADIO-MAC, BSSID, SSID, FRONTHAUL, BACKHAUL, UTILIZATION, BRANCH-UTILIZATION, STA-COUNT, OPCLASS, PRIMARY-CHAN, IEEE-CHAN
#   ALMAC              RADIO-MAC          BSSID              SSID   FRONTHAUL  BACKHAUL  UTI  BRA  S  OPCLASS  PRI  IEEE-CHAN
0 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:76  48:XX:XX:XX:XX:76  em_bh  no         yes       0%   0%   0  128      136  138
1 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:77  48:XX:XX:XX:XX:77  em_bh  no         yes       33%  33%  1  84       5    5
2 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:76  4A:XX:XX:XX:XX:76  em_fh  yes        no        0%   0%   1  128      136  138
3 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:77  4A:XX:XX:XX:XX:77  em_fh  yes        no        33%  33%  0  84       5    5
4 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D9  D0:XX:XX:XX:XX:D9  em_bh  no         yes       0%   33%  0  129      64   50
5 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D8  D2:XX:XX:XX:XX:D8  em_bh  no         yes       0%   33%  0  84       5    5
6 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D8  D2:XX:XX:XX:XX:D9  em_fh  yes        no        0%   33%  0  84       5    5
7 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D9  D2:XX:XX:XX:XX:DA  em_fh  yes        no        0%   33%  0  129      64   50
```

The STA table lists connected clients and backhaul stations:

```ros
[admin@cAP] > /interface/wifi/easymesh/sta/print
Columns: BSSID, SSID, ALMAC, MAC-ADDRESS, UPTIME, LAST-ACTIVITY, SIGNAL, BACKHAUL
#  BSSID              SSID   ALMAC              MAC-ADDRESS        UPTIME  LAST-ACTIVITY  SIGNAL  BACKHAUL
0  4A:XX:XX:XX:XX:76  em_fh  48:XX:XX:XX:XX:74  3C:XX:XX:XX:XX:AD  6s      1s510ms        -32     no
1  48:XX:XX:XX:XX:77  em_bh  48:XX:XX:XX:XX:74  D0:XX:XX:XX:XX:D8  16s     1s820ms        -22     yes
```

## Troubleshooting

- If the agent does not appear in `topology`, check that both devices are in the same Layer 2 network, that the agent's bridge includes the correct ports, and that `enabled=yes`, `role=agent`, and `configuration.manager=easymesh` are set.
- If the wireless backhaul does not come up, run the WPS push-button command on both devices again. Start with the controller.
- If clients do not see the network, check that the controller has the correct `fhaul-configurations` value and that the agent has completed onboarding.
- A radio can use only one manager. Do not combine EasyMesh and CAPsMAN on the same interface.

## Notes

:::note

- Use one controller per EasyMesh network.
- All controllers and agents must be in the same Layer 2 network.
- Cross-vendor interoperability requires certified EasyMesh devices. Test the specific controller and agent combination before deployment.

:::
