Task 1: Create Deployment

Create a deployment named nginx-deployment with:

Image: nginx
Replicas: 3

kubectl get deployments
kubectl get rs
kubectl get pods -o wide


Ans: 
deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get deploy
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           7m14s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get rs
NAME                          DESIRED   CURRENT   READY   AGE
frontend-rs                   4         4         4       44h
nginx-deployment-7ccccd94f7   3         3         3       7m18s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
backend                             1/1     Running   0          2d
frontend                            1/1     Running   0          2d
frontend-rs-btcwk                   1/1     Running   0          44h
frontend-rs-cd82t                   1/1     Running   0          44h
frontend-rs-hh2d2                   1/1     Running   0          44h
mysql                               1/1     Running   0          2d
nginx-deployment-7ccccd94f7-5zccv   1/1     Running   0          7m23s
nginx-deployment-7ccccd94f7-mbjk7   1/1     Running   0          7m23s
nginx-deployment-7ccccd94f7-wgnzj   1/1     Running   0          7m23s
nginx-service-test                  1/1     Running   0          2d
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl rollout status deployment/nginx-deployment
deployment "nginx-deployment" successfully rolled out
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl rollout history deployment/nginx-deployment
deployment.apps/nginx-deployment 
REVISION  CHANGE-CAUSE
1         <none>








***********************************************************************************************************************

Task 2: Expose Deployment Using ClusterIP

Create a Service named:

nginx-clusterip

Requirements:

Type: ClusterIP
Port: 80
TargetPort: 80
Selector: app=nginx
Verify
kubectl get svc
kubectl describe svc nginx-clusterip
Questions
What IP does the service receive? - 10.96.20.149

Is that IP reachable outside the cluster? - No
How many endpoints are attached? - 3 endpoints are attached
'


karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ cat service.yaml 
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-clusterip
  labels:
    app: nginx
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80




karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get svc
NAME              TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes        ClusterIP   10.96.0.1      <none>        443/TCP   3d
nginx-clusterip   ClusterIP   10.96.20.149   <none>        80/TCP    53s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl describe svc nginx-clusterip
Name:                     nginx-clusterip
Namespace:                default
Labels:                   app=nginx
Annotations:              <none>
Selector:                 app=nginx
Type:                     ClusterIP
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.96.20.149
IPs:                      10.96.20.149
Port:                     <unset>  80/TCP
TargetPort:               80/TCP
Endpoints:                10.244.2.14:80,10.244.1.17:80,10.244.1.16:80
Session Affinity:         None
Internal Traffic Policy:  Cluster
Events:                   <none>
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ 



***********************************************************************************************************************
Task 3: Verify Service Discovery

Launch a temporary pod:

kubectl run test-pod --image=busybox -it --rm -- sh

Inside the pod:

wget -qO- http://nginx-clusterip

or

nslookup nginx-clusterip
Question

Why can the pod reach the service without knowing pod IPs?
Ans: Because pod is hitting the service name in which coreDNS is resolving the service name to the endpoints IP



***********************************************************************************************************************

Task 4: Inspect Endpoints

Check:

kubectl get endpoints

or

kubectl describe endpoints nginx-clusterip
Question

What endpoint IPs are shown?
 10.244.1.16:80,10.244.1.17:80,10.244.2.14:80

Do they match pod IPs?

yes
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get endpoints nginx-clusterip
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME              ENDPOINTS                                      AGE
nginx-clusterip   10.244.1.16:80,10.244.1.17:80,10.244.2.14:80   124m
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods -o wide
NAME                                READY   STATUS    RESTARTS   AGE    IP            NODE               NOMINATED NODE   READINESS GATES
nginx-deployment-7ccccd94f7-5zccv   1/1     Running   0          141m   10.244.1.16   learning-worker    <none>           <none>
nginx-deployment-7ccccd94f7-mbjk7   1/1     Running   0          141m   10.244.2.14   learning-worker2   <none>           <none>
nginx-deployment-7ccccd94f7-wgnzj   1/1     Running   0          141m   10.244.1.17   learning-worker    <none>           <none>
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ 


***********************************************************************************************************************

Task 5: Create NodePort Service

Expose deployment externally.

Create service:

Name: nginx-nodeport
Type: NodePort
Port: 80
TargetPort: 80
NodePort: 30080

Verify:

