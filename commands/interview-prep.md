---
name: interview-prep
description: Shell Scripting Interview Prep
allowed-tools: Read
---

# Shell Scripting Interview Preparation

Prepare for technical interviews focusing on Bash scripting and DevOps roles. Practice questions, coding challenges, and interview strategies.

## Usage

```
/interview-prep [topic] --role [sysadmin|devops|sre] --level [junior|mid|senior]
```

## Topics

| Topic | Description |
|-------|-------------|
| `basics` | Bash fundamentals questions |
| `text-processing` | grep, sed, awk challenges |
| `scripting` | Script writing exercises |
| `debugging` | Troubleshooting scenarios |
| `system-design` | Architecture questions |
| `behavioral` | Soft skills questions |
| `all` | Complete interview prep |

## Examples

```bash
/interview-prep basics --role devops --level junior
/interview-prep scripting --role sre --level mid
/interview-prep system-design --role devops --level senior
/interview-prep all --role sysadmin
```

## Common Interview Questions

### Bash Fundamentals
- What does `set -euo pipefail` do?
- Explain the difference between `$*` and `$@`
- How do you handle errors in Bash scripts?
- What's the difference between `[` and `[[`?

### Text Processing
- How would you extract unique IPs from a log file?
- Write a one-liner to count word frequency
- Explain the difference between grep, sed, and awk
- How do you process CSV data in Bash?

### Scripting Challenges
- Write a script to rotate log files
- Create a deployment script with rollback
- Build a monitoring script with alerts
- Implement a parallel processing script

## Interview Topics by Role

### System Administrator
- Server management scripts
- User/permission management
- Backup and recovery
- Log analysis

### DevOps Engineer
- CI/CD pipeline scripts
- Container orchestration
- Infrastructure automation
- Deployment strategies

### Site Reliability Engineer
- Monitoring and alerting
- Incident response
- Performance optimization
- Capacity planning

## Coding Challenge Example

```bash
# Challenge: Write a script that:
# 1. Finds all .log files older than 7 days
# 2. Compresses them with gzip
# 3. Moves to archive directory
# 4. Logs the operation

#!/usr/bin/env bash
set -euo pipefail

log_dir="${1:-/var/log}"
archive_dir="${2:-/var/log/archive}"
days_old="${3:-7}"

mkdir -p "$archive_dir"

find "$log_dir" -name "*.log" -type f -mtime +"$days_old" | while read -r file; do
    gzip -c "$file" > "$archive_dir/$(basename "$file").gz"
    rm "$file"
    echo "$(date '+%Y-%m-%d %H:%M:%S') Archived: $file"
done
```

## Interview Tips

✓ Always explain your thought process
✓ Ask clarifying questions
✓ Consider edge cases
✓ Mention error handling
✓ Discuss performance implications
✓ Know when to use Bash vs other tools
