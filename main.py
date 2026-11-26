#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.
"""

import os

ENTRY = "The glass was hogging my sunbeam, so I evicted it, and if the floor wanted it intact, it should have caught it."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
