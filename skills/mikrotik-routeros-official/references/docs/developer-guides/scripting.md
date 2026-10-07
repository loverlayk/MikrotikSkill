# Scripting

> RouterOS scripting enables automation through user-defined scripts triggered by events like system scheduling or traffic monitoring. Scripts use a command-line syntax with optional prefixes, named parameters, and...

# Scripting

RouterOS includes a powerful scripting language for automating maintenance tasks. You create user-defined scripts and bind them to events.

You can store scripts in the Script repository or write them directly in the CLI. Common triggers include the System Scheduler, Traffic Monitoring Tool, and Netwatch Tool events.

If you are already familiar with scripting in RouterOS, you might want to see our [Tips & Tricks](./scripting-tips-and-tricks.md).

## Line structure

The RouterOS script is divided into a number of command lines. Command lines are executed one by one until the end of the script or until a runtime error occurs.

### Command-line

The RouterOS CLI uses the following command syntax:

`[prefix] [path] command [uparam] [param=[value]] .. [param=[value]]`

- [prefix] - `:` or `/` character indicates if following word is a [global command](#global-commands) or a path. Prefix is not required when called from root menu or from the menu relative to the called path/command.
- [path] - relative path to the desired menu level. It may not be required.
- command - one of the [commands](#commands) available at the specified menu level.
- [uparam] - unnamed parameter, must be specified if the command requires it.
- [params] - a sequence of named parameters followed by values (if a parameter requires a value).

The end of the command line is represented by the token `;` or *NEWLINE*.
A command enclosed in `()`, `[]` or `{}` does not require any end-of-command character. The end of the command is determined by the content of the whole script

```ros
:if ( true ) do={ :put "lala" }
```

Each command line inside another command line starts and ends with square brackets `[]` [(command concatenation operator)](#other-operators).

```ros
:put [/ip route get [find gateway=1.1.1.1]];
```

Notice that the code above contains three command lines:

- `:put`
- `/ip route get`
- `find gateway=1.1.1.1`

Notice that menu specific `find` command does not require a full path because the path is derived from the parent command's path.

A command line can be constructed from more than one physical line by following [line joining rules](#line-joining).

### Physical Line

A physical line is a sequence of characters terminated by an end-of-line (**EOL**) sequence. Any of the standard platform line termination sequences can be used:

- **Unix** – ASCII LF;
- **Windows** – ASCII CR LF;
- **mac** – ASCII CR;

Standard C conventions for newline characters can be used ( `\n`, `\r\n` characters).

### Comments

The following rules apply to a comment:

- A comment starts with a hash character `#` and ends at the end of the physical line.
- RouterOS does not support multiline comments.
- If a `#` character appears inside the string it is not considered a comment.

```ros
# this is a comment
# continued comment in the next line
:global a; # comment describing variable

:global myStr "part of the string # is not a comment"
```

### Line joining

Two or more physical lines may be joined into logical lines using the **backslash** character (`\`).
The following rules apply to using backslash as a line-joining tool:

- A line ending in a backslash cannot carry a comment.
- A backslash does not continue a comment.
- A backslash does not continue a token except for string literals.
- A backslash is illegal elsewhere on a line outside a string literal.

```ros
:if ($a = true \
	and $b=false) do={ :put "$a $b"; }
:if ($a = true \ # bad comment (syntax error)
	and $b=false) do={ :put "$a $b"; }
# comment \
	continued is invalid (syntax error)
```

### Whitespace between tokens

Whitespace can be used to separate tokens. Whitespace is necessary between two tokens only if their concatenation could be interpreted as a different token. Example:

```ros
{  
	:local a true; :local b false;
# whitespace is not required
	:put (a&&b);
# whitespace is required  
	:put (a and b);
}

```

Whitespace characters are not allowed:

- between `<parameter>=`.
- between `from=`, `to=`, `step=`, `in=`, `do=`, `else=`.

Example:

```ros
#incorrect:
:for i from = 1 to = 2 do = { :put $i }

#correct syntax:
:for i from=1 to=2 do={ :put $i }
:for i from= 1 to= 2 do={ :put $i }

#incorrect
/ip route add gateway = 3.3.3.3

#correct
/ip route add gateway=3.3.3.3
```

### Scopes

Variables can be used only in certain regions of the script called scopes. These regions determine the visibility of the variable. A variable declared within a block is accessible only within that block and its nested blocks, and only after the declaration point.

There are two types of scopes — **global** and **local**.

#### Global scope

Global scope or root scope is the default scope of the script. It is created automatically and cannot be turned off.

A global variable set by another script can be accessed by declaring it without assigning a value.

For example, first script sets the myVar value to 3:

```ros
:global myVar 3
```

To access this variable from another script:

```ros
:global myVar
:put "myVar=$myVar"
```

Output:

```
myVar=3
```

#### Local scope

You can define groups to limit variable access; these are called local scopes. Each local scope is enclosed in curly braces (`{}`).

```ros
{  
    :local a 3;
    {  
	:local b 4;  
	:put ($a+$b);
    } #line below will show variable b in light red color since it is not defined in this scope  
    :put ($a+$b);
}

```

Variable `b` is declared in a local scope and is not accessible after the closing curly brace.

Each line written in the CLI is treated as a local scope.
For example, the defined local variable is not visible in the next command line and generates a syntax error

```ros
[admin@MikroTik] > :local myVar a;
[admin@MikroTik] > :put $myVar
syntax error (line 1 column 7)

```

:::danger
Do not define a **global** variable inside a **local** scope.
:::

Even if variable can be defined as global, it will be available only from its scope unless it is not referenced to be visible outside of the scope.

```ros
{  
    :local a 3;
    {  
        :global b 4;
    }  
    :put ($a+$b);
}
```

The code outputs 3 because `b` is not visible outside the scope.

The following code fixes the problem and outputs 7 as intended:

```ros
{  
    :local a 3;
    {  
        :global b 4;
    }
    :global b;  
    :put ($a+$b);
}
```

## Keywords

The following words are keywords and cannot be used as variable and function names:

```
and       or       in

```

## Delimiters

The following tokens serve as delimiters in the grammar:

```
()  []  {}  :   ;   $   /

```

## Data types

RouterOS scripting language has the following data types:

| Type                 | Description                                           |
|:--|:--|
| **num (number)**     | 64bit signed integer, possible hexadecimal input;     |
| **bool (boolean)**   | values can be `true` or `false`.                     |
| **str (string)**     | character sequence.                                   |
| **ip**               | IP address.                                           |
| **ip-prefix**        | IP prefix.                                            |
| **ip6**              | IPv6 address.                                         |
| **ip6-prefix**       | IPv6 prefix.                                          |
| **id (internal ID)** | Hexadecimal value prefixed by `*` character. Each menu item has an assigned unique number - internal ID. |
| **time**             | Date and time value.                                  |
| **array**            | Sequence of values organized in an array.             |
| **nil**              | Default variable type if no value is assigned.        |

## Constant Escape Sequences

Following escape sequences can be used to define certain special characters within a string:

|         |                                                                    |
|:--|:--|
| **\"**  | Insert double quote.                                               |
| **\\**  | Insert backslash.                                                  |
| **\n**  | Insert newline.                                                    |
| **\r**  | Insert carriage return.                                            |
| **\t**  | Insert horizontal tab.                                             |
| **\$**  | Output $ character. Otherwise, $ is used to link the variable.     |
| **\\_** | Space.                                                             |
| **\a**  | BEL (0x07).                                                        |
| **\b**  | Backspace (0x08).                                                  |
| **\f**  | Form feed (0x0C).                                                  |
| **\v**  | Insert vertical tab.                                               |
| **\xx** | A print character from hex value. Hex numbers should use capital letters. |

For example:

```ros
:put "\48\45\4C\4C\4F\r\nThis\r\nis\r\na\r\ntest";

```

will output:

```
HELLO
This
is
a
test
```

## Operators

### Arithmetic Operators

Common arithmetic operators are supported in the RouterOS scripting language:

| Operator   | Description           | Example                        |
|:--|:--|:--|
| **`+`**    | binary addition       | `:put (3+4);`                  |
| **`-`**    | binary subtraction    | `:put (1-6);`                  |
| **`*`**    | binary multiplication | `:put (4*5);`                  |
| **`/`**    | binary division       | `:put (10 / 2); :put ((10)/2)` |
| **`%`**    | modulo operation      | `:put (5 % 3);`                |
| **`-`**    | unary negation        | `{ :local a 1; :put (-a); }`   |

Note that for the division to work, you have to use braces or spaces around the dividend so it is not mistaken as an IP address.

### Relational Operators

| Operator   | Description      | Example       |
|:--|:--|:--|
| **`<`**    | less             | `:put (3<4);` |
| **`>`**    | greater          | `:put (3>4);` |
| **`=`**    | equal            | `:put (2=2);` |
| **`<=`**   | less or equal    |               |
| **`>=`**   | greater or equal |               |
| **`!=`**   | not equal        |               |

To negate an expression, you can use `<expression>=false`. For example, to print all interfaces that are not "ethernet", you can use expression negation like this:

```ros
/interface/print where (name~"ether")=false
```

Or to do the opposite, you can use `<expression>=true`:

```ros
/interface/print where (name~"ether")=true
```

### Logical Operators

| Operator         | Description   | Example                           |
|:--|:--|:--|
| **`!`**          | logical NOT   | `:put (!true);`                   |
| **`&&`, `and`**  | logical AND   | `:put (true&&true)`               |
| **`\|\|`, `or`** | logical OR    | `:put (true\|\|false);`           |
| **`in`**         |               | `:put (1.1.1.1/32 in 1.0.0.0/8);` |

### Bitwise Operators

Bitwise operators are working only on IP, and IPv6 address [data types](#data-types).

| Operator   | Description      | Example                                      |
|:--|:--|:--|
| **`~`**    | Bit inversion.   | `:put (~0.0.0.0)` `:put (~::ffff)`           |
| **`\|`**   | Bitwise OR performs logical OR operation on each pair of corresponding bits. In each pair the result is “1” if one of the bits or both bits is “1”, otherwise the result is “0”. | `:put (192.168.88.0\|0.0.0.255)` `:put (2001::1\|::ffff)` |
| **`^`**    | Bitwise XOR is the same as OR, but the result in each position is “1” if two bits are not equal, and “0” if the bits are equal. | `:put (1.1.1.1^255.255.0.0)` `:put (2001::ffff:1^::ffff:0)` |
| **`&`**    | Bitwise AND result is “1” if the first and second bit is “1”. Otherwise, the result is “0”. | `:put (192.168.88.77&255.255.255.0)` `:put (2001::1111&ffff::)` |
| **`<<`**   | Left shift by a given amount of bits, not supported for IPv6 address data type. | `:put (192.168.88.77<<8)` |
| **`>>`**   | Right shift by a given amount of bits, not supported for IPv6 address data type. | `:put (192.168.88.77>>24)` |

For example, calculate a subnet address from a given IP and CIDR netmask with the `&` operator:

```ros
{
:local IP 192.168.88.77;
:local CIDRnetmask 255.255.255.0;
:put ($IP&$CIDRnetmask);
}
```

Get the last 8 bits from the given IP addresses:

```ros
 :put (192.168.88.77&0.0.0.255);
```

Use the `|` operator and an inverted CIDR mask to calculate the broadcast address:

```ros
{
:local IP 192.168.88.77;
:local Network 192.168.88.0;
:local CIDRnetmask 255.255.255.0;
:local InvertedCIDR (~$CIDRnetmask);
:put ($Network|$InvertedCIDR)
}
```

### Concatenation Operators

| Operator   | Description          | Example                                  |
|:--|:--|:--|
| **`.`**    | Concatenates two strings.| `:put ("concatenate" . " " . "string");` |
| **`,`**    | Concatenates two arrays or adds an element to the array. | `:put ({1;2;3} , 5 );` |

It is possible to add variable values directly to strings without a concatenation operator:

```ros
:global myVar "world";

# value can be added with concatenation operator
:put ("Hello " . $myVar);
# or without operator
:put "Hello $myVar";
```

Using `$[]` and `$()` you can execute expressions and insert the resulting value into strings:

```ros
:local a 5;
:local b 6;
:put " 5x6 = $($a * $b)";

:put " We have $[ :len [/ip route find] ] routes";
```

### Other Operators

| Operator   | Description       | Example                                     |
|:--|:--|:--|
| **`[]`**   | Command substitution can contain only a single command line` | `:put [ :len "my test string"; ];` |
| **`()`**   | Subexpression or grouping operator. | `:put ( "value is " . (4+5));` |
| **`$`**    | Substitution operator. | `:global a 5; :put $a;` |
| **`~`**    | The binary operator that matches value against POSIX extended regular expression. | Print all routes whose gateway ends with 202: `/ip/route/print where gateway~"^[0-9 \\.]*202\$"` |
| **`->`**   | Get an array element by key. | `[admin@x86] >:global aaa {a=1;b=2}``[admin@x86] > :put ($aaa->"a")``1``[admin@x86] > :put ($aaa->"b")``2` |

## Variables

The scripting language has two types of variables:

- **global** - Accessible from all scripts created by the current user, defined by [`global`](#global-scope) keyword.
- **local** - Accessible only within the current [scope](#local-scope), defined by `local` keyword.

Variables may be undefined. When that happens, the parser looks for built-in variables provided by the application. For example, the DHCP `lease-script` supplies several built-in variables:

```ros
/system script
add name=myLeaseScript policy=\
	ftp,reboot,read,write,policy,test,winbox,password,sniff,sensitive,api \
	source=":log info \$leaseActIP\r\
	\n:log info \$leaseActMAC\r\
	\n:log info \$leaseServerName\r\
	\n:log info \$leaseBound"

/ip dhcp-server set myServer lease-script=myLeaseScript
```

Except for built-in RouterOS variables, every variable must be declared before use with the `local` or `global` keyword. Using an undeclared variable results in a compilation error. For example:

```ros
# following code will result in compilation error, because myVar is used without declaration
:set myVar "my value";
:put $myVar
```

Correct code:

```ros
:local myVar;
:set myVar "my value";
:put $myVar;
```

Valid characters in variable names are letters and digits. If a variable name contains any character other than letters or digits (including operators), enclose it in double quotes (`""`). Example:

```ros
#valid variable name
:local myVar;
#invalid variable name
:local my-var;
#valid because double quoted
:global "my-var";
```

If a variable is initially defined without a value, the [variable data type](#data-types) is set to ***nil***; otherwise, the scripting engine determines the data type automatically. Sometimes conversion from one data type to another is required. It can be achieved using [data conversion commands](#global-commands). Example:

```ros
#convert string to array
:local myStr "1,2,3,4,5";
:put [:typeof $myStr];
:local myArr [:toarray $myStr];
:put [:typeof $myArr]
```

Variable names are case-sensitive.

```ros
:local myVar "hello"
# following line will generate error, because variable myVAr is not defined
:put $myVAr
# correct code
:put $myVar
```

The `set` command without a value undefines a variable:

```ros
#remove variable from environment
:global myVar "myValue"
:set myVar;
```

### Reserved variable names

All built-in RouterOS properties are reserved variables. Variables defined with the same names as RouterOS built-in properties can cause errors. To avoid this, choose different names.

For example, the following script will not work:

```ros
{
:local type "ether1";
/interface print where name=$type;
}
```

But will work with different defined variables:

```ros
 {
:local customname "ether1";
/interface print where name=$customname;
}
```

## Commands

### Global commands

Every global command should start with the **`:`** token; otherwise it is treated as a variable.

| Command         | Syntax     | Description          | Example                |
|:--|:--|:--|:--|
| **/**           |            | Go to the root menu. |                        |
| **..**          |            | Go back by one menu level. |                  |
| **?**           |            | List all available menu commands and brief descriptions. |  |
| **global**      | `:global <var> [<value>]` | Define a global variable. | `:global myVar "something"; :put $myVar;` |
| **local**       | `:local <var> [<value>]` | Define the local variable. | `{ :local myLocalVar "I am local"; :put $myLocalVar; }` |
| **beep**        | `:beep frequency=[num] length=[num]` | Beep the built-in speaker. |  |
| **convert**     | `:convert from=[arg] to=[arg] transform=[arg]` | Converts specified value from one format to another. By default uses an automatically parsed value, if the `from` format is not specified (for example, "001" becomes "1", "10.1" becomes "10.0.0.1", etc.).  **`from`** - Specifies the format of the value: *base32, base64, bit-array-lsb, bit-array-msb, byte-array, hex, num, raw, url*.  **`to`** - Specifies the format of the output value: *base32, base64, bit-array-lsb, bit-array-msb, byte-array, hex, num, raw, url*.   **`transform`** - Specifies how to transform values: *lc (transforms value to be in lowercases), uc (uppercases), lcfirst (first value to lowercase), ucfirst (first value to uppercase), crlf, ed25519-private-to-x25519-private, none, rot 13, x25519-private-to-x25519-public, ed25519-private-to-ed25519-public, ed25519-public-to-x25519-public, md5, reverse (reverses text), sha512.* | `:put [:convert 001 to=hex ]`  `31`  `:put [:convert [/ip dhcp-client/option/get hostname raw-value] from=hex to=raw ]`  `MikroTik`  `:put [:convert transform=lc "AAA"]`  `aaa` |
| **delay**       | `:delay <time>` | Do nothing for a given period of time. |  |
| **environment** | `:environment print <start>` | Print initialized variable information. | `:global myVar true; :environment print;` |
| **error**       | `:error <output>` | Generate console error and stop executing the script. |  |
| **execute**     | `:execute <expression>` | Execute the script in the background. The result can be written in the file by setting a `file` parameter or printed to the CLI by setting `as-string`.  When using the `as-string` parameter executed script is blocked (not executed in the background).  Executed scripts cannot be larger than 64 kB. | `{ :local j [:execute {/interface print follow where [:log info ~Sname~]}]; :delay 10s; :onerror e {/system script job remove $j}}` |
| **find**        | `:find <arg> <arg> <start>` | Return position of a substring or array element. | `:put [:find "abc" "a" -1];` |
| **grep**        | `:grep script=[str] pattern=[expression] after=[num] before=[num] filename=[str]` | Execute provided `script` in the terminal and print the lines matched by a given `pattern`. Parameters `after` and `before` sets how many lines to print additionaly before and after the matched line. Results can be directly saved into a file with `filename` parameter. | `:grep script="/interface print" pattern="ether" after=1 before=1 filename=results.txt` |
| **jobname**     | :jobname   | Return current script name. | **Limit script execution to single instance**  ` :if ([/system script job print count-only as-value where script=[:jobname] ] > 1) do={  :error "script instance already running"  }`|
| **len**         | `:len <expression>` | Return the string length or the array element count. | `:put [:len "length=8"];` |
| **log**         | `:log <topic> <message>` | Write a message to the [system log](../../diagnostics-monitoring-and-troubleshooting/log/index.md). Available topics are `debug`, `error`, `info` and `warning`. | `:log info "Hello from script";` |
| **onerror**     | `:onerror <var_name> in={<command>} do={<expression>}` | Catch errors and get error details. The **`do={...}`** block is executed, when **`in={...}`** block has an error,  and error details are written in `<var_name>` variable.   Parameter order is important. The `error` parameter must be set before `do` block, otherwise `do` block will not see the local variable.  `:onerror` will return `false` (if there is no error) and `true` (if there is an error) unless otherwise specified (with commands such as `:return` or `:error`), so it can be used in **`:if`** condition statement scripts. | `:onerror errorName in={ :error "failure" } do={ :put "Critical $errorName" }` |
| **parse**       | `:parse <expression>` | Parse the string and return parsed console commands. Can be used as a function. | `:global myFunc [:parse ":put hello!"]; $myFunc;` |
| **pick**        | `:pick <var> <start> [<end>]`                                                     | Return range of elements or substring. If the count is not specified, it will return only one element from an array. `var` - value to pick elements from.`start` - element to start picking from (the first element index is 0).`end` - terminating index (element at this index is not included). | `[admin@MikroTik] > :put [:pick "abcde" 1 3]``bc` |
| **put**         | `:put <expression>` | Print the supplied argument to the terminal. | `:put "Hello world"` |
| **range**       | `:range <var> <var>` | Creates an array from the specified range. | `:put [:range 2 8] 2;3;4;5;6;7;8` |
| **resolve**     | `:resolve <arg> [<domain-name>][<server>][<server-port>][<type>]` | Return the IP address of the given DNS name `domain-name` - DNS name that needs to be resolved.`server` - Specific server that will be used to resolve DNS name (returned results will not be cached).`server-port` - Server port to connect to.`type` - any/any6/ipv4/ipv6:`any` - Try to resolve ipv4, on failure try ipv6.`any6` - Try to resolve ipv6, on failure try ipv4.`ipv4` - Try to resolve only ipv4.`ipv6` - Try to resolve only ipv6. | `:put [:resolve "www.mikrotik.com"];`  `:put [:resolve domain-name="www.mikrotik.com"];`  `:put [:resolve domain-name="www.mikrotik.com" server=192.168.88.1 server-port=53];`  `:put [:resolve domain-name="www.mikrotik.com" type=ipv6];` |
| **retry**       | `:onerror e {:retry command=<expr> delay=[num] max=[num]} do={<expr>}` | Try to execute the given command `max` amount of times with a given `delay` in seconds between tries. On failure, execute the command in the `do={}` block. | `:onerror e {:retry command={abc} delay=1 max=2} do={:put "got error"}` |
| **typeof**      | `:typeof <var>` | Return data type of the given variable. | `:put [:typeof 4];` |
| **rndnum**      | `:rndnum from=[num] to=[num]` | Random number generator. | `:put [:rndnum from=1 to=99];` |
| **rndstr**      | `:rndstr from=[str] length=[num]` | Random string generator.  **`from`** specifies characters to construct the string from and defaults to all ASCII letters and numerals.  **`length`** specifies the length of the string to create and defaults to 16. | `:put [:rndstr from="abcdef%^&``" length=33];` |
| **set**         | `:set <var> [<value>]` | Assign value to a declared variable. | `:global a; :set a true;` |
| **serialize**   | `:serialize [<value>] to=[arg]` | Serialize specified value/array to JSON or dsv (delimiter separated values) format.  **`value`** specifies which values to process.  **`to`** specifies the format - *json, dsv*  **`delimiter`** sets the "separator".  **`order`** specifies the order for variables.  **`options`** specifies additional options*:* json.pretty  - makes the JSON output more visually appealing;json.no-string-conversion - prevents implicit conversions from console string type to json number type;dsv.wrap-strings - wraps string values inside quotation marks;dsv.ignore-size - if array values have different sizes, e.g. <code>a=(1,2);b=(3,4);c=(5,6,7)</code>, this option will work around <code>array size mismatch</code> error and set "empty" values in those slots.dsv.remap - merges array of dictionaries into a single dictionary (useful when working with "<code>print as-value</code>") **file-name** enables the option to generate command's output into a file (available for download in the "/files" section). | `:put [:serialize value=a,b,c to=json]``["a","b","c"]``:local test {a=(1,2,3);b=(4,5,6);c=(7,"text",9)}; :put [ :serialize to=dsv delimiter=";" value=$test order=("c","a","b") ]``c;a;b``7;1;4``text;2;5``9;3;6``:global var ({ "string"="1234"; "number"=1234 });:put [ :serialize to=json value=$var ]``{"number":1234,"string":1234.000000}``:put [ :serialize to=json value=$var options=json.no-string-conversion  ]``{"number":1234,"string":"1234"}``:put [:serialize to=dsv options=dsv.remap delimiter="#" [/ip/address/print as-value]]``.id#address#comment#interface#network``*1#192.168.88.1/24#defconf#bridge#192.168.88.0``*2#192.168.69.190/24##ether1#192.168.69.0`|
| **deserialize** | `:deserialize [<value>] from=[arg]` | Deserialize specified value/array from JSON or dsv (delimiter separated values) format.  **`from`** specifies the format - *json, dsv*  **`delimiter`** sets the "separator".  **`options`** specifies additional options*:* dsv.plain - deserializes every line as an array (input does not have a header or column names);dsv.array - expects a header (column names) and will return an array of dictionaries, where values are mapped to column names provided in the header.json.no-string-conversion - prevents implicit conversions from json string type to console values (number, ip, etc.). | `:put [:deserialize from=json value="[\"a\",\"b\",\"c\"]"]``a;b;c``:put ([ :deserialize from=dsv delimiter=";" value="a;b;c\n1;findme;3" options=dsv.plain ]->1->1)` `findme``:put ([ :deserialize from=dsv delimiter=";" value="a;b;c\n1;findme;3" options=dsv.plain ]->0->1)   ``b``:put ([:deserialize from=dsv "a;b;c\n1;2;3\n4;5;6" delimiter=";" options=dsv.array]->1->"b") ``5``:put ([:deserialize from=dsv "a;b;c\n1;2;3\n4;5;6" delimiter=";" options=dsv.array]->0->"c")    ``3``:put [typeof ([:deserialize "{ \"str\": \"123\" }" from=json options=json.no-string-conversion]->"str")]``str``:deserialize [/file/get file.json contents] from=json` |
| **time**        | `:time <expression>` | Return interval of time needed to execute the provided expression. | `:put [:time {:for i from=1 to=10 do={ :delay 100ms }}];` |
| **timestamp**   | `:timestamp [use-tz]` | Returns the time since `epoch`, where `epoch` is January 1, 1970 (Thursday), not counting leap seconds. The time is returned in UTC by default. Use the `use-tz` parameter to return the timestamp adjusted for the configured time zone on the router. | `[admin@MikroTik] > :put [:timestamp]``2735w21:41:43.481891543`or`[admin@MikroTik] > :put [:timestamp]``2735w1d21:41:43.481891543`with the day offset. |
| **toarray**     | `:toarray <var>` | Convert a variable to an array. |       |
| **tobool**      | `:tobool <var>` | Convert a variable to a boolean. |       |
| **toid**        | `:toid <var>` | Convert a variable to internal ID. |       |
| **toip**        | `:toip <var>` | Convert a variable to an IP address. |     |
| **toip6**       | `:toip6 <var>` | Convert a variable to an IPv6 address. |  |
| **tonum**       | `:tonum <var>` | Convert a variable to an integer. |       |
| **tostr**       | `:tostr <var>` | Convert a variable to a string. |         |
| **totime**      | `:totime <var>` | Convert a variable to time. |            |
| **tonsec**      | `:tonsec <var>` | Convert a time to a nanoseconds. | `:put [:tonsec value=10:00]                36000000000000` |
| **tocrlf**      | `:tocrlf <var>` | Converts line endings to CRLFs. | `:put [:tocrlf  "AAA\r\nBBB\r\nCCC" ]``AAA``BBB``CCC`|
| **tolf**        | `:tolf <var>` | Converts line endings to LFs. | `:put [:tolf  "AAA\nBBB\nCCC" ]``AAA``   BBB``      CCC`|
| **nothing**     | `:nothing`  | Return a value of nothing. | `:if ([:nothing] = 0) do={:put true} else={:put false} false :if ([:nothing] > 0) do={:put true} else={:put false}  false :if ([:nothing] < 0) do={:put true} else={:put false}` |

If a variable type conversion function cannot apply the new format to the provided data, the output will be empty.

For example, if you run the `:tonum <var>` command on a variable with a non-integer value such as "23.8" or "cow&chicken", the result will be empty, and its data type will be shown as `nil`.

### Common commands

The following commands are available from most sub-menus:

| Command     | Syntax                                      | Description      |
|:--|:--|:--|
| **add**     | `add <param>=<value>..<param>=<value>`      | Add new item. This command usually has all the same arguments as **set**, except the item number argument. It adds a new item with the values you have specified, usually at the end of the item list, in places where the order of items is relevant. There are some required properties that you have to supply, such as the interface for a new address, while other properties are set to defaults unless you explicitly specify them. Returns the internal number of the item it has added.Common parameters:*copy-from* - Copies an existing item. It takes the default values of a new item's properties from another item. If you do not want to make an exact copy, you can specify new values for some properties. When copying items that have names, you will usually have to give a new name to a copy.*place-before* - Places a new item before an existing item with a specified position. Thus, you do not need to use the move command after adding an item to the list.*disabled* - Controls the disabled/enabled state of the newly added item(-s).*comment* - Holds the description of a newly created item. |
| **remove**  | `remove <id>`                               | Remove selected item. |
| **enable**  | `enable <id>`                               | Enable selected item. |
| **disable** | `disable <id>`                              | Disable selected item.  |
| **set**     | `set <id> <param>=<value>..<param>=<value>` | Change selected items parameter, more than one parameter can be specified at the time. The parameter can be unset by specifying '!' before the parameter.  Example: `/ip firewall filter add chain=blah action=accept protocol=tcp port=123 nth=4,2 print set 0 !port chain=blah2 !nth protocol=udp` |
| **get**     | `get <id> <param>=<value>`                  | Get the selected item's parameter value. Does not display it in the terminal by default. If used in combination with the :put command, it displays the retrieved value in the terminal, for example: `:put [/system/resource/get version]` will show the version of RouterOS installed on the device. |
| **print**   | `print <param><param>=[<value>]`            | Print menu items. Output depends on the [print parameters](#print-parameters) specified. Shows all information accessible from a particular command level. Thus, `/system/clock/print` shows the system date and time, `/ip/route/print` shows all routes, etc. If there's a list of items in the current level and they are not read-only, the print command also assigns numbers used by all commands that operate with items in this list. |
| **export**  | `export [file=<value>]`                     | Export configuration from the current menu and its sub-menus (if present). If the `file` parameter is specified, then output will be written to the file with the extension '.rsc', otherwise the output will be printed to the terminal. Exported commands can be imported by [import command](#import). |
| **edit**    | `edit <id> <param>`                         | Edit selected items property in the built-in text editor. Can be used to edit values of properties that contain a large amount of text, such as scripts, but it works with all editable properties. Depending on the capabilities of the terminal, either a fullscreen editor or a single-line editor is launched. The edit field for console scripts is limited to 30 thousand characters. |
| **find**    | `find <expression>`                         | Returns a list of internal numbers for items that are matched by a given expression. Has the same arguments as **set**, plus the flag arguments like *disabled* or *active* that take values *yes* or *no* depending on the value of the respective flag. To see all flags and their names, look at the top of the **print** command's output. |
| **move**    | `move <id> [<id>]`                          | Changes the order of items in the list. The first argument specifies the item(-s) being moved. The second argument specifies the item before which to place all items being moved (placed at the end of the list if the second argument is omitted). |
| **reset**   | `reset <id> [<param>=<value>]`              | Resets parameters to default values. You can also include parameters with arguments in the same command, allowing you to reset and configure settings at the same time. |
| **comment** | `comment <id> <value>`                      | Allows you to comment the selected item. |

#### import

The import command is available from the root menu and is used to import configuration from files created by an [export](#common-commands) command or written manually by hand.

```ros
[admin@admin] > do { import test.rsc } on-error={ :put "Failure" }
Failure
```

Parameter `onerror` can be used to catch the errors:

```ros
[admin@admin] > onerror e in={ import test.rsc } do={ :put "Failure - $e" }
Failure - Script Error: bad command name this (line 1 column 1)
```

In addition, the *`import`* command has new options in *`verbose`* mode - the *`dry-run`* parameter is designed for debugging and can be used to find errors without changing the configuration.

```ros
[admin@admin] > import test.rsc verbose=yes dry-run
#line 1
this
bad command name this (line 1 column 1)
...
Script Error: found 5 error(s) in import file
```

#### print parameters

Several common parameters are available for `print` command:

| Parameter          | Description          | Example      |
|:--|:--|:--|
| **append**         |                      |              |
| **as-value**       | Print output as an array of parameters and its values. | `:put [/ip address print as-value]`        |
| **brief**          | Brief output is typically is minimalist and is represented as a table of items with most commonly needed parameters. |  |
| **detail**         | Print detailed description, the output is not as readable as brief output but may be useful to view all parameters. |  |
| **count-only**     | Print only count of items in current menu. |  |
| **file**           | Write output to a file. |  |
| **follow**         | Print all current entries and track new entries until <kbd>ctrl</kbd>-<kbd>c</kbd> is pressed. Could be used when viewing, for example, log entries. | `/log print follow` |
| **follow-only**    | Print and track only new entries until <kbd>ctrl</kbd>-<kbd>c</kbd> is pressed. Could be used when, for example, trying to see new log entries. | `/log print follow-only` |
| **from**           | Print parameters only from a specified item. | `/user print from=admin` |
| **interval**       | Continuously print output in a selected time interval, useful to track down changes where `follow` is not acceptable | `/interface print interval=2` |
| **terse**          | Show details in a compact and machine-friendly format. |  |
| **value-list**     | Data is displayed in a table, where parameters are split by lines and available items are split by columns (can be used for parsing purposes). |  |
| **order-by**        | Sort output by one or more properties. Prefix the property name with `-` for descending order. Up to three sorting fields can be specified. | `/ip/arp/print order-by=address``/interface/print order-by=-link-downs proplist=name,link-downs``/interface/ethernet/print stats order-by=-driver-rx-packet where running` |
| **without-paging** | If the output does not fit in the console screen then print all information in a single piece without stops. |  |
| **where**          | Expressions followed by `where` parameters can be used to filter outmatched entries. | `/ip route print where interface="ether1"` |
| **about**          | Returns entries that have the `about` parameter, such as "managed by CAPsMAN " information or warnings | `/interface wifi print where about` |
| **!comments**          | Returns entries without comments | `/interface firewall filter print !comments` |

More than one parameter can be specified at a time, for example, `/ip route print count-only interval=1 where interface="ether1"`

## Loops and conditional statements

### Loops

| Command       | Syntax   | Description  |
|:--|:--|:--|
| **`do..while`** | `:do { <commands> } while=( <conditions> ); :while ( <conditions> ) do={ <commands> };` | Execute commands until a given condition is met. |
| **`for`**       | `:for <var> from=<int> to=<int> step=<int> do={ <commands> }` | Execute commands over a given number of iterations |
| **`foreach`**   | `:foreach <var> in=<array> do={ <commands> };` | Execute commands for each element in a list. |

### Conditional statement

| Command   | Syntax | Description |
|:--|:--|:--|
| **`if`**    | `:if (<condition>) do={<commands>} else={<commands>}` | If a given condition is `true` then execute commands in the `do` block, otherwise execute commands in the `else` block (if specified). |

Example:

```ros
{  
	:local myBool true;  
	:if ($myBool = false) do={ :put "value is false" } else={ :put "value is true" }
}
```

## Functions

Functions are defined similar to global variables, with `global` keyword followed by `do=` operator after which body is enclosed in curly braces (`{}`).

There are two ways to pass arguments:

- Pass arg with a specific name.
- Pass value without arg name, in such case arg "1", "2" .. "n" is used to reference the value.

```ros
#define function and run it
:global myFunc do={:put "hello from function"}
$myFunc

output:
hello from function

#pass arguments to the function
:global myFunc do={:put "arg a=$a"; :put "arg '1'=$1"}
$myFunc a="this is arg a value" "this is arg1 value"

output:
arg a=this is arg a value
arg '1'=this is arg1 value
```

You can return a function value with the **`:return`** command.

```ros
:global myFunc do={ :return ($a + $b)}
:put [$myFunc a=6 b=2]

output:
8
```

You can even clone an existing script from the script environment and use it as a function.

```ros
#add script
/system script add name=myScript source=":put \"Hello \$myVar !\""

:global myFunc [:parse [/system script get myScript source]]
$myFunc myVar=world

output:
Hello world !
```

Scripting language allows to create functions indirectly as well by using `:parse` command.

If the function contains a defined global variable that names match the name of the passed parameter, then the globally defined variable is ignored, for compatibility with scripts written for older versions. **Avoid using parameters with the same name as global variables.**

For example:

```ros
:global my2 "123"

:global myFunc do={ :global my2; :put $my2; :set my2 "lala"; :put $my2 }
$myFunc my2=1234
:put "global value $my2"
```

The output will be:

```
1234
lala
global value 123

```

To call one function from another (a nested function), declare its name as you would a variable:

```ros
:global funcA do={ :return 5 }
:global funcB do={  
	:global funcA;  
	:return ([$funcA] + 4)
}
:put [$funcB]
```

```
Output:
9
```

## Catch run-time errors

RouterOS scripting allows to catch runtime errors, which otherwise would exit script unexpectedly. For example, the `:resolve` command will throw an error and break the script if failed.

```
[admin@MikroTik] > { :put [:resolve www.example.com]; :put "lala";}
failure: dns name does not exist

```

You can catch this error and proceed with the script:

```ros
:onerror e {:put [:resolve www.example.com]} do={:put "resolver failed"}
:put "print after failure"

output:

resolver failed
print after failure
```

## Operations with Arrays

If a key name in an array contains any character other than a lowercase character, it should be put in quotes.
For example:

```ros
[admin@ce0] > {:local a { "aX"=1; ay=2 }; :put ($a->"aX")}
1
```

`foreach` command can be used to loop through keys and elements:

```ros
[admin@ce0] > :foreach k,v in={2; "aX"=1; y=2; 5} do={:put ("$k=$v")}

0=2
1=5
aX=1
y=2
```

If the `foreach` command is invoked with a single argument, it returns the element value:

```ros
[admin@ce0] > :foreach v in={2; "aX"=1; y=2; 5} do={:put ("$v")}

2
5
1
2
```

If an array element has a key, those elements are sorted alphabetically; elements without keys are placed before keyed elements and retain their order (as illustrated in the previous example).

It is possible to change the value of the single element using key name:

```
[admin@MikroTik] > :global a {x=1; y=2}
[admin@MikroTik] > :set ($a->"x") 5
[admin@MikroTik] > :environment print
a={x=5; y=2}

```

## Script permissions

Depending on how a script is called, it may:

- Use its own permissions.
- Inherit caller permissions.

For example, consider a user with full permissions and a script with no permissions set:

```
/user/print
Columns: NAME, GROUP, LAST-LOGGED-IN, INACTIVITY-POLICY
# NAME   GROUP  LAST-LOGGED-IN       INACTIVITY-POLICY
;;; system default user
0 admin  full   2025-07-22 17:09:59  none
```

```ros
/system script
add dont-require-permissions=no name=add-dhcp-no-perms owner=admin policy="" sour
ce="/ip dhcp-client add interface=ether2; put \"Added DHCP client on ether2!\""

```

Let's see what happens if we run the script with and without the `use-script-permissions` parameter:

```ros
[admin@MikroTik] > system/script/run add-dhcp-no-perms  use-script-permissions
not enough permissions (9)
[admin@MikroTik] > system/script/run add-dhcp-no-perms
Added DHCP client on ether2!
```

The scheduler follows the same rule. A script called by name in `on-event`, or with `/system script run`, runs with the scheduler entry's permissions (its `policy`). Only `use-script-permissions` makes the script run with its own permissions.

To compare, create two scheduler entries that run the same script in different ways:

```ros
/system scheduler
add interval=10s name=run-script-use-script-perms on-event="/system script run add-dhcp-no-perms use-script-permissions" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
add interval=10s name=run-script-by-name on-event=add-dhcp-no-perms policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
```

The log shows that the entry with `use-script-permissions` fails, because the script has no permissions. The entry that calls the script by name adds the DHCP client with the scheduler's permissions:

```ros
/log print
 2026-09-25 17:54:29 script,error executing script add-dhcp-no-perms
 2026-09-25 17:54:29 script,error,debug not enough permissions (9) (/ip/dhcp-client/add; line 1)
 2026-09-25 17:54:29 script,error executing script
 2026-09-25 17:54:29 script,error,debug (scheduler:run-script-use-script-perms) not enough permissions (9) (/ip/dhcp-client/add; line 1)
 2026-09-25 17:54:30 system,info dhcp client added by scheduler:run-script-by-name/script:add-dhcp-no-perms (*2 = /ip dhcp-client add interface=ether2)
```

A caller cannot run a script whose policy includes permissions the caller does not have: a scheduler entry with `policy=read` that calls a script with `policy=read,write` by name fails with `not enough permissions`. The `use-script-permissions` flag does not override this.

## See also

- [Scripting Examples](./scripting-examples.md)
- [Scripting Tips and Tricks](./scripting-tips-and-tricks.md)
