---
name: find-my-role
description: Find Your Shell Scripting Role
allowed-tools: Read
---

# Find My Shell Scripting Role

Discover your ideal shell scripting role based on your interests, strengths, and career goals.

## Usage

```
/find-my-role --interests [keywords] --strengths [skills]
```

## Interests

| Interest | Related Roles |
|----------|---------------|
| `servers` | SysAdmin, Platform Engineer |
| `automation` | DevOps, Automation Engineer |
| `reliability` | SRE, Platform Engineer |
| `security` | Security Engineer, SysAdmin |
| `infrastructure` | DevOps, Platform Engineer |
| `monitoring` | SRE, DevOps |

## Strengths

| Strength | Best Fit |
|----------|----------|
| `scripting` | All roles |
| `networking` | SysAdmin, Security |
| `ci-cd` | DevOps, Platform |
| `troubleshooting` | SRE, SysAdmin |
| `linux` | SysAdmin, DevOps |
| `cloud` | DevOps, Platform, SRE |

## Examples

```bash
/find-my-role --interests automation infrastructure --strengths scripting ci-cd
/find-my-role --interests reliability monitoring --strengths troubleshooting
/find-my-role --interests servers security --strengths linux networking
```

## How It Works

1. **Interest Matching** - Find roles aligned with your passions
2. **Skill Assessment** - See which roles fit your Bash strengths
3. **Goal Alignment** - Consider your career objectives
4. **Job Market** - Factor in current demand
5. **Learning Path** - Skills needed for each role
6. **Recommendations** - Get ranked role suggestions

## Role Finder Matrix

```
Your Interests + Strengths = Ideal Role

┌─────────────────────────────────────────────┐
│                                             │
│   Servers + Linux ──────► System Admin      │
│                                             │
│   Automation + CI/CD ───► DevOps Engineer   │
│                                             │
│   Reliability + Metrics ► SRE               │
│                                             │
│   Infrastructure + Cloud ► Platform Eng     │
│                                             │
│   Security + Networking ► Security Eng      │
│                                             │
└─────────────────────────────────────────────┘
```

## Next Steps

After finding your role:
- Use `/explore-roadmap` to see the learning path
- Use `/skill-assessment` to check your current level
- Use `/career-progression` to plan your growth
