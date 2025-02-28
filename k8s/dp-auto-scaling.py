# script to auto scaled deployment to a specific number of replicas
# Usage: python dp-auto-scaling.py <deployment-name> <replicas>
# Example: python dp-auto-scaling.py my-deployment 3

from kubernetes import client, config

def scale_dp(dp_name, replicas, namespace):
    config.load_kube_config()
    api_instance = client.AppsV1Api()   
    body = {"spec": {"replicas": replicas}}
    api_instance.patch_namespaced_deployment_scale(name=dp_name, namespace=namespace, body=body)
    print("Deployment scaled to %s replicas" % replicas)


dp_name = input("Enter the deployment name: ")
replicas = int(input("Enter the number of replicas: "))
ns = input("Enter the namespace: ")

scale_dp(dp_name, replicas, ns)