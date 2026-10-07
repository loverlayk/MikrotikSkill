# Ports

> This page documents MikroTik RouterOS port configuration options, covering serial and USB ports for initial setup, 3G modem connections, remote access via RFC 2217, and detailed port properties like baud rate, flow...

# Ports

## Summary

The router provides multiple options for utilizing its ports. The most common use is the serial port, which is used for the initial RouterOS configuration after installation. By default, serial0 is used by the serial terminal.

Serial and USB ports can also be used to:

- Connect 3G modems.
- Connect to another device through a serial cable.
- Access the device connected to a serial cable remotely.

## General

**Sub-menu:** `/port`

This menu displays all available serial and USB ports on the router and allows you to configure port parameters such as baud-rate, flow-control, and other settings.

The following example shows the default port configuration on an LtAP device:

```ros
[admin@LtAP] > /port/print                 
Columns: DEVICE, NAME, CHANNELS, USED-BY, BAUD-RATE
# DEVICE  NAME     CHANNELS  USED-BY                                     BAUD-RATE
0         serial0         1  Serial Console(#0)                          auto     
1         gps             1  GPS(#0)                                     115200   
```

:::warning
The port list is maintained automatically by RouterOS.

:::

## Properties

| Property | Description |
| :-- | :-- |
| **baud-rate** (*integer \| auto*; Default: **auto**) | Baud rate (speed) used by the port. If set to **auto**, then RouterOS tries to detect baud rate automatically. |
| **data-bits** (*7 \| 8*; Default: ) | The number of data bits in each character.7 - true ASCII8 - any data (matches the size of a byte) |
| **dtr** (*on \| off*; Default: ) | Whether to enable RS-232 DTR signal circuit used by flow control. |
| **flow-control** (*hardware \| none \| xon-xoff*; Default: ) | Method of flow control to pause and resume the transmission of data. |
| **name** (*string*; Default: ) | Name of the port. |
| **parity** (*even \| none \| odd*; Default: ) | Error detection method. If enabled, an extra bit is sent to detect the communication errors. In most cases parity is set to **none** and errors are handled by the communication protocol. |
| **rts** (*on \| off*; Default: ) | Whether to enable RS-232 RTS signal circuit used by flow control. |
| **stop-bits** (*1 \| 2*; Default: ) | Stop bits sent after each character. Electronic devices usually use 1 stop bit. |

### Read-only properties

| Property | Description |
| :-- | :-- |
| **channels** (*integer*) | Number of channels supported by the port. |
| **inactive** (*yes \| no*) | Shows current port state, **inactive=yes** - device to which the port was previously connected, but currently is not present |
| **line-state** () |  |
| **used-by** (*string*) | Shows who is currently using port and channel (#).  For example, by default **Serial0** is used by serial-console. |

## Remote Access

**Sub-menu:** `/port/remote-access`

The remote access feature allows you to connect to a serial device that communicates via a COM port and is located behind the router. Using RFC 2217, RouterOS can transfer data to and from a serial device over a TCP connection.

Enabling remote access on RouterOS is straightforward:

```ros
/port/remote-access/add port=serial0 protocol=rfc2217 tcp-port=9999
```

:::warning
By default, serial0 is used by the serial terminal. The port must be released before it can be used by remote-access or other services.

:::

## Properties

| Property | Description |
| :-- | :-- |
| **allowed-addresses** (*IP address range*; Default: **0.0.0.0/0**) | Range of IP addresses allowed to access port remotely. |
| **channel** (*integer [0..4294967295]*; Default: **0**) | Port channel that will be used. If the port has only one channel then the channel number should always be **0**. |
| **disabled** (*yes \| no*; Default: **no**) |  |
| **local-address** (*IP address*; Default: ) | IP address used as source address. |
| **log-file** (*string*; Default: **""**) | Name of the file, where communication will be logged. By default logging is disabled. |
| **port** (*string*; Default: ) | Name of the port from the Port list. |
| **protocol** (*raw \| rfc2217*; Default: **rfc2217**) | RFC 2217 defines a protocol to transfer data from/to a serial device over TCP. If set to **raw**, then data is sent to serial as is. |
| **tcp-port** (*integer [0..65535]*; Default: **0**) | TCP port on which to listen for incoming connections. |

## Read-only properties

| Property | Description |
| :-- | :-- |
| **active** (*yes \| no*) | Whether remote access is active and ready to accept a connection. |
| **busy** (*yes \| no*) | Whether the port is currently busy. |
| **inactive** (*yes \| no*) |  |
| **logging-active** (*yes \| no*) | Whether logging to file is currently running |
| **remote-address** (*IP address*) | IP address of the remote location that is currently connected. |
