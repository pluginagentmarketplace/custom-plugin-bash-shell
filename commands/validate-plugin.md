# Validate Plugin

Validate your plugin structure, manifest, and all components for correctness and completeness.

## Usage

```
/validate-plugin [--strict] [--verbose]
```

## Examples

```
/validate-plugin
/validate-plugin --strict
/validate-plugin --verbose
```

## What It Checks

### Structure
- ✓ `.claude-plugin/` directory exists
- ✓ `plugin.json` present
- ✓ `agents/` directory with `.md` files
- ✓ `commands/` directory with `.md` files
- ✓ `skills/` directory with `SKILL.md` files
- ✓ `README.md` exists
- ✓ `CHANGELOG.md` exists

### Manifest Validation
- ✓ Valid JSON syntax
- ✓ Required fields: name, version, displayName, description
- ✓ Semantic versioning (X.Y.Z)
- ✓ Valid agent references
- ✓ Valid command references
- ✓ Valid skill references

### Agent Validation
- ✓ YAML frontmatter present
- ✓ Description field exists
- ✓ Capabilities array defined
- ✓ Content is substantive
- ✓ Consistent with manifest

### Command Validation
- ✓ Markdown file present
- ✓ Title (# Command Name)
- ✓ Usage section
- ✓ Examples provided
- ✓ Clear instructions

### Skill Validation
- ✓ SKILL.md in subdirectory
- ✓ YAML frontmatter present
- ✓ Name and description defined
- ✓ Quick start section
- ✓ Code examples included

## Flags

### --strict
Enforces stricter rules:
- No TODO/FIXME comments
- Documentation must be complete
- All examples must be tested
- Description character limits

### --verbose
Shows detailed output:
- Line numbers of issues
- Exact validation errors
- Suggestions for fixes
- Component counts

## Output Example

```
✓ Plugin Structure Valid
  agents/        (3 files)
  commands/      (4 files)
  skills/        (5 files)

✓ Manifest Valid
  name: my-plugin
  version: 1.0.0
  agents: 3 referenced
  commands: 4 referenced
  skills: 5 referenced

✓ Agents Valid
  ✓ 01-specialist.md
  ✓ 02-helper.md
  ✓ 03-coordinator.md

✓ Commands Valid
  ✓ main.md
  ✓ helper.md
  ✓ test.md
  ✓ deploy.md

✓ Skills Valid
  ✓ core-skill/SKILL.md
  ✓ advanced-skill/SKILL.md
  ✓ integration-skill/SKILL.md

✓ All Validation Passed!
```

## Common Issues

### Missing plugin.json
**Error**: `.claude-plugin/plugin.json` not found
**Fix**: Create `.claude-plugin/` and add `plugin.json`

### Invalid JSON
**Error**: JSON syntax error in plugin.json
**Fix**: Run through JSON validator, check quotes and commas

### Missing YAML Frontmatter
**Error**: Agent missing `---` frontmatter
**Fix**: Add proper YAML frontmatter to agent files

### Broken References
**Error**: plugin.json references non-existent agent
**Fix**: Ensure agent file exists or update reference

### Missing Sections
**Error**: Command missing "## Usage" section
**Fix**: Add required sections to all commands

## Fixing Issues

After validation finds issues:

1. **Check the error message** - Understand what's wrong
2. **Find the file** - Locate the problematic file
3. **Fix the issue** - Make the correction
4. **Run validation again** - Verify the fix

## Integration with Other Commands

Workflow:
- `/scaffold-plugin` → Create structure
- → `/validate-plugin` → Check structure
- → `/test-plugin` → Run tests
- → `/deploy-plugin` → Release

## Tips

- Run validation frequently during development
- Use --verbose to see detailed reports
- Use --strict before release
- Fix issues immediately
- Keep your plugin valid at all times

## Quick Fixes

```bash
# Quick manual validation
# Check JSON
python -m json.tool .claude-plugin/plugin.json

# Check file structure
ls -la agents/ commands/ skills/

# Count components
ls -1 agents/*.md | wc -l
ls -1 commands/*.md | wc -l
find skills -name "SKILL.md" | wc -l
```

Use `/validate-plugin` to ensure quality before deployment!
