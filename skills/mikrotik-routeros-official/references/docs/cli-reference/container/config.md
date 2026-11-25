# config

> Settings for all containers: registry, download directory and global memory limits.

-----------

## container/config 
**Package:** container
**Type:** Settings Directory

Settings for all containers: registry, download directory and global memory limits.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="registry-url" typ="string">Registry to download images from, for example `https://registry-1.docker.io`. When empty, the registry in `assumed-registry-url` is used.</ArgTableRow>
<ArgTableRow arg="username" typ="string">User name for the registry.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password for the registry. It is a [sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters) value.</ArgTableRow>
<ArgTableRow arg="layer-dir" typ="file">Directory for image layers that containers can share.</ArgTableRow>
<ArgTableRow arg="tmpdir" typ="file">Directory where downloaded images are extracted. Use an attached disk.</ArgTableRow>
<ArgTableRow arg="memory-high" typ="num">Global soft memory limit for each container. If a container has its own value, the lower one applies. Default: `unlimited`.</ArgTableRow>
<ArgTableRow arg="memory-max" typ="num">Global hard memory limit for each container. If a container has its own value, the lower one applies. Values below 1 MB are refused. Default: `unlimited`.</ArgTableRow>
<ArgTableRow arg="swap-max" typ="num">Global swap limit for each container. If a container has its own value, the lower one applies. Requires swap on the router. Default: `unlimited`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-registry-url" typ="string">Registry used when `registry-url` is empty: `docker.io`.</ArgTableRow>
<ArgTableRow arg="memory-current" typ="num">Memory all containers use now.</ArgTableRow>
<ArgTableRow arg="swap-current" typ="num">Swap all containers use now.</ArgTableRow>
</ArgTable>
