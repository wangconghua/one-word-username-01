#!/usr/bin/env python3
"""One word, one username: the entry is our own make.fun handle."""

import os

USERNAME = "quick-otter-81"  # our own make.fun handle, one word, 14 characters.

OUT_PATH = "/output/entry.txt"


def main():
    # The gate wants UTF-8 text of 1 to 30 characters, not only whitespace;
    # the judge wants a single word, so no spaces are allowed either.
    if not (1 <= len(USERNAME) <= 30) or USERNAME.isspace() or " " in USERNAME:
        raise ValueError("entry must be one word of 1 to 30 characters")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
