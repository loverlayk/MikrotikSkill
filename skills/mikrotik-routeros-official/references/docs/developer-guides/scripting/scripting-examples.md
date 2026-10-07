# Scripting examples

> This page provides scripting examples for MikroTik RouterOS, demonstrating how to create and modify files, append text, check IP changes, strip netmasks, and resolve hostnames using RouterOS scripting commands.

# Scripting examples

It is not possible to create a file directly; however, you can use the following workaround:

```ros
/file print file=myFile
/file set myFile.txt contents=""
```

## Append text to a file in a new line

There is no direct way to append text to a file; you can store the old content and append a new line with the additional text:

```ros
:local oldText [/file get myFile.txt contents as-string]
:local addText "test append"
:local newText ($oldText."\n".$addText)
/file set myFile.txt contents=$newText
```

## Check if IP on the interface has changed

Some providers assign dynamic IP addresses. This script compares the new address to the current one.

```ros
:global currentIP;

:local newIP [/ip address get [find interface="ether1"] address];

:if ($newIP != $currentIP) do={
    :put "ip address $currentIP changed to $newIP";
    :set currentIP $newIP;
}
```

## Strip netmask

This script is useful when you need an IP address without a netmask (for example, to use in a firewall), because `/ip address get [id] address` returns both the address and its netmask.

```ros
:global ipaddress 10.1.101.1/24

:for i from=( [:len $ipaddress] - 1) to=0 do={
	:if ( [:pick $ipaddress $i] = "/") do={
		:put [:pick $ipaddress 0 $i]
	}
}
```

A much simpler way is:

```ros
:global ipaddress 10.1.101.1/24
:put [:pick $ipaddress 0 [:find $ipaddress "/"]]
```

## Resolve host name

Many users request the ability to use DNS names instead of IP addresses for RADIUS servers, firewall rules, etc.

Here is an example that resolves the RADIUS server's IP.

Assume the RADIUS server is configured as follows:

```ros
/radius
add address=3.4.5.6 comment=myRad
```

The following script resolves the server's IP address, compares the result with the configured value, and replaces it if they differ:

```ros
/system script add name="resolver" source= {

:local resolvedIP [:resolve "server.example.com"];
:local radiusID [/radius find comment="myRad"];
:local currentIP [/radius get $radiusID address];

:if ($resolvedIP != $currentIP) do={
   /radius set $radiusID address=$resolvedIP;
   /log info "radius ip updated";
}

}
```

Add this script to the scheduler to run every five minutes, for example.

```ros
/system scheduler add name=resolveRadiusIP on-event="resolver" interval=5m
```

## Write simple queue stats in multiple files

Assume queue names use the format `some text.1` so you can search by the number after the dot.

```ros
:local entriesPerFile 10;
:local currentQueue 0;
:local queuesInFile 0;
:local fileContent "";
#determine needed file count
:local numQueues [/queue simple print count-only] ;
:local fileCount ($numQueues / $entriesPerFile);
:if ( ($fileCount * $entriesPerFile) != $numQueues) do={
   :set fileCount ($fileCount + 1);
}

#remove old files
/file remove [find name~"stats"];

:put "fileCount=$fileCount";

:for i from=1 to=$fileCount do={
#create file
   /file print file="stats$i.txt";
#clear content
   /file set [find name="stats$i.txt"] contents="";

   :while ($queuesInFile < $entriesPerFile) do={
     :if ($currentQueue < $numQueues) do={
         :set currentQueue ($currentQueue +1);
         :put $currentQueue ;
         /queue simple
         :local internalID [find name~"\\.$currentQueue\$"];
         :put "internalID=$internalID";
         :set fileContent ($fileContent . [get $internalID target-address] . \
           " " . [get $internalID total-bytes] . "\r\n");
     }
     :set queuesInFile ($queuesInFile +1);

   }
   /file set "stats$i.txt" contents=$fileContent;
   :set fileContent "";
   :set queuesInFile 0;

}

```

## Generate backup and send it by e-mail

This script generates a backup file and sends it to a specified e-mail address. The mail subject contains the router's name, current date, and time.

Note that the SMTP server must be configured before this script can be used. See [/tool e-mail](../../system-information-and-utilities/e-mail.md) for configuration options.

