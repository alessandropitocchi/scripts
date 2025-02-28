# script per listare i pod di un namespace
# Usage: python list-pod.py <namespace>
# Example: python list-pod.py default

from kubernetes import client, config

def list_pods(ns):
    config.load_kube_config()
    api_instance = client.CoreV1Api()

    pods = api_instance.list_namespaced_pod(ns)
    for pod in pods.items:
        print(f"Pod: {pod.metadata.name} | Status: {pod.status.phase}")

ns = input("Enter the namespace: ")
list_pods(ns)