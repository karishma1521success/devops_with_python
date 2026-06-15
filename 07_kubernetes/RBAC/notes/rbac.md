# Kubernetes Authentication & Authorization Mastery Roadmap

## Goal

Become confident in Kubernetes Authentication and Authorization from beginner to advanced level with:

* Deep theory understanding
* Real-world industry concepts
* Hands-on labs on a Kind cluster
* Troubleshooting practice
* RBAC debugging
* ServiceAccount usage
* TLS certificates
* OIDC and enterprise auth concepts

This roadmap is designed like a real DevOps/SRE/Kubernetes Engineer training path.

---

# PHASE 1 — FOUNDATION

Before learning authentication and authorization, you must understand:

## Concepts You Must Know

### 1. Kubernetes Architecture

Understand:

* API Server
* etcd
* Controller Manager
* Scheduler
* Kubelet
* kube-proxy

Most authentication and authorization happens through:

👉 kube-apiserver

Every request goes through:

```text
Authentication → Authorization → Admission Controller
```

---

## Request Flow

```text
kubectl get pods
        ↓
Kubeconfig sends credentials
        ↓
API Server authenticates user
        ↓
API Server checks permissions
        ↓
If allowed → response returned
```

---

# PHASE 2 — SETUP REAL PRACTICE ENVIRONMENT

# Install Tools

## Install Kind

Official website:

