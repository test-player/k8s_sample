kubectl apply -f web-app-deployment.yaml
kubectl apply -f web-app-svc.yaml
 kubectl expose deployment web-app --type=NodePort --name=web-app-svc-outside

