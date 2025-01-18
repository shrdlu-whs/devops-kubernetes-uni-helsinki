#!/usr/bin/env bash
# Script to generate the required Auth token for GCS
kubectl create secret generic gcs-auth \
    --from-literal=gcs-auth-token= $(gcloud auth print-access-token)