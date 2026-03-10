
```
User Browser
     ↓
DNS (nginx.local)
     ↓
Ingress Controller
     ↓
Ingress Rule
     ↓
Service (ClusterIP)
     ↓
kube-proxy
     ↓
Pod
     ↓
Container (NGINX)
```
