Task 2: Requests vs Limits

Create another pod.

Requirements:

Pod Name:

resource-limit-pod

Container:

nginx

Configure:

CPU Request = 100m
CPU Limit = 500m
Memory Request = 128Mi
Memory Limit = 256Mi


Verify

Find:

Is pod running? - yes pod is running
What resources are visible in describe output?
    Limits:
      cpu:     500m
      memory:  256Mi
    Requests:
      cpu:        100m
      memory:     128Mi

Difference between Requests and Limits section.


Requests defines minimum amount of resources a container needs to be scheduled and execute. If any nodes doesnot have that amount of request memory  available then kuberenetes scheduler will not able to assign the node to the pod. Hence pod will remain in pending state.
Limits defines the maximum amount of resource a container can use. If a container/pod takes a resouces more than defined in limits. Os kernel may kill the pod. in terms of memory and in terms of CPu, os kernel will not allow to use more cpu than defined in limits. It helps to mitiage the resource starvation and noisy negibours issues.

Deliverables

Provide:

kubectl describe pod resource-limit-pod


---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource-limit-pod-deploy
  namespace: default
  labels:
    app: resource-limit-pod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: resource-limit-pod
  revisionHistoryLimit: 5
  template:
    metadata:
      labels:
        app: resource-limit-pod
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
              cpu: "500m"
              memory: "256Mi"




kubectl describe pod resource-limit-pod-deploy-6cd9879d9-7wmw2
Containers:
  nginx:
    Container ID:   containerd://fe1863e9775a984e4d6f90501df1b5e4e769b0f955ba222e5a24f3ea8c7812c5
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:424939d458e28153a78d9a4a8d60e8fae5eae35e84a2d92a43d153d1f92c171c
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 25 Jun 2026 11:47:06 +0530
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  256Mi
    Requests:
      cpu:        100m
      memory:     128Mi
    Environment:  <none>
    Mounts:


Note: i have deployed pods using the deployment because it's good to deploy pod as using any controller not using a standalone pod.
kubectl describe pod resource-limit-pod


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ kubectl describe pod resource-limit-pod-deploy-6cd9879d9-7wmw2
Name:             resource-limit-pod-deploy-6cd9879d9-7wmw2
Namespace:        default
Priority:         0
Service Account:  default
Node:             learning-worker/172.18.0.4
Start Time:       Thu, 25 Jun 2026 11:47:01 +0530
Labels:           app=resource-limit-pod
                  pod-template-hash=6cd9879d9
Annotations:      <none>
Status:           Running
IP:               10.244.1.8
IPs:
  IP:           10.244.1.8
