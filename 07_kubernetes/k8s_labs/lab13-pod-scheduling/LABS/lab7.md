Lab 7: Node Affinity Failure
Task
Create a pod with affinity rules that no node satisfies.
Pod should stay Pending.
Investigate scheduler events.
Correct the rule.
Verify pod becomes Running.
Deliverables

Provide:

YAML
Events
Analysis



control plane (learning-control-plane):;    Tainsts: node-role.kubernetes.io/control-plane:NoSchedule                  labels: node-role.kubernetes.io/control-plane=
Worker node1 (learning-worker) :            Taints:  node=worker1                                                      labels: env=uat , storage=hdd
Worker node 2 (learning-worker2):           Taints:  node=worker2                                                       labels: env=prod , storage=sdd


Create a pod with affinity rules that no node satisfies.

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-affinity-failure-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: node-affinity-failure-label
  template:
    metadata:
      labels:
        app: node-affinity-failure-label
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
                  - key: "env"
                    operator: "In"
                    values:
                      - "QA"
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "100m"
              memory: "100Mi"
            limits:
              cpu: "200m"
              memory: "200Mi"




Pod should stay Pending.


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
node-affinity-failure-deployment   0/2     2            0           21h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                                READY   STATUS    RESTARTS   AGE
node-affinity-failure-deployment-5cf49b54c7-68vft   0/1     Pending   0          21h
node-affinity-failure-deployment-5cf49b54c7-n6csw   0/1     Pending   0          21h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 

