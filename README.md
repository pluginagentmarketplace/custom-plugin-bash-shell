# Custom Plugin Bash Shell Toolkit

Professional toolkit for developing, testing, and deploying Claude Code plugins using bash scripting. Create production-ready plugins with intelligent automation, comprehensive testing, and streamlined deployment.

## 🎯 What This Plugin Does

Streamline your Claude Code plugin development:

- **Scaffold** - Generate plugin structure instantly
- **Validate** - Verify manifest and components
- **Test** - Run comprehensive quality checks
- **Deploy** - Release with confidence

## 🚀 Quick Start

### First Command
```bash
/scaffold-plugin my-plugin
```

### Complete Workflow
```bash
/scaffold-plugin my-plugin        # Create structure
/validate-plugin                  # Check validity
/test-plugin                      # Run tests
/deploy-plugin                    # Release
```

## 📚 Components

### 5 Specialized Agents

1. **Plugin Architect** - Structure and design decisions
2. **Bash Specialist** - Shell scripting and automation
3. **Testing & QA** - Quality assurance strategies
4. **Deployment & DevOps** - Release management
5. **Automation & Hooks** - Event automation workflows

### 5 Skill Modules

- **bash-scripting** - Shell scripting fundamentals and patterns
- **plugin-architecture** - Official Claude Code plugin format
- **testing-validation** - Testing strategies and quality gates
- **deployment** - Version management and release workflows
- **hook-automation** - Event automation and workflows

### 4 Slash Commands

#### /scaffold-plugin
Generate new plugin with proper structure
```bash
/scaffold-plugin my-awesome-plugin --template advanced
```

#### /validate-plugin
Check manifest, structure, and components
```bash
/validate-plugin --strict --verbose
```

#### /test-plugin
Run comprehensive test suite
```bash
/test-plugin --coverage
```

#### /deploy-plugin
Release plugin to marketplace
```bash
/deploy-plugin --version 1.1.0
```

## 🎓 Learning Path

### Phase 1: Understand
- Explore plugin architecture with Plugin Architect agent
- Review `plugin-architecture` skill
- Study official format documentation

### Phase 2: Build
- Use `/scaffold-plugin` to create structure
- Use Bash Specialist agent for scripting help
- Follow bash-scripting skill examples

### Phase 3: Verify
- Use `/validate-plugin` to check structure
- Use `/test-plugin` to run quality checks
- Review Testing & QA agent guidance

### Phase 4: Release
- Use `/deploy-plugin` to release
- Follow deployment skill for versioning
- Use Deployment & DevOps agent guidance

## 📋 Official Format Compliance

This toolkit enforces official Claude Code plugin format:

✅ `.claude-plugin/plugin.json` - Manifest
✅ `agents/` - YAML frontmatter markdown files
✅ `commands/` - Slash command documentation
✅ `skills/` - SKILL.md modules
✅ `hooks/` - Automation configuration
✅ Complete documentation

## 💡 Example Workflow

### Creating Your First Plugin

```bash
# 1. Generate structure
/scaffold-plugin learning-system

# 2. Edit your components
# Edit agents/01-*.md
# Edit commands/command.md
# Edit skills/*/SKILL.md
# Edit hooks/hooks.json

# 3. Validate structure
/validate-plugin

# 4. Run tests
/test-plugin

# 5. Deploy to marketplace
/deploy-plugin --version 1.0.0
```

### Common Tasks

**Start developing a plugin**
```bash
/scaffold-plugin project-name
```

**Check if plugin is valid**
```bash
/validate-plugin --strict
```

**Ensure quality before release**
```bash
/test-plugin --coverage
```

**Release version 2.0.0**
```bash
/deploy-plugin --version 2.0.0
```

## 🔧 Key Concepts

### Plugin.json
Central manifest defining your plugin:
- Metadata (name, version, description)
- Agent references
- Command references
- Skill references
- Hook configuration