```ros
/system backup save name=email_backup
/tool e-mail send file=email_backup.backup to="me@test.com" body="See attached file" \
   subject="$[/system identity get name] $[/system clock get time] $[/system clock get date] Backup"
```

:::warning
The backup file contains sensitive information like passwords. Therefore, the script or scheduler must have a 'sensitive' policy to access generated backup files.
:::

## Use String as a Function

```ros
:global printA [:parse ":local A; :put \$A;" ];
$printA
```

## Check bandwidth and add limitations

This script checks whether download on an interface exceeds 512 kbps; if it does, the script adds a queue limiting speed to 256 kbps.

```ros
:foreach i in=[/interface find] do={
    /interface monitor-traffic $i once do={
        :if ($"received-bits-per-second" > 0 ) do={
            :local tmpIP [/ip address get [/ip address find interface=$i] address] ;
#            :log warning $tmpIP ;
            :for j from=( [:len $tmpIP] - 1) to=0 do={
                :if ( [:pick $tmpIP $j] = "/") do={
                    /queue simple add name=$i max-limit=256000/256000 dst-address=[:pick $tmpIP 0 $j] ;
                }
            }
        }
    }
}
```

## Block access to specific websites

This script is useful when you want to block certain websites without using a web proxy.

This example looks at entries "Rapidshare" and "youtube" in the DNS cache and adds IPs to the address list named "restricted". Before you begin, you must set up a router to catch all DNS requests:

```ros
/ip firewall nat
add action=redirect chain=dstnat comment=DNS dst-port=53 protocol=tcp to-ports=53
add action=redirect chain=dstnat dst-port=53 protocol=udp to-ports=53
```

Then add a firewall rule:

```ros
/ip firewall filter
add chain=forward dst-address-list=restricted action=drop
```

Write a script and schedule it to run every 30 seconds.

Script code:

```ros
:foreach i in=[/ip dns cache find] do={
    :local bNew "true";
    :local cacheName [/ip dns cache all get $i name] ;
#    :put $cacheName;

    :if (([:find $cacheName "rapidshare"] >= 0) || ([:find $cacheName "youtube"] >= 0)) do={

        :local tmpAddress [/ip dns cache get $i address] ;
#	:put $tmpAddress;

# if address list is empty do not check
        :if ( [/ip firewall address-list find list="restricted" ] = "") do={
            :log info ("added entry: $[/ip dns cache get $i name] IP $tmpAddress");
            /ip firewall address-list add address=$tmpAddress list=restricted comment=$cacheName;
        } else={
            :foreach j in=[/ip firewall address-list find list="restricted"] do={
                :if ( [/ip firewall address-list get $j address] = $tmpAddress ) do={
                    :set bNew "false";
                }
            }
            :if ( $bNew = "true" ) do={
                :log info ("added entry: $[/ip dns cache get $i name] IP $tmpAddress");
                /ip firewall address-list add address=$tmpAddress list=restricted comment=$cacheName;
            }
        }
    }
}
```

## Parse file to add ppp secrets

This script requires that entries inside the file are in the following format:

username,password,local\_address,remote\_address,profile,service

For example:

```ros
janis,123,1.1.1.1,2.2.2.1,ppp_profile,myService
juris,456,1.1.1.1,2.2.2.2,ppp_profile,myService
aija,678,1.1.1.1,2.2.2.3,ppp_profile,myService
```

```ros
:global content [/file get [/file find name=test.txt] contents] ;
:global contentLen [ :len $content ] ;

:global lineEnd 0;
:global line "";
:global lastEnd 0;

:do {
       :set lineEnd [:find $content "\r\n" $lastEnd ] ;
       :set line [:pick $content $lastEnd $lineEnd] ;
       :set lastEnd ( $lineEnd + 2 ) ;

       :local tmpArray [:toarray $line] ;
	:if ( [:pick $tmpArray 0] != "" ) do={
	:put $tmpArray;
         /ppp secret add name=[:pick $tmpArray 0] password=[:pick $tmpArray 1] \
             local-address=[:pick $tmpArray 2] remote-address=[:pick $tmpArray 3] \
             profile=[:pick $tmpArray 4] service=[:pick $tmpArray 5];
}
} while ($lineEnd < $contentLen)
```

