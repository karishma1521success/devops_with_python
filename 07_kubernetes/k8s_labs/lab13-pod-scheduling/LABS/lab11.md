Lab 11: Multiple Taints
Task
Add two taints to one node.
Create:
Pod A (matches first taint)
Pod B (matches second taint)
Pod C (matches both)
Observe placement.
Deliverables

Provide:

Commands
YAML



control plane (learning-control-plane):;    Tainsts: node-role.kubernetes.io/control-plane:NoSchedule                  labels: node-role.kubernetes.io/control-plane=
Worker node1 (learning-worker) :            Taints:  node=worker1   nodeName=learning-worker                                                    labels: env=uat , storage=hdd
Worker node 2 (learning-worker2):           Taints:  node=worker2                                                       labels: env=prod , storage=sdd



Add two taints to one node.
Create:
Pod A (matches first taint)

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat lab11-multiple-taints-podA.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-multiple-taints-deployment
  annotations:
    reason: "podA-matches-only-one-taint"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: "podA"
  template:
    metadata:
      labels:
        app: "podA"
    spec:
      tolerations:
        - key: "node"
          operator: "Equal"
          value: "worker1"
          effect: "NoSchedule"
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: "storage"
                    operator: "In"
                    values:
                      - "na"
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


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
node-affinity-preffered-deployment   2/2     2            2           3d17h
node-multiple-taints-deployment      0/2     2            0           17h
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                                  READY   STATUS    RESTARTS      AGE
node-affinity-preffered-deployment-6fb9d97765-44wwf   1/1     Running   1 (22h ago)   3d17h
node-affinity-preffered-deployment-6fb9d97765-n5m4w   1/1     Running   1 (22h ago)   3d17h
node-multiple-taints-deployment-9f8d468c7-fldzr       0/1     Pending   0             17h
node-multiple-taints-deployment-9f8d468c7-px8h6       0/1     Pending   0             17h


Events:
  Type     Reason            Age                  From               Message
  ----     ------            ----                 ----               -------
  Warning  FailedScheduling  11m (x209 over 17h)  default-scheduler  0/3 nodes are available: 3 node(s) had untolerated taint(s). no new claims to deallocate, preemption: 0/3 nodes are available: 3 Preemption is not helpful for scheduling.


scheduler did not find any suitable nodes to assign the pod because out of 3 nodes all are tainted and our pod doesn't have the untolerated taints. To assign the node to a pod. All the taints of a node must satisy by the pod using tolerations. Hence sheduler did not find any node to assign to the pod. pod is in the pending state. 


Pod B (matches second taint)

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat lab11-multiple-taints-podB.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-multiple-taints-deployment-podb
  annotations:
    reason: "podB-matches-only-second-taint"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: "podB"
  template:
    metadata:
      labels:
        app: "podB"
    spec:
      tolerations:
        - key: "nodeName"
          operator: "Equal"
          value: "learning-worker"
          effect: "NoSchedule"
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: "storage"
                    operator: "In"
                    values:
                      - "na"
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



karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
node-multiple-taints-deployment-podb   0/2     2            0           2m27s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods -o wide
NAME                                                    READY   STATUS    RESTARTS   AGE     IP       NODE     NOMINATED NODE   READINESS GATES
node-multiple-taints-deployment-podb-5b68c799dc-2kwvb   0/1     Pending   0          2m34s   <none>   <none>   <none>           <none>
node-multiple-taints-deployment-podb-5b68c799dc-f9gkl   0/1     Pending   0          2m34s   <none>   <none>   <none>           <none>


Events:
  Type     Reason            Age                From               Message
  ----     ------            ----               ----               -------
  Warning  FailedScheduling  26m (x8 over 61m)  default-scheduler  0/3 nodes are available: 3 node(s) had untolerated taint(s). no new claims to deallocate, preemption: 0/3 nodes are available: 3 Preemption is not helpful for scheduling.


IN short, if we are deploying a pod then scheduler will assign the pod only when all the considerations will meet. If a node has two taints, then pod must tolerated all taints

Pod C (matches both)
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl apply -f lab11-multiple-taints-podC.yaml
deployment.apps/node-multiple-taints-deployment-podc created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
node-multiple-taints-deployment-podc   1/2     2            1           6s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get deploy
NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
node-multiple-taints-deployment-podc   2/2     2            2           9s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pods
NAME                                                    READY   STATUS    RESTARTS   AGE
node-multiple-taints-deployment-podc-7456575475-bmt4b   1/1     Running   0          12s
node-multiple-taints-deployment-podc-7456575475-zdhlx   1/1     Running   0          12s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat lab11-multiple-taints-podC.yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-multiple-taints-deployment-podc
  annotations:
    reason: "podC-matches-all-taints"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: "podC"
  template:
    metadata:
      labels:
        app: "podC"
    spec:
      tolerations:
        - key: "nodeName"
          operator: "Equal"
          value: "learning-worker"
          effect: "NoSchedule"
        - key: "node"
          operator: "Equal"
          value: "worker1"
          effect: "NoSchedule"
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: "storage"
                    operator: "In"
                    values:
                      - "na"
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
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 


Pods are scheduled on the learning-worker becauase it has all the tolerated taints. 


Observe placement.
Deliverables