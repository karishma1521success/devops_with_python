Task 1: Create a Basic Resource-Constrained Pod
Requirements

Create a pod named:

resource-pod

Container:

nginx

Configure:

CPU Request = 100m
Memory Request = 128Mi

Verify:

Pod gets scheduled
Find which node it landed on
Inspect resource configuration
Deliverables

Provide:

kubectl get pod -o wide

and

kubectl describe pod resource-pod

Output only.


control plane (learning-control-plane):;    Tainsts: node-role.kubernetes.io/control-plane:NoSchedule                  labels: node-role.kubernetes.io/control-plane=
Worker node1 (learning-worker) :            Taints:  node=worker1   nodeName=learning-worker                                                    labels: env=uat , storage=hdd
Worker node 2 (learning-worker2):           Taints:  node=worker2                                                       labels: env=prod , storage=sdd



karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ cat resource-deploy.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource-pod-deploy
  namespace: default
  labels:
    app: resource-pod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: resource-pod
  revisionHistoryLimit: 5
  template:
    metadata:
      labels:
        app: resource-pod
    spec:
      dnsPolicy: ClusterFirst
      restartPolicy: Always  # because I want my application to be run always.
      tolerations:
        - key: "node"
          operator: "Equal"
          value: "worker1"
          effect: "NoSchedule"
        - key: "nodeName"
          operator: "Equal"
          value: "learning-worker"
          effect: "NoSchedule"
      affinity:
        nodeAffinity:
          # Mandotary conditions
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: "env"
                    operator: "In"
                    values:
                      - "uat"
          # Preferred condition
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: "storage"
                    operator: "In"
                    values:
                      - "hdd"
      containers:
        - name: nginx
          image: nginx
          imagePullPolicy: Always
          ports:
            - protocol: TCP
              containerPort: 80
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "150m"
              memory: "130Mi"





This is my file and I have provided the tolerations and affinity to be deploy on the worker1 but I have provided the resource requests as well. 

It landed the pod on learning-worker






karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ kubectl describe pod resource-pod-deploy-6d46f9fdbb-c8nsm
Name:             resource-pod-deploy-6d46f9fdbb-c8nsm
Namespace:        default
Priority:         0
Service Account:  default
Node:             learning-worker/172.18.0.4
Start Time:       Wed, 24 Jun 2026 16:36:43 +0530
Labels:           app=resource-pod
                  pod-template-hash=6d46f9fdbb
Annotations:      <none>
Status:           Running
IP:               10.244.1.7
IPs:
  IP:           10.244.1.7
Controlled By:  ReplicaSet/resource-pod-deploy-6d46f9fdbb
Containers:
  nginx:
    Container ID:   containerd://8fcd789d04a8d9d3ba4fcaec5e71dba592339506fff5b80934ba1f14cece093d
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:424939d458e28153a78d9a4a8d60e8fae5eae35e84a2d92a43d153d1f92c171c
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 24 Jun 2026 16:36:46 +0530
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     150m
      memory:  130Mi
    Requests:
      cpu:        100m
      memory:     128Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-nqfc5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-nqfc5:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node=worker1:NoSchedule
                             node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nodeName=learning-worker:NoSchedule
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  3m9s  default-scheduler  Successfully assigned default/resource-pod-deploy-6d46f9fdbb-c8nsm to learning-worker
  Normal  Pulling    3m8s  kubelet            spec.containers{nginx}: Pulling image "nginx"
  Normal  Pulled     3m6s  kubelet            spec.containers{nginx}: Successfully pulled image "nginx" in 1.325s (2.356s including waiting). Image size: 63132621 bytes.
  Normal  Created    3m6s  kubelet            spec.containers{nginx}: Created container: nginx


container has the request and limits 






## Chatgpt answers. 
Good work. You successfully combined **resource requests/limits** with **scheduling constraints** (taints/tolerations + node affinity). That's actually closer to a real production deployment than a simple resource-only pod.

### What I Observe

Your pod landed on:

```text
learning-worker
```

and the scheduler event confirms:

```text
Successfully assigned default/resource-pod-deploy-6d46f9fdbb-c8nsm to learning-worker
```

### Why did it land on learning-worker?

Let's analyze the scheduling rules you configured:

#### Required Node Affinity

```yaml
requiredDuringSchedulingIgnoredDuringExecution:
  nodeSelectorTerms:
    - matchExpressions:
        - key: env
          operator: In
          values:
            - uat
```

Only nodes with:

```text
env=uat
```

are eligible.

From your cluster:

```text
learning-worker   -> env=uat
learning-worker2  -> env=prod
```

So:

```text
learning-worker   ✅ Eligible
learning-worker2  ❌ Rejected
```

At this point, the scheduler has only one worker node available.

---

#### Preferred Affinity

```yaml
preferredDuringSchedulingIgnoredDuringExecution:
  - weight: 100
    preference:
      matchExpressions:
        - key: storage
          operator: In
          values:
            - hdd
```

The eligible node also has:

```text
storage=hdd
```

so the preference is satisfied.

---

#### Tolerations

You added:

```yaml
tolerations:
- key: node
  value: worker1
```

and

```yaml
- key: nodeName
  value: learning-worker
```

These merely allow the pod to be scheduled onto tainted nodes.

A common interview question:

> Did tolerations force the pod onto learning-worker?

Answer:

```text
No.
Tolerations only allow scheduling on a tainted node.
They do not force placement.
Node Affinity was what actually selected learning-worker.
```

---

### Resource Section

Scheduler sees:

```yaml
requests:
  cpu: 100m
  memory: 128Mi
```

These are the values used during scheduling.

The scheduler checks:

```text
Does learning-worker have at least:
100m CPU
128Mi Memory
available?
```

Since it does, scheduling succeeds.

---

### Interesting Observation

Your lab task originally asked for:

```text
CPU Request = 100m
Memory Request = 128Mi
```

But you additionally configured:

```yaml
limits:
  cpu: 150m
  memory: 130Mi
```

which is perfectly fine.

That is why the describe output shows:

```text
QoS Class: Burstable
```

Interview question:

> Why is QoS Class Burstable and not Guaranteed?

Think about that yourself first. Don't look it up yet. Try to derive it from the Requests and Limits section.

---

### One Production-Level Comment

You named the file:

```yaml
resource-deploy.yaml
```

and created a:

```yaml
Deployment
```

The task asked for a Pod, but using a Deployment is actually better practice in real environments because Deployments manage ReplicaSets and self-healing.

Just be aware that in interviews:

```text
Pod = workload unit
Deployment = controller managing Pods
```

and they are not the same Kubernetes object.

---

### Interviewer's Follow-up Question

Suppose you change:

```yaml
requests:
  cpu: 20
  memory: 40Gi
```

and keep all affinity/toleration rules the same.

Without running anything:

1. Will the scheduler still choose learning-worker?
2. Will the pod be Running?
3. What status do you expect?
4. Which section of `kubectl describe pod` would you check first?

Answer these as if you're in an interview, and then move to **Task 2 (Requests vs Limits)**.
