# Scripting Tips and Tricks

> This page provides scripting tips for MikroTik RouterOS, emphasizing the importance of using internal IDs instead of literal values to avoid errors when objects are renumbered. It explains how to correctly reference...

# Scripting Tips and Tricks

Let's start with the basics. When you work from the terminal, you are used to the following syntax for accessing parameters:

```text
[admin@r1] /interface> print
Flags: D - dynamic, X - disabled, R - running, S - slave
 #     NAME                                TYPE       ACTUAL-MTU L2MTU  MAX-L2MTU
 0  R  ether1                              ether            1500  1580      1022
[admin@r1] /interface> set 0 name=LAN

```

`print` command temporary saves buffer with id numbers referencing to internal ID numbers, so obviously if you are trying to use non-existent values script will fail, like, for example in this script:

```ros
/system script add name=script1 source={
  /ip route set 1 gateway=3.3.3.3
}

```

The script does not know what “1” refers to and throws an error. Proper way is to use internal ID numbers, those numbers can be seen if you are doing `print as-value` or returned by find command, for example:

```ros
[admin@r1] /ip route> :put [find where dst-address="10.0.0.0/8"]
*1

```

So in this case the proper script would be:

```ros
/system script add name=script1 source={
  /ip route set *1 gateway=3.3.3.3
}

```

Note that using internal numbers directly is not recommended, because items can be removed and re‑added; the internal ID then changes and the script will fail. Use the `find` command in your code instead:

```ros
/system script add name=script1 source={
  /ip route set [find dst-address="0.0.0.0/0"] gateway=3.3.3.3
}

```

## Why find does not work even if correct value is specified?

Let's say we want to print a specific address:

```text
[admin@r1] /ip address> print where address=111.111.1.1/24
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE

```

We know that such an address exists, so why is there no output?

Because the scripting engine tries to convert variable types as aggressively as it can, but it does not always succeed. Let's look closely at why this particular example fails. First, let's check what variable type the `address` is:

```text
[admin@r1] /ip address> :put [:typeof ([print as-value]->0->"address")]
str

```

So obviously we are comparing string to ip-prefix and conversion from ip-prefix to string does not happen automatically. To fix the problem we need to convert variable to correct format:

```text
[admin@r1] /ip address> print where address=[:tostr 111.111.1.1/24]

Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   111.111.1.1/24     111.111.1.0     ether2

```

Or use a string directly by placing the query value in double quotes:

```text
[admin@r1] /ip address> print where address="111.111.1.1/24"

Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   111.111.1.1/24     111.111.1.0     ether2

```

Obviously the second method is not suitable if you obtain the IP prefix from a variable; in that case, convert it as demonstrated in the first example or write the variable to a string with `"$myVar"`.

## How to define empty array

RouterOS does not allow to define empty array in a way that you think it should:

```ros
[admin@1p_DUT_wAP ac] /interface> :global array {}
syntax error (line 1 column 17)

```

Workaround is to convert empty string to an array:

```ros
[admin@r1] > :global array [:toarray ""]
[admin@r1] > :environment print
array={}
```

From here we can use this array to set elements:

```ros
[admin@r1] > :set ($array->"el0") "el0_val"
[admin@r1] > :environment print
array={el0="el0_val"}
```

## How to remove variables

You can use `/system script environment remove` to delete unused variables; however, the preferred method is to unset the variable.

Setting no value for an existing parameter unsets it; for example:

```ros
[admin@MikroTik] /system script environment> :global myVar 1
[admin@MikroTik] /system script environment> print
 # NAME               VALUE
 0 myVar              1
[admin@MikroTik] /system script environment> :set myVar
[admin@MikroTik] /system script environment> print
 # NAME               VALUE
[admin@MikroTik] /system script environment>

```

## Get values for properties if 'get' command is not available

Some menus, such as the interactive `info` commands, have no `get` subcommand — use the `as-value` parameter to get a usable value for scripting.

The example below uses the legacy `wireless` package (`/interface wireless info`), which is available only on devices with the legacy wireless stack. Devices with the newer `wifi` package (for example, hAP ax²) do not have these menus:

```ros
[admin@1p_DUT_wAP ac] /interface wireless info> :put [hw-info wlan1 as-value ]
ranges=2312-2732/5/b;g;gn20;gn40;2484-2484/5/b;g;gn20;gn40;rx-chains=0;1;tx-chains=0;1

```

