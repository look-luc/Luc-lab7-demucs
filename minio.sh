#!/bin/bash

kubectl create namespace minio-ns
 kubectl apply -f minio/minio-deployment.yaml
 kubectl apply -f minio/minio-external-service.yaml
