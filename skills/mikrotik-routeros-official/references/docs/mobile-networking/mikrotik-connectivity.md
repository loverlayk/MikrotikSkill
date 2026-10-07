# MikroTik Connectivity

> MikroTik Connectivity introduces an eSIM solution for seamless device connectivity without physical SIM swaps, featuring activation steps through the MikroTik account portal and RouterOS CLI/WinBox interfaces.

# MikroTik Connectivity

### Summary

MikroTik Connectivity is our new built-in eSIM solution that ensures your devices stay connected anywhere, without the need for physical SIM swaps or external activation steps. For additional info visit [https://mikrotik.com/connectivity](https://mikrotik.com/connectivity)

### Activation example

1) Sign in to your MikroTik account, select "My devices".

![](img/esim_1.png)

1) Enter your device’s Serial Number – the system will detect. Choose the region and then press "Add to list".

![](img/esim_2.png)

1) Choose a data plan and payment method that suits your needs. Then add it to the cart.

![](img/esim_3.png)

1) Proceed with payment in the cart.

![](img/esim_4.png)

1) Once payment is done go back to "My devices" and you will see that the subscription is now Active.

![](img/esim_5.png)

:::info
MikroTik eSIM profiles are preloaded, so there’s no need for an internet connection during activation. The activation itself usually takes a few minutes, but in some cases it can take even a few hours.
:::

1) In RouterOS check that your device is set to use "esim" and the correct profile is active.  
  
CLI:

```
[admin@EG25-G&KNe] > /interface/lte/settings/print 
                 mode: auto    
         esim-channel: auto    
        firmware-path: firmware
  link-recovery-timer: 120     
             sim-slot: sim      
[admin@EG25-G&KNe] > /interface/lte/settings/set sim-slot=esim      
[admin@EG25-G&KNe] > /interface/lte/esim/print
Flags: A - ACTIVE
Columns: INTERFACE, NAME, SPN, ICCID
#   INTERFACE  NAME       SPN                      ICCID
0 A lte1       Profile 1  MikroTik  89358152000001049461
1   lte1       Profile 4  MikroTik  89358152000001349465
```

In WinBox:

 Go to Interfaces > LTE > Modem to select the esim SIM slot:

![](img/esim_6.png)

Go to Interfaces > LTE > eSIM to check which is the active esim profile:

![](img/esim_7.png)

If you need to change the Active profile, right click on the profile and select "Activate":

![](img/esim_8.png)

#### [Video Tutorial: Our official YT channel, MikroTips series](https://www.youtube.com/watch?v=2YxHL9A4Ys0)

### FAQ

<details>
<summary>Is the IP address assigned to my device a public IP address?</summary>

No, the IP address is private. You can configure BTH to get access to your device remotely: [Back To Home](../network-management/cloud/back-to-home)

</details>

<details>
<summary>Is IPv6 also supported?</summary>

Only IPv4 is supported.

</details>

<details>
<summary>What Access Point Name (APN) should I configure?</summary>

You can use the "use-network-apn=yes" option, or set the APN manually to "[mikrotik.net](http://mikrotik.net "http://mikrotik.net/")"

</details>

<details>
<summary>Why is the latency higher when using MikroTik Connectivity compared to using my local operator’s SIM?</summary>

MikroTik Connectivity works as a roaming service. It routes data through a set pool of PDN gateways that can be located in another country. The extra distance and additional network hop increase round‑trip time, so the latency appears higher than when you use local operators' service.

</details>

<details>
<summary>Why is the download/upload speed lower when using MikroTik Connectivity compared to using my local operator’s SIM?</summary>

MikroTik Connectivity works as a roaming service. It routes data through a set pool of PDN gateways that can be located in another country. The extra distance and additional network hop increase round‑trip time so the latency increases. Because of this higher latency, TCP performance is directly affected. TCP relies on acknowledgements to increase its congestion window and scale throughput. When the round-trip time becomes longer, acknowledgements take more time to return, the congestion window grows more slowly, and the achievable throughput decreases.

</details>

<details>
<summary>How do I pause, upgrade, or cancel my MikroTik Connectivity subscription?</summary>

To manage your eSIM subscription plan, log into your **mikrotik.com** account and navigate to the **"My devices"** section. Search for your device's serial number and click on it.

From there, you have two ways to manage your plan:

* **Via the "Plan" tab:** Here you will find the option to **"Unsubscribe"** or upgrade by choosing a different data plan.
* **Via the "Details" tab:** Go to the **"Status"** field, which allows you to switch between **Active**, **Pause data transfer**, or **Cancel subscription**.

</details>
