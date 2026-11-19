## Log output app
An example app that prints timestamp and a random hash every 5 seconds.
Also responds the same text via HTTP GET "/".

### Recreate k3d cluster with port forward from host to loadbalancer
```
k3d cluster create -p 8081:80@loadbalancer --agents 2
```

### Deploy to existing k3d cluster
```
kubectl apply -f manifests
kubectl logs -f deployments/log-output-dep
```

### Access app
```
# instead of port-forward or NodePort we now use Ingress Service
curl http://localhost:8081
```
