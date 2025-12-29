# NoSQL Guide

## Database Types

| Type | Example | Use Case |
|------|---------|----------|
| Document | MongoDB | Flexible schema |
| Key-Value | Redis | Caching |
| Column | Cassandra | Time series |
| Graph | Neo4j | Relationships |

## MongoDB Query
```javascript
db.users.find({ age: { $gte: 18 } })
```
