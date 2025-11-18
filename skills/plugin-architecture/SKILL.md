---
name: plugin-architecture
description: Claude Code plugin structure, manifest design, component organization, and architectural patterns
---

# Plugin Architecture Skill

Design robust Claude Code plugins with proper structure.

## Official Plugin Format

Claude Code plugins must follow this structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          ← Manifest (required)
├── agents/                  ← Agent markdown files
│   ├── agent-1.md
│   └── agent-2.md
├── commands/                ← Slash command files
│   ├── command-1.md
│   └── command-2.md
├── skills/                  ← Skill modules
│   ├── skill-1/SKILL.md
│   └── skill-2/SKILL.md
├── hooks/                   ← Automation config
│   └── hooks.json
├── scripts/                 ← Helper scripts
├── README.md               ← Documentation
└── CHANGELOG.md            ← Version history
```

## Plugin Manifest (plugin.json)

**Minimum Required:**

```json
{
  "name": "plugin-id",
  "version": "1.0.0",
  "displayName": "Plugin Display Name",
  "description": "Plugin description (max 200 chars)",
  "author": "Your Name",
  "license": "MIT"
}
```

**Full Example:**

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "displayName": "My Plugin",
  "description": "Does something useful",
  "author": "Your Name",
  "license": "MIT",
  "homepage": "https://github.com/user/plugin",
  "repository": {
    "type": "git",
    "url": "https://github.com/user/plugin.git"
  },
  "keywords": ["plugin", "automation", "tool"],
  "agents": [
    {
      "name": "agent-id",
      "description": "What this agent does"
    }
  ],
  "commands": [
    {
      "name": "command-id",
      "description": "What this command does"
    }
  ],
  "skills": [
    {
      "name": "skill-id",
      "description": "What this skill teaches"
    }
  ],
  "hooks": {
    "supported": ["user-prompt-submit", "command-execution"]
  },
  "minClaudeVersion": "2.0.0"
}
```

## Agent Files

**Structure with YAML Frontmatter:**

```markdown
---
description: What the agent does (max 200 chars)
capabilities:
  - Capability 1
  - Capability 2
---

# Agent Name

Detailed description and content...

## Section 1
Content here

## Section 2
More content
```

**Example Agent:**

```markdown
---
description: Expert in system design and architecture patterns
capabilities:
  - Architecture design
  - Design patterns
  - Scalability planning
---

# System Architect

This agent specializes in designing large-scale systems...
```

## Command Files

**Format:**

```markdown
# Command Title

Clear description of what the command does.

## Usage

```
/command-name [args]
```

## Examples

```
/command-name arg1 arg2
```

## Details

Detailed explanation of functionality.
```

**Example Command:**

```markdown
# Validate Plugin

Validates your plugin structure and manifest.

## Usage

```
/validate-plugin
```

## What It Checks

- plugin.json validity
- Agent files present
- Command files present
- Skill files present
```

## Skill Module Files

**Location & Structure:**

```
skills/
├── skill-1/
│   └── SKILL.md
└── skill-2/
    └── SKILL.md
```

**SKILL.md Format:**

```markdown
---
name: skill-id
description: What this skill teaches (max 200 chars)
---

# Skill Name

## Quick Start

```bash
# Quick example
code here
```

## Core Concepts

Main topics covered.

## Best Practices

Do's and don'ts.

## Resources

Links to learn more.
```

## Hooks Configuration

**hooks.json Format:**

```json
{
  "hooks": [
    {
      "event": "user-prompt-submit",
      "conditions": {
        "keywords": ["keyword1", "keyword2"]
      },
      "actions": [
        {
          "type": "suggest-command",
          "command": "/command-name"
        }
      ]
    }
  ]
}
```

## Naming Conventions

| Component | Convention | Example |
|-----------|-----------|---------|
| Plugin name | kebab-case | my-plugin-tool |
| Agent files | number + kebab-case | 01-specialist.md |
| Command names | kebab-case | /validate-plugin |
| Skill names | kebab-case | plugin-architecture |

## Component Relationships

```
Plugin (plugin.json)
├── Agents (call skills, executed)
│   └── Skills (reusable knowledge)
├── Commands (triggered by user)
│   └── Agents (orchestrate work)
└── Hooks (automate triggers)
    └── Commands/Agents (suggest/run)
```

## Size Guidelines

| Component | Size Limit | Guidelines |
|-----------|-----------|------------|
| Description | 200 chars | Clear, actionable |
| Agent file | 5KB | Focused expertise |
| Command file | 3KB | Clear instructions |
| Skill content | 10KB | Code examples |
| Manifest | 1KB | Structure only |

## Validation Rules

### plugin.json
- Valid JSON syntax ✓
- Required fields present ✓
- Semantic versioning ✓
- No circular references ✓

### Agents
- `.md` files in agents/ ✓
- YAML frontmatter present ✓
- Description < 200 chars ✓
- Content is substantive ✓

### Commands
- `.md` files in commands/ ✓
- Usage section present ✓
- Examples provided ✓
- Related agents listed ✓

### Skills
- SKILL.md in subdirectory ✓
- YAML frontmatter present ✓
- Quick start included ✓
- Code examples present ✓

## Best Practices

1. **Clear Naming** - Names describe purpose
2. **Focused Scope** - Each component has one job
3. **Reusability** - Share skills across agents
4. **Documentation** - Everything is documented
5. **Consistency** - Follow conventions
6. **Validation** - Test structure regularly
7. **Version Control** - Use semantic versioning
8. **Modularity** - Allow customization

## Common Mistakes

❌ Missing plugin.json
❌ Incomplete YAML frontmatter
❌ Agents without descriptions
❌ Commands without examples
❌ Skills without quick start
❌ Circular agent dependencies
❌ Non-standard file structure
❌ Missing README/CHANGELOG

## Antecedent Architecture

Build modular, reusable plugins:

- Agents = Deep expertise
- Commands = User interactions
- Skills = Teachable knowledge
- Hooks = Smart automation

Follow this structure and your plugin will be professional and maintainable!
