# CLI Reference Version Comparison

> Compare parameters between two RouterOS CLI reference versions.

Every RouterOS release brings a new CLI reference: commands and parameters are
added, renamed, and removed as features evolve. Select two versions below to
see which parameters were added and which were removed between them.

<CliCompare />

## How the comparison works

- The data is generated from the versioned CLI reference pages in this
  repository (`versioned_docs/version-*/cli-reference`), so it reflects the
  published pages, not the RouterOS source itself.
- **Parameters** are the arguments of a command or menu, including read-only
  arguments. **Flags** are item properties such as `disabled`, `running`, and
  `invalid`.
- A command or menu is listed under *New commands* or *Removed commands* when
  the whole page is missing from the other version.
- Directory pages (for example `ip/firewall`) list the parameters of every
  entry of that menu, so a removed parameter there may actually have moved to
  a submenu page.
