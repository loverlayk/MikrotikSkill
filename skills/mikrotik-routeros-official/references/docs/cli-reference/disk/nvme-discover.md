# nvme-discover

> RouterOS command reference for /disk/nvme-discover.

-----------

## disk/nvme-discover 
**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="ipAddr">IP address of the NVMe over TCP controller.</ArgTableRow>
<ArgTableRow arg="port" typ="num">TCP port of the controller's discovery service. Default: 4420.</ArgTableRow>
<ArgTableRow arg="host-name" typ="string">Host NQN this router presents to the controller, used for identification and host-based access control.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="nqn" typ="string">NVMe Qualified Name of a subsystem the controller exposes.</ArgTableRow>
</ArgTable>
