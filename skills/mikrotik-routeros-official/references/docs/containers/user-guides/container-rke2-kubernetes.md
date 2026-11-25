# Container - Kubernetes (RKE2) single-node cluster

> This guide shows how to install a single-node Kubernetes cluster on a ROSE Data Server (RDS) with the RKE2 container for RouterOS: storage, network, configuration files, the container itself, and access with kubectl...

# Container - Kubernetes (RKE2) single-node cluster

[RKE2](https://docs.rke2.io/) is a Kubernetes distribution from Rancher. MikroTik publishes an RKE2 container image for RouterOS, [mikrotik/rke2](https://hub.docker.com/r/mikrotik/rke2). This guide runs it as a single-node Kubernetes cluster on a ROSE Data Server (RDS) with the [Calico](https://docs.tigera.io/calico/latest/about/) network plugin.

:::warning
The image is published for testing. The container runs with `privileged=yes`. Run it on a router that you can dedicate to this task.
:::

## Requirements

- A [ROSE Data Server](https://mikrotik.com/product/rds2216). RKE2 has its own [hardware requirements](https://docs.rke2.io/install/requirements#hardware) for processor and memory.
- Two U.2 NVMe disks of at least 100 GB each, inserted in the first two slots. The guide deletes all data on them.
- The `container` and `rose-storage` [packages](../../getting-started/installation-and-upgrade/packages).
- Container mode enabled in [device-mode](../../system-information-and-utilities/device-mode).
- Access from the router to Docker Hub, or to a private container registry.

The examples use these values. Replace them with the values of your network:

| Value | Meaning |
| :-- | :-- |
| `bridge` | Bridge of the network where the cluster is reachable. This is the bridge of the default configuration |
| `192.168.1.1` | Gateway of this network |
| `192.168.1.2` | Address of the router |
| `192.168.1.3` | Address of the RKE2 container, and of the Kubernetes API. Use an address that no other device has and that is outside the DHCP pool |
| `rke2.k8s` | Host name of the node |
| `192.168.192.0/19` | Pod network inside the cluster |
| `192.168.224.0/19` | Service network inside the cluster |

The pod and service networks exist only inside the cluster. Change them only when they overlap with networks that the cluster must reach.

## Prepare the router

### Packages and device-mode

Enable the two packages. The router reboots when the changes are applied. If both packages are already enabled, skip this step:

```ros
/system/package/enable container
/system/package/enable rose-storage
/system/package/apply-changes
```

Check that container mode is enabled:

```ros
/system/device-mode/print
```

If the output shows `container: no`, enable it and confirm with the reset button of the router when the command asks for it. The router reboots:

```ros
/system/device-mode/update container=yes
```

### Time

Kubernetes components reject TLS certificates when the clock is wrong. The container uses the clock of the router. Enable the NTP client of the router and use the NTP server of your network:

```ros
/system/ntp/client/servers/add address=pool.ntp.org
/system/ntp/client/set enabled=yes
```

### Storage

RouterOS adds only disks without a file system to an array. If the disks were in use before, wipe them first:

```ros
/disk/format nvme1 file-system=wipe-quick
/disk/format nvme2 file-system=wipe-quick
```

Create a RAID 1 array from the two disks and format it. All data of the container and of the cluster is stored on this array:

```ros
/disk/add type=raid slot=raid1 raid-type=1 raid-device-count=2
/disk/set nvme1 raid-master=raid1 raid-role=0
/disk/set nvme2 raid-master=raid1 raid-role=1
/disk/format raid1 file-system=ext4 label=containers
```

:::warning
Wiping and formatting delete all data on both disks.
:::

See [RAID](../../storage/raid) for the RAID types and for other disk layouts.

### Network

The container connects to the network through a virtual Ethernet (veth) interface that is a port of the bridge:

```ros
/interface/veth/add name=ens18 address=192.168.1.3/24 \
    gateway=192.168.1.1
/interface/bridge/port/add bridge=bridge interface=ens18
/interface/bridge/settings/set use-ip-firewall=yes
```

The cluster requires `use-ip-firewall=yes`. With this setting, the traffic that the bridge forwards passes the IP firewall of the router. The setting applies to all bridges of the router.

:::warning
The container is a port of the bridge, so every device in this network reaches it directly. This includes the Kubernetes API on port 6443. Use a network that you trust, or a separate bridge or VLAN for the cluster.
:::

## Create the configuration files

### Directories

Create the directories for the container layers and for the RKE2 data and configuration:

```ros
/file/add type=directory name=raid1/containers/tmp
/file/add type=directory name=raid1/containers/layers
/file/add type=directory name=raid1/rke2/ntp
/file/add type=directory name=raid1/rke2/etc
/file/add type=directory name=raid1/rke2/data/server/manifests
```

RKE2 installs every manifest file that it finds in `raid1/rke2/data/server/manifests` when it starts.

### NTP

The container runs its own NTP daemon. Create its configuration file and replace the servers with the NTP servers of your network:

```ros
/file/add type=file name=raid1/rke2/ntp/ntp.conf contents="
driftfile /var/lib/ntpsec/ntp.drift
leapfile /usr/share/zoneinfo/leap-seconds.list

server 0.pool.ntp.org iburst
server 1.pool.ntp.org iburst

restrict default kod nomodify nopeer noquery limited
restrict 127.0.0.1
restrict ::1
"
```

### Calico

This file configures the Calico network plugin: VXLAN between pods, the iptables data plane, and the pod network. `cidr` must be the same as `--cluster-cidr` of the RKE2 container, and `blockSize` the same as `node-cidr-mask-size`. `interface` is the name of the veth interface.

```ros
/file/add type=file \
    name=raid1/rke2/data/server/manifests/rke2-calico-config.yaml \
    contents="---
apiVersion: helm.cattle.io/v1
kind: HelmChartConfig
metadata:
  name: rke2-calico
  namespace: kube-system
spec:
  failurePolicy: abort
  valuesContent: |-
    apiServer:
      enabled: true
    goldmane:
      enabled: true
    whisker:
      enabled: true
    felixConfiguration:
      featureDetectOverride: ChecksumOffloadBroken=false
      logSeverityScreen: Warning
      logSeveritySys: Warning
      wireguardEnabled: false
    installation:
      backend: VXLAN
      calicoNetwork:
        bgp: Disabled
        linuxDataplane: Iptables
        ipPools:
          - blockSize: 21
            cidr: 192.168.192.0/19
            encapsulation: VXLANCrossSubnet
            natOutgoing: Enabled
            nodeSelector: all()
        nodeAddressAutodetectionV4:
          interface: ens18
"
```

Use the iptables data plane (`linuxDataplane: Iptables`) in RouterOS containers. See the [rke2-calico chart](https://github.com/rancher/rke2-charts/tree/main/charts/rke2-calico/rke2-calico) for all values.

The second file enables the [Calico Ingress Gateway](https://docs.tigera.io/calico/latest/networking/ingress-gateway/about-calico-ingress-gateway), which provides the Kubernetes Gateway API:

```ros
/file/add type=file \
    name=raid1/rke2/data/server/manifests/rke2-calico-custom.yaml \
    contents="---
apiVersion: operator.tigera.io/v1
kind: GatewayAPI
metadata:
  name: default
"
```

### Private registry (optional)

If the router has no direct Internet access, RKE2 can pull its images from a private registry. Create a [registry configuration](https://docs.rke2.io/install/private_registry) with the address of your registry:

```ros
/file/add type=file name=raid1/rke2/registries.yaml contents="
mirrors:
  docker.io:
    endpoint:
      - https://registry.example.com
  ghcr.io:
    endpoint:
      - https://registry.example.com
"
```

### cert-manager and Rancher (optional)

[Rancher](https://ranchermanager.docs.rancher.com/) is a web interface for Kubernetes clusters. It needs cert-manager. Skip both files if you manage the cluster only with `kubectl`.

```ros
/file/add type=file \
    name=raid1/rke2/data/server/manifests/cert-manager.yaml \
    contents="---
apiVersion: helm.cattle.io/v1
kind: HelmChart
metadata:
  name: cert-manager
  namespace: kube-system
spec:
  bootstrap: true
  chart: cert-manager
  createNamespace: true
  repo: https://charts.jetstack.io
  targetNamespace: cert-manager
  valuesContent: |-
    crds:
      enabled: true
    global:
      priorityClassName: system-cluster-critical
    config:
      gatewayAPI:
        enabled: true
    replicaCount: 1
    podDisruptionBudget:
      enabled: true
      minAvailable: 1
    webhook:
      replicaCount: 1
      podDisruptionBudget:
        enabled: true
        minAvailable: 1
    cainjector:
      replicaCount: 1
      podDisruptionBudget:
        enabled: true
        minAvailable: 1
  version: v1.21.3
"
```

In a RouterOS command, a double quote inside the file contents needs a backslash in front of it:

```ros
/file/add type=file \
    name=raid1/rke2/data/server/manifests/rancher.yaml \
    contents="---
apiVersion: helm.cattle.io/v1
kind: HelmChart
metadata:
  name: rancher
  namespace: kube-system
spec:
  chart: rancher
  createNamespace: true
  repo: https://releases.rancher.com/server-charts/stable
  targetNamespace: cattle-system
  valuesContent: |-
    debug: false
    replicas: 1
    certmanager:
      version: \"1.21.3\"
    useBundledSystemChart: true
    ingress:
      enabled: false
  version: v2.15.3
"
```

Each Rancher version supports a range of Kubernetes versions. Check the [Rancher support matrix](https://www.suse.com/suse-rancher/support-matrix/all-supported-versions/) before you select the tag of the RKE2 image.

## Create the container

### Container settings and mounts

Store the container layers and temporary files on the array. The settings in `/container/config` apply to all containers of the router:

```ros
/container/config/set tmpdir=raid1/containers/tmp
/container/config/set layer-dir=raid1/containers/layers
```

Set the registry from which the router downloads the image. The image is on Docker Hub:

```ros
/container/config/set registry-url=https://registry-1.docker.io
```

With a private registry, set its address instead:

```ros
/container/config/set registry-url=https://registry.example.com
```

Create the mounts for the RKE2 data, its configuration, and the NTP configuration file:

```ros
/container/mounts/add list=RKE2_DATA src=raid1/rke2/data \
    dst=/var/lib/rancher/rke2 mode=rw
/container/mounts/add list=RKE2_ETC src=raid1/rke2/etc \
    dst=/etc/rancher mode=rw
/container/mounts/add list=RKE2_NTP_CONFIG \
    src=raid1/rke2/ntp/ntp.conf dst=/mnt/rke2-ntp.conf mode=ro
```

With a private registry, add one more mount:

```ros
/container/mounts/add list=RKE2_REGISTRIES \
    src=raid1/rke2/registries.yaml dst=/mnt/rke2-registries.yaml \
    mode=ro
```

### RKE2 container

The command starts the NTP daemon, the device manager, and then the RKE2 server. `cmd` is a list with commas between its items: `/bin/bash`, `-c` and the script. `bash` gets the script as one argument, spaces included (see `cmd` in [`/container`](../../cli-reference/container/container.md)):

```ros
/container/add \
name=rke2 \
remote-image=mikrotik/rke2:v1.36.6-rke2r1-ubuntu2604-beta \
interface=ens18 \
privileged=yes \
root-dir=raid1/containers/rke2 \
stop-time="00:00:30" \
restart-interval="00:00:10" \
restart-max-count=100 \
restart-policy=on-failure \
start-on-boot=yes \
healthcheck-cmd="kubectl get node rke2.k8s | grep --color=none -i ' ready ' || exit 1" \
healthcheck-interval="00:01:00" \
healthcheck-retries=10 \
healthcheck-start-interval="00:00:20" \
healthcheck-start-period="00:03:00" \
entrypoint="" \
cmd="/bin/bash,-c,\
  /usr/sbin/ntpd -c /mnt/rke2-ntp.conf && \
  /usr/lib/systemd/systemd-udevd --daemon && udevadm trigger --wait-daemon=20 && \
  /bin/rke2 server \
  --snapshotter=fuse-overlayfs \
  --kubelet-arg=feature-gates=KubeletInUserNamespace=true \
  --cni=calico \
  --cluster-cidr=192.168.192.0/19 \
  --service-cidr=192.168.224.0/19 \
  --cluster-dns=192.168.224.10 \
  --kube-controller-manager-arg=node-cidr-mask-size=21 \
  --tls-san=192.168.1.3 \
  --tls-san=rke2.k8s \
  --node-name=rke2.k8s \
  --ingress-controller=none \
  --data-dir=/var/lib/rancher/rke2" \
mountlists=RKE2_DATA,RKE2_ETC,RKE2_NTP_CONFIG \
hostname=rke2.k8s
```

What to change:

- `remote-image` - the tag selects the Kubernetes version. The tag in this command is the one that this guide was tested with. Newer tags are listed on [mikrotik/rke2](https://hub.docker.com/r/mikrotik/rke2).
- `--tls-san`, `--node-name`, `hostname` and the node name in `healthcheck-cmd` - the address and the name of your node.
- `--cluster-cidr`, `--service-cidr`, `--cluster-dns` and `node-cidr-mask-size` - only together with the Calico file.
- `--snapshotter` - use `fuse-overlayfs` or `native`. The default RKE2 snapshotter, `overlayfs`, does not work in a RouterOS container.

With a private registry, add `--private-registry=/mnt/rke2-registries.yaml \` after the `--ingress-controller` line, and add `RKE2_REGISTRIES` to `mountlists`.

### Start and check

Start the container:

```ros
/container/start rke2
```

The first start downloads and extracts the image, and then RKE2 installs the cluster components. Both steps take several minutes. Check the status of the container:

```ros
/container/print
Flags: H - HEALTHY
Columns: NAME, ROOT-DIR, INTERFACE, MEMORY-CURRENT, CPU-USAGE, CONTAINER-SIZE
#   NAME  ROOT-DIR                INTERFACE  MEMORY  CPU-USAGE  CONTAINER
0 H rke2  /raid1/containers/rke2  ens18      5.3GiB  20.1       2071.4MiB
```

The `H` flag means that the node answers. The pods of the cluster need a few more minutes to start. If the container does not get the `H` flag, read the container log:

```ros
/container/log/print
```

The container has `start-on-boot=yes`, so it starts again after a reboot of the router.

## Use the cluster

### From the router

The container has `kubectl` and `helm`. Open a shell in the container:

```ros
/container/shell rke2
```

Then run the commands in this shell. The cluster is ready when `kubectl get pods -A` shows all pods as `Running` or `Completed`:

```shell
kubectl get node
kubectl get pods -A
helm ls -A
```

### From your computer

The access file of the cluster is `/etc/rancher/rke2/rke2.yaml` in the container. Print it in the container shell:

```shell
cat /etc/rancher/rke2/rke2.yaml
```

:::warning
This file gives full administrator access to the cluster. Keep it secret.
:::

On your computer, create the directory `~/.kube` and save the contents as `~/.kube/config`. Then make the file readable only by you:

```shell
mkdir -p ~/.kube
chmod 600 ~/.kube/config
```

In the file, change the `server` line to the address of the container:

```yaml
server: https://192.168.1.3:6443
```

Install [kubectl](https://kubernetes.io/docs/tasks/tools/) and, if you need it, [helm](https://helm.sh/docs/intro/install/). Then check the connection:

```shell
kubectl get node
NAME       STATUS   ROLES                AGE    VERSION
rke2.k8s   Ready    control-plane,etcd   112s   v1.36.6+rke2r1
```

### Calico Whisker

Whisker is the Calico web console for flow logs. Forward its port to your computer and open `http://localhost:8081`:

```shell
kubectl port-forward -n calico-system service/whisker 8081:8081
```

### Rancher

If you installed Rancher, forward its port to your computer and open `https://localhost:8443`:

```shell
kubectl port-forward -n cattle-system service/rancher 8443:443
```

Get the password for the first login:

```shell
kubectl get secret --namespace cattle-system bootstrap-secret \
  -o go-template='{{.data.bootstrapPassword|base64decode}}{{"\n"}}'
```

See the [Rancher documentation](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/access-clusters/) for access to clusters through Rancher.

## Read more

- [Container](../) - the container package, its settings and limits.
- [VETH](../veth) - virtual Ethernet interfaces for containers.
- [RAID](../../storage/raid) - disk arrays.
- [RKE2 documentation](https://docs.rke2.io/).
