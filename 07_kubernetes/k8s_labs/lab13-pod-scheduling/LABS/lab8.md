Lab 8: Preferred Node Affinity
Task
Configure Preferred Affinity.
Create pod.
Observe where scheduler places it.
Explain why the pod still runs even if preference isn't met.
Deliverables

Provide:

YAML
Scheduling result
Explanation

control plane (learning-control-plane):;    Tainsts: node-role.kubernetes.io/control-plane:NoSchedule                  labels: node-role.kubernetes.io/control-plane=
Worker node1 (learning-worker) :            Taints:  node=worker1                                                      labels: env=uat , storage=hdd
Worker node 2 (learning-worker2):           Taints:  node=worker2                                                       labels: env=prod , storage=sdd


Configure Preferred Affinity.

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-affinity-preffered-deployment
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
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: "storage"
                    operator: "In"
                    values:
                      - "sdd"
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




Create pod.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl apply -f lab8-node-affinity-failure.yaml 
deployment.apps/node-affinity-preffered-deployment created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
node-affinity-preffered-deployment   2/2     2            2           9s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods -o wide
NAME                                                  READY   STATUS    RESTARTS   AGE   IP            NODE               NOMINATED NODE   READINESS GATES
node-affinity-preffered-deployment-6fb9d97765-44wwf   1/1     Running   0          28s   10.244.2.25   learning-worker2   <none>           <none>
node-affinity-preffered-deployment-6fb9d97765-n5m4w   1/1     Running   0          28s   10.244.2.26   learning-worker2   <none>           <none>


Observe where scheduler places it.
learning-worker2

Explain why the pod still runs even if preference isn't met.
preference is met but the node taints are met to the tolerations pod





You've correctly created and scheduled the pods, but for **Lab 8** there's a conceptual issue.

## What Happened?

Your affinity configuration is:

```yaml
requiredDuringSchedulingIgnoredDuringExecution:
  nodeSelectorTerms:
    - matchExpressions:
        - key: env
          operator: In
          values:
            - prod

preferredDuringSchedulingIgnoredDuringExecution:
  - weight: 100
    preference:
      matchExpressions:
        - key: storage
          operator: In
          values:
            - sdd
```

And your node labels are:

```text
learning-worker   env=uat   storage=hdd
learning-worker2  env=prod  storage=sdd
```

So:

### Required Affinity

```text
env=prod
```

Only:

```text
learning-worker2
```

matches.

### Preferred Affinity

```text
storage=sdd
```

Also only:

```text
learning-worker2
```

matches.

Therefore:

```text
Required = matched
Preferred = matched
```

The scheduler had only one eligible node anyway.

---

# Why This Doesn't Fully Demonstrate Preferred Affinity

The lab asked:

> Explain why the pod still runs even if preference isn't met.

But in your test:

```text
Preference WAS met.
```

So you didn't actually observe the behavior of Preferred Affinity when the preference cannot be satisfied.

---

# Your Explanation

You wrote:

> preference is met but the node taints are met to the tolerations pod

That's true, but it doesn't answer the lab question.

The key concept of Preferred Affinity is:

> Preferred rules influence scoring, not eligibility.

---

# Interview Explanation

A strong answer would be:

> `preferredDuringSchedulingIgnoredDuringExecution` is a soft rule. The scheduler tries to place the pod on nodes matching the preference and gives those nodes a higher score. However, if no node satisfies the preferred rule, the pod can still be scheduled on another eligible node as long as all required scheduling conditions are met.

---

# How to Properly Demonstrate Preferred Affinity

With your cluster:

```text
learning-worker   env=uat   storage=hdd
learning-worker2  env=prod  storage=sdd
```

you could test something like:

```yaml
required:
  env=prod

preferred:
  storage=nvme
```

No node has:

```text
storage=nvme
```

Then:

### Required check

```text
learning-worker2 -> PASS
```

### Preferred check

```text
storage=nvme -> no match
```

Yet the pod would still schedule to:

```text
learning-worker2
```

because preferred affinity is only a preference.

That would perfectly demonstrate the concept.

---

# Scheduler Perspective

Think of it like:

### Required Affinity

```text
Can this node be considered?
```

If No:

```text
Reject node
```

---

### Preferred Affinity

```text
How much do I like this node?
```

If preference matches:

```text
Higher score
```

If preference doesn't match:

```text
Lower score
```

But the node can still be selected.

---

# Interview Question

### What is the difference between Required and Preferred Node Affinity?

Expected answer:

**Required**

> Mandatory. If no node satisfies the rule, the pod remains Pending.

**Preferred**

> Optional. Nodes matching the rule receive a higher scheduling score, but the pod can still run on other eligible nodes.

---

# Score

### YAML

10/10

### Scheduling Verification

10/10

### Preferred Affinity Understanding

7.5/10

The deployment works correctly, but it doesn't actually demonstrate the "preference not met" scenario that this lab is designed to teach.

### What I'd Do

Keep the same deployment and change only the preferred label to something that doesn't exist in the cluster.

Then observe:

```text
Pod still Running
```

and explain:

> The required affinity was satisfied, so the scheduler found an eligible node. The preferred affinity was not satisfied, but preferred rules are not mandatory; they only affect node scoring.

Once you do that, you'll have fully mastered the difference between **Required** and **Preferred** Node Affinity—a very common Kubernetes interview topic.
