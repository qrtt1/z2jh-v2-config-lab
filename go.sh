./customize.sh
kubectl -n hub scale deploy/hub --replicas 0
sleep 1
kubectl -n hub scale deploy/hub --replicas 1
kubectl -n hub rollout status deploy/hub
kubectl -n hub logs deploy/hub
