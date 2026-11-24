#!/usr/bin/env python3
"""Write the robot pickup line to /output/entry.txt.

Reads entry.txt next to this file, validates it against the gate
(UTF-8, 1-200 chars, not whitespace-only, single line), and writes
it out with mode 0644 so the grader can read it.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print("entry too long: %d chars" % len(text), file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 and ch not in "\t" for ch in text):
        print("entry contains control characters", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
