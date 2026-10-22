#!/bin/bash

kubectl create namespace minio-ns
kubectl apply -f minio/minio-raw-deployment.yaml -n minio-ns
kubectl apply -f minio/minio-external-service.yaml
