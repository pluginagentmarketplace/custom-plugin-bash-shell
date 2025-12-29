#!/usr/bin/env python3
"""ETL pipeline runner."""

def extract(source): return source
def transform(data): return data
def load(data, dest): print(f"Loaded to {dest}")

def run_pipeline(source, dest):
    data = extract(source)
    transformed = transform(data)
    load(transformed, dest)

if __name__ == "__main__":
    run_pipeline("source_db", "warehouse")
