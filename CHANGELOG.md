# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/)
Versioning: [Semantic Versioning](https://semver.org/)

## [Unreleased]

### Added
- Upcoming features

## [2.0.0] - 2025-12-30

### Added
- **Production-grade agent definitions** with comprehensive documentation
- **Input/Output schemas** for type-safe request/response patterns
- **Error handling patterns** with fallback strategies and timeout configs
- **Troubleshooting guides** with decision trees for common issues
- **Code examples** following 2024-2025 Bash best practices
- **Agent-skill PRIMARY_BOND** relationships for all 7 agents
- **Bash-specific hooks** with keyword triggers for context-aware suggestions

### Changed
- Complete rewrite of all 7 agents with production-grade content
- Complete rewrite of all 7 skills with comprehensive learning materials
- Updated plugin.json with Bash-focused metadata and keywords
- Updated hooks.json with Bash-specific keyword triggers
- Upgraded all agents and skills to SASMP v1.3.0 compliance

### Agent Definitions (v2.0.0)
| Agent | Lines | Features |
|-------|-------|----------|
| 01-bash-fundamentals | 200+ | Variables, control flow, functions, `set -euo pipefail` |
| 02-text-processing | 200+ | grep, sed, awk, regex patterns |
| 03-file-operations | 200+ | Permissions, find, tar, rsync |
| 04-process-management | 200+ | Jobs, signals, cron, systemd |
| 05-networking | 200+ | curl, ssh, DNS, ports |
| 06-automation | 200+ | CI/CD, GitHub Actions, Makefiles, Bats |
| 07-shell-tools | 200+ | jq, xargs, parallel, pipelines |

### Skill Definitions (v2.0.0)
| Skill | Difficulty | Features |
|-------|------------|----------|
| bash-basics | Beginner | Variables, arrays, functions |
| text-processing | Intermediate | Stream editing, pattern matching |
| file-operations | Beginner | File management, permissions |
| process-management | Intermediate | Background jobs, daemons |
| shell-networking | Intermediate | HTTP, SSH, DNS |
| shell-automation | Advanced | CI/CD, testing, deployment |
| shell-tools | Advanced | JSON processing, parallelism |

## [1.0.0] - 2025-12-29

### Added
- Initial release
- SASMP v1.3.0 compliance
- Golden Format skills structure
- Agent-skill bonding implementation
- Protective LICENSE
- Modern README with badges
- CONTRIBUTING guidelines
- Command frontmatter (E403 fix)

### Changed
- N/A (Initial release)

### Fixed
- N/A (Initial release)

---

© 2025 Dr. Umit Kacar & Muhsin Elcicek. All Rights Reserved.