kubectl get svc

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ cat node-port-service.yaml 
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
  labels:
    app: nginx
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - nodePort: 30080
      port: 80
      targetPort: 80
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ yamllint node-port-service.yaml 
node-port-service.yaml
  1:1       warning  missing document start "---"  (document-start)

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ nano node-port-service.yaml 
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ yamllint node-port-service.yaml 
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f  node-port-service.yaml --dry-run=client
service/nginx-nodeport created (dry run)
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f  node-port-service.yaml --dry-run=server
service/nginx-nodeport created (server dry run)
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f  node-port-service.yaml
service/nginx-nodeport created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get svc
NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP        3d2h
nginx-nodeport   NodePort    10.96.169.163   <none>        80:30080/TCP   4s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get endpoints nginx-nodeport
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME             ENDPOINTS                                      AGE
nginx-nodeport   10.244.1.16:80,10.244.1.17:80,10.244.2.14:80   18s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods -o wide
NAME                                READY   STATUS    RESTARTS   AGE    IP            NODE               NOMINATED NODE   READINESS GATES
nginx-deployment-7ccccd94f7-5zccv   1/1     Running   0          171m   10.244.1.16   learning-worker    <none>           <none>
nginx-deployment-7ccccd94f7-mbjk7   1/1     Running   0          171m   10.244.2.14   learning-worker2   <none>           <none>
nginx-deployment-7ccccd94f7-wgnzj   1/1     Running   0          171m   10.244.1.17   learning-worker    <none>           <none>
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ 




***********************************************************************************************************************
Task 6: Access Application

Find node IP:

kubectl get nodes -o wide

Access:

http://NODE-IP:30080
Question

Why can users access application without knowing pod IPs?
yes, pod is ephemeral in nature. if a user is accessing the application using the pod IP, then if pod dies, then using that Ip user won't be able to access the application. 
that's why service came into a picture which provides a stable ip to access the application and it also provides the load balancing feature. 
user will only able to know the IP of service and they can access the application irrespective of pod lifecycle.



***********************************************************************************************************************
Task 7: Test Load Balancing

Refresh browser multiple times.

Or:

while true
do
curl http://NODE-IP:30080
sleep 1
done
Question

How does Kubernetes distribute traffic among pods?
service in kubernetes provide the features of the load balancing, it automatically distribute the traffic to it's endpoints. 
It also makes sure that if any pod of it's endpoint is unhealthy at that time it only sends the traffic to other healthy endpoints.





***********************************************************************************************************************
Task 8: Delete One Pod

Delete one nginx pod.

kubectl delete pod POD_NAME

Verify:

kubectl get pods
kubectl get endpoints
Questions

Did service stop working?
No
Did endpoints change automatically? yes it automatically removed the endpoint of the deleted pod and updated with the new pod.
Why?

kubernetes service selects the pod using the labels and selectors. and if a pod deleted then a new pod is created with the same label by the replic set to mantain the desired state. hence the new IP address assigned to that Ip and that pods has the same labels as the service selectors so it select that pod.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-7ccccd94f7-5zccv   1/1     Running   0          177m
nginx-deployment-7ccccd94f7-mbjk7   1/1     Running   0          177m
nginx-deployment-7ccccd94f7-wgnzj   1/1     Running   0          177m
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl delete pod/nginx-deployment-7ccccd94f7-5zccv
pod "nginx-deployment-7ccccd94f7-5zccv" deleted from default namespace
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-7ccccd94f7-8j7hn   1/1     Running   0          3s
nginx-deployment-7ccccd94f7-mbjk7   1/1     Running   0          178m
nginx-deployment-7ccccd94f7-wgnzj   1/1     Running   0          178m
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get endpoints nginx-nodeport
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME             ENDPOINTS                                      AGE
nginx-nodeport   10.244.1.17:80,10.244.2.14:80,10.244.2.17:80   7m54s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods -o wide
NAME                                READY   STATUS    RESTARTS   AGE    IP            NODE               NOMINATED NODE   READINESS GATES
nginx-deployment-7ccccd94f7-8j7hn   1/1     Running   0          33s    10.244.2.17   learning-worker2   <none>           <none>
nginx-deployment-7ccccd94f7-mbjk7   1/1     Running   0          179m   10.244.2.14   learning-worker2   <none>           <none>
nginx-deployment-7ccccd94f7-wgnzj   1/1     Running   0          179m   10.244.1.17   learning-worker    <none>           <none>


***********************************************************************************************************************
Task 9: Scale Deployment

Scale to 5 replicas.

kubectl scale deployment nginx-deployment --replicas=5

Verify:

kubectl get pods
kubectl get endpoints
Question

How many endpoints are attached now?
5





***********************************************************************************************************************
Task 10: Selector Matching

Check labels on pods.

kubectl get pods --show-labels

Check service selectors.

kubectl describe svc nginx-clusterip
Question

What happens if selector doesn't match any pod?
It will not create the service. because to create the service. selector and labels must match all the expressions. 
selectors follow the logical AND.




***********************************************************************************************************************



Challenge Task 1

Create:

Deployment: apache-deployment
Image: httpd
Replicas: 2

Expose with:

Service: apache-service
Type: ClusterIP
Port: 80

