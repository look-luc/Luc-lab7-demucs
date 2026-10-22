#!/bin/sh

# Ensure the namespace exists first
kubectl create namespace minio-ns

# Apply MinIO using the correct filename
kubectl apply -f minio/minio-deployment.yaml
kubectl apply -f minio/minio-external-service.yaml

# Apply Redis, REST, Logs, and Worker components
kubectl apply -f redis/redis-deployment.yaml
kubectl apply -f redis/redis-service.yaml

kubectl apply -f rest/rest-deployment.yaml
kubectl apply -f rest/rest-service.yaml

kubectl apply -f logs/logs-deployment.yaml

kubectl apply -f worker/worker-deployment.yaml
