---
name: deployment
description: Plugin deployment strategies, version management, publishing, marketplace submission, and release workflows
---

# Deployment Skill

Master plugin distribution and release management.

## Quick Start

```bash
#!/bin/bash
# Simple deployment

VERSION="1.0.0"

# Update manifest
jq ".version = \"$VERSION\"" .claude-plugin/plugin.json > tmp && mv tmp .claude-plugin/plugin.json

# Git workflow
git add .
git commit -m "chore: Release v$VERSION"
git tag -a "v$VERSION" -m "Release v$VERSION"
git push origin main --tags

echo "✓ Released v$VERSION"
```

## Semantic Versioning

```
MAJOR.MINOR.PATCH
  ↑      ↑      ↑
  │      │      └─ Patch: bug fixes (1.0.1)
  │      └────────── Minor: new features (1.1.0)
  └────────────────── Major: breaking changes (2.0.0)
```

**Rules:**
- Start at 1.0.0
- Increment PATCH for bug fixes
- Increment MINOR for features (reset PATCH)
- Increment MAJOR for breaking changes (reset MINOR, PATCH)
- Never reuse a version number

## Full Release Workflow

### 1. Plan Release
```bash
# Determine version
VERSION="1.1.0"

# Check what changed
git log $(git describe --tags --abbrev=0)..HEAD --oneline
```

### 2. Update Files
```bash
# Update plugin.json
jq ".version = \"$VERSION\"" .claude-plugin/plugin.json > tmp && mv tmp .claude-plugin/plugin.json

# Update CHANGELOG.md
cat > CHANGELOG_NEW.md << EOF
## [$VERSION] - $(date +%Y-%m-%d)

### Added
- Feature 1
- Feature 2

### Fixed
- Bug fix 1

### Changed
- Breaking change description
EOF

cat CHANGELOG.md >> CHANGELOG_NEW.md
mv CHANGELOG_NEW.md CHANGELOG.md
```

### 3. Commit & Tag
```bash
git add .
git commit -m "chore: Release v$VERSION"
git tag -a "v$VERSION" -m "Release v$VERSION

## Changes
- Feature 1
- Bug fix 1"

git push origin main
git push origin "v$VERSION"
```

### 4. Create Release
```bash
# GitHub CLI
gh release create "v$VERSION" \
  --title "Version $VERSION" \
  --notes "See CHANGELOG.md for details"
```

## Release Script Template

```bash
#!/bin/bash
# scripts/release.sh

set -euo pipefail

VERSION=${1:-}
[ -z "$VERSION" ] && {
  echo "Usage: ./scripts/release.sh <version>"
  echo "Example: ./scripts/release.sh 1.1.0"
  exit 1
}

# Validate version
if [[ ! $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "✗ Invalid version: $VERSION"
  echo "  Use semantic versioning: MAJOR.MINOR.PATCH"
  exit 1
fi

# Check git status
if [ -n "$(git status --porcelain)" ]; then
  echo "✗ Uncommitted changes"
  git status
  exit 1
fi

echo "Releasing v$VERSION..."

# Update plugin.json
jq ".version = \"$VERSION\"" .claude-plugin/plugin.json > tmp && mv tmp .claude-plugin/plugin.json

# Run tests
echo "Running tests..."
./scripts/test-plugin.sh || {
  echo "✗ Tests failed"
  git checkout .claude-plugin/plugin.json
  exit 1
}

# Git workflow
git add .
git commit -m "chore: Release v$VERSION"
git tag -a "v$VERSION" -m "Release version $VERSION"

# Push
git push origin main
git push origin "v$VERSION"

echo "✓ Released v$VERSION"
echo "→ Push to marketplace at https://..."
```

## Changelog Format

```markdown
# Changelog

All notable changes documented here.

## [1.1.0] - 2024-11-20

### Added
- New feature X
- New feature Y

### Fixed
- Bug fix for issue Z
- Performance improvement

### Changed
- Breaking change: removed feature A
- Updated dependency

### Deprecated
- Feature B is deprecated

## [1.0.0] - 2024-11-18

### Added
- Initial release
- Core functionality
```

## Marketplace Submission

### Prerequisites
1. GitHub account
2. Public repository
3. All files in place
4. Tests passing
5. Clean git history
6. MIT or Apache 2.0 license
7. Comprehensive README

### Steps

1. **Ensure Code Quality**
```bash
./scripts/test-plugin.sh
```

2. **Document Everything**
```bash
# README should have:
- Clear description
- Installation instructions
- Usage examples
- All features listed

# CHANGELOG should be updated
```

3. **Create GitHub Release**
```bash
gh release create "v1.0.0" \
  --title "Version 1.0.0" \
  --notes "See CHANGELOG.md"
```

4. **Submit to Marketplace**
   - Visit marketplace website
   - Submit plugin URL
   - Fill in metadata
   - Await review

## Hotfix Release

For critical bugs in production:

```bash
#!/bin/bash
# Create hotfix from latest release

CURRENT_VERSION=$(jq -r '.version' .claude-plugin/plugin.json)
HOTFIX_VERSION="${CURRENT_VERSION%.*}.$((${CURRENT_VERSION##*.}+1))"

# Create hotfix branch
git checkout -b hotfix/critical-bug

# Make fix
# ... edit files ...

# Release
./scripts/release.sh "$HOTFIX_VERSION"

# Merge back
git checkout main
git merge --no-ff hotfix/critical-bug
git push origin main
```

## Rollback Procedure

```bash
#!/bin/bash
# If release breaks things

PREVIOUS_VERSION=$(git tag --list 'v*' | sort -V | tail -2 | head -1)

echo "Rolling back to $PREVIOUS_VERSION..."

git checkout "$PREVIOUS_VERSION"
git push origin main --force
git tag -d v$(jq -r '.version' .claude-plugin/plugin.json)
git push origin :v$(jq -r '.version' .claude-plugin/plugin.json)

echo "✓ Rolled back to $PREVIOUS_VERSION"
```

## Release Checklist

- [ ] Version bumped (semantic versioning)
- [ ] CHANGELOG updated
- [ ] Tests passing
- [ ] Documentation updated
- [ ] README reviewed
- [ ] Examples tested
- [ ] Code reviewed
- [ ] No security issues
- [ ] Git tags created
- [ ] GitHub release published
- [ ] Team notified

## Deployment Environments

```
Development  →  Testing  →  Staging  →  Production
Local plugin    Beta users   Pre-release  Marketplace
```

## Monitoring After Deploy

- Watch error reports
- Monitor user feedback
- Track install count
- Be ready to hotfix
- Plan next iteration

Master deployment to release with confidence!
