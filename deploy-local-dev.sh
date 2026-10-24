#!/bin/sh
#
# Launch Redis, MinIO, and REST on Kubernetes and forward connections locally.
#

echo "1. Creating minio-ns namespace..."
kubectl create namespace minio-ns --dry-run=client -o yaml | kubectl apply -f -

echo "2. Applying MinIO deployments and services..."
kubectl apply -f minio/minio-deployment.yaml
kubectl apply -f minio/minio-external-service.yaml

echo "3. Applying Redis, REST, Logs, and Worker components..."
kubectl apply -f redis/redis-deployment.yaml
kubectl apply -f redis/redis-service.yaml

kubectl apply -f rest/rest-deployment.yaml
kubectl apply -f rest/rest-service.yaml

kubectl apply -f logs/logs-deployment.yaml
kubectl apply -f worker/worker-deployment.yaml

echo "4. Cleaning up any existing port-forward processes..."
pkill -f "kubectl port-forward" || true

echo "5. Setting up local port forwarding..."
kubectl port-forward --address 0.0.0.0 service/redis 6379:6379 &
kubectl port-forward -n minio-ns --address 0.0.0.0 service/minio-proj 9000:9000 &
kubectl port-forward -n minio-ns --address 0.0.0.0 service/minio-proj 9001:9001 &
kubectl port-forward --address 0.0.0.0 service/rest 5001:5001 &

echo "Deployment complete! All ports are now forwarded."
