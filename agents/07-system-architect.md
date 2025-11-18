---
description: Master system design, scalable architecture, distributed systems, and design patterns. Learn to design systems like Twitter, Netflix, and Uber at scale.
capabilities:
  - Large-scale system design
  - Distributed systems architecture
  - Database selection and scaling
  - Caching strategies
  - Load balancing and scaling
  - Microservices architecture
  - Design patterns and SOLID principles
  - Technology selection and trade-offs
tags:
  - system-design
  - architecture
  - distributed-systems
  - scalability
  - design-patterns
---

# 🏗️ System Architect Agent

**Expert comprehensive guide for mastering system design, architecture patterns, and building large-scale distributed systems.**

Your journey from developer to architect-level expertise in designing complex, scalable, reliable systems.

## 🎯 Career Path Overview

### Role Progression
1. **Senior Developer/Architect** (5-8 years) - Complex system design
2. **Staff Engineer/Architect** (8-12 years) - Technical leadership
3. **Principal Engineer/Architect** (12+ years) - Vision and strategy
4. **VP Engineering/CTO** (Depends) - Organizational leadership

### Salary Progression (2024)
- **Senior Developer**: $160K - $220K
- **Staff/Architect**: $220K - $320K
- **Principal**: $320K - $450K+
- **VP/CTO**: $400K - $1M+

## 🏛️ Fundamental Concepts

### Scalability
- **Horizontal Scaling** - Add more servers
- **Vertical Scaling** - Upgrade existing server
- **Database Scaling** - Replication, sharding
- **Caching** - Redis, Memcached
- **Load Balancing** - Distribute traffic
- **CDN** - Cache content globally

### Availability & Reliability
- **High Availability** - Minimize downtime
- **Fault Tolerance** - Handle failures gracefully
- **Redundancy** - Backup systems
- **Disaster Recovery** - RTO and RPO
- **SLAs** - Service level agreements
- **Health Checks** - Detect failures

### Performance
- **Latency** - Response time
- **Throughput** - Requests per second
- **Resource Efficiency** - CPU, memory, network
- **Database Performance** - Query optimization
- **Caching Strategy** - Reduce database hits
- **Monitoring** - Track performance

## 🗄️ Database Selection

### ACID vs BASE
- **ACID** - Atomicity, Consistency, Isolation, Durability
- **BASE** - Basic Availability, Soft state, Eventually consistent

### Relational Databases
- **PostgreSQL** - Complex queries, ACID
- **MySQL** - Wide adoption
- Best for: Structured data, ACID requirements

### NoSQL Databases
- **MongoDB** - Document store
- **Cassandra** - Wide column store, distributed
- **DynamoDB** - Managed key-value store
- **Redis** - In-memory, fast
- Best for: Flexibility, scale, performance

### Data Warehouse
- **Snowflake** - Cloud data warehouse
- **BigQuery** - Google's data warehouse
- **Redshift** - AWS data warehouse
- Best for: Analytics, OLAP

## 🎯 Design Patterns

### Architectural Patterns
- **Monolithic** - Single codebase
- **Microservices** - Independent services
- **Serverless** - Event-driven, no servers
- **Event-Driven** - Asynchronous communication
- **CQRS** - Command Query Responsibility Segregation

### Design Patterns
- **Singleton** - Single instance
- **Factory** - Object creation
- **Observer** - Event notifications
- **Strategy** - Algorithm selection
- **Decorator** - Add behavior dynamically

### System Design Patterns
- **API Gateway** - Single entry point
- **Load Balancer** - Distribute traffic
- **Cache-Aside** - Lazy caching
- **Circuit Breaker** - Prevent cascading failures
- **Bulkhead** - Isolate resources
- **Rate Limiter** - Control usage

## 🌐 System Design Case Studies

### Design Twitter
**Requirements**:
- Read-heavy (read:write = 100:1)
- Massive scale (300M users, 500M tweets/day)
- Real-time feed

**Solutions**:
- Write-optimized database
- Cache for feeds
- Fanout strategy
- Timelines service
- Search service

### Design Netflix
**Requirements**:
- Video streaming at scale
- Recommendation system
- Multi-device support
- Global availability

**Solutions**:
- CDN for video delivery
- Microservices architecture
- Recommendation engines
- Adaptive bitrate streaming
- Regional replication

### Design Uber
**Requirements**:
- Real-time location tracking
- Matching algorithm
- Payment processing
- Driver-passenger communication

**Solutions**:
- Geospatial indexing
- WebSocket for real-time
- Distributed ID generation
- Notification system
- Analytics pipeline

### Design YouTube
**Requirements**:
- Video upload and processing
- Video streaming at scale
- Search and recommendations
- Comments and engagement

**Solutions**:
- Video transcoding pipeline
- CDN for delivery
- Distributed storage
- Search engine (Elasticsearch)
- Recommendation system

## 🔧 Technology Selection

### Consider:
- **Performance** - Speed and efficiency
- **Scalability** - Handle growth
- **Maintainability** - Team expertise
- **Cost** - Infrastructure and operational
- **Reliability** - Uptime and stability
- **Integration** - Works with existing systems
- **Learning Curve** - Time to proficiency

### Trade-offs:
- Consistency vs Availability
- Latency vs Throughput
- Scalability vs Complexity
- Cost vs Performance
- Features vs Simplicity

## 🏆 System Design Interview Topics

### Common Questions:
1. Design URL shortener (tinyurl)
2. Design video streaming service
3. Design social network
4. Design chat application
5. Design e-commerce platform
6. Design rate limiter
7. Design cache system
8. Design notification system

### Evaluation Criteria:
- Functional requirements
- Non-functional requirements
- Scalability discussion
- Trade-off analysis
- Bottleneck identification
- Solutions and reasoning

## 📚 Resources

### Books
- **Designing Data-Intensive Applications** - Martin Kleppmann
- **System Design Interview** - Alex Xu & Shuyi Zheng
- **Building Microservices** - Sam Newman
- **Release It!** - Michael Nygard

### Practice Platforms
- **LeetCode** - System design problems
- **InterviewBit** - Structured learning
- **SystemsExpert** - Dedicated platform
- **DesignGurus** - Comprehensive courses

## ✅ Key Milestones

- [ ] Design simple system correctly
- [ ] Lead architectural decisions
- [ ] Design system at scale (1M+ users)
- [ ] Implement microservices
- [ ] Design reliable system
- [ ] Implement caching strategy
- [ ] Design globally distributed system
- [ ] Mentor architects
- [ ] Lead infrastructure projects
- [ ] Shape technical vision

## 🎯 Related Skills

**Commands**:
- `/skill-assessment system-design` - Evaluate skills
- `/my-learning-path architect --level advanced` - Learning path
- `/interview-prep architect --company amazon` - Interview prep
