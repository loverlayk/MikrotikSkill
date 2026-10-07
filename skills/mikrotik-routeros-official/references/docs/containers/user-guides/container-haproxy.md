# Container - HAProxy

> This page documents configuring HAProxy as a Container in MikroTik RouterOS, providing step-by-step instructions for setting up reverse proxy and load balancing with HTTPS support using Certbot.

# Container - HAProxy

HAProxy is a high-performance reverse proxy and load balancer as a Container.

For optimal security, it is highly recommended to use a reverse HTTP/HTTPS proxy like HAProxy as an intermediary between external users and your internal services, rather than exposing containers directly to the network.

## Configuration

To set up a HAProxy Container on your RouterOS device, follow these steps below.

:::info

Make sure you have created a [Container network](../#networking-examples) before proceeding.

:::

1. Create HAProxy Container mount points.  

   ```routeros
   /container/mounts/add list=haproxy_etc src=disk1/haproxy-etc dst=/usr/local/etc/haproxy
   ```

2. Create a HAProxy Container.  

   ```routeros
   /container/add remote-image=haproxy:latest interface=veth1 root-dir=disk1/haproxy mountlists=haproxy_etc user=0:0 name=haproxy
   ```

3. Connect to your RouterOS device using an SFTP client (for example, WinSCP when using Microsoft Windows) and create a new file `disk1/haproxy-etc/haproxy.cfg` , you can use the following config as an example.  

```cfg
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

1. Start the HAProxy Container.  

   ```routeros
   /container/start [find where name=haproxy]
   ```

## Advanced: HAProxy with Certbot

This example shows how to configure HAProxy to serve HTTPS traffic and automatically renew the certificates by using Certbot and RFC2136.

1. Create HAProxy Container:  

   ```routeros
   /container/mounts/add list=MOUNT_HAPROXY src=disk1/volumes/haproxy/config dst=/usr/local/etc/haproxy
   /container/add remote-image=haproxy:latest interface=veth1 root-dir=disk1/images/haproxy mountlists=MOUNT_HAPROXY name=haproxy start-on-boot=yes user=0:0 logging=yes
   ```

2. Create a new file called `haproxy.cfg`  on your PC and upload it to `disk1/volumes/haproxy/config/` , adjust the configuration to your needs:  

```cfg
global
  log stdout format raw local0 info
  stats socket :9999 level admin expose-fd listeners
  ssl-default-bind-ciphers EECDH+AESGCM:EDH+AESGCM
  ssl-default-server-ciphers EECDH+AESGCM:EDH+AESGCM
  ssl-default-bind-options ssl-min-ver TLSv1.2
  ssl-default-server-options ssl-min-ver TLSv1.2
  tune.ssl.default-dh-param 2048
  tune.bufsize 43768
  tune.ssl.cachesize 1000000
  nbthread 8

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
  http-request set-header X-Forwarded-For %[src]
  use_backend backend_webapp

backend backend_webapp
  mode http
  balance roundrobin
  option http-server-close
  option forwardfor
  server server1 172.17.0.2:8080

```

1. Create the Certbot Container:  

   ```routeros
   /container/mounts/add list=MOUNT_CERTBOT_CONFIG src=disk1/volumes/certbot/config dst=/etc/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_DATA src=disk1/volumes/certbot/data dst=/var/lib/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_LOG src=disk1/volumes/certbot/log dst=/var/log/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_HAPROXY src=disk1/volumes/haproxy/config dst=/etc/haproxy
   /container/add remote-image=certbot/dns-rfc2136 cmd="certonly -n --agree-tos --dns-rfc2136 --dns-rfc2136-credentials /etc/letsencrypt/rfc2136.ini -m admin@<FQDN> --deploy-hook 'cat /etc/letsencrypt/li\
       ve/<FQDN>/fullchain.pem /etc/letsencrypt/live/<FQDN>/privkey.pem | tee /etc/haproxy/certs/<FQDN>.pem > /dev/null; echo -e \"set ssl cert /usr/local/e\
       tc/haproxy/certs/<FQDN>.pem <<\
       \n\$(cat /etc/haproxy/certs/<FQDN>.pem)\
       \n\" | nc 127.0.0.1:9999; echo \"commit ssl cert /usr/local/etc/haproxy/certs/<FQDN>.pem\" | nc 127.0.0.1:9999' -d <FQDN> --cert-name <FQDN>" \
       interface=veth1 logging=yes mountlists=MOUNT_CERTBOT_CONFIG,MOUNT_CERTBOT_DATA,MOUNT_CERTBOT_LOG,MOUNT_CERTBOT_HAPROXY name=certbot root-dir=\
       disk1/images/certbot start-on-boot=yes workdir=/opt/certbot

   ```

:::warning

Make sure to replace all `<FQDN>` placeholders in the example above with your fully qualified domain name!

:::

1. Wait for the Container image to be downloaded and start the Certbot Container:  

   ```routeros
   /container/start [find where name=certbot]
   ```

2. Check the logs to make sure you successfully received a new certificate:  

   ```routeros
   /log/print follow
   ```

3. Start HAProxy Container:  

   ```routeros
   /container/start [find where name=haproxy]
   ```

4. Set up a schedule, for example, each day at 06:30 to check for a new certificate:  

   ```routeros
   /system/scheduler
   add interval=1d name=SCHEDULE_RenewCertbot on-event=SCRIPT_RenewCertbot policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=\
       2025-03-10 start-time=06:30:00
   /system/script
   add dont-require-permissions=no name=SCRIPT_RenewCertbot owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=\
       "/container/start [find where name=\"certbot\"]"
   ```

5. Done

The certificate will automatically renew and replace old certificates in HAProxy without needing to restart the Container.
