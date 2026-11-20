## Log output app
Two apps in separate containers, one writes a timestamp and a random hash every 5 seconds to a file.
Another responds to HTTP GET "/", reads the file and outputs its contents.

### Recreate k3d cluster with port forward from host to loadbalancer
```
k3d cluster create -p 8081:80@loadbalancer --agents 2
```

### Deploy to existing k3d cluster
```
kubectl apply -f manifests
kubectl logs -f deployments/log-output-dep --all-containers
```

### Access app
```
# instead of port-forward or NodePort we now use Ingress Service
curl http://localhost:8081
```
