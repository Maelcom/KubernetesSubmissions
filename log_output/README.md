## Log output app
Two apps in separate containers, one writes a timestamp and a random hash every 5 seconds to a file.
Another responds to HTTP GET "/", reads the file and outputs its contents.

Uses shared Ingress defined in the `pingpong` app.

### Recreate k3d cluster with port forward from host to loadbalancer
```
k3d cluster create -p 8081:80@loadbalancer --agents 2
kubectl apply -f shared_storage/manifests
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
```

### Deploy to existing k3d cluster
```
kubectl apply -f log_output/manifests
kubectl apply -f pingpong/manifests
kubectl logs -f deployments/log-output-dep --all-containers
```

### Access app
```
# instead of port-forward or NodePort we now use Ingress Service
curl http://localhost:8081
```
