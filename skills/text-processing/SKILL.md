---
name: text-processing
description: Production-grade text processing - grep, sed, awk, regex
sasmp_version: "1.3.0"
bonded_agent: 02-text-processing
bond_type: PRIMARY_BOND
version: "2.0.0"
difficulty: intermediate
estimated_time: "6-8 hours"
---

# Text Processing Skill

> Master text manipulation with grep, sed, awk, and regular expressions

## Learning Objectives

After completing this skill, you will be able to:
- [ ] Search files efficiently with grep and ripgrep
- [ ] Transform text with sed substitutions
- [ ] Process structured data with awk
- [ ] Write and debug regular expressions
- [ ] Build efficient text processing pipelines

## Prerequisites

- Bash basics (variables, control flow)
- Command line navigation
- Understanding of stdin/stdout

## Core Concepts

### 1. Grep Essentials
```bash
# Basic search
grep 'pattern' file.txt
grep -i 'pattern' file.txt      # Case insensitive
grep -v 'pattern' file.txt      # Invert match
grep -n 'pattern' file.txt      # Line numbers
grep -c 'pattern' file.txt      # Count only

# Extended regex
grep -E 'pat1|pat2' file.txt
grep -E '^start.*end$' file.txt

# Recursive search
grep -r 'pattern' ./
grep -rn --include='*.py' 'def ' ./
```

### 2. Sed Essentials
```bash
# Substitution
sed 's/old/new/' file           # First match
sed 's/old/new/g' file          # All matches
sed -i 's/old/new/g' file       # In-place

# Line operations
sed -n '5p' file                # Print line 5
sed '5d' file                   # Delete line 5
sed '/pattern/d' file           # Delete matching

# Multiple operations
sed -e 's/a/b/' -e 's/c/d/' file
```

### 3. Awk Essentials
```bash
# Field processing
awk '{print $1}' file           # First field
awk -F: '{print $1}' file       # Custom delimiter
awk '{print $NF}' file          # Last field

# Patterns
awk '/pattern/' file            # Match lines
awk '$3 > 100' file             # Condition

# Calculations
awk '{sum+=$1} END{print sum}' file
awk 'NR>1 {total++} END{print total}' file
```

### 4. Regex Quick Reference
```bash
# Metacharacters
.     # Any character
^     # Start of line
$     # End of line
*     # Zero or more
+     # One or more (ERE)
?     # Zero or one (ERE)

# Character classes
[abc]     # Any of a, b, c
[^abc]    # Not a, b, c
[a-z]     # Range
\d        # Digit (PCRE)
\w        # Word char (PCRE)
\s        # Whitespace (PCRE)
```

## Common Patterns

### Log Analysis
```bash
# Count requests by IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn

# Find errors
grep -E 'ERROR|FATAL' app.log | tail -20

# Extract timestamps
grep 'ERROR' app.log | sed 's/.*\[\([^]]*\)\].*/\1/'
```

### Data Transformation
```bash
# CSV to TSV
sed 's/,/\t/g' data.csv

# JSON value extraction
grep -oP '"name":\s*"\K[^"]+' data.json

# Remove blank lines
sed '/^$/d' file.txt
```

## Anti-Patterns

| Don't | Do | Why |
|-------|-----|-----|
| `cat file \| grep` | `grep pattern file` | Useless use of cat |
| Multiple sed calls | Single sed with `-e` | Reduces overhead |
| `grep -E ".*"` | Omit if not needed | Slower with regex |

## Practice Exercises

1. **Log Parser**: Extract top 10 IPs from access log
2. **CSV Filter**: Filter CSV rows by column value
3. **Config Editor**: Update config values with sed
4. **Report Generator**: Summarize data with awk

## Troubleshooting

### Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Invalid regex` | Bad pattern | Escape special chars |
| `No match` | Wrong case | Use `-i` flag |
| `sed delimiter` | `/` in pattern | Use `#` or `\|` |

### Debug Techniques
```bash
# Test regex online
# https://regex101.com/

# Print matched groups
echo "test" | sed -n 's/\(.*\)/\1/p'

# Debug awk
awk '{print NR, NF, $0}' file
```

## Performance Tips

```bash
# Use ripgrep for speed
rg 'pattern' --type py

# Set locale for speed
LC_ALL=C grep 'pattern' file

# Limit output
grep -m 10 'pattern' file
```

## Resources

- [GNU Grep Manual](https://www.gnu.org/software/grep/manual/)
- [Sed One-Liners](http://sed.sourceforge.net/sed1line.txt)
- [AWK Tutorial](https://www.grymoire.com/Unix/Awk.html)
- [Regex101](https://regex101.com/)
