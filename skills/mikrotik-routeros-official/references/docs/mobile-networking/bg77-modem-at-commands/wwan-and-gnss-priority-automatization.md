# WWAN and GNSS priority automatization

> Cellular connection and GNSS can not work simultaneously (WWAN and GNSS Rx chains in the BG77 module share certain hardware blocks, meaning the module does not support concurrent operation of WWAN and GNSS.). That is...

# Overview

Cellular connection and GNSS can not work simultaneously (WWAN and GNSS Rx chains in the BG77 module share certain hardware blocks, meaning the module does not support concurrent operation of WWAN and GNSS.). That is why the ***at+qgpscfg="priority",(0-1)*** command was introduced. With the help of the command, you can manually change the priority for one or the other.

***at+qgpscfg="priority",0*** command sets the **highest priority for GNSS**.

***at+qgpscfg="priority",1*** command sets the **highest priority for LTE (WWAN)**.

In real-life applications, it is not very convenient to change the priority by hand and this is why, to automatically change the priority, we advise using the methods shown below.

:::info
 Starting with the 7.1rc3 firmware release, it is possible to check when is the last time that the device got NMEA data (GPS data). This information can be used for troubleshooting purposes. You can check this parameter in CLI with the command "system gps monitor once". "data-age" parameter is the one that demonstrates when was the last time that the device received an NMEA message.
:::

## Automatic switch to GNSS when no outgoing traffic is detected

Automation can be achieved using ppp profile "**on-down**" script, "**idle-timeout**" features and PPP interface "**dial on demand**" setting.

When implemented, BG77 modem will use cellular data when there is internet traffic present (during this time GNSS coordinates are not received), and will automatically enable GPS reception when there is no internet traffic detected.

**Idle-timeout** parameter specifies the amount of time after which the link will be terminated if there is no activity present.

**On-down** script field allows you to configure a script that will be run every time the PPP interface goes down (including after **idle-timeout** inactivity). The script will set modem's priority to GNSS reception.

**Dial-on-demand** will make sure that PPP interface tries to establish the connection only when there is outgoing traffic present (additionally, the modem will automatically set WWAN/cellular connection priority). This will make sure that after **idle-timeout** occurs, the connection is not automatically reestablished unless outgoing packets are detected.

By combining the three features, you can achieve the scenario, where:

- If you have outgoing traffic, PPP interface is going to be up (because of the "**dial on demand**") and the priority will be set to the cellular connection. PPP interface's modem initialization AT command (that is configured under PPP interface's `modem-init="AT+QGPSCFG="priority",1"` setting) for WWAN priority is sent. During this time, GPS coordinates will not be received.
- If no traffic is detected after "**idle-timeout**" inactivity window, the PPP interface will go down and, because of the "**dial on demand**" setting, it will not establish the connection until outgoing packets are detected. This is where "**on-down**" script is run that switches WWAN priority to GNSS priority.
In order to implement it, simply add a new PPP profile:

```ros
/ppp profile add idle-timeout=30s name=BG77 on-down="/interface ppp-client at-chat [find where modem-init=\"AT+QGPSCFG=\\\"priority\\\",1\"] input=\"AT+QGPSCFG=\\\"priority\\\",0\""
```

The example above, creates a new profile with the name "BG77", sets **idle-timeout** to 30 seconds, and enables the **on-down** script that will send GNSS priority AT command.

After that, make sure to apply this newly created profile onto the PPP interface:

```ros
/interface ppp-client set profile=BG77 0
```

And confirm that it was applied (`profile=BG77`):

```ros
/interface ppp-client print
Flags: X - disabled; R - running 
0 R name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=2 
apn="internet" pin="" user="" password="" profile=BG77 phone="" dial-command="ATDT" 
modem-init="AT+QGPSCFG="priority",1" null-modem=no dial-on-demand=yes add-default-route=yes 
default-route-distance=1 use-peer-dns=yes keepalive-timeout=30 allow=pap,chap,mschap1,mschap2 
```

## Switch to GNSS using scripts and scheduler