Investigate scheduler events.
Annotations:      <none>
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    ReplicaSet/node-affinity-failure-deployment-5cf49b54c7
Containers:
  nginx:
    Image:      nginx
    Port:       80/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     200m
      memory:  200Mi
    Requests:
      cpu:        100m
      memory:     100Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-w7gml (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  kube-api-access-w7gml:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node=worker2:NoSchedule
                             node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age                  From               Message
  ----     ------            ----                 ----               -------
  Warning  FailedScheduling  53s (x262 over 21h)  default-scheduler  0/3 nodes are available: 1 node(s) didn't match Pod's node affinity/selector, 2 node(s) had untolerated taint(s). no new claims to deallocate, preemption: 0/3 nodes are available: 3 Preemption is not helpful for scheduling.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 

Out of 3 nodes, 2 nodes has the taints which pod does not have tolerated taints. scheduler finds the matched tolerated taints on 1 node but they have unmatched pod's node affinity. 

Correct the rule.
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-affinity-failure-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: node-affinity-failure-label
  template:
    metadata:
      labels:
        app: node-affinity-failure-label
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
                  - key: "env"
                    operator: "In"
                    values:
                      - "prod"
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "100m"
              memory: "100Mi"
            limits:
              cpu: "200m"


updated the pod's node affintiy matched with the node labels. but the pod must tolerated the node taints as well.  

Verify pod becomes Running.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
node-affinity-failure-deployment   2/2     2            2           21h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                               READY   STATUS    RESTARTS   AGE
node-affinity-failure-deployment-56fc456bb-fdtql   1/1     Running   0          8m32s
node-affinity-failure-deployment-56fc456bb-pwb22   1/1     Running   0          8m38s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 







This is a very strong Lab 7 submission. You didn't just create a failure—you analyzed the scheduler's reasoning and then fixed it. That's exactly what happens during Kubernetes troubleshooting.

---

# Lab 7 Review

## What You Built

### Affinity Rule

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: env
              operator: In
              values:
                - QA
```

Available labels:

```text
learning-worker   env=uat
learning-worker2  env=prod
```

No node has:

```text
env=QA
```

Therefore:

✅ No node satisfies the affinity rule

---

# Verification of Failure

Output:

```bash
kubectl get pods
```

Result:

```text
Pending
Pending
```

✅ Correct

---

# Scheduler Events Analysis

Event:

```text
FailedScheduling

0/3 nodes are available:
1 node(s) didn't match Pod's node affinity/selector,
2 node(s) had untolerated taint(s).
```

This is where your troubleshooting becomes interesting.

---

# Let's Decode the Scheduler Message

Cluster:

```text
control-plane
learning-worker
learning-worker2
```

Pod tolerates:

```text
node=worker2:NoSchedule
```

---

## Node: learning-worker

Taint:

```text
node=worker1:NoSchedule
```

Pod does NOT tolerate it.

Result:

❌ Rejected due to taint

---

## Node: control-plane

Taint:

```text
node-role.kubernetes.io/control-plane:NoSchedule
```

Pod does NOT tolerate it.

Result:

❌ Rejected due to taint

---

## Node: learning-worker2

Taint:

```text
node=worker2:NoSchedule
```

Pod tolerates it.

Scheduler proceeds to affinity check.

Affinity:

```text
env=QA
```

Node label:

```text
env=prod
```

Result:

❌ Rejected due to affinity mismatch

---

That's exactly why the scheduler reports:

```text
2 node(s) had untolerated taint(s)
1 node(s) didn't match Pod's node affinity
```

Excellent scheduler reasoning.

---

# One Small Correction

You wrote:

> scheduler finds the matched tolerated taints on 1 node but they have unmatched pod's node affinity

A more precise interview answer:

> The scheduler first filtered out two nodes because the pod lacked the required tolerations. The remaining node passed the taint check but failed the required node affinity rule because its `env` label was `prod` while the pod required `env=QA`.

That wording shows understanding of the scheduler's filtering process.

---

# Fix Review

You changed:

```yaml
values:
  - QA
```

to:

```yaml
values:
  - prod
```

Now:

Node:

```text
learning-worker2
env=prod
```

Affinity:

```text
env=prod
```

Match:

✅ Yes

---

Toleration:

```yaml
value: worker2
```

Node taint:

```text
node=worker2:NoSchedule
```

Match:

✅ Yes

---

Scheduler now has an eligible node.

Result:

```text
Running
Running
```

Perfect.

---

# Production-Level Lesson

This lab demonstrates something many engineers miss:

A node must pass **all** scheduling filters.

Not:

```text
Affinity OR Toleration
```

but effectively:

```text
Affinity AND Toleration AND Resources AND Node Conditions
```

If any required filter fails:

```text
Pending
```

---

# Interview Questions

### Q1

Why did the pod remain Pending?

Expected answer:

> No node satisfied all scheduling constraints. Two nodes were rejected because of untolerated taints, and the remaining node was rejected because its label did not satisfy the required node affinity rule.

---

### Q2

Which scheduler phase failed?

Expected answer:

> The filtering phase. The scheduler could not find any eligible node after applying taint and affinity filters.

---

### Q3

What would happen if the affinity was changed to Preferred instead of Required?

Expected answer:

> The scheduler would try to place the pod on a node with the preferred label, but if none existed, it could still schedule the pod on another eligible node.

This is the next lab.

---

### Q4

Why didn't the scheduler place the pod on learning-worker?

Expected answer:

> Because learning-worker had a `NoSchedule` taint that the pod did not tolerate.

---

### Q5

Could adding a toleration alone fix the issue?

Expected answer:

> No. The node affinity requirement would still fail because no node had the required `env=QA` label.

That's a strong troubleshooting answer.

---

# What an MNC Interviewer Likes About This Lab

You demonstrated:

✅ Reading scheduler events

✅ Understanding taints

✅ Understanding tolerations

✅ Understanding required node affinity

✅ Understanding scheduler filtering

✅ Root cause analysis

✅ Fix validation

This is much closer to a real Kubernetes incident than simple deployment exercises.

---

# Score

| Category                  | Score |
| ------------------------- | ----- |
| Affinity Knowledge        | 10/10 |
| Scheduler Troubleshooting | 10/10 |
| Event Analysis            | 10/10 |
| Root Cause Analysis       | 10/10 |
| Interview Readiness       | 10/10 |

This is the strongest scheduling lab you've submitted so far because it required reasoning across **multiple scheduling constraints simultaneously**, which is exactly what happens in production environments.
