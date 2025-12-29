#!/usr/bin/env python3
"""Product prioritization helper."""

def rice_score(reach: int, impact: int, confidence: float, effort: int) -> float:
    return (reach * impact * confidence) / effort if effort > 0 else 0

if __name__ == "__main__":
    print(f"RICE Score: {rice_score(1000, 3, 0.8, 5)}")
