---
name: backend-frameworks
description: Backend frameworks including Node.js, Spring Boot, Laravel, ASP.NET Core. Learn API design, database integration, and server-side development.
---

# Backend Frameworks Skill

Master server-side development and backend API creation.

## Quick Start

### Understanding Backend Development

Backend handles:
- **Business Logic** - Core application functionality
- **Database Operations** - Data storage and retrieval
- **API Endpoints** - Routes for client communication
- **Authentication & Security** - User management and protection
- **Scalability** - Handling multiple concurrent requests

### Popular Backend Frameworks

#### Node.js (JavaScript)
```javascript
// Express.js example
const express = require('express');
const app = express();

app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
});

app.post('/users', async (req, res) => {
  const user = await User.create(req.body);
  res.status(201).json(user);
});
```

#### Spring Boot (Java)
```java
// Spring Boot REST Controller
@RestController
@RequestMapping("/users")
public class UserController {
  @GetMapping("/{id}")
  public User getUser(@PathVariable Long id) {
    return userService.findById(id);
  }

  @PostMapping
  public User createUser(@RequestBody User user) {
    return userService.save(user);
  }
}
```

#### Laravel (PHP)
```php
// Laravel Route + Controller
Route::get('/users/{id}', [UserController::class, 'show']);
Route::post('/users', [UserController::class, 'store']);

public function show($id) {
  return User::find($id);
}
```

## Core Backend Competencies

### RESTful API Design
- HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Status codes (200, 201, 400, 401, 404, 500)
- Request/response formats (JSON)
- API versioning
- Rate limiting and throttling

### Database Integration
- SQL basics (SELECT, INSERT, UPDATE, DELETE)
- ORMs (Object-Relational Mapping)
- Database migrations
- Connection pooling
- Query optimization

### Authentication & Authorization
- Password hashing and storage
- JWT tokens and sessions
- OAuth2 and third-party auth
- Role-based access control (RBAC)
- API key management

### Error Handling
- Custom error responses
- Logging and monitoring
- Graceful degradation
- Error tracking services

### Middleware
- Request validation
- CORS handling
- Compression
- Caching
- Security headers

### Scalability
- Load balancing
- Database sharding
- Caching layers (Redis)
- Async processing (message queues)
- Horizontal scaling

### Testing
- Unit tests for business logic
- Integration tests for APIs
- Test databases
- Mocking and stubbing
- Coverage metrics

## Framework Comparison

### Node.js Ecosystem
**Express.js** - Minimal, flexible
```javascript
const app = express();
app.use(express.json());
```

**NestJS** - Full-featured, TypeScript
```typescript
@Controller('users')
export class UsersController {
  @Get(':id')
  findOne(@Param('id') id: string) {}
}
```

**Fastify** - High-performance
```javascript
fastify.get('/users/:id', async (request, reply) => {});
```

### Java Ecosystem
**Spring Boot** - Comprehensive, enterprise
**Quarkus** - Cloud-native, fast startup
**Play Framework** - Reactive programming

### PHP Ecosystem
**Laravel** - Modern, developer-friendly
**Symfony** - Enterprise-grade
**Slim** - Minimal microframework

### Other Languages
**Python (FastAPI, Django)** - Rapid development
**Go (Gin, Echo)** - Performance and concurrency
**Rust (Actix, Rocket)** - Safety and performance
**C# (ASP.NET Core)** - Enterprise applications

## Learning Path

### Phase 1: Fundamentals (2-4 weeks)
- Choose a framework and language
- Basic CRUD operations
- Database integration
- Simple REST API
- Request/response handling

### Phase 2: Intermediate (4-8 weeks)
- Authentication and authorization
- Error handling strategies
- Validation and middleware
- Database relationships
- Testing basics

### Phase 3: Advanced (8-12 weeks)
- Caching strategies
- Performance optimization
- Advanced database patterns
- Message queues
- Deployment and DevOps

### Phase 4: Specialization
- Microservices architecture
- Event-driven systems
- Real-time features
- GraphQL APIs
- Advanced security

## Database Integration Patterns

### Active Record
```ruby
# Rails example
@user = User.find(1)
@user.posts  # Lazy-loaded association
```

### Data Mapper
```python
# SQLAlchemy example
user = session.query(User).get(1)
posts = session.query(Post).filter_by(user_id=1).all()
```

## API Design Best Practices

### RESTful Resources
```
GET    /api/v1/users           # List all users
GET    /api/v1/users/:id       # Get specific user
POST   /api/v1/users           # Create user
PUT    /api/v1/users/:id       # Update user
DELETE /api/v1/users/:id       # Delete user
```

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      {"field": "email", "message": "Invalid format"}
    ]
  }
}
```

### Pagination
```
GET /api/v1/users?page=2&limit=10&sort=created_at:desc
```

## Technology Stack Example

```
Frontend               Backend              Database
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ React        │────▶│ Express.js   │────▶│ PostgreSQL   │
└──────────────┘     │ + Node.js    │     └──────────────┘
                     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │ Redis        │ (cache)
                     └──────────────┘
```

## Common Patterns

### Service Layer
```javascript
// Separation of concerns
class UserService {
  async getUser(id) {
    return UserRepository.findById(id);
  }

  async createUser(userData) {
    // Business logic here
    return UserRepository.save(userData);
  }
}
```

### Middleware Chain
```javascript
app.use(corsMiddleware);
app.use(authMiddleware);
app.use(validationMiddleware);
app.use(routes);
```

### Dependency Injection
```typescript
// Angular/NestJS style
@Injectable()
export class UserService {
  constructor(private database: DatabaseService) {}
}
```

## Security Essentials

- **Password Hashing** - bcrypt, Argon2
- **HTTPS** - Encrypt in transit
- **CORS** - Cross-Origin Resource Sharing
- **CSRF Protection** - Cross-Site Request Forgery
- **Rate Limiting** - Prevent abuse
- **Input Validation** - Prevent injection attacks
- **SQL Injection Prevention** - Use parameterized queries
- **XSS Prevention** - Escape user input

## Resources

- **Official Documentation**: Each framework's official docs
- **Learning**: Udemy, Pluralsight, Frontend Masters
- **Practice**: Build real projects, contribute to open source
- **Community**: GitHub issues, Stack Overflow, Discord servers

## Next Steps

After mastering backend development:
- Learn **DevOps** for deployment and scaling
- Explore **Microservices** architecture
- Study **Database optimization** and scaling
- Master **API security** and authentication
- Learn **Full-stack development** integration
