# Kid Control

> Kid Control limits the internet access of the devices of a child: allowed hours for each day of the week, a rate limit, and pause and resume. RouterOS identifies the devices by their MAC address.

# Kid Control

Kid Control is a parental control feature that limits the internet access of devices in the local network. You create a profile for each child with the hours of each day in which internet access is allowed, add the devices of the child to it, and the router blocks or limits these devices according to the profile.

A device is identified by its MAC address. The router takes the IP address of the device from the ARP table and adds firewall rules and queues for that address.

## Limit the devices of a child

This example creates a profile for Anna. Her devices get internet access from 16:00 to 20:00 on school days and from 9:00 to 21:00 at weekends, limited to 5 Mbps in each direction:

```ros
/ip/kid-control
add name=Anna mon=16h-20h tue=16h-20h wed=16h-20h thu=16h-20h \
    fri=16h-20h sat=9h-21h sun=9h-21h rate-limit=5M
```

Add each device of the child to the profile by its MAC address. Replace the MAC address of the example with the address of the device. The list `/ip/kid-control/device/print` shows the MAC addresses of the devices that the router has seen.

```ros
/ip/kid-control/device
add name=Tablet user=Anna mac-address=00:00:5E:00:53:63
```

Many phones and tablets use a private, random MAC address for each Wi-Fi network. If the address of a device changes, the profile no longer matches it: turn off the private address for your network on the device.

The profile has three kinds of settings:

- `mon`, `tue`, `wed`, `thu`, `fri`, `sat` and `sun` set the time of each day in which internet access is allowed. An empty value, such as `mon=""`, allows no access on that day. A day that you do not set keeps its default: 7h-21h from Monday to Thursday, 7h-22h on Friday, 6h-22h on Saturday and 6h-21h on Sunday.
- `rate-limit` limits the data rate of each device during the allowed time, in each direction.
- `tur-mon` to `tur-sun` set the time of each day in which the rate limit does not apply ("time unlimited rate"). These settings do not allow access by themselves: outside the allowed time of the day the devices stay blocked.

The time ranges use the clock of the router: check that `/system/clock` shows the right time and time zone.

Kid Control works with the IPv4 address of a device.

### Hours without a rate limit

This profile for Peter uses all three kinds of settings:

```ros
/ip/kid-control
add name=Peter mon="" tur-tue="00:00-24h" wed="" \
    tur-thu="11:00-22:00" fri="" sat="18:30-22:00" \
    tur-sun="15h-21h" rate-limit=3M
```

```ros
/ip/kid-control/device
add name=Mobile-phone user=Peter mac-address=00:00:5E:00:53:64
```

It gives Peter's phone this week:

- Monday, Wednesday and Friday: no access.
- Tuesday: access from 7:00 to 21:00, the default, without a rate limit.
- Thursday: access from 7:00 to 21:00, the default. The rate is limited to 3 Mbps until 11:00 and not limited after that.
- Saturday: access from 18:30 to 22:00, limited to 3 Mbps.
- Sunday: access from 6:00 to 21:00, the default. The rate is limited to 3 Mbps until 15:00 and not limited after that.

## Check the state

The profile list shows whether the devices of a child are blocked (`B`), rate-limited (`L`) or paused (`P`) now. The list shows the days that have a value; `print detail` shows all settings. This is Anna's profile on a Wednesday at 15:00, before the allowed time, and at 17:00:

```ros
/ip/kid-control/print
```

```text
Flags: B - BLOCKED
Columns: NAME, SUN, MON, TUE, WED, THU, FRI, SAT
#   NAME  SUN     MON      TUE      WED      THU      FRI      SAT   
0 B Anna  9h-21h  16h-20h  16h-20h  16h-20h  16h-20h  16h-20h  9h-21h
```

