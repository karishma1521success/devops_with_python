# Kubernetes NGINX Deployment and Service (Interview Ready Guide)

## 1. What is NGINX in Kubernetes?

NGINX is a lightweight web server and reverse proxy commonly used to
test Kubernetes deployments.

In Kubernetes we run it inside a **Pod**, which is managed by a
**Deployment** and exposed using a **Service**.

Architecture:

    User
      │
      ▼
    Service (ClusterIP / NodePort / LoadBalancer)
      │
      ▼
    Deployment
      │
      ▼
    ReplicaSet
      │
      ▼
    Pods (NGINX Containers)

------------------------------------------------------------------------

# 2. Why We Use Deployment Instead of Pod

In production environments, standalone Pods are not used. Deployments
provide:

  Feature                 Why Important
  ----------------------- ----------------------------
  Self healing            Restarts failed pods
  Rolling updates         Zero downtime deployment
  Rollback                Revert to previous version
  Scaling                 Increase replicas
  ReplicaSet management   Maintains desired state

Example interview answer:

> Deployment ensures high availability and manages ReplicaSets, enabling
> rolling updates and automatic recovery of failed Pods.

------------------------------------------------------------------------

# 3. NGINX Deployment YAML (Production Standard)

Create file:

    nginx-deployment.yaml

``` yaml
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
        image: nginx:1.25
        ports:
        - containerPort: 80

        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"

        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 5

        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
```

------------------------------------------------------------------------

# 4. Explanation (Interview Important)

### Replicas

    replicas: 3

Runs 3 pods for high availability.

If one pod crashes, Kubernetes automatically recreates it.

------------------------------------------------------------------------

### Selector

    selector:
      matchLabels:
        app: nginx

Deployment identifies pods using these labels.

------------------------------------------------------------------------

### Template

Defines the **Pod specification** that will be created.

------------------------------------------------------------------------

### Container Image

    image: nginx:1.25

Always pin versions in production.

Bad practice:

    nginx:latest

------------------------------------------------------------------------

# 5. Resource Management (Production Standard)

    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "200m"
        memory: "256Mi"

  Field      Purpose
  ---------- --------------------
  requests   minimum guaranteed
  limits     maximum allowed

Prevents pods from consuming all node resources.

------------------------------------------------------------------------

# 6. Health Checks

## Liveness Probe

Checks whether the container is alive.

If it fails, Kubernetes restarts the container.

## Readiness Probe

Checks whether the container is ready to accept traffic.

If it fails, the pod is removed from service endpoints.

Difference:

  Liveness                      Readiness
  ----------------------------- -----------------------------
  Checks if container alive     Checks if ready for traffic
  Restart container if failed   Stop routing traffic

------------------------------------------------------------------------

# 7. Apply Deployment

    kubectl apply -f nginx-deployment.yaml

Check pods:

    kubectl get pods

Check deployment:

    kubectl get deployment

------------------------------------------------------------------------

# 8. Creating Service for NGINX

Pods have dynamic IP addresses.

A **Service** provides a stable endpoint.

Create file:

    nginx-service.yaml

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort

  selector:
    app: nginx

  ports:
  - port: 80
    targetPort: 80
    nodePort: 30007
```

------------------------------------------------------------------------

# 9. Service Types (Interview Important)

  Service        Purpose
  -------------- ------------------------
  ClusterIP      Internal communication
  NodePort       Expose via node IP
  LoadBalancer   Cloud load balancer
  ExternalName   DNS mapping

In cloud environments like AWS, **LoadBalancer** is commonly used.

------------------------------------------------------------------------

# 10. Apply Service

    kubectl apply -f nginx-service.yaml

Check:

    kubectl get svc

Example output:

    nginx-service   NodePort   10.96.100.5   <none>   80:30007/TCP

Access using:

    http://NODE_IP:30007

------------------------------------------------------------------------

# 11. Production DevOps Flow

Typical CI/CD flow in companies:

    Git Repository
          │
          ▼
    CI Pipeline (Jenkins / GitLab)
          │
          ▼
    Build Docker Image
          │
          ▼
    Push to Registry (ECR / DockerHub)
          │
          ▼
    CD Pipeline (ArgoCD / Flux)
          │
          ▼
    Deploy to Kubernetes

------------------------------------------------------------------------

# 12. Important Interview Questions

## Difference between Deployment and StatefulSet

  Deployment               StatefulSet
  ------------------------ -----------------------
  Stateless applications   Stateful applications
  Random pod names         Fixed pod names
  Web applications         Databases

------------------------------------------------------------------------

## What happens when a pod crashes?

The Deployment automatically creates a new pod to maintain the desired
replica count.

------------------------------------------------------------------------

## How to scale deployment

    kubectl scale deployment nginx-deployment --replicas=5

------------------------------------------------------------------------

## Rollout update

    kubectl set image deployment/nginx-deployment nginx=nginx:1.26

------------------------------------------------------------------------

## Rollback deployment

    kubectl rollout undo deployment nginx-deployment

------------------------------------------------------------------------

# 13. Production Best Practices

Always include:

-   Resource limits
-   Health probes
-   Versioned images
-   Labels
-   Namespace separation
-   ConfigMaps
-   Secrets

------------------------------------------------------------------------

# 14. Production Folder Structure

    k8s/
     ├── deployment.yaml
     ├── service.yaml
     ├── ingress.yaml
     ├── configmap.yaml
     └── namespace.yaml

------------------------------------------------------------------------

# Next Learning Topics

To become strong in Kubernetes interviews, also study:

-   Ingress Controllers
-   ConfigMaps and Secrets
-   Horizontal Pod Autoscaling (HPA)
-   Kubernetes Networking
-   EKS Architecture
-   GitOps using ArgoCD
