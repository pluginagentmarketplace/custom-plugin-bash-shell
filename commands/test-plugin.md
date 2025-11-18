# Test Plugin

Run comprehensive tests on your plugin to ensure quality and correctness.

## Usage

```
/test-plugin [--coverage] [--watch]
```

## Examples

```
/test-plugin
/test-plugin --coverage
/test-plugin --watch
```

## What It Tests

### Structure Tests
- Directory structure is correct
- All required files present
- No missing components

### Manifest Tests
- JSON is valid
- All fields are correct
- References resolve
- Version is valid

### Content Tests
- Agents have YAML frontmatter
- Commands have usage sections
- Skills have code examples
- All descriptions present

### Link Tests
- Markdown links are valid
- No broken references
- URLs are reachable
- File paths exist

### Quality Tests
- No TODO/FIXME comments
- Consistent formatting
- Documentation complete
- Examples are valid

## Test Phases

### Phase 1: Basic Structure
```
Checking directories... ✓
Checking files... ✓
Checking JSON... ✓
```

### Phase 2: Content Validation
```
Validating agents... ✓
Validating commands... ✓
Validating skills... ✓
```

### Phase 3: Link Checking
```
Checking markdown links... ✓
Checking file references... ✓
Checking URLs... ✓
```

### Phase 4: Quality Assurance
```
Checking for TODOs... ✓
Checking formatting... ✓
Checking examples... ✓
```

## Test Report

```
=== Plugin Test Report ===

Passed:  42/42 tests
Failed:  0/0 tests
Skipped: 0/0 tests

Coverage: 100%

✓ All tests passed!
Ready for deployment.
```

## Flags

### --coverage
Detailed coverage report:
- Which components tested
- Test coverage percentage
- Untested areas
- Recommendations

### --watch
Watch mode:
- Re-run tests on file changes
- Live feedback
- Quick iteration
- Development mode

## Test Failures

When tests fail:

1. **Read the error** - Understand what failed
2. **Locate the issue** - Find the problematic file
3. **Fix the problem** - Make corrections
4. **Run tests again** - Verify the fix

## Example Test Output

```
Running Plugin Tests...
========================

[Structure Tests]
✓ Directory structure
✓ Required files present
✓ No extra files
✓ File permissions

[Manifest Tests]
✓ JSON syntax valid
✓ Required fields present
✓ Version format correct
✓ References resolve

[Agent Tests]
✓ Agent 1: YAML valid
✓ Agent 1: Description present
✓ Agent 2: YAML valid
✓ Agent 2: Description present

[Command Tests]
✓ Command 1: Title present
✓ Command 1: Usage section
✓ Command 2: Title present
✓ Command 2: Usage section

[Skill Tests]
✓ Skill 1: SKILL.md present
✓ Skill 1: Code examples
✓ Skill 2: SKILL.md present
✓ Skill 2: Code examples

[Quality Tests]
✓ No TODO comments
✓ Formatting consistent
✓ Links valid
✓ Documentation complete

========================
✓ 28/28 tests passed
Ready for deployment!
```

## Test Categories

| Category | Count | Status |
|----------|-------|--------|
| Structure | 4 | ✓ Pass |
| Manifest | 4 | ✓ Pass |
| Agents | 2 | ✓ Pass |
| Commands | 2 | ✓ Pass |
| Skills | 2 | ✓ Pass |
| Quality | 4 | ✓ Pass |

## Common Test Failures

**Failed: JSON syntax**
- Check plugin.json for errors
- Use Python to validate: `python -m json.tool`

**Failed: Missing file**
- Add the missing file
- Update manifest if needed

**Failed: Broken link**
- Check link syntax
- Verify file path
- Update reference

**Failed: Missing section**
- Add required sections
- Follow template format

## Before Release Checklist

Before deploying, ensure:
- [ ] All tests passing
- [ ] No TODO comments
- [ ] Documentation complete
- [ ] Examples working
- [ ] Version bumped
- [ ] CHANGELOG updated

## Integration

Typical workflow:
- `/scaffold-plugin` → Create structure
- → `/validate-plugin` → Check structure
- → `/test-plugin` → Run tests
- → `/deploy-plugin` → Release

## Continuous Testing

Run tests frequently:
- After every change
- Before committing
- Before deploying
- Regularly in development

Use `/test-plugin` to maintain quality!
