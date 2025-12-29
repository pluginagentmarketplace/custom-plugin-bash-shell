# SQL Database Guide

## Index Types

| Type | Use Case |
|------|----------|
| B-Tree | Equality, range |
| Hash | Equality only |
| GIN | Arrays, JSONB |
| GiST | Full-text, geo |

## Optimization Tips

1. Use EXPLAIN ANALYZE
2. Index frequently queried columns
3. Avoid SELECT *
4. Use prepared statements
5. Partition large tables
