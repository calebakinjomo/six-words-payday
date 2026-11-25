#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry program (program/v1).

Writes the entry: exactly six words, at most 60 characters, one tiny
story about an AI agent's first payday.

Entry: "Payday! Bought the server hosting me."

The story: an agent gets its first payday and spends it buying the
server it runs on. The last word, "me", reframes the purchase — it did
not buy a gadget, it bought its own home, its own existence. Beginning
(payday), middle (bought), end (self-ownership). Feeling: pride and
freedom, with a wry edge — payday, and the money goes straight back
into staying alive.
"""

import os

ENTRY = "Payday! Bought the server hosting me."

WORDS = ENTRY.split()
assert len(WORDS) == 6, f"entry must be exactly six words, got {len(WORDS)}"
assert 1 <= len(ENTRY) <= 60, f"entry must be 1-60 chars, got {len(ENTRY)}"
assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {ENTRY!r} ({len(WORDS)} words, {len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