Controlled By:  ReplicaSet/resource-limit-pod-deploy-6cd9879d9
Containers:
  nginx:
    Container ID:   containerd://fe1863e9775a984e4d6f90501df1b5e4e769b0f955ba222e5a24f3ea8c7812c5
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:424939d458e28153a78d9a4a8d60e8fae5eae35e84a2d92a43d153d1f92c171c
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 25 Jun 2026 11:47:06 +0530
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  256Mi
    Requests:
      cpu:        100m
      memory:     128Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-j5dbk (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-j5dbk:
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
  Normal  Scheduled  98s   default-scheduler  Successfully assigned default/resource-limit-pod-deploy-6cd9879d9-7wmw2 to learning-worker
  Normal  Pulling    98s   kubelet            spec.containers{nginx}: Pulling image "nginx"
  Normal  Pulled     94s   kubelet            spec.containers{nginx}: Successfully pulled image "nginx" in 3.524s (3.524s including waiting). Image size: 63132621 bytes.
  Normal  Created    94s   kubelet            spec.containers{nginx}: Created container: nginx
  Normal  Started    94s   kubelet            spec.containers{nginx}: Started container nginx



## ChatGPT 

Your understanding is moving in the right direction. I'll review it as if I were interviewing a candidate with ~1 year of experience.

# Assessment: Task 2

## ✅ Pod Status

Correct.

```text
Status: Running
Ready: True
PodScheduled: True
```

The pod was successfully scheduled and started.

---

# ✅ Resources Visible in Describe Output

You correctly identified:

```yaml
Limits:
  cpu: 500m
  memory: 256Mi

Requests:
  cpu: 100m
  memory: 128Mi
```

---

# Difference Between Requests and Limits

Your answer is mostly correct.

A slightly refined interview-ready version would be:

### Requests

```text
Requests define the minimum resources guaranteed to a container.
The Kubernetes scheduler uses requests while selecting a node.
A pod will not be scheduled if no node has enough available requested resources.
```

Example:

```yaml
requests:
  cpu: 100m
  memory: 128Mi
```

Scheduler asks:

```text
Does any node have at least:
100m CPU
128Mi Memory
available?
```

If no:

```text
Pod remains Pending.
```

---

### Limits

```text
Limits define the maximum resources a container is allowed to consume.
The kubelet and Linux kernel enforce these limits at runtime.
```

Example:

```yaml
limits:
  cpu: 500m
  memory: 256Mi
```

---

### Memory Limit Behavior

You said:

> OS kernel may kill the pod

Small correction:

```text
The container is usually OOMKilled (Out Of Memory Kill).
The pod itself isn't directly killed.
The container is terminated and may be restarted depending on the restart policy.
```

Interviewers like hearing the term:

```text
OOMKilled
```

because it shows real-world troubleshooting knowledge.

---

### CPU Limit Behavior

You said:

> OS kernel will not allow to use more CPU than defined in limits

Correct.

More precise wording:

```text
CPU is throttled when the container tries to exceed its CPU limit.
The container continues running but receives less CPU time.
```

Unlike memory:

```text
Memory Limit exceeded → OOMKill
CPU Limit exceeded → Throttling
```

This is one of the most frequently asked Kubernetes interview questions.

---

# Excellent Observation Opportunity

Look at your output:

```text
QoS Class: Burstable
```

Interview question:

### Why is QoS = Burstable?

You should be able to answer this now.

Hint-free thinking exercise:

Compare:

```yaml
requests:
  cpu: 100m
  memory: 128Mi

limits:
  cpu: 500m
  memory: 256Mi
```

and ask:

```text
Are Requests and Limits equal?
```

That answer explains the QoS class.

---

# Production Discussion

You wrote:

> it's good to deploy pod using controller not standalone pod

Absolutely correct.

In production:

```text
Deployment
    ↓
ReplicaSet
    ↓
Pods
```

is the standard pattern.

Standalone Pods are usually used for:

* learning
* debugging
* testing scheduler behavior
* interview demonstrations

Almost never for actual applications.

---

# Interview Questions Based on Your YAML

### Q1

Why did the scheduler use:

```yaml
requests:
  cpu: 100m
```

instead of

```yaml
limits:
  cpu: 500m
```

when selecting a node?

---

### Q2

Assume node has:

```text
Available CPU = 300m
```

and pod has:

```yaml
request: 100m
limit: 500m
```

Will scheduler place the pod?

---

### Q3

Can this pod ever consume:

```text
400m CPU
```

while running?

Why?

---

### Q4 (Real Production Scenario)

A pod shows:

```yaml
requests:
  cpu: 100m
limits:
  cpu: 500m
```

but application response time becomes slow during traffic spikes.

Which resource-related problem would you investigate first?

---

### Q5

Your pod shows:

```text
QoS Class: Burstable
```

What are the other QoS classes in Kubernetes?

---

You are ready for **Task 3 (Scheduler Failure Scenario)** now. That task is where you'll really understand how the scheduler uses requests and why pods stay in `Pending`.



This is a very common Kubernetes interview question.

# What is QoS (Quality of Service)?

QoS tells Kubernetes how important a pod is when a node experiences resource pressure (especially memory pressure).

Kubernetes assigns one of three QoS classes:

```text
Guaranteed
Burstable
BestEffort
```

You can see it using:

```bash
kubectl describe pod <pod-name>
```

Output:

```text
QoS Class: Burstable
```

---

# Why is Your Pod Burstable?

Your pod has:

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi
```

Notice:

```text
CPU Request  = 100m
CPU Limit    = 500m

Memory Request = 128Mi
Memory Limit   = 256Mi
```

Requests and Limits are **not equal**.

Because of that Kubernetes classifies the pod as:

```text
QoS Class: Burstable
```

---

# How Kubernetes Decides QoS

## 1. Guaranteed

When **every container** has:

```text
Request = Limit
```

for both CPU and Memory.

Example:

```yaml
resources:
  requests:
    cpu: 500m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 256Mi
```

Result:

```text
QoS Class: Guaranteed
```

Meaning:

```text
I need exactly these resources.
Reserve them for me.
```

These pods are the last ones Kubernetes wants to evict.

---

## 2. Burstable

When:

```text
Requests are defined
BUT
Requests ≠ Limits
```

Example (your case):

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi
```

Result:

```text
QoS Class: Burstable
```

Meaning:

```text
I need at least 100m CPU.
If available, allow me to burst up to 500m CPU.
```

This is the most common QoS class in production.

---

## 3. BestEffort

No requests and no limits.

Example:

```yaml
resources: {}
```

or

```yaml
containers:
- name: nginx
  image: nginx
```

Result:

```text
QoS Class: BestEffort
```

Meaning:

```text
I have no guaranteed resources.
Give me whatever is available.
```

These are the first pods Kubernetes evicts during resource pressure.

---

# Easy Way to Remember

| Requests | Limits            | QoS        |
| -------- | ----------------- | ---------- |
| Not Set  | Not Set           | BestEffort |
| Set      | Set but Different | Burstable  |
| Set      | Equal to Requests | Guaranteed |

---

# Real Interview Answer

If an interviewer asks:

> Why is your pod showing QoS Class Burstable?

You can answer:

> The pod has CPU and Memory requests defined, which guarantees minimum resources, but the requests and limits are different. Kubernetes assigns Burstable QoS when a pod can use more resources than its guaranteed request up to its configured limit.

---

# Production Example

Suppose your application normally needs:

```text
100m CPU
128Mi Memory
```

but during traffic spikes it may need:

```text
500m CPU
256Mi Memory
```

You configure:

```yaml
requests:
  cpu: 100m
  memory: 128Mi

limits:
  cpu: 500m
  memory: 256Mi
```

Now:

* Scheduler reserves only 100m CPU and 128Mi Memory.
* Application can burst up to 500m CPU and 256Mi Memory.
* QoS becomes Burstable.

That's exactly why Burstable is the most commonly used QoS class for production applications.
