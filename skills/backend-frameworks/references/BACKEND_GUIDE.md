# Backend Frameworks Guide

## Framework Selection

| Framework | Language | Best For |
|-----------|----------|----------|
| Express.js | Node.js | APIs, real-time |
| FastAPI | Python | ML, async APIs |
| Spring Boot | Java | Enterprise |
| Django | Python | Full-stack |
| Go/Gin | Go | High performance |

## Express.js Patterns

```javascript
// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: err.message });
});
```

## FastAPI Patterns

```python
@app.get("/items/{id}")
async def get_item(id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_item(db, id)
```
