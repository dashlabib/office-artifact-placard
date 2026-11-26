# Office Artifacts: The One-Line Placard Contest

Entry for the make.fun bounty `u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2`.

`main.py` writes a single-line museum placard — a stapler recast as an
ancient artifact, complete with catalogue date, material, and donor — to
`entry.txt` in the output directory.

## Run

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. Override the directory with
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/placard-out python3 main.py
```

Python 3.13, standard library only, no network. The output is one fixed,
deterministic line (163 characters).
