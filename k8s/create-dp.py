# script per creazione di un deployment
# Usage: python create-dp.py <deployment-name> <image> <replicas> <namespace>
# Example: python create-dp.py my-deployment nginx 3 default

# Importing the Kubernetes client and config to interact with the Kubernetes API
from kubernetes import client, config

def create_dp(dp_name, image, replicas, namespace):
    config.load_kube_config()
    api_instance = client.AppsV1Api()

    container = client.V1Container(name=dp_name, image=image)
    template = client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={"app": dp_name}), spec=client.V1PodSpec(containers=[container]))
    selector = client.V1LabelSelector(match_labels={"app": dp_name})
    spec = client.V1DeploymentSpec(replicas=replicas, template=template, selector=selector)
    deployment = client.V1Deployment(metadata=client.V1ObjectMeta(name=dp_name), spec=spec)

    api_instance.create_namespaced_deployment(namespace=namespace, body=deployment)
    print("Deployment created")

dp_name = input("Enter the deployment name: ")
image = input("Enter the image: ")          
replicas = int(input("Enter the number of replicas: "))
ns = input("Enter the namespace: ")

create_dp(dp_name, image, replicas, ns)