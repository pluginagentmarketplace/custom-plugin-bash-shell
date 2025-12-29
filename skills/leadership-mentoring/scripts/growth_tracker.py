#!/usr/bin/env python3
"""Team growth tracker."""

def track_growth(team_size: int, promoted: int) -> float:
    return (promoted / team_size) * 100 if team_size > 0 else 0

if __name__ == "__main__":
    print(f"Promotion rate: {track_growth(10, 2)}%")
