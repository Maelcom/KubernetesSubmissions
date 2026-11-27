## Todo app
A minimal web app in Flask to learn k8s deployments.
Runs on the port specified by env var $PORT, default 8000.

Now with a separate backend service running in another Pod (Deployment).
Backend service serves GET and POST for `/todos`.

Network exchange between services is done with a single Ingress and two ClusterIP Services.

### Create k3d cluster with port forward from host to agent node
```
k3d cluster create -p 8081:80@loadbalancer --agents 2
kubectl apply -f shared_storage/manifests
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
```

### Build images
```
docker build -t maelcom/todo_app:2.2 -f Dockerfile .
k3d image import maelcom/todo_app:2.2
```

### Deploy to existing k3d cluster
```
kubectl apply -f manifests
kubectl logs -f deployments/todo-app-dep
kubectl logs -f deployments/todo-backend-dep
```

### Access app
```
# instead of port-forward or NodePort we now use Ingress Service
curl http://localhost:8081
```
