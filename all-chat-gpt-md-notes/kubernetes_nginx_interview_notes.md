# Kubernetes NGINX Deployment -- Complete DevOps Interview Notes

## 1. What is Kubernetes?

Kubernetes (K8s) is an open-source container orchestration platform used
to automate deployment, scaling, and management of containerized
applications.

Key Features: - Container orchestration - Auto scaling - Self healing -
Load balancing - Rolling updates

------------------------------------------------------------------------

# 2. Kubernetes Architecture

## Control Plane Components

-   **API Server** -- Entry point for all kubernetes requests
-   **Scheduler** -- Assigns pods to nodes
-   **Controller Manager** -- Maintains desired state
-   **etcd** -- Key-value database storing cluster state

## Worker Node Components

-   **Kubelet** -- Agent running on each node
-   **Kube Proxy** -- Handles networking rules
-   **Container Runtime** -- Runs containers (Docker/containerd)

------------------------------------------------------------------------

# 3. Namespace

Namespaces logically isolate resources in a Kubernetes cluster.

Example environments: - dev - staging - production

Example YAML:

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dep-svc-ingress-namespace
```

Command:

    kubectl apply -f namespace.yaml

Interview Question:

Q: Why do we use namespaces?

A: Namespaces logically separate workloads in a cluster and help manage
environments like dev, staging, and production.

------------------------------------------------------------------------

# 4. Labels and Selectors

Labels are key value pairs attached to objects.

Example:

    app: nginx
    env: UAT
    team: devops

Selectors use labels to identify resources.

Example:

    kubectl get pods -l app=nginx

------------------------------------------------------------------------

# 5. Deployment

Deployment manages pods and provides: - Self healing - Rolling updates -
Scaling - Rollback

Example Deployment YAML:

``` yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx-deployment
  namespace: dep-svc-ingress-namespace
  labels:
    app: nginx
    env: UAT

spec:
  replicas: 3

  selector:
    matchLabels:
      app: nginx
      env: UAT

  template:
    metadata:
      labels:
        app: nginx
        env: UAT

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
```

Interview Question:

Q: What happens when a pod crashes?

A: The deployment controller creates a new pod automatically to maintain
the desired replica count.

------------------------------------------------------------------------

# 6. Service

Pods have dynamic IPs. Services provide stable networking.

Types of Services:

  Type           Purpose
  -------------- ------------------------
  ClusterIP      Internal communication
  NodePort       Expose via node port
  LoadBalancer   Cloud load balancer
  ExternalName   DNS mapping

Example ClusterIP Service:

``` yaml
apiVersion: v1
kind: Service

metadata:
  name: nginx-service
  namespace: dep-svc-ingress-namespace
  labels:
    app: nginx
    env: UAT

spec:
  type: ClusterIP

  selector:
    app: nginx
    env: UAT

  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
```

Interview Question:

Q: Why do we use services in Kubernetes?

A: Services provide a stable IP and load balance traffic across pods.

------------------------------------------------------------------------

# 7. Ingress

Ingress manages external HTTP/HTTPS access to services.

Traffic Flow:

User → Ingress → Service → Pods

Example Ingress YAML:

``` yaml
apiVersion: networking.k8s.io/v1
kind: Ingress

metadata:
  name: nginx-ingress
  namespace: dep-svc-ingress-namespace

spec:
  rules:
  - host: nginx.example.com

    http:
      paths:
      - path: /
        pathType: Prefix

        backend:
          service:
            name: nginx-service
            port:
              number: 80
```

Important:

Ingress requires an **Ingress Controller** such as: - NGINX Ingress
Controller - AWS ALB Ingress - Traefik

Interview Question:

Q: Can Ingress directly connect to pods?

A: No. Ingress always routes traffic to a Service, which then forwards
traffic to pods.

------------------------------------------------------------------------

# 8. ConfigMap

ConfigMaps store non-sensitive configuration data.

Example:

``` yaml
apiVersion: v1
kind: ConfigMap

metadata:
  name: nginx-config
  namespace: dep-svc-ingress-namespace

data:
  APP_ENV: UAT
```

Interview Question:

Q: What is ConfigMap used for?

A: ConfigMaps store application configuration separate from container
images.

------------------------------------------------------------------------

# 9. Secrets

Secrets store sensitive information.

Examples: - database passwords - API keys - tokens

Example YAML:

``` yaml
apiVersion: v1
kind: Secret

metadata:
  name: nginx-secret
  namespace: dep-svc-ingress-namespace

type: Opaque

data:
  username: YWRtaW4=
  password: cGFzc3dvcmQ=
```

Interview Question:

Q: Difference between ConfigMap and Secret?

A:

  ConfigMap            Secret
  -------------------- ----------------
  Non sensitive data   Sensitive data
  Plain text           Base64 encoded

------------------------------------------------------------------------

# 10. Horizontal Pod Autoscaler (HPA)

HPA automatically scales pods based on CPU or memory.

Example:

``` yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler

metadata:
  name: nginx-hpa
  namespace: dep-svc-ingress-namespace

spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment

  minReplicas: 3
  maxReplicas: 10

  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 60
```

Interview Question:

Q: What is HPA?

A: HPA automatically increases or decreases pod replicas based on
resource usage.

------------------------------------------------------------------------

# 11. Kubernetes Debugging Commands

Check pods

    kubectl get pods

Describe pod

    kubectl describe pod POD_NAME

Check logs

    kubectl logs POD_NAME

Exec inside container

    kubectl exec -it POD_NAME -- /bin/bash

Check services

    kubectl get svc

Check endpoints

    kubectl get endpoints

------------------------------------------------------------------------

# 12. Common Kubernetes Interview Questions

### Q1: Difference between Deployment and StatefulSet

Deployment: - Stateless applications - Dynamic pod names

StatefulSet: - Stateful applications - Stable pod identities

------------------------------------------------------------------------

### Q2: What happens when a node fails?

Pods are rescheduled to another healthy node.

------------------------------------------------------------------------

### Q3: What is rolling update?

Rolling update gradually replaces old pods with new pods without
downtime.

------------------------------------------------------------------------

### Q4: What is self healing in Kubernetes?

Kubernetes automatically recreates failed containers and pods.

------------------------------------------------------------------------

### Q5: What is the difference between Service and Ingress?

Service: - Internal networking - Layer 4

Ingress: - External HTTP/HTTPS routing - Layer 7

------------------------------------------------------------------------

# 13. Real DevOps CI/CD Flow

Developer pushes code

→ GitHub / GitLab

→ CI Pipeline (Jenkins / GitLab CI)

→ Build Docker Image

→ Push to Container Registry

→ CD Pipeline (ArgoCD / Flux)

→ Deploy to Kubernetes

------------------------------------------------------------------------

# 14. Production Folder Structure

    k8s/
     ├── namespace.yaml
     ├── deployment.yaml
     ├── service.yaml
     ├── ingress.yaml
     ├── configmap.yaml
     ├── secret.yaml
     └── hpa.yaml

------------------------------------------------------------------------

# 15. Key DevOps Tools Used with Kubernetes

-   Docker
-   Kubernetes
-   Helm
-   ArgoCD
-   Prometheus
-   Grafana
-   Jenkins
-   GitLab CI

------------------------------------------------------------------------

# 16. Final Interview Tips

Always mention:

-   Resource limits
-   Health checks
-   Namespace isolation
-   ConfigMaps
-   Secrets
-   Autoscaling
-   CI/CD integration
