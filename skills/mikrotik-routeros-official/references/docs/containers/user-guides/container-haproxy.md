# Container - HAProxy

> Run HAProxy in a RouterOS container as a reverse proxy for other containers, and serve HTTPS with Let's Encrypt certificates that Certbot renews and installs in HAProxy without a restart.

# Container - HAProxy

[HAProxy](https://www.haproxy.org/) is a reverse proxy and load balancer. In a container, it sits between users and the services that other containers run, so that those services are not exposed to the network directly. HAProxy can also terminate HTTPS for them.

This guide first runs HAProxy with a minimal HTTP configuration, then adds HTTPS with [Let's Encrypt](https://letsencrypt.org/) certificates that [Certbot](https://certbot.eff.org/) obtains and renews in a second container.

## Summary

Read the [container](../) guide first, especially the [disclaimer](../#disclaimer) and the [requirements](../#requirements): the `container` package must be installed and containers enabled in device-mode.

The examples use the [container network](../#bridge-with-nat) of the container guide: the veth interface `veth1` with the address `172.17.0.2`, and a disk named `disk1`. Containers that use the same veth interface share its address, so HAProxy reaches a backend on `veth1` at `172.17.0.2` and the backend's port.

The examples upload files to the router with SFTP; the SSH [service](../../system-information-and-utilities/services.md) must be enabled.

## Basic configuration

1. Add the mount for the HAProxy configuration folder:

   ```routeros
   /container/mounts/add list=haproxy_etc src=disk1/haproxy-etc \
       dst=/usr/local/etc/haproxy
   ```

2. Add the HAProxy container:

   ```routeros
   /container/add remote-image=haproxy:latest interface=veth1 \
       root-dir=disk1/haproxy mountlists=haproxy_etc user=0:0 \
       name=haproxy logging=yes
   ```

3. Create the configuration file `haproxy.cfg` on your computer. This example forwards HTTP requests on port 80 to a backend on port 8008 of the same veth interface, such as the [Matrix Synapse](container-matrix-synapse.md) server:

   ```text
   defaults
     mode http
     timeout client 10s
     timeout connect 10s
     timeout server 10s
     timeout http-request 10s

   frontend http_synapse
     bind *:80
     use_backend synapse

   backend synapse
     server server1 172.17.0.2:8008 maxconn 32
   ```

4. Upload the file into the mounted folder. The folder does not exist until the container starts for the first time, so create it first:

   ```shell
   sftp admin@192.168.88.1
   sftp> mkdir disk1/haproxy-etc
   sftp> put haproxy.cfg disk1/haproxy-etc/haproxy.cfg
   sftp> exit
   ```

5. Start the container:

   ```routeros
   /container/start [find where name=haproxy]
   ```

To reach HAProxy from the LAN or the internet, forward ports 80 and 443 to `172.17.0.2`, as the [Bridge with NAT](../#bridge-with-nat) example does for another port.

## HTTPS with Certbot

This example serves HTTPS with a certificate from Let's Encrypt, and renews it automatically:

- a Certbot container obtains the certificate with the DNS-01 challenge: it creates a TXT record in your domain with an [RFC 2136](https://www.rfc-editor.org/rfc/rfc2136) dynamic DNS update, so ports 80 and 443 do not have to be open for the validation;
- a deploy hook copies each new certificate into the HAProxy configuration folder, and updates the running HAProxy through its runtime API, without a restart;
- the RouterOS scheduler starts the Certbot container once a day; Certbot renews the certificate when it is due.

Both containers use `veth1`, so the hook reaches the HAProxy runtime API at `127.0.0.1`.

You need:

- a domain name that points to your router, `router.example.com` in this example;
- a DNS server for that domain that accepts RFC 2136 updates signed with a TSIG key, and the key's name, algorithm and secret.

Replace `router.example.com`, `admin@example.com` and the DNS details with your own in all files and commands below.

### HAProxy

1. Add the mount and the HAProxy container:

   ```routeros
   /container/mounts/add list=MOUNT_HAPROXY \
       src=disk1/volumes/haproxy/config dst=/usr/local/etc/haproxy
   /container/add remote-image=haproxy:latest interface=veth1 \
       root-dir=disk1/images/haproxy mountlists=MOUNT_HAPROXY \
       name=haproxy start-on-boot=yes user=0:0 logging=yes
   ```

2. Create `haproxy.cfg` on your computer, and adjust it to your needs. This configuration redirects HTTP to HTTPS, loads every certificate in the `certs` folder, refuses requests from a client address that sends more than 10000 requests in 10 seconds, and forwards the requests to a backend on port 8080:

   ```text
   global
     log stdout format raw local0 info
     stats socket ipv4@127.0.0.1:9999 level admin
     ssl-default-bind-ciphers EECDH+AESGCM:EDH+AESGCM
     ssl-default-server-ciphers EECDH+AESGCM:EDH+AESGCM
     ssl-default-bind-options ssl-min-ver TLSv1.2
     ssl-default-server-options ssl-min-ver TLSv1.2
     tune.ssl.default-dh-param 2048

   defaults
     log global
     timeout client 10s
     timeout connect 10s
     timeout server 10s
     timeout http-request 10s

   frontend frontend_webapp
     mode http
     option httplog
     option http-server-close
     option forwardfor except 127.0.0.0/8
     stick-table type ipv6 size 100k expire 30s store http_req_rate(10s)
     http-request track-sc0 src
     http-request deny deny_status 429 if { sc_http_req_rate(0) gt 10000 }
     bind *:80
     bind *:443 ssl crt /usr/local/etc/haproxy/certs/
     http-request redirect scheme https unless { ssl_fc }
     http-request set-header X-Forwarded-Host %[req.hdr(host)]
     use_backend backend_webapp

   backend backend_webapp
     mode http
     balance roundrobin
     option http-server-close
     option forwardfor
     server server1 172.17.0.2:8080
   ```

   - `stats socket ipv4@127.0.0.1:9999 level admin` - the runtime API that the deploy hook uses. It accepts commands without authentication, so it listens only on `127.0.0.1`, which only the containers on `veth1` can reach.
   - `option forwardfor` - HAProxy adds the `X-Forwarded-For` header with the client's address to each request it forwards to the backend.

3. Upload the file. Do not start HAProxy yet: it does not start without a certificate in the `certs` folder.

   ```shell
   sftp admin@192.168.88.1
   sftp> mkdir disk1/volumes
   sftp> mkdir disk1/volumes/haproxy
   sftp> mkdir disk1/volumes/haproxy/config
   sftp> put haproxy.cfg disk1/volumes/haproxy/config/haproxy.cfg
   sftp> exit
   ```

### Certbot

Certbot reads its options from `/etc/letsencrypt/cli.ini`. With the options in this file, the container's `cmd` only names the Certbot command and the domain.

1. Create these three files on your computer.

   `rfc2136.ini`, the DNS server and the TSIG key for the update:

   ```text
   dns_rfc2136_server = 192.0.2.53
   dns_rfc2136_port = 53
   dns_rfc2136_name = certbot.
   dns_rfc2136_secret = <TSIG secret>
   dns_rfc2136_algorithm = HMAC-SHA512
   ```

   `cli.ini`, the Certbot options:

   ```text
   non-interactive = true
   agree-tos = true
   email = admin@example.com
   authenticator = dns-rfc2136
   dns-rfc2136-credentials = /etc/letsencrypt/rfc2136.ini
   deploy-hook = sh /etc/letsencrypt/haproxy-deploy.sh
   ```

   `haproxy-deploy.sh`, the deploy hook. Certbot runs it after it receives a new certificate, and sets `RENEWED_LINEAGE` to the certificate's folder, `/etc/letsencrypt/live/router.example.com`:

   ```shell
   #!/bin/sh
   # Certbot deploy hook: install a new certificate in HAProxy.
   # Certbot sets RENEWED_LINEAGE to /etc/letsencrypt/live/<name>.
   name=$(basename "$RENEWED_LINEAGE")
   mkdir -p /etc/haproxy/certs
   cat "$RENEWED_LINEAGE/fullchain.pem" "$RENEWED_LINEAGE/privkey.pem" \
     > "/etc/haproxy/certs/$name.pem"
   # Update a running HAProxy through its runtime API (path as HAProxy sees it).
   crt=/usr/local/etc/haproxy/certs/$name.pem
   { echo "set ssl cert $crt <<"; cat "/etc/haproxy/certs/$name.pem"; echo; } \
     | nc 127.0.0.1 9999
   echo "commit ssl cert $crt" | nc 127.0.0.1 9999
   ```

   Files uploaded to the router are not executable in the container, so `cli.ini` runs the hook with `sh`.

2. Upload the files into the Certbot configuration folder:

   ```shell
   sftp admin@192.168.88.1
   sftp> mkdir disk1/volumes/certbot
   sftp> mkdir disk1/volumes/certbot/config
   sftp> cd disk1/volumes/certbot/config
   sftp> put rfc2136.ini
   sftp> put cli.ini
   sftp> put haproxy-deploy.sh
   sftp> exit
   ```

3. Add the mounts and the Certbot container. The fourth mount gives Certbot the HAProxy configuration folder, where the hook writes the certificate:

   ```routeros
   /container/mounts
   add list=MOUNT_CERTBOT src=disk1/volumes/certbot/config \
       dst=/etc/letsencrypt
   add list=MOUNT_CERTBOT src=disk1/volumes/certbot/data \
       dst=/var/lib/letsencrypt
   add list=MOUNT_CERTBOT src=disk1/volumes/certbot/log \
       dst=/var/log/letsencrypt
   add list=MOUNT_CERTBOT src=disk1/volumes/haproxy/config \
       dst=/etc/haproxy
   /container/add remote-image=certbot/dns-rfc2136 \
       cmd="certonly -d router.example.com" interface=veth1 \
       root-dir=disk1/images/certbot mountlists=MOUNT_CERTBOT \
       name=certbot start-on-boot=yes logging=yes
   ```

4. When the image is extracted (the container status is `stopped`), start the Certbot container:

   ```routeros
   /container/start [find where name=certbot]
   ```

5. Check the log. Certbot waits 60 seconds for the DNS record to propagate, then receives the certificate and stops (some lines left out):

   ```routeros
   /log/print where topics~"container" and message~"certbot"
   ```

   ```text
    2026-11-24 06:57:28 container,info,debug certbot: Account registered.
    2026-11-24 06:57:28 container,info,debug certbot: Requesting a certificate for router.example.com
    2026-11-24 06:57:28 container,info,debug certbot: Unsafe permissions on credentials configuration file: /etc/letsencrypt/rfc2136.ini
    2026-11-24 06:57:28 container,info,debug certbot: Waiting 60 seconds for DNS changes to propagate
    2026-11-24 06:58:31 container,info,debug certbot: Hook 'deploy-hook' reported error code 1
    2026-11-24 06:58:31 container,info,debug certbot: Successfully received certificate.
    2026-11-24 06:58:31 container,info,debug certbot: Certificate is saved at: /etc/letsencrypt/live/router.example.com/fullchain.pem
    2026-11-24 06:58:31 container,info,debug certbot: Key is saved at:         /etc/letsencrypt/live/router.example.com/privkey.pem
   ```

   Certbot warns about `Unsafe permissions` because files uploaded to the router are readable by every user in the container; only Certbot runs in it.

   On this first run, HAProxy is not running yet, so the hook cannot reach the runtime API, and Certbot logs `Hook 'deploy-hook' reported error code 1`. The certificate is already in the `certs` folder, and HAProxy loads it when it starts.

6. Start HAProxy:

   ```routeros
   /container/start [find where name=haproxy]
   ```

7. Start the Certbot container every day, for example at 06:30. Certbot renews the certificate when it is due; otherwise, it stops with `Certificate not yet due for renewal; no action taken.`

   ```routeros
   /system/scheduler/add name=certbot-renew interval=1d \
       start-time=06:30:00 \
       on-event="/container/start [find where name=certbot]"
   ```

When Certbot renews the certificate, the hook replaces it in the running HAProxy, and the log shows the runtime API's answers (some lines left out):

```text
 2026-11-24 06:59:04 container,info,debug certbot: Renewing an existing certificate for router.example.com
 2026-11-24 06:59:04 container,info,debug certbot: Waiting 60 seconds for DNS changes to propagate
 2026-11-24 07:00:07 container,info,debug certbot: Hook 'deploy-hook' ran with output:
 2026-11-24 07:00:07 container,info,debug certbot:  Transaction created for certificate /usr/local/etc/haproxy/certs/router.example.com.pem!
 2026-11-24 07:00:07 container,info,debug certbot:  Committing /usr/local/etc/haproxy/certs/router.example.com.pem.
 2026-11-24 07:00:07 container,info,debug certbot:  Success!
 2026-11-24 07:00:07 container,info,debug certbot: Successfully received certificate.
```

For the commands used in this guide, see [`/container`](../../cli-reference/container/container.md), [`/container/mounts`](../../cli-reference/container/mounts) and [`/system/scheduler`](../../cli-reference/system/scheduler).
