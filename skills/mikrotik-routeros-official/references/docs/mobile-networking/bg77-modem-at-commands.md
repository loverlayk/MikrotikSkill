# BG77 modem AT commands

> This short guide will help you understand how to troubleshoot issues/problems with the CAT-M/NB-IoT connection. A lot of information about the connection can be obtained using modem "AT" commands. By definition, "AT"...

#

# Overview

This short guide will help you understand how to troubleshoot issues/problems with the CAT-M/NB-IoT connection. A lot of information about the connection can be obtained using modem "AT" commands. By definition, "AT" means 'attention'. Each command string is prefixed with "AT", and a number of discrete commands can be concatenated after the "AT".

Please check the examples below to better understand how to initiate those commands and what information can be obtained using them.

:::info
 Mobile network is managed by the ISP. If there are any issues with the connection, we advise contacting ISP beforehand and making sure that they support/allow the connection or the setting in the first place. If you decide to change the configuration with AT commands (without consulting with the ISP), you can do it at your own risk.
:::

## Initiating AT Commands

### Option A

To send the command, you must use the CLI.

Open the terminal and type in the following:

```ros
[admin@MikroTik] > system serial-terminal port=modem channel=2
```

Pay attention to the port and channel used. Select the port and channel that is used by the PPP-OUT interface. In our example, the port is "modem" and the data channel is "2".

Once the command is initiated it should show the following output where you can now type in the AT commands:

```ros
[admin@MikroTik] > system serial-terminal port=modem channel=2

[Ctrl-A is the prefix key]

at+cpin?
+CPIN: READY

OK 
```

In the example above, AT command "at+cpin?" is used and the answer "+CPIN: READY" is received.

### Option B

The second way to send AT commands is through the ppp-client interface:

```ros
[admin@MikroTik] > interface ppp-client at-chat input="AT+CPIN\?"
number: 0
  output: +CPIN: READY
```

You can get the same result as with **Option A**.

## AT Commands

### at

Simple ***at*** command checks communication between the module (device) and application.

```ros
[Ctrl-A is the prefix key]

at

OK 
```

When "OK" is returned, it means the module successfully responded.

### at+cpin?

This command is used to check the status of the SIM card.

```ros
[Ctrl-A is the prefix key]

at+cpin?
+CPIN: READY

OK 
```

Status "+CPIN: READY" means that the SIM card is installed properly.

If the SIM PIN is used, you should get the answer "+CPIN: SIM PIN" → in this case, you can unlock it via the command ***at+cpin="xxxx"***, where ***xxxx*** is the pin code.

If you get the response "+CME ERROR: SIM not inserted" → double-check that the SIM card is properly installed in the SIM slot.

### at+cfun?

The "CFUN" command is used to check the functional mode. There could be different responses to this command.

```ros
[Ctrl-A is the prefix key]   

at+cfun?
+CFUN: 1

OK
```

When the status is "+CFUN: 1" it means that the device is set to full functionality. It is suggested to use this mode.

Among many other responses, for example, you can get "+CFUN: 4" which means that the device is set to flight mode where Tx, Rx, LTE, and GNSS services, are disabled.

You can manually set the mode to full functionality with the command ***at+cfun=1***.

### at+cops?

The **at+cops?** command is used to check the current network connection.

```ros
[Ctrl-A is the prefix key]      

at+cops?
+cops: 0,0,"LMT",8

OK
```

Using the example above as the reference, we can see that we got the response "0,0,"LMT",8".

The first value in the response dictates whether the "automatic" or "manual" mode is used. When ISP connection is set to be "automatic" the value will show "0". When ISP connection is set to be "manual" the value will show "1".

The second value in the response represents ISP's name format. If it is "0", it means the ISP name is in "long format alphanumeric". If it is "1", it means the ISP name is in "short format alphanumeric".

The third part of the response is the ISP name itself.

The fourth part of the response represents the technology used. "8" stands for eMTC (CAT-M) and "9" for NB-IoT.

### at+cops=?

The **at+cops=?** is used to get the list of all available ISPs. This command can take some time (up ~ 1 min) to display the results.

```ros
[Ctrl-A is the prefix key]      

at+cops=?
+cops: (1,"LMT","LMT","24701",9),(2,"LMT","LMT","24701",8),,(0,1,2,3,4),(0,1,2)

OK
```

You can manually set up the ISP that you wish to connect to via the command ***at+cops=mode,format,"provider"***, where ***mode*** is the mode used (0→ automatic network selection; 1→ manual network selection), **format** is the ISP name format (0→ long alphanumeric format; 1→ short alphanumeric format; 2→ numeric format), and "***provider***" is the ISP name (in the format that was selected). For example, to manually select the network from the list, use the command ***at+cops=1,1,"LMT"***.

To select ISP automatically, use the command ***at+cops=0***.

### at+creg?

***at+creg?*** command is used to check the network's registration status.

