Lab 3: Unschedulable Pod
Task
Create a pod.
Intentionally configure it so Kubernetes cannot schedule it anywhere.
Pod should remain in Pending.
Find the exact reason.
Fix the issue and make pod run.
Deliverables

Provide:

YAML
Commands
Events output
Root cause analysis



Create a pod.
---
apiVersion: v1
kind: Pod
metadata:
  name: unschedulable-pod
spec:
  nodeName: learning-worker3
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80

Intentionally configure it so Kubernetes cannot schedule it anywhere.


Pod should remain in Pending.
nodeName: learning-worker3


Find the exact reason.
It's in pending because the nodeName we have mentioned manually that node doesn't exists and schedular is not involved hence. no events shown


Fix the issue and make pod run.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl apply -f unschedulable-pod.yaml 
pod/unschedulable-pod created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
unschedulable-pod                    1/1     Running   0          3s
web-pod-deployment-7bc68dffc-x7v8l   1/1     Running   0          23h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat unschedulable-pod.yaml 
---
apiVersion: v1
kind: Pod
metadata:
  name: unschedulable-pod
spec:
  nodeName: learning-worker2
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get nodes
NAME                     STATUS   ROLES           AGE   VERSION
learning-control-plane   Ready    control-plane   8d    v1.34.8
learning-worker          Ready    <none>          8d    v1.34.8
learning-worker2         Ready    <none>          8d    v1.34.8
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 

As you can see I have fixed the yaml manifest and provide the correct node name to it. hence the pod is in running state. 


What I Want You To Do

Redo Lab 3.

This time:

Do not use nodeName.
Make Kubernetes Scheduler try to schedule the pod.
Cause the scheduler to fail.
Keep the pod in Pending.
Collect:
kubectl get pods
kubectl describe pod
Events
Explain exactly why scheduling failed.
Then fix it and make it run.

Don't worry about finding the method immediately. The investigation process is where most of the learning happens.

This is much closer to real-world DevOps incidents, where the scheduler is active but unable to place a pod.

I have tainted both the nodes

kubectl taint node learning-worker node=worker1:NoSchedule
kubectl taint node learning-worker2 node=worker2:NoSchedule


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat unschedulable-pod-deploy.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: unschedulable-pod-deployment
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      name: unschedule-pod
      labels:
        app: nginx
    spec:
      tolerations:
        - key: "node"
          operator: "Equal"
          value: "worker3"
          effect: "NoSchedule"
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl apply -f unschedulable-pod-deploy.yaml
deployment.apps/unschedulable-pod-deployment created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
unschedulable-pod-deployment   0/1     1            0           3s
web-pod-deployment             1/1     1            1           24h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                            READY   STATUS    RESTARTS   AGE
unschedulable-pod                               1/1     Running   0          57m
unschedulable-pod-deployment-596fc67d99-dbcc2   0/1     Pending   0          8s
web-pod-deployment-7bc68dffc-x7v8l              1/1     Running   0          24h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl describe pods unschedulable-pod-deployment-596fc67d99-dbcc2
Name:             unschedulable-pod-deployment-596fc67d99-dbcc2
Namespace:        default
Priority:         0
Service Account:  default
Node:             <none>
Labels:           app=nginx
                  pod-template-hash=596fc67d99
Annotations:      <none>
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    ReplicaSet/unschedulable-pod-deployment-596fc67d99
Containers:
  nginx:
    Image:        nginx
    Port:         80/TCP
    Host Port:    0/TCP
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-b2fwf (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  kube-api-access-b2fwf:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node=worker3:NoSchedule
                             node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  18s   default-scheduler  0/3 nodes are available: 3 node(s) had untolerated taint(s). no new claims to deallocate, preemption: 0/3 nodes are available: 3 Preemption is not helpful for scheduling.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat unschedulable-pod-deploy.yaml 




All the nodes are tainted and the pods created using the deployment has the tolerations but it does not match with any available nodes. hence schedular did not find any nodes to assign the pod because pod does not match the tolerations to schedule on the pod. 

Taints and toleration works on logical AND.

taints on node must match the tolerations on pod.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl apply -f unschedulable-pod-deploy.yaml 
deployment.apps/unschedulable-pod-deployment configured
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                            READY   STATUS    RESTARTS   AGE
unschedulable-pod                               1/1     Running   0          70m
unschedulable-pod-deployment-78b7cc764d-s96p5   1/1     Running   0          6s
web-pod-deployment-7bc68dffc-x7v8l              1/1     Running   0          24h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat unschedulable-pod-deploy.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: unschedulable-pod-deployment
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      name: unschedule-pod
      labels:
        app: nginx
    spec:
      tolerations:
        - key: "node"
          operator: "Equal"
          value: "worker2"
          effect: "NoSchedule"
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 


## All worker nodes were tainted with NoSchedule taints. The pod had a toleration for node=worker3:NoSchedule, but no node in the cluster had that taint. Since the pod did not tolerate the taints present on any available node, the scheduler could not find a suitable node and left the pod in Pending state.
## Every NoSchedule taint on a node must be tolerated by the pod. If even one taint is not tolerated, the scheduler will reject that node.

## No. A toleration only allows the scheduler to consider that node. The scheduler may still choose another eligible node if it satisfies all scheduling requirements and receives a better score.