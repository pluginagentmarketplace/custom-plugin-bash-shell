#!/usr/bin/env python3
"""MongoDB helper utilities."""
from pymongo import MongoClient

def get_client(uri: str = "mongodb://localhost:27017"):
    return MongoClient(uri)

def find_one(collection, query):
    return collection.find_one(query)

if __name__ == "__main__":
    print("MongoDB helper loaded")
