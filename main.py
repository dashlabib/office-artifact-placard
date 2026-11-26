#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard for an ordinary office object,
recast as an ancient artifact, to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Python 3.13, standard library only, no network, deterministic output.
"""

import os

PLACARD = (
    "Stapler, c. 1994, pressed steel. Found in a manager's drawer beside "
    "47 resignation letters, each stapled to the next. Gift of the "
    "Department of Passive Aggression."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
