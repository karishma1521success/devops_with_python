# Kubernetes YAML & NGINX Deployment Notes (Interview Ready)

## 1. YAML Document Separators

### What is `---` in YAML?

`---` is a YAML **document separator**.

It indicates the **start of a new YAML document** inside the same file.

In Kubernetes, a single YAML file can contain **multiple resources**,
such as:

-   Namespace
-   Deployment
-   Service
-   ConfigMap
-   Ingress

To separate them, we use `---`.

------------------------------------------------------------------------

## 2. Example: Multiple Kubernetes Resources in One File

``` yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: dep-svc-ingress-namespace

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: dep-svc-ingress-namespace

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  namespace: dep-svc-ingress-namespace
```

Here:

-   First document → Namespace
-   Second document → Deployment
-   Third document → Service

Apply everything using:

``` bash
kubectl apply -f app.yaml
```

------------------------------------------------------------------------

## 3. Why Namespace YAML Sometimes Starts with `---`

Example:

``` yaml
---
kind: Namespace
apiVersion: v1
metadata:
  name: dep-svc-ingress-namespace
```

This simply means:

> Start of a new YAML document.

------------------------------------------------------------------------

## 4. Why Deployment YAML May Not Use `---`

If the file contains **only one resource**, `---` is optional.

Example:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
```

Kubernetes accepts this without any issue.

------------------------------------------------------------------------

## 5. Production Best Practices (MNC Standard)

### Option 1 --- Separate Files

    k8s/
     ├── namespace.yaml
     ├── deployment.yaml
     ├── service.yaml
     └── ingress.yaml

Deploy using:

``` bash
kubectl apply -f k8s/
```

### Option 2 --- Single Combined File

    k8s-manifest.yaml

``` yaml
---
Namespace

---
Deployment

---
Service

---
Ingress
```

Here `---` **must be used**.

------------------------------------------------------------------------

## 6. Interview Question

**Q: What is `---` in Kubernetes YAML?**

Answer:

`---` is a YAML document separator used to define multiple Kubernetes
resources within a single YAML file. Each section separated by `---` is
treated as a separate Kubernetes object when applied using kubectl.

------------------------------------------------------------------------

## 7. YAML End of Document (`...`)

`...` indicates the **end of a YAML document**.

Example:

``` yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: dev
...
```

However in Kubernetes this is **rarely used** because the file ending
already indicates document completion.

Both of these work:

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev
```

or

``` yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: dev
...
```

------------------------------------------------------------------------

## 8. Why Indentation is Critical in YAML

YAML is **space sensitive** and represents hierarchy using indentation.

Correct:

``` yaml
spec:
  containers:
    - name: nginx
      image: nginx
```

Structure:

    spec
     └── containers
          └── name
          └── image

Wrong:

``` yaml
spec:
containers:
  - name: nginx
    image: nginx
```

Because `containers` must be inside `spec`.

------------------------------------------------------------------------

## 9. Kubernetes Deployment Example (Realistic)

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

## 10. YAML Lists (`-`)

The dash (`-`) represents a **list item**.

Example:

``` yaml
containers:
  - name: nginx
  - name: redis
```

Equivalent JSON:

``` json
containers: [
  {"name": "nginx"},
  {"name": "redis"}
]
```

------------------------------------------------------------------------

## 11. Kubernetes Containers Example

``` yaml
containers:
  - name: nginx
    image: nginx
    ports:
      - containerPort: 80
```

Hierarchy:

    containers
     └── container object
          ├── name
          ├── image
          └── ports
                └── containerPort

------------------------------------------------------------------------

## 12. YAML Anchors & Aliases

Used to reuse configuration.

Example:

``` yaml
default: &default_settings
  memory: 128Mi
  cpu: 100m

container1:
  <<: *default_settings

container2:
  <<: *default_settings
```

Useful in:

-   Helm charts
-   CI/CD pipelines
-   Large YAML files

------------------------------------------------------------------------

## 13. Validation Best Practice

Always validate YAML before applying.

``` bash
kubectl apply --dry-run=client -f deployment.yaml
```

or

``` bash
kubectl apply -f deployment.yaml --validate=true
```

------------------------------------------------------------------------

## 14. Important YAML & Kubernetes Concepts to Learn Next

Senior DevOps engineers often use:

-   envFrom
-   configMapKeyRef
-   secretKeyRef
-   initContainers
-   nodeSelector
-   tolerations
-   affinity

Mastering these will make Kubernetes deployments **production ready and
interview strong**.

------------------------------------------------------------------------

# End of Notes
