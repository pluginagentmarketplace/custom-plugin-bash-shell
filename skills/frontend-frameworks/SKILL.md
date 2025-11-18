---
name: frontend-frameworks
description: Frontend frameworks including React, Vue, Angular. Learn component architecture, state management, routing, and modern web development practices.
---

# Frontend Frameworks Skill

Master modern frontend development with popular frameworks and libraries.

## Quick Start

### Understanding Frontend Frameworks

Frontend frameworks provide structure for building web applications with:
- **Components** - Reusable UI pieces
- **State Management** - Managing application data
- **Routing** - Navigation between pages
- **Templating** - Dynamic HTML generation

### The Big Three Frameworks

#### React
```jsx
// Component-based, functional, JSX syntax
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

#### Vue.js
```vue
<!-- Template-based, progressive, single-file components -->
<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  data() {
    return { count: 0 };
  },
  methods: {
    increment() { this.count++; }
  }
}
</script>
```

#### Angular
```typescript
// Full-featured framework, TypeScript-first
import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  template: `
    <p>Count: {{count}}</p>
    <button (click)="increment()">Increment</button>
  `
})
export class CounterComponent {
  count = 0;
  increment() { this.count++; }
}
```

## Core Frontend Concepts

### Components
- Reusable, self-contained UI units
- Props (input) and state (internal data)
- Composition and nesting
- Lifecycle methods
- Performance optimization (memoization)

### State Management
- Local component state
- Props drilling (passing through parents)
- Global state (Redux, Vuex, Context API)
- State management patterns
- When to use which approach

### Routing
- Page navigation without reload (SPA)
- Route parameters and dynamic segments
- Nested routes
- Route guards and authentication
- Navigation history

### Form Handling
- Form inputs (text, select, radio, checkbox)
- Controlled vs uncontrolled components
- Validation (client-side)
- Form submission
- File uploads

### API Integration
- Fetching data from servers
- HTTP methods (GET, POST, PUT, DELETE)
- Handling responses and errors
- Loading and error states
- Caching and optimization

### Styling
- CSS-in-JS (styled-components, Emotion)
- CSS Modules
- Tailwind CSS and utility-first
- SCSS/LESS preprocessors
- CSS-in-JS vs traditional CSS

### Performance
- Code splitting and lazy loading
- Tree-shaking unused code
- Image optimization
- Virtual scrolling for long lists
- Memoization and useMemo/useCallback

## Learning Path

### Phase 1: Core Concepts (2-4 weeks)
- Choose a framework (React, Vue, or Angular)
- Learn component basics
- Understand JSX/templates
- Build simple components
- Props and state

### Phase 2: Intermediate Features (4-8 weeks)
- Advanced component patterns
- State management solutions
- Routing implementation
- Form handling
- API integration
- Styling strategies

### Phase 3: Advanced Topics (8-12 weeks)
- Performance optimization
- Testing components
- Build tools and bundling
- Server-side rendering (SSR) / Static generation
- Advanced state patterns
- TypeScript integration

### Phase 4: Specialization
- Learn meta-frameworks (Next.js, Nuxt, etc.)
- Mobile frameworks (React Native, NativeScript)
- Desktop frameworks (Electron, Tauri)
- Full-stack development

## Technology Ecosystem

### State Management
- **Redux** - Predictable state container
- **Zustand** - Minimal state manager
- **Jotai** - Atomic state
- **Pinia/Vuex** - Vue-specific solutions
- **NgRx** - Angular state management

### UI Component Libraries
- **Material UI** - Google Material Design
- **Chakra UI** - Accessibility-first components
- **Ant Design** - Enterprise UI library
- **Bootstrap** - Popular CSS framework
- **Tailwind CSS** - Utility-first CSS

### Testing
- **Jest** - Testing framework
- **React Testing Library** - Component testing
- **Vitest** - Fast unit test framework
- **Cypress** - E2E testing
- **Playwright** - Multi-browser E2E testing

### Build Tools
- **Webpack** - Module bundler
- **Vite** - Fast build tool
- **Parcel** - Zero-config bundler
- **esbuild** - Fast JavaScript bundler

### Meta-Frameworks
- **Next.js** - React meta-framework (SSR, SSG)
- **Nuxt** - Vue meta-framework (SSR, SSG)
- **SvelteKit** - Svelte meta-framework
- **Remix** - Full-stack React framework

## Best Practices

### Component Design
- Keep components focused and small
- Use composition over inheritance
- Props should be immutable
- Separate container and presentational components
- Use TypeScript for type safety

### State Management
- Store minimal state
- Derive computed values
- Keep state as local as possible
- Use unidirectional data flow
- Avoid prop drilling with context/stores

### Performance
- Use React.memo/memoization appropriately
- Implement code splitting
- Optimize re-renders
- Use production builds
- Monitor bundle size

### Accessibility
- Semantic HTML elements
- ARIA attributes where needed
- Keyboard navigation support
- Color contrast and visual design
- Screen reader testing

### Security
- Sanitize user input
- Avoid XSS vulnerabilities
- Use HTTPS
- Validate server-side
- Keep dependencies updated

## Common Patterns

### Render Props
```jsx
function DataFetcher({render}) {
  const [data, setData] = useState(null);
  // Fetch data...
  return render(data);
}
```

### Higher-Order Components
```jsx
function withAuth(Component) {
  return (props) => {
    const [authenticated, setAuthenticated] = useState(false);
    return authenticated ? <Component {...props} /> : <Login />;
  };
}
```

### Hooks (Modern React)
```jsx
// Custom hook
function useFetch(url) {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch(url).then(r => r.json()).then(setData);
  }, [url]);
  return data;
}
```

## Framework Comparison

| Aspect | React | Vue | Angular |
|--------|-------|-----|---------|
| Learning Curve | Medium | Easy | Hard |
| Job Market | Excellent | Good | Good |
| Bundle Size | Medium | Small | Large |
| Performance | Excellent | Excellent | Good |
| Ecosystem | Huge | Moderate | Complete |
| Company Backing | Meta | Community | Google |
| Best For | Startups, large apps | Small-medium apps | Enterprise |

## Resources

- **Official Docs**: React.dev, Vue.js.org, Angular.io
- **Learning**: Frontend Masters, egghead.io, Udemy courses
- **Practice**: CodePen, Codesandbox, GitHub projects
- **Community**: Twitter, Discord, local meetups

## Next Steps

After mastering a frontend framework:
- Learn **TypeScript** for type safety
- Explore **Server-side rendering** with meta-frameworks
- Develop **Mobile apps** with React Native or Flutter
- Build **Full-stack applications** with backend integration
- Master **Advanced patterns** and architecture