The output is a 1‑D array, so you can easily get the property value you are interested in.

```ros
[admin@1p_DUT_wAP ac] /interface wireless info> :put ([hw-info wlan1 as-value ]->"tx-chains")
0;1

```

## Always check what value and type command returns

Let's say we are trying to get the gateway of a specific route using `as-value`, but the script returns nothing:

```ros
[admin@r1] /ip address> :put ([/ip route print as-value where gateway="ether1"]->"gateway")

```

First let's check if `print` actually finds anything:

```ros
[admin@r1] /ip address> :put ([/ip route print as-value where gateway="ether1"])

.id=*400ae12f;distance=255;dst-address=111.111.111.1/32;gateway=ether1;pref-src=111.111.111.1

```

The command assumes the output will be a 1‑D array from which we can extract the element named `gateway`. Obviously there is something wrong with the variable or its type. Let's examine it more closely:

```ros
[admin@r1] /ip address> :global aa ([/ip route print as-value where gateway="ether1"])
[admin@r1] /ip address> :environment print

aa={{.id=*400ae12f; distance=255; dst-address=111.111.111.1/32; gateway={"ether1"}; pref-src=111.11
1.111.1}}

```

Now it is clear that returned value is 2D array with one element. So the right sequence to extract gateway should be:

- get 2d array
- get first element
- get `gateway` from picked element

```ros
[admin@r1] /ip address> :put ([:pick [/ip route print as-value where gateway="ether1"] 0]->"gateway")

ether1

```

## Be careful when adding an array to a string

If you print an array or append it to an existing string, be very careful, as the result may be unexpected. For example, with an array containing two elements:

```ros
[admin@1p_DUT_wAP ac] /> :global array {"cccc", "ddddd"}
[admin@1p_DUT_wAP ac] /> :put ("array value is: " . $array )

array value is: cccc;array value is: ddddd

```

Concatenation operator (`.`) is adding string to each array element and then prints the output. To fix the problem we need to convert to string first:

```ros
[admin@1p_DUT_wAP ac] /> :put ("array value is: " . [:tostr  $array] )

array value is: cccc;ddddd

```

## Get/Set unnamed elements in an array

Let's say we have an array with three elements `{ "el1"; "el2"; "el3" }`. You can pick elements with the `pick` command, but a better way is to access an element directly by its index:

```ros
[admin@1p_DUT_wAP ac] /> :global test { "el1"; "el2"; "el3" }
[admin@1p_DUT_wAP ac] /> :put ($test->1)

el2

```

The same syntax can be used to set values:

```ros
[admin@1p_DUT_wAP ac] /> :set ($test->2) "el3_changed"
[admin@1p_DUT_wAP ac] /> :environment print

test={"el1"; "el2"; "el3_changed"}

```

## Set element value in 2D array

You can also set a value directly by index in a 2‑D array:

```ros
[admin@1p_DUT_wAP ac] /> :global test {{"11";"12";"13"};{"21";"22";"23"}}
[admin@1p_DUT_wAP ac] > :set ($test->1->1) "22_changed"
[admin@1p_DUT_wAP ac] > :put [($test->1->1)]
22_changed
[admin@1p_DUT_wAP ac] > :environment print
test={{"11"; "12"; "13"}; {"21"; "22_changed"; "23"}}

```

## Read the value of a global variable defined in another script

Let's say we have one script that declares a variable and sets its value:

```ros
/system script add name=script1 source={
  :global myVar "hello!"
}
```

Global variables are shared between all scripts of the same user. Another script can read the value of `myVar` even without declaring it first:

```ros
/system script add name=script2 source={
  :log info "value is: $myVar"
}
```

Declaring the variable (`:global myVar;`) before using it is still good practice — it makes the dependency explicit. In either case, the variable holds a value only after `script1` has been run at least once; reading a variable that was never set returns an empty value.

To **change** the value of a global variable from a script, the variable must be declared first — see the example in the next section.

## Accessing global variable from function

A function can read a global variable (or call another function) that is defined earlier in the same session or script, without declaring it inside the function:

```ros
:global myVar "test"
:global myFunc do={
  :put "global var=$myVar"
}
[$myFunc]
```

Output:

```text
global var=test
```

You need to declare the variable inside the function only when you want to **change** its value:

