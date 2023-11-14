## Kustomize

This project utilizes Kubernetes Kustomize for streamlined management and customization of Kubernetes manifests.

## Viewing Kustomize Configs - (Using kubectl kustomize integration)
```
kubectl kustomize .
kubectl kustomize overlays/dev/
kubectl kustomize overlays/prod/
```

## Applying Kustomize Configs - (Using kubectl kustomize integration)
```
kubectl apply -k .
kubectl apply -k overlays/dev/
kubectl apply -k overlays/prod/
```
Note: if you get field is immutable error, check your configuration and try deleting the resources then applying again.


## Creating Namespaces if you dont have them already
```
kubectl create namespace dev; kubectl create namespace prod;
```


## Accessing the application
```
minikube service kustom-mywebapp-v1
minikube service kustom-mywebapp-v1 -n dev
minikube service kustom-mywebapp-v1 -n prod
```

## References:
https://github.com/kubernetes-sigs/kustomize/blob/master/README.md

https://kubectl.docs.kubernetes.io/guides/config_management/offtheshelf/
