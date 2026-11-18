## Todo app
A minimal web app in Flask to learn k8s deployments.
Runs on the port specified by env var $PORT, default 8000.

### Recreate k3d cluster with port forward from host to agent node
```
k3d cluster create -p 8000:30083@agent:0 --agents 2
```

### Deploy to existing k3d cluster
```
kubectl apply -f manifests
kubectl logs -f deployments/todo-app-dep
```
### Access app
```
# instead of `kubectl port-forward` we now use a NodePort Service deployments/todo-app-dep 8000:8000
curl http://localhost:8000
```
