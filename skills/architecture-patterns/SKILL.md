---
name: architecture-patterns
description: System design patterns, architectural principles, and design decisions for scalable systems.
---

# Architecture & Design Patterns Skill

Master software design patterns and architectural best practices.

## Quick Start

### The Problem with Bad Architecture

```
❌ Monolith Gone Wrong:
   - Single point of failure
   - Hard to scale specific components
   - Tightly coupled code
   - Difficult to deploy
   - Slow development velocity
```

### Architectural Patterns Overview

| Pattern | Best For | Complexity |
|---------|----------|-----------|
| Monolithic | Small teams, startup | Low |
| Microservices | Large teams, complex domains | High |
| Serverless | Event-driven, variable load | Medium |
| Event-driven | Real-time, asynchronous | Medium |

## Design Principles (SOLID)

### Single Responsibility Principle (SRP)
```java
// ❌ Bad: Multiple responsibilities
class User {
  void save() { }           // Database logic
  void sendEmail() { }      // Email logic
  void validateEmail() { }  // Validation logic
}

// ✅ Good: Single responsibility
class User {
  // Just user data and business logic
}

class UserRepository {
  void save(User user) { }  // Database only
}

class UserValidator {
  void validateEmail(String email) { }  // Validation only
}
```

### Open/Closed Principle (OCP)
```python
# ❌ Bad: Must modify class for new payment types
class PaymentProcessor:
    def process(self, type, amount):
        if type == "credit_card":
            # process credit card
        elif type == "paypal":
            # process paypal

# ✅ Good: Open for extension, closed for modification
class PaymentProcessor:
    def process(self, payment_method, amount):
        return payment_method.process(amount)

class CreditCard:
    def process(self, amount): ...

class PayPal:
    def process(self, amount): ...
```

### Liskov Substitution Principle (LSP)
```typescript
// ❌ Bad: Square breaks the contract
class Rectangle {
  setWidth(w: number) { this.width = w; }
  setHeight(h: number) { this.height = h; }
  getArea() { return this.width * this.height; }
}

class Square extends Rectangle {
  setWidth(w: number) { this.width = this.height = w; }  // Breaks contract!
}

// ✅ Good: Follow the contract
interface Shape {
  getArea(): number;
}

class Rectangle implements Shape {
  constructor(width, height) { }
  getArea() { return this.width * this.height; }
}

class Square implements Shape {
  constructor(size) { }
  getArea() { return this.size * this.size; }
}
```

### Interface Segregation Principle (ISP)
```csharp
// ❌ Bad: Fat interface
interface Worker {
  void work();
  void eat();
  void sleep();
}

// ✅ Good: Segregated interfaces
interface Workable {
  void work();
}

interface Eatable {
  void eat();
}

class Robot implements Workable {
  public void work() { }
}

class Human implements Workable, Eatable {
  public void work() { }
  public void eat() { }
}
```

### Dependency Inversion Principle (DIP)
```javascript
// ❌ Bad: High-level depends on low-level
class UserService {
  constructor() {
    this.db = new PostgresDatabase();  // Concrete dependency
  }
}

// ✅ Good: Both depend on abstraction
class UserService {
  constructor(database) {  // Injected interface
    this.db = database;
  }
}

new UserService(new PostgresDatabase());
new UserService(new MongoDatabase());
```

## Creational Patterns

### Singleton (One instance globally)
```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Initialize connection
        pass

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
assert db1 is db2  # Same instance
```

### Factory (Create objects polymorphically)
```typescript
interface Transport {
  deliver(): void;
}

class Truck implements Transport {
  deliver() { console.log("Deliver by truck"); }
}

class Ship implements Transport {
  deliver() { console.log("Deliver by ship"); }
}

class LogisticsCompany {
  createTransport(type: string): Transport {
    if (type === "truck") return new Truck();
    if (type === "ship") return new Ship();
  }
}
```

### Builder (Construct complex objects)
```java
class DatabaseConfig {
  String host;
  int port;
  String database;
  String username;

  DatabaseConfig(Builder builder) {
    this.host = builder.host;
    this.port = builder.port;
    // ...
  }

  static class Builder {
    String host = "localhost";
    int port = 5432;
    String database;
    String username;

    Builder withDatabase(String db) {
      this.database = db;
      return this;
    }

    DatabaseConfig build() {
      return new DatabaseConfig(this);
    }
  }
}

// Usage
DatabaseConfig config = new Builder()
  .withDatabase("mydb")
  .build();
```

## Structural Patterns

### Adapter (Make incompatible interfaces work together)
```python
# Old interface
class LegacyPaymentSystem:
    def pay_amount(self, amount):
        pass

# New interface
class PaymentGateway:
    def process_payment(self, amount):
        pass

# Adapter
class PaymentAdapter(PaymentGateway):
    def __init__(self, legacy):
        self.legacy = legacy

    def process_payment(self, amount):
        return self.legacy.pay_amount(amount)
```