```ros
[Ctrl-A is the prefix key]              

at+creg?
+CREG: 0,1

OK
```

The first value shows whether the network registration unsolicited result code is enabled or disabled (0→ disabled, 1→ enabled; 2→ enabled + location information). The second value shows circuit mode registration status (0→ not registered/the device is not searching for an operator to register to; 1→ registered/home network; 2→ not registered, but trying to search for an operator to register to; 3→ registration was denied; 4→ unknown; 5→ registered and roaming).

If you have more than 2 values returned, it means that network registration and location information unsolicited result code is enabled. The second value will show a two-byte location area code in hexadecimal format, the third value will show four-byte GERANE/E-UTRAN cell ID in hexadecimal format and the last value will show access technology of the serving cell ("8" for CAT-M and "9" for NB-IoT).

### at+csq

The ***at+csq*** command returns received signal strength indication (RSSI) and channel bit error (BER) values. This command will return proper values only when the registration in the network is complete.

```ros
[Ctrl-A is the prefix key]           

at+csq
+csq: 25,99

OK
```

The first value is RSSI (dBm):

| Value | RSSI |
| --- | --- |
| 0 | -113 dBm or less |
| 1 | -111 dBm |
| 2-30 | -109 to -53 dBm |
| 31 | -51 dBm or greater |
| 99 | not know/not detectable (network not found) |

The second value is BER (%):

| Value | BER |
| --- | --- |
| 0 | &lt; 0,2 % |
| 1 | 0,2 % &lt; 0,4 % |
| 2 | 0,4 % &lt; 0,8 % |
| 3 | 0,8 % &lt; 1,6 % |
| 4 | 1,6 % &lt; 3,2 % |
| 5 | 3,2 % &lt; 6,4 % |
| 6 | 6,4 % &lt; 12,8 % |
| 7 | 12,8 % &lt; |
| 99 | not known/not detectable |

As per the example/output "***+csq: 25,99***", the result translates to RSSI~63 dBm and BER parameter not detectable.

### at+qnwinfo

The command returns information about access technology, ISP and band selected. This command will return proper information only when the registration in the network is complete.

```ros
[Ctrl-A is the prefix key]              

at+qnwinfo
+QNWINFO: "eMTC","24701","LTE BAND 20",6300

OK
```

As per the example above, you can see that the current module uses "eMTC" (CAT-M), ISP is "24701" (numeric format, which stands for "LMT"), LTE Band 20, and channel ID "6300".

### at+qcsq

The command **at+qcsq** returns information about the signal strength of the current ISP connection and the technology used.

```ros
[Ctrl-A is the prefix key]                 

at+qcsq
+QCSQ: "eMTC",-62,-87,111,-12

OK
```

The first parameter returned is "eMTC" which shows the technology used by the module (CAT-M). If the network can not be determined (is uncertain) →  "NOSERVICE" will be returned.

The rest of the parameters show the signal strength of the connection.

When the technology is recognized as "NBIoT" or "eMTC" (CAT-M):

- the first numeric value displays received signal strength (LTE RSSI);
- the second value displays the reference signal received power (LTE RSRP);
- the third value displays the signal to interference plus noise ratio (LTE SINR) →  the value is displayed as the logarithmical value of SINR and the value is 1/5th of a dB (result can be in between 0-250 range, which translates to -20 dB to +30 dB range);
- the fourth value displays the reference signal received quality (LTE RSRQ).
As per the example above, RSSI=-62 dBm, RSRP=-87 dBm, SINR=111(111/5-20)~2 dB, RSRQ=-12 dB.

### at+qcfg="iotopmode"?

The command is used to check which technology is used to connect to ISP. It is possible for the modem to work only in CAT-M mode, only in NB-IoT mode, or in both.

```ros
[Ctrl-A is the prefix key]   

at+qcfg="iotopmode"?
+QCFG: "iotopmode",2

OK
```

You can lock the SIM card to work only in the specific mode with the command ***at+qcfg="iotopmode"****,****mode***,***effect***, where*** mode*** is the mode (0→ only CAT-M; 1→ only NB-IoT; 2→ both), and ***effect*** is when to take effect (0→ to take effect after reboot; 1→ to take effect immediately).

To speed up network searching, it is suggested to execute the command ***at+cfun=0*** (to turn off the radio) and then use the described command. After that, execute ***at+cfun=1,1*** (to turn on the radio back and reset the module to take effect).

### at+qcfg="band"?

This command is used to check which bands/frequencies are currently accepted.

```ros
[Ctrl-A is the prefix key]   

at+qcfg="band"?
+QCFG: "band",0x0,0x100002000000000f0e189f,0x10004200000000090e189f

OK
```

The first value in the "qcfg" response shows a hexadecimal value that specifies the **GSM frequency band**. This value is not relevant for the Quectel BG77 module. This value can be ignored.

