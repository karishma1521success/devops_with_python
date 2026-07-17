Task 4: Node Capacity Investigation

Without changing any pod:

Find:

Total CPU available on each node
Total memory available on each node
Allocatable CPU
Allocatable Memory
Deliverables

Provide commands used and outputs.



## First get the nodes and then describe each node to get the CPU and memory 
# 1. control plane: learning-control-plane  
# Total CPU, Memory: (CPU: 12     Memory: 16239500Ki  Pod: 110)
# Allocatatable CPU , Memroy: (CPU: 12, Memory:16239500Ki, ephermeral-storage: 459848776Ki, Pods: 110)


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs$ kubectl get nodes
NAME                     STATUS   ROLES           AGE   VERSION
learning-control-plane   Ready    control-plane   22d   v1.34.8
learning-worker          Ready    <none>          22d   v1.34.8
learning-worker2         Ready    <none>          22d   v1.34.8
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs$ kubectl describe node learning-control-plane
Name:               learning-control-plane
Roles:              control-plane
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=learning-control-plane
                    kubernetes.io/os=linux
                    node-role.kubernetes.io/control-plane=
                    node.kubernetes.io/exclude-from-external-load-balancers=
Annotations:        node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Tue, 09 Jun 2026 15:28:44 +0530
Taints:             node-role.kubernetes.io/control-plane:NoSchedule
Unschedulable:      false
Lease:
  HolderIdentity:  learning-control-plane
  AcquireTime:     <unset>
  RenewTime:       Wed, 01 Jul 2026 18:06:21 +0530
Conditions:
  Type             Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----             ------  -----------------                 ------------------                ------                       -------
  MemoryPressure   False   Wed, 01 Jul 2026 18:01:44 +0530   Tue, 09 Jun 2026 15:28:44 +0530   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure     False   Wed, 01 Jul 2026 18:01:44 +0530   Tue, 09 Jun 2026 15:28:44 +0530   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure      False   Wed, 01 Jul 2026 18:01:44 +0530   Tue, 09 Jun 2026 15:28:44 +0530   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready            True    Wed, 01 Jul 2026 18:01:44 +0530   Tue, 09 Jun 2026 15:29:05 +0530   KubeletReady                 kubelet is posting ready status
Addresses:
  InternalIP:  172.18.0.5
  Hostname:    learning-control-plane
Capacity:
  cpu:                12
  ephemeral-storage:  459848776Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             16239500Ki
  pods:               110
Allocatable:
  cpu:                12
  ephemeral-storage:  459848776Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             16239500Ki
  pods:               110
System Info:
  Machine ID:                 5cdeb1e4a0a14c0a9b04c5ff28b3ab30
  System UUID:                b176a805-aca7-4fd2-9e3f-6246f5ffd628
  Boot ID:                    120d9c8d-2e8f-4149-b06e-4d31c816e56b
  Kernel Version:             6.8.0-124-generic
  OS Image:                   Debian GNU/Linux 13 (trixie)
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  containerd://2.3.1
  Kubelet Version:            v1.34.8
  Kube-Proxy Version:         
PodCIDR:                      10.244.0.0/24
PodCIDRs:                     10.244.0.0/24
ProviderID:                   kind://docker/learning/learning-control-plane
Non-terminated Pods:          (10 in total)
  Namespace                   Name                                              CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                              ------------  ----------  ---------------  -------------  ---
  kube-system                 coredns-66bc5c9577-k5cmj                          100m (0%)     0 (0%)      70Mi (0%)        170Mi (1%)     22d
  kube-system                 coredns-66bc5c9577-tpxhj                          100m (0%)     0 (0%)      70Mi (0%)        170Mi (1%)     22d
  kube-system                 etcd-learning-control-plane                       100m (0%)     0 (0%)      100Mi (0%)       0 (0%)         8h
  kube-system                 kindnet-vfmjs                                     100m (0%)     100m (0%)   50Mi (0%)        50Mi (0%)      22d
  kube-system                 kube-apiserver-learning-control-plane             250m (2%)     0 (0%)      0 (0%)           0 (0%)         8h
  kube-system                 kube-controller-manager-learning-control-plane    200m (1%)     0 (0%)      0 (0%)           0 (0%)         22d
  kube-system                 kube-proxy-dc2p9                                  0 (0%)        0 (0%)      0 (0%)           0 (0%)         22d
  kube-system                 kube-scheduler-learning-control-plane             100m (0%)     0 (0%)      0 (0%)           0 (0%)         22d
  kube-system                 metrics-server-6df6bc799-sj9nw                    100m (0%)     0 (0%)      200Mi (1%)       0 (0%)         6d23h
  local-path-storage          local-path-provisioner-64478cc988-rp285           0 (0%)        0 (0%)      0 (0%)           0 (0%)         22d
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests    Limits
  --------           --------    ------
  cpu                1050m (8%)  100m (0%)
  memory             490Mi (3%)  390Mi (2%)
  ephemeral-storage  0 (0%)      0 (0%)
  hugepages-1Gi      0 (0%)      0 (0%)
  hugepages-2Mi      0 (0%)      0 (0%)
