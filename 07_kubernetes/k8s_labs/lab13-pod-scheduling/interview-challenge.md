Interview Challenge (No Google)

After completing all labs, answer these from memory:

What is the difference between nodeSelector and nodeAffinity?
What is the difference between Required and Preferred affinity?
What happens if nodeSelector label doesn't exist?
Difference between NoSchedule and NoExecute?
Can a toleration force a pod onto a node?
Who schedules a pod when nodeName is used?
Why would a pod stay Pending?
How does Kubernetes scheduler select a node?
What is node anti-affinity?
Which scheduling concepts have you used in production and why?

















## ChatGPT Answers ***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************8

These are common Kubernetes scheduling interview questions. Since you have around 1 year of DevOps experience, keep answers simple, practical, and confident.

---

## 1. What is the difference between nodeSelector and nodeAffinity?

**Answer:**

`nodeSelector` is the simplest way to schedule a pod on a node based on labels.

`nodeAffinity` does the same thing but provides more flexibility. It supports conditions like **In, NotIn, Exists** and also supports preferred scheduling.

**Example:**

* nodeSelector → "Run pod only on nodes with label env=prod"
* nodeAffinity → "Prefer prod nodes, but if not available, use another node."

**Interview one-liner:**

> nodeSelector is a simple label-based scheduling method, while nodeAffinity is an advanced and flexible version of nodeSelector.

---

## 2. What is the difference between Required and Preferred affinity?

**Answer:**

### Required Affinity

The condition must be met.

If no matching node is found, the pod remains **Pending**.

### Preferred Affinity

The scheduler tries to follow the rule, but it's not mandatory.

If no matching node exists, the pod can still run on another node.

**Interview one-liner:**

> Required means "must match"; Preferred means "try to match if possible."

---

## 3. What happens if nodeSelector label doesn't exist?

**Answer:**

The scheduler cannot find any matching node.

The pod remains in **Pending** state until a matching node becomes available.

**Interview answer:**

> If the label specified in nodeSelector doesn't exist on any node, Kubernetes cannot schedule the pod and it stays Pending.

---

## 4. Difference between NoSchedule and NoExecute?

**Answer:**

### NoSchedule

Prevents new pods from being scheduled on the node.

Existing pods continue running.

### NoExecute

Prevents new pods and also removes existing pods that don't tolerate the taint.

**Interview one-liner:**

> NoSchedule blocks new pods, while NoExecute blocks new pods and evicts existing ones.

---

## 5. Can a toleration force a pod onto a node?

**Answer:**

No.

A toleration only allows a pod to run on a tainted node.

It does not force scheduling.

To force scheduling, use:

* nodeSelector
* nodeAffinity
* nodeName

**Interview answer:**

> Toleration only allows scheduling on a tainted node. It does not guarantee the pod will be placed there.

---

## 6. Who schedules a pod when nodeName is used?

**Answer:**

The Kubernetes scheduler is bypassed.

The pod is directly assigned to the specified node.

**Interview answer:**

> When nodeName is used, the scheduler does not participate. Kubernetes directly places the pod on the specified node.

---

## 7. Why would a pod stay Pending?

**Answer:**

Common reasons:

* No available node
* nodeSelector mismatch
* nodeAffinity rules not satisfied
* Taints without tolerations
* Insufficient CPU or memory
* PVC not bound
* Node not ready

**Interview answer:**

> A pod stays Pending when Kubernetes cannot find a suitable node or required resources are unavailable.

---

## 8. How does Kubernetes scheduler select a node?

**Answer:**

The scheduler works in two phases:

### 1. Filtering

Removes nodes that don't satisfy requirements:

* Resources
* nodeSelector
* nodeAffinity
* Taints/Tolerations

### 2. Scoring

Ranks remaining nodes and chooses the best one.

**Interview answer:**

> First the scheduler filters unsuitable nodes, then it scores the remaining nodes and selects the best node.

---

## 9. What is node anti-affinity?

**Answer:**

Node anti-affinity prevents pods from running on certain nodes.

It is used when you want to avoid specific nodes.

**Simple example:**

Don't run application pods on GPU nodes or control-plane nodes.

**Interview answer:**

> Node anti-affinity is used to avoid scheduling pods on nodes with specific labels.

---

## 10. Which scheduling concepts have you used in production and why?

Since you worked as a Junior DevOps Engineer, this answer is realistic:

**Answer:**

> In production, I mostly worked with nodeSelector, taints and tolerations, and resource requests/limits.
>
> We used taints and tolerations to keep workloads away from specific nodes and nodeSelector to place workloads on dedicated nodes.
>
> I also checked Pending pods and troubleshooting scheduling issues using kubectl describe pod.
>
> For manual testing and learning, I have also worked with nodeAffinity and nodeName.

This sounds believable for someone with ~1 year of experience and is much better than claiming to use every scheduling feature in production.

---

### Quick Revision (30-second version)

| Question                         | Short Answer                                                   |
| -------------------------------- | -------------------------------------------------------------- |
| nodeSelector vs nodeAffinity     | Simple vs advanced label-based scheduling                      |
| Required vs Preferred            | Must match vs try to match                                     |
| Missing nodeSelector label       | Pod stays Pending                                              |
| NoSchedule vs NoExecute          | Block new pods vs block + evict existing pods                  |
| Can toleration force scheduling? | No                                                             |
| nodeName uses scheduler?         | No, scheduler is bypassed                                      |
| Why Pending?                     | No suitable node/resources                                     |
| Scheduler process?               | Filter → Score → Select                                        |
| Node anti-affinity?              | Avoid specific nodes                                           |
| Production use?                  | nodeSelector, taints/tolerations, troubleshooting Pending pods |

These are exactly the level of answers most interviewers expect from a Junior/Mid DevOps Engineer.
