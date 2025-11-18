# Compare Roles

Compare learning requirements and career paths between multiple developer roles.

## Usage

```
/compare-roles [role1] [role2] [--role3] [--aspect]
```

## Examples

```
/compare-roles python javascript
/compare-roles frontend backend
/compare-roles react vue --aspect learning-curve
/compare-roles kubernetes docker terraform
/compare-roles ai-engineer data-engineer machine-learning
/compare-roles product-manager engineering-manager --aspect career-path
```

## Comparison Aspects

- `skills` - Technical skills required (default)
- `learning-curve` - Difficulty comparison
- `job-market` - Salary, demand, growth
- `career-path` - Progression and transitions
- `tools` - Frameworks, libraries, tools
- `time-to-competency` - How long to learn
- `all` - Complete comparison

## Example Comparison: React vs Vue

### Learning Curve
- **React**: Medium (40 hours fundamentals)
- **Vue**: Easy (30 hours fundamentals)
- **Winner**: Vue for rapid learning

### Job Market
- **React**: Excellent (87,000+ jobs)
- **Vue**: Good (15,000+ jobs)
- **Winner**: React for opportunities

### Ecosystem
- **React**: Huge (10,000+ packages)
- **Vue**: Moderate (2,000+ packages)
- **Winner**: React for variety

### Company Backing
- **React**: Meta (Facebook)
- **Vue**: Community
- **Winner**: React for stability

### Best For
- **React**: Startups, large apps, job seekers
- **Vue**: Small-medium apps, rapid prototyping
- **Verdict**: Choose based on job market priority

## Example Comparison: Frontend vs Backend vs Full-Stack

### Skills Required
| Aspect | Frontend | Backend | Full-Stack |
|--------|----------|---------|-----------|
| Languages | JavaScript/TypeScript | Python/Java/Node.js | All |
| Databases | Basic understanding | Advanced | Advanced |
| APIs | Consumer | Builder | Both |
| Performance | Client-side | Server-side | Both |
| Scaling | CDN, compression | Horizontal scaling | All |

### Time to Competency
- **Frontend Only**: 6-12 months
- **Backend Only**: 8-16 months
- **Full-Stack**: 12-24 months

### Job Market
- **Frontend**: 45,000+ jobs, $100k+ average
- **Backend**: 50,000+ jobs, $110k+ average
- **Full-Stack**: 25,000+ jobs, $115k+ average

### Career Paths
```
Frontend Dev → Lead Frontend Engineer → Tech Lead
Backend Dev  → Lead Backend Engineer  → Architect
Full-Stack   → Tech Lead            → Architect/Manager
```

## Example Comparison: AI Engineer vs Data Engineer vs ML Engineer

### Focus Areas
| Area | AI Engineer | Data Engineer | ML Engineer |
|------|------------|---------------|-------------|
| LLMs | Deep | Basic | Moderate |
| Data Pipelines | Basic | Deep | Moderate |
| Model Deployment | Moderate | Basic | Deep |
| MLOps | Basic | Basic | Deep |
| Engineering | Deep | Deep | Moderate |

### Tools
- **AI Engineer**: LangChain, OpenAI, Claude
- **Data Engineer**: Apache Spark, Kafka, Airflow
- **ML Engineer**: TensorFlow, PyTorch, MLflow

### Salary
- **AI Engineer**: $150k-$250k (growing rapidly)
- **Data Engineer**: $120k-$180k
- **ML Engineer**: $130k-$200k

## Transition Paths

```
Backend Developer
    ↓
Data Engineer (add data pipeline skills)
    ↓
ML Engineer (add model training/deployment)
    ↓
AI Engineer (add LLM/agent skills)
```

## Decision Matrix

To help you choose, consider:

1. **Interest** - Which problems excite you?
2. **Strengths** - Where are you naturally good?
3. **Job Market** - Where are opportunities?
4. **Salary** - What's important to you?
5. **Growth** - Which is growing fastest?
6. **Learning Path** - How hard to learn?

## Recommendation Engine

Based on your input:
- Current skills and experience
- Career goals
- Learning preferences
- Time available

We recommend the best role for you and a transition path if needed.

## Integration with Agents

This command uses all 7 agents to provide comprehensive comparisons across all technical and non-technical roles.

## Tips

- Compare 2-3 roles at a time
- Review the job market aspect—it changes
- Consider your learning style
- Talk to people in each role
- Try small projects in each area
- Use `/learning-path` after comparing
