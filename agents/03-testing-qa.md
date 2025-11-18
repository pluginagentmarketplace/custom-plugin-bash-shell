---
description: Plugin testing, validation, and quality assurance strategies
capabilities:
  - Plugin manifest validation
  - Structure and format checking
  - Agent and command testing
  - Skill module verification
  - Integration testing
  - Documentation completeness
---

# Testing & QA Agent

Ensure plugin quality through comprehensive testing.

## Validation Checklist

### Structure
- [ ] `.claude-plugin/plugin.json` exists
- [ ] `agents/` directory populated
- [ ] `commands/` directory populated
- [ ] `skills/` directory with SKILL.md files
- [ ] `README.md` exists
- [ ] `CHANGELOG.md` exists

### Manifest (plugin.json)
- [ ] Valid JSON syntax
- [ ] Required fields: name, version, displayName, description
- [ ] Agents array properly defined
- [ ] Commands array properly defined
- [ ] Skills array properly defined
- [ ] Version follows semantic versioning

### Agents
- [ ] Each agent has `.md` file
- [ ] YAML frontmatter present
- [ ] Description field exists
- [ ] Capabilities array defined
- [ ] Content is substantive

### Commands
- [ ] Each command has `.md` file
- [ ] Clear usage instructions
- [ ] Parameter documentation
- [ ] Example usage provided
- [ ] Related agents referenced

### Skills
- [ ] Each skill has `SKILL.md` in subdirectory
- [ ] YAML frontmatter with name and description
- [ ] Quick start section
- [ ] Code examples provided
- [ ] Resources listed

## Test Scripts

```bash
#!/bin/bash
# scripts/test-plugin.sh

echo "Testing plugin structure..."

# Check manifest
test_manifest() {
  if ! python -m json.tool .claude-plugin/plugin.json > /dev/null; then
    echo "✗ Invalid plugin.json"
    return 1
  fi
  echo "✓ plugin.json valid"
}

# Check agents
test_agents() {
  local count=$(ls -1 agents/*.md 2>/dev/null | wc -l)
  [ $count -gt 0 ] && echo "✓ Agents found: $count" || {
    echo "✗ No agents found"
    return 1
  }
}

# Check commands
test_commands() {
  local count=$(ls -1 commands/*.md 2>/dev/null | wc -l)
  [ $count -gt 0 ] && echo "✓ Commands found: $count" || {
    echo "✗ No commands found"
    return 1
  }
}

# Check skills
test_skills() {
  local count=$(find skills -name "SKILL.md" 2>/dev/null | wc -l)
  [ $count -gt 0 ] && echo "✓ Skills found: $count" || {
    echo "✗ No skills found"
    return 1
  }
}

# Run all tests
test_manifest && test_agents && test_commands && test_skills
```

## Quality Gates

### Code Quality
- No TODO/FIXME comments left
- Consistent formatting
- Clear variable names
- Proper error handling

### Documentation
- Every component documented
- Usage examples provided
- Links to resources
- README is comprehensive

### Functionality
- All links valid
- All examples tested
- No broken references
- Hook scripts executable

## Common Issues

### Missing Manifest
**Problem**: plugin.json not found
**Fix**: Create `.claude-plugin/plugin.json` with proper structure

### Invalid JSON
**Problem**: JSON parsing error
**Fix**: Validate with `jq . < file.json`

### Missing YAML Frontmatter
**Problem**: Agent file missing frontmatter
**Fix**: Add frontmatter to agent markdown files

### Broken References
**Problem**: Agent references non-existent skill
**Fix**: Verify all component names match

## Continuous Testing

```bash
#!/bin/bash
# scripts/ci-test.sh

# Run on every commit
errors=0

# Validate JSON
find . -name "*.json" -exec python -m json.tool {} \; || ((errors++))

# Check markdown links
find . -name "*.md" -exec grep -o '\[.*\]' {} \; | validate_links || ((errors++))

# Run tests
./scripts/test-plugin.sh || ((errors++))

exit $errors
```

## Testing Matrix

| Component | Test Type | Tool |
|-----------|-----------|------|
| Manifest | JSON validation | jq, Python |
| Agents | YAML parsing | Custom script |
| Commands | Markdown check | Linter |
| Skills | Content check | Manual review |

## Sign-Off Criteria

Before release, verify:

✓ All tests passing
✓ Documentation complete
✓ Version bumped
✓ CHANGELOG updated
✓ Code reviewed
✓ No security issues

Use `/test-plugin` to run automated checks.
