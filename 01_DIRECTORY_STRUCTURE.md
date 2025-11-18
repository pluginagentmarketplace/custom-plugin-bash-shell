# Developer Roadmap Repository Structure Analysis

## Complete Directory Structure Overview

```
developer-roadmap/
├── .astro/                 # Astro framework configuration
├── .github/                # GitHub workflows and templates
├── .vscode/                # VS Code settings
├── public/
│   ├── roadmaps/          # Compiled PNG roadmap images (102 files)
│   ├── pdfs/              # PDF versions of roadmaps
│   ├── best-practices/    # Best practice guides
│   ├── img/               # Image assets
│   ├── og-images/         # Open Graph social sharing images
│   └── fonts/             # Font files
├── src/
│   ├── pages/
│   │   ├── index.astro           # Homepage
│   │   ├── roadmaps.astro        # Roadmaps listing page
│   │   ├── [roadmapId].astro     # Dynamic route for individual roadmaps
│   │   ├── [roadmapId].json.ts   # API endpoint for roadmap data
│   │   ├── ai-roadmaps/          # AI-specific roadmap routes
│   │   ├── best-practices/       # Best practice pages
│   │   ├── projects/             # Project-based learning
│   │   ├── courses/              # Course content
│   │   └── [various other pages]
│   ├── data/
│   │   ├── roadmaps/             # Source data for all 69 roadmaps
│   │   ├── best-practices/       # Best practice content
│   │   ├── projects/             # Project data
│   │   ├── videos/               # Video metadata
│   │   ├── question-groups/      # Quiz/assessment questions
│   │   └── authors/              # Author information
│   ├── components/        # React/UI components
│   ├── queries/           # Data access queries (20 TypeScript files)
│   ├── hooks/             # Custom React hooks
│   ├── layouts/           # Layout components
│   └── [other src subdirectories]
├── scripts/               # Build and utility scripts
├── tests/                 # Playwright test suite
└── [configuration files]
```

## Available Roadmaps (69 Total)

### Programming Languages (11)
- cpp, golang, java, javascript, kotlin, php, python, rust, shell-bash, swift-ui, typescript

### Frontend & UI (7)
- angular, css, frontend, html, react, react-native, vue

### Backend & Frameworks (7)
- aspnet-core, backend, laravel, nextjs, nodejs, spring-boot, full-stack

### Mobile Development (4)
- android, flutter, ios, react-native

### Databases & Storage (4)
- mongodb, postgresql-dba, redis, sql

### Cloud & Infrastructure (7)
- aws, cloudflare, devops, docker, kubernetes, linux, terraform

### Data Science & AI (7)
- ai-agents, ai-data-scientist, ai-engineer, ai-red-teaming, data-analyst, data-engineer, machine-learning

### Specialized Technical (8)
- api-design, blockchain, code-review, computer-science, cyber-security, datastructures-and-algorithms, design-system, devrel, game-developer, graphql, mlops, postgresql-dba, qa, server-side-game-developer, software-architect, software-design-architecture, system-design

### Non-Technical Roles (5)
- bi-analyst, engineering-manager, product-manager, technical-writer, ux-design

### Emerging Technologies (2)
- prompt-engineering, git-github

## File Structure for Each Roadmap

Each roadmap directory follows a consistent structure:

```
src/data/roadmaps/[roadmap-name]/
├── [roadmap-name].json          # Main roadmap data (React Flow format)
├── [roadmap-name]-beginner.json # Beginner-level variant (when available)
├── [roadmap-name].md            # Markdown documentation
├── faqs.astro                   # FAQ component
├── migration-mapping.json       # Migration reference mappings
└── content/                     # Additional content directory
```

### Example: Frontend Roadmap
```
src/data/roadmaps/frontend/
├── frontend.json                # 166,451 bytes
├── frontend-beginner.json       # 22,587 bytes
├── frontend.md                  # 6,281 bytes
├── faqs.astro                   # 8,907 bytes
├── migration-mapping.json       # 6,485 bytes
└── content/
```

## File Format Details

### Main Roadmap Files (JSON)
**Format**: React Flow-compatible JSON
**Schema**: Root key is `nodes` containing an array of node objects

**Node Object Structure**:
```json
{
  "nodes": [
    {
      "id": "unique-identifier",
      "type": "title|topic|subtopic|paragraph|button|vertical",
      "position": { "x": number, "y": number },
      "width": number,
      "height": number,
      "data": {
        "label": string,
        "description": string,
        "url": string (for buttons)
      },
      "style": { /* CSS properties */ },
      "zIndex": number,
      "selected": boolean,
      "measured": { "width": number, "height": number }
    }
  ]
}
```

**Node Types**:
- `title` - Section headings (e.g., "Frontend Development")
- `topic` - Main subject areas (e.g., "HTML", "CSS", "JavaScript")
- `subtopic` - Detailed concepts and skills
- `paragraph` - Descriptive text and explanations
- `button` - Interactive links to external resources
- `vertical` - Visual connector lines

**File Sizes**: Typically 20KB - 210KB depending on complexity

### Markdown Files (.md)
- Overview and description of the roadmap
- Typical size: 2KB - 6KB
- Contains roadmap introduction and context

