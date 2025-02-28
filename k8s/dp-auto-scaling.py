# script to auto scaled deployment to a specific number of replicas
# Usage: python dp-auto-scaling.py <deployment-name> <replicas>
# Example: python dp-auto-scaling.py my-deployment 3 default

import argparse
from kubernetes import client, config

def scale_dp(dp_name, replicas, namespace):
    config.load_kube_config()
    api_instance = client.AppsV1Api()   
    body = {"spec": {"replicas": replicas}}
    api_instance.patch_namespaced_deployment_scale(name=dp_name, namespace=namespace, body=body)
    print("Deployment scaled to %s replicas" % replicas)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scale a Kubernetes deployment.")
    parser.add_argument("deployment_name", type=str, help="The name of the deployment to scale.")
    parser.add_argument("replicas", type=int, help="The number of replicas to scale to.")
    parser.add_argument("namespace", type=str, help="The namespace of the deployment.")
    
    args = parser.parse_args()
    
    scale_dp(args.deployment_name, args.replicas, args.namespace)