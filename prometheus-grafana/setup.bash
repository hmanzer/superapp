kubectl create namespace prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack -n prometheus
kubectl get pods -n prometheus
kubectl port-forward -n prometheus prometheus-prometheus-kube-prometheus-prometheus-0 9090
kubectl port-forward -n prometheus prometheus-grafana-cdb9d9755-fdqth 3000
kubectl get secret -n prometheus prometheus-grafana -o yaml