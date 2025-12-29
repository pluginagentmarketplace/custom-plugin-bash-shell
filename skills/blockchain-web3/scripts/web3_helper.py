#!/usr/bin/env python3
"""Web3 helper utilities."""

def validate_address(address: str) -> bool:
    return address.startswith("0x") and len(address) == 42

if __name__ == "__main__":
    print(validate_address("0x742d35Cc6634C0532925a3b844Bc9e7595f23456"))
