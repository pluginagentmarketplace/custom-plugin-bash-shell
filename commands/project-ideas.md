---
name: project-ideas
description: Bash Project Ideas
allowed-tools: Read, Glob
---

# Bash Project Ideas

Get hands-on Bash project ideas to build real scripting skills. Projects tailored to your current level and goals.

## Usage

```
/project-ideas [topic] --level [beginner|intermediate|advanced]
```

## Topics

| Topic | Example Projects |
|-------|------------------|
| `fundamentals` | Setup scripts, config managers |
| `text-processing` | Log analyzers, data parsers |
| `file-operations` | Backup systems, file organizers |
| `automation` | CI/CD pipelines, deployment scripts |
| `devops` | Monitoring tools, infrastructure scripts |
| `tools` | Custom CLI tools, utility scripts |

## Examples

```bash
/project-ideas fundamentals --level beginner
/project-ideas text-processing --level intermediate
/project-ideas automation --level advanced
/project-ideas devops
```

## Project Levels

### Beginner Projects (1-2 days)
- **System Info Script** - Display system information
- **File Backup Script** - Automated file backup
- **User Setup Script** - New user environment setup
- **Directory Cleaner** - Remove old/temp files

### Intermediate Projects (3-7 days)
- **Log Analyzer** - Parse and analyze log files
- **Git Automation** - Branch management scripts
- **Config Manager** - Application configuration
- **Database Backup** - Automated DB backups with rotation

### Advanced Projects (1-4 weeks)
- **CI/CD Pipeline** - GitHub Actions + Bash
- **Monitoring System** - Health checks and alerts
- **Deployment Tool** - Zero-downtime deployments
- **Infrastructure Manager** - Server provisioning

## For Each Project

✓ Clear requirements
✓ Learning objectives
✓ Step-by-step guide
✓ Best practices
✓ Bonus challenges
✓ Portfolio value
✓ Code examples

## Sample Project: Log Analyzer

```bash
#!/usr/bin/env bash
set -euo pipefail

# Log Analyzer - Parse Apache/Nginx logs
# Learning: grep, awk, sort, uniq

log_file="${1:-/var/log/nginx/access.log}"

echo "=== Top 10 IPs ==="
awk '{print $1}' "$log_file" | sort | uniq -c | sort -rn | head -10

echo "=== HTTP Status Codes ==="
awk '{print $9}' "$log_file" | sort | uniq -c | sort -rn

echo "=== Top Requested URLs ==="
awk '{print $7}' "$log_file" | sort | uniq -c | sort -rn | head -10
```
