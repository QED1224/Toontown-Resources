## LoggerPlus

A simple logging utility for Toontown.

## Configuration

There are two steps to configuring `LoggerPlus`.

- Creating your test suites in debugging.json:

```json
{
    "lure":
    {
        "BattleCalculatorAI": ["__calcToonAtkHit", "__addLuredSuitInfo"]
    },
    "knockback":
    {
        "BattleCalculatorAI": ["__applyToonAttackDamages", "__addDmgToBonuses", "__processBonuses", "__postProcessToonAttacks", "__initRound"],
        "DistributedBattleBaseAI": ["__adjustDone", "addSuit"]
    },
    "cog-acc":
    {
        "BattleCalculatorAI": ["__suitAtkHit", "__calcSuitAtkHp", "__calcSuitTarget"],
        "SuitBattleGlobals": ["pickSuitAttack"]
    }
}
```

- The Panda3D configuration file (.prc):

    - Setting the active suite.
    
    ```
    suite <suite name>
    ```
    This can also be done by saying `~config suite <suite name>` in-game.
    
    - Optionally specifying an output file.
    
    ```
    output-file <filename>
    ```

## Usage

```python
from debug.LoggerPlusGlobal import logger

logger.log(msg, whisper=False, whisperOnly=False, suites=[])
```

- `msg`: The message to be logged.
- `whisper` (optional): If True, `msg` will also be sent via an in-game whisper.
- `whisperOnly` (optional): If True, `msg` will only be sent via an in-game whisper.
- `suites` (optional): A list of test suites that `msg` is associated with. If provided, it will ensure that that `msg` is only logged when one of its suites is active, even if another suite includes the message's encompassing method.
