---
name: system-design
description: Master system design and architecture. Learn scalability, databases, caching, APIs, and building large-scale systems.
---

# System Design

## Core Concepts

### Scalability
- Horizontal vs vertical scaling
- Database scaling (replication, sharding)
- Caching layers (Redis, Memcached)
- Load balancing
- Auto-scaling groups

### Availability
- Redundancy (active-active, active-passive)
- Replication
- Disaster recovery (RTO, RPO)
- Health checks and failover
- Multi-region deployment

### Performance
- Latency vs throughput
- Network optimization
- Database optimization
- Caching strategies
- CDN usage

### Database Selection

| Use Case | Choice | Why |
|----------|--------|-----|
| Strong consistency | PostgreSQL | ACID, relational |
| Flexibility | MongoDB | Flexible schema |
| Speed | Redis | In-memory |
| Analytics | BigQuery | OLAP optimized |
| Search | ElasticSearch | Full-text search |

## Interview Topics

- Design Twitter/Instagram
- Design Uber
- Design YouTube
- Design Netflix
- Load balancing
- Caching
- Database design