The script below should be configured with a scheduler. The scheduler will make sure that the script is initiated each ***x*** hours/minutes (whenever you need it).

```
:global lat
:global lon
:global spd
:global alt
/interface ppp-client set ppp-out1 disabled=yes
log info ("disabling WWAN to get GPS coordinates")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",0"
log info ("enabling priority for GPS")
###the time in the delay below is the time that the device will wait for to get the coordinate fix
delay 32000ms
log info ("reading GPS coordinates")
/system gps monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
:set $spd $("speed")
:set $alt $("altitude")
}
:set $spd [:pick $spd 0 [find $spd " km"]]
:set $alt [:pick $alt 0 [find $alt "m"]]
if ($lat != "none") do={\
log info ("enabling priority back to WWAN")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",1"
log info ("enabling WWAN")
/interface ppp-client set ppp-out1 disabled=no
delay 1000ms
###if dial on demand is enabled
###/ping 1.1.1.1 count=1
#the delay below waits for 5 seconds for the ppp connection to get established - this time can differ based on the signal strength
delay 5000ms
log info ("posting coordinates via fetch")
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
else={
log info ("could not read GPS coordinates...enabling back WWAN")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",1"
/interface ppp-client set ppp-out1 disabled=no
delay 1000ms
###if dial on demand is enabled
###/ping 1.1.1.1 count=1
}
```

If "dial on demand" is enabled, uncomment (remove "###" for) ping lines "/ping 1.1.1.1 count=1" in the script because without outgoing traffic →  ppp interface will not establish the connection.

What this script is going to do is it going to disable ppp interface, send the GNSS priority command and wait for 32 seconds until the device gets the coordinates (it is the time/period that is suggested for the Quectel modem to get the coordinate fix). You can alter this time based on your preference and signal strength. Each individual case might be unique. After a 32-second delay, if the coordinates were successfully received (if latitude does not equal "none" but equals any other value), the script will send a WWAN priority command, enable back the ppp interface, and use "/tool fetch" to post the coordinates to the configured HTTP server. If the coordinates were not received after a 32-second delay (if latitude is going to be "none"), the script is going to send WWAN priority command and enable back the ppp interface without posting any results.

Do not forget to alter the "/tool fetch" part of the script accordingly to your HTTP server configuration/requirement.

You can also use MQTT instead of HTTP post. In order to do that, change the "/tool fetch" part of the configuration from:

```
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
```

To MQTT:

```
/iot mqtt publish broker="AWS" topic="my/test/topic" message="{\
                                 \"lat\":$lat,\
                                  \"lng\":$lon,\
                                   \"speed\":$spd,\
                                    \"altitude\":$alt \                                
  }"}\
```

Alter the broker, topic, and message as you see fit. You can find more information on how to configure MQTT following the link.

For example, if the MQTT server/broker is AWS, the posted result would look like this:

![](./img/image2021-8-30_14-8-26.webp)

## Switch to GNSS when no outgoing traffic is detected using scripts and scheduler

The 1st script is used to check whether there is any traffic and to switch the priority back and forth based on that.

The 2nd script can be used to enable WWAN priority and to publish the GPS coordinates to the server of your choice. You can use any supported protocol, like HTTPS post (fetch) or MQTT to post the coordinates.

### 1st script

This script below will automatically create a scheduler:

