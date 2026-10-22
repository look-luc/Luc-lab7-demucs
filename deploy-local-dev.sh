#!/bin/sh
#
# Launch Redis and MinIO on Kubernetes with local port forwarding
#

# Ensure the namespace exists first
kubectl create namespace minio-ns

# Apply MinIO deployments and services using the correct filename
kubectl apply -f minio/minio-deployment.yaml
kubectl apply -f minio/minio-external-service.yaml

# Apply Redis, REST, Logs, and Worker components
kubectl apply -f redis/redis-deployment.yaml
kubectl apply -f redis/redis-service.yaml

kubectl apply -f rest/rest-deployment.yaml
kubectl apply -f rest/rest-service.yaml
kubectl apply -f logs/logs-deployment.yaml
kubectl apply -f worker/worker-deployment.yaml

# Port-forward Redis
kubectl port-forward --address 0.0.0.0 service/redis 6379:6379 &

# Port-forward MinIO API and Console using the correct service name (minio-proj)
kubectl port-forward -n minio-ns --address 0.0.0.0 service/minio-proj 9000:9000 &
kubectl port-forward -n minio-ns --address 0.0.0.0 service/minio-proj 9001:9001 &