### FAQ Component Files (.astro)
- Astro template files for FAQ sections
- Typical size: 6KB - 9KB
- Interactive FAQ component for the roadmap page

### Migration Mapping Files
- `migration-mapping.json`: Maps relationships between roadmap versions
- Used for tracking changes and updates
- Typically 2KB - 7KB

## URL Access Patterns

### Website URLs (roadmap.sh)
Standard format: `https://roadmap.sh/[roadmap-id]`

**Examples**:
- https://roadmap.sh/frontend
- https://roadmap.sh/backend
- https://roadmap.sh/python
- https://roadmap.sh/system-design
- https://roadmap.sh/devops
- https://roadmap.sh/data-engineer
- https://roadmap.sh/ai-engineer

### API Endpoints
**Format**: `https://roadmap.sh/[roadmapId].json`

**Implementation**: 
- Dynamic route via `src/pages/[roadmapId].json.ts`
- Returns 200 with JSON data if found
- Returns 404 if roadmap not found
- Returns 400 if roadmapId parameter is missing
- Non-prerendered endpoint (generated on-demand)

### Repository Raw File URLs
**Source Data**: `https://raw.githubusercontent.com/kamranahmedse/developer-roadmap/master/src/data/roadmaps/[name]/[name].json`

**Examples**:
- https://raw.githubusercontent.com/kamranahmedse/developer-roadmap/master/src/data/roadmaps/frontend/frontend.json
- https://raw.githubusercontent.com/kamranahmedse/developer-roadmap/master/src/data/roadmaps/backend/backend.json
- https://raw.githubusercontent.com/kamranahmedse/developer-roadmap/master/src/data/roadmaps/python/python.json

## Naming Conventions

### Directory/File Naming
- **Format**: Lowercase with hyphens
- **Pattern**: `[role-name]` (kebab-case)
- **Examples**:
  - `ai-data-scientist`
  - `devops`
  - `full-stack`
  - `system-design`
  - `react-native`

### JSON Files
- Main file: `[name].json`
- Beginner variant: `[name]-beginner.json` (if available)
- Migration mapping: `migration-mapping.json`

### Image Files
- Format: PNG
- Location: `public/roadmaps/[name].png`
- Naming: Same as roadmap ID

### URL IDs
- Same as directory/file naming convention
- Lowercase with hyphens
- No file extensions in URLs

## Content Organization Hierarchy

### By Role/Career Path
The primary organization is around professional roles and specializations:
- **Development Roles**: Frontend, Backend, Full-Stack, DevOps, QA, Engineering Manager
- **Language-Specific**: Python, JavaScript, Java, Go, Rust, PHP, etc.
- **Framework-Specific**: React, Angular, Vue, Spring Boot, Django, Laravel, etc.
- **Technology-Specific**: Docker, Kubernetes, AWS, PostgreSQL, Redis, MongoDB
- **Domain-Specific**: Machine Learning, Data Engineering, Game Development, Blockchain, Cybersecurity
- **Non-Technical**: Product Manager, Technical Writer, UX Designer, Business Analyst

### By Skill Level
Some roadmaps have multiple difficulty levels:
- **Standard**: Full comprehensive roadmap (main [name].json)
- **Beginner**: Simplified version for newcomers (when [name]-beginner.json exists)
- **Advanced**: (implied through content organization)

## Supporting Content Structure

Each roadmap integrates with these complementary resources:

1. **Best Practices** (`src/data/best-practices/`)
   - AWS Best Practices
   - API Security
   - Performance optimization guides

2. **Projects** (`src/data/projects/`)
   - Frontend projects
   - Backend projects
   - DevOps projects with difficulty levels

3. **Question Groups** (`src/data/question-groups/`)
   - Quiz and assessment questions organized by topic
   - Used for skill validation and practice

4. **Video Resources** (`src/data/videos/`)
   - Linked video content for each roadmap
   - Supports multimedia learning

5. **Guides** 
   - Official guides integrated with roadmaps
   - Topic-specific deep dives

## Technology Stack

**Framework**: Astro (static site generation)
**Primary Language**: TypeScript (84.5%)
**UI/Components**: React components
**Styling**: Tailwind CSS
**Testing**: Playwright
**Package Manager**: pnpm

## Key Observations for Plugin Development

1. **Consistent Structure**: Every roadmap follows the same directory and file naming pattern
2. **JSON Schema**: All roadmap data uses React Flow-compatible JSON format
3. **API Available**: Direct JSON endpoint for each roadmap at `[roadmapId].json`
4. **Raw Content**: Source files directly accessible via GitHub raw content URL
5. **Dynamic Routing**: Website uses Astro's dynamic routes for URL patterns
6. **Variants Support**: Framework supports multiple difficulty levels (e.g., -beginner)
7. **Modular Design**: Roadmaps are independent, self-contained directories
8. **Scalable**: Adding new roadmaps is as simple as creating a new directory with required files

## Integration Points for Claude Code Plugin

1. **JSON Data Source**: Direct access to roadmap JSON files
2. **URL Pattern**: Predictable, consistent URL structure
3. **API Endpoints**: JSON API for programmatic access
4. **Markdown Support**: Documentation files for context
5. **Skill-based Agents**: Each roadmap can have dedicated agents
6. **Resource Linking**: Integration with projects, best practices, and guides

