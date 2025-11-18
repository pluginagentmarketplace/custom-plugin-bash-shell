---
name: hook-automation
description: Claude Code hooks, event automation, workflow triggers, and intelligent plugin automation patterns
---

# Hook Automation Skill

Automate plugin workflows using Claude Code hooks.

## Quick Start

```json
{
  "hooks": [
    {
      "event": "user-prompt-submit",
      "conditions": {
        "keywords": ["test", "validate"]
      },
      "actions": [
        {
          "type": "suggest-command",
          "command": "/test-plugin"
        }
      ]
    }
  ]
}
```

## Hook Events

| Event | Trigger | Use Case |
|-------|---------|----------|
| user-prompt-submit | User enters prompt | Suggest relevant commands |
| command-execution | Command completes | Guide next steps |
| agent-invocation | Agent called | Provide context |
| skill-activation | Skill invoked | Offer related skills |

## Keyword-Based Triggers

```json
{
  "event": "user-prompt-submit",
  "conditions": {
    "keywords": ["deploy", "release", "publish"]
  },
  "actions": [
    {
      "type": "suggest-command",
      "command": "/deploy-plugin",
      "message": "Ready to deploy your plugin?"
    }
  ]
}
```

## Command Execution Hooks

```json
{
  "event": "command-execution",
  "description": "After any command runs",
  "actions": [
    {
      "type": "suggest-next-steps",
      "based-on": "command-type",
      "suggestions": {
        "scaffold-plugin": [
          "1. Customize your agents",
          "2. Test with /test-plugin",
          "3. Deploy with /deploy-plugin"
        ],
        "validate-plugin": [
          "Fix any errors shown",
          "Run /test-plugin",
          "Ready to deploy!"
        ]
      }
    }
  ]
}
```

## Hook Actions

### suggest-command
```json
{
  "type": "suggest-command",
  "command": "/command-name",
  "message": "Optional custom message"
}
```

### run-script
```json
{
  "type": "run-script",
  "script": "./scripts/hook-action.sh",
  "args": ["arg1", "arg2"]
}
```

### suggest-next-steps
```json
{
  "type": "suggest-next-steps",
  "suggestions": [
    "First step",
    "Second step",
    "Third step"
  ]
}
```

### activate-skill
```json
{
  "type": "activate-skill",
  "skill": "bash-scripting",
  "message": "Suggesting bash scripting skill"
}
```

## Advanced Patterns

### Workflow Chain

```json
{
  "hooks": [
    {
      "event": "user-prompt-submit",
      "conditions": {
        "keywords": ["new plugin", "create"]
      },
      "actions": [
        {
          "type": "suggest-command",
          "command": "/scaffold-plugin"
        }
      ]
    },
    {
      "event": "command-execution",
      "description": "After scaffolding",
      "actions": [
        {
          "type": "suggest-next-steps",
          "suggestions": [
            "/validate-plugin (check structure)",
            "/test-plugin (run tests)",
            "/deploy-plugin (release)"
          ]
        }
      ]
    }
  ]
}
```

### Conditional Hooks

```json
{
  "event": "user-prompt-submit",
  "conditions": {
    "keywords": ["bash", "script"],
    "excludeKeywords": ["python", "javascript"],
    "minLength": 10
  },
  "actions": [
    {
      "type": "activate-skill",
      "skill": "bash-scripting"
    }
  ]
}
```

## Hook Script Example

```bash
#!/bin/bash
# hooks/on-deploy.sh

set -e

echo "Deployment hook triggered"

# Get plugin version
VERSION=$(jq -r '.version' .claude-plugin/plugin.json)

# Verify tests pass
./scripts/test-plugin.sh || {
  echo "✗ Tests failed, aborting deployment"
  exit 1
}

# Create backup
cp -r .claude-plugin .claude-plugin.backup

echo "✓ Deployment hook completed"
```

## Configuration Template

```json
{
  "hooks": {
    "enabled": true,
    "autoSuggest": true,
    "logging": {
      "enabled": true,
      "level": "info"
    },
    "features": [
      "keyword-detection",
      "command-suggestion",
      "workflow-guidance",
      "progress-tracking"
    ]
  },
  "hooks": [
    {
      "event": "user-prompt-submit",
      "description": "Suggest commands on relevant keywords",
      "conditions": {
        "keywords": [
          "test",
          "validate",
          "check",
          "debug",
          "deploy",
          "release"
        ]
      },
      "actions": [
        {
          "type": "suggest-command",
          "command": "/test-plugin"
        }
      ]
    },
    {
      "event": "command-execution",
      "description": "Guide workflow after commands",
      "actions": [
        {
          "type": "suggest-next-steps",
          "based-on": "command-type",
          "suggestions": {
            "scaffold-plugin": [
              "Edit agents and commands",
              "Run /validate-plugin",
              "Test with /test-plugin"
            ],
            "validate-plugin": [
              "Fix any validation errors",
              "Run /test-plugin again"
            ],
            "test-plugin": [
              "All tests passed! Ready to deploy?"
            ],
            "deploy-plugin": [
              "Plugin deployed successfully!",
              "Monitor for issues"
            ]
          }
        }
      ]
    }
  ]
}
```

## Best Practices

1. **Clear Triggers** - Obvious when hooks activate
2. **Helpful Actions** - Provide real value
3. **Non-Intrusive** - Suggest, don't interrupt
4. **Fast Execution** - Complete quickly
5. **Graceful Failure** - Continue if hook fails
6. **Documentation** - Explain what each hook does
7. **Testing** - Verify hooks work correctly

## Hook Debugging

```bash
#!/bin/bash
# Enable debug logging
export HOOK_DEBUG=1

# Run command with hooks
/test-plugin

# Check hook logs
cat ~/.claude-code/logs/hooks.log
tail -f ~/.claude-code/logs/hooks.log
```

## Testing Hooks

```bash
#!/bin/bash
test_hooks() {
  echo "Testing hooks configuration..."

  # Validate JSON
  python -m json.tool hooks/hooks.json > /dev/null || {
    echo "✗ Invalid hooks.json"
    return 1
  }

  # Check events are valid
  jq -r '.hooks[].event' hooks/hooks.json | while read event; do
    case "$event" in
      user-prompt-submit|command-execution|agent-invocation|skill-activation)
        echo "✓ Valid event: $event"
        ;;
      *)
        echo "✗ Unknown event: $event"
        return 1
        ;;
    esac
  done
}
```

## Common Hook Patterns

### Learning Path
```
Input → Suggest command → Command runs → Next steps
```

### Error Recovery
```
Error → Detect problem → Suggest fix → Offer validation
```

### Development Workflow
```
Create → Validate → Test → Deploy → Announce
```

## Integration Example

```json
{
  "event": "user-prompt-submit",
  "conditions": {
    "keywords": ["how to create", "guide", "help"]
  },
  "actions": [
    {
      "type": "activate-skill",
      "skill": "plugin-architecture"
    },
    {
      "type": "suggest-command",
      "command": "/scaffold-plugin",
      "message": "Create a plugin structure?"
    }
  ]
}
```

Master hooks to create intelligent, responsive plugins!
