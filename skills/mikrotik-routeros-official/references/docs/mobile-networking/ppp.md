# PPP

> PPP in RouterOS enables point-to-point protocol communication for transporting multi-protocol datagrams, featuring LCP and NCP components. It supports PPP client and server configurations with examples like...

# PPP

## Overview

The Point-to-Point Protocol (PPP) provides a standard method for transporting multi-protocol datagrams over point-to-point links. PPP in RouterOS is based on [RFC 1661 standard.](https://tools.ietf.org/html/rfc1661)

## Introduction

The basic purpose of PPP at this point is to transport Layer-3 packets across a Data Link layer point-to-point link.  Packets between both peers are assumed to be delivered in order.

PPP is comprised of three main components:

1. A method for encapsulating multi-protocol datagrams.
2. A Link Control Protocol (LCP) for establishing, configuring, and testing the data-link connection.
3. A family of Network Control Protocols (NCPs) for establishing and configuring different network-layer protocols.

For detailed PPP packet processing in RouterOS, you can see in the [Packet Flow Diagram](../firewall-and-quality-of-service/packet-flow-in-routeros.md).

### PPP Client

**Sub-menu:** `/interface/ppp-client`

### PPP Client example

This is an example of how to add a client using an exposed serial port from an LTE modem.

```ros
/interface/ppp-client/add apn=yourapn dial-on-demand=no disabled=no port=usb2
```

The dial-on-demand should be set to 'no' for a continuous connection.

### PPP Server

**Sub-menu:** `/interface/ppp-server`

## KNOT RB924i-2nD-BT5&BG77

If you see the message “*A newer version of modem firmware is available!*” and you want to upgrade the firmware of your BG77 modem, use this command:

```routeros
/interface/ppp-client/firmware-upgrade [find] upgrade=yes
```