```
/system scheduler
add name="GPS/WWAN enabler" on-event=":delay 30s\r\
    \n\r\
    \n:local pppName ppp-out1\r\
    \n:local pppModemInitInit \"AT+QGPSCFG=\\\"priority\\\",1\"\r\
    \n:local gpsCmd \"AT+QGPSCFG=\\\"priority\\\",0\"\r\
    \n:local idleCount 5\r\
    \n\r\
    \n\r\
    \n:local pppStats\r\
    \n:local pppStatsPrev\r\
    \n:local pppStatsReset\r\
    \n:local idleCounter\r\
    \n\r\
    \n:while (true) do={\r\
    \n\r\
    \n:if ( \\\r\
    \n  [/interface ppp-client get \$pppName running] \\\r\
    \n  && [/system gps get enabled] \\\r\
    \n  && [/interface ppp-client get \$pppName dial-on-demand] \\\r\
    \n  && \$pppModemInitInit=[/interface ppp-client get \$pppName modem-init]\
    \_) \\\r\
    \n  do={\r\
    \n    :set pppStats [:toarray ([/interface print stats as-value where name\
    =ppp-out1]->0)] \r\
    \n    :if ( \\\r\
    \n      \$pppStats->\"rx-packet\"=\$pppStatsPrev->\"rx-packet\" \\\r\
    \n      && \$pppStats->\"tx-packet\"=\$pppStatsPrev->\"tx-packet\" ) \\\r\
    \n      do={\r\
    \n        :set idleCounter (\$idleCounter+1)\r\
    \n:put (\"debug: idle \".\$idleCounter)\r\
    \n        :if ( \\\r\
    \n          \$idleCounter>=\$idleCount \\\r\
    \n          && \$pppStats->\"rx-packet\"!=\$pppStatsReset->\"rx-packet\" \
    \\\r\
    \n          && \$pppStats->\"tx-packet\"!=\$pppStatsReset->\"tx-packet\" )\
    \_\\\r\
    \n          do={\r\
    \n            :set pppStatsReset \$pppStats\r\
    \n            :set idleCounter 0\r\
    \n            :log info (\$pppName.\" idling - reseting dial-on-demand, pr\
    ioritizing GPS\")\r\
    \n            /interface ppp-client set \$pppName disabled=yes\r\
    \n            :do { /interface ppp-client at-chat \$pppName input=\$gpsCmd\
    \_} \\\r\
    \n                on-error={\r\
    \n:put (\"debug: GPS at-chat error\")                \r\
    \n                  :set idleCounter 0\r\
    \n                  :set pppStatsReset ({})\r\
    \n                  }\r\
    \n            /interface ppp-client set \$pppName disabled=no\r\
    \n            }\r\
    \n          :delay 1s\r\
    \n        } \\\r\
    \n      else={\r\
    \n:put (\"debug: no idle\")      \r\
    \n        :set idleCounter 0\r\
    \n        :set pppStatsPrev \$pppStats\r\
    \n        :delay 1s \r\
    \n        }\r\
    \n    } \\\r\
    \n  else={\r\
    \n:put (\"debug: unsupported config\")\r\
    \n    :set idleCounter 0\r\
    \n    :set pppStatsReset ({})\r\
    \n    :delay 1s\r\
    \n    }\r\
    \n}" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup
```

Copy all the lines above and paste them into a new script. Run the script and you will create a "scheduler". You can check the "scheduler" under System>Scheduler>"GPS/WWAN enabler".

The raw script looks like this:

```
:local pppName ppp-out1
:local pppModemInitInit "AT+QGPSCFG=\"priority\",1"
:local gpsCmd "AT+QGPSCFG=\"priority\",0"
:local idleCount 5
:local pppStats
:local pppStatsPrev
:local pppStatsReset
:local idleCounter
:while (true) do={
:if ( \
  [/interface ppp-client get $pppName running] \
  && [/system gps get enabled] \
  && [/interface ppp-client get $pppName dial-on-demand] \
  && $pppModemInitInit=[/interface ppp-client get $pppName modem-init] ) \
  do={
    :set pppStats [:toarray ([/interface print stats as-value where name=ppp-out1]->0)] 
    :if ( \
      $pppStats->"rx-packet"=$pppStatsPrev->"rx-packet" \
      && $pppStats->"tx-packet"=$pppStatsPrev->"tx-packet" ) \
      do={
        :set idleCounter ($idleCounter+1)
:put ("debug: idle ".$idleCounter)
        :if ( \
          $idleCounter>=$idleCount \
          && $pppStats->"rx-packet"!=$pppStatsReset->"rx-packet" \
          && $pppStats->"tx-packet"!=$pppStatsReset->"tx-packet" ) \
          do={
            :set pppStatsReset $pppStats
            :set idleCounter 0
            :log info ($pppName." idling - reseting dial-on-demand, prioritizing GPS")
            /interface ppp-client set $pppName disabled=yes
            :do { /interface ppp-client at-chat $pppName input=$gpsCmd } \
                on-error={
:put ("debug: GPS at-chat error")                
                  :set idleCounter 0
                  :set pppStatsReset ({})
                  }
            /interface ppp-client set $pppName disabled=no
            }
          :delay 1s
        } \
      else={
:put ("debug: no idle")      
        :set idleCounter 0
        :set pppStatsPrev $pppStats
        :delay 1s 
        }
    } \
  else={
:put ("debug: unsupported config")
    :set idleCounter 0
    :set pppStatsReset ({})
    :delay 1s
    }
}
```