```ros
:global myVar "test"
:global myFunc do={
  :global myVar;
  :set myVar "new value";
  :put "global var=$myVar"
}
[$myFunc]
```

Output:

```text
global var=new value
```

Assigning a value to a variable that is not declared in the function (`:set myVar "new value"` without `:global myVar;`) results in a compilation error.

## Running a function from another function

A function defined earlier in the current session or script can be called from another function directly, without declaring it:

```ros
:global addOne do={
  :return ($1 + 1)
}

:global addOneAndReport do={
  :local x 5
  :local y [$addOne $x]
  :put "typeof = $[:typeof $y]"
  :put "result=$y"
}

$addOneAndReport
```

Output:

```text
typeof = num
result=6
```

The same applies when the called function is defined in another script of the same user — as long as that script has been run at least once, the function is available by name. Declaring the name (`:global addOne;`) inside the calling function is optional and only makes the dependency explicit.

## Always use unique variable names

One of the most common mistakes is using non‑unique variable names. For example, a variable defined in a function may share the name of a global variable, leading to unexpected results:

```ros
:global my2 "123"

:global myFunc do={ :global my2; :put $my2; :set my2 "lala"; :put $my2 }
$myFunc my2=1234
:put "global value $my2"

```

Output will be:

```text
1234
lala
global value 123

```

Another common problem occurs when a user‑defined variable has the same name as a RouterOS built‑in property. For example, to print a route with a `dst-address` defined in a variable:

```ros
[admin@1p_DUT_wAP ac] /ip route> :global "dst-address" "0.0.0.0/0"
[admin@1p_DUT_wAP ac] /ip route> print where dst-address=$"dst-address"
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0 ADS  0.0.0.0/0                          10.155.136.1              1
 1 ADC  10.155.136.0/24    10.155.136.41   ether1                    0

```

Obviously result is not as expected, simple solution, use unique variable name:

```ros
[admin@1p_DUT_wAP ac] /ip route> :global myDst "0.0.0.0/0"
[admin@1p_DUT_wAP ac] /ip route> print where dst-address=$myDst
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0 ADS  0.0.0.0/0                          10.155.136.1              1

```

## Get values from looped interactive commands like "monitor"

A frequently asked question is how to fetch values returned by interactive commands such as `monitor` in a script. The first problem is that these commands run indefinitely until a user intervenes, which a script cannot do. Instead run them with the `once` parameter, which executes the command a single time and then stops. Another issue is retrieving the returned variables: there is no `as-value` and no `get`, but there is `do`. It allows you to access variables returned by the command. For example:

```ros
[admin@1p_DUT_wAP ac] /interface> monitor-traffic ether1 once do={:global myBps $"rx-bits-per-second" }
...
[admin@1p_DUT_wAP ac] /interface> :environment print

myBps=71464

```

## Get file content received by fetch tool

The fetch tool makes it easy to download file content into memory and access it from a script. To do this, use the `as-value` parameter with `output=user`:

```ros
[admin@rack1_b34_CCR1036] > :put ([/tool fetch ftp://admin:@10.155.136.41/test.txt
 output=user as-value ]->"data")

my file content

```

## Check script permissions

Let's say we have a script that creates and writes content to a file:

```ros
/system script add name=script1 policy=ftp,read,write source={
        /file print file=test;
        /file set test.txt contents="my content"
}

```

Now let's add a scheduler that will try to execute this script:

```ros
/system scheduler
add interval=10s name=test on-event=script1 policy=read,write

```

After waiting 10 seconds, we can see that file was not created. If you look closely, script requires policy "ftp", to create a file, but scheduler has only "read" and "write" policies. To fix the problem, set scheduler to run with correct policies "read,write,ftp".

This also applies when you run a script from netwatch, ppp `on-event`, and similar hooks, which are limited to the policies `read,write,test,reboot`. In such cases you cannot execute advanced scripts that create backups or files.

You can fix the limitation by using `dont-require-permissions`, but be very careful granting unrestricted permissions to scripts.

## Be careful when using dont-require-permissions

It is possible to set script with `dont-require-permissions` parameter. Basically it allows anyone without adequate permissions to execute the script. For example, if a script has policies "read,write,test,sensitive", but user or application that executes the script has less, (for example, only "read,write"), then by setting `dont-require-permissions=yes` we will allow to run script anyway.

This could potentially allow to change sensitive information using script even if user that executes the script does not have enough permissions.
