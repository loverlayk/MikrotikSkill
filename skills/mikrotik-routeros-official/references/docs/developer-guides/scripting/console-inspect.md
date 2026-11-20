# Console inspect

> Use /console/inspect to discover RouterOS menus, commands and arguments, read command help, get tab-completion candidates and syntax highlighting, and check command lines from the console, scripts and the REST API.

The `/console/inspect` command returns the data the console uses for command completion, syntax highlighting, and built-in help. Scripts and external tools use it to discover menus, commands, arguments, and value types, or to check a command line before running it. The same data is available over the REST API at `/rest/console/inspect`.

## Requests

The `request` argument is a set of flags. Combine values with commas, for example `request=child,completion`. Each returned row has a `type` field that names the request that produced it.

| Request | Returns |
| :-- | :-- |
| `self` | The addressed node and its children. |
| `child` | The same rows as `self`. Use it to walk the command tree. |
| `completion` | Tab-completion candidates for `input`. |
| `syntax` | Built-in help for a path, or the syntax that applies at the end of `input`. |
| `highlight` | One style for each character of `input`. |
| `error` | Accepted by the command but adds no rows. Use `highlight` to find invalid input. |

## Paths and input

- `path` selects a menu or command with a comma-separated list of names, for example `ip,address,add`. Omit it for the root menu.
- Do not use slashes or a leading slash in `path`. Names are case-sensitive.
- `input` is the command line to analyze. It can be an absolute path such as `/ip/address/print`, or a path relative to `path`.
- `self`, `child`, and `syntax` with `path` read `path`. `completion`, `highlight`, `syntax` with `input`, and `error` read `input`.
- In a REST body, pass `path` as a string, for example `"path":"ip,address,add"`. A JSON array is not accepted.

## Discover menus and arguments

Use `child` to list the entries at a path. Without `path`, it lists the root menu.

```ros
/console/inspect request=child path=console,inspect
```

```text
Columns: TYPE, NAME, NODE-TYPE
TYPE   NAME            NODE-TYPE
self   inspect         cmd
child  as-value        arg
child  input           arg
child  path            arg
child  proplist        arg
child  request         arg
child  without-paging  arg
```

The first row is the addressed node, and its `type` is `self`. The other rows are its children, and their `type` is `child`. The `node-type` field tells what each row is:

- `path` — A top-level menu path, such as `ip` or `system`.
- `dir` — A menu directory, such as `ip,address` or `console,settings`.
- `cmd` — A command, such as `add` or `print`.
- `arg` — A command argument, such as `address` or `interface`.

To walk the whole command tree, start with `request=child` from the root, then use the name of each `dir` or `path` row as the next `path` value.

## Read built-in help

`syntax` returns the text of the built-in help. With `path`, it describes the entries at that path. The result is a flat table: the first row is only the collection container, and each following row is one entry with its help text. Read the `Symbol` and `Text` columns; the other columns describe the structure of the help tree.

```ros
/console/inspect request=syntax path=ip,address,add
```

| Type | Symbol | Symbol type | Nested | Nonorm | Text |
| :-- | :-- | :-- | :-- | :-- | :-- |
| syntax |  | collection | 0 | true |  |
| syntax | `address` | explanation | 1 | false | Local IP address |
| syntax | `broadcast` | explanation | 1 | false | Broadcast address |
| syntax | `comment` | explanation | 1 | false | Short description of the item |
| syntax | `copy-from` | explanation | 1 | false | Item number |
| syntax | `disabled` | explanation | 1 | false | Defines whether item is ignored or used |
| syntax | `interface` | explanation | 1 | false | Interface name |
| syntax | `netmask` | explanation | 1 | false | Network mask |
| syntax | `network` | explanation | 1 | false | Network prefix |

The `symbol-type` field is `explanation` for each argument row. The first row has `symbol-type` set to `collection`, an empty `symbol`, and `nested` set to `0`; it is only the container for the list. The `nested` field is the depth in the help tree, and `nonorm` is a console-internal flag you can ignore.

With `input`, `syntax` describes the syntax that applies at the end of the command line. When the line ends with an argument followed by `=`, the result is a type tree for that argument.

```ros
/console/inspect request=syntax input="/ip/address/add address="
```

| Type | Symbol | Symbol type | Nested | Nonorm | Text |
| :-- | :-- | :-- | :-- | :-- | :-- |
| syntax | `Address` | definition | 0 | false | Address[/Netmask] |
| syntax | `Address` | definition | 1 | false | A.B.C.D (IP address) |
| syntax | `Netmask` | definition | 1 | false | IpNetmask \| Num |
| syntax | `IpNetmask` | definition | 2 | false | A.B.C.D |
| syntax | `Num` | definition | 2 | false | 0..32 (integer number) |

The table above is a type tree, not a list of command entries. It says that `address` expects an `Address[/Netmask]`. An `Address` is an IP address, and a `Netmask` is either an `IpNetmask` (`A.B.C.D`) or a `Num` from `0` to `32`. The `nested` column gives the depth in the tree: `0` for the argument type, `1` for its alternatives, and `2` for the parts of an alternative.

