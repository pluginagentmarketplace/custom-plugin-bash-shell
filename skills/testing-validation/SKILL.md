---
name: testing-validation
description: Plugin testing strategies, validation techniques, and quality assurance workflows for Claude Code plugins
---

# Testing & Validation Skill

Ensure plugin quality through comprehensive testing.

## Quick Start

```bash
#!/bin/bash
# Basic validation

# Check JSON
python -m json.tool .claude-plugin/plugin.json > /dev/null && echo "✓ Valid JSON"

# Check files exist
[ -d "agents" ] && echo "✓ Agents directory"
[ -d "commands" ] && echo "✓ Commands directory"
[ -d "skills" ] && echo "✓ Skills directory"
```

## Manifest Validation

```bash
#!/bin/bash
validate_manifest() {
  local manifest=".claude-plugin/plugin.json"

  # Check JSON syntax
  python -m json.tool "$manifest" > /dev/null || {
    echo "✗ Invalid JSON"
    return 1
  }

  # Check required fields
  jq -e '.name' "$manifest" > /dev/null || {
    echo "✗ Missing: name"
    return 1
  }

  jq -e '.version' "$manifest" > /dev/null || {
    echo "✗ Missing: version"
    return 1
  }

  echo "✓ Manifest valid"
}
```

## Structure Validation

```bash
#!/bin/bash
validate_structure() {
  local errors=0

  # Check required directories
  [ -d "agents" ] || { echo "✗ Missing: agents/"; ((errors++)); }
  [ -d "commands" ] || { echo "✗ Missing: commands/"; ((errors++)); }
  [ -d "skills" ] || { echo "✗ Missing: skills/"; ((errors++)); }

  # Check files exist
  [ -f "README.md" ] || { echo "✗ Missing: README.md"; ((errors++)); }
  [ -f "CHANGELOG.md" ] || { echo "✗ Missing: CHANGELOG.md"; ((errors++)); }

  # Count components
  local agent_count=$(ls -1 agents/*.md 2>/dev/null | wc -l)
  local cmd_count=$(ls -1 commands/*.md 2>/dev/null | wc -l)
  local skill_count=$(find skills -name "SKILL.md" 2>/dev/null | wc -l)

  echo "✓ Agents: $agent_count"
  echo "✓ Commands: $cmd_count"
  echo "✓ Skills: $skill_count"

  return $errors
}
```

## Content Validation

```bash
#!/bin/bash
validate_agents() {
  echo "Validating agents..."

  for agent in agents/*.md; do
    [ -f "$agent" ] || continue

    # Check YAML frontmatter
    grep -q "^---$" "$agent" || {
      echo "✗ $agent: Missing YAML frontmatter"
      continue
    }

    # Check description
    grep -q "^description:" "$agent" || {
      echo "✗ $agent: Missing description"
      continue
    }

    echo "✓ $(basename $agent)"
  done
}

validate_commands() {
  echo "Validating commands..."

  for cmd in commands/*.md; do
    [ -f "$cmd" ] || continue

    # Check title
    grep -q "^# " "$cmd" || {
      echo "✗ $cmd: Missing title"
      continue
    }

    # Check usage section
    grep -q "## Usage" "$cmd" || {
      echo "⚠ $cmd: Missing Usage section"
    }

    echo "✓ $(basename $cmd)"
  done
}

validate_skills() {
  echo "Validating skills..."

  for skill in skills/*/SKILL.md; do
    [ -f "$skill" ] || continue

    # Check YAML
    grep -q "^---$" "$skill" || {
      echo "✗ $skill: Missing YAML frontmatter"
      continue
    }

    # Check name
    grep -q "^name:" "$skill" || {
      echo "✗ $skill: Missing name"
      continue
    }

    echo "✓ $(basename $(dirname $skill))"
  done
}
```

## Automated Test Suite

```bash
#!/bin/bash
# scripts/test-plugin.sh

set -e

echo "Running plugin tests..."
echo "====================="

validate_manifest
validate_structure
validate_agents
validate_commands
validate_skills

echo "====================="
echo "✓ All tests passed"
```

## Link Validation

```bash
#!/bin/bash
validate_links() {
  echo "Checking links..."

  # Extract all links from markdown
  grep -rho '\[.*\](.*\.md)' --include="*.md" | while read link; do
    url=$(echo "$link" | sed 's/.*(\(.*\)).*/\1/')

    if [ -n "$url" ] && [[ ! -f "$url" ]]; then
      echo "✗ Broken link: $url"
    fi
  done
}
```

## Version Validation

```bash
#!/bin/bash
validate_version() {
  local version=$(jq -r '.version' .claude-plugin/plugin.json)

  # Check semantic versioning
  if [[ ! $version =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "✗ Invalid version format: $version"
    echo "   Use semantic versioning: MAJOR.MINOR.PATCH"
    return 1
  fi

  echo "✓ Version: $version"
}
```

## Quality Gates

```bash
#!/bin/bash
run_quality_checks() {
  local failed=0

  # No TODO/FIXME comments
  if grep -r "TODO\|FIXME" --include="*.md" --include="*.sh"; then
    echo "⚠ Found TODO/FIXME comments"
    ((failed++))
  fi

  # Consistent formatting
  # (Add your formatting checks)

  # Documentation complete
  [ -s README.md ] || { echo "✗ README is empty"; ((failed++)); }
  [ -s CHANGELOG.md ] || { echo "✗ CHANGELOG is empty"; ((failed++)); }

  return $failed
}
```

## CI/CD Integration

```yaml
name: Validate Plugin

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: |
          apt-get update && apt-get install -y jq
      - name: Run validation
        run: ./scripts/test-plugin.sh
```

## Test Checklist

- [ ] JSON files valid
- [ ] All required directories present
- [ ] All agents documented
- [ ] All commands have usage
- [ ] All skills have examples
- [ ] Links are valid
- [ ] Version is semantic
- [ ] README is complete
- [ ] CHANGELOG is updated
- [ ] No TODO comments
- [ ] Files are readable
- [ ] Examples run

## Debugging Failed Tests

```bash
#!/bin/bash
debug_test() {
  echo "Debugging: $1"

  # Show detailed error
  cat "$1"

  # Try to parse if JSON
  if [[ "$1" == *.json ]]; then
    python -m json.tool "$1"
  fi

  # Show relevant lines
  grep -n "error\|Error\|ERROR" "$1" || true
}
```

## Performance Testing

```bash
#!/bin/bash
# Test loading speed
time {
  jq . .claude-plugin/plugin.json > /dev/null
  find agents -name "*.md" | wc -l > /dev/null
  find skills -name "SKILL.md" | wc -l > /dev/null
}
```

## Test Documentation

Always document:
- What you're testing
- Why you're testing it
- How to run the test
- Expected output
- How to debug failures

Master testing to ship quality plugins!
