## Todo app
A minimal web app in Flask to learn k8s deployments.
Runs on the port specified by env var $PORT, default 8000.

### Recreate k3d cluster with port forward from host to agent node
```
k3d cluster create -p 8081:80@loadbalancer --agents 2
```

### Deploy to existing k3d cluster
```
kubectl apply -f manifests
kubectl logs -f deployments/todo-app-dep
```

### Access app
```
# instead of port-forward or NodePort we now use Ingress Service
curl http://localhost:8081
```
