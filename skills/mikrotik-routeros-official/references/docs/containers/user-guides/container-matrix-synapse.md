# Container - Matrix (Synapse)

> Run a Synapse Matrix server with a PostgreSQL database in RouterOS containers, register a user, and add a Discord bridge.

# Container - Matrix (Synapse)

## Introduction

[Matrix](https://matrix.org/) is a decentralized communication protocol. Each Matrix server operates independently, with its own users, rules and policies. With containers, you can host your own Matrix server on a RouterOS device and keep full control over your communication.

- **Federation** - Matrix servers connect to each other, so that users on different servers can communicate securely without a central authority.
- **Bridges** - a bridge relays messages between Matrix and another chat platform, such as WhatsApp, Discord, Signal or Telegram. With bridges, you can use one Matrix client, such as [Element](https://element.io/), to talk to users on several platforms.

This guide sets up [Synapse](https://element-hq.github.io/synapse/latest/), one of several Matrix servers, with a PostgreSQL database, and then adds a Discord bridge. Each of them runs in its own container.

## Summary

Read the [container](../) guide first, especially the [disclaimer](../#disclaimer) and the [requirements](../#requirements): the `container` package must be installed and containers enabled in device-mode.

All containers in this guide use the veth interface `veth1` (`172.17.0.2/24`) with NAT from the container guide's [Bridge with NAT](../#bridge-with-nat) example; create it first. Containers on the same veth interface share its address, so each service listens on its own port:

| Container | Port |
| --- | --- |
| `postgresql_synapse` | 5433 |
| `synapse` | 8008 |
| `postgresql_discord` | 5434 |
| `synapse_discord` | 29334 |

The images are downloaded from their registries (see [Registry](../#registry)) and extracted to an external disk, `disk1`; set the directory for the downloads:

```routeros
/container/config/set tmpdir=disk1/pull
```

:::warning

The passwords in this guide are examples; use your own long random passwords. Consult the [Synapse documentation](https://element-hq.github.io/synapse/latest/) for the latest configuration options and best practices, as configuration procedures can change with newer versions.

:::

## Synapse server

### PostgreSQL database

Create the environment variables for the PostgreSQL container:

```routeros
/container/envs/add list=postgres_synapse_envs key=POSTGRES_DB value="synapse"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_PASSWORD value="Example-db-pass-1"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_USER value="synapse_user"
/container/envs/add list=postgres_synapse_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
/container/envs/add list=postgres_synapse_envs key=PGPORT value=5433
```

Synapse needs a database with `UTF8` encoding and the `C` collation, which `POSTGRES_INITDB_ARGS` sets when the database is created. `PGPORT` moves PostgreSQL to port 5433, so that it does not clash with other containers on `veth1`, such as the PostgreSQL example in the container guide (port 5432).

Create a mount, so that the database is kept on the disk:

```routeros
/container/mounts/add list=synapse_postgres_data src=disk1/synapse-postgres-data dst=/var/lib/postgresql/data
```

Add the PostgreSQL container:

```routeros
/container/add remote-image=postgres:17.2-alpine interface=veth1 \
    root-dir=disk1/postgres-17.2-synapse mountlists=synapse_postgres_data \
    envlists=postgres_synapse_envs logging=yes name=postgresql_synapse
```

### Synapse container

Create the environment variables for the Synapse container:

```routeros
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_DIR value="/data"
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_PATH value="/data/homeserver.yaml"
/container/envs/add list=synapse_envs key=SYNAPSE_SERVER_NAME value="matrix.example.com"
/container/envs/add list=synapse_envs key=SYNAPSE_REPORT_STATS value="no"
```

- `SYNAPSE_SERVER_NAME` - your server's domain name. It becomes part of every user ID (`@alice:matrix.example.com`) and cannot be changed later.
- `SYNAPSE_REPORT_STATS` - `yes` sends anonymous usage statistics to the Synapse developers.

Create a mount for the Synapse configuration and data:

```routeros
/container/mounts/add list=synapse_data src=disk1/synapse-data dst=/data
```

Add the Synapse container with the `generate` command, which creates the configuration files:

```routeros
/container/add remote-image=matrixdotorg/synapse:latest interface=veth1 \
    cmd="generate" root-dir=disk1/synapse mountlists=synapse_data \
    envlists=synapse_envs logging=yes name=synapse
```

RouterOS downloads and extracts both images. Check the progress with `/container/print`; when the extraction is done, the container status is `stopped`.

### Generate the configuration

Start the Synapse container:

```routeros
/container/start [find where name=synapse]
```

It creates the configuration files in `disk1/synapse-data` and stops by itself. This takes a few minutes; the log shows when it is done:

```text
container,info,debug synapse: Generating config file /data/homeserver.yaml
container,info,debug synapse: Generating signing key file /data/matrix.example.com.signing.key
container,info,debug synapse: A config file has been generated in '/data/homeserver.yaml' for server name 'matrix.example.com'. Please review this file and customise it to your needs.
```

Clear the command, so that the container runs the server from now on:

```routeros
/container/set [find where name=synapse] cmd=""
```

### Configure the database

Download `disk1/synapse-data/homeserver.yaml` with an SFTP client, such as `sftp` or WinSCP (the SSH [service](../../system-information-and-utilities/services.md) must be enabled). Replace its `database` section, which uses SQLite, with:

```yaml
database:
  name: psycopg2
  args:
    user: synapse_user
    password: Example-db-pass-1
    dbname: synapse
    host: 172.17.0.2
    port: 5433
    cp_min: 5
    cp_max: 10
    keepalives_idle: 10  # optional
    keepalives_interval: 10  # optional
    keepalives_count: 3     # optional
```

`password` is the `POSTGRES_PASSWORD` from the PostgreSQL environment variables. Upload the file back to the same place.

### Start the server

Start PostgreSQL first, then Synapse:

```routeros
/container/start [find where name=postgresql_synapse]
/container/start [find where name=synapse]
```

When Synapse is ready, the router can reach its client API:

```routeros
/tool/fetch url=http://172.17.0.2:8008/_matrix/client/versions output=user
```

The `code` in the output is `200`.

### Register a user

Open a shell in the Synapse container:

```routeros
/container/shell [find where name=synapse]
```

In the shell, register a user, answer the questions, and leave the shell:

```shell
# register_new_matrix_user -c /data/homeserver.yaml
New user localpart [root]: alice
Password: 
Confirm password: 
Make admin [no]: yes
Sending registration request...
Success!
# exit
```

The user ID is `@alice:matrix.example.com`.

### Access the server

Synapse listens on HTTP port 8008. Devices in the router's LAN can reach it at `http://172.17.0.2:8008`. Matrix clients on the internet and federation with other Matrix servers need HTTPS on your server's domain name; see the [HAProxy](./container-haproxy.md) guide for a reverse proxy with HTTPS, with `172.17.0.2:8008` as the backend, and the Synapse documentation for the federation settings.

## Discord bridge

:::tip

This example adds the [mautrix-discord](https://docs.mau.fi/bridges/go/discord/index.html) bridge; other [bridges](https://matrix.org/ecosystem/bridges/) are set up in a similar way. Check the documentation of your bridge for more information.

:::

The bridge has its own PostgreSQL database. Create its environment variables:

```routeros
/container/envs/add list=postgres_discord_envs key=POSTGRES_DB value="synapse-discord"
/container/envs/add list=postgres_discord_envs key=POSTGRES_PASSWORD value="Example-db-pass-2"
/container/envs/add list=postgres_discord_envs key=POSTGRES_USER value="synapse_discord"
/container/envs/add list=postgres_discord_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
/container/envs/add list=postgres_discord_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
/container/envs/add list=postgres_discord_envs key=PGPORT value=5434
```

Create the mounts for the database and for the bridge configuration:

```routeros
/container/mounts/add list=discord_postgres_data src=disk1/discord-postgres-data dst=/var/lib/postgresql/data
/container/mounts/add list=synapse_discord_data src=disk1/synapse-discord-data dst=/data
```

Add the PostgreSQL container and the bridge container. The bridge image comes from the bridge developers' own registry, `dock.mau.dev`:

```routeros
/container/add remote-image=postgres:17.2-alpine interface=veth1 \
    root-dir=disk1/postgres-17.2-discord mountlists=discord_postgres_data \
    envlists=postgres_discord_envs logging=yes name=postgresql_discord
/container/add remote-image=dock.mau.dev/mautrix/discord:latest interface=veth1 \
    root-dir=disk1/synapse-discord mountlists=synapse_discord_data \
    restart-policy=on-failure logging=yes name=synapse_discord
```

`restart-policy=on-failure` restarts the bridge when it exits with an error, for example when it starts before its database is ready.

When both are extracted, start the bridge once. It creates `disk1/synapse-discord-data/config.yaml` and stops:

```routeros
/container/start [find where name=synapse_discord]
```

Download `config.yaml` with SFTP and change these settings; keep the rest of the file as it is:

```yaml
homeserver:
    address: http://172.17.0.2:8008
    domain: matrix.example.com
    async_media: true

appservice:
    database:
        type: postgres
        uri: postgres://synapse_discord:Example-db-pass-2@172.17.0.2:5434/synapse-discord?sslmode=disable

bridge:
    encryption:
        allow: true
    permissions:
        "*": relay
        "matrix.example.com": user
        "@alice:matrix.example.com": admin
```

- `homeserver` - where the bridge reaches Synapse, and your server name.
- `appservice` - `database` is the bridge's PostgreSQL database, with the password and port from its environment variables. Keep the default `address`, `hostname` and `port`: Synapse reaches the bridge at `localhost:29334`, which works because both containers use `veth1`.
- `bridge` - `permissions` sets who can use the bridge: everyone as relay, the users of your server as users, and `alice` as admin.

Upload `config.yaml` back, start the bridge's database, and start the bridge again. It creates the registration file `disk1/synapse-discord-data/registration.yaml` and stops:

```routeros
/container/start [find where name=postgresql_discord]
/container/start [find where name=synapse_discord]
```

Download `registration.yaml` and upload it to the Synapse data folder as `disk1/synapse-data/mautrix-discord-registration.yaml`. Then add these lines at the end of `disk1/synapse-data/homeserver.yaml`:

```yaml
app_service_config_files:
  - /data/mautrix-discord-registration.yaml
```

Restart Synapse and start the bridge:

```routeros
/container/restart [find where name=synapse]
/container/start [find where name=synapse_discord]
```

The log shows `Bridge started!`, and your Matrix server has a new user, `@discordbot:matrix.example.com`, with the name "Discord bridge bot". Follow the [bridge documentation](https://docs.mau.fi/bridges/go/discord/index.html) to log in to Discord and create bridged rooms.

Containers start with the router only when they have `start-on-boot=yes`. When you start them by hand, for example after a reboot, start the databases first:

```routeros
/container/start [find where name=postgresql_synapse]
/container/start [find where name=postgresql_discord]
/container/start [find where name=synapse]
/container/start [find where name=synapse_discord]
```

For the commands used in this guide, see [`/container`](../../cli-reference/container/container.md), [`/container/config`](../../cli-reference/container/config), [`/container/mounts`](../../cli-reference/container/mounts) and [`/container/envs`](../../cli-reference/container/envs).
