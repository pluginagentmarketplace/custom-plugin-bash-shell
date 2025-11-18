# Scaffold Plugin

Generate a new Claude Code plugin with proper directory structure and boilerplate files.

## Usage

```
/scaffold-plugin <plugin-name> [--template basic|advanced]
```

## Examples

```
/scaffold-plugin my-awesome-plugin
/scaffold-plugin bash-tools --template advanced
/scaffold-plugin learning-system --template basic
```

## What It Creates

```
my-awesome-plugin/
├── .claude-plugin/
│   └── plugin.json          # Manifest with your name
├── agents/
│   └── 01-specialist.md     # Template agent with YAML frontmatter
├── commands/
│   └── main-command.md      # Template command
├── skills/
│   └── core-skill/SKILL.md  # Template skill module
├── hooks/
│   └── hooks.json           # Automation configuration
├── scripts/
│   ├── test.sh              # Test automation
│   └── deploy.sh            # Release automation
├── README.md                # Documentation template
├── CHANGELOG.md             # Version history template
└── LICENSE                  # MIT license
```

## Template Options

### basic
- 1 agent
- 1 command
- 1 skill
- Minimal setup

### advanced (default)
- 3 agents
- 3 commands
- 3 skills
- Full examples
- Hook setup

## Next Steps After Scaffolding

1. **Edit plugin.json**
   - Update name and description
   - Add your metadata

2. **Create Agents**
   - Edit `agents/01-specialist.md`
   - Add more agents as needed
   - Use YAML frontmatter

3. **Define Commands**
   - Create slash commands in `commands/`
   - Each command is a markdown file
   - Include usage examples

4. **Build Skills**
   - Create skill modules in `skills/`
   - Each skill has `SKILL.md` in a subdirectory
   - Add code examples

5. **Configure Hooks**
   - Edit `hooks/hooks.json`
   - Define automation triggers
   - Test your workflows

6. **Validate**
   - Run `/validate-plugin`
   - Fix any issues
   - Ensure structure is correct

7. **Test**
   - Run `/test-plugin`
   - Verify all files
   - Check manifest validity

8. **Deploy**
   - When ready, use `/deploy-plugin`
   - Publish to marketplace

## Generated Files

### plugin.json
Pre-filled with:
- Your plugin name
- Version 1.0.0
- Agent references
- Command references
- Skill references

### README.md
Template includes:
- Plugin description
- Quick start
- Installation
- Usage examples
- Features list

### CHANGELOG.md
Starts with:
- Version 1.0.0 release notes
- Initial features list

### Test Script
Includes checks for:
- JSON validity
- File structure
- Required components

## Customization

After scaffolding, you can:
- Rename agents/commands/skills
- Add more components
- Customize metadata
- Update descriptions

Make sure to update plugin.json when you add new components!

## Tips

- Choose a unique plugin name
- Keep descriptions under 200 characters
- Write clear agent descriptions
- Include code examples in skills
- Document all commands
- Update CHANGELOG with releases
- Follow semantic versioning

## Integration with Other Commands

After scaffolding:
- → `/validate-plugin` to check structure
- → `/test-plugin` to run tests
- → `/deploy-plugin` to release

Use `/scaffold-plugin` to start developing!
