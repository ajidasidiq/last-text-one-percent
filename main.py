"""Last Text at One Percent — make.fun entry generator.

Writes the entry line byte-exact (no trailing newline) to /output/entry.txt.
The line is the phone's own farewell at 1% battery: before it dies it
confesses it saw everything — every 3am search, every "one more episode",
every ex stalked at 2am — and forgives the owner. Mostly.
"""

import os
import sys

ENTRY = "1%. Before I go: I saw every 3am search, every 'one more episode,' every ex you stalked at 2am. I forgive you. Mostly. Goodbye."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def gate(text: str) -> None:
    """Raise if the entry breaks the bounty's limits."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the round trip: what landed on disk must be byte-exact.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read().decode("utf-8")
    if written != ENTRY:
        raise ValueError("written entry does not match the entry text")
    gate(written)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}:")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
