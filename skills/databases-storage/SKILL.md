---
name: databases-storage
description: Database selection and management. Learn SQL, NoSQL design, caching strategies, and optimize data storage systems.
---

# Databases & Storage Skill

Master data storage, retrieval, and optimization.

## Quick Start

### Database Types

#### Relational (SQL)
```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

SELECT * FROM users WHERE id = 1;
```

**Best for**: Structured data, complex queries, transactions

#### Document (NoSQL)
```javascript
// MongoDB
db.users.insertOne({
  _id: ObjectId(),
  name: "Alice",
  email: "alice@example.com",
  preferences: { theme: "dark" }
});
```

**Best for**: Flexible schema, hierarchical data, scalability

#### Key-Value (Cache)
```bash
# Redis
SET user:1:name "Alice"
GET user:1:name
```

**Best for**: Fast access, caching, sessions, real-time

#### Graph
```cypher
// Neo4j
MATCH (user:User {id: 1})-[:FOLLOWS]->(friend)
RETURN friend
```

**Best for**: Relationships, recommendations, social networks

## SQL Fundamentals

### Basic Operations

```sql
-- SELECT (Read)
SELECT id, name, email FROM users WHERE age > 18;

-- INSERT (Create)
INSERT INTO users (name, email) VALUES ('Alice', 'alice@ex.com');

-- UPDATE (Modify)
UPDATE users SET email = 'newemail@ex.com' WHERE id = 1;

-- DELETE (Remove)
DELETE FROM users WHERE id = 1;
```

### Joins

```sql
-- INNER JOIN (matching records only)
SELECT users.name, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN (all users, matching orders)
SELECT users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id;
```

### Advanced Queries

```sql
-- Window Functions
SELECT
  name,
  salary,
  AVG(salary) OVER (PARTITION BY department) as avg_dept_salary
FROM employees;

-- CTEs (Common Table Expressions)
WITH high_earners AS (
  SELECT * FROM employees WHERE salary > 100000
)
SELECT * FROM high_earners;

-- Subqueries
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders WHERE amount > 1000);
```

## NoSQL Design

### Document Structure

```javascript
// User with nested data
{
  _id: ObjectId("..."),
  name: "Alice",
  email: "alice@example.com",
  posts: [
    {
      title: "My First Post",
      content: "...",
      likes: 42
    }
  ],
  metadata: {
    created_at: ISODate("2024-01-01"),
    login_count: 5
  }
}
```

### Collections Design Patterns

**One-to-Many**: Embed small arrays in document
**Many-to-Many**: Use references (IDs) between collections
**Polymorphic**: Flexible schema with type field

## Indexing & Performance

### Creating Indexes

```sql
-- Single column index
CREATE INDEX idx_email ON users(email);

-- Composite index
CREATE INDEX idx_user_date ON posts(user_id, created_at);

-- Unique index
CREATE UNIQUE INDEX idx_username ON users(username);
```

### Query Optimization

```sql
-- Bad: Full table scan
SELECT * FROM users WHERE SUBSTRING(name, 1, 1) = 'A';

-- Good: Index-friendly
SELECT * FROM users WHERE name LIKE 'A%';

-- Analyze query plan
EXPLAIN SELECT * FROM users WHERE email = 'test@ex.com';
```

### Redis Caching

```javascript
// Cache frequently accessed data
app.get('/user/:id', async (req, res) => {
  const cached = await redis.get(`user:${req.params.id}`);
  if (cached) return res.json(JSON.parse(cached));

  const user = await User.findById(req.params.id);
  await redis.setex(`user:${req.params.id}`, 3600, JSON.stringify(user));
  res.json(user);
});
```

## Database Selection Criteria

### Choose PostgreSQL if you need:
- Complex relationships
- ACID guarantees
- Advanced queries (CTEs, window functions)
- Reliability for financial/transactional systems
- JSON support with advanced querying

### Choose MongoDB if you need:
- Flexible, evolving schema
- Document-oriented data
- Horizontal scaling
- Developer-friendly queries
- Content management systems

### Choose Redis if you need:
- Millisecond response times
- Session management
- Real-time leaderboards
- Pub/sub messaging
- Rate limiting
- Cache layer

