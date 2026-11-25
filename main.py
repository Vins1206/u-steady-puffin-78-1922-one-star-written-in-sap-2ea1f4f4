#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line, one-star review in the voice of a houseplant
about its human owner to /output/entry.txt. Pure standard library,
deterministic: the same line on every run.
"""

import os

ENTRY = (
    "One star. She repotted me into a mug with no drainage, called it "
    "'rustic', and now I sit in a puddle of my own regrets, "
    "photosynthesizing out of spite."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 279, "entry must be 1-279 characters"
    assert ENTRY.strip(), "entry must not be whitespace-only"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