### Decorator (Add behavior dynamically)
```javascript
class Coffee {
  cost() { return 2.0; }
}

class MilkDecorator {
  constructor(coffee) {
    this.coffee = coffee;
  }

  cost() {
    return this.coffee.cost() + 0.5;  // Add milk cost
  }
}

const coffee = new MilkDecorator(new Coffee());
console.log(coffee.cost());  // 2.5
```

### Facade (Simplify complex subsystems)
```python
# Complex subsystem
class Engine:
    def start(self): pass

class Transmission:
    def change_gear(self): pass

class Lights:
    def turn_on(self): pass

# Facade
class Car:
    def __init__(self):
        self.engine = Engine()
        self.transmission = Transmission()
        self.lights = Lights()

    def start(self):
        self.engine.start()
        self.transmission.change_gear()
        self.lights.turn_on()
```

## Behavioral Patterns

### Observer (Notify multiple objects)
```typescript
class Subject {
  private observers: Observer[] = [];

  attach(observer: Observer) {
    this.observers.push(observer);
  }

  notify(data: any) {
    this.observers.forEach(obs => obs.update(data));
  }
}

interface Observer {
  update(data: any): void;
}

class Logger implements Observer {
  update(data: any) {
    console.log("Log:", data);
  }
}
```

### Strategy (Encapsulate algorithms)
```python
class PaymentStrategy:
    def pay(self, amount): pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} with credit card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} with PayPal")

class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)
```

### State (Change behavior based on state)
```java
interface OrderState {
  void process(Order order);
}

class PendingState implements OrderState {
  public void process(Order order) {
    order.setState(new ShippedState());
  }
}

class ShippedState implements OrderState {
  public void process(Order order) {
    order.setState(new DeliveredState());
  }
}
```

## Architectural Patterns

### Layered Architecture
```
┌──────────────────┐
│  Presentation    │
├──────────────────┤
│  Business Logic  │
├──────────────────┤
│  Persistence     │
├──────────────────┤
│  Database        │
└──────────────────┘
```

### Microservices Architecture
```
User Service
API Gateway ─── Product Service
Order Service

Each with own:
- Database
- Deployment
- Scaling
```

### Event-Driven Architecture
```
Event Source → Event Bus → Event Handlers

Order Created → Event Bus →
  ├─ Send Confirmation Email
  ├─ Update Inventory
  └─ Record Analytics
```

### CQRS (Command Query Responsibility Segregation)
```
Commands (writes) ──┬─→ Command Handler
                    │
                    └─→ Event Store

Queries (reads) ────→ Read Model (optimized for queries)
```

## System Design Principles

### Scalability Dimensions

**Horizontal Scaling** (more machines)
- Load balancing
- Database replication
- Stateless services

**Vertical Scaling** (bigger machine)
- Faster CPU, more RAM
- Limited by hardware
- Single point of failure

**Database Scaling**
- Read replicas
- Sharding
- NoSQL for specific use cases

### High Availability

**Redundancy**
```
Active-Active:  Server1 ←→ Server2 (both active)
Active-Passive: Server1 → Server2 (failover)
```

**Circuit Breaker Pattern**
```
Healthy → Degraded → Open (fail fast) → Half-Open → Healthy
```

### Caching Strategy

```
L1: Application cache (in-memory)
    ↓ (miss)
L2: Distributed cache (Redis)
    ↓ (miss)
L3: Database
    ↓
L4: Disk/Storage
```

## Common Architectural Mistakes

1. **Premature Optimization** - Build simple first, optimize later
2. **Over-Engineering** - Don't add complexity you don't need
3. **Tight Coupling** - Depend on abstractions, not implementations
4. **Ignoring Performance** - Measure, don't assume
5. **Poor Documentation** - Document decisions and trade-offs
6. **Not Planning Scaling** - Scalability should be built in
7. **Skipping Testing** - Architecture needs to be tested too

## Technology Selection Framework

```
Business Requirements
    ↓
Non-functional Requirements (scale, latency, availability)
    ↓
Technology Evaluation
  - Familiarity
  - Community/Support
  - Performance
  - Cost
  - Learning curve
    ↓
Prototype
    ↓
Decision
```

## Resources

- **Design Patterns**: "Gang of Four" book, Refactoring.guru
- **Architecture**: "Software Architecture in Practice" by Bass, Clements, Kazman
- **System Design**: "Designing Data-Intensive Applications" by Kleppmann
- **Practice**: Design real systems, read others' architectures

## Next Steps

After mastering patterns:
- Study **Enterprise Architecture** frameworks
- Learn **Event Sourcing & CQRS** in depth
- Explore **Domain-Driven Design** (DDD)
- Master **Distributed Systems** patterns
- Build **Large-scale systems** in practice
