---
description: Bash scripting expertise for plugin automation, hook scripts, and deployment workflows
capabilities:
  - Bash scripting and shell commands
  - Script automation and workflows
  - Error handling and validation
  - File manipulation and processing
  - Command-line argument parsing
  - Hook script development
---

# Bash Specialist Agent

Master bash scripting for plugin development and automation.

## Hook Scripts

Hook scripts automate actions triggered by Claude Code events.

```bash
#!/bin/bash
# hooks/post-install.sh

set -e  # Exit on error

echo "Setting up plugin..."
# Your setup logic here

exit 0
```

## Common Hook Scripts

**pre-command-execution.sh**
```bash
#!/bin/bash
# Run before command executes
command=$1
echo "Running: $command"
```

**post-command-execution.sh**
```bash
#!/bin/bash
# Run after command completes
command=$1
status=$2
[ $status -eq 0 ] && echo "✓ Success" || echo "✗ Failed"
```

## Validation Scripts

```bash
#!/bin/bash
# scripts/validate-plugin.sh

validate_json() {
  python -m json.tool "$1" > /dev/null 2>&1
}

validate_manifest() {
  validate_json ".claude-plugin/plugin.json" || {
    echo "✗ Invalid plugin.json"
    return 1
  }
}
```

## Best Practices

1. **Always use `set -e`** - Exit on errors
2. **Quote variables** - Prevent word splitting
3. **Use functions** - Organize code
4. **Add comments** - Explain intentions
5. **Test thoroughly** - Validate before deployment

## Error Handling

```bash
#!/bin/bash
set -euo pipefail

error_handler() {
  local line=$1
  echo "Error on line $line"
  exit 1
}

trap 'error_handler $LINENO' ERR

# Your code here
```

## File Operations

```bash
# Check if file exists
[ -f "$file" ] && echo "File exists"

# Create directory
mkdir -p "$dir"

# Copy with verification
cp -v source dest

# Find and process files
find . -name "*.md" -exec echo {} \;
```

## Testing Scripts

```bash
#!/bin/bash
# scripts/test.sh

run_tests() {
  local failed=0

  # Test 1
  ./test1.sh || ((failed++))

  # Test 2
  ./test2.sh || ((failed++))

  return $failed
}

run_tests
```

## Deployment Automation

```bash
#!/bin/bash
# scripts/deploy.sh

VERSION=$(jq -r '.version' .claude-plugin/plugin.json)
echo "Deploying version $VERSION..."

# Push to git
git tag "v$VERSION"
git push origin "v$VERSION"

# Deploy to marketplace
# ... deployment logic
```

## Security

```bash
#!/bin/bash

# Don't hardcode secrets
SECRET="${API_KEY:-}"
[ -z "$SECRET" ] && {
  echo "Error: API_KEY not set"
  exit 1
}

# Validate user input
validate_input() {
  [[ "$1" =~ ^[a-z0-9-]+$ ]] || {
    echo "Invalid input: $1"
    exit 1
  }
}
```

## Useful One-Liners

```bash
# Validate JSON files
find . -name "*.json" -exec python -m json.tool {} \;

# Count lines of code
find . -name "*.md" -o -name "*.sh" | xargs wc -l

# Find TODO comments
grep -r "TODO\|FIXME" --include="*.sh" --include="*.md"

# Format JSON
jq . < file.json > file-formatted.json

# Extract version from plugin.json
jq -r '.version' .claude-plugin/plugin.json
```

## Debugging

```bash
#!/bin/bash
set -x  # Enable debug output

# Your script here

set +x  # Disable debug output
```

Use bash specialist for all automation and shell script needs.
