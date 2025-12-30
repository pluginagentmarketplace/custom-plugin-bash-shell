---
name: compare-roles
description: Compare Shell Scripting Roles
allowed-tools: Read
---

# Compare Shell Scripting Roles

Compare shell scripting roles side-by-side. See differences in skills, responsibilities, and career prospects.

## Usage

```
/compare-roles [role1] [role2] --aspect [all|skills|salary|tools]
```

## Roles

| Role | Primary Focus |
|------|---------------|
| `sysadmin` | System Administration |
| `devops` | DevOps Engineer |
| `sre` | Site Reliability Engineer |
| `platform` | Platform Engineer |
| `automation` | Automation Engineer |
| `security` | Security Engineer |

## Examples

```bash
/compare-roles sysadmin devops
/compare-roles devops sre
/compare-roles platform automation
/compare-roles sysadmin devops sre --aspect skills
```

## Comparison Aspects

| Aspect | Description |
|--------|-------------|
| **Bash Skills** | Required scripting proficiency |
| **Tools** | Common tools and utilities |
| **Responsibilities** | Day-to-day tasks |
| **Career Path** | Growth opportunities |
| **Salary Range** | Compensation expectations |
| **Learning Curve** | Time to proficiency |

## Role Comparison Matrix

```
┌──────────────┬────────────┬────────────┬────────────┐
│    Aspect    │  SysAdmin  │   DevOps   │    SRE     │
├──────────────┼────────────┼────────────┼────────────┤
│ Bash Level   │ Advanced   │ Advanced   │ Expert     │
│ Automation   │ Medium     │ High       │ Very High  │
│ CI/CD        │ Low        │ Very High  │ High       │
│ Monitoring   │ Medium     │ High       │ Very High  │
│ Coding       │ Scripts    │ Scripts+   │ Full Stack │
│ On-Call      │ Sometimes  │ Often      │ Always     │
└──────────────┴────────────┴────────────┴────────────┘
```

## Bash Skills by Role

### System Administrator
- Server management scripts
- User administration
- Backup and recovery
- Log management

### DevOps Engineer
- CI/CD pipeline scripts
- Infrastructure as Code
- Container orchestration
- Deployment automation

### Site Reliability Engineer
- Monitoring and alerting
- Incident response scripts
- Capacity planning
- Performance optimization

## Key Differentiators

| Factor | SysAdmin | DevOps | SRE |
|--------|----------|--------|-----|
| Focus | Operations | Delivery | Reliability |
| Metrics | Uptime | Deploy Freq | SLO/SLI |
| Scope | Servers | Pipelines | Systems |
