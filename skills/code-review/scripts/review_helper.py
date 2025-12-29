#!/usr/bin/env python3
"""Code review helper."""

CHECKS = ["functionality", "security", "readability", "tests"]

def generate_checklist() -> list:
    return [{"item": c, "status": "pending"} for c in CHECKS]

if __name__ == "__main__":
    print(generate_checklist())
