Task 3: Scheduler Failure Scenario

Create a pod that requests an unrealistically large amount of resources.

Requirements:

Pod Name:

huge-request-pod

Use nginx.

Configure resource requests high enough that your cluster cannot satisfy them.

Verify

Observe:

kubectl get pods
Not able to create the replica set hence pod is not also created
and

kubectl describe pod huge-request-pod
Deliverables

Provide outputs only.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ kubectl apply -f huge-request-pod-deploy.yaml --dry-run=server
deployment.apps/huge-request-pod-deploy created (server dry run)
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ kubectl apply -f huge-request-pod-deploy.yaml
deployment.apps/huge-request-pod-deploy created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ kubectl get deploy
NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
huge-request-pod-deploy   0/2     0            0           3s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ kubectl describe pod huge-request-pod-deploy
Error from server (NotFound): pods "huge-request-pod-deploy" not found
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ kubectl describe deploy huge-request-pod-deploy
Name:                   huge-request-pod-deploy
Namespace:              default
CreationTimestamp:      Thu, 25 Jun 2026 12:32:57 +0530
Labels:                 app=huge-request-pod
Annotations:            <none>
Selector:               app=huge-request-pod
Replicas:               2 desired | 0 updated | 0 total | 0 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=huge-request-pod
  Containers:
   nginx:
    Image:      nginx
    Port:       80/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     5
      memory:  9223372036854775807
    Requests:
      cpu:         100M
      memory:      9223372036854775807
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     node=worker1:NoSchedule
                   nodeName=learning-worker:NoSchedule
Conditions:
  Type          Status  Reason
  ----          ------  ------
  Progressing   False   ReplicaSetCreateError
Events:
  Type     Reason                 Age                From                   Message
  ----     ------                 ----               ----                   -------
  Warning  ReplicaSetCreateError  5s (x13 over 25s)  deployment-controller  Failed to create new replica set "huge-request-pod-deploy-565fb7cbdc": ReplicaSet.apps "huge-request-pod-deploy-565fb7cbdc" is invalid: spec.template.spec.containers[0].resources.requests: Invalid value: "100M": must be less than or equal to cpu limit of 5
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ cat huge-request-pod-deploy.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: huge-request-pod-deploy
  namespace: default
  labels:
    app: huge-request-pod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: huge-request-pod
  revisionHistoryLimit: 5
  template:
    metadata:
      labels:
        app: huge-request-pod
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
              cpu: "100000000000m"
              memory: "1280000000000000Mi"
            limits:
              cpu: "5000000000000000000000000000000m"
              memory: "256000000000000000000000000Mi"
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab14-Resources/labs$ 



## Chat gpt

This is actually a very valuable learning moment because you did **not reach the scheduler at all**.

You discovered a different validation layer in Kubernetes.

# What Happened?

You expected:

```text
Deployment -> ReplicaSet -> Pod -> Pending
```

because of insufficient resources.

Instead you got:

```text
Deployment -> ReplicaSet creation failed
```

with:

```text
ReplicaSetCreateError
```

---

# Why?

Look at the error:

```text
Invalid value: "100M": must be less than or equal to cpu limit of 5
```

Kubernetes validates resource specifications before creating Pods.

Your values became effectively:

```yaml
requests:
  cpu: 100M

limits:
  cpu: 5
```

and Kubernetes detected:

```text
Request > Limit
```

which is invalid.

A container cannot request more resources than its limit.

Therefore:

```text
Deployment created ✅
ReplicaSet created ❌
Pod created ❌
Scheduler involved ❌
```

---

# Interviewer's Question

If I ask:

> Why was no Pod created?

A good answer is:

> The Deployment object was accepted, but the Pod template was invalid. Kubernetes validation rejected ReplicaSet creation because the CPU request exceeded the CPU limit. Since no ReplicaSet was created, no Pods were created and the scheduler never got a chance to evaluate the workload.

That's a strong answer.

---

# Did Task 3 Succeed?

Not yet.

The purpose of Task 3 is to observe:

```text
Pod = Pending
```

due to:

```text
Insufficient CPU
or
Insufficient Memory
```

Your configuration failed earlier during API validation.

---

# What You Need To Do

Create a valid resource configuration.

Meaning:

```text
Request <= Limit
```

must be true.

Then make the request so large that no node can satisfy it.

Example thought process:

1. Find node allocatable resources.

```bash
kubectl describe node learning-worker
```

2. Observe allocatable CPU and memory.

3. Create a pod requesting more than available.

Result should be:

```text
Pod Created ✅
Pod Scheduled ❌
Pod Pending ✅
```

Then you'll see events similar to:

```text
0/2 nodes are available:
Insufficient cpu
```

or

```text
0/2 nodes are available:
Insufficient memory
```

Now you're testing the scheduler.

---

# Another Important Observation

You tried:

```yaml
cpu: "100000000000m"
memory: "1280000000000000Mi"
```

This is not how engineers usually test scheduling failures.

In interviews and production troubleshooting we use realistic values:

Example:

```yaml
requests:
  cpu: "10"
  memory: "20Gi"
```

or

```yaml
requests:
  cpu: "50"
  memory: "100Gi"
```

Large enough to exceed node capacity but still readable.

---

# What I Like

You checked:

```bash
kubectl describe deploy
```

instead of assuming the scheduler was broken.

That's exactly what a DevOps engineer should do:

```text
Observe
Read Events
Identify Layer of Failure
```

You discovered:

```text
API Validation Failure
```

not

```text
Scheduler Failure
```

which is a very important distinction.

---

### Next Challenge

Without creating anything yet, answer this:

Suppose a node has:

```text
Allocatable CPU: 2 cores
Allocatable Memory: 4Gi
```

and a pod requests:

```yaml
requests:
  cpu: "3"
  memory: "1Gi"
limits:
  cpu: "3"
  memory: "1Gi"
```

What do you expect?

1. Deployment created?
2. ReplicaSet created?
3. Pod created?
4. Pod status?
5. Event message?

Think through each Kubernetes component step-by-step before running it. That's the mindset that helps in interviews and production troubleshooting.
