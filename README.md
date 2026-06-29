# NexaOps — AI-Powered DevOps Command Center

> Enterprise-grade agentic infrastructure management platform powered by Claude AI

## What is NexaOps?

NexaOps integrates Claude AI directly into the DevOps workflow — enabling intelligent failure diagnosis, infrastructure drift detection, AI-powered pipeline reviews, and automated runbook generation.

## Tech Stack

| Layer | Tools |
|-------|-------|
| AI Engine | Claude API (Anthropic) |
| Backend | Python FastAPI |
| CI/CD | GitHub Actions |
| IaC | Terraform (AWS + Azure) |
| Container Orchestration | Kubernetes (EKS / AKS) |
| Monitoring | Prometheus + Grafana |
| Config Management | Ansible |
| Containerization | Docker |

## Core AI Capabilities

1. **Intelligent Failure Diagnosis** — Claude reads K8s events + pod logs and generates root cause analysis
2. **Infrastructure Drift Detection** — Compares live cloud state vs Terraform code
3. **AI Pipeline Review** — On every PR, Claude audits GitHub Actions YAML
4. **Runbook Generation** — Prometheus alert fires → Claude auto-generates incident runbook
5. **Deployment Checklist** — Pre-deployment AI audit before every production push

## Project Structure

\`\`\`
nexaops/
├── backend/          # FastAPI application + Claude API integration
├── frontend/         # React dashboard
├── infrastructure/   # Terraform (AWS + Azure) + Ansible
├── kubernetes/       # K8s manifests + Helm charts
├── monitoring/       # Prometheus + Grafana configs
├── .github/          # GitHub Actions CI/CD pipelines
└── docs/             # Architecture docs
\`\`\`

## Author

**Hani (Hina Naseer)** — DevOps & Cloud Engineer