## Get completion candidates

`completion` returns the candidates for the text in `input`. Completion assumes the cursor is at the end of the string. Add a trailing space to get the arguments of a command.

```ros
/console/inspect request=completion input="/ip/addr"
```

| Type | Completion | Style | Offset | Preference | Show | Text |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| completion | `address` | dir | 4 | 96 | true | Address management |
| completion | `/` | dir | 8 | 95 | true | top of command hierarchy |
| completion | ` ` | none | 8 | -1 | false | whitespace |
| completion | `{` | syntax-meta | 8 | 40 | false | start of command block |
| completion | `;` | syntax-meta | 8 | 40 | false | end of command |

The fields have these meanings:

- `completion` — The text to insert.
- `offset` — The zero-based character position in `input` where the candidate applies.
- `preference` — The ordering weight. Higher values are offered before lower values.
- `show` — Whether the candidate appears in the interactive Tab list.
- `style` — The style class of the candidate.
- `text` — The description of the candidate.

Use `path` to set the menu for input that does not start with an absolute path. For example, `path=ip,address input="pr"` returns the `print` command.

## Check syntax with highlighting

`highlight` returns one row. The `highlight` field holds one style for each character of `input`, in the same order.

```bash
curl -k -u monitoring -X POST \
    https://192.168.88.1/rest/console/inspect \
    -H "Content-Type: application/json" \
    --data '{"request":"highlight","input":"/badcmd"}'
```

```json
[{"highlight":"dir,obj-inactive,obj-inactive,obj-inactive,obj-inactive,obj-inactive,obj-inactive","type":"highlight"}]
```

The first character `/` is a valid directory separator and has the `dir` style. The rest of the input is an unknown command and has the `obj-inactive` style. Common style values are `dir`, `cmd`, `arg`, `none`, and `syntax-meta`. The values `error`, `obj-inactive`, and `syntax-obsolete` mark input the console cannot use.

To find the first invalid character in a command line, check the styles in a script:

```ros
:local line "/badcmd"
:local result [/console/inspect request=highlight input=$line as-value]
:local styles ($result->"highlight")
:foreach index,style in=$styles do={
    :if (($style="error") or ($style="obj-inactive") or ($style="syntax-obsolete")) do={
        :put "Invalid input at character $index ($style)"
    }
}
```

## Response fields

Each request fills only the fields it needs. Every value is a string.

| Field | Request | Description |
| :-- | :-- | :-- |
| `type` | All | The request that produced the row: `self`, `child`, `completion`, `highlight`, `syntax`, or `error`. |
| `name` | `self`, `child` | The name of the menu, command, or argument. |
| `node-type` | `self`, `child` | The kind of node: `path`, `dir`, `cmd`, or `arg`. |
| `completion` | `completion` | The text to insert. |
| `style` | `completion`, `highlight` | The style class of a candidate or of a character. |
| `offset` | `completion` | The zero-based character position in `input`. |
| `preference` | `completion` | The ordering weight of the candidate. |
| `show` | `completion` | Whether the candidate appears in the Tab list. |
| `text` | `completion`, `syntax` | A description, help text, or value type description. |
| `symbol` | `syntax` | The name of the described symbol. |
| `symbol-type` | `syntax` | `collection`, `explanation`, or `definition`. |
| `nested` | `syntax` | The nesting level. The collection row is `0`, and its entries start at `1`. |
| `nonorm` | `syntax` | A console-internal flag. The collection row sets it to `true`. |
| `highlight` | `highlight` | The style of each character in `input`, in order. |

## Use over the REST API

Send a POST request to `/rest/console/inspect` with the same arguments in a JSON body:

```bash
curl -k -u monitoring -X POST \
    https://192.168.88.1/rest/console/inspect \
    -H "Content-Type: application/json" \
    --data '{"request":"completion","input":"/ip/addr"}'
```

```json
[{"completion":"address","offset":"4","preference":"96","show":"true","style":"dir","text":"Address management","type":"completion"},{"completion":"/","offset":"8","preference":"95","show":"true","style":"dir","text":"top of command hierarchy","type":"completion"},{"completion":" ","offset":"8","preference":"-1","show":"false","style":"none","text":"whitespace","type":"completion"},{"completion":"{","offset":"8","preference":"40","show":"false","style":"syntax-meta","text":"start of command block","type":"completion"},{"completion":";","offset":"8","preference":"40","show":"false","style":"syntax-meta","text":"end of command","type":"completion"}]
```

Use `.proplist` to limit the returned fields:

```bash
curl -k -u monitoring -X POST \
    https://192.168.88.1/rest/console/inspect \
    -H "Content-Type: application/json" \
    --data '{"request":"child","path":"ip,address,add",".proplist":"name,node-type"}'
```

The command requires read access to the menus and commands you inspect. It does not change the configuration.

## See also

- [CLI reference: console/inspect](../../cli-reference/console/inspect)
- [Console](../../management-tools/console)
- [REST API](../rest-api)
