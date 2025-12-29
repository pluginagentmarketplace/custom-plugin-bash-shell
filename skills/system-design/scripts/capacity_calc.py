#!/usr/bin/env python3
"""Capacity calculator."""

def calculate_rps(users: int, requests_per_user: int = 10) -> float:
    daily = users * requests_per_user
    return daily / 86400

if __name__ == "__main__":
    print(f"RPS: {calculate_rps(100000):.2f}")
