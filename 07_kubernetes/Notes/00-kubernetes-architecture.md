# Kubernetes Architecture Deep Dive -- CKA & DevOps Notes

## 1. What is Kubernetes?

Kubernetes is a container orchestration system.

It: - Deploys containers - Scales applications - Manages networking -
Handles failures - Maintains desired state

Core Principle: Kubernetes continuously ensures the **current state
matches the desired state**.

------------------------------------------------------------------------

## 2. Kubernetes Cluster Structure

A Kubernetes cluster consists of:

-   Control Plane (Master Components)
-   Worker Nodes

Architecture Overview:

Cluster ├── Control Plane └── Worker Nodes

------------------------------------------------------------------------

## 3. Control Plane Components (Brain of the Cluster)

### 3.1 kube-apiserver

-   Entry point for all cluster operations
-   kubectl communicates with API Server
-   Validates requests
-   Stores cluster state in etcd

If API Server is down → cluster becomes unusable.

------------------------------------------------------------------------

### 3.2 etcd

-   Distributed key-value store
-   Stores entire cluster state
-   Stores Pods, Services, Secrets, ConfigMaps, etc.

Important: If etcd is lost and no backup exists → cluster data is lost.

------------------------------------------------------------------------

### 3.3 kube-scheduler

-   Watches for new Pods without assigned nodes
-   Decides which node should run the Pod
-   Decision based on:
    -   CPU availability
    -   Memory availability
    -   Taints & tolerations
    -   Affinity rules

Important: Scheduler assigns node but does NOT create the Pod.

------------------------------------------------------------------------

### 3.4 kube-controller-manager

Runs controllers such as:

-   ReplicaSet controller
-   Deployment controller
-   Node controller
-   Endpoint controller

Controllers ensure desired state is maintained.

Example: If 3 replicas are desired, controller ensures 3 are always
running.

------------------------------------------------------------------------

## 4. Worker Node Components

Each worker node runs:

### 4.1 kubelet

-   Communicates with API Server
-   Ensures containers are running
-   Pulls images
-   Reports status back

------------------------------------------------------------------------

### 4.2 kube-proxy

-   Handles networking rules
-   Manages iptables or IPVS
-   Routes traffic to correct Pods

------------------------------------------------------------------------

### 4.3 Container Runtime

-   containerd (default modern runtime)
-   Docker (deprecated in newer versions)

Responsible for actually running containers.

------------------------------------------------------------------------

## 5. Complete Pod Creation Flow (Very Important)

When you run:

kubectl apply -f pod.yaml

Internal Flow:

1.  kubectl sends request to API Server
2.  API Server validates request
3.  API Server stores object in etcd
4.  Scheduler detects unscheduled Pod
5.  Scheduler assigns a Node
6.  kubelet on that Node pulls image
7.  Container runtime starts container
8.  Status updated back to API Server

------------------------------------------------------------------------

## 6. What Happens If Components Fail?

-   If Scheduler fails → Pods remain in Pending state
-   If kubelet fails → Node becomes NotReady
-   If etcd fails → Cluster state lost
-   If API Server fails → No operations possible

------------------------------------------------------------------------

## 7. Important kubectl Commands for Architecture

Check Nodes:

kubectl get nodes

Check Control Plane Pods:

kubectl get pods -n kube-system

Describe Control Plane Component:

kubectl describe pod `<pod-name>`{=html} -n kube-system

Check Pod Scheduling:

kubectl get pod `<pod-name>`{=html} -o wide

------------------------------------------------------------------------

## 8. Interview-Level Understanding

You must clearly explain:

-   How a Pod is created internally
-   What each control plane component does
-   Why etcd backup is critical
-   What happens when scheduler is down

------------------------------------------------------------------------

## 9. Troubleshooting Scenario

If a Pod is stuck in Pending:

1.  kubectl describe pod
2.  Check events section
3.  Check node resources
4.  Check taints
5.  Check scheduler logs

------------------------------------------------------------------------

End of Kubernetes Architecture Notes