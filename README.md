
# superapp

This is a simple API built in python/flask/mysql-sqlalchemy. The microservice is containerized and converted into helmcharts. A docker build and compose file is available for local testing. The terraform code (tested) spins up a GKE cluster, it utilizes terraform workspaces to maintain 3 environments prod/dev/stg. The monitoring is setup via helmcharts on the GKE cluster too. Sample CPU/Memory alerts are setup on GRAFANA. A simple jenkins pipeline is setup to pull code from github, build docker image and push it to google container registry and also deploy application via helm.

**Table of Contents**
 - [superapp]
  - [customers_api]
    - [environment]
    - [docker]
  - [kubernetes]
    - [secrets]
    - [environment]
    - [helmcharts]
  - [monitoring]
  - [terraform]
    - [workspaces]
    - [backend]
    - [tfvars]
  - [jenkins]
    - [pipeline]
## customers_api
### environment
The environment must be provided at run-time. 

#### customers_api container

DB_PORT=<br>
DB_NAME=<br>
DB_HOST=<br>
MYSQL_DATABASE=<br>
MYSQL_USER=<br>
MYSQL_PASSWORD=<br>
MYSQL_ROOT_PASSWORD=<br>

#### mysql container
MYSQL_DATABASE=<br>
MYSQL_USER=<br>
MYSQL_PASSWORD=<br>
MYSQL_ROOT_PASSWORD=<br>


### docker
python:3.10-slim image is used for python. it is chosen over python:3.10 which was quite big in size and over a very small image alpine and fixing linkages and maintaining the dependencies ourselves. The tradeoff seems fine for this application.

mysql is used for mysql. It doesn't require building or running any other sql script apart from inbuilt scripts that come prepackaged with the container.

#### local-run
run docker-compose up<br>
**This will bring up a multi-container environment for testing purposes.**<br>

## kubernetes
### volumes
For deploying to GKE, we changed the persistent volume to use StorageClass instead of local mountpoint.
### secrets

secret_mysql.yml <br>
```
---
apiVersion: v1
kind: Secret
metadata:
  name: mysql-secrets
type: Opaque
stringData:
  db_root_password: 
  database: 
  username: 
  password: 
  ```
### environment
same environment as docker.

### helmcharts
Converted to helm as we realized it will be easier to install/upgrade with a CI/CD pipeline. <br>
The environment, secrets, volumes are not part of values.yaml </br>

## monitoring

used community repository <br>

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack -n prometheus

```

Forwarded ports to local and setup the alerts on local browser.

```
kubectl port-forward -n prometheus prometheus-prometheus-kube-prometheus-prometheus-0 9090
kubectl port-forward -n prometheus prometheus-grafana-cdb9d9755-fdqth 3000
kubectl get secret -n prometheus prometheus-grafana -o yaml
```

Alerts: <br>

```
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100
instance:node_cpu_utilisation:rate5m
```

## terraform

### workspaces
prod/dev/stg.
### backend
Google bucket is used for backend.
### tfvars
Authentication is done via a key file generated for a service account created that has sufficient rights to do most of the operations in terraform.<br>
A cluster is created of 1 node each in each availability zone. <br>
machine-type is chosen as e2-small.

## jenkins
### pipeline

The pipeline is simple that it runs on demand and pulls code from version control/builds image/pushes to registry and deploys to cluster. </br>
A future improvement is planned to use a trigger like a webhook to run the pipeline and scan the container for any vulnerabilities before deploying to gcr.