## Data Modeling Patterns

### Relational Design

```
Users
├─ id (PK)
├─ name
└─ email

Posts
├─ id (PK)
├─ user_id (FK)
├─ title
└─ content

Comments
├─ id (PK)
├─ post_id (FK)
├─ user_id (FK)
└─ content
```

### NoSQL Design

```javascript
// Embed related data
User {
  _id: 1,
  name: "Alice",
  posts: [
    { id: 1, title: "...", comments: [...] },
    { id: 2, title: "..." }
  ]
}
```

## Normalization vs Denormalization

### Normalization (SQL)
- **Pro**: Reduce redundancy, smaller storage
- **Con**: More joins needed, slower reads
- **Use**: Transactional systems, OLTP

### Denormalization (NoSQL)
- **Pro**: Fast reads, simpler queries
- **Con**: Redundant data, complex updates
- **Use**: Read-heavy systems, OLAP

## Transaction Management

```javascript
// PostgreSQL ACID transaction
await db.query('BEGIN');
try {
  await db.query('UPDATE accounts SET balance = balance - 100 WHERE id = 1');
  await db.query('UPDATE accounts SET balance = balance + 100 WHERE id = 2');
  await db.query('COMMIT');
} catch (e) {
  await db.query('ROLLBACK');
}
```

```javascript
// MongoDB session (multi-document transactions)
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Account.updateOne({_id: 1}, {$inc: {balance: -100}}, {session});
  await Account.updateOne({_id: 2}, {$inc: {balance: 100}}, {session});
  await session.commitTransaction();
} catch (e) {
  await session.abortTransaction();
}
```

## Replication & Scaling

### PostgreSQL Replication
```
Primary (read/write)
    ↓ WAL (Write-Ahead Logs)
Replicas (read-only)
```

### MongoDB Sharding
```
Shard Key: user_id
    ↓
├─ Shard 1: user_id 0-1000
├─ Shard 2: user_id 1001-2000
└─ Shard 3: user_id 2001-3000
```

## Backup & Recovery

```bash
# PostgreSQL backup
pg_dump database_name > backup.sql

# Restore from backup
psql database_name < backup.sql

# MongoDB backup
mongodump --db database_name

# Restore MongoDB
mongorestore --db database_name dump/
```

## Learning Path

### Phase 1: SQL Fundamentals (1-2 weeks)
- CRUD operations
- JOINs and queries
- Indexes and basic optimization
- Transactions

### Phase 2: Advanced SQL (2-4 weeks)
- Window functions, CTEs
- Query optimization
- Replication setup
- Backup strategies

### Phase 3: NoSQL Basics (1-2 weeks)
- Document design
- MongoDB operations
- Comparison with SQL

### Phase 4: Specialized Areas
- Data warehousing
- Distributed systems
- Performance at scale

## Tools & Resources

### PostgreSQL
- pgAdmin - Web UI
- DBeaver - SQL IDE
- Adminer - Simple interface

### MongoDB
- MongoDB Compass - GUI
- mongosh - CLI shell
- Atlas - Cloud hosting

### Redis
- redis-cli - CLI tool
- RedisInsight - GUI client
- StackExchange.Redis - .NET client

## CAP Theorem Reminder

Every distributed system chooses 2 of 3:
- **Consistency** - All nodes have same data
- **Availability** - System always responsive
- **Partition Tolerance** - Survives network splits

```
PostgreSQL (replication): CA (consistency + availability)
MongoDB (distributed): AP (availability + partition tolerance)
```

## Resources

- **PostgreSQL**: postgresql.org, PostgreSQL documentation
- **MongoDB**: mongodb.com, MongoDB University
- **SQL Practice**: SQLZoo, HackerRank SQL
- **Design**: Database Design Guru, Normalization
- **Tools**: DBeaver, DataGrip, MongoDB Compass

## Next Steps

After mastering databases:
- Learn **Data Engineering** for large-scale data
- Study **Database Administration** (DBA)
- Explore **Data Warehousing** (Snowflake, BigQuery)
- Master **Performance tuning** at scale
