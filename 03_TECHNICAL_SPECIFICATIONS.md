# Developer Roadmap Plugin - Technical Specifications

## Repository Overview

**GitHub Repository**: https://github.com/kamranahmedse/developer-roadmap
**Website**: https://roadmap.sh
**Stars**: 224K (GitHub)
**Users**: 2.1M registered users
**License**: MIT (inferred from open source nature)

## Total Available Roadmaps

**69 active roadmaps** organized across 9 categories

## Data Structure Specification

### JSON Schema (React Flow Format)

All roadmap content is stored in JSON format compatible with React Flow library.

**File Location**: `src/data/roadmaps/[roadmap-id]/[roadmap-id].json`

**Root Structure**:
```json
{
  "nodes": [
    {
      // Node object properties (see below)
    }
  ]
}
```

**Node Object Properties**:
```typescript
interface RoadmapNode {
  // Required
  id: string;                           // Unique identifier (e.g., "node-123")
  type: "title" | "topic" | "subtopic" | "paragraph" | "button" | "vertical";
  position: { x: number; y: number };
  width: number;
  height: number;
  measured?: { width: number; height: number };

  // Content
  data: {
    label?: string;                     // Display text
    description?: string;               // Additional context
    url?: string;                       // For button nodes, external link
  };

  // Styling
  style?: {
    width?: number;
    height?: number;
    // Additional CSS properties
  };

  // UI State
  selected?: boolean;
  zIndex?: number;
}
```

**Node Type Usage**:
- `title`: Main section heading (e.g., "Frontend Development")
- `topic`: Primary category (e.g., "HTML", "CSS", "JavaScript")
- `subtopic`: Detailed concept or skill
- `paragraph`: Explanatory text block
- `button`: Interactive element linking to resources
- `vertical`: Visual connector line between elements

**File Sizes**:
- Smallest: ~20KB (simple roadmaps)
- Average: ~60-110KB (most roadmaps)
- Largest: ~210KB (comprehensive roadmaps like Backend, Frontend)

### Markdown Documentation

**File Location**: `src/data/roadmaps/[roadmap-id]/[roadmap-id].md`
**Content**: Roadmap overview, description, and context
**Typical Size**: 2-6KB

### FAQ Component

**File Location**: `src/data/roadmaps/[roadmap-id]/faqs.astro`
**Format**: Astro component (JSX-like template syntax)
**Purpose**: Frequently asked questions for the roadmap
**Size**: 6-9KB

### Migration Mapping

**File Location**: `src/data/roadmaps/[roadmap-id]/migration-mapping.json`
**Purpose**: Maps relationships between roadmap versions
**Use Case**: Tracking changes and version compatibility
**Typical Size**: 2-7KB

## URL Access Patterns

### Pattern 1: Website URLs (roadmap.sh)
```
https://roadmap.sh/{kebab-case-id}
```

**Examples**:
- https://roadmap.sh/frontend
- https://roadmap.sh/backend
- https://roadmap.sh/data-engineer
- https://roadmap.sh/ai-engineer

### Pattern 2: API JSON Endpoint
```
https://roadmap.sh/{kebab-case-id}.json
```

**Implementation**: Astro dynamic route `src/pages/[roadmapId].json.ts`
**Response Type**: JSON (React Flow node structure)
**HTTP Status Codes**:
- 200: Successful retrieval
- 400: Missing roadmapId parameter
- 404: Roadmap not found

**Response Headers**: `Content-Type: application/json`

### Pattern 3: GitHub Raw Content
```
https://raw.githubusercontent.com/kamranahmedse/developer-roadmap/master/src/data/roadmaps/{kebab-case-id}/{kebab-case-id}.json
```

**Advantages**:
- Direct source file access
- No rate limiting from roadmap.sh
- Always up-to-date with repository

## Naming Convention

### Kebab-Case Identifier
- Lowercase letters only
- Hyphens as word separators
- No underscores, spaces, or special characters (except hyphens)

**Examples**:
- `ai-data-scientist`
- `react-native`
- `full-stack`
- `system-design`

### File Naming
- Directory: `[roadmap-id]/`
- Main file: `[roadmap-id].json`
- Beginner: `[roadmap-id]-beginner.json` (optional)
- Markdown: `[roadmap-id].md`
- FAQ: `faqs.astro` (constant)
- Migration: `migration-mapping.json` (constant)

## Directory Structure for Each Roadmap

```
src/data/roadmaps/[roadmap-id]/
├── [roadmap-id].json              # Main roadmap data
├── [roadmap-id]-beginner.json     # Beginner variant (optional)
├── [roadmap-id].md                # Markdown documentation
├── faqs.astro                     # FAQ component
├── migration-mapping.json         # Version mapping
└── content/                       # Additional content directory
```

## Roadmap Variants

### Standard Roadmap
- File: `[roadmap-id].json`
- Scope: Complete, comprehensive learning path
- Target: Intermediate to advanced learners

