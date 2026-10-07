# API

> The API page introduces RouterOS's Application Programming Interface for secure communication with routers, detailing syntax rules, sentence structure, encoding methods, and supported commands like login and cancel...

# API

**Application Programming Interface (API)** lets users create custom software solutions to communicate with RouterOS for information gathering, adjusting configuration, and managing the router. The API closely follows the syntax of the **command-line interface (CLI)**. You can use it to create translated or custom configuration tools that make it easier to run and manage RouterOS routers.

The API service must be enabled before you try to establish a connection. By default, the API uses TCP ports **8728** and **8729** (secure).

The **API-SSL** service can operate in two modes: with or without a certificate. Without a certificate provided in the `/ip service` settings, the client must use an anonymous Diffie-Hellman cipher to establish a connection. If the service uses a certificate, the client can establish a TLS session.

## Protocol

You communicate with the router by sending sentences and receiving one or more sentences in return. A sentence is a sequence of words terminated by a zero-length word. A word is part of a sentence encoded in a certain way: encoded length followed by data. When the router receives a full sentence (command word, one or more attribute words, and a zero-length word), it evaluates and executes the sentence and then forms and returns a reply.

### API sentences

Sentence is the main object of communication with the API.

- Empty sentences are ignored.
- A sentence is processed after receiving zero length word.
- There is a limit on the number and size of sentences that the client can send before it has logged in.
- Do not rely on the order of attribute words, because the order and count can be changed by the `.proplist` attribute.

The sentence structure is as follows:

- The first word must contain a *command word*.
- The sentence must contain a *zero-length word* to terminate it.
- The sentence can contain zero or more *attribute words*. The order of attribute words does not matter.
- The sentence can contain zero or more *query words*. The order of query words is important.

:::danger
If a zero-length word is not provided, the router will not start evaluating the sent words and will consider all the following input as part of the same sentence.
:::

### API words

- Words are grouped into sentences. A zero-length word terminates a sentence.
- Each word is encoded as a length followed by that many bytes of content.
- The scheme allows encoding of lengths up to **0xFFFFFFFF**; only four-byte lengths are supported.
- **len** bytes are sent most significant first (network order).
- If the first byte of the word is **>= 0xF8**, it is a reserved control byte. After receiving an unknown control byte, an API client cannot proceed because it does not know how to interpret the following bytes.
- Currently, control bytes are not used.

The length of the word is encoded as follows:

| Value of length                |   # of bytes | Encoding                          |
|:--|--:|:--|
| `0 <= len <= 0x7F`             |            1 | len, lowest byte                  |
| `0x80 <= len <= 0x3FFF`        |            2 | len | 0x8000, two lower bytes     |
| `0x4000 <= len <= 0x1FFFFF`    |            3 | len | 0xC00000, three lower bytes |
| `0x200000 <= len <= 0xFFFFFFF` |            4 | len | 0xE0000000                  |
| `len >= 0x10000000`            |            5 | 0xF0 and len as four bytes        |

