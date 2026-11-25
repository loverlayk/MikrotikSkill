# Container - Postgres

> This guide provides step-by-step instructions for setting up PostgreSQL and pgAdmin containers on MikroTik RouterOS, including creating mount points, configuring environment variables, and starting the containers...

# Container - Postgres

PostgreSQL is a powerful, widely-used SQL database engine that serves as the backbone for numerous applications, ranging from small web projects to enterprise-level systems. This guide will walk you through the essential steps required to get PostgreSQL up and running on RouterOS. Additionally, this guide will provide you with the necessary instructions to set up pgAdmin—a feature-rich, web-based interface that allows you to easily manage your PostgreSQL database.

## Configuration

This section provides step-by-step instructions for setting up a PostgreSQL container on your MikroTik RouterOS device. PostgreSQL is a powerful, open-source relational database system that supports SQL standards and offers advanced features such as transactions, subqueries, and user-defined types. Before proceeding, ensure that you have already created a container network as described in the [Container network](../#networking-examples) documentation.

### Step 1: Create Mount Point for PostgreSQL Container

Before creating the container, you need to create a persistent storage location where PostgreSQL will store its database files. This ensures that your data persists even if the container is recreated or removed, protecting your valuable database information.

```routeros
/container/mounts/add list=MOUNT_POSTGRES src=disk1/volumes/postgres/data dst=/var/lib/postgresql/data
```

This mount point maps your local data directory to the container's `/var/lib/postgresql/data` path, which is where PostgreSQL will store all database files, transaction logs, and system catalogs.

### Step 2: Configure Environment Variables for PostgreSQL Container

Environment variables provide configuration parameters that PostgreSQL requires at startup. These variables define the initial database name, user credentials, and data directory location.

```routeros
/container/envs/add list=ENV_POSTGRES key=POSTGRES_DB value="myapp"
/container/envs/add list=ENV_POSTGRES key=POSTGRES_PASSWORD value="<changeme>"
/container/envs/add list=ENV_POSTGRES key=POSTGRES_USER value="myapp"
/container/envs/add list=ENV_POSTGRES key=PGDATA value="/var/lib/postgresql/data/pgdata"
/container/envs/add list=ENV_POSTGRES key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
```

The `POSTGRES_DB` variable specifies the name of the initial database that will be created when PostgreSQL starts for the first time. The `POSTGRES_USER` and `POSTGRES_PASSWORD` variables define the superuser account credentials that you'll use to connect to and manage your database. The `PGDATA` variable indicates the location within the container where PostgreSQL will store its data files. The `POSTGRES_INITDB_ARGS` variable provides additional initialization parameters that set the database encoding to UTF8 and the locale settings to C for consistent behavior.

### Step 3: Create the PostgreSQL Container

Now you're ready to create and configure the PostgreSQL container instance. This command pulls the official PostgreSQL Docker image from the remote registry and configures it with the environment variables and mount point which were established in the previous steps.

```routeros
/container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres mountlists=MOUNT_POSTGRES envlists=ENV_POSTGRES name=postgres start-on-boot=yes logging=yes
```

:::note

To run a different PostgreSQL version, replace `postgres:15` with another PostgreSQL image tag.

:::

### Step 4: Start the PostgreSQL Container

With all configuration complete, you're now ready to initiate the PostgreSQL container. Starting the container will launch the PostgreSQL database server, which will become ready to accept connections from your applications.

```routeros
/container/start [find where name=postgres]
```

On the first start, PostgreSQL creates the initial database and user from the environment variables. When the log shows `database system is ready to accept connections`, PostgreSQL accepts connections on port 5432 of the container's address (`172.17.0.2` in the [Bridge with NAT](../#bridge-with-nat) example). Because of `start-on-boot=yes`, the container also starts when the router boots.

## Advanced: PostgreSQL with pgAdmin

This guide demonstrates how to configure and deploy pgAdmin, the popular web-based administration tool for PostgreSQL databases, as a container on your MikroTik RouterOS device. pgAdmin provides an intuitive graphical interface for managing your PostgreSQL databases servers, allowing you to create databases, execute queries, manage users, and perform various administrative tasks through a web browser.

### Step 1: Create Mount Points Directories for pgAdmin Container

Before creating the container, you need to create persistent storage locations where pgAdmin will store its configuration files, session data, and server connection settings. This ensures that your settings and connections remain intact even after container restarts or updates.

```routeros
/container/mounts/add list=MOUNT_PGADMIN_CONFIG src=disk1/volumes/pgadmin/config dst=/config
/container/mounts/add list=MOUNT_PGADMIN_DATA src=disk1/volumes/pgadmin/data dst=/var/lib/pgadmin
```

The first mount point maps your local configuration directory to the container's `/config` path, where pgAdmin will store server definitions and user preferences. The second mount point maps your local data directory to the container's `/var/lib/pgadmin` path, which houses session information, logs, and runtime data.

### Step 2: Configure Environment Variables for pgAdmin Container

Environment variables provide configuration parameters that pgAdmin requires at startup. These variables define the application behavior, default credentials, and network settings.

```routeros
/container/envs/add list=ENV_PGADMIN key=PGADMIN_LISTEN_PORT value=80
/container/envs/add list=ENV_PGADMIN key=PGADMIN_DEFAULT_EMAIL value="sysadmin@domain.com"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_DEFAULT_PASSWORD value="<changeme>"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_SERVER_JSON_FILE value="/config/servers.json"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_PREFERENCES_JSON_FILE value="/config/preferences.json"
/container/envs/add list=ENV_PGADMIN key=PGPASS_FILE value="/config/pgpass"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_DISABLE_POSTFIX value="True"
```

The `PGADMIN_LISTEN_PORT` variable specifies which port pgAdmin will listen on for incoming web connections—port 80 is used by default for standard HTTP access. The `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` variables define the initial administrator credentials that you'll use to log into the pgAdmin web interface for the first time. The remaining variables specify file paths within the container where pgAdmin will store and retrieve server connection configurations, user preferences, and password files data.

### Step 3: Create the pgAdmin Container

Now you're ready to create and configure the pgAdmin container instance. This command pulls the official dpage/pgadmin4 Docker image from the remote registry and configures it with the environment variables and mount points which were established in the previous steps.

```routeros
/container/add remote-image=dpage/pgadmin4 envlists=ENV_PGADMIN mountlists=MOUNT_PGADMIN_CONFIG,MOUNT_PGADMIN_DATA interface=veth1 logging=yes name=pgadmin root-dir=disk1/images/pgadmin start-on-boot=yes user=0:0
```

This command specifies the official pgAdmin4 Docker image from Docker Hub, applies your previously defined environment variable list and mount point list, assigns the container to the `veth1` virtual ethernet interface (the same interface as the PostgreSQL container, so both containers share its address), enables logging for troubleshooting purposes, names the container "pgadmin" for easy identification, stores the container image files in the designated disk location, configures the container to start automatically whenever the router boots, and runs the container with root user privileges.

### Step 4: Start the pgAdmin Container

With all configuration complete, you're now ready to initiate the pgAdmin container. Starting the container will launch the pgAdmin web application.

```routeros
/container/start [find where name=pgadmin]
```

On the first start, pgAdmin sets up its own database before it opens the web interface, which can take a few minutes on a slow device. Until then, connections to the container's port 80 are refused.

### Step 5: Open the pgAdmin Web Interface

pgAdmin listens on port 80 of the container's address, not of the router, so it does not conflict with WebFig, and the `www` service can stay enabled. From a host that has a route to the container network, open `http://172.17.0.2/`.

To reach pgAdmin through the router's address instead, forward a free router port to the container. This rule forwards port 8080 for connections that arrive on the `LAN` interface list, so pgAdmin is not exposed on the WAN side:

```routeros
/ip/firewall/nat
add chain=dstnat action=dst-nat protocol=tcp dst-port=8080 \
    in-interface-list=LAN to-addresses=172.17.0.2 to-ports=80 \
    comment=pgadmin
```

Open `http://192.168.88.1:8080/` and log in with the email address and password from Step 2. To manage the database, register a server with host `172.17.0.2`, port `5432`, and the `POSTGRES_USER` and `POSTGRES_PASSWORD` values of the PostgreSQL container.

For the container commands used in this guide, see [`/container`](../../cli-reference/container/container.md), [`/container/envs`](../../cli-reference/container/envs) and [`/container/mounts`](../../cli-reference/container/mounts).
