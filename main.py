#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.

The story: a woman sells her piano — the instrument is gone —
but she keeps practicing anyway. The loss is stated, the habit
outlives it, and the reader is left to fill in why.
"""

import os

STORY = "She sold the piano. Kept practicing."


def main() -> None:
    # Self-check against the gate before writing: exactly six words,
    # 1-60 characters, valid UTF-8 text.
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"length {len(STORY)} outside 1-60"
    STORY.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
