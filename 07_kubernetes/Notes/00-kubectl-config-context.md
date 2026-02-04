[kubernetes-official-website](https://kubernetes.io/)

```md
# Kubernetes (k8s) – Working with Multiple Clusters using kubectl

When working with multiple Kubernetes clusters (e.g., dev, UAT, prod, minikube, EKS), `kubectl` uses **contexts** defined inside the kubeconfig file to determine which cluster to communicate with.

By default, the kubeconfig file is located at:

```

~/.kube/config

````

A **context** in Kubernetes is a combination of:
- Cluster
- User (credentials)
- Namespace

---

# 📌 1. Check Current Kubernetes Context

This command shows which cluster `kubectl` is currently connected to.

```bash
kubectl config current-context
````

### Example Output:

```
minikube
```

This means all `kubectl` commands will run against the `minikube` cluster.

---

# 📌 2. List All Available Contexts

To see all configured cluster contexts:

```bash
kubectl config get-contexts
```

### Example Output:

```
CURRENT   NAME              CLUSTER           AUTHINFO            NAMESPACE
*         minikube         minikube          minikube            default
          dev-cluster      dev-cluster       dev-user            default
          prod-cluster     prod-cluster      prod-user           default
```

* `*` indicates the current active context.
* `NAME` is the context name.
* `CLUSTER` is the actual cluster endpoint.
* `AUTHINFO` is the user credential used.
* `NAMESPACE` is the default namespace for that context.

---

# 📌 3. Switch Between Kubernetes Clusters

To switch to another cluster:

```bash
kubectl config use-context <context-name>
```

### Example:

```bash
kubectl config use-context prod-cluster
```

### Output:

```
Switched to context "prod-cluster".
```

Now all kubectl commands will run against `prod-cluster`.

---

# 📌 4. Verify Cluster After Switching

After switching, verify:

```bash
kubectl cluster-info
```

This shows the API server endpoint of the active cluster.

You can also confirm nodes:

```bash
kubectl get nodes
```

---

# 📌 5. View Complete kubeconfig File

To see full configuration:

```bash
kubectl config view
```

To see it in readable format:

```bash
kubectl config view --minify
```

* `--minify` shows only the current context details.

---

# 📌 6. Rename a Context (Optional but Useful)

```bash
kubectl config rename-context old-name new-name
```

Example:

```bash
kubectl config rename-context arn:aws:eks:region:123456:cluster/prod prod-eks
```

---

# 📌 7. Delete a Context

If you no longer need a cluster:

```bash
kubectl config delete-context <context-name>
```

Example:

```bash
kubectl config delete-context dev-cluster
```

---

# 📌 8. Use Multiple kubeconfig Files (Advanced)

Sometimes you may have multiple kubeconfig files.

You can temporarily specify another kubeconfig:

```bash
KUBECONFIG=/path/to/config kubectl get pods
```

Or export it:

```bash
export KUBECONFIG=/path/to/config
```

You can also merge multiple kubeconfig files:

```bash
export KUBECONFIG=~/.kube/config:~/eks-config
kubectl config view --merge --flatten > merged-config
```

---

# 📌 9. Change Default Namespace in Current Context

Instead of writing `-n namespace` every time:

```bash
kubectl config set-context --current --namespace=<namespace-name>
```

Example:

```bash
kubectl config set-context --current --namespace=production
```

Now all commands run in `production` namespace by default.

---

# 📌 Real-World Example (Dev → Prod Switch)

### Step 1: Check Current Context

```bash
kubectl config current-context
```

### Step 2: Switch to Production

```bash
kubectl config use-context prod-cluster
```

### Step 3: Verify

```bash
kubectl get nodes
kubectl get pods -A
```

---

# 🎯 Important for CKA Exam

In CKA:

* Always verify context before running commands.
* You may need to switch clusters frequently.
* Use `kubectl config get-contexts` quickly to avoid mistakes.
* Double-check namespace before deleting resources.

---

# 🧠 Quick Summary Commands

| Purpose         | Command                                                 |
| --------------- | ------------------------------------------------------- |
| Current Context | `kubectl config current-context`                        |
| List Contexts   | `kubectl config get-contexts`                           |
| Switch Context  | `kubectl config use-context <name>`                     |
| View Config     | `kubectl config view`                                   |
| Set Namespace   | `kubectl config set-context --current --namespace=<ns>` |
| Delete Context  | `kubectl config delete-context <name>`                  |

---

# ✅ Best Practice

Before performing production operations:

```bash
kubectl config current-context
kubectl get nodes
```

Always confirm the cluster to avoid accidental changes in production.

```

---

If you'd like, I can now convert this into a **complete Kubernetes learning roadmap .md file (beginner → advanced → real-world projects → CKA strategy)** tailored to your CKA preparation on Ubuntu.
```
