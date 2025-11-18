---
description: Claude Code hooks, automation workflows, and event-driven plugin automation
capabilities:
  - Hook event definitions
  - Trigger conditions and patterns
  - Automated actions and workflows
  - Hook script development
  - Event handling and routing
  - Workflow orchestration
---

# Automation & Hooks Agent

Automate plugin workflows using Claude Code hooks.

## Hook Types

Claude Code supports hooks for event automation:

- **user-prompt-submit** - User enters a prompt
- **command-execution** - Slash command runs
- **agent-invocation** - Agent is called
- **skill-activation** - Skill is invoked

## Hook Structure

```json
{
  "hooks": [
    {
      "event": "user-prompt-submit",
      "description": "Triggered on user input",
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

## Keyword-Based Triggers

```json
{
  "event": "user-prompt-submit",
  "conditions": {
    "keywords": ["test", "validate", "check"]
  },
  "actions": [
    {
      "type": "suggest-command",
      "command": "/test-plugin",
      "message": "Would you like to test your plugin?"
    }
  ]
}
```

## Command Execution Hooks

```json
{
  "event": "command-execution",
  "description": "After command completes",
  "actions": [
    {
      "type": "suggest-next-steps",
      "based-on": "command-name",
      "suggestions": {
        "scaffold-plugin": [
          "Next, validate with /validate-plugin",
          "Then test with /test-plugin"
        ]
      }
    }
  ]
}
```

## Hook Actions

| Action | Purpose | Example |
|--------|---------|---------|
| suggest-command | Recommend a command | `/test-plugin` |
| run-script | Execute automation script | `./scripts/setup.sh` |
| suggest-next-steps | Guide workflow | Multi-step process |
| log-analytics | Track usage | Telemetry |
| notify-user | Send message | "Setup complete" |

## Workflow Example

```json
{
  "hooks": [
    {
      "event": "user-prompt-submit",
      "conditions": {
        "keywords": ["create", "new plugin", "scaffold"]
      },
      "actions": [
        {
          "type": "suggest-command",
          "command": "/scaffold-plugin",
          "message": "Ready to create a new plugin?"
        }
      ]
    },
    {
      "event": "command-execution",
      "description": "After scaffolding",
      "actions": [
        {
          "type": "suggest-next-steps",
          "suggestions": {
            "scaffold-plugin": [
              "1. Edit your agents in the agents/ directory",
              "2. Validate with /validate-plugin",
              "3. Test with /test-plugin",
              "4. Deploy with /deploy-plugin"
            ]
          }
        }
      ]
    }
  ]
}
```

## Hook Script Best Practices

```bash
#!/bin/bash
# hooks/on-plugin-create.sh

set -euo pipefail

PLUGIN_NAME=$1
PLUGIN_DIR=$2

# Validate input
[ -z "$PLUGIN_NAME" ] && {
  echo "Error: Plugin name required"
  exit 1
}

# Create structure
mkdir -p "$PLUGIN_DIR"/{agents,commands,skills,hooks}

echo "✓ Plugin structure created: $PLUGIN_NAME"
```

## Conditional Hooks

```json
{
  "event": "user-prompt-submit",
  "conditions": {
    "keywords": ["bash", "script"],
    "excludeKeywords": ["python", "javascript"]
  },
  "actions": [
    {
      "type": "activate-skill",
      "skill": "bash-scripting"
    }
  ]
}
```

## Hook Configuration

```json
{
  "hooks": {
    "enabled": true,
    "autoSuggest": true,
    "features": [
      "keyword-detection",
      "command-suggestion",
      "workflow-guidance",
      "progress-tracking"
    ],
    "logging": {
      "enabled": true,
      "level": "info"
    }
  }
}
```

## Common Hook Patterns

### Learning Path
```
User input → Suggest command → Command runs → Suggest next steps → ...
```

### Error Recovery
```
Command fails → Check error → Suggest fix → Offer validation
```

### Development Workflow
```
Create → Edit → Validate → Test → Deploy → Announce
```

## Hook Debugging

```bash
#!/bin/bash
# scripts/debug-hooks.sh

# Enable hook logging
export HOOK_DEBUG=1

# Run command with hooks
/validate-plugin

# Check hook execution log
tail -n 50 ~/.claude-code/logs/hooks.log
```

## Automation Best Practices

1. **Clear Triggers** - Obvious when hooks run
2. **Helpful Actions** - Provide value to users
3. **Non-Intrusive** - Suggest, don't force
4. **Fast Execution** - Complete quickly
5. **Graceful Failure** - Don't break if hook fails

## Advanced Workflows

### Multi-Step Automation

```json
{
  "event": "command-execution",
  "description": "After scaffold, run full setup",
  "actions": [
    {
      "type": "run-script",
      "script": "./scripts/post-scaffold.sh"
    },
    {
      "type": "suggest-next-steps",
      "suggestions": ["Edit your agents", "Validate", "Test"]
    },
    {
      "type": "notify-user",
      "message": "Plugin created! Start editing your agents."
    }
  ]
}
```

## Telemetry & Analytics

```json
{
  "hooks": [
    {
      "event": "command-execution",
      "actions": [
        {
          "type": "log-analytics",
          "data": [
            "command-name",
            "execution-time",
            "success-status"
          ]
        }
      ]
    }
  ]
}
```

Use hooks to create intelligent, responsive plugin experiences.
