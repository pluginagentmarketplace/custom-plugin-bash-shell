#!/usr/bin/env python3
"""React component generator."""
from pathlib import Path

def create_component(name: str):
    Path(f"src/components/{name}").mkdir(parents=True, exist_ok=True)
    (Path(f"src/components/{name}/{name}.tsx")).write_text(f'''
export function {name}() {{
  return <div>{name}</div>;
}}
''')
    print(f"Created: {name}")

if __name__ == "__main__":
    import sys
    create_component(sys.argv[1] if len(sys.argv) > 1 else "Button")
