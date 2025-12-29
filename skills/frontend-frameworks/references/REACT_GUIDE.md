# Frontend Frameworks Guide

## React Patterns

```tsx
// Custom Hook
function useAsync<T>(fn: () => Promise<T>) {
  const [state, setState] = useState<T>();
  useEffect(() => { fn().then(setState); }, []);
  return state;
}
```

## State Management

| Library | Use Case |
|---------|----------|
| useState | Local |
| Zustand | Global |
| TanStack Query | Server |
