# API

> The API page introduces RouterOS's Application Programming Interface for secure communication with routers, detailing syntax rules, sentence structure, encoding methods, and supported commands like login and cancel...

# API

**Application Programming Interface (API)** lets users create custom software solutions to communicate with RouterOS for information gathering, adjusting configuration, and managing the router. The API closely follows the syntax of the **command-line interface (CLI)**. You can use it to create translated or custom configuration tools that make it easier to run and manage RouterOS routers.

The API service must be enabled before you try to establish a connection — enable it with `/ip/service set api disabled=no`. By default, the API uses TCP ports **8728** and **8729** (secure).

The **API-SSL** service can operate in two modes: with or without a certificate. Without a certificate configured for the service, the service offers only anonymous Diffie-Hellman ciphers, which current TLS clients do not accept, so the connection fails with a handshake error. With a certificate configured for the service, the client can establish a regular TLS session. For the service settings, see [the `ip/service` CLI reference](../../cli-reference/ip/service).

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
- The encoding supports lengths up to **0xFFFFFFFF**; the five-byte form (`0xF0` + four bytes) encodes the largest lengths.
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

```ros
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

The `login` command supports two authentication methods.

Plain-text password — the method used by accounts created with the current password format:

```ros
/login
=name=admin
=password=
```

The router replies with `!done` if authentication is successful. The password is sent in plain text. After a successful login, the client can start issuing commands.

If the credentials are wrong or the account cannot use the API, the router replies with an error:

```ros
!trap
=message=invalid user name or password

!done
```

Legacy challenge-response — the method used by accounts created with the older password format:

When the router answers a login with `=ret=<challenge>` instead of a plain `!done`, the login uses the legacy method. A login sentence without a password is answered with a challenge, for example:

```ros
/login

!done
=ret=93b438ec9b80057c06dd9fe67d56aa9a
```

The client answers in the second message with the user name and the challenge response: the two characters `00` followed by the lowercase hex MD5 digest of the `0x00` byte, the password and the received challenge.

```ros
/login
=name=admin
=response=00e134102a9d330dd7b1849fedfea3cb57

!done
```

Accounts with the current password format cannot complete the legacy exchange; the router rejects the response.

Closing the TCP connection ends the API session.

## Tags

The **API** allows running several commands simultaneously without waiting for the previous one to complete. To tell the replies apart, add the API attribute word `.tag=<value>` to the command sentence; every reply for that sentence then carries the same `.tag=<value>` word.

If you omit the `.tag` word or leave its value empty, replies for the command carry no tag.

Note the distinction between the tag and an argument named `tag`: the tag is an API attribute word (`.tag=`), while a command argument such as `/cancel`'s `=tag=` is a regular attribute word (`=name=value`).

## Command description

- `/cancel`
  - Optional argument: `=tag=<tag of command to cancel>`; without it, all running commands are cancelled.
  - Does not cancel itself.
  - All canceled commands are interrupted and usually generate `!trap` and `!done` responses.
  - Note that `/cancel` is a separate command and can have its own unique `.tag` parameter that is not related to the command's `=tag` argument.

- `listen`
  - The `listen` command is available wherever the CLI `print` command is available, but it may not work everywhere.
  - `!re` sentences are generated when something changes in a particular item list.
  - When an item is deleted or disappears, the `!re` sentence includes the boolean value `=.dead=true`.
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

In the CLI, OID values can be seen by running the `print oid` command. In the API, properties that have an OID expose it through a property whose name ends with `.oid`; add those names to the value of `.proplist` to retrieve them. An example:

```ros
/system/resource/print
=.proplist=uptime,cpu-frequency,uptime.oid,cpu-frequency.oid
```

The router sends a reply:

```ros
!re
=uptime=16m44s
=cpu-frequency=864
=uptime.oid=.1.3.6.1.2.1.1.3.0
=cpu-frequency.oid=.1.3.6.1.4.1.14988.1.1.3.14.0

!done
```

Not every SNMP property is exposed through the API. The properties that have an OID are the ones the router shows with the `print oid` command; a property without an OID, such as `cpu-load` for the system resources, has no `.oid` counterpart.

### !trap

When an API sentence fails, the router returns a trap sentence. The trap carries a `message` attribute with details about the failure; some traps also carry a `category` attribute with the error category:

- 0 - missing item or command
- 1 - argument value failure
- 2 - execution of command interrupted
- 3 - scripting related failure
- 4 - a general failure
- 5 - API related failure
- 6 - TTY related failure
- 7 - value generated with :return command

For example, an unknown command returns a trap with `=category=0`:

```ros
/foobar/print
```

Router reply with:

```ros
!trap
=category=0
=message=no such command or directory (foobar)

!trap
=message=no such command prefix

!done
```

A wrong argument value returns a trap with only a `message`:

```ros
/ip/address/add
=address=192.168.88.1
=interface=asdf
```

Router reply with:

```ros
!trap
=message=input does not match any value of interface

!done
```

## Modify existing items

Like its CLI counterpart, the API has a `set` command that accepts an item's ID and parameters to set. The value of the `.id` attribute can be the internal number (for example `*1`) or, for items that have a name, the name (for example `ether1`).
The only exception is that the API does not accept queries directly with the `set` command. For example, the CLI command to set the MTU on all ethernet interfaces:

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

The router answers a successful `set` with a single `!done` (no data), and with `!trap` if the item was not found.

## Command examples

### listen notifications

Start listening for changes in the interface list:

```ros
/interface/listen
```

The router sends an `!re` sentence whenever an item appears or changes. When an item is removed, the `!re` sentence carries the boolean `=.dead=true`:

```ros
!re
=.id=*1
=name=ether1
=disabled=false
=running=true

!re
=.id=*1
=.dead=true
```

Stop listening with `/cancel`.

### /cancel, simultaneous commands

Start listening for interface changes (tag is 2):

```ros
/interface/listen
.tag=2
```

Send a command to disable the interface (tag is 3):

```ros
/interface/set
=disabled=true
=.id=ether1
.tag=3
```

The router replies with `!done` for the `disable` command (executed with tag 3); the change also generates an update for the `listen` command (tag 2):

```ros
!re
=.id=*1
=disabled=true
=dynamic=false
=running=false
=name=ether1
=mtu=1500
=type=ether
.tag=2

!done
.tag=3
```

Enable the interface (tag is 4):

```ros
/interface/set
=disabled=false
=.id=ether1
.tag=4
```

The change generates another update for the `listen` command, followed by `done` for the `enable` command:

```ros
!re
=.id=*1
=disabled=false
=dynamic=false
=running=true
=name=ether1
=mtu=1500
=type=ether
.tag=2

!done
.tag=4
```

Send a command to get the interface list (tag is 5):

```ros
/interface/getall
.tag=5
```

The client receives replies to the `getall` command (executed with tag 5):

```ros
!re
=.id=*1
=disabled=false
=dynamic=false
=running=true
=name=ether1
=mtu=1500
=type=ether
.tag=5

!re
=.id=*2
=disabled=false
=dynamic=false
=running=true
=name=ether2
=mtu=1500
=type=ether
.tag=5

!done
.tag=5
```

Stop listening — request cancelling the command with tag 2; `cancel` itself uses tag 7:

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

A simple [API client in Python3](./python3-example.md) that supports both login methods and prints the whole exchange on the terminal.