In order for the script to work, a few conditions must be met.

The first condition is that both ppp interface (Interfaces>Interface) and GPS (System>GPS) must be enabled and work simultaneously. You may need to disable ppp before enabling GPS because they both use the same serial port. When both GPS and ppp are enabled, make sure that the second condition is met.

The second condition is that AT command "***AT+QGPSCFG="priority",1***" is configured for the ppp interface under the "Modem Init" field:

![](./img/image2021-8-30_12-10-52.webp)

What this is going to do, is send a WWAN priority command whenever ppp connection gets successfully established.

Lastly, the third condition, is that "dial on demand" is enabled for the ppp interface:

![](./img/image2021-8-30_12-27-59.webp)

This is required because otherwise, when "dial on demand" is disabled → ppp interface will automatically send the AT command with a WWAN priority setting (attempt to establish the connection), whenever the port is enabled back on. When "dial on demand" is enabled → after the interface gets enabled back on, ppp connection will not be established and the AT command for WWAN priority will not be sent until outgoing packets are detected.

When all 3 conditions are met → the script is going to do the following:

The script is going to compare "counters" to figure out whether there is traffic present or not (based on Tx packets and Rx packets for the ppp interface). If there is no traffic, the "counter" goes up, and when it reaches the "idleCount", ppp interface is disabled, enabled back on, and the GNS priority command is sent. During this time, if there is still no outgoing traffic present, GPS coordinates should be updated (under System>GPS). As soon as any traffic is detected, the "counter" is reset and the WWAN priority command is sent by establishing ppp connection.

Once all 3 conditions are met and the scheduler is ready, reboot the device for the script to take action.

### 2nd script

The second script is used to collect GPS coordinates and send them further to the server.

```
:global lat
:global lon
:global spd
:global alt
/system gps monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
:set $spd $("speed")
:set $alt $("altitude")
}
:set $spd [:pick $spd 0 [find $spd " km"]]
:set $alt [:pick $alt 0 [find $alt "m"]]
:if ($lat != "none") do={
/ping 1.1.1.1 count=1
:delay 3000ms;
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL"}\
else={log info ("could not read GPS coordinates")}
```

The script is going to "read" GPS coordinates, and if latitude could be "read" successfully (if latitude does not equal "none" but equals any other value), ping "1.1.1.1" once (to generate outgoing traffic), wait for 3 seconds for the ppp connection to get established and initiate "/tool fetch" (HTTP post). Otherwise, if latitude could not be determined (when the script was initiated), nothing will happen (you will see a log message that the device could not read GPS coordinates).

You can change the "delay" line in the script to the actual time that it takes your device to successfully establish a ppp (CAT-M/NB-IoT) connection with the ISP.

You can set up a scheduler to run the script whenever you like.

The "/tool fetch" part of the script should be configured accordingly to your server settings.

You can also use MQTT instead of HTTP post. If you wish to do that, change the "/tool fetch" part, from:

```
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
```

To:

```
/iot mqtt publish broker="AWS" topic="my/test/topic" message="&#123;\
                                 \"lat\":$lat,\
                                  \"lng\":$lon,\
                                   \"speed\":$spd,\
                                    \"altitude\":$alt \                                  
  }"}\
```

Do not forget to alter the broker, topic, and message as you see fit. You can find more information on how to configure MQTT following the link.

For example, if the MQTT server is AWS, the result would look like this:

![](./img/image2021-8-30_14-8-26.webp)
