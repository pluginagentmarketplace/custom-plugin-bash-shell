# Developer Roadmap Learning Plugin

A comprehensive Claude Code plugin providing guided learning paths for 69+ developer roles from [roadmap.sh](https://roadmap.sh). Master any technical career path with structured learning plans, skill assessments, and intelligent guidance.

## 🎯 What This Plugin Does

Transform your developer career journey with:

- **69+ Role Coverage** - Every role on roadmap.sh included
- **Structured Learning Paths** - Personalized 4-phase curricula
- **Skill Assessment** - Measure progress against industry standards
- **Role Comparison** - Compare career paths side-by-side
- **Intelligent Discovery** - Find roles matching your interests

## 🚀 Quick Start

### Installation

```bash
# Load from local directory
claude-code load ./developer-roadmap-learning
```

### First Commands

```bash
# Explore a specific role
/explore-roadmap python

# Get a personalized learning path
/learning-path full-stack --duration 12 --experience beginner

# Discover your ideal role
/find-role --interests web --skills javascript

# Assess your current level
/skill-assessment react --format detailed

# Compare career paths
/compare-roles frontend backend
```

## 📚 Plugin Components

### 7 Specialized Agents

1. **Programming Fundamentals** - Python, JavaScript, Java, Go, Rust, C++, PHP, Kotlin, TypeScript, Swift, Shell
2. **Web Development** - React, Vue, Angular, Frontend, Backend, Full-Stack, Next.js, CSS, HTML
3. **Mobile & Cloud** - Android, iOS, Flutter, AWS, Docker, Kubernetes, DevOps, Linux, Terraform
4. **Data Infrastructure** - SQL, MongoDB, Redis, PostgreSQL, Data Engineering, Data Analysis
5. **AI/ML Specialist** - Machine Learning, AI Engineering, Data Science, MLOps, LLMs, AI Agents
6. **Architecture & Design** - System Design, Software Architecture, Design Patterns, SOLID Principles
7. **Specialized Roles** - Blockchain, Cybersecurity, Game Development, GraphQL, Management, UX Design

### 5 Interactive Commands

- `/explore-roadmap` - Deep dive into specific roles
- `/learning-path` - Create personalized curriculum
- `/compare-roles` - Compare career paths
- `/skill-assessment` - Measure your proficiency
- `/find-role` - Discover your ideal role

### 7 Skill Modules

Practical guides with code examples for:
- Programming Languages
- Frontend Frameworks
- Backend Frameworks  
- Cloud & DevOps
- Databases & Storage
- AI/ML Tools
- Architecture Patterns

## 🎓 69 Covered Roles

**Programming Languages (11):** Python, JavaScript, Java, Go, Rust, PHP, C++, Kotlin, TypeScript, Swift UI, Shell/Bash

**Frontend & UI (7):** React, Vue, Angular, Frontend, CSS, HTML, Design Systems

**Backend & Frameworks (7):** Node.js, Spring Boot, Laravel, ASP.NET Core, Backend, Full-Stack, Next.js

**Mobile (4):** Android, iOS, Flutter, React Native

**Cloud & Infrastructure (7):** AWS, Docker, Kubernetes, DevOps, Linux, Terraform, Cloudflare

**Databases (4):** PostgreSQL, MongoDB, Redis, SQL

**Data & AI/ML (8):** AI Engineer, Machine Learning, Data Engineer, Data Scientist, MLOps, Data Analyst, AI Agents, AI Red Teaming

**Specialized (16+):** System Design, Software Architect, Blockchain, Cybersecurity, Game Developer, GraphQL, Code Review, QA, API Design, and more

**Non-Technical (5):** Product Manager, Engineering Manager, Technical Writer, UX Designer, BI Analyst

**Emerging (2):** Prompt Engineering, Git & GitHub

## 📖 Learning Path Example

Each role includes a 4-phase curriculum:

### Phase 1: Fundamentals
- Prerequisites, core concepts, learning resources

### Phase 2: Building Skills
- Technologies, hands-on projects, best practices

### Phase 3: Specialization  
- Advanced topics, real-world scenarios, patterns

### Phase 4: Mastery
- Industry standards, open source, production systems

## 💡 Example Workflows

### Learning React
```bash
/explore-roadmap react
/learning-path react --duration 12
/skill-assessment react
/compare-roles react vue --aspect job-market
```

### Career Transition
```bash
/find-role --interests automation --goals startup
/compare-roles full-stack backend
/learning-path backend --experience beginner
```

### ML Journey with Python
```bash
/find-role --skills python --interests machine-learning
/learning-path machine-learning --experience intermediate
/skill-assessment machine-learning
```

## 🔧 Plugin Structure

```
developer-roadmap-learning/
├── .claude-plugin/plugin.json
├── agents/ (7 markdown files)
├── skills/ (7 SKILL.md files)
├── commands/ (5 markdown files)
├── hooks/hooks.json
└── README.md
```

## 📊 Data Source

Built on [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap):
- 69 comprehensive roadmaps
- 224,000+ GitHub stars
- 2.1M+ active users
- MIT licensed

## 🌟 Key Features

- **Intelligent Suggestions** - Context-aware command recommendations
- **Progress Tracking** - Automated milestone tracking
- **Personalization** - Adaptive paths based on your background
- **Career Insights** - Job market data and salary ranges
- **Industry Benchmarks** - Compare against professionals at all levels
- **Real Projects** - Curated project ideas for practice

## 🚀 Getting Started

1. Load the plugin
2. Try `/explore-roadmap python` or `/find-role`
3. Create a learning path with `/learning-path [role]`
4. Track progress with `/skill-assessment`
5. Start learning!

## ❓ FAQ

**How long to learn each role?** 3-12 months depending on background and role

**Can I customize paths?** Yes, use `--duration` and `--experience` parameters

**Are projects included?** Yes, each path includes project ideas

**Can I switch roles?** Absolutely, the plugin helps you explore alternatives

**Is data current?** Yes, references roadmap.sh directly for latest information

## 📄 License

MIT License - See developer-roadmap repository

## 🎯 Quick Links

- [Official Roadmap Site](https://roadmap.sh)
- [Developer Roadmap GitHub](https://github.com/kamranahmedse/developer-roadmap)
- [Claude Code Docs](https://docs.claude.com)

---

**Happy learning! 🚀**

Transform your developer career with structured, intelligent guidance.