Events:              <none>



# 1. Worker node 1: learning-worker
# Total CPU, Memory: (CPU: 12     Memory: 16239500Ki  Pod: 110)
# Allocatatable CPU , Memroy: (CPU: 12, Memory:16239500Ki, ephermeral-storage: 459848776Ki, Pods: 110)


# 1. Worker node 2: learning-worker2
# Total CPU, Memory: (CPU: 12     Memory: 16239500Ki  Pod: 110)
# Allocatatable CPU , Memroy: (CPU: 12, Memory:16239500Ki, ephermeral-storage: 459848776Ki, Pods: 110)


# I use the kubectl describe node/nodeName 
Above command to get the total cpu and memory and allocated cpu and memroy





Excellent. This is one of those labs that directly translates to production troubleshooting. I'll review it as an interviewer would.

# Overall Assessment

**Score: 9.5/10**

You found the correct information and used the correct command:

```bash
kubectl describe node <node-name>
```

This is exactly what most engineers use when investigating scheduling issues.

---

# One Important Correction

The task asked for:

* Total CPU
* Total Memory
* **Allocatable** CPU
* **Allocatable** Memory

You correctly identified these sections:

```text
Capacity:
```

and

```text
Allocatable:
```

However, don't confuse **Allocatable** with **Allocated**.

There are actually **three** different concepts in the output.

---

## 1. Capacity

```text
Capacity:
  cpu: 12
  memory: 16239500Ki
```

This is the **physical (or virtual) capacity** of the node.

Think of it as:

> "How much CPU and memory does this machine have?"

---

## 2. Allocatable

```text
Allocatable:
  cpu: 12
  memory: 16239500Ki
```

This is what Kubernetes makes available for scheduling.

Normally:

```text
Capacity
        ↓
Reserve resources for OS + kubelet
        ↓
Allocatable
```

In your Kind cluster they happen to be equal:

```text
Capacity CPU      = 12
Allocatable CPU   = 12
```

That is **not** always true in production.

---

### Production Example

Suppose an EC2 instance has:

```text
Capacity
CPU = 8
Memory = 32Gi
```

Kubernetes reserves resources for:

* kubelet
* container runtime
* OS
* system daemons

Now Allocatable becomes:

```text
CPU = 7500m

Memory = 30Gi
```

The scheduler uses **Allocatable**, not Capacity.

This distinction is asked surprisingly often in interviews.

---

## 3. Allocated Resources

This is another section lower in the output:

```text
Allocated resources:

Requests:

CPU = 1050m

Memory = 490Mi
```

This answers a different question:

> "How much of the allocatable capacity has already been requested by running pods?"

For example:

```text
CPU Requests = 1050m (8%)
```

means:

```text
Pods have reserved 1.05 CPU cores.
```

It does **not** mean the node is currently using 8% CPU.

That's another common interview trap.

---

# Why Does the Scheduler Care?

Suppose:

```text
Allocatable CPU = 12
```

Existing pods have requested:

```text
11.5 CPU
```

New pod requests:

```yaml
requests:
  cpu: 1
```

The scheduler calculates:

```text
Available =

12 - 11.5

= 0.5 CPU
```

New pod needs:

```text
1 CPU
```

Result:

```text
Pending
```

Even if:

```text
top
```

shows the node using only 10% CPU.

This confuses many beginners because **the scheduler uses requests, not actual CPU utilization**.

---

# Interview Question

Suppose:

```text
Node Capacity

CPU = 8
```

```text
Allocatable

CPU = 7.5
```

Running pods have requests totaling:

```text
7.2 CPU
```

Actual CPU usage (from `top`) is:

```text
20%
```

A new pod requests:

```yaml
cpu: 500m
```

Will it be scheduled?

Many people answer:

> "Yes, because CPU usage is only 20%."

That's incorrect.

The scheduler looks at **requested resources**, not real-time utilization. If only **300m** allocatable CPU remains based on requests, a pod requesting **500m** will stay **Pending**, regardless of current CPU usage.

---

# Production Tip

When a pod is stuck in `Pending`, the first commands I typically run are:

```bash
kubectl describe pod <pod-name>
```

to inspect scheduling events, followed by:

```bash
kubectl describe node <node-name>
```

to review:

* Capacity
* Allocatable
* Allocated resources

This sequence quickly tells you whether the issue is related to insufficient requested resources, taints, affinity rules, or something else.

---

You're building the right troubleshooting mindset by reading the node details instead of only checking whether a pod is `Running`. That's the habit that distinguishes someone who can operate Kubernetes in production from someone who only knows how to write YAML.
