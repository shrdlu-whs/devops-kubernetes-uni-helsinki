# Cloud Native Computing Foundation Projects (CNCF) Overview

### Application Definition & Image Build

   - **HELM**: Used in this course to install packages, e.g. to install Prometheus and Grafana. Used previously to create HELM charts for my own application to simplify deployment.
   - **Gradle**: Used to automate Java builds
   - **OpenAPI**: Used Swagger to document APIs

### Continuous Itegration & Delivery

  - **Argo**: Used Argo Rollouts in this course to simplify application deployment into Kubernetes, enable more sophisticated deployment strategies (canary) and analysis templates to monitor the status.
  - **AWS CodePipeline**: Used outside this course
  - **Azure Pipelines**: Used outside this course
  - **Github Actions**: Used outside this course
  - **Flagger**: Used with Linkerd for automated canary deployment and monitoring of Kubernetes resources.
  - **Flux**: Used for CI: to monitor the repo for changes and apply changes to the cluster.
  - **Gitlab**: Used as code repository for other projects
  - **Jenkins**: Used outside this course to automate deployment for a Java app into AWS EKS in another project
  - **Liquibase**: Used to manage database schema changes in another project

### Databases

  - **PostgreSQL**: Used as database for the Log Output project and the ToDo App project to store the To Dos.
  - **MongoDB**: Used as  storage for a quick prototype project
  - **MS SQL**: Used as database for other projects
  - **Redis**: Used in the previous course 'DevOps with Docker' and as cache database in a Java project
  - **Snowflake** Used outside of this course

### Streaming & Messaging

  - **NATS**: Used in the course to implement the communication with a messenger app.
  - **Azure Event Hubs** Used in projects outside this course
  - **Apache Spark**: Used as PySpark on MS Azure for Data Analytics
  - **RabbitMQ**: Used in another project for frontend/backend communication

### Scheduling & Orchestration
  - **Kubernetes**: Main focus of this course.
  - **KNative**: Used in section 5 to try out serverless computing
  - **Docker Swarm**: Used in DevOps with Docker course

### Service Mesh
  - **Istio** Used in another project as service mesh for Kubernetes
  - **Linkerd** Used in this course as a service mesh for Kubernetes

### Service Proxy
  - **nginx**: Used in this course, the Docker course as well as own projects as web server and proxy

### API Gateway
  - **Ngrok**: Used in project outside this course
  - **Traefik**: Used in this course as Ingress traffic controller since k3s uses it by default

### Cloud Native Storage
  - **Google Persistent Disk** Used in this course as cloud storage when deploying applications to GKE.

- Security & Compliance

### Container Registry
  - **Amazon ECR**: Used in other projects to store Docker containers
  - **Azure Registry**: Used in other projects to store Docker containers

### Automation & Configuration
- **AWS CloudFormation**: Used outside of this course
- **Terraform**: Used outside of this course

### Observability
  - **Prometheus**: Used in this course for monitoring and querying the state of the cluster and deployments
  - **Grafana**: Used in this course for graphical analysis and dashboard creation for the data collected by Prometheus
  - **Grafana Loki**: Log aggregation component for Grafana. Used in this course to analyse Pod log outputs
  - **Amazon CloudWatch**: Used outside this course
  - **Azure Monitor**: Used outside ths course

### Key Management
- **OAuth2 Proxy**: Used outside this course for a project



### Used indirectly in this course:
  - **OpenAPI**: Used indirectly in other applications that implement the standard, e.g. from Atlassian.
  - **etcd**: etcd is the primary datastore for Kubernetes. It is where the cluster state is kept.
  - **CNI**: Kubernetes uses Container Network Interface (CNI) specification to implement container networking and communications between pods.
  - **Flannel**: K3D uses this to implement the Kubernetes Container Network Interface (CNI)
  - **Rancher**: K3s is a lightweight Kubernetes distro by Rancher
  - **containerd**: Docker uses this under the hood to manage containers
  - **CoreDNS**: k3s uses this as the cluster DNS service
  - **fluentd**: k3s uses fluentd as logging layer to collect data
  - **envoy**: Knative kourier uses envoy proxy as Ingress implementation
  - **go**: Used e.g. in the KNative sample project