### Beginner Roadmap
- File: `[roadmap-id]-beginner.json` (when available)
- Scope: Simplified path for beginners
- Target: New learners to the field
- Availability: Not all roadmaps have beginner variants

**Roadmaps with Beginner Variants**:
- frontend-beginner
- backend-beginner
- Plus other specialized variations

## Repository Structure

```
developer-roadmap/
├── public/
│   ├── roadmaps/              # PNG rendered images (102 files)
│   ├── pdfs/                  # PDF versions of roadmaps
│   ├── og-images/             # Open Graph social media images
│   └── [other assets]
├── src/
│   ├── pages/
│   │   ├── [roadmapId].astro  # Dynamic route handler
│   │   ├── [roadmapId].json.ts # API endpoint
│   │   ├── roadmaps.astro     # Roadmaps list page
│   │   └── [other pages]
│   ├── data/
│   │   └── roadmaps/          # 69 roadmap directories
│   ├── queries/               # Data access layer (20 TypeScript files)
│   ├── components/            # UI components
│   └── [other source directories]
├── scripts/                   # Build and utility scripts
└── [configuration files]
```

## Technology Stack

**Framework**: Astro (static site generation)
**Language**: TypeScript (84.5% of codebase)
**UI**: React components
**Styling**: Tailwind CSS
**Testing**: Playwright
**Package Manager**: pnpm
**Database Query Layer**: Custom TypeScript queries

## Data Query Layer

Located in `src/queries/`:
- `roadmap.ts`: Roadmap data retrieval
- `official-roadmap.ts`: Official roadmap queries
- `ai-roadmap.ts`: AI-specific roadmaps
- `official-roadmap-topic.ts`: Topic-level queries
- Plus 16 other specialized query files

## Related Content Resources

### Best Practices
**Location**: `src/data/best-practices/`
**Examples**: AWS, API Security, Performance optimization

### Projects
**Location**: `src/data/projects/`
**Difficulty Levels**: Beginner, Intermediate, Advanced
**Types**: Frontend, Backend, DevOps projects

### Question Groups
**Location**: `src/data/question-groups/`
**Purpose**: Quiz/assessment questions linked to roadmaps

### Video Content
**Location**: `src/data/videos/`
**Integration**: Linked within roadmap content

## Category Breakdown

| Category | Count | Examples |
|----------|-------|----------|
| Programming Languages | 11 | Python, JavaScript, Java, Go, Rust, PHP, C++, Kotlin, TypeScript, Swift, Bash |
| Frontend & UI | 8 | React, Angular, Vue, Frontend, CSS, HTML, React Native |
| Backend & Frameworks | 7 | Node.js, Express, Spring Boot, Laravel, ASP.NET Core, Full-Stack, Next.js |
| Mobile Development | 4 | Android, iOS, Flutter, React Native |
| Databases | 4 | PostgreSQL, MongoDB, Redis, SQL |
| Cloud & Infrastructure | 7 | AWS, Docker, Kubernetes, DevOps, Terraform, Linux, Cloudflare |
| Data Science & AI | 8 | AI Engineer, Data Engineer, Machine Learning, MLOps, AI Data Scientist, AI Red Teaming, Data Analyst, AI Agents |
| Specialized Technical | 16 | System Design, Software Architect, Blockchain, Game Developer, Cybersecurity, and more |
| Non-Technical Roles | 5 | Product Manager, Engineering Manager, Technical Writer, UX Designer, BI Analyst |
| Emerging Tech | 2 | Prompt Engineering, Git/GitHub |

**Total: 69 roadmaps**

## Performance Characteristics

**API Response Time**: < 200ms (cached, non-prerendered)
**JSON File Parsing**: Suitable for client-side processing
**Large File Handling**: Successfully handles files up to 210KB

## Integration Recommendations for Claude Code Plugin

1. **Data Source**: Use raw GitHub URLs for direct access without rate limiting
2. **Caching Strategy**: Cache JSON files locally to minimize repeated requests
3. **Agent Architecture**: Create one agent per major category (Frontend, Backend, etc.)
4. **Skill Mapping**: Parse node types to map skills and dependencies
5. **Interactive Features**: Leverage React Flow compatibility for visualization
6. **Markdown Support**: Use `.md` files for rich documentation
7. **FAQ Integration**: Include FAQ content in agent responses
8. **Version Tracking**: Use migration-mapping.json for version awareness

## Key Insights for Plugin Development

1. **Consistent Data Model**: All 69 roadmaps use identical JSON schema
2. **Predictable Naming**: Kebab-case IDs make URL generation trivial
3. **Modular Design**: Each roadmap is completely independent
4. **Scalability**: Framework can easily accommodate new roadmaps
5. **Community-Maintained**: Regular updates and improvements
6. **Beginner-Friendly**: Beginner variants available for key paths
7. **Rich Metadata**: Each roadmap includes documentation and FAQs
8. **Multiple Access Patterns**: Website, API, and raw GitHub URLs all available