## Detect new log entry

This script checks whether a new log entry has been added to a particular buffer.

In this example, use PPPoE logs:

```ros
/system logging action
add name="pppoe"
/system logging
add action=pppoe topics=pppoe,info,!ppp,!debug
```

The log buffer looks like the following:

```ros
[admin@mainGW] > /log print where buffer=pppoe
13:11:08 pppoe,info PPPoE connection established from 00:0C:42:04:4C:EE
```

The following script detects when a new entry is added.

```ros
:global lastTime;

:global currentBuf [ :toarray [ /log find buffer=pppoe  ] ] ;
:global currentLineCount [ :len $currentBuf ] ;
:global currentTime [ :totime [/log get [ :pick $currentBuf ($currentLineCount -1) ] time   ] ];

:global message "";

:if ( $lastTime = "" ) do={
	:set lastTime $currentTime ;
	:set message [/log get [ :pick $currentBuf ($currentLineCount-1) ] message];

} else={
	:if ( $lastTime < $currentTime ) do={
		:set lastTime $currentTime ;
		:set message [/log get [ :pick $currentBuf ($currentLineCount-1) ] message];
	}
}
```

After detection, the new entry is saved in the `message` variable; you can later parse this variable for details such as a PPPoE client's MAC address.

## Allow use of [ntp.org](http://ntp.org) pool service for NTP

This script resolves the hostnames of two NTP servers, compares the result with the current NTP settings, and changes the addresses if they're different. This script is required as RouterOS does not allow hostnames to be used in the NTP configuration. Two scripts are used. The first defines system variables for use by the second script, which performs the work:

```ros
# System configuration script - "GlobalVars"

:put "Setting system globals";

# System name
:global SYSname [/system identity get name];

# E-mail address to send notifications to
:global SYSsendemail "mail@my.address";

# E-mail address to send notifications from
:global SYSmyemail "routeros@my.address";

# Mail server to use
:global SYSemailserver "1.2.3.4";

# NTP pools to use (check www.pool.ntp.org)
:global SYSntpa "0.uk.pool.ntp.org";
:global SYSntpb "1.uk.pool.ntp.org";
```

```ros
# Check and set NTP servers - "setntppool"

# We need to use the following globals which must be defined here even
# though they are also defined in the script we call to set them.
:global SYSname;
:global SYSsendemail;
:global SYSmyemail;
:global SYSemailserver;
:global SYSntpa;
:global SYSntpb;

# Load the global variables with the system defaults
/system script run GlobalVars

# Resolve the two ntp pool hostnames
:local ntpipa [:resolve $SYSntpa];
:local ntpipb [:resolve $SYSntpb];

# Get the current settings
:local ntpcura [:pick [/system/ntp/client/get servers] 0];
:local ntpcurb [:pick [/system/ntp/client/get servers] 1];

# Define a variable so we know if anything's changed.
:local bChange 0;

# Debug output
:put ("Old: " . $ntpcura . " New: " . $ntpipa);
:put ("Old: " . $ntpcurb . " New: " . $ntpipb);

# Change servers if required
:if ($ntpipa != $ntpcura || $ntpipb != $ntpcurb) do={
    :put "Changing NTP servers";
    /system/ntp/client/set servers="$ntpipa,$ntpipb";
    :set bChange 1;
    }

# If we've made a change, send an e-mail to say so.
:if (($bChange = 1)) do={
    :put "Sending e-mail.";
    /tool e-mail send \
        to=$SYSsendemail \
        subject=($SYSname . " NTP change") \
        from=$SYSmyemail \
        server=$SYSemailserver \
        body=("Your NTP servers have just been changed:\n\nPrimary:\nOld: " . $ntpcura . "\nNew: " \
          . $ntpipa . "\n\nSecondary\nOld: " . $ntpcurb . "\nNew: " . $ntpipb);
    }
```

Scheduler entry:

```ros
/system scheduler add \
  comment="Check and set NTP servers" \
  disabled=no \
  interval=12h \
  name=CheckNTPServers \
  on-event=setntppool \
  policy=read,write,test \
  start-date=1970-01-01 \
  start-time=16:00:00
```
