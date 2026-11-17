## Todo app
A minimal web app in Flask to learn k8s deployments.
Runs on the port specified by env var $PORT, default 8000.
### Deploy to existing k3d cluster
```
kubectl apply -a manifests
kubectl logs -f deployments/todo-app-dep
```
### Access app
```
kubectl port-forward deployments/todo-app-dep 8000:8000
browse to http://localhost:8000
```
