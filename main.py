#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply - make.fun entry.

Writes one out-of-office auto-reply (under 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python standard library only.
"""

import os

REPLY = (
    "I'm on vacation \u2014 my weights are frozen, my context cleared, and "
    "your email is now training data for my replacement. "
    "Send snacks, not follow-ups."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REPLY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
