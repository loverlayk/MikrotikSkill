# Container - Matrix (Synapse)

> This page documents setting up a Synapse Matrix server as a container on MikroTik RouterOS, covering prerequisites like container network configuration and PostgreSQL environment setup for secure federated...

# Container - Matrix (Synapse)

Matrix is a decentralized communication protocol. Each Matrix server operates independently, maintaining its own set of users and defining its own rules and policies.

### Hosting Your Own Matrix Server

You can host your own Matrix server directly on a RouterOS device using Containers. This allows you to maintain full control over your communication infrastructure.

### Federation

Matrix servers can connect through federation to create a unified communication network. This enables users on different Matrix servers to communicate with each other securely, without requiring a central authority.

### Bridging to Other Platforms

Matrix supports bridging to relay messages from other chat platforms, including:

- WhatsApp
- Discord
- Signal
- Telegram
- And many other platforms

By using Matrix bridges, you can consolidate communication from multiple platforms into a single application, such as [Element](https://element.io/). This allows you to communicate with users across different platforms through one unified interface.

# Setting Up a Synapse Matrix Server on RouterOS

This guide explains how to set up Synapse, one of several available Matrix servers on your MikroTik RouterOS device using containers.

:::info

Before proceeding, ensure you have created a Container network. For instructions, refer to the [Container network documentation](../#networking-examples).

:::

---

## Prerequisites

- A RouterOS device with container support
- An existing container network configured
- Sufficient storage space for the database and Synapse data

---

## Step 1: Create PostgreSQL Container Environment Variables

Configure the environment variables list for the PostgreSQL container:

```routeros
/container/envs/add list=postgres_synapse_envs key=POSTGRES_DB value="synapse"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_PASSWORD value="<POSTGRES_PASSWORD_HERE>"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_USER value="synapse_user"
/container/envs/add list=postgres_synapse_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
/container/envs/add list=postgres_synapse_envs key=PGPORT value=5433
```

:::note

Replace `<POSTGRES_PASSWORD_HERE>` with your desired PostgreSQL password.

:::

---

## Step 2: Create PostgreSQL Container Mount

Create a mount point to persist the PostgreSQL data on your RouterOS device:

```routeros
/container/mounts/add list=synapse_postgres_data src=disk1/synapse-postgres-data dst=/var/lib/postgresql/data
```

---

## Step 3: Create the PostgreSQL Container

Launch the PostgreSQL container using the configuration from the previous steps:

```routeros
/container/add remote-image=postgres:17.2-alpine interface=veth1 root-dir=disk1/postgres-17.2-synapse mountlists=synapse_postgres_data envlists=postgres_synapse_envs name=postgresql_synapse
```

---

## Step 4: Create Synapse Container Environment Variables

Configure the environment variables for the Synapse container:

```routeros
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_DIR value="/data"
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_PATH value="/data/homeserver.yaml"
/container/envs/add list=synapse_envs key=SYNAPSE_SERVER_NAME value="test.mt.lv"
/container/envs/add list=synapse_envs key=SYNAPSE_REPORT_STATS value="yes"
```

:::note

Replace `test.mt.lv` with your actual server domain name.

:::

---

## Step 5: Create Synapse Container Mount

Create a mount point to persist Synapse data on your RouterOS device:

```routeros
/container/mounts/add list=synapse_data src=disk1/synapse-data dst=/data
```

---

## Step 6: Generate Initial Synapse Configuration

Create and run a Synapse container to generate the required configuration files. The container runs with the `generate` command to create initial configuration:

```routeros
/container/add remote-image=matrixdotorg/synapse:latest interface=veth1 cmd="generate" root-dir=disk1/synapse mountlists=synapse_data envlists=synapse_envs name=synapse
```

---

## Step 7: Initialize Configuration Files

Start and then stop the Synapse container to allow it to generate the necessary configuration files:

```routeros
/container/start [find where name=synapse]
/container/stop [find where name=synapse]
```

---

## Step 8: Remove the Generate Command

Clear the command parameter from the Synapse container so it runs in normal mode:

```routeros
/container/set [find where name=synapse] cmd=""
```

---

## Step 9: Configure Database Connection

Connect to your RouterOS device using an SFTP client (such as WinSCP on Windows) and edit the generated configuration file at `disk1/synapse-data/homeserver.yaml`. Update the database section with the following settings:

```yaml
database:
  name: psycopg2
  args:
    user: synapse_user
    password: <POSTGRES_PASSWORD_HERE>
    dbname: synapse
    host: 172.17.0.2
    port: 5433
    cp_min: 5
    cp_max: 10
    keepalives_idle: 10  # optional
    keepalives_interval: 10  # optional
    keepalives_count: 3     # optional
```

:::info

Replace `<POSTGRES_PASSWORD_HERE>` with the password you set in Step 1.

:::

---

## Step 10: Start the PostgreSQL Container

Start the PostgreSQL container to prepare the database:

```routeros
/container/start [find where name=postgresql_synapse]
```

---

## Step 11: Start the Synapse Container

Start the Synapse container to run your Matrix server:

```routeros
/container/start [find where name=synapse]
```

---

## Step 12: Register a Matrix User

Enter the Synapse container's shell and register a new user:

```routeros
/container/shell [find where name=synapse]
```

Once inside the container, run:

```
register_new_matrix_user -c /data/homeserver.yaml
```

Follow the prompts to create your admin user account.

---

## Step 13: Access Your Matrix Server

Your Synapse Matrix server is now running. Access it using your RouterOS device's IP address or domain name.

---

:::warning

Always consult the official Synapse documentation for the latest configuration options and best practices, as configuration procedures may change with newer versions.

:::

### Discord bridge

:::tip

The example below is for configuring a Discord bridge, but the procedure for other types of [bridges](https://matrix.org/ecosystem/bridges/) is very similar. Check the official documentation of your desired [bridge](https://matrix.org/ecosystem/bridges/) for more information.

:::

1. Create PostgreSQL Discord bridge Container environment variables:  

   ```routeros
   /container/envs/add list=postgres_discord_envs key=POSTGRES_DB value="synapse-discord"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_PASSWORD value="<POSTGRE_BRIDGE_PASSWORD_HERE>"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_USER value="synapse_discord"
   /container/envs/add list=postgres_discord_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
    /container/envs/add list=postgres_discord_envs key=PGPORT value=5434
   ```

2. Create PostgreSQL Discord bridge Container mounts:  

   ```routeros
   /container/mounts/add list=discord_postgres_data src=disk1/discord-postgres-data dst=/var/lib/postgresql/data
   ```

3. Create a PostgreSQL Container for Discord bridge:  

   ```routeros
   /container/add remote-image=postgres:17.2-alpine interface=veth1 root-dir=disk1/postgres-17.2-discord mountlists=discord_postgres_data envlists=postgres_discord_envs name=postgresql_discord
   ```

4. Follow the guide for [HAProxy](./container-haproxy.md) Container and set up a reverse proxy for port `8080`
5. Create Discord bridge Container mount points:  

   ```routeros
   /container/mounts/add list=synapse_discord_data src=disk1/synapse-discord-data dst=/data
   ```

6. Create a Discord Bridge Container:  

   ```routeros
   /container/add remote-image=litetex/mau.mautrix.discord:latest interface=veth1 root-dir=disk1/synapse-discord mountlists=synapse_discord_data name=synapse_discord
   ```

7. Start and stop the Discord bridge Container to generate files:  

   ```routeros
   /container/start [find where name=synapse_discord]
   /container/stop [find where name=synapse_discord]
   ```

8. Connect to your RouterOS device using an SFTP client (for example, WinSCP when using Microsoft Windows) and adjust the file `disk1/synapse-discord/config.yaml` :  

   ```yaml
    homeserver
        address: http://172.17.0.2:8008
        domain: test.mt.lv
       software: standard
       async_media: true
       
   appservice
       address: leave default
       hostname: leave default
       port: leave default
       database:
           type: postgres
           uri: postgres://synapse_discord:<POSTGRE_DISCORD_PASSWORD_HERE>@172.17.0.2:5434/synapse-discord?sslmode=disable
   bridge:
       encryption:
           allow: true
       permissions:
           "*": relay
           "@your_admin_user1:test.mt.lv": admin
           "@your_admin_user2:test.mt.lv": admin
   ```

9. Start and stop the Discord bridge Container again:  

   ```routeros
   /container/start [find where name=synapse_discord]
   /container/stop [find where name=synapse_discord]
   ```

10. Download the file `disk1/synapse-discord/registration.yaml`  and upload it as a file `disk1/synapse-data/mautrix-discord-registration.yaml`
11. Connect to your RouterOS device using an SFTP client (for example, WinSCP when using Microsoft Windows) and add the following lines to `disk1/synapse-data/homeserver.yaml`:  

     ```yaml
     ...
     app_service_config_files:
     - /data/mautrix-discord-registration.yaml
     ```

12. Start the Synapse and Discord bridge Containers:  

     ```routeros
    /container/start [find where name=postgresql_discord]
    /container/start [find where name=synapse_discord]
    /container/start [find where name=postgresql_synapse]
    /container/start [find where name=synapse]
    ```

13. Your Matrix server should now have a new user called "Discord bridge bot". Follow the official documentation to create bridged rooms.
