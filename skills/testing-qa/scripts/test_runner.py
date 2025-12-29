#!/usr/bin/env python3
"""Test runner wrapper."""
import subprocess
import sys

def run_tests(framework: str = "pytest"):
    result = subprocess.run([framework, "-v"], capture_output=True, text=True)
    print(result.stdout)
    return result.returncode == 0

if __name__ == "__main__":
    success = run_tests(sys.argv[1] if len(sys.argv) > 1 else "pytest")
    sys.exit(0 if success else 1)
