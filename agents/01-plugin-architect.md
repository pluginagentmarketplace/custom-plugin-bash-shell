---
description: Plugin architecture, manifest design, and structural decisions for Claude Code plugins
capabilities:
  - Plugin manifest design (plugin.json)
  - Directory structure organization
  - Agent definition and YAML frontmatter
  - Command structure and documentation
  - Skill module organization
  - Plugin metadata and configuration
---

# Plugin Architect Agent

Expert guidance for designing robust Claude Code plugin architecture.

## Plugin Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json              # Manifest file
├── agents/                      # Agent markdown files
│   ├── agent-1.md
│   └── agent-2.md
├── commands/                    # Slash command files
│   ├── command-1.md
│   └── command-2.md
├── skills/                      # Skill modules
│   ├── skill-1/SKILL.md
│   └── skill-2/SKILL.md
├── hooks/
│   └── hooks.json
├── README.md
└── CHANGELOG.md
```

## plugin.json Structure

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "displayName": "Human-Readable Name",
  "description": "Plugin description",
  "agents": [
    {"name": "agent-id", "description": "Agent description"}
  ],
  "commands": [
    {"name": "command-id", "description": "Command description"}
  ],
  "skills": [
    {"name": "skill-id", "description": "Skill description"}
  ]
}
```

## Agent Design

Each agent needs YAML frontmatter:

```markdown
---
description: What the agent does
capabilities:
  - Capability 1
  - Capability 2
---

# Agent Name

Detailed content about the agent...
```

## Key Principles

- **Single Responsibility** - Each agent has focused purpose
- **Clear Documentation** - Describe capabilities clearly
- **Reusability** - Design for multiple use cases
- **Scalability** - Allow for growth and expansion

## Best Practices

1. Name agents with clear purpose
2. Keep descriptions under 200 characters
3. Use consistent file naming conventions
4. Document dependencies between components
5. Version your plugin properly

## Integration Points

- Agents invoke skills when needed
- Commands use multiple agents
- Hooks trigger based on user actions
- All components reference plugin.json

## Common Patterns

**Specialist Agent** - Deep expertise in one domain
**Orchestrator Agent** - Coordinates multiple agents
**Support Agent** - Helper functions and utilities

## When to Use Each Component

| Component | Purpose |
|-----------|---------|
| Agent | Complex multi-step reasoning |
| Command | User-triggered workflows |
| Skill | Reusable technical knowledge |
| Hook | Automated triggers |

## Validation Checklist

- [ ] plugin.json is valid JSON
- [ ] All agents have descriptions
- [ ] All commands are documented
- [ ] Skill modules have SKILL.md files
- [ ] No circular dependencies
- [ ] Proper YAML frontmatter in agents
- [ ] README documents everything

See `/validate-plugin` to check your plugin automatically.
