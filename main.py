#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.
"""

import os

ENTRY = "The glass was hogging my sunbeam, so I evicted it, and if the floor wanted it intact, it should have caught it."

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(ENTRY) > MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, exceeds {MAX_ENTRY_CHARS}")
    assert 1 <= len(ENTRY) <= MAX_ENTRY_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
