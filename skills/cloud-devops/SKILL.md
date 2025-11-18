---
name: cloud-devops
description: Cloud platforms and DevOps tools including AWS, Docker, Kubernetes, Terraform, and DevOps practices for deployment and infrastructure.
---

# Cloud & DevOps Skill

Master cloud infrastructure, containerization, and DevOps practices.

## Quick Start

### Cloud Computing Basics

Cloud provides:
- **On-demand computing** - Pay for what you use
- **Scalability** - Grow capacity as needed
- **Reliability** - Built-in redundancy
- **Global reach** - Deploy worldwide
- **Managed services** - Focus on applications, not infrastructure

### Three Deployment Models

| Model | When to Use | Examples |
|-------|-----------|----------|
| **IaaS** (Infrastructure) | Need flexibility | AWS EC2, Azure VMs |
| **PaaS** (Platform) | Want simplicity | Heroku, Railway |
| **SaaS** (Software) | Use applications | Salesforce, Google Workspace |

### Container Basics (Docker)

```dockerfile
# Dockerfile example
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]
```

```bash
# Build and run
docker build -t my-app .
docker run -p 3000:3000 my-app
```

### Kubernetes Orchestration

```yaml
# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: my-app:1.0
        ports:
        - containerPort: 3000
```

## Core Cloud Competencies

### AWS Services
- **EC2** - Virtual machines
- **S3** - Object storage
- **RDS** - Relational databases
- **Lambda** - Serverless functions
- **ECS/EKS** - Container orchestration
- **CloudFront** - CDN
- **Route 53** - DNS management
- **IAM** - Identity and access

### Docker & Containerization
- **Container images** - Defining applications
- **Registries** - Storing images (Docker Hub, ECR)
- **Volumes** - Persistent data
- **Networking** - Container communication
- **Compose** - Multi-container applications
- **Security** - Image scanning, least privilege

### Kubernetes
- **Pods** - Smallest deployable units
- **Services** - Networking and load balancing
- **ConfigMaps & Secrets** - Configuration management
- **StatefulSets** - Stateful applications
- **DaemonSets** - Node-level services
- **Ingress** - HTTP routing
- **RBAC** - Access control

### Infrastructure as Code (Terraform)

```hcl
# Terraform example
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "web-server"
  }
}
```

### DevOps Practices

#### CI/CD Pipelines
```yaml
# GitHub Actions example
name: CI/CD
on: [push]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install
      - run: npm test
      - run: npm run build
      - run: deploy.sh
```

#### Monitoring & Logging
- Application performance monitoring (APM)
- Centralized logging
- Metrics collection
- Alert configuration
- Incident response

#### Security
- Network security (VPCs, security groups)
- Secrets management
- Encryption (data in transit and at rest)
- DDoS protection
- Vulnerability scanning

## Learning Path

### Phase 1: Basics (2-4 weeks)
- Cloud provider fundamentals (AWS)
- Virtual machines (EC2)
- Storage (S3)
- Basic networking
- IAM and security basics

### Phase 2: Containerization (2-4 weeks)
- Docker fundamentals
- Writing Dockerfiles
- Docker Compose for local development
- Pushing to registries
- Container security

### Phase 3: Orchestration (4-8 weeks)
- Kubernetes architecture
- Deploying applications
- Services and networking
- Scaling and auto-scaling
- Storage and StatefulSets
- Security policies (RBAC, network policies)

### Phase 4: Infrastructure as Code (2-4 weeks)
- Terraform basics
- AWS resources as code
- State management
- Modules and reusability
- Best practices

### Phase 5: DevOps & CI/CD (4-8 weeks)
- Git workflows
- CI/CD pipelines
- Build automation
- Testing automation
- Deployment strategies
- Monitoring and alerting

## DevOps Workflow

