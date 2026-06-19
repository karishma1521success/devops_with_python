Kubernetes Scheduling Practice Lab Series
Lab 1: Observe Default Scheduling
Task
Create a pod named web-pod using nginx image.
Do not specify any scheduling configuration.
Verify which node the pod gets scheduled on.
Find which component made the scheduling decision.
Delete the pod.
Deliverables

Provide:

Note: I have used the deployment to create the pods because in production we will create pods through deployment, instead of using the standalone pods


YAML:

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-pod-deployment
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
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80


Commands
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
web-pod-deployment   1/1     1            1           4m44s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
web-pod-deployment-7bc68dffc-x7v8l   1/1     Running   0          4m48s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl describe pod/web-pod-deployment-7bc68dffc-x7v8l | grep -i "Node"
Node:             learning-worker2/172.18.0.3
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s

Output showing node assignment  - learning-worker2



Explanation
  When I apply kubectl apply -f web-pod-deployment.yaml file to create the pods. It first go to API server to authenticate and authorize and create the deployment and update the object in etcd. Deployment controller will see that there is no replica set created for this deployment so it will created and update to etcd. Now replica set is continously montiroing that the desired state in not maintined there is 1 replica that needs to be created. so api server creates the object for that pod in etcd and transfer the request to the scheduler to assign the node. scheduler will find the suitable node accroding to its method, it has assinged to learning-worker2 node to run this pod. now API server send the request to the kubelet of that node which scheduler assigned a node for that pod. kubelet will instructs the continaer runtime to create and start the pod. container runtime will pull the image, create the container and start the container. and will revert back to kubelet. kubelet will revert back to api server and update the etcd. replica set will also see the desired state is now maintained. 

******************************************************************************************************************

Here's a more interview-ready version of your explanation. It keeps the flow you understand, but uses terminology and sequencing that Kubernetes interviewers expect:

---

### Kubernetes Pod Scheduling Flow (Using Deployment)

When I run:

```bash
kubectl apply -f web-pod-deployment.yaml
```

the request first reaches the **API Server**, which performs authentication and authorization. After validation, the Deployment object is stored in **etcd**, which is Kubernetes' source of truth.

The **Deployment Controller** continuously watches the API Server and notices that a new Deployment has been created. Since no ReplicaSet exists for this Deployment, it creates a ReplicaSet and stores its state in etcd through the API Server.

Next, the **ReplicaSet Controller** observes that the desired replica count is 1, but currently no Pod exists. It creates a Pod object through the API Server. At this stage, the Pod is stored in etcd but has not yet been assigned to any node (`spec.nodeName` is empty).

The **Kubernetes Scheduler** continuously watches for unscheduled Pods. It detects the newly created Pod, evaluates the available nodes using its scheduling process (filtering and scoring), and selects the most suitable node. In my case, the scheduler selected:

```text
learning-worker2
```

The scheduler then updates the Pod's `nodeName` field through the API Server, and this information is stored in etcd.

The **Kubelet** running on `learning-worker2` continuously watches for Pods assigned to its node. Once it sees the Pod assignment, it instructs the container runtime (containerd/CRI-O/Docker, depending on the environment) to start the Pod.

The container runtime:

1. Pulls the nginx image (if not already available).
2. Creates the container.
3. Starts the container.

After the container starts successfully, the Kubelet updates the Pod status through the API Server, which stores the updated state in etcd.

Finally, the ReplicaSet Controller verifies that the desired state (1 replica) matches the current state (1 running Pod), so no further action is required.

---

### Short Interview Version (30 Seconds)

> When I apply a Deployment YAML, the API Server validates and stores the Deployment in etcd. The Deployment Controller creates a ReplicaSet, and the ReplicaSet creates the required Pod. The Pod is initially unscheduled. The Scheduler watches for unscheduled Pods, selects the best node, and updates the Pod's nodeName. The Kubelet on that node then instructs the container runtime to pull the image and start the container. Once the Pod is running, the Kubelet updates its status through the API Server, and the ReplicaSet confirms that the desired number of replicas is maintained.

This version is concise enough for interviews while still demonstrating a solid understanding of how Deployments, ReplicaSets, the Scheduler, Kubelet, API Server, and etcd work together.
