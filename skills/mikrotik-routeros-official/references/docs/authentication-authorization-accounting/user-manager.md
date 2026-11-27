# User Manager

> User Manager is the RADIUS server of RouterOS: add routers and users, send RADIUS attributes, limit speed, traffic and time with profiles, change the plan of a connected user with CoA, limit simultaneous sessions,...

# User Manager

User Manager is a RADIUS server that runs on RouterOS. It keeps one user database for many routers, and each router asks it to authenticate users with the [RADIUS](radius) client. DHCP, [Dot1X](dot1x), HotSpot, IPsec, [PPP](ppp-aaa), wireless and the router login can use it.

- User Manager is a separate [package](../getting-started/installation-and-upgrade/packages), `user-manager`. It is available for all architectures except SMIPS. The database is stored on the router, so check the free space of a device with a small disk.
- The authentication methods are PAP, CHAP, MS-CHAP, MS-CHAPv2, EAP-TLS, EAP-TTLS and EAP-PEAP.
- The license level limits the number of active sessions: see the tables for [MikroTik devices](../getting-started/routeros-licensing/mikrotik-hardware/) and for [x86 and CHR](../getting-started/routeros-licensing/x86/). Two sessions of one user count as two.
- User Manager follows [RFC 2865](https://tools.ietf.org/html/rfc2865) and [RFC 3579](https://tools.ietf.org/html/rfc3579).

![PPPoE, DHCP and VPN servers, wireless access points, 802.1X switches and HotSpot routers send RADIUS requests to User Manager](./img/user-manager-01.webp)

The examples use two routers. User Manager runs on the router 172.31.30.195. The router 172.31.30.25 is an L2TP and PPPoE server and sends its users to User Manager. A router that asks a RADIUS server is called a NAS (network access server).

## Add a router and a user

On the User Manager router, enable User Manager, add the NAS with a shared secret, and add a user:

```ros
/user-manager/set enabled=yes
/user-manager/router/add name=vpn-server address=172.31.30.25 \
    shared-secret=Radius-Secret-1
/user-manager/user/add name=mario password=Mario-Pass-1
```

On the NAS, add User Manager as the RADIUS server with the same secret and let PPP use RADIUS:

```ros
/radius/add address=172.31.30.195 secret=Radius-Secret-1 service=ppp
/radius/incoming/set accept=yes
/ppp/aaa/set use-radius=yes interim-update=1m
```

- `/radius/incoming/set accept=yes` lets User Manager change and disconnect a session. User Manager needs it to enforce limits, to change plans and to close sessions. If the NAS listens on another `port` in `/radius/incoming`, set the same port in `coa-port` of the router entry.
- `interim-update` makes the NAS send the counters of a session every minute. User Manager checks the limits when it receives the counters.
- User Manager listens on UDP ports 1812 (authentication) and 1813 (accounting). The firewall of the User Manager router must accept them from the NAS, and the firewall of the NAS must accept the `port` of `/radius/incoming` (default 3799) from User Manager.

The default firewall of a home or office router drops these packets on the WAN side. Accept them before the default drop rule. On the User Manager router:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    dst-port=1812,1813 src-address=172.31.30.25 comment="RADIUS from NAS" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

On the NAS:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    dst-port=3799 src-address=172.31.30.195 comment="RADIUS CoA" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

When mario connects to the L2TP server, the session appears in User Manager:

```ros
[admin@MikroTik] > /user-manager/session/print detail
Flags: A - ACTIVE
0  A user=mario acct-session-id="81100080" nas-port-type=virtual
     nas-ip-address=172.31.30.25 nas-identifier="nas1"
     calling-station-id="172.31.30.195" user-address=10.0.0.99 status=start
     started=2026-11-19 13:25:28 uptime=0s download=0 upload=0
     last-accounting-packet=2026-11-19 13:25:28
```

Sessions are listed only when the NAS sends accounting. `/user-manager/router/monitor` counts the requests of a router:

```ros
[admin@MikroTik] > /user-manager/router/monitor [find] once
      broken-requests: 0
     unknown-requests: 0
      access-requests: 1
      access-failures: 0
  accounting-requests: 2
  accounting-failures: 0
       disconnect-ack: 0
       disconnect-nak: 0
              coa-ack: 0
              coa-nak: 0
      sent-from-cache: 0
```

User Manager can also serve the router it runs on. Add a router entry and a `/radius` entry with the address 127.0.0.1. The L2TP/IPsec example near the end of this page is a complete configuration of this kind.

The connection to a NAS can be encrypted with RadSec: see [RADIUS](radius). With RadSec, User Manager sends the change and disconnect requests inside the TLS connection, and `coa-port` is not used.

## Send RADIUS attributes to the NAS

User Manager adds the attributes of a user to the Access-Accept message. The NAS applies them to the session. This user always gets the address 10.0.0.5:

```ros
/user-manager/user/set [find name=mario] \
    attributes=Framed-IP-Address:10.0.0.5
```

A user with a fixed address can have one session only, so keep `shared-users=1`.

`/user-manager/user/monitor` shows the attributes that the user gets:

```ros
[admin@MikroTik] > /user-manager/user/monitor [find name=mario] once
         total-uptime: 31s                                             
       total-download: 469                                             
         total-upload: 1901                                            
      active-sessions: 1                                               
  active-sub-sessions: 1                                               
   attributes-details: Framed-IP-Address:10.0.0.5:ip-address:0x0A000005
```

Several attributes are separated with commas:

```ros
/user-manager/user/set [find name=mario] \
    attributes=Mikrotik-Address-List:vpn-users,Acct-Interim-Interval:120
```

This replaces the earlier attributes of the user.

`/user-manager/attribute` has the attributes that User Manager knows, and the list of predefined attributes is at the end of this page. To send another attribute, add it with its number first:

```ros
/user-manager/attribute/add name=Reply-Message type-id=18 \
    value-type=string
```

[RADIUS](radius) explains what RouterOS does with each attribute.

## Group users

A group gives the same attributes to many users and sets the authentication methods that its users can use. This group gives its users addresses from the pool `branch-pool`, which must exist on the NAS:

```ros
/user-manager/user/group/add name=branch outer-auths=mschap2,chap \
    attributes=Framed-Pool:branch-pool
/user-manager/user/set [find name=mario] group=branch
```

- A new group has no authentication methods. Set `outer-auths`, or the users of the group cannot log in.
- `outer-auths` are the methods of the request itself: `pap`, `chap`, `mschap1`, `mschap2`, `eap-tls`, `eap-ttls`, `eap-peap`, `eap-mschap2`.
- `inner-auths` are the methods inside an EAP-TTLS or EAP-PEAP tunnel: `ttls-pap`, `ttls-chap`, `ttls-mschap1`, `ttls-mschap2`, `peap-mschap2`.
- There are two built-in groups. `default` allows all methods and is the group of a new user. `default-anonymous` allows EAP-TTLS and EAP-PEAP without inner methods.

For the EAP methods, set a server certificate from the [certificate](certificates) store in `certificate` of `/user-manager`.

## Limit speed, traffic and time with profiles

Without profiles, a user needs only a name and a password. With `use-profiles=yes`, each user must have a valid profile, and the profile sets the limits. The setting applies to all users: give a profile to the users that exist, including accounts for the router login, before you turn it on.

The parts are:

- A limitation (`/user-manager/limitation`) is a set of limits: speed, traffic, time.
- A profile (`/user-manager/profile`) is a plan for users. It has a validity time and can have a price.
- A profile limitation (`/user-manager/profile-limitation`) connects a limitation to a profile for the given days and time of day.
- A user profile (`/user-manager/user-profile`) gives a profile to a user.

This example gives mario a 30-day plan with 5 Mbps upload and 10 Mbps download:

```ros
/user-manager/set use-profiles=yes
/user-manager/limitation/add name=10M rate-limit-rx=5M \
    rate-limit-tx=10M
/user-manager/profile/add name=home name-for-users="Home 10M" \
    validity=30d
/user-manager/profile-limitation/add profile=home limitation=10M
/user-manager/user-profile/add user=mario profile=home
```

The `rx` values limit what the NAS receives from the user (upload), and the `tx` values limit what it sends to the user (download). User Manager sends the speed in the Mikrotik-Rate-Limit attribute, and at the next login the NAS creates a queue for the user:

```ros
[admin@MikroTik] > /queue/simple/print
Flags: D - DYNAMIC
0 D name="<l2tp-mario>" target=<l2tp-mario> parent=none packet-marks=""
    priority=8/8 queue=default-small/default-small limit-at=5M/10M
    max-limit=5M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
    bucket-size=0.1/0.1
```

When the speed of the limitation changes later, User Manager sends the new speed to the connected users at once.

The user profile shows the state of the plan and when it ends:

```ros
[admin@MikroTik] > /user-manager/user-profile/print detail
0  user=mario profile=home state=running-active end-time=2026-12-26 08:56:06
```

| State | Meaning |
| :-- | :-- |
| `waiting` | The profile has `starts-when=first-auth` and the user has not logged in yet. |
| `running-active` | The profile that the user has now. |
| `running` | A valid profile that is not in use: the user has another profile, or the limits of this one are reached. |
| `used` | The validity time is over. The profile cannot be used again. |

:::warning
The IPsec service of RouterOS does not apply rate limits.
:::

### Traffic and time limits

`download-limit`, `upload-limit`, `transfer-limit` (download and upload together) and `uptime-limit` set how much a user can use:

```ros
/user-manager/limitation/set [find name=10M] transfer-limit=50G \
    uptime-limit=10h
```

- The limits count all sessions of the user together, not each session.
- User Manager checks the limits when the NAS sends the counters of a session, and when a limitation changes. The NAS must send accounting with interim updates, and it must accept disconnect requests (`/radius/incoming/set accept=yes`).
- When a limit is reached and the user has no other profile, User Manager disconnects the session. The session has `terminate-cause=um-limits-reached`, and the next logins are refused. When the user has another profile, the user stays connected and gets that profile, as the next section shows.
- `reset-counters-interval` clears the counters of the users every hour, day, week or month, counted from `reset-counters-start-time`.

### Validity

`validity` is how long a user can use a profile. With `starts-when=assigned` the time starts when the profile is given to the user. With `starts-when=first-auth` it starts at the first login:

```ros
/user-manager/limitation/add name=1M rate-limit-rx=1M \
    rate-limit-tx=1M
/user-manager/profile/add name=trial validity=1d \
    starts-when=first-auth
/user-manager/profile-limitation/add profile=trial limitation=1M
```

When the validity time is over, User Manager disconnects the session and the state of the user profile changes to `used`.

### Several profiles and limitations

- A user can have several profiles, and uses one at a time. When the profile is over, or its limits are reached, the user gets the next one. `/user-manager/user-profile/activate-user-profile` makes a profile the active one at once.
- To slow a user down after a traffic limit and not cut the user off, give the user two profiles: the first with the limit, the second with a lower speed and no limit. When the limit is reached, User Manager makes the second profile active and sends its speed to the NAS in a CoA request. The user stays connected.
- A profile can have several limitations for different days and hours. This gives the full speed during the day and a lower speed at night:

```ros
/user-manager/profile-limitation/set [find profile=home] \
    from-time=6h till-time=23h59m59s
/user-manager/profile-limitation/add profile=home limitation=1M \
    from-time=0s till-time=6h
```

- At a time that no limitation of the profile covers, the user cannot log in.
- When several limitations of a profile cover the same time, the user must comply with all of them. For example, one limitation can set a traffic limit for a day and another for a month.

## Change a plan while the user is connected

User Manager changes a running session with a Change of Authorization (CoA) request to the NAS, and the user stays connected. The NAS must accept these requests (`/radius/incoming/set accept=yes`). The examples in this section use a PPPoE server as the NAS.

This moves mario from the `home` profile to a faster profile at once:

```ros
/user-manager/limitation/add name=50M rate-limit-rx=10M \
    rate-limit-tx=50M
/user-manager/profile/add name=fast name-for-users="Fast 50M" \
    validity=30d
/user-manager/profile-limitation/add profile=fast limitation=50M
/user-manager/user-profile/add user=mario profile=fast
/user-manager/user-profile/activate-user-profile \
    [find user=mario profile=fast]
```

The NAS replaces the queue of mario, so the queue gets a new number, and counts the request:

```ros
[admin@MikroTik] > /queue/simple/print where dynamic
Flags: D - DYNAMIC
1 D name="<pppoe-mario>" target=<pppoe-mario> parent=none packet-marks=""
    priority=8/8 queue=default-small/default-small limit-at=10M/50M
    max-limit=10M/50M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
    bucket-size=0.1/0.1
```

```ros
[admin@MikroTik] > /radius/incoming/monitor once
      requests: 1
  bad-requests: 0
          acks: 1
          naks: 0
```

The new profile is active. The old profile keeps the state `running`:

```ros
[admin@MikroTik] > /user-manager/user-profile/print detail
0  user=mario profile=home state=running end-time=2026-12-26 08:56:06
 
1  user=mario profile=fast state=running-active end-time=2026-12-26 08:56:26
```

The old profile can be removed. The user stays connected:

```ros
/user-manager/user-profile/remove [find user=mario profile=home]
```

A change of a limitation reaches every connected user who has it. This raises the speed of the `fast` plan:

```ros
/user-manager/limitation/set [find name=50M] rate-limit-rx=20M \
    rate-limit-tx=100M
```

```ros
[admin@MikroTik] > /queue/simple/print where dynamic
Flags: D - DYNAMIC
2 D name="<pppoe-mario>" target=<pppoe-mario> parent=none packet-marks=""
    priority=8/8 queue=default-small/default-small limit-at=20M/100M
    max-limit=20M/100M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
    bucket-size=0.1/0.1
```

The counters of the NAS add up, so `requests` and `acks` grow by one:

```ros
[admin@MikroTik] > /radius/incoming/monitor once
      requests: 2
  bad-requests: 0
          acks: 2
          naks: 0
```

### What User Manager sends to the NAS

| Change in User Manager | Request to the NAS |
| :-- | :-- |
| The speed of a limitation (`rate-limit-rx`, `rate-limit-tx` and the burst, priority and minimum values) | CoA with the new Mikrotik-Rate-Limit |
| A limitation added to or removed from the active profile | CoA |
| `/user-manager/user-profile/activate-user-profile` | CoA |
| A traffic or time limit is reached, and the user has another profile | CoA with the speed of the next profile |
| A traffic or time limit is reached, and the user has no other profile | Disconnect |
| The user is disabled or removed | Disconnect |
| The user profile in use is removed, and the user has no other profile | Disconnect |
| `/user-manager/session/close-session` | Disconnect |
| `use-profiles=yes` is set and a connected user has no profile | Disconnect |
| `attributes` of a user or of a group | Nothing. The NAS gets the new attributes at the next login. |

- The request has User-Name, Acct-Session-Id, Framed-IP-Address and Calling-Station-Id of the session. With them, a RouterOS NAS finds PPP, HotSpot and DHCP sessions.
- The router login service of a NAS does not support these requests and answers with a NAK. After a CoA-NAK, User Manager sends a disconnect request, which is also refused, and the user stays logged in.

### When the NAS does not answer

User Manager sends a request three times, five seconds apart. When the NAS does not answer, the change does not reach the user: the user stays connected on the NAS with the old settings. `/user-manager/router/monitor` does not count an ACK or a NAK for the request. Check:

- `accept=yes` in `/radius/incoming` of the NAS, and the same port in `port` there and in `coa-port` of the router entry. The default is 3799.
- The firewall of the NAS accepts UDP on that port from User Manager.
- The NAS has User Manager in `/radius` with the address that the requests come from. The NAS checks a request with the secret of the first `/radius` entry whose address is the source address of the request, and does not answer requests from other addresses.
- User Manager sends the requests from the address that its routing selects for the NAS. When the User Manager router has several addresses, make sure the route to the NAS uses the address that the NAS has in `/radius`.

Then disconnect the user on the NAS. A PPP client connects again by itself, and a HotSpot user logs in again on the login page. The new session gets the current settings:

```ros
/ppp/active/remove [find name=mario]
/ip/hotspot/active/remove [find user=mario]
```

## Limit simultaneous sessions

`shared-users` of a user sets how many sessions the user can have at the same time. The default is 1.

```ros
/user-manager/user/set [find name=mario] shared-users=2
```

When the user is at the limit and logs in again, User Manager refuses the new login and disconnects the oldest session of the user. The next attempt of the new device is then accepted. The NAS must accept disconnect requests for this.

`override-shared-users` of a profile replaces the value of the user while the user has this profile.

## Restrict where a user connects from

`caller-id` of a user is compared with the Calling-Station-Id attribute of the request. For an L2TP user this is the address that the user connects from, for a PPPoE user and some other services it is a MAC address. A login from another address is refused.

```ros
/user-manager/user/set [find name=mario] caller-id=192.0.2.20
```

To remove the restriction, clear the value:

```ros
/user-manager/user/set [find name=mario] caller-id=""
```

## User names with a domain

User Manager compares the complete user name. A user who logs in as `luigi@example.net` must have this name in User Manager:

```ros
/user-manager/user/add name=luigi@example.net password=Luigi-Pass-1
/user-manager/user-profile/add user=luigi@example.net profile=home
```

```ros
[admin@MikroTik] > /user-manager/session/print where active
Flags: A - ACTIVE
4  A user=luigi@example.net acct-session-id="81300024" nas-port-type=ethernet
     nas-port-id="access" nas-ip-address=172.31.30.25 nas-identifier="nas1"
     calling-station-id="F6:34:B6:38:23:90" user-address=10.0.0.196
     status=start started=2026-11-26 09:06:52 uptime=0s download=0 upload=0
     last-accounting-packet=2026-11-26 09:06:52
```

- A login as `mario@example.net` is refused when only `mario` exists. The log has `username doesn't exist`.
- A RouterOS NAS sends a name in the form `EXAMPLE\mario` as `mario`, with `EXAMPLE` in the MS-CHAP-Domain attribute. User Manager then checks the user `mario`. `EXAMPLE\mario` and `OTHER\mario` are both the user `mario` in User Manager.

## Send the users of another realm to another server

A NAS can send the users of one domain (realm) to another RADIUS server, and all other users to User Manager. In this example the users of `partner.example` belong to a partner whose RADIUS server is 172.31.29.183. On the NAS, add the server of the partner before the User Manager entry:

```ros
/radius/add address=172.31.29.183 secret=Partner-Secret-1 \
    service=ppp domain=partner.example \
    place-before=[find address=172.31.30.195]
```

The NAS uses the first entry that matches the user, and an entry with an empty `domain` matches every user. When the User Manager entry is first, User Manager refuses the users of the partner, and the NAS does not ask the next server.

```ros
[admin@MikroTik] > /radius/print
Columns: SERVICE, DOMAIN, ADDRESS
# SERVICE  DOMAIN           ADDRESS      
0 ppp      partner.example  172.31.29.183
1 ppp                       172.31.30.195
```

The user `mario@partner.example` logs in through the server of the partner. The partner server gets the complete name, with the domain:

```ros
[admin@MikroTik] > /ppp/active/print where name=mario@partner.example
Flags: R - RADIUS
Columns: NAME, SERVICE, CALLER-ID, ADDRESS, UPTIME
#   NAME                   SERVICE  CALLER-ID          ADDRESS     UPTIME
1 R mario@partner.example  pppoe    3A:64:9B:7C:74:6B  10.0.0.195  9s
```

```ros
[admin@MikroTik] > /radius/monitor [find domain=partner.example] once
               pending: 0
              requests: 3
               accepts: 1
               rejects: 0
            challenges: 0
  accounting-responses: 2
         other-replies: 0
               resends: 0
              timeouts: 0
           bad-replies: 0
      last-request-rtt: 10ms
```

- The partner server must have the NAS as a client with the same secret.
- The accounting of the session goes to the same entry as the login.
- When the server of the partner does not answer, the NAS asks the next matching entry. The User Manager entry then gets the request with the complete name, and the user can log in only when User Manager has a user with this name.
- Add the entry on every NAS that the users of the partner connect to. User Manager does not forward requests to other servers.
- `realm` of a `/radius` entry sets the Mikrotik-Realm attribute in its requests, for example to tell the partner which network the user comes from. The user name does not change. User Manager does not use the attribute.
- For HotSpot, `radius-default-domain` of the HotSpot server profile sends all logins of the profile to the entry with the same `domain`, also names with another domain. The name is sent as the user typed it, and MS-CHAP-Domain and Mikrotik-Realm have the default domain.

:::warning
The NAS accepts change and disconnect requests from every server in `/radius`, for every session. The server of the partner can also change and disconnect the sessions of the users of User Manager. Add only servers that you trust.
:::

## Use one-time passwords

With `otp-secret`, a user must add a time-based one-time password (TOTP) to the password. The code has six digits and changes every 30 seconds.

```ros
/user-manager/user/add name=luigi password=Luigi-Pass-2 \
    otp-secret=JBSWY3DPEHPK3PXP
/user-manager/user-profile/add user=luigi profile=home
```

- `otp-secret` is the key in Base32 format, as authenticator applications such as Google Authenticator use it. Enter the same key in the application.
- The user types the password and the code together. When the application shows 620872, luigi logs in with `Luigi-Pass-2620872`.
- The password alone is refused, and a code works for one login only.
- The codes depend on the time. Set the [clock](../system-information-and-utilities/clock) of the User Manager router correctly, for example with an NTP client.

### Log in to the router with a one-time password

This gives the router login a second factor. The example runs User Manager on the same router, so the address is 127.0.0.1.

Add the router to User Manager and add a user. The Mikrotik-Group attribute sets the [user group](user) of the login:

```ros
/user-manager/set enabled=yes
/user-manager/router/add name=local address=127.0.0.1 \
    shared-secret=Radius-Secret-2
/user-manager/user/add name=carol password=Carol-Pass-1 \
    otp-secret=JBSWY3DPEHPK3PXP attributes=Mikrotik-Group:full
/user-manager/user-profile/add user=carol profile=home
```

Let the router login use RADIUS:

```ros
/radius/add address=127.0.0.1 secret=Radius-Secret-2 service=login
/user/aaa/set use-radius=yes
```

- The router checks its local users first. It asks RADIUS only for a name that is not a local user.
- Without the Mikrotik-Group attribute, the user gets the group in `default-group` of `/user/aaa`.
- A local account logs in without a code. Keep one local administrator account with a strong password: it is the way in when User Manager does not answer or the clock is wrong.

Add the key to an authenticator application. To log in, type the password and the code that the application shows:

![An authenticator application shows the six-digit code for 192.168.88.1 and the seconds until it changes](./img/user-manager-authenticator-code.jpg)

## Create many users at once

`add-batch-users` creates users with random names and passwords. This creates three users with six lowercase letters as the name and a password of eight letters and digits, and gives them a profile:

```ros
/user-manager/user/add-batch-users number-of-users=3 \
    username-length=6 username-characters=lowercase \
    password-length=8 \
    password-characters=lowercase,numbers,uppercase \
    profile=trial comment=guests
```

`username-prefix` starts all the names with the same text.

## Export and print user credentials

`generate-voucher` writes the names and passwords of users to a file from a template. The templates are in the folder `um5files/PRIVATE/TEMPLATES/vouchers` of the router:

- `printable_vouchers.html` makes a page of cards to print.
- `export.csv` and `export.xml` make a list for another program.

```ros
/user-manager/user/generate-voucher \
    voucher-template=printable_vouchers.html [find comment=guests]
/user-manager/user/generate-voucher voucher-template=export.csv \
    [find]
```

The files are written to `um5files/PRIVATE/GENERATED/vouchers` with `gen_` before the name of the template. The CSV file has one line for each user:

```text
Login,Password
"mario","Mario-Pass-1"
"rriieu","s3W4t9kt"
"ysdlre","syCVSvKO"
"vqbnad","OGs4Ca7C"
```

By default, each user gets a card with the user name, the password and the name of the profile:

![Three printable vouchers with the MikroTik logo, the user name, the password, the profile name trial and the text "If you want to extend time, please contact reception"](./img/user-manager-printable-vouchers.png)

The files can be copied from the router as any other [file](../system-information-and-utilities/files), or opened in a web browser at `/um/PRIVATE/GENERATED/vouchers/`. The web server refuses the `PRIVATE` folder until a name and a password are set:

```ros
/user-manager/advanced/set web-private-username=report \
    web-private-password=Report-Pass-1
```

The templates can be changed. They can use these variables:

- `$(username)` - the name of the user.
- `$(password)` - the password of the user.
- `$(userprofname)` - the profile that the user has now.
- `$(userprofendtime)` - the time when the profile ends, if it has an end.

## Generate a usage report

`generate-report` writes the sessions to a file, for example for billing. The template `report_default.html` is in `um5files/PRIVATE/TEMPLATES/reports`:

```ros
/user-manager/generate-report report-template=report_default.html \
    columns=username,uptime,download,upload
```

The report is written to `um5files/PRIVATE/GENERATED/reports/gen_report_default.html`. In a web browser it is at `/um/PRIVATE/GENERATED/reports/gen_report_default.html`.

![A usage report with the user name, uptime, download and upload columns](./img/user-manager-04.webp)

## See and close sessions

`/user-manager/session` has the active and the finished sessions with their counters. `status` shows which accounting messages were received:

- `start`, `interim`, `stop` - the accounting messages of the session.
- `close-acked` - the session is closed. A closed session can also have `expired`.

`terminate-cause` shows why a session ended: for example `user-request` when the user disconnected, `um-limits-reached` when a limit was reached, `um-user-disabled` when the user was disabled, and `um-admin-request` after `close-session` (`admin-reset` for a HotSpot session).

To disconnect a user, close the session. The NAS must accept disconnect requests:

```ros
/user-manager/session/close-session [find user=mario active]
```

`/user-manager/user/monitor` shows the totals of a user, and `/user-manager/router/reset-counters` clears the counters of a router.

## Web page for users

Each user can open a web page to see the statistics of the account and the profiles. The page is at `/um/` of the User Manager router, for example `http://172.31.30.195/um/`. It uses the `www` and `www-ssl` [services](../system-information-and-utilities/services) of the router.

The page can be changed. Its files are in the folder `um5files`:

| File | Description |
| :-- | :-- |
| **css/login.css** | Style sheet of the login page. |
| **css/user.css** | Style sheet of the page of the user. |
| **img/PayPal\_mark\_37x23.gif** | PayPal logo. |
| **img/ajax-loader.gif** | Image that is shown while a page loads. |
| **img/mikrotik\_logo.png** | MikroTik logo that is shown on all pages. |
| **js/generic.js** | JavaScript file of all pages. |
| **js/login.js** | JavaScript file of the login page. |
| **js/user.js** | JavaScript file of the page of the user. |
| **user/login\_dynamic.html** | Layout of the login page. |
| **user/user\_dynamic.html** | Layout of the page of the user. |

### Sell profiles

Users can buy a profile on the web page and pay with PayPal. Set the PayPal API account in `/user-manager/advanced` (`paypal-allow`, `paypal-user`, `paypal-password`, `paypal-signature`, `paypal-currency`) and give the profile a `price`.

A profile with a price has the button **Buy this Profile**:

![The profile list with the Buy this Profile button](./img/user-manager-05.webp)

The user continues on the PayPal page, selects how to pay and confirms with **Pay Now**:

![The PayPal checkout page with the PayPal balance and a card to pay with, and the Pay Now button](./img/user-manager-06.webp)

When the payment is completed, User Manager asks PayPal to approve it. After the approval the profile is given to the user.

![The purchased profile in the list of the user](./img/user-manager-07.webp)

`/user-manager/payment` lists the payments. Only a payment with the status `approved` is complete. `paypal-use-sandbox=yes` uses the test environment of PayPal.

## Back up and move the database

User Manager keeps its users, profiles, routers, sessions and payments in its own database, in the folder set with `db-path` of `/user-manager/database`.

- The system [backup](../getting-started/configuration-management/backup) and `/export` of the router do not include the database.
- `enabled` and `db-path` are part of the router configuration, not of the database. A configuration reset changes them.
- Save the database before and after large changes.

```ros
/user-manager/database/save name=um-backup
```

This writes the file `um-backup.umb`. `overwrite=yes` replaces a file that exists. To restore, also on another router, copy the file to the router and load it:

```ros
/user-manager/database/load name=um-backup
```

`load` replaces the database with the saved one. `/user-manager/database/optimize-db` compacts the database file.

On a new router, install the `user-manager` package and set `enabled=yes` as well: these are not in the saved file. If the address of the User Manager router changes, change it in the `/radius` entry of each NAS.

### Migrate from RouterOS v6

After an upgrade from RouterOS v6, User Manager starts with a new, empty database. To convert the old one, the folder of the old User Manager (`user-manager`) with all its files must be on the router. The folder can be renamed or copied to another router.

```ros
/user-manager/database/migrate-legacy-db \
    database-path=user-manager
```

The command converts the users, profiles, user profiles, limitations, profile limitations, user counters, routers and sessions. `overwrite=yes` replaces the current database.

## L2TP/IPsec server with User Manager on the same router

In this example one router is the L2TP/IPsec server and runs User Manager for its users. It is a separate router with a new configuration, not the routers of the earlier examples.

![Two clients connect over the internet to the router with L2TP/IPsec tunnels](./img/user-manager-08.webp)

Enable User Manager, add the router itself as a NAS, and add a user:

```ros
/user-manager/set enabled=yes
/user-manager/router/add name=local address=127.0.0.1 \
    shared-secret=Radius-Secret-2
/user-manager/user/add name=user1 password=Example-pass-1
```

Add the RADIUS client with the same secret and let PPP use it:

```ros
/radius/add address=127.0.0.1 secret=Radius-Secret-2 service=ppp
/radius/incoming/set accept=yes
/ppp/aaa/set use-radius=yes interim-update=1m
```

Add a pool for the users, set the addresses in the PPP profile, and enable the L2TP server with IPsec:

```ros
/ip/pool/add name=vpn-pool ranges=192.168.99.2-192.168.99.100
/ppp/profile/set default-encryption local-address=192.168.99.1 \
    remote-address=vpn-pool
/interface/l2tp-server/server/set enabled=yes use-ipsec=required \
    ipsec-secret=Example-ipsec-secret-1
```

The users of an L2TP/IPsec server are PPP users, so the service of the RADIUS client is `ppp`.

## Find why a login is refused

User Manager writes the reason to the log when the `manager` topic is logged:

```ros
/system/logging/add topics=manager action=memory
```

The log of the User Manager router then has a line for each refused request, for example `rejected for user: <guest1> no valid profile for this user`. Read it with `/log/print where topics~"manager"`.

| Reason in the log | What to check |
| :-- | :-- |
| `username doesn't exist` | The name is not in `/user-manager/user`. A name with a domain, such as `luigi@example.net`, must be added with the domain. |
| `Username or Password wrong.` | The name and the password. A user with `otp-secret` must add the current code to the password. |
| `OTP already used` | The code of a one-time password works for one login. Wait for the next code. |
| `no valid profile for this user` | `use-profiles=yes` is set and the user has no profile, or the validity of the profile is over. |
| `Uptime limit reached`, `Transfer limit reached` | The user reached a limit of the limitation. Give the user another profile, or wait for the counters to be cleared. |
| `simultaneous user session limit reached` | The user has `shared-users` sessions. User Manager disconnects the oldest one, and the next attempt is accepted. |

A login is also refused when the method of the request is not in `outer-auths` of the group of the user, and at a time that no limitation of the profile covers.

## Predefined attributes

These attributes exist in `/user-manager/attribute` after the installation. Vendor 14988 is MikroTik. [RADIUS](radius) explains the attributes.

| Attribute | Vendor ID | Type ID | Value type |
| :-- | :-- | --: | :-- |
| Framed-IP-Address | 0 (standard) | 8 | ip-address |
| Framed-IP-Netmask | 0 (standard) | 9 | ip-address |
| Session-Timeout | 0 (standard) | 27 | uint32 |
| Idle-Timeout | 0 (standard) | 28 | uint32 |
| Tunnel-Type | 0 (standard) | 64 | uint32 |
| Tunnel-Medium-Type | 0 (standard) | 65 | uint32 |
| Tunnel-Private-Group-ID | 0 (standard) | 81 | string |
| Acct-Interim-Interval | 0 (standard) | 85 | uint32 |
| Framed-Pool | 0 (standard) | 88 | string |
| Framed-IPv6-Prefix | 0 (standard) | 97 | ip6-prefix |
| Framed-IPv6-Pool | 0 (standard) | 100 | string |
| Delegated-IPv6-Prefix | 0 (standard) | 123 | ip6-prefix |
| Framed-IPv6-Address | 0 (standard) | 168 | ip-address |
| Mikrotik-Recv-Limit | 14988 | 1 | uint32 |
| Mikrotik-Xmit-Limit | 14988 | 2 | uint32 |
| Mikrotik-Group | 14988 | 3 | string |
| Mikrotik-Wireless-Forward | 14988 | 4 | uint32 |
| Mikrotik-Wireless-Skip-Dot1x | 14988 | 5 | uint32 |
| Mikrotik-Wireless-Enc-Algo | 14988 | 6 | uint32 |
| Mikrotik-Wireless-Enc-Key | 14988 | 7 | string |
| Mikrotik-Rate-Limit | 14988 | 8 | string |
| Mikrotik-Realm | 14988 | 9 | string |
| Mikrotik-Host-IP | 14988 | 10 | ip-address |
| Mikrotik-Mark-Id | 14988 | 11 | string |
| Mikrotik-Advertise-URL | 14988 | 12 | string |
| Mikrotik-Advertise-Interval | 14988 | 13 | uint32 |
| Mikrotik-Recv-Limit-Gigawords | 14988 | 14 | uint32 |
| Mikrotik-Xmit-Limit-Gigawords | 14988 | 15 | uint32 |
| Mikrotik-Wireless-PSK | 14988 | 16 | string |
| Mikrotik-Total-Limit | 14988 | 17 | uint32 |
| Mikrotik-Total-Limit-Gigawords | 14988 | 18 | uint32 |
| Mikrotik-Address-List | 14988 | 19 | string |
| Mikrotik-Wireless-MPKey | 14988 | 20 | string |
| Mikrotik-Wireless-Comment | 14988 | 21 | string |
| Mikrotik-Delegated-IPv6-Pool | 14988 | 22 | string |
| Mikrotik-DHCP-Option-Set | 14988 | 23 | string |
| Mikrotik-DHCP-Option-Param-STR1 | 14988 | 24 | string |
| Mikrotik-DHCP-Option-Param-STR2 | 14988 | 25 | string |
| Mikrotik-Wireless-VLANID | 14988 | 26 | uint32 |
| Mikrotik-Wireless-VLANIDtype | 14988 | 27 | uint32 |
| Mikrotik-Wireless-Minsignal | 14988 | 28 | string |
| Mikrotik-Wireless-Maxsignal | 14988 | 29 | string |
| Mikrotik-Switching-Filter | 14988 | 30 | string |

All predefined attributes are sent in Access-Accept messages. `packet-types` of an attribute can add Access-Challenge.

Values of Tunnel-Type ([RFC 2868](https://tools.ietf.org/html/rfc2868)):

| Value | Description |
| --: | :-- |
| 1 | Point-to-Point Tunneling Protocol (PPTP) |
| 2 | Layer Two Forwarding (L2F) |
| 3 | Layer Two Tunneling Protocol (L2TP) |
| 4 | Ascend Tunnel Management Protocol (ATMP) |
| 5 | Virtual Tunneling Protocol (VTP) |
| 6 | IP Authentication Header in the Tunnel-mode (AH) |
| 7 | IP-in-IP Encapsulation (IP-IP) |
| 8 | Minimal IP-in-IP Encapsulation (MIN-IP-IP) |
| 9 | IP Encapsulating Security Payload in the Tunnel-mode (ESP) |
| 10 | Generic Route Encapsulation (GRE) |
| 11 | Bay Dial Virtual Services (DVS) |
| 12 | IP-in-IP Tunneling |
| 13 | Virtual LAN |

Values of Tunnel-Medium-Type:

| Value | Description |
| --: | :-- |
| 1 | IPv4 (IP version 4) |
| 2 | IPv6 (IP version 6) |
| 3 | NSAP |
| 4 | HDLC (8-bit multidrop) |
| 5 | BBN 1822 |
| 6 | 802 (includes all 802 media plus Ethernet "canonical format") |
| 7 | E.163 (POTS) |
| 8 | E.164 (SMDS, Frame Relay, ATM) |
| 9 | F.69 (Telex) |
| 10 | X.121 (X.25, Frame Relay) |
| 11 | IPX |
| 12 | Appletalk |
| 13 | Decnet IV |
| 14 | Banyan Vines |
| 15 | E.164 with NSAP format subaddress |

## Read more

- [`/user-manager`](../cli-reference/user-manager/), [`/user-manager/user`](../cli-reference/user-manager/user/), [`/user-manager/user/group`](../cli-reference/user-manager/user/group), [`/user-manager/router`](../cli-reference/user-manager/router/), [`/user-manager/session`](../cli-reference/user-manager/session/)
- [`/user-manager/limitation`](../cli-reference/user-manager/limitation), [`/user-manager/profile`](../cli-reference/user-manager/profile), [`/user-manager/profile-limitation`](../cli-reference/user-manager/profile-limitation), [`/user-manager/user-profile`](../cli-reference/user-manager/user-profile/)
- [`/user-manager/attribute`](../cli-reference/user-manager/attribute), [`/user-manager/database`](../cli-reference/user-manager/database/), [`/user-manager/advanced`](../cli-reference/user-manager/advanced), [`/user-manager/payment`](../cli-reference/user-manager/payment)
- [RADIUS](radius)
- [PPP AAA](ppp-aaa)
- [Dot1X](dot1x)
- [Enterprise wireless security with User Manager](../wireless/user-guides/enterprise-wireless-security-user)
- [Enterprise Wi-Fi and MAC authentication with User Manager](../wireless/wifi/configuring-enterprise-and-mac-authentication)
