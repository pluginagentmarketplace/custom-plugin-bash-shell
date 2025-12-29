#!/usr/bin/env python3
"""Detect design patterns in code."""
import re

PATTERNS = {
    "singleton": r"getInstance|_instance|__new__.*cls\._",
    "factory": r"create[A-Z]|Factory",
    "observer": r"subscribe|notify|addEventListener",
}

def detect_patterns(code: str) -> list:
    found = []
    for pattern, regex in PATTERNS.items():
        if re.search(regex, code):
            found.append(pattern)
    return found

if __name__ == "__main__":
    print(detect_patterns("getInstance()"))
