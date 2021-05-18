# dice-alfredworkflow

<p align='center'><img src="./pngegg.png" width="144">

A workflow to roll a dice/dices for fun.

## Usage

Type `roll` to trigger workflow, then type your quest and dice set (ndn).
For example,

```
roll "How long should I read this" "1d100"
```

will roll one d100 dice for your quest, "How long ..."
Output in alfred:

```
How long should I read this
Each dice: 81, sum: 81
```

## Requirements

`pip install dice` or `pip3 install dice`

## Necessary configuration

After adding the workflow to alfred, please change the python path in `Script filter` to your own.

E.g., `/opt/homebrew/bin/python3`, `/usr/local/bin/python3`