### Agents
Expert specialists in markdown:
- YAML frontmatter for metadata
- Focused expertise area
- Clear descriptions and capabilities
- Content covering the domain

### Commands
User-triggered workflows:
- Clear documentation
- Usage instructions
- Practical examples
- Step-by-step guidance

### Skills
Reusable technical knowledge:
- SKILL.md in subdirectory
- Quick start examples
- Code samples
- Best practices

### Hooks
Intelligent automation:
- Event-based triggers
- Keyword detection
- Smart suggestions
- Workflow guidance

## 🌟 Features

- **Bash Integration** - Automate everything with shell scripts
- **Proper Structure** - Official Claude Code format compliance
- **Validation** - Catch errors before deployment
- **Testing** - Comprehensive quality assurance
- **Deployment** - One-command releases
- **Automation** - Intelligent hooks and workflows
- **Documentation** - Complete skill modules

## 📊 Plugin Overview

| Component | Count | Purpose |
|-----------|-------|---------|
| Agents | 5 | Domain expertise |
| Skills | 5 | Technical knowledge |
| Commands | 4 | User workflows |
| Hooks | 5 | Event automation |
| Scripts | Optional | Custom automation |

## 🚦 Getting Started

1. **Understand the Format**
   - Read `plugin-architecture` skill
   - Review official Claude Code docs

2. **Create Your Plugin**
   - Use `/scaffold-plugin` command
   - Choose template (basic or advanced)

3. **Develop Components**
   - Edit agents with YAML frontmatter
   - Create slash commands with examples
   - Add skills with code samples

4. **Validate & Test**
   - Use `/validate-plugin` regularly
   - Run `/test-plugin` before release

5. **Deploy**
   - Use `/deploy-plugin` to release
   - Follow semantic versioning

## 📖 Documentation

### For Quick Questions
- Use agent guidance (/scaffold-plugin suggests next steps)
- Check command help sections
- Review skill modules

### For Detailed Learning
- Read `plugin-architecture` skill
- Study deployment skill for releases
- Explore bash-scripting for automation

### For Troubleshooting
- Run `/validate-plugin --verbose`
- Run `/test-plugin` to see issues
- Check error messages carefully

## 🎯 Best Practices

1. **Semantic Versioning** - Follow MAJOR.MINOR.PATCH
2. **Proper Structure** - Use official format strictly
3. **Clear Documentation** - Write for users
4. **Code Examples** - Show, don't tell
5. **Test Before Release** - Quality first
6. **Keep Changelog** - Document all changes
7. **Use Hooks** - Automate workflows

## 🔗 Integration

This plugin helps you create other plugins:
- Complete plugin development toolkit
- All official format requirements met
- Professional quality standards
- Production-ready deployment

## 📦 What Comes After

After developing your plugin:
- Load locally in Claude Code
- Distribute to GitHub
- Submit to marketplace
- Monitor user adoption
- Plan next iteration

## ❓ FAQ

**How long does it take to create a plugin?**
With this toolkit: 1-2 hours for basic plugins, 4-8 hours for advanced

**Can I customize the scaffolding?**
Yes, scaffolding creates templates you can fully customize

**Do I need to know bash?**
For basic plugins, no. The `bash-scripting` skill teaches what you need

**How do I test my plugin?**
Use `/test-plugin` for automated testing

**When should I deploy?**
After `/validate-plugin` and `/test-plugin` pass

## 🚀 Next Steps

1. Try `/scaffold-plugin` to create your first plugin
2. Review the created structure
3. Read the skill modules for your task
4. Build your plugin using the agents
5. Validate with `/validate-plugin`
6. Test with `/test-plugin`
7. Deploy with `/deploy-plugin`

## 📄 License

MIT - See LICENSE file

## 🙋 Support

- Check the skill modules for detailed help
- Use agent guidance for specific tasks
- Review commands for workflow help
- Read documentation thoroughly

---

**Ready to create amazing Claude Code plugins?**

Start with `/scaffold-plugin your-plugin-name` and let the toolkit guide you!
