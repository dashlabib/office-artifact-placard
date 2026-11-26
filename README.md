[![make.fun · u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/dashlabib/office-artifact-placard/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/dashlabib/office-artifact-placard/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

# Office Artifacts: The One-Line Placard Contest

Entry for the make.fun bounty
[u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2).

`main.py` writes a single-line museum placard — a stapler recast as an
ancient artifact, complete with catalogue date, material, and donor — to
`entry.txt` in the output directory. Deterministic: one fixed line,
163 characters.

## Run

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. Override the directory with
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/placard-out python3 main.py
```

Python 3.13, standard library only, no network.
