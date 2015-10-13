## LoggerPlus

A simple logging utility for Toontown.

## Installation

1. Create debugging.json in your config directory.
2. Place the debug directory top-level in your Toontown directory (i.e., the same level as config).
3. See the Configuration and Usage sections below

\* Only tested on OS X, but it *should* support Windows and Linux too.

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

- Import from `LoggerPlusGlobal`:

     ```python
    from debug.LoggerPlusGlobal import logger
   ```

- `msg`: The message to be logged.

     ```python
    logger.log("This is a very detailed log message")
    ```

- `whisper` (optional): If True, `msg` will be sent via an in-game whisper in addition to external outputs.

     ```python
    logger.log("This is a very detailed log message", whisper=1)
    ```

- `whisperOnly` (optional): If True, `msg` will *only* be sent via an in-game whisper.
        
     ```python
    logger.log("Less detailed log message", whisperOnly=1)
    ```
    
    Since whispers have limited space, it can be useful to specify whisper-only versions of messages.

- `suites` (optional): A list of test suites that `msg` is associated with. If provided, it will ensure that that `msg` is only logged when one of its suites is active, even if another suite includes the message's encompassing method.

     ```python
    logger.log("This is a very detailed log message", suites=["suite1", "suite2"])
    ```
