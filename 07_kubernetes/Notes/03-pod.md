# Kubernetes Pods Deep Dive -- CKA & DevOps Notes

## 1. What is a Pod?

A Pod is the smallest deployable unit in Kubernetes.

A Pod: - Wraps one or more containers - Shares the same network (IP) -
Shares storage volumes - Shares lifecycle

Containers inside a Pod communicate using `localhost`.

------------------------------------------------------------------------

## 2. Why Pod Instead of Direct Container?

Pods allow: - Sidecar pattern - Init containers - Shared storage -
Shared networking

------------------------------------------------------------------------

## 3. Pod Networking

-   Each Pod gets its own IP
-   Containers inside share the same IP
-   Pod IP changes if recreated
-   Services provide stable access

Check Pod IP:

``` bash
kubectl get pod -o wide
```

------------------------------------------------------------------------

## 4. Pod Lifecycle Phases

-   Pending
-   Running
-   Succeeded
-   Failed
-   Unknown

Common failure state: ImagePullBackOff

------------------------------------------------------------------------

## 5. Restart Policies

``` yaml
restartPolicy: Always
```

Options: - Always (default) - OnFailure - Never

Deployments always use `Always`.

------------------------------------------------------------------------

## 6. Multi-Container Pod Example

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container
spec:
  containers:
  - name: nginx
    image: nginx
  - name: busybox
    image: busybox
    command: ["sh", "-c", "while true; do sleep 5; done"]
```

Containers communicate via:

    localhost

------------------------------------------------------------------------

## 7. Init Containers

Used for: - Pre-setup tasks - DB checks - Config initialization

Example:

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-example
spec:
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'echo Initializing...; sleep 5']
  containers:
  - name: nginx
    image: nginx
```

Init container must complete before main container starts.

------------------------------------------------------------------------

## 8. Probes (Very Important for CKA)

### Liveness Probe

Checks if container is alive. If fails → container restarts.

### Readiness Probe

Checks if container is ready to receive traffic. If fails → removed from
service endpoints.

### Startup Probe

Used for slow-starting applications.

Example:

``` yaml
livenessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 5
  periodSeconds: 5
```

------------------------------------------------------------------------

## 9. Resource Requests & Limits

``` yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "250m"
  limits:
    memory: "256Mi"
    cpu: "500m"
```

If memory limit exceeded → OOMKilled.

------------------------------------------------------------------------

## 10. Pod Troubleshooting Checklist

1.  kubectl get pod
2.  kubectl describe pod
3.  kubectl logs
4.  kubectl exec
5.  kubectl get events

------------------------------------------------------------------------

## 11. CKA Practice Tasks

1.  Create Pod `cka-pod`
2.  Image: nginx
3.  Label: app=web
4.  Add resource requests
5.  Add liveness probe
6.  Verify restart count

------------------------------------------------------------------------

## Interview Questions

-   Difference between readiness and liveness?
-   What happens if liveness fails?
-   Can a Pod have multiple containers?
-   Why is Pod IP not stable?

------------------------------------------------------------------------

End of Notes