```
Code Push
    ↓
GitHub Actions/Jenkins
    ↓
Build & Test
    ↓
Build Docker Image
    ↓
Push to Registry
    ↓
Deploy to Kubernetes
    ↓
Monitor & Alert
    ↓
(Log data for improvement)
```

## Cloud Provider Comparison

| Feature | AWS | Google Cloud | Azure |
|---------|-----|--------------|-------|
| Market Share | 33% | 11% | 23% |
| Services | 200+ | 100+ | 200+ |
| Pricing | Pay-as-you-go | Sustained discounts | Enterprise-friendly |
| Learning Curve | Medium | Medium | Medium |
| Job Market | Excellent | Good | Good |

## Infrastructure Patterns

### Microservices Architecture
```
  API Gateway
       ↓
    ├─ User Service
    ├─ Order Service
    ├─ Payment Service
    └─ Inventory Service

All in Kubernetes with separate databases
```

### Serverless Pattern
```
AWS Lambda functions
    ↓
Triggered by:
- API Gateway
- S3 events
- Database changes
- Scheduled events
```

### Load Balancing
```
  Load Balancer
    ↓
┌───┴───┐
v       v
Web-1  Web-2  Web-3
   ↓   ↓   ↓
    Database
```

## Best Practices

### Infrastructure
- **Infrastructure as Code** - Version control infrastructure
- **Immutable infrastructure** - Don't modify servers, replace them
- **Auto-scaling** - Scale based on demand
- **Multi-region** - Redundancy and latency
- **Disaster recovery** - Regular backups and testing

### Security
- **Least privilege** - Minimal permissions
- **Secrets management** - Don't hardcode secrets
- **Encryption** - In transit and at rest
- **Network segmentation** - VPCs and subnets
- **Audit logging** - Track all actions

### Monitoring
- **Key metrics** - CPU, memory, disk, network
- **Application metrics** - Response time, errors
- **Log aggregation** - Centralized logging
- **Alerting** - Notify on thresholds
- **Dashboards** - Visualize system health

## Essential Tools

### Container & Orchestration
- Docker, Docker Compose
- Kubernetes, Helm
- Container registries (ECR, Docker Hub)

### Infrastructure as Code
- Terraform, CloudFormation
- Ansible, Chef, Puppet

### CI/CD
- GitHub Actions, GitLab CI/CD
- Jenkins, CircleCI, Travis CI
- ArgoCD (GitOps)

### Monitoring & Logging
- Prometheus, Grafana
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Datadog, New Relic
- CloudWatch (AWS)

## Common Deployment Strategies

### Blue-Green Deployment
```
Current (Blue)    ┐
                  ├─ Load Balancer
New (Green)       ┘
Switch when ready
```

### Canary Deployment
```
Current Version    └─ 95% traffic
New Version        └─ 5% traffic
Gradually increase traffic to new version
```

### Rolling Deployment
```
V1 → Replace with V2 (1/3)
V1 → Replace with V2 (2/3)
V1 → Replace with V2 (3/3)
No downtime, gradual rollout
```

## Cost Optimization

- **Use reserved instances** - Save 30-70% vs on-demand
- **Spot instances** - Save 70-90% for fault-tolerant workloads
- **Right-sizing** - Use appropriate instance types
- **Auto-scaling** - Only run what you need
- **Managed services** - Less operational overhead
- **Cleanup** - Remove unused resources

## Resources

- **AWS**: AWS Free Tier, AWS Training, CloudAcademy
- **Kubernetes**: Kubernetes.io tutorials, Linux Academy
- **Docker**: Docker documentation, Play with Docker
- **Terraform**: Terraform.io, Gruntwork examples
- **Practice**: Deploy real applications, implement full CI/CD

## Next Steps

After mastering cloud and DevOps:
- Learn **advanced Kubernetes** (operators, CRDs)
- Master **serverless architecture** (AWS Lambda, GCP Functions)
- Study **SRE practices** (reliability, observability)
- Explore **multi-cloud strategies**
- Build **automated disaster recovery**
