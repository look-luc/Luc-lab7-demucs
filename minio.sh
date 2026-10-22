#!/bin/bash

kubectl create namespace minio-ns
<<<<<<< HEAD
kubectl apply -f minio/minio-raw-deployment.yaml -n minio-ns
=======
kubectl apply -f minio/minio-deployment.yaml
>>>>>>> 775b922 (trying to get things up and running)
kubectl apply -f minio/minio-external-service.yaml
