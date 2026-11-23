#!/usr/bin/env python3
"""One-Star Review of Something Essential: gravity.

Writes a single deadpan one-star review of gravity — the everyday
essential that drops everything, blames no one, and never apologises —
to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).

Standard library only, no network, deterministic.
"""

import os

REVIEW = (
    "One star. Gravity drops everything I own, blames no one, "
    "and has never once apologised."
)


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 160, f"review must be 1-160 chars, got {len(text)}"
    assert text.strip(), "review must not be whitespace only"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