In general, *words* can be described like this `<encoded-word-length><word-content>`.
Word content can be separated into five parts: *[command word](#command-word)*, *[attribute word](#attribute-word)*, *[API attribute word](#api-attribute-word)*, *[query word](#query-word)*, and *[reply word](#reply-word)*

#### Command word

The first word in the sentence must be a command, followed by attribute words and a zero-length or terminating word. The name of the command word must begin with a slash (`/`). Names of commands closely follow the CLI. Spaces between path objects are not supported; they must be replaced with slashes (`/`).

Some commands are specific to API:

- `login` - used for login process to provide login credentials.
- `cancel` - used to cancel currently running command.

Command word structure in the strict order:

- encoded length
- content prefix */*
- CLI converted command

A few examples of command word content:

```ros
/login

```

```ros
/user/active/listen

```

```ros
/interface/vlan/remove

```

```ros
/system/reboot

```

#### Attribute word

Each *command word* has its list of *attribute words* depending on content.

The *attribute word* structure consists of five parts in this order:

- encoded length
- content is prefixed with equals (`=`) character
- attribute name
- equals (`=`) character as a name and value separator
- attribute value if there is one.

Some attribute examples (excluding encoded length prefix):

```ros
=address=10.0.0.1

```

```ros
=disable-running-check=yes

```

The value can contain *equal* (`=`) symbols:

```
=name=iu=c3Eeg

```

Value can be empty:

```ros
=comment=
```

Keep in mind that the order of attribute words and **API** parameters is not important and should not be relied on.

#### API attribute word

API attribute word structure is in the strict order:

- encoded length
- content is prefixed with the dot (`.`) character
- attribute name
- equals (`=`) character as a name and value separator
- attribute value

Currently, the only such API attribute is the [`tag`](#tags).

#### Query word

Sentences can have additional query parameters that restrict their scope. See the [query section](#queries) for details.

- Query words begin with `?`.
- Currently, only the `print` command handles query words.

Example of a sentence using query word attributes:

```ros
/interface/print
?type=ether
?type=vlan
?#|!

```

:::info
The order of query words is significant
:::

#### Reply word

It is only sent by the router in response to the full sentence received from the client.

- The first word of reply begins with `!`.
- Each sentence sent generates at least one reply (if a connection does not get terminated).
- The last reply for every sentence is the reply that has the first word `!done`.
- Errors and exceptional conditions begin with `!trap`.
- Data replies begin with `!re`.
- Replies of commands which do not have any data to reply with, begin with `!empty`.
- If the **API** connection must be closed, RouterOS sends a `!fatal` with a reason in a description and then closes the connection.

## Initial login

- The client sends a username and password in the first message. In our example, we use `admin` with an empty password:

  ```ros
  /login
  =name=admin
  =password=
  ```

  The router replies with `!done` if authentication is successful.

- The password is sent in plain text.
- If an error occurs, the reply contains `=message=<error message>`.
- After a successful login, the client can start issuing commands.

## Tags

The **API** allows running several commands simultaneously without waiting for the previous one to complete. If the API client does this and needs to differentiate command responses, it can use the `tag` parameter in the command sentences.

If a sentence contains a `tag`, each reply for that sentence will carry the same tag value.

If you omit the `tag` parameter or leave it empty, responses for the command will not include a tag parameter.

## Command description

- `/cancel`
  - Optional argument: `=tag=<tag of command to cancel>`; without it, all running commands are cancelled.
  - Does not cancel itself.
  - All canceled commands are interrupted and usually generate `!trap` and `!done` responses.
  - Note that `/cancel` is a separate command and can have its own unique `.tag` parameter that is not related to the command's `=tag` argument.

- `listen`
  - The `listen` command is available wherever the CLI `print` command is available, but it may not work everywhere.
  - `!re` sentences are generated when something changes in a particular item list.
  - When an item is deleted or disappears, the `!re` sentence includes the value `=.dead=yes`.
  - This command does not terminate on its own; use the `/cancel` command to stop it.

- `getall`
  - The `getall` command is available wherever the CLI `print` command is available (`getall` is an alias for `print`).
  - Replies contain a `=.id=<item internal number>` property.

- `print`
  - The API `print` command differs from the CLI counterpart in the following ways:
    - The `where` argument is not supported; items can be filtered using [query words](#queries).
    - The `.proplist` argument is a comma-separated list of property names to include in returned items.
      - Returned items may have additional properties.
      - The order of returned properties is not significant and cannot be relied on.
      - If the list contains duplicate entries, handling of those duplicates is undefined.
      - If a property appears in `.proplist` but is absent from an item, that item does not have the property value (`?name` evaluates to false for that item).
      - If `.proplist` is absent, all properties are included as requested by the `print` command, even those with slow access time (such as file contents and performance counters). Therefore, use of `.proplist` is encouraged. Omitting `.proplist` may incur a high performance penalty if the `=detail=` argument is set.

### Queries

The `print` and `getall` commands accept query words that limit the set of returned sentences.

- Query words begin with `?`.
- The order of query words is significant. A query is evaluated starting from the first word.
- A query is evaluated for each item in the list. If the query succeeds, the item is processed, if a query fails, the item is ignored.
- A query is evaluated using a stack of boolean values. Initially, the stack contains an infinite amount of `true` values. At the end of the evaluation, if the stack contains at least one `false` value, the query fails.
- Query words operate according to the following rules:

| Query                            | Description                                |
|:--|:--|
| `?name`                        | pushes `true` if an item has a value of property `name`, `false` if it does not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `?-name`                       | pushes `true` if an item does not have a value of property `name`, `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `?name=x` | pushes `true` if the property `name` has a value equal to *x*, `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `?<name=x`                   | pushes `true` if the property `name` has a value less than *x*, `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `?>name=x`                   | pushes `true` if the property `name` has a value greater than *x*, `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `?#operations`               | applies operations to the values in the stack. operation string is evaluated from left to right.the sequence of decimal digits followed by any other character or end of the word is interpreted as a stack index. top value has an index 0.an index that is followed by a character pushes a copy of the value at that index.an index that is followed by the end of the word replaces all values with the value at that index.`!` character replaces the top value with the opposite.<code>&amp;</code> pops two values and pushes the result of logical `and` operation.`\|` pops two values and pushes the result of logical `or` operation.`.` after an index does nothing.`.` after another character pushes a copy of the top value. |

:::info
Regular expressions are not supported in API, so do not try to send a query with the **`~`** symbol
:::

Examples:

- Get all ethernet and VLAN interfaces (equivalent to CLI command `/interface/print where type=ether || type=vlan`):

```ros
/interface/print
?type=ether
?type=vlan
?#|

```

- Get all routes that have a non-empty comment (equivalent to CLI command `/ip/route/print where comment`):

```ros
/ip/route/print
?>comment=

```

- Get all routes that do not have distance greater than 1 and gateway equal to 172.16.1.1 (equivalent to CLI command `/ip/route/print where !(distance>1 && gateway=172.16.1.1)`):

```ros
/ip/route/print
?>distance=1
?gateway=172.16.1.1
?#&!

```

### OID

The `print` command can return OID values for properties that are available in SNMP.

In the CLI, OID values can be seen by running the `print oid` command. In the API, these properties have names that end with `.oid` and can be retrieved by adding their names to the value of `.proplist`. An example:

```ros
/system/resource/print
=.proplist=uptime,cpu-load,uptime.oid,cpu-load.oid
```

The router sends a reply:

```ros
!re
=uptime=01:22:53
=cpu-load=0
=uptime.oid=.1.3.6.1.2.1.1.3.0
=cpu-load.oid=.1.3.6.1.2.1.25.3.3.1.2.1

!done
```

### !trap

When an API sentence fails for any reason, the router returns a trap accompanied by a:

- A `message` attribute that provides more details about the failure.
- A `category` attribute. If the error is general, the router returns the error category. Possible values for this attribute are:
  - 0 - missing item or command
  - 1 - argument value failure
  - 2 - execution of command interrupted
  - 3 - scripting related failure
  - 4 - a general failure
  - 5 - API related failure
  - 6 - TTY related failure
  - 7 - value generated with :return command

```ros
/ip/address/add
=address=192.168.88.1
=interface=asdf
```

Router reply with:

```bash
!trap
=category=1
=message=input does not match any value of interface
```

## Modify existing items

Like its CLI counterpart, the API has a `set` command that accepts an item's ID and parameters to set.
The only exception is that the API does not accept queries directly with the `set` command. For example, CLI command to set MTU value on all ethernet interfaces:

```ros
/interface set [find where type=ether] mtu=1500
```

To achieve the same with API, you first need to run a `print` query to get IDs, and only then execute the `set` command.

```ros
/interface/print
=.proplist=.id
?type=ether
```

Router reply with:

```bash
!re
=.id=*1

!re
=.id=*2
```

Now you need to loop through returned IDs and send the `set` command for each:

```ros
/interface/set
=.id=*1
=mtu=1500

/interface/set
=.id=*2
=mtu=1500
```

## Command examples

### `/user/active/listen`

```ros
/user/active/listen

!re
=.id=*68
=radius=no
=when=2006-10-24 08:40:42
=name=admin
=address=0.0.0.0
=via=console

!re
=.id=*68
=.dead=yes

... more !re sentences ...
```

### /cancel, simultaneous commands

Start listening for interface changes (tag is 2):

```ros
/interface/listen
.tag=2
```

Send a command to disable interface (tag is 3):

```ros
/interface/set
=disabled=yes
=.id=ether1
.tag=3
```

The router replies with `!done` for the `disable` command (executed with tag 3):

```ros
!done
.tag=3
```

Enable interface (tag is 4):

```ros
/interface/set
=disabled=no
=.id=ether1
.tag=4
```

Client receives from the router an update for the `listen` command generated by a change made by the first `set` command (executed with tag 3):

```ros
!re
=.id=*1
=disabled=yes
=dynamic=no
=running=no
=name=ether1
=mtu=1500
=type=ether
.tag=2
```

Followed by `done` for `enable` command (executed with tag 4):

```ros
!done
.tag=4
```

Send a command to get interface list (tag is 5):

```ros
/interface/getall
.tag=5
```

Client receives updates generated by a change made by the second `set` command (executed with tag 4):

```ros
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=2
```

Client receives replies to `getall` command (executed with tag 5):

```ros
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=5

!re
=.id=*2
=disabled=no
=dynamic=no
=running=yes
=name=ether2
=mtu=1500
=type=ether
.tag=5

!done
.tag=5
```

Stop listening - request to cancel command with tag 2, `cancel` itself uses tag 7:

```ros
/cancel
=tag=2
.tag=7
```

`listen` command is interrupted (tag 2):

```ros
!trap
=category=2
=message=interrupted
.tag=2
```

`cancel` command is finished (tag 7):

```ros
!done
.tag=7
```

`listen` command is finished (tag 2):

```ros
!done
.tag=2
```

## Example client

A simple [API client in Python3](./python3-example.md)

Example output with the old login method:

```bash
debian@localhost:~/api-test$ ./api.py 10.0.0.1 admin ''
<<< /login
<<<
>>> !done
>>> =ret=93b438ec9b80057c06dd9fe67d56aa9a
>>>
<<< /login
<<< =name=admin
<<< =response=00e134102a9d330dd7b1849fedfea3cb57
<<<
>>> !done
>>>
/user/getall

<<< /user/getall
<<<
>>> !re
>>> =.id=*1
>>> =disabled=no
>>> =name=admin
>>> =group=full
>>> =address=0.0.0.0/0
>>> =netmask=0.0.0.0
>>>
>>> !done
>>>
```
