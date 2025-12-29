#!/usr/bin/env python3
"""Docker management utilities."""
import subprocess

def docker_ps() -> list:
    result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)
    return result.stdout.strip().split("\n") if result.stdout else []

if __name__ == "__main__":
    print("Running containers:", docker_ps())
