# DevOps Tools Guide

## Container Commands

```bash
docker build -t app .
docker run -d -p 3000:3000 app
docker-compose up -d
kubectl apply -f deployment.yaml
```

## CI/CD

| Tool | Use Case |
|------|----------|
| GitHub Actions | GitHub native |
| GitLab CI | GitLab native |
| Jenkins | Self-hosted |
| ArgoCD | GitOps |
