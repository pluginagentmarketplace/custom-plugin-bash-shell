<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Bash+Shell+Assistant;7+Agents+%7C+20+Skills;Claude+Code+Plugin" alt="Bash Shell Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-2.1.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-bash-shell/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-7-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-20-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-8-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-bash-shell)

---

### What is this?

> **Bash Shell Assistant** is a Claude Code plugin with **7 agents** and **20 skills** for bash shell development.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin add marketplace pluginagentmarketplace/custom-plugin-bash-shell

# Step 2️⃣ Install the plugin
/plugin install custom-plugin-bash-shell@pluginagentmarketplace-bash-shell

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-bash-shell.git
cd custom-plugin-bash-shell

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
custom-plugin-bash-shell:05-mobile-developer
custom-plugin-bash-shell:02-frontend-developer
custom-plugin-bash-shell:06-ai-ml-engineer
custom-plugin-bash-shell:07-system-architect
custom-plugin-bash-shell:01-backend-developer
... and 2 more
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **7 Agents** | Specialized AI agents for bash shell tasks |
| 🛠️ **20 Skills** | Reusable capabilities with Golden Format |
| ⌨️ **8 Commands** | Quick slash commands |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |

---

## 🤖 Agents

### 7 Specialized Agents

| # | Agent | Purpose |
|---|-------|---------|
| 1 | **05-mobile-developer** | Master mobile development with Android, iOS, Flutter, React  |
| 2 | **02-frontend-developer** | Master modern frontend development with React, Vue, Angular, |
| 3 | **06-ai-ml-engineer** | Master machine learning, deep learning, LLMs, AI agents, dat |
| 4 | **07-system-architect** | Master system design, scalable architecture, distributed sys |
| 5 | **01-backend-developer** | Master backend development, APIs, server architecture, and e |
| 6 | **04-database-data-specialist** | Master databases (SQL, NoSQL), data engineering, ETL pipelin |
| 7 | **03-cloud-devops-engineer** | Master cloud platforms (AWS, GCP, Azure), containerization ( |

---

## 🛠️ Skills

### Available Skills

| Skill | Description | Invoke |
|-------|-------------|--------|
| `mobile-platforms` | Mobile platforms Android, iOS, Flutter. Learn native develop | `Skill("custom-plugin-bash-shell:mobile-platforms")` |
| `ai-ml-frameworks` | Master machine learning frameworks. Learn TensorFlow, PyTorc | `Skill("custom-plugin-bash-shell:ai-ml-frameworks")` |
| `frontend-frameworks` | Master modern frontend frameworks. Learn React, Vue, Angular | `Skill("custom-plugin-bash-shell:frontend-frameworks")` |
| `devops-tools` | Master DevOps tools and practices. Learn Docker, Kubernetes, | `Skill("custom-plugin-bash-shell:devops-tools")` |
| `cloud-platforms` | Master cloud platforms AWS, GCP, Azure. Learn compute, stora | `Skill("custom-plugin-bash-shell:cloud-platforms")` |
| `code-review` | Code review and quality practices. Learn best practices, ref | `Skill("custom-plugin-bash-shell:code-review")` |
| `devrel-community` | Developer relations and community. Learn advocacy, technical | `Skill("custom-plugin-bash-shell:devrel-community")` |
| `design-patterns` | Software design patterns. Learn creational, structural, beha | `Skill("custom-plugin-bash-shell:design-patterns")` |
| `llm-ai-agents` | Large Language Models and AI Agents. Learn LLM prompting, fi | `Skill("custom-plugin-bash-shell:llm-ai-agents")` |
| `leadership-mentoring` | Engineering leadership and mentoring. Learn team management, | `Skill("custom-plugin-bash-shell:leadership-mentoring")` |
| ... | +10 more | See skills/ directory |

---

## ⌨️ Commands

| Command | Description |
|---------|-------------|
| `/skill-assessment` | Skill Assessment |
| `/career-progression` | Career Progression |
| `/project-ideas` | Project Ideas |
| `/compare-roles` | Compare Roles |
| `/explore-roadmap` | Explore Roadmap |
| `/interview-prep` | Interview Prep |
| `/my-learning-path` | My Learning Path |
| `/find-my-role` | Find My Role |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [LICENSE](LICENSE) | License information |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
custom-plugin-bash-shell/
├── 📁 .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── 📁 agents/              # 7 agents
├── 📁 skills/              # 20 skills (Golden Format)
├── 📁 commands/            # 8 commands
├── 📁 hooks/
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 LICENSE
```

</details>

---

## 📅 Metadata

| Field | Value |
|-------|-------|
| **Version** | 2.1.0 |
| **Last Updated** | 2025-12-29 |
| **Status** | Production Ready |
| **SASMP** | v1.3.0 |
| **Agents** | 7 |
| **Skills** | 20 |
| **Commands** | 8 |

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

---

## ⚠️ Security

> **Important:** This repository contains third-party code and dependencies.
>
> - ✅ Always review code before using in production
> - ✅ Check dependencies for known vulnerabilities
> - ✅ Follow security best practices
> - ✅ Report security issues privately via [Issues](../../issues)

---

## 📝 License

Copyright © 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

Custom License - See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

<table>
<tr>
<td align="center">
<strong>Dr. Umit Kacar</strong><br/>
Senior AI Researcher & Engineer
</td>
<td align="center">
<strong>Muhsin Elcicek</strong><br/>
Senior Software Architect
</td>
</tr>
</table>

---

<div align="center">

**Made with ❤️ for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>
