#!/usr/bin/env python3
"""Basic security checker."""
import re

def check_secrets(code: str) -> list:
    patterns = [
        (r'password\s*=\s*["\'][^"\']+["\']', "Hardcoded password"),
        (r'api[_-]?key\s*=\s*["\'][^"\']+["\']', "Hardcoded API key"),
    ]
    findings = []
    for pattern, desc in patterns:
        if re.search(pattern, code, re.I):
            findings.append(desc)
    return findings

if __name__ == "__main__":
    print(check_secrets('password = "secret123"'))
