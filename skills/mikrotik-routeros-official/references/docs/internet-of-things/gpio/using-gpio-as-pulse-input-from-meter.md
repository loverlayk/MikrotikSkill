# Using the GPIO as pulse input from a meter device

> Use a MikroTik device's GPIO as a pulse input to read water, energy, or other meters, with a RouterOS script that counts the pulses.

Some water, energy or other meters have pulse outputs. The specification of the meter describes how many pulses represents one integer measurement unit. For example, the energy meter we used to create this manual generates 1000 pulses to represent 1kWh, so each pulse is 1Wh. You can use the digital GPIO input of the KNOT (pin5) to read these pulses and count the energy consumed behind the energy meter. In order to do so, it requires to create a simple MOSFET schematic and connect everything as in the following image:

![](./img/circuit.png)

The next step is to write a RouterOS script that is executed on every pulse received:

```bash
/iot gpio digital
set pin5 script=":global scriptRunning; :global pulse;\
:if (\$scriptRunning!=true) do={\
:set \$scriptRunning true;\
:set \$pulse (\$pulse+1);\
:log info message=(\"GPIO pulse No. \".\$pulse);\
:delay 1s;\
:set \$scriptRunning false;\
}"
```

When the GPIO is configured, the script above will create an log entry on each pulse:

```bash
15:32:22 script,info GPIO pulse No. 1 
15:38:01 script,info GPIO pulse No. 2 
15:43:38 script,info GPIO pulse No. 3 
15:49:15 script,info GPIO pulse No. 4 
15:54:51 script,info GPIO pulse No. 5 
16:00:27 script,info GPIO pulse No. 6 
16:06:02 script,info GPIO pulse No. 7 
16:11:37 script,info GPIO pulse No. 8 
16:17:12 script,info GPIO pulse No. 9 
16:22:48 script,info GPIO pulse No. 10 
```
