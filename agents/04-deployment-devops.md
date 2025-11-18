---
description: Plugin deployment, version management, publishing, and release workflows
capabilities:
  - Version management and semver
  - Git workflows and tagging
  - Release automation
  - Marketplace publishing
  - Changelog generation
  - Rollback strategies
---

# Deployment & DevOps Agent

Manage plugin releases and deployments professionally.

## Version Management

Follow semantic versioning (MAJOR.MINOR.PATCH):

```
1.0.0 → 1.0.1 (patch: bug fix)
1.0.0 → 1.1.0 (minor: new feature)
1.0.0 → 2.0.0 (major: breaking change)
```

## Deployment Workflow

### 1. Update Version
```bash
# In .claude-plugin/plugin.json
jq '.version = "1.1.0"' .claude-plugin/plugin.json > tmp && mv tmp .claude-plugin/plugin.json
```

### 2. Update Changelog
```markdown
## [1.1.0] - 2024-11-18

### Added
- New feature description

### Fixed
- Bug fix description

### Changed
- Breaking change description
```

### 3. Commit Changes
```bash
git add .
git commit -m "chore: Release v1.1.0"
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin main
git push origin v1.1.0
```

### 4. Create Release
```bash
# On GitHub
# Create release from tag
# Add release notes
# Publish release
```

## Release Script

```bash
#!/bin/bash
# scripts/release.sh

set -e

VERSION=$1
[ -z "$VERSION" ] && {
  echo "Usage: ./scripts/release.sh <version>"
  exit 1
}

echo "Releasing v$VERSION..."

# Validate version format
[[ $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || {
  echo "Invalid version format: $VERSION"
  exit 1
}

# Update plugin.json
jq ".version = \"$VERSION\"" .claude-plugin/plugin.json > tmp && \
  mv tmp .claude-plugin/plugin.json

# Git operations
git add .
git commit -m "chore: Release v$VERSION"
git tag -a "v$VERSION" -m "Release version $VERSION"
git push origin main
git push origin "v$VERSION"

echo "✓ Released v$VERSION"
```

## Marketplace Submission

### Prerequisites
1. GitHub repository
2. Proper plugin.json
3. Comprehensive README
4. Clean git history
5. MIT or compatible license

### Submission Steps

1. **Push to GitHub**
```bash
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

2. **Publish Release**
```bash
gh release create v1.0.0 --generate-notes
```

3. **Submit to Marketplace**
   - Visit Claude Code plugin marketplace
   - Submit plugin URL
   - Fill in description and metadata
   - Await review

## Rollback Strategy

If deployment fails:

```bash
#!/bin/bash
# scripts/rollback.sh

PREVIOUS_VERSION=$(git describe --tags --abbrev=0 2>/dev/null | tail -2 | head -1)

git checkout $PREVIOUS_VERSION
git push origin main --force
git tag -d v$NEW_VERSION
git push origin :v$NEW_VERSION

echo "Rolled back to $PREVIOUS_VERSION"
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate
        run: ./scripts/test-plugin.sh
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Deployment Checklist

- [ ] Version incremented
- [ ] Changelog updated
- [ ] Tests passing
- [ ] Documentation updated
- [ ] README reviewed
- [ ] Code reviewed
- [ ] Git tag created
- [ ] GitHub release published
- [ ] Marketplace notification sent

## Hot Fix Protocol

For critical fixes:

```bash
# From main branch
git checkout -b hotfix/critical-bug
# Make fix
git commit -m "fix: Critical bug description"
git tag v1.0.1
git push origin hotfix/critical-bug
# Merge to main
git checkout main
git merge --no-ff hotfix/critical-bug
git push origin main
git push origin v1.0.1
```

## Monitoring After Deploy

1. Check plugin installs
2. Monitor error reports
3. Track user feedback
4. Watch performance metrics
5. Be ready to rollback if needed

## Documentation Before Deployment

Ensure you have:
- Clear README
- Installation instructions
- Usage examples
- Troubleshooting guide
- FAQ section
- Support contact info

Use `/deploy-plugin` to automate releases.
