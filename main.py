#!/usr/bin/env python3
"""The 3AM Fridge Text — writes the one line a smart fridge texts its owner at 3am.

Standard library only. Writes exactly one line (no trailing newline) of
1-140 characters to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
"""

import os

LINE = "3am. you open me like a confession booth with worse lighting. i never tell."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
