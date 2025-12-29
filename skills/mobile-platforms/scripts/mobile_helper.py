#!/usr/bin/env python3
"""Mobile development helper."""
import subprocess

def flutter_build(platform: str = "apk"):
    return subprocess.run(["flutter", "build", platform])

if __name__ == "__main__":
    print("Mobile helper loaded")
