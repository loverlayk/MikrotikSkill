# save

> Saves a container as an OCI image archive. The command returns at once and the archive is written in the background; wait until the file stops growing before you copy it. See Saving a container.

-----------

## container/save 
**Package:** container
**Type:** Command

Saves a container as an OCI image archive. The command returns at once and the archive is written in the background; wait until the file stops growing before you copy it. See [Saving a container](../../containers/#saving-a-container).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file">Archive to write, for example `disk1/nginx.tar`.</ArgTableRow>
<ArgTableRow arg="commit" typ="switch" unset="1">Adds the root directory content as a layer and the container's settings (entrypoint, cmd, environment) to the image configuration, so other container engines see the changes.</ArgTableRow>
<ArgTableRow arg="name" typ="string" unset="1">Image name to save the archive as.</ArgTableRow>
</ArgTable>
