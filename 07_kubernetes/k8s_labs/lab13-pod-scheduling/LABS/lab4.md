Lab 4: Node Labels
Task
Add a custom label to one node.
Verify label exists.
Create a pod that can only run on nodes having that label.
Confirm placement.
Remove pod.
Deliverables

Provide:

Label command
YAML
Verification commands
Results


Add a custom label to one node.


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get nodes
NAME                     STATUS   ROLES           AGE   VERSION
learning-control-plane   Ready    control-plane   8d    v1.34.8
learning-worker          Ready    <none>          8d    v1.34.8
learning-worker2         Ready    <none>          8d    v1.34.8


kubectl label node learning-worker env=uat
kubectl label node learning-worker2 env=prod


Verify label exists.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get nodes --show-labels
NAME                     STATUS   ROLES           AGE   VERSION   LABELS
learning-control-plane   Ready    control-plane   8d    v1.34.8   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=learning-control-plane,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node.kubernetes.io/exclude-from-external-load-balancers=
learning-worker          Ready    <none>          8d    v1.34.8   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,env=uat,kubernetes.io/arch=amd64,kubernetes.io/hostname=learning-worker,kubernetes.io/os=linux
learning-worker2         Ready    <none>          8d    v1.34.8   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,env=prod,kubernetes.io/arch=amd64,kubernetes.io/hostname=learning-worker2,kubernetes.io/os=linux
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 

for learning-worker: env=uat
for learning-worker2: env=prod

Create a pod that can only run on nodes having that label.
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-labels-deployment
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      name: web-pod
      labels:
        app: nginx
    spec:
      tolerations:
        - key: "node"
          operator: "Equal"
          value: "worker1"
          effect: "NoSchedule"
      nodeSelector:
        env: uat
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80

Note: I have provided the nodeSelector and taints because worker 1 have both taints and tolerations, we must use both taints tolerations and labels based scheduling (nodeSelector and node affintiy and node antiaffinity)

Confirm placement.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                     READY   UP-TO-DATE   AVAILABLE   AGE
node-labels-deployment   1/1     1            1           5m5s


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                      READY   STATUS    RESTARTS   AGE
node-labels-deployment-67b79dbf85-25dzt   1/1     Running   0          3m33s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl describe pods node-labels-deployment-67b79dbf85-25dzt
Name:             node-labels-deployment-67b79dbf85-25dzt
Namespace:        default
Priority:         0
Service Account:  default
Node:             learning-worker/172.18.0.4
Start Time:       Thu, 18 Jun 2026 12:28:11 +0530
Labels:           app=nginx
                  pod-template-hash=67b79dbf85
Annotations:      <none>
Status:           Running
IP:               10.244.1.11
IPs:
  IP:           10.244.1.11
Controlled By:  ReplicaSet/node-labels-deployment-67b79dbf85
Containers:
  nginx:
    Container ID:   containerd://3ef4e6dff4eb53ca52d0d2161149a4d0e2802738cdf56ef852349c44dd2a229e
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:6415da96b72a2f6ff433053df1da4bd507e45bc44b2c83dbac0ddeea80c6f066
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 18 Jun 2026 12:28:33 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-w56p6 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-w56p6:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              env=uat
Tolerations:                 node=worker1:NoSchedule
                             node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  3m49s  default-scheduler  Successfully assigned default/node-labels-deployment-67b79dbf85-25dzt to learning-worker
  Normal  Pulling    3m48s  kubelet            spec.containers{nginx}: Pulling image "nginx"
  Normal  Pulled     3m27s  kubelet            spec.containers{nginx}: Successfully pulled image "nginx" in 21.462s (21.462s including waiting). Image size: 63132582 bytes.
  Normal  Created    3m27s  kubelet            spec.containers{nginx}: Created container: nginx
  Normal  Started    3m27s  kubelet            spec.containers{nginx}: Started container nginx

scheduler assigned the nodeName to that pod by fitlering and scoring the node based on the resource availabity, taints and tolerations and nodeSelector in this case. out of all the node learning-worker node is filter out. hence that only node has highest scoring. pod now have nodeName as learning-worker and the kubelete of that node will run that pod with the help of container runtime. 

Remove pod.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl delete -f node-labels-deployment.yaml 
deployment.apps "node-labels-deployment" deleted from default namespace
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
No resources found in default namespace.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
No resources found in default namespace.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 
























Excellent work. This lab shows you're beginning to connect multiple scheduling concepts together instead of treating them as isolated topics.

