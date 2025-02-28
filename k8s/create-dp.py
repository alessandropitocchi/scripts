# script per creazione di un deployment
# Usage: python create-dp.py <deployment-name> <image> <replicas> <namespace>
# Example: python create-dp.py my-deployment nginx 3 default

# Importing the Kubernetes client and config to interact with the Kubernetes API
from kubernetes import client, config
import sys

def create_dp(dp_name, container_image, replicas, namespace):
    config.load_kube_config()
    api_instance = client.AppsV1Api()

    container = client.V1Container(name=dp_name, image=container_image)
    template = client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={"app": dp_name}), spec=client.V1PodSpec(containers=[container]))
    selector = client.V1LabelSelector(match_labels={"app": dp_name})
    spec = client.V1DeploymentSpec(replicas=replicas, template=template, selector=selector)
    deployment = client.V1Deployment(metadata=client.V1ObjectMeta(name=dp_name), spec=spec)

    api_instance.create_namespaced_deployment(namespace=namespace, body=deployment)
    print("Deployment created")

if len(sys.argv) != 5:
    print("Usage: python create-dp.py <deployment-name> <image> <replicas> <namespace>")
    sys.exit(1)

dp_name = sys.argv[1]
container_image = sys.argv[2]
replicas = int(sys.argv[3])
namespace = sys.argv[4]

create_dp(dp_name, container_image, replicas, namespace)