urlKind[https://kind.sigs.k8s.io/](https://kind.sigs.k8s.io/)

## Install kubectl

Official docs:

urlkubectl[https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

## Install OpenSSL

Used for:

* generating certificates
* creating users
* signing CSRs

Check:

```bash
openssl version
```

---

# Create Kind Cluster

```bash
kind create cluster --name auth-lab
```

Check:

```bash
kubectl cluster-info
kubectl get nodes
```

---

# PHASE 3 — AUTHENTICATION BASICS

# What is Authentication?

Authentication answers:

```text
WHO ARE YOU?
```

Kubernetes supports:

* Client Certificates
* Bearer Tokens
* Service Accounts
* OpenID Connect (OIDC)
* Webhook
* X509 Certificates

In real companies:

* OIDC is very common
* ServiceAccounts are heavily used
* RBAC is standard

---

# LAB 1 — Understand Current Authentication

Run:

```bash
kubectl config view
```

Observe:

* cluster
* user
* context
* certificate-authority-data
* client-certificate-data
* client-key-data

Theory:
Your kubectl uses certificates stored in kubeconfig.

---

# LAB 2 — Check Current User

```bash
kubectl auth whoami
```

You will see:

```text
ATTRIBUTE   VALUE
Username    kubernetes-admin
Groups      system:masters
```

Meaning:
You are cluster admin.

---

# PHASE 4 — AUTHORIZATION BASICS

# What is Authorization?

Authorization answers:

```text
WHAT ARE YOU ALLOWED TO DO?
```

Kubernetes checks:

* verbs
* resources
* namespaces
* API groups

---

# Common Verbs

| Verb   | Meaning           |
| ------ | ----------------- |
| get    | read one resource |
| list   | list resources    |
| watch  | monitor changes   |
| create | create resource   |
| update | modify resource   |
| patch  | partial update    |
| delete | delete resource   |

---

# PHASE 5 — RBAC

# What is RBAC?

RBAC = Role Based Access Control

Industry standard authorization method.

Main objects:

| Object             | Scope                |
| ------------------ | -------------------- |
| Role               | Namespace            |
| ClusterRole        | Cluster-wide         |
| RoleBinding        | Namespace binding    |
| ClusterRoleBinding | Cluster-wide binding |

---

# LAB 3 — Create Namespace

```bash
kubectl create namespace dev-team
```

---

# LAB 4 — Create Role

Create file:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev-team
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```

Apply:

```bash
kubectl apply -f role.yaml
```

---

# Understanding the YAML

```yaml
apiGroups: [""]
```

Means core API group.

Examples in core group:

* pods
* services
* configmaps

---

# LAB 5 — Create User Using Certificates

Create private key:

```bash
openssl genrsa -out dev-user.key 2048
```

Create CSR:

```bash
openssl req -new -key dev-user.key -out dev-user.csr -subj "/CN=dev-user/O=developers"
```

Meaning:

| Field | Meaning  |
| ----- | -------- |
| CN    | username |
| O     | group    |

So:

```text
username = dev-user
group = developers
```

---

# IMPORTANT REAL-WORLD CONCEPT

Kubernetes does NOT store users internally.

It trusts:

* certificates
* OIDC
* external identity systems

This is very important for interviews.

---

# PHASE 6 — CSR SIGNING INSIDE KUBERNETES

# LAB 6 — Create Kubernetes CSR Object

Base64 encode CSR:

```bash
cat dev-user.csr | base64 | tr -d '\n'
```

Create YAML:

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: dev-user
spec:
  request: BASE64_CSR
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
```

Apply:

```bash
kubectl apply -f csr.yaml
```

Check:

```bash
kubectl get csr
```

Approve:

```bash
kubectl certificate approve dev-user
```

---

# LAB 7 — Extract Certificate

```bash
kubectl get csr dev-user -o jsonpath='{.status.certificate}' | base64 -d > dev-user.crt
```

Now you have:

* dev-user.key
* dev-user.crt

---

# PHASE 7 — CREATE NEW KUBECONFIG USER

# LAB 8 — Add User to kubeconfig

Get cluster name:

```bash
kubectl config get-clusters
```

Add credentials:

```bash
kubectl config set-credentials dev-user \
--client-certificate=dev-user.crt \
--client-key=dev-user.key
```

Create context:

```bash
kubectl config set-context dev-user-context \
--cluster=kind-auth-lab \
--user=dev-user \
--namespace=dev-team
```

Switch context:

```bash
kubectl config use-context dev-user-context
```

Test:

```bash
kubectl get pods
```

Expected:

```text
Error from server (Forbidden)
```

WHY?

Authenticated ✅
Authorized ❌

This is the most important learning moment.

---

# PHASE 8 — ROLEBINDING

# LAB 9 — Bind Role

Switch back to admin:

```bash
kubectl config use-context kind-auth-lab
```

Create RoleBinding:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: dev-user-binding
  namespace: dev-team
subjects:
- kind: User
  name: dev-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

Apply:

```bash
kubectl apply -f rolebinding.yaml
```

Switch user:

```bash
kubectl config use-context dev-user-context
```

Test:

```bash
kubectl get pods
```

Now it works.

---

# PHASE 9 — AUTHORIZATION DEBUGGING

# LAB 10 — Check Permissions

```bash
kubectl auth can-i create deployments
```

```bash
kubectl auth can-i delete pods
```

Check another user:

```bash
kubectl auth can-i list pods \
--as=dev-user \
-n dev-team
```

This command is used heavily in industry.

---

# PHASE 10 — SERVICE ACCOUNTS

# Why ServiceAccounts?

Humans use:

* kubectl
* certificates
* OIDC

Applications inside cluster use:

👉 ServiceAccounts

Examples:

* Jenkins
* ArgoCD
* Prometheus
* GitLab Runner
* CI/CD tools

---

# LAB 11 — Create ServiceAccount

```bash
kubectl create sa backend-sa -n dev-team
```

Check:

```bash
kubectl get sa -n dev-team
```

Describe:

```bash
kubectl describe sa backend-sa -n dev-team
```

---

# LAB 12 — Use ServiceAccount in Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: dev-team
spec:
  serviceAccountName: backend-sa
  containers:
  - name: nginx
    image: nginx
```

Apply:

```bash
kubectl apply -f pod.yaml
```

---

# IMPORTANT REAL-WORLD CONCEPT

Pods authenticate using:

```text
Mounted ServiceAccount token
```

Inside pod:

```bash
/var/run/secrets/kubernetes.io/serviceaccount
```

Contains:

* token
* ca.crt
* namespace

---

# PHASE 11 — CLUSTERROLE

# LAB 13 — Create ClusterRole

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pod-reader-cluster
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```

---

# Difference

| Role           | ClusterRole    |
| -------------- | -------------- |
| Namespace only | Entire cluster |
| Limited scope  | Global scope   |

---

# PHASE 12 — ADVANCED RBAC

# Important Topics

You must practice:

## 1. Aggregated ClusterRoles

Used internally by Kubernetes.

## 2. Impersonation

```bash
kubectl auth can-i list pods --as=user1
```

## 3. Group-based access

```yaml
subjects:
- kind: Group
  name: developers
```

## 4. Least privilege principle

Very important in production.

## 5. Wildcards dangers

Avoid:

```yaml
verbs: ["*"]
resources: ["*"]
```

---

# PHASE 13 — REAL-WORLD SCENARIOS

# Scenario 1

Create:

* namespace for frontend team
* read-only access
* deployment creation access
* deny secret access

---

# Scenario 2

Create CI/CD ServiceAccount with:

* deployment permissions
* namespace restriction

---

# Scenario 3

Developer should:

* view pods
* logs
* services
* but cannot delete anything

---

# PHASE 14 — OIDC AUTHENTICATION

# Real Industry Standard

Most companies use:

* Okta
* Azure AD
* Google
* Keycloak
* Dex

Authentication flow:

```text
User → Identity Provider → Kubernetes API Server
```

Concepts:

* JWT
* ID Token
* Refresh Token
* Claims
* Groups

---

# ADVANCED TOPICS

You should eventually learn:

* kubeconfig internals
* X509 certificates
* TLS bootstrapping
* Admission Controllers
* OPA Gatekeeper
* Kyverno
* Pod Security Admission
* Bound ServiceAccount Tokens
* SPIFFE/SPIRE
* IAM Roles for Service Accounts (IRSA)
* EKS Authentication
* GKE Workload Identity

---

# PHASE 15 — TROUBLESHOOTING

# Common Errors

## Forbidden

```text
Error from server (Forbidden)
```

Means:

✅ Authenticated
❌ Not authorized

---

## Unauthorized

```text
You must be logged in to the server
```

Means:

❌ Authentication failed

---

# Debug Commands

```bash
kubectl auth can-i --list
```

```bash
kubectl describe role
```

```bash
kubectl describe rolebinding
```

```bash
kubectl get events
```

---

# INTERVIEW QUESTIONS YOU MUST MASTER

## Beginner

1. Difference between authentication and authorization?
2. What is RBAC?
3. Difference between Role and ClusterRole?
4. Difference between RoleBinding and ClusterRoleBinding?
5. What is ServiceAccount?

---

## Intermediate

1. How does kubectl authenticate?
2. How does kube-apiserver authorize requests?
3. How do pods talk to API server?
4. What is least privilege access?
5. How to debug Forbidden errors?

---

## Advanced

1. Explain Kubernetes request flow.
2. Explain OIDC authentication.
3. Explain ServiceAccount token projection.
4. How does EKS authentication work?
5. Explain admission controllers.

---

# PRACTICE PLAN

## Week 1

* Kubernetes request flow
* Authentication basics
* kubeconfig
* Certificates

## Week 2

* RBAC
* Role
* ClusterRole
* RoleBinding
* ClusterRoleBinding

## Week 3

* ServiceAccounts
* Real-world scenarios
* Troubleshooting
* can-i command

## Week 4

* OIDC
* Advanced security
* Admission controllers
* Production patterns

---

# HOW WE WILL CONTINUE

We will learn like this:

1. Theory
2. Real-world analogy
3. YAML breakdown
4. Hands-on practical
5. Troubleshooting
6. Interview questions
7. Mini assignment

---

# NEXT STEP

Start with:

👉 Kubernetes Request Flow + Authentication Basics

You should first create the Kind cluster and verify kubectl connectivity.

Commands:

```bash
kind create cluster --name auth-lab
```

```bash
kubectl cluster-info
```

```bash
kubectl get nodes
```

Then we will deeply understand:

```text
kubectl → kubeconfig → API Server → Authentication → Authorization
```

That is the foundation of everything.