```text
Flags: L - RATE-LIMITED
Columns: NAME, SUN, MON, TUE, WED, THU, FRI, SAT
#   NAME  SUN     MON      TUE      WED      THU      FRI      SAT   
0 L Anna  9h-21h  16h-20h  16h-20h  16h-20h  16h-20h  16h-20h  9h-21h
```

This is Peter's profile on a Monday:

```ros
/ip/kid-control/print
```

```text
Flags: B - BLOCKED
Columns: NAME, SUN, TUE, THU, SAT
#   NAME   SUN     TUE     THU     SAT       
;;; Unlimited Rate does not grant access, it only changes the Rate Limit
0 B Peter  6h-21h  7h-21h  7h-21h  18h30m-22h
```

The line above the profile is a note from the router: a "time unlimited rate" range does not allow access by itself.

To see how much data each device has used, print the device statistics. The list also shows, with the `D` flag, the other devices that the router has seen. In this output, Peter's phone is rate-limited:

```ros
/ip/kid-control/device/print stats
```

```text
Flags: D - DYNAMIC, L - LIMITED
Columns: NAME, IDLE-TIME, RATE-DOWN, RATE-UP, BYTES-DOWN, BYTES-UP
#   NAME          IDLE-TIME  RATE-DOWN  RATE-UP  BYTES-DOWN  BYTES-UP
0 D               1m48s      0bps       0bps     0           1020    
1 D               0s         0bps       0bps     2892        1872    
2 D                          0bps       0bps     0           0       
3 D               1s         0bps       0bps     98.7KiB     132.8KiB
4 D                          0bps       0bps     0           0       
5 L Mobile-phone  0s         0bps       0bps     3240        3240    
```

To set the counters of a device back to zero, use `/ip/kid-control/device/reset-counters [find name=Mobile-phone]`.

## How the router blocks and limits

Kid Control adds dynamic firewall rules and queues. You do not have to add firewall rules yourself. The outputs in this section are from Peter's profile.

The router adds a rule with the comment "jump to kid-control rules" at the top of the `forward` chain of the firewall filter, and puts its rules into the `kid-control` chain. While a device is blocked, the chain has two rules that reject the packets from and to the device:

```ros
/ip/firewall/filter/print where dynamic and comment~"kid"
```

```text
Flags: D - DYNAMIC
0 D ;;; Mobile-phone, kid-control
    chain=kid-control action=reject src-address=10.0.0.2
 
1 D ;;; Mobile-phone, kid-control
    chain=kid-control action=reject dst-address=10.0.0.2
```

While a device is rate-limited, the router adds a dynamic simple queue for it:

```ros
/queue/simple/print where dynamic
```

```text
Flags: D - DYNAMIC
0 D ;;; Mobile-phone, kid-control
    name="queue1" target=10.0.0.2/32 parent=none packet-marks="" priority=8/8
    queue=default-small/default-small limit-at=3M/3M max-limit=3M/3M
    burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1
```

The `kid-control` chain then has rules that accept the established connections of the device. Because the jump rule is at the top of the `forward` chain, these rules come before the FastTrack rule of the default firewall.

## Pause and resume

To block all devices of a child immediately, whatever the schedule says, pause the profile. `resume` returns to the schedule.

```ros
/ip/kid-control/pause Anna
/ip/kid-control/print
```

```text
Flags: P - PAUSED, B - BLOCKED
Columns: NAME, SUN, MON, TUE, WED, THU, FRI, SAT
#   NAME  SUN     MON      TUE      WED      THU      FRI      SAT   
0 P Anna  9h-21h  16h-20h  16h-20h  16h-20h  16h-20h  16h-20h  9h-21h
```

```ros
/ip/kid-control/resume Anna
```

A disabled profile (`disabled=yes`) does not restrict its devices.

When you remove a profile, remove its devices from `/ip/kid-control/device` too: the router keeps the device entries, and they no longer belong to a profile.

All properties are described in the CLI reference of [`/ip/kid-control`](../cli-reference/ip/kid-control) and [`/ip/kid-control/device`](../cli-reference/ip/kid-control/device).
