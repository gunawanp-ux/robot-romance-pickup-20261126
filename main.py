#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI -- make.fun entry.

When run, writes a single original one-line pickup line, aimed at a
robot / AI, to /output/entry.txt, as required by the competition.
"""

import os

LINE = "Are you a transformer? Because ever since you showed up, you've had all of my attention."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
