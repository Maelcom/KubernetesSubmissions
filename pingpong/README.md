## Pingpong app
Responds to HTTP GET `/pingpong` with "pong `count`" where `count` is the counter of accepted requests.
Responds to HTTP GET `/pings` with raw `count` without incrementing the counter.

Defines shared Ingress for both itself and `log_output` app.

### Create k3d cluster with port forward from host to loadbalancer
```
k3d cluster create -p 8081:80@loadbalancer --agents 2
kubectl apply -f shared_storage/manifests
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
```

### Deploy to existing k3d cluster
```
kubectl apply -f log_output/manifests
kubectl apply -f pingpong/manifests
kubectl logs -f deployments/pingpong-dep
```

### Access app
```
# instead of port-forward or NodePort we now use Ingress Service
curl http://localhost:8081/pingpong
curl http://localhost:8081/pings
```
