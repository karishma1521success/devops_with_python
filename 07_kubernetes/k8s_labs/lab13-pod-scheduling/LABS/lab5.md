Lab 5: Multiple Node Labels
Task
Create two different labels on nodes.
Create two pods.
Each pod must land on a different node based on labels.
Verify scheduling.
Deliverables

Provide:

Commands
YAML
Results



Create two different labels on nodes.
kubectl label node learning-worker storage=hdd

kubectl label node learning-worker2 storage=sdd

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get nodes --show-labels
NAME                     STATUS   ROLES           AGE   VERSION   LABELS
learning-control-plane   Ready    control-plane   8d    v1.34.8   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=learning-control-plane,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node.kubernetes.io/exclude-from-external-load-balancers=
learning-worker          Ready    <none>          8d    v1.34.8   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,env=uat,kubernetes.io/arch=amd64,kubernetes.io/hostname=learning-worker,kubernetes.io/os=linux,storage=hdd
learning-worker2         Ready    <none>          8d    v1.34.8   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,env=prod,kubernetes.io/arch=amd64,kubernetes.io/hostname=learning-worker2,kubernetes.io/os=linux,storage=sdd
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 

Worker node1 (learning-worker) : Taints: node=worker1         labels: env=uat , storage=hdd
Worker node 2 (learning-worker2): Taints: node=worker2        labels: env=prod , storage=sdd

Create two pods.

Pod1 deployment yaml file
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat multiple-node-labels-deploy1.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: multiple-node-labels-deployment
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      tolerations:
        - key: "node"
          operator: "Equal"
          value: "worker1"
          effect: "NoSchedule"
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: "storage"
                    operator: "In"
                    values:
                      - hdd
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80



Pod2 deployment.yaml file
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: multiple-node-labels-deployment2
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      tolerations:
        - key: "node"
          operator: "Equal"
          value: "worker2"
          effect: "NoSchedule"
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: "storage"
                    operator: "In"
                    values:
                      - "sdd"
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80



karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl apply -f multiple-node-labels-deploy2.yaml 
deployment.apps/multiple-node-labels-deployment2 created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
multiple-node-labels-deployment    1/1     1            1           155m
multiple-node-labels-deployment2   1/1     1            1           99m



Each pod must land on a different node based on labels.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods -o wide
NAME                                                READY   STATUS    RESTARTS   AGE    IP            NODE               NOMINATED NODE   READINESS GATES
multiple-node-labels-deployment-75d5d88979-tk6b5    1/1     Running   0          155m   10.244.1.13   learning-worker    <none>           <none>
multiple-node-labels-deployment2-746b79c895-8vl2m   1/1     Running   0          99m    10.244.2.18   learning-worker2   <none>           <none>
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 

Verify scheduling.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods -o wide
NAME                                                READY   STATUS    RESTARTS   AGE    IP            NODE               NOMINATED NODE   READINESS GATES
multiple-node-labels-deployment-75d5d88979-tk6b5    1/1     Running   0          155m   10.244.1.13   learning-worker    <none>           <none>
multiple-node-labels-deployment2-746b79c895-8vl2m   1/1     Running   0          99m    10.244.2.18   learning-worker2   <none>           <none>
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 










Excellent work. One interesting thing is that you unintentionally moved ahead of the lab and started using **Node Affinity** instead of **nodeSelector**. That's actually a good sign because Node Affinity is the more advanced and production-oriented approach.

---

# Lab 5 Review

## 1. Labels Added

Commands:

```bash
kubectl label node learning-worker storage=hdd
kubectl label node learning-worker2 storage=sdd
```

Verification:

```bash
kubectl get nodes --show-labels
```

Output confirms:

```text
learning-worker   storage=hdd
learning-worker2  storage=sdd
```

✅ Correct

---

# 2. Scheduling Logic

You configured:

### Pod 1

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: storage
              operator: In
              values:
                - hdd
```

and

```yaml
tolerations:
  - key: node
    value: worker1
```

Result:

```text
learning-worker
```

✅ Correct

---

### Pod 2

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: storage
              operator: In
              values:
                - sdd
```

and

```yaml
tolerations:
  - key: node
    value: worker2
```

Result:

```text
learning-worker2
```

✅ Correct

---

# One Minor Issue

You labeled the node as:

```text
storage=sdd
```

Normally it would be:

```text
storage=ssd
```

(Solid State Drive)

Not a Kubernetes issue, just a spelling typo.

Since both the label and affinity use `sdd`, Kubernetes works fine.

---

# Verification

Your verification is perfect:

```bash
kubectl get pods -o wide
```

Output:

```text
multiple-node-labels-deployment      -> learning-worker
multiple-node-labels-deployment2     -> learning-worker2
```

This proves the scheduler respected your affinity rules.

---

# What the Scheduler Did

For Pod 1:

### Filtering

| Node             | Result               |
| ---------------- | -------------------- |
| learning-worker  | Pass                 |
| learning-worker2 | Fail (`storage=sdd`) |
| control-plane    | Fail (label missing) |

Remaining node:

```text
learning-worker
```

Scheduler assigns the pod there.

---

For Pod 2:

### Filtering

| Node             | Result               |
| ---------------- | -------------------- |
| learning-worker  | Fail (`storage=hdd`) |
| learning-worker2 | Pass                 |
| control-plane    | Fail                 |

Remaining node:

```text
learning-worker2
```

Scheduler assigns the pod there.

---

# Interview Observation

You used:

```yaml
requiredDuringSchedulingIgnoredDuringExecution
```

This means:

> The label requirement must be satisfied at scheduling time, otherwise the pod remains Pending.

This is a very important interview concept.

---

# Question I Would Ask

### Why did you use Node Affinity instead of nodeSelector?

Strong answer:

> nodeAffinity is more expressive. It supports operators such as In, NotIn, Exists, DoesNotExist, Gt, and Lt. nodeSelector only supports exact key-value matching.

That's one of the main reasons companies prefer affinity for complex workloads.

---

# Another Interview Question

### What does `IgnoredDuringExecution` mean?

Expected answer:

> The rule is enforced only when the pod is scheduled. If the node label changes later, Kubernetes does not evict the running pod.

Example:

```text
Pod scheduled on storage=hdd
```

Later:

```text
storage=hdd removed
```

Pod keeps running.

Many engineers struggle with this question.

---

# One Improvement I'd Make

You currently have:

```yaml
selector:
  matchLabels:
    app: nginx
```

in both Deployments.

Although it works because they're separate ReplicaSets, in production I'd usually use:

### Deployment 1

```yaml
app: nginx-hdd
```

### Deployment 2

```yaml
app: nginx-ssd
```

to make troubleshooting easier.

Not required for the lab, but it's a good habit.

---

# Interview Question Based on Your Solution

### If I remove:

```yaml
tolerations:
```

from Pod 1, what happens?

Expected answer:

> The node matches the affinity rule (`storage=hdd`), but it still has a `NoSchedule` taint. Without a matching toleration, the scheduler rejects the node and the pod remains Pending.

That's exactly the type of combined scheduling question interviewers ask.

---

# Score

### Labels

10/10

### Node Affinity

10/10

### Taints/Tolerations Integration

10/10

### Scheduler Understanding

9.5/10

### Interview Readiness

10/10

At this point you're already working with:

* Default scheduling ✅
* Manual scheduling (`nodeName`) ✅
* Scheduling failures (`Pending`) ✅
* Labels (`nodeSelector`) ✅
* Taints & Tolerations ✅
* Required Node Affinity ✅

So when you start **Lab 6**, you're not learning Node Affinity from scratch anymore—you've already used it in a realistic scheduling scenario.
