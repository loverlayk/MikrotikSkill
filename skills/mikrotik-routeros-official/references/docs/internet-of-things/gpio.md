# GPIO

> GPIO allows configuring digital and analog input/output pins on MikroTik routers for tasks like voltage measurement, dry contact sensing, and relay control. Settings are managed via CLI under /iot/gpio with submenus...

# GPIO

***note**: In order to access GPIO settings, make sure that the **iot** [package](../../getting-started/installation-and-upgrade/packages) is installed beforehand.*

You can find more information about GPIO by following the [link](https://en.wikipedia.org/wiki/General-purpose_input/output).

GPIO stands for General-Purpose Input/Output. It is a digital signal pin/pins on the routerboard that allows you to send/receive the signal. It can be useful in different scenarios, like:

1. Measuring voltage through an ADC input.
2. Reading 0 and 1 signals received from another device - "dry contact".
3. Controlling connected relays by sending a logical 0 or 1 signal to the pin.

:::info
[KNOT](https://help.mikrotik.com/docs/spaces/UM/pages/41680915/RB924i-2nD-BT5+BG77), [KNOT Embedded LTE4](https://mikrotik.com/product/knot_embedded_lte4) and [RBM33G](https://help.mikrotik.com/docs/spaces/UM/pages/14222434/RBM33G) support GPIO functionality.

- [KNOT pinout can be found here](https://help.mikrotik.com/docs/spaces/UM/pages/41680915/RB924i-2nD-BT5+BG77#RB924i2nDBT5%26BG77-GPIOpinout).
- [KNOT embedded LTE 4 pinout, here.](https://help.mikrotik.com/docs/spaces/UM/pages/366477381/KNOT+Embedded+LTE4+EC25-EU+KNe#KNOTEmbeddedLTE4EC25EU%26KNe-GPIOpinout)
- [RBM33G pinout, here](https://help.mikrotik.com/docs/spaces/UM/pages/14222434/RBM33G#RBM33G-GPIOpinout).

:::

### RouterOS configuration

**GPIO settings are available only using the CLI.**

**Sub-menu:** `/iot/gpio`

GPIO settings are divided into:

- analog (/iot/gpio/analog)
- digital (/iot/gpio/digital)

:::warning
In our examples, we are using [KNOT](https://mikrotik.com/product/knot) as a reference device (with x2 analog input pins, x2 digital output pins and x1 digital input pin). Other devices may have a different pinout but the same principles apply.
:::

#### Analog pin

**Sub-menu:** `/iot/gpio/analog`

***note**:* please check on a product page whether your hardware supports analog input or not.

In the "analog" setting you can measure voltages on the analog input/ADC input pins:

```ros
[admin@device] /iot/gpio/analog> print
 # NAME                                                                                     VALUE       OFFSET
 0 pin2                                                                                       0mV          0mV
 1 pin3                                                                                      32mV          0mV
```

"OFFSET" can be used to manually compensate for voltage drop on the wires. "VALUE" is measured with `value = adc_input + offset`, where adc\_input is the voltage on the pin.

"OFFSET" configuration example is shown below:

```ros
[admin@device] /iot/gpio/analog> set pin2 offset  

Offset ::= [-]Num[mV]
  Num ::= -2147483648..2147483647    (integer number)

[admin@device] /iot/gpio/analog> set pin2 offset 2   
[admin@device] /iot/gpio/analog> print            
 # NAME                                                                                           VALUE       OFFSET
 0 pin2                                                                                             2mV          2mV
 1 pin3                                                                                             0mV          0mV 
```

#### Digital pin

**Sub-menu:** `/iot/gpio/digital`

In the "digital" section you can send/receive a logical 0 or 1 signal using the digital output/input pins (output pins are "open drain"):

```ros
[admin@device] /iot/gpio/digital> print             
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                   
 0   pin5                                        input     0      0    
 1   pin4                                        output    0     
 2   pin6                                        output    0     
```

"DIRECTION" for the pin can be either "input" (a pin that can receive the signal) or "output" (a pin that can send the signal).

:::info
[KNOT](https://mikrotik.com/product/knot) pins' "DIRECTION" for pin4 and pin6 cannot be changed. Both pins are meant to be used only as "output" pins.
:::

When the pin's direction is set to "output", you can configure the "OUTPUT" value. Changing the "OUTPUT" value sends the signal to the pin.

```ros
[admin@device] /iot/gpio/digital> set pin4 output=

Output ::= 0 | 1

[admin@device] /iot/gpio/digital> set pin4 output=1        
[admin@device] /iot/gpio/digital> print            
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                      
 0   pin5                                        input     0      0    
 1   pin4                                        output    1     
 2   pin6                                        output    0     
```

The "script" field allows you to configure a script that will be initiated whenever the "INPUT" or "OUTPUT" value changes (from 0 to 1 or from 1 to 0).

```ros
[admin@device] /iot/gpio/digital> set pin4 script=script1
[admin@device] /iot/gpio/digital> set pin5 script="/system .."   
[admin@device] /iot/gpio/digital> print                       
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                      
 0   pin5                                        input     0      0     /system ..                                  
 1   pin4                                        output    1            script1                                     
 2   pin6                                        output    0     
```

### Different scenarios

#### Controlling relays

One of the scenarios for the GPIO implementation is "controlling other relays" using digital output pins. Basically, sending a "0" or "1" signal to the unit that is connected to the pin. To automate the process, you can use a [scheduler](../../system-information-and-utilities/scheduler), which will run the script at specific times.

For example, you can add the first [script](../../developer-guides/scripting/) (a single line shown below) and name it "output=0":

```ros
/iot/gpio/digital set pin4 output=0
```

Then add a second script (a single line shown below) and name it "output=1":

```ros
/iot/gpio/digital set pin4 output=1
```

Having both scripts, you can configure a schedule:

```ros
[admin@device] /system/scheduler> add name=run-30s interval=30s on-event="output=0"
```

The schedule configuration shown above will run the script with the name "output=0" every 30 seconds.

```ros
[admin@device] /system/scheduler> add name=run-45s interval=45s on-event="output=1"
```

The schedule configuration shown above will run the script with the name "output=1" every 45 seconds.

As a result, the device will automatically send a signal to the 4th pin (digital output pin) with output value=0 every 30 seconds and a signal with output value=1 every 45 seconds.

You can change the scheduled time as you see fit (depending on the requirements).

#### Monitoring input signal

Another scenario is to "monitor input signal" using the digital input pins. You need a script that will initiate e-mail notification or MQTT/HTTPS (fetch) publish whenever the "INPUT" value changes for the pin with the direction="input" (whenever the RouterOS device receives a signal "0 or 1" from another device connected to the pin).

*E-mail notification script:*

```ros
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]" body="$[/iot/gpio/digital/get pin5 input]"
```

After creating a script, apply/set it to the "input" pin:

```ros
[admin@device] /iot/gpio/digital> set pin5 script=script1 
[admin@device] /iot/gpio/digital> print                  
Flags: X - disabled 
 #   NAME                     DIRECTION OUTPUT INPUT SCRIPT                    
 0   pin5                     input     0      0     script1                   
 1   pin4                     output    0            script1                   
 2   pin6                     output    0     
```

In the example above, the e-mail notification script is named "script1".

As a result, whenever the input value changes (from 0 to 1 or from 1 to 0), the script automatically initiates an e-mail notification that will display the input value in the e-mail body.

Do not forget to change the script line and configure the e-mail settings ([/tool/e-mail](../../system-information-and-utilities/e-mail) accordingly:

```ros
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]"  body="$[/iot/gpio/digital/get pin5 input]"
```

Configure the actual e-mail address that you use. You can also change the subject and the body of the mail as you see fit.

*MQTT publish script:*

```ros
:local broker "name"
:local topic "topic"
:local message "\{\"inputVALUE\":$[/iot/gpio/digital/get pin5 input]}"  
/iot/mqtt/publish broker=$broker topic=$topic message=$message
```

This script works the same way as the "*e-mail notification*" script, only when the input value changes, the script initiates MQTT publish (instead of e-mail notification) and sends the input value received on the pin in the JSON format.

Do not forget to set up an MQTT broker (*`/iot/mqtt/brokers/add` ..*) and alter a few script lines beforehand:

```ros
:local broker "name"
```

The broker's "name" should be changed accordingly (you can check all created brokers and their names using the CLI command /*iot mqtt brokers print*).

```ros
:local topic "topic"
```

The topic should be changed as well. The topic itself is configured on the server-side, so make sure that the correct topic is used.

Do not forget to apply/set the script to pin5 (/iot/gpio/digital/set pin5 script=script\_name), as shown in the "email notification" example above.

If the mechanical switch is used to send the signal to the GPIO pin, it is suggested to use the following script instead (in case the script is initiated more than once when the signal is received on the pin):

```ros
:global gpioscriptrunning;  
if (!$gpioscriptrunning) do=\{:set $gpioscriptrunning true;  
:log info "script started - GPIO changed";  
:do \{if ([/iot/gpio/digital/get pin5 input] = "0") do=\{/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]" body="pin5 received logical 0"} else \{/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]"  body="pin5 received logical 1"};  
:delay 1s;  
:set $gpioscriptrunning false} on-error=\{:set $gpioscriptrunning false;  
:log info "e-mail error, resetting script state..."}}
```

If the GPIO pin state changes more than once within milli/microseconds - the script above is going to make sure that e-mail notification is not sent more than once.

#### Monitoring voltage

Last but not least is to "monitor voltage" using the analog pins.  You need a script that will read/monitor voltage on schedule and then send the data via e-mail, MQTT or HTTPS (fetch).

Create a script, as shown below. In this example, we will be using MQTT publish (but you can create a similar script with "/tool/e-mail .." to use e-mail notifications):

```ros
:local broker "name"
:local topic "topic"
:local message "\{\"voltage(mV)\":$[/iot/gpio/analog/get pin3 value]}"  
/iot/mqtt/publish broker=$broker topic=$topic message=$message
```

The script will read/measure the voltage on pin3 and publish the data to the MQTT broker.

Do not forget to set up an MQTT broker (*`/iot/mqtt/brokers/add` ..*) and alter a few script lines beforehand:

```ros
:local broker "name"
```

The broker's "name" should be changed accordingly (you can check all created brokers and their names using the CLI command `/iot/mqtt/brokers/print`).

```ros
:local topic "topic"
```

The topic should be changed as well. The topic itself is configured on the server-side, so make sure that the correct topic is used.

Save the script and name it, for example, "voltagepublish". To automate the process, you can use the [scheduler](../../system-information-and-utilities/scheduler).

```ros
[admin@device] /system/scheduler> add name=run-45s interval=45s on-event="voltagepublish"
```

The schedule configuration shown above will run the script every 45 seconds.
