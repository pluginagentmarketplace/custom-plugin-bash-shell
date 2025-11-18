# Deploy Plugin

Deploy and publish your Claude Code plugin to the marketplace or distribute it.

## Usage

```
/deploy-plugin [--version VERSION] [--draft] [--force]
```

## Examples

```
/deploy-plugin
/deploy-plugin --version 1.1.0
/deploy-plugin --draft
/deploy-plugin --force
```

## Pre-Deployment Checklist

Before deploying:
- [ ] `/validate-plugin` passed
- [ ] `/test-plugin` passed
- [ ] Version incremented
- [ ] CHANGELOG updated
- [ ] README reviewed
- [ ] No security issues
- [ ] Code reviewed
- [ ] Git committed

## Deployment Steps

### 1. Validate & Test
```
✓ Run /validate-plugin
✓ Run /test-plugin
✓ All checks pass
```

### 2. Update Version
```
Update .claude-plugin/plugin.json:
  "version": "1.1.0"

Update CHANGELOG.md:
  ## [1.1.0] - 2024-11-20
  ### Added
  - New features...
```

### 3. Create Git Tag
```
git add .
git commit -m "chore: Release v1.1.0"
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin main --tags
```

### 4. Create Release
```
Create GitHub release from tag
Include release notes
Attach plugin files
```

### 5. Publish to Marketplace
```
Submit plugin URL
Complete metadata
Await review/approval
```

## Deployment Flags

### --version
Specify version explicitly:
```
/deploy-plugin --version 2.0.0
```

### --draft
Create draft release (not published):
```
/deploy-plugin --draft
```

### --force
Skip validation (not recommended):
```
/deploy-plugin --force
```

## Deployment Output

```
=== Plugin Deployment ===

Plugin: my-plugin
Version: 1.1.0
Status: Ready

Pre-flight checks:
✓ Validation passed
✓ Tests passed
✓ Manifest valid
✓ Git status clean

Deployment steps:
→ Creating git tag: v1.1.0
→ Pushing to origin
→ Creating GitHub release
→ Publishing to marketplace

Deployment Result:
✓ Successfully deployed v1.1.0
🎉 Plugin is now available!
```

## Version Management

### Semantic Versioning
- 1.0.0 = Initial release
- 1.0.1 = Bug fix
- 1.1.0 = New feature
- 2.0.0 = Breaking change

### Automatic Versioning
If no --version specified:
- Patch version incremented by default
- Can manually specify MAJOR.MINOR.PATCH

## Rollback

If deployment fails:

```
/deploy-plugin --rollback [VERSION]

This will:
- Revert to previous version
- Remove failed release
- Restore previous state
- Document what happened
```

## Marketplace Requirements

Your plugin must have:
- ✓ Valid plugin.json
- ✓ Comprehensive README
- ✓ Updated CHANGELOG
- ✓ Clear description
- ✓ MIT or compatible license
- ✓ Public GitHub repository
- ✓ All tests passing

## Marketplace Submission

After deploying:

1. **Get deployment URL**
   - Provided after successful deployment

2. **Visit Marketplace**
   - Go to Claude Code plugin marketplace
   - Select "Submit Plugin"

3. **Fill Information**
   - Plugin URL
   - Description
   - Keywords
   - Category

4. **Wait for Review**
   - Marketplace team reviews
   - May request changes
   - Approval takes 1-7 days

5. **Publish**
   - Once approved
   - Plugin appears in marketplace
   - Users can install via /plugin add

## Deployment Notifications

After deployment, your team is notified:
- Email notification sent
- Release notes shared
- Installation instructions provided
- Metrics dashboard updated

## Monitoring After Deploy

Post-deployment tasks:
- [ ] Check install count
- [ ] Monitor error reports
- [ ] Track user feedback
- [ ] Be ready to hotfix
- [ ] Plan next release

## Hotfix Deployment

For critical fixes:

```
/deploy-plugin --hotfix

This will:
- Create hotfix branch
- Deploy immediately
- Skip normal workflow
- Alert team
```

## Integration with Other Commands

Complete workflow:
1. `/scaffold-plugin` → Create plugin
2. → `/validate-plugin` → Check structure
3. → `/test-plugin` → Run tests
4. → `/deploy-plugin` → Release

## Tips

- Deploy during business hours
- Have a rollback plan
- Monitor after deployment
- Communicate with team
- Document any issues
- Plan next iteration

## Success Criteria

Deployment is successful when:
- ✓ Version tag created
- ✓ GitHub release published
- ✓ Plugin files uploaded
- ✓ Marketplace submission received
- ✓ Installation works
- ✓ No user errors reported

Use `/deploy-plugin` to release with confidence!
