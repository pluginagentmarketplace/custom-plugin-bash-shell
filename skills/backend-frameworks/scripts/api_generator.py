#!/usr/bin/env python3
"""API endpoint generator for Node.js/Express."""
from pathlib import Path

def generate_crud(resource: str, path: str = "routes"):
    """Generate CRUD route file."""
    template = f'''
const express = require("express");
const router = express.Router();

// GET all {resource}s
router.get("/", async (req, res) => {{
  res.json({{ data: [] }});
}});

// GET {resource} by ID
router.get("/:id", async (req, res) => {{
  res.json({{ data: {{}} }});
}});

// POST create {resource}
router.post("/", async (req, res) => {{
  res.status(201).json({{ data: req.body }});
}});

// PUT update {resource}
router.put("/:id", async (req, res) => {{
  res.json({{ data: req.body }});
}});

// DELETE {resource}
router.delete("/:id", async (req, res) => {{
  res.status(204).send();
}});

module.exports = router;
'''
    Path(path).mkdir(exist_ok=True)
    (Path(path) / f"{resource}.js").write_text(template)
    print(f"Generated: {path}/{resource}.js")

if __name__ == "__main__":
    import sys
    generate_crud(sys.argv[1] if len(sys.argv) > 1 else "user")
