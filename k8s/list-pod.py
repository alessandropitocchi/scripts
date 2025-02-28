# script per listare i pod di un namespace
# Usage: python list-pod.py <namespace>
# Example: python list-pod.py default

import sys
from kubernetes import client, config

def list_pods(ns):
    config.load_kube_config()
    api_instance = client.CoreV1Api()

    pods = api_instance.list_namespaced_pod(ns)
    for pod in pods.items:
        print(f"Pod: {pod.metadata.name} | Status: {pod.status.phase}")

if len(sys.argv) != 2:
    print("Usage: python list-pod.py <namespace>")
    sys.exit(1)

namespace = sys.argv[1]
list_pods(namespace)