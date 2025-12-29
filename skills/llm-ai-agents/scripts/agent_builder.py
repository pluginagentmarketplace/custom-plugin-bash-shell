#!/usr/bin/env python3
"""LLM Agent builder template."""

class SimpleAgent:
    def __init__(self, llm, tools=None):
        self.llm = llm
        self.tools = tools or []

    def run(self, prompt: str) -> str:
        return self.llm.generate(prompt)

if __name__ == "__main__":
    print("Agent builder loaded")