The second hexadecimal value specifies **CAT-M frequency bands** (which is 0x100002000000000f0e189f). If it is set to 0,  it means not to change the frequency band. If, for example, it is 0x15, it means → 0x01(LTE Band 1)+0x04(LTE Band 3)+0x10(LTE Band 5).

| Value | Band |
| --- | --- |
| 0 | No change |
| 0x1 | LTE Band 1 |
| 0x2 | LTE Band 2 |
| 0x4 | LTE Band 3 |
| 0x8 | LTE Band 4 |
| 0x10 | LTE Band 5 |
| 0x80 | LTE Band 8 |
| 0x800 | LTE Band 12 |
| 0x1000 | LTE Band 13 |
| 0x20000 | LTE Band 18 |
| 0x40000 | LTE Band 19 |
| 0x80000 | LTE Band 20 |
| 0x1000000 | LTE Band 25 |
| 0x2000000 | LTE Band 26 |
| 0x4000000 | LTE Band 27 |
| 0x8000000 | LTE Band 28 |
| 0x20000000000000000 | LTE Band 66 |
| 0x1000000000000000000000 | LTE Band 85 |
| 0x100002000000000F0E189F | All of the supported bands mentioned above |

The last hexadecimal value specifies **NB-IoT frequency bands** (which is 0x10004200000000090e189f). If it is set to 0,  it means not to change the frequency band. If, for example, it is 0x15, it means → 0x01(LTE Band 1)+0x04(LTE Band 3)+0x10(LTE Band 5).

| Value | Band |
| --- | --- |
| 0 | No change |
| 0x1 | LTE Band 1 |
| 0x2 | LTE Band 2 |
| 0x4 | LTE Band 3 |
| 0x8 | LTE Band 4 |
| 0x10 | LTE Band 5 |
| 0x80 | LTE Band 8 |
| 0x800 | LTE Band 12 |
| 0x1000 | LTE Band 13 |
| 0x20000 | LTE Band 18 |
| 0x40000 | LTE Band 19 |
| 0x80000 | LTE Band 20 |
| 0x1000000 | LTE Band 25 |
| 0x8000000 | LTE Band 28 |
| 0x20000000000000000 | LTE Band 66 |
| 0x400000000000000000 | LTE Band 71 |
| 0x1000000000000000000000 | LTE Band 85 |
| 0x10004200000000090E189F | All of the supported bands mentioned above |

You can change the band with the command ***at+qcfg="band",GSM_band,CAT_M_band,NB_IoT_band,effect***, where ***GSM_band*** is GSM frequency band (can be left 0x0), ***CAT_M_band*** is the CAT-M frequency band, ***NB_IoT_band*** is the NB-IoT band and ***effect*** is whether to take effect immediately (1) or to take effect after module reboots (0).

To setup module the way so that all bands are supported, use the command:

```ros
[Ctrl-A is the prefix key]     

at+qcfg="band",0x0,0x100002000000000f0e189f,0x10004200000000090e189f,1

OK
```

To speed up network searching, it is suggested to execute the command ***at+cfun=0*** (to turn off the radio) and then use the described command. After that, execute ***at+cfun=1,1*** (to turn on the radio back and reset the module to take effect).

### at+qgpscfg="priority",(0-1)

It is important to understand that data transfer over CAT-M/NB-IoT and GNSS can not work simultaneously (WWAN and GNSS Rx chains in the BG77 module share certain hardware blocks, meaning the module does not support concurrent operation of WWAN and GNSS.). That is why the ***at+qgpscfg="priority",(0-1)*** command was introduced.

It is possible to change the priority with the commands:

```ros
[Ctrl-A is the prefix key]    

at+qgpscfg="priority",0

OK

at+qgpscfg="priority",1

OK
```

***at+qgpscfg="priority",0*** command sets the **highest priority for GNSS**.

***at+qgpscfg="priority",1*** command sets the **highest priority for LTE (WWAN)**.

When the device is in the **LTE (WWAN) priority mode**, the GNSS positioning request can successfully go through only when the RRC is released (Radio Resource Control protocol has many functions, but mainly is responsible for connection establishment and its release function) and LTE (WWAN) enters an idle sleep mode. Both LTE (WWAN) and GNSS can co-exist in **LTE (WWAN) priority mode** only under the condition that eDRX is supported and not blocked by the ISP. If the network connection gets established (RRC is in the connected state) and the data begins flowing to the server → GNSS will be deferred until the data transmission is over and RCC is released. In case the eDRX is supported and the module enters this mode (data transmission is over) → GNSS coordinates will be sent. Once the data begins flowing to the server again, GNSS will be deferred until the device enters eDRX mode again.

When the device is in the **GNSS priority mode**, the GNSS positioning request succeeds in all WWAN states. If the device is in the RCC-connected state → it will release the RCC connection and initiates the GNSS session. After that, if there is WWAN data to be sent → RCC connection will be initiated again.