# Lab 4 Review

## 1. Adding Labels

Commands:

```bash
kubectl label node learning-worker env=uat
kubectl label node learning-worker2 env=prod
```

✅ Correct

Verification:

```bash
kubectl get nodes --show-labels
```

Output confirms:

```text
learning-worker   env=uat
learning-worker2  env=prod
```

✅ Correct

---

# 2. YAML Review

```yaml
spec:
  nodeSelector:
    env: uat
```

This is the key part of the lab.

The scheduler will only consider nodes that have:

```text
env=uat
```

In your cluster:

```text
learning-worker   env=uat
learning-worker2  env=prod
```

Therefore:

```text
learning-worker
```

is the only worker node matching the selector.

---

# 3. Nice Observation About Taints

You wrote:

> I have provided the nodeSelector and taints because worker1 has both taints and tolerations.

This is actually a realistic production scenario.

A node can simultaneously have:

* Labels
* Taints
* Resource constraints
* Affinity rules

The scheduler evaluates all applicable constraints together.

---

# Interview Improvement

If an interviewer asks:

### Why was the toleration needed?

A strong answer would be:

> The node matched the nodeSelector (`env=uat`), but it was also protected by a `NoSchedule` taint. Without a matching toleration, the scheduler would still reject the node even though the label matched.

That's exactly how scheduling works in production.

---

# 4. Placement Verification

You verified:

```text
Node: learning-worker
```

and

```text
Node-Selectors: env=uat
```

Perfect.

This proves the scheduler respected the nodeSelector rule.

---

# 5. Scheduler Event

This is one of the strongest pieces of evidence:

```text
Normal Scheduled default-scheduler
Successfully assigned default/node-labels-deployment-67b79dbf85-25dzt to learning-worker
```

As an interviewer, I'd consider that complete verification.

---

# One Technical Correction

You wrote:

> out of all the node learning-worker node is filter out. hence that only node has highest scoring.

Slight wording issue.

What actually happened:

### Filtering Phase

Scheduler evaluates nodes:

| Node             | Result                     |
| ---------------- | -------------------------- |
| learning-worker  | Pass                       |
| learning-worker2 | Fail (`env=prod`)          |
| control-plane    | Fail (`env` label missing) |

After filtering:

```text
learning-worker
```

is the only candidate.

Since only one node remains:

### Scoring Phase

There is effectively no competition.

The scheduler schedules the pod there.

---

### Better Interview Answer

> During the filtering phase, only `learning-worker` satisfied the nodeSelector requirement (`env=uat`) and the required toleration. Since it was the only eligible node remaining after filtering, the scheduler assigned the pod to that node.

That answer sounds very strong.

---

# Interview Questions From This Lab

### Q1. What is a node label?

Expected answer:

> A node label is a key-value pair attached to a node that can be used by the scheduler to make placement decisions.

---

### Q2. What is nodeSelector?

Expected answer:

> nodeSelector is the simplest scheduling mechanism that restricts a pod to nodes containing specific labels.

---

### Q3. What happens if no node matches the nodeSelector?

Expected answer:

> The pod remains Pending and the scheduler generates a FailedScheduling event.

---

### Q4. Can a node match nodeSelector and still reject the pod?

Expected answer:

> Yes. For example, if the node has a NoSchedule taint and the pod lacks a matching toleration.

This question is asked surprisingly often.

---

### Q5. Which is more flexible: nodeSelector or nodeAffinity?

Expected answer:

> nodeAffinity is more flexible because it supports expressions, operators, and preferred scheduling rules. nodeSelector only supports exact label matching.

---

# Production Perspective

If a company has:

```text
Node-1 -> environment=dev
Node-2 -> environment=uat
Node-3 -> environment=prod
```

they often use:

```yaml
nodeSelector:
  environment: prod
```

to ensure production workloads never run on development nodes.

This is one of the most common real-world uses of labels.

---

# Score

### Hands-on

10/10

### Scheduling Understanding

9.5/10

### Troubleshooting

9.5/10

### Interview Readiness

9.5/10

You're now covering the progression that interviewers expect:

1. Default Scheduling ✅
2. Manual Scheduling (`nodeName`) ✅
3. Scheduling Failure (`Pending`) ✅
4. Label-Based Scheduling (`nodeSelector`) ✅

The next logical step is **Lab 5 (Multiple Labels)** and then **Node Affinity**, where you'll see why companies often prefer affinity over simple nodeSelectors.