Verify connectivity using BusyBox pod.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ cat apache-deployment.yaml 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: apache-deployment
  labels:
    app: apache
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: apache
    spec:
      containers:
        - name: apache
          image: httpd
          ports:
            - containerPort: 80
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ yamllint apache-deployment.yaml 
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f apache-deployment.yaml --dry-run=client
deployment.apps/apache-deployment created (dry run)
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f apache-deployment.yaml --dry-run=server
The Deployment "apache-deployment" is invalid: spec.template.metadata.labels: Invalid value: {"app":"apache"}: `selector` does not match template `labels`
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ nano apache-deployment.yaml
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ nano apache-deployment.yaml 
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f apache-deployment.yaml --dry-run=server
deployment.apps/apache-deployment created (server dry run)
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f apache-deployment.yaml
deployment.apps/apache-deployment created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ ls
apache-deployment.yaml  deployment.yaml  lab5-answers.md  node-port-service.yaml  service.yaml
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ nano apache-service.yaml
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ nano apache-service.yaml

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ cat service.yaml 
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-clusterip
  labels:
    app: nginx
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ yamllint apache-service.yaml 
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f apache-service.yaml --dry-run=server
service/apache-service created (server dry run)
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl apply -f apache-service.yaml
service/apache-service created
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get svc
NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
apache-service   ClusterIP   10.96.49.117    <none>        80/TCP         30s
kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP        3d3h
nginx-nodeport   NodePort    10.96.169.163   <none>        80:30080/TCP   24m
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get endpoints apache-service
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME             ENDPOINTS                       AGE
apache-service   10.244.1.19:80,10.244.2.19:80   63s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods -o wide
NAME                                 READY   STATUS    RESTARTS   AGE     IP            NODE               NOMINATED NODE   READINESS GATES
apache-deployment-558c6fc8bc-cpfwq   1/1     Running   0          3m46s   10.244.2.19   learning-worker2   <none>           <none>
apache-deployment-558c6fc8bc-g8864   1/1     Running   0          3m46s   10.244.1.19   learning-worker    <none>           <none>
nginx-deployment-7ccccd94f7-8j7hn    1/1     Running   0          17m     10.244.2.17   learning-worker2   <none>           <none>
nginx-deployment-7ccccd94f7-hh2wl    1/1     Running   0          13m     10.244.1.18   learning-worker    <none>           <none>
nginx-deployment-7ccccd94f7-mbjk7    1/1     Running   0          3h16m   10.244.2.14   learning-worker2   <none>           <none>
nginx-deployment-7ccccd94f7-s5n9w    1/1     Running   0          13m     10.244.2.18   learning-worker2   <none>           <none>
nginx-deployment-7ccccd94f7-wgnzj    1/1     Running   0          3h16m   10.244.1.17   learning-worker    <none>           <none>
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get deploy
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
apache-deployment   2/2     2            2           4m6s
nginx-deployment    5/5     5            5           3h16m
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl run test --image=busybox --it --rm -- bash
error: unknown flag: --it
See 'kubectl run --help' for usage.
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl run test --image=busybox -it --rm -- /bin/bash



curl
^Ckarishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl run test --image=busybox -it --rm -- sh
Error from server (AlreadyExists): pods "test" already exists
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl get pods
NAME                                 READY   STATUS             RESTARTS      AGE
apache-deployment-558c6fc8bc-cpfwq   1/1     Running            0             5m33s
apache-deployment-558c6fc8bc-g8864   1/1     Running            0             5m33s
nginx-deployment-7ccccd94f7-8j7hn    1/1     Running            0             19m
nginx-deployment-7ccccd94f7-hh2wl    1/1     Running            0             15m
nginx-deployment-7ccccd94f7-mbjk7    1/1     Running            0             3h17m
nginx-deployment-7ccccd94f7-s5n9w    1/1     Running            0             15m
nginx-deployment-7ccccd94f7-wgnzj    1/1     Running            0             3h17m
test                                 0/1     CrashLoopBackOff   2 (21s ago)   45s
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl delete pod test
pod "test" deleted from default namespace
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ kubectl run test-pod --image=busybox -it --rm -- sh
All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
/ # wget -qO- apache-service
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>It works! Apache httpd</title>
</head>
<body>
<p>It works!</p>
</body>
</html>
/ # exit
Session ended, resume using 'kubectl attach test-pod -c test-pod -i -t' command when the pod is running
pod "test-pod" deleted from default namespace
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab5-service$ 



***********************************************************************************************************************

Challenge Task 2

Create two deployments:

frontend
backend

Create separate services for both.

Verify:

frontend-service
backend-service

Only frontend service should route traffic to frontend pods.

Only backend service should route traffic to backend pods.





***********************************************************************************************************************


Challenge Task 3 (Interview Level)

Create:

Deployment: nginx
Replicas: 3

Create Service:

Type: ClusterIP

Delete all pods one by one and observe:

kubectl get endpoints -w

Understand how Kubernetes dynamically updates service endpoints.







Expected Interview Topics After This Lab

Be ready to answer:

Service vs Pod
Why Pod IP is not reliable
ClusterIP vs NodePort vs LoadBalancer
What is Service Discovery
What are Endpoints
How Service Selectors work
How Load Balancing works
Why Services are needed
What happens when Pod IP changes
DNS in Kubernetes