# CMR-Client

> The CMR-client is the device-side component that connects to a CMR server and is managed centrally from it.

# CMR-Client

A CMR-client is a RouterOS device that connects to a CMR server and is managed centrally from it. The CMR-client functionality is included in the main RouterOS package.

:::warning
CMR-client is not supported on devices with the **smips** and **powerpc** architectures.
:::

The [`CMR-Client CLI Reference`](../../cli-reference/cmr/client) provides detailed descriptions for every parameter and command in the `/cmr/client` menu.

## Enable the CMR client

The client must be able to reach the CMR server on TCP port `54321`. Allow connections to this port in the server's firewall and through any firewalls between the client and the server.

Enable the client and specify the CMR server it should connect to:

```ros
[admin@MikroTik] > /cmr/client set enabled=yes controller-addresses=192.168.88.1 pairing-requirement=password
```

`controller-addresses` is not obligatory, but it is recommended to set it when you want the client to connect to a specific CMR server, or the client is unable to discover the server automatically through neighbor discovery or DNS (the [How it works](./#how-it-works) section of the CMR guide describes both).

The client contacts the server and reports its pairing status. The current state and the server it is connected to are shown in the read-only parameters `status`, `controller-address`, and `controller-identity`:

```ros
[admin@MikroTik] > /cmr/client print
  enabled: yes
  pairing-requirement: password
  controller-addresses: 192.168.88.1
  status: paired,connected
  controller-identity: CMR-1
  controller-address: 192.168.88.1
```

The client logs each change of its `status` with the `cmr` topic, for example `client status changed: paired,connected`. When the connection to the server drops, for example while CMR restarts on the server, the client reconnects with its existing pairing.

## Pair the client to the server

Pairing links the client with a CMR server. Running the `pair` command locally always approves the pairing from the client side, regardless of the client's configured `pairing-requirement`:

```ros
[admin@MikroTik] > /cmr/client/pair username=admin password=secret
Columns: ADDRESS, STATUS
ADDRESS         STATUS
192.168.88.1    paired
```

The client pairs with the server at `controller-addresses`. A username and password are only needed to satisfy the server's requirement when the server is configured with `pairing-requirement=password`. They are the credentials of a RouterOS user on the server; CMR has no separate pairing password. By giving them, the client satisfies the server's requirement remotely.

The client also has its own `pairing-requirement` in the `/cmr/client` menu, which defines what the server must do before the client accepts the pairing. The client supports `none` and `password`, and the default is `password`. The CMR server also supports `confirm`. The [Pairing](./#pairing) section explains how the requirements on both devices combine.

## Disconnect the client

To forget the pairing and disconnect the client from the server:

```ros
[admin@MikroTik] > /cmr/client/forget
```

Disabling the client (`/cmr/client set enabled=no`) removes the configuration that CMR provisioned on the device. Enabling it again reconnects the client with its existing pairing.

## Troubleshooting

The `status` and `pairing-status` values in `/cmr/client print` show where the connection or the pairing stops. `pairing-status` lists the server address, the server's pairing state (`cmr:`), and the client's own pairing state (`device:`).

- `status: searching` - the client has not found a CMR server. Set `controller-addresses` to the server's IP address, or check that the server is reachable from the client on TCP port `54321` and that firewalls allow the connection.
- `status: waiting-for-pairing,connected` with `pairing-status: 192.168.88.1: cmr:waiting confirmation, device:ok` - the client accepted the pairing and is connected, and the server waits for local approval because its `pairing-requirement` is `confirm`. On the server, the device is listed in `/cmr/device` with the **P** (pending) flag. Run [`/cmr/device/pair`](../../cli-reference/cmr/device/pair) on the server for that device.
- `status: paired,disconnected`, and the device is not listed on the server - the client keeps a pairing with a server it can no longer reach, for example an earlier CMR server. As a workaround, forget the pairing and enable the client again, so that it pairs with the server in `controller-addresses`:

  ```ros
  [admin@MikroTik] > /cmr/client/forget
  [admin@MikroTik] > /cmr/client set enabled=yes controller-addresses=192.168.88.1
  ```

On the CMR server itself, `/cmr/client print` shows the comment "settings ignored because used by local controller". The server manages itself through its local controller, and the `/cmr/client` settings on the server have no effect.
