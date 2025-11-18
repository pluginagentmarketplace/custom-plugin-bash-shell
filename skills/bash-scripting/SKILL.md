---
name: bash-scripting
description: Shell scripting fundamentals, advanced bash techniques, and automation patterns for plugin development
---

# Bash Scripting Skill

Master bash for plugin automation and deployment.

## Quick Start

```bash
#!/bin/bash
set -euo pipefail

# Variables
NAME="value"
echo "Hello, $NAME"

# Functions
greet() {
  echo "Hi, $1!"
}
greet "World"

# Loops
for i in {1..5}; do
  echo "Number: $i"
done

# Conditions
if [ -f "file.txt" ]; then
  echo "File exists"
fi
```

## Essential Bash

### Variables & Strings

```bash
# Basic variables
VAR="value"
VAR=$(command)  # Command substitution

# String operations
echo "${VAR:0:5}"      # Substring
echo "${VAR//old/new}" # Replace
echo "${VAR#prefix}"   # Remove prefix
echo "${VAR%suffix}"   # Remove suffix

# Arrays
ARRAY=(one two three)
echo "${ARRAY[0]}"     # First element
echo "${ARRAY[@]}"     # All elements
```

### Control Flow

```bash
# If-else
if [ $? -eq 0 ]; then
  echo "Success"
elif [ -z "$VAR" ]; then
  echo "Empty"
else
  echo "Error"
fi

# Case statement
case "$1" in
  start) echo "Starting..." ;;
  stop)  echo "Stopping..." ;;
  *)     echo "Unknown" ;;
esac

# Loops
while IFS= read -r line; do
  echo "$line"
done < file.txt

for file in *.md; do
  echo "$file"
done
```

### Functions

```bash
# Define function
my_func() {
  local arg=$1
  echo "Argument: $arg"
  return 0
}

# Call function
my_func "value"
result=$?

# Function with defaults
with_default() {
  local param="${1:-default}"
  echo "$param"
}
```

## Advanced Patterns

### Error Handling

```bash
#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Custom error handling
error_exit() {
  echo "Error: $1" >&2
  exit 1
}

command || error_exit "Command failed"

# Trap errors
trap 'echo "Error on line $LINENO"' ERR
```

### File Operations

```bash
# Check existence
[ -f "$file" ] && echo "File exists"
[ -d "$dir" ]  && echo "Directory exists"
[ -e "$path" ] && echo "Path exists"

# File manipulation
touch file.txt
cp source dest
mv old new
rm file
mkdir -p dir/subdir

# Safe file operations
cp -v source dest  # Verbose
cp -i source dest  # Interactive
rm -f file         # Force
```

### JSON Handling with jq

```bash
# Parse JSON
jq '.version' plugin.json

# Modify JSON
jq '.version = "1.0.0"' plugin.json

# Pretty print
jq . < file.json

# Filter arrays
jq '.agents[] | .name' plugin.json
```

### Command Substitution

```bash
# Get command output
VERSION=$(jq -r '.version' plugin.json)
COUNT=$(find . -name "*.md" | wc -l)

# Command pipeline
STATUS=$(command1 | command2 | command3)
```

## Plugin Automation

### Validation Script

```bash
#!/bin/bash
set -e

validate_json() {
  python -m json.tool "$1" > /dev/null || {
    echo "✗ Invalid JSON: $1"
    return 1
  }
}

# Validate all JSON
for json in $(find . -name "*.json"); do
  validate_json "$json" && echo "✓ $json"
done
```

### Testing Script

```bash
#!/bin/bash
test_suite() {
  local failed=0

  echo "Running tests..."

  test1() { true; }
  test2() { [ -f "README.md" ]; }
  test3() { grep -q "version" plugin.json; }

  test1 || { echo "✗ Test 1 failed"; ((failed++)); }
  test2 || { echo "✗ Test 2 failed"; ((failed++)); }
  test3 || { echo "✗ Test 3 failed"; ((failed++)); }

  [ $failed -eq 0 ] && echo "✓ All tests passed"
  return $failed
}

test_suite
```

### Deployment Script

```bash
#!/bin/bash
deploy() {
  local version=$1

  echo "Deploying v$version..."

  # Update version
  jq ".version = \"$version\"" plugin.json > tmp && mv tmp plugin.json

  # Git operations
  git add .
  git commit -m "chore: Release v$version"
  git tag -a "v$version" -m "Release v$version"
  git push origin main
  git push origin "v$version"

  echo "✓ Deployed v$version"
}
```

## Best Practices

1. Always use `set -euo pipefail`
2. Quote variables: `"$VAR"` not `$VAR`
3. Use local variables in functions
4. Add comments explaining logic
5. Test scripts thoroughly
6. Handle errors gracefully
7. Use functions for reusability
8. Validate user input

## Common Patterns

### Command-line Argument Parsing

```bash
#!/bin/bash

while [[ $# -gt 0 ]]; do
  case $1 in
    --name) NAME="$2"; shift 2 ;;
    --version) VERSION="$2"; shift 2 ;;
    *) echo "Unknown: $1"; shift ;;
  esac
done

[ -z "${NAME:-}" ] && echo "Error: --name required" && exit 1
```

### File Processing

```bash
#!/bin/bash

process_files() {
  for file in "$@"; do
    if [ -f "$file" ]; then
      echo "Processing: $file"
      # Process file
    fi
  done
}

process_files *.md
```

### Conditional Execution

```bash
# AND
command1 && command2

# OR
command1 || command2

# Pipe with error handling
command1 | command2 || {
  echo "Pipeline failed"
  exit 1
}
```

## Resources

- GNU Bash Manual: bash.gnu.org
- ShellCheck: shellcheck.net
- BashGuide: mywiki.wooledge.org/BashGuide
- RegexOne: regexone.com (for advanced patterns)

Master bash to automate everything in your plugins!
