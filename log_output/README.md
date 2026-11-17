## Log output app
An example app that prints timestamp and a random hash every 5 seconds.
### Deploy to existing k3d cluster
```
kubectl apply -a manifests
kubectl logs -f deployments/log-output-dep
```
