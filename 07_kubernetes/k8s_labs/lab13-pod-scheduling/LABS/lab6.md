Lab 6: Node Affinity (Required)
Task
Create a pod.
Use Required Node Affinity.
Pod must run only on a node matching a specific label.
Verify behavior.
Deliverables

Provide:

YAML
Commands
Scheduling verification

control plane (learning-control-plane):;    Tainsts: node-role.kubernetes.io/control-plane:NoSchedule                  labels: node-role.kubernetes.io/control-plane=
Worker node1 (learning-worker) :            Taints:  node=worker1                                                      labels: env=uat , storage=hdd
Worker node 2 (learning-worker2):           Taints:  node=worker2                                                       labels: env=prod , storage=sdd



Create a pod.

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-affinity-deployment
spec:
  replicas: 2
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
              memory: "200Mi"

Use Required Node Affinity.
affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: "env"
                    operator: "In"
                    values:
                      - "prod"


It matches with the labels of worker node2 - learning-worker2

Pod must run only on a node matching a specific label.


Verify behavior.


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods -o wide
NAME                                                READY   STATUS    RESTARTS   AGE     IP            NODE               NOMINATED NODE   READINESS GATES
multiple-node-labels-deployment-75d5d88979-tk6b5    1/1     Running   0          3h54m   10.244.1.13   learning-worker    <none>           <none>
multiple-node-labels-deployment2-746b79c895-8vl2m   1/1     Running   0          178m    10.244.2.18   learning-worker2   <none>           <none>
node-affinity-deployment-696959b745-qndxh           1/1     Running   0          52m     10.244.2.20   learning-worker2   <none>           <none>
node-affinity-deployment-696959b745-w6zqk           1/1     Running   0          52m     10.244.2.19   learning-worker2   <none>           <none>
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 




Excellent. This lab is correct and demonstrates the intended behavior of **Required Node Affinity**.

---

# Lab 6 Review

## Objective

> Pod must run only on a node matching a specific label.

You chose:

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: env
              operator: In
              values:
                - prod
```

Node labels:

```text
learning-worker   env=uat
learning-worker2  env=prod
```

Therefore only:

```text
learning-worker2
```

matches the requirement.

✅ Correct

---

# YAML Review

The key scheduling rule is:

```yaml
requiredDuringSchedulingIgnoredDuringExecution
```

The word **required** means:

> If no node satisfies this rule, the pod cannot be scheduled.

This differs from Preferred Node Affinity, which we'll cover later.

---

# Toleration Review

You also included:

```yaml
tolerations:
  - key: "node"
    operator: "Equal"
    value: "worker2"
    effect: "NoSchedule"
```

This is necessary in your lab because you previously tainted:

```text
learning-worker2 -> node=worker2:NoSchedule
```

Without this toleration:

```text
Affinity matches
Taint check fails
Pod remains Pending
```

That's an important production lesson:

> Matching affinity alone is not enough. All scheduling constraints must be satisfied.

---

# Verification

Output:

```bash
kubectl get pods -o wide
```

Result:

```text
node-affinity-deployment-696959b745-qndxh   Running   learning-worker2
node-affinity-deployment-696959b745-w6zqk   Running   learning-worker2
```

Both replicas landed on:

```text
learning-worker2
```

which has:

```text
env=prod
```

✅ Correct

---

# What the Scheduler Did

### Filtering Phase

#### learning-worker

```text
env=uat
```

Affinity requirement:

```text
env=prod
```

Result:

❌ Rejected

---

#### learning-worker2

```text
env=prod
```

Affinity requirement:

```text
env=prod
```

Toleration matches:

```text
node=worker2:NoSchedule
```

Result:

✅ Eligible

---

#### control-plane

Missing label:

```text
env=prod
```

Result:

❌ Rejected

---

Remaining node:

```text
learning-worker2
```

Scheduler assigns both replicas there.

---

# Interview Question

### What does `requiredDuringSchedulingIgnoredDuringExecution` mean?

Strong answer:

> The node affinity rule must be satisfied when the pod is scheduled. If no node matches the rule, the pod remains Pending. After scheduling, Kubernetes does not continuously enforce the rule, so the pod is not evicted if the node labels change later.

That's a very interview-friendly answer.

---

# Another Interview Question

### What would happen if you removed the `env=prod` label from learning-worker2 after the pods were already running?

Expected answer:

> The pods would continue running because the affinity type is `IgnoredDuringExecution`. Kubernetes only evaluates the rule during scheduling.

Many candidates miss this.

---

# One More Interview Question

### Could nodeSelector achieve the same result?

Answer:

Yes.

Example:

```yaml
nodeSelector:
  env: prod
```

would also force scheduling to `learning-worker2`.

The difference is that nodeAffinity provides:

* In
* NotIn
* Exists
* DoesNotExist
* Gt
* Lt

and more complex matching capabilities.

---

# Production Example

A common pattern is:

```text
Node A -> env=dev
Node B -> env=uat
Node C -> env=prod
```

Production workloads:

```yaml
requiredDuringSchedulingIgnoredDuringExecution:
  ...
  env=prod
```

This ensures production applications never run on development or testing nodes.

---

# One Small Improvement

For interview demonstrations, I like to explicitly prove the label exists:

```bash
kubectl get node learning-worker2 --show-labels
```

or

```bash
kubectl describe node learning-worker2
```

before showing pod placement.

Not required, but it strengthens the evidence trail.

---

# Score

### Node Affinity Concepts

10/10

### Scheduling Logic

10/10

### Taints + Affinity Understanding

10/10

### Verification

10/10

### Interview Readiness

10/10

At this point you're already answering Kubernetes scheduling questions at a level above many junior DevOps candidates because you're consistently explaining **why the scheduler selected a node**, not just showing that it happened. The next lab (**Node Affinity Failure**) will build directly on this by intentionally making the affinity rule impossible to satisfy and analyzing the resulting `FailedScheduling` events.
