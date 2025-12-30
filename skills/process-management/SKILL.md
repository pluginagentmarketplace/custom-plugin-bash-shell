---
name: process-management
description: Production-grade process management - jobs, signals, cron, systemd
sasmp_version: "1.3.0"
bonded_agent: 04-process-management
bond_type: PRIMARY_BOND
version: "2.0.0"
difficulty: intermediate
estimated_time: "5-7 hours"
---

# Process Management Skill

> Master process control, signals, scheduling, and monitoring

## Learning Objectives

After completing this skill, you will be able to:
- [ ] List and inspect running processes
- [ ] Send and handle signals properly
- [ ] Run background jobs and daemons
- [ ] Schedule tasks with cron and systemd
- [ ] Monitor system resources

## Prerequisites

- Bash basics
- Linux system fundamentals
- User permissions understanding

## Core Concepts

### 1. Process Inspection
```bash
# List processes
ps aux                      # All processes
ps -ef                      # Full format
ps --forest                 # Tree view

# Find processes
pgrep -f "pattern"          # PID by pattern
pidof nginx                 # PID by name
ps aux | grep '[n]ginx'     # Grep trick

# Resource usage
top                         # Real-time view
htop                        # Better interface
```

### 2. Signal Handling
```bash
# Send signals
kill PID                    # SIGTERM (15)
kill -9 PID                 # SIGKILL (9)
kill -HUP PID               # SIGHUP (1)
killall nginx               # By name
pkill -f "pattern"          # By pattern

# Handle signals in scripts
trap 'cleanup' EXIT
trap 'echo "Interrupted"' INT

cleanup() {
    rm -f "$TEMP_FILE"
    exit 0
}
```

### 3. Background Jobs
```bash
# Background execution
command &                   # Run in background
nohup command &             # Immune to hangup
nohup cmd > log.txt 2>&1 &  # With logging

# Job control
jobs                        # List jobs
fg %1                       # Foreground job 1
bg %1                       # Background job 1
disown                      # Detach from shell
```

### 4. Cron Scheduling
```bash
# Cron format
# ┌─── minute (0-59)
# │ ┌─── hour (0-23)
# │ │ ┌─── day of month (1-31)
# │ │ │ ┌─── month (1-12)
# │ │ │ │ ┌─── day of week (0-6)
# * * * * * command

# Examples
0 * * * *     # Every hour
*/15 * * * *  # Every 15 minutes
0 0 * * *     # Daily at midnight
0 0 * * 0     # Weekly on Sunday

# Edit crontab
crontab -e
crontab -l
```

## Common Patterns

### Daemon Pattern
```bash
start_daemon() {
    nohup ./daemon.sh >> /var/log/daemon.log 2>&1 &
    echo "$!" > /var/run/daemon.pid
    disown
}

stop_daemon() {
    if [[ -f /var/run/daemon.pid ]]; then
        kill "$(cat /var/run/daemon.pid)"
        rm /var/run/daemon.pid
    fi
}
```

### Cron with Locking
```bash
# Prevent overlapping runs
0 * * * * /usr/bin/flock -n /var/lock/job.lock /path/to/script.sh
```

### Signal Handler
```bash
#!/usr/bin/env bash
set -euo pipefail

cleanup() {
    echo "Cleaning up..."
    rm -f "$TEMP_FILE"
}

trap cleanup EXIT INT TERM

# Main logic
TEMP_FILE=$(mktemp)
# ... work with temp file
```

## Signal Reference

| Signal | Number | Default | Common Use |
|--------|--------|---------|------------|
| SIGHUP | 1 | Terminate | Reload config |
| SIGINT | 2 | Terminate | Ctrl+C |
| SIGQUIT | 3 | Core dump | Ctrl+\ |
| SIGKILL | 9 | Terminate | Force kill |
| SIGTERM | 15 | Terminate | Graceful stop |
| SIGSTOP | 19 | Stop | Pause |
| SIGCONT | 18 | Continue | Resume |

## Anti-Patterns

| Don't | Do | Why |
|-------|-----|-----|
| `kill -9` first | `kill -TERM` first | Allow cleanup |
| Kill PID 1 | Never | Crashes system |
| Cron without logs | Log all output | Debug issues |

## Practice Exercises

1. **Process Monitor**: Script to monitor a process
2. **Daemon Script**: Create a proper daemon
3. **Cron Job**: Schedule a backup job
4. **Signal Handler**: Graceful shutdown script

## Troubleshooting

### Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `No such process` | Already dead | Check with ps |
| `Operation not permitted` | Wrong owner | Use sudo |
| Cron not running | PATH issues | Use full paths |

### Debug Techniques
```bash
# Check if process exists
ps -p $PID

# Debug cron
grep CRON /var/log/syslog

# Trace process
strace -p $PID
```

## Resources

- [GNU Coreutils - Process](https://www.gnu.org/software/coreutils/manual/)
- [Crontab Guru](https://crontab.guru/)
- [systemd Timers](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)
