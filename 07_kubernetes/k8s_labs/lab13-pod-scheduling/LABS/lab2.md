Lab 2: Manual Scheduling (nodeName)
Task
Find available worker nodes.
Create a pod named manual-pod.
Force it to run on a specific node using YAML.
Verify that scheduler did not participate.
Delete the pod.
Deliverables

Provide:

YAML
Commands
Output
Explanation



ANS: 
Find available worker nodes.

kubectl get nodes
NAME                     STATUS   ROLES           AGE     VERSION
learning-control-plane   Ready    control-plane   7d22h   v1.34.8
learning-worker          Ready    <none>          7d22h   v1.34.8
learning-worker2         Ready    <none>          7d22h   v1.34.8


Create a pod named manual-pod.

Note: For the manual pod scheduling, we need to use the standalone pods, because deployment, statefulset and daemonset doesn't provide the feature of manual scheduling. In that case kuberenetes scheduler is involed for scheduling the pod replicas. 

## this is wrong manual scheduling can be done on the deployment, replica set as well but that is not recommended

manual scheduling is used for the testing purposes.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ cat manual-pod.yaml 
---
apiVersion: v1
kind: Pod
metadata:
  name: manual-pod
spec:
  nodeName: learning-worker2
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80



Force it to run on a specific node using YAML.
I have force the pod to run the pod on worker node 2 by providing the nodeName to the spec of the pod. 
This totally bypasses the kubernetes default scheduler. tthe node name is already assigned then the kubelet of that node will insturct the container runtime to create the pods on that node. 

container runtime will pull the image, setup the network namespace, shared storage, and will create the containers within the pod. 


Verify that scheduler did not participate.
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-kz7zh:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason   Age   From     Message
  ----    ------   ----  ----     -------
  Normal  Pulling  9s    kubelet  spec.containers{nginx}: Pulling image "nginx"
  Normal  Pulled   8s    kubelet  spec.containers{nginx}: Successfully pulled image "nginx" in 1.291s (1.291s including waiting). Image size: 63125971 bytes.
  Normal  Created  8s    kubelet  spec.containers{nginx}: Created container: nginx
  Normal  Started  8s    kubelet  spec.containers{nginx}: Started container nginx
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ 

Delete the pod.

karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl delete pod manual-pod
pod "manual-pod" deleted from default namespace
karishma@HO-Desk-D3:~/Documents/devops_with_python/07_kubernetes/k8s_labs/lab13-pod-scheduling$ kubectl get pod
NAME                                 READY   STATUS    RESTARTS   AGE
web-pod-deployment-7bc68dffc-x7v8l   1/1     Running   0          22h