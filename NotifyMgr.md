## What is debugging?

In this context, it simply refers to the process of logging information about Toontown's logic through Panda3D's `Notify` class. This can be done through external files or command prompt messages (or a combination thereof).

## Why isn't `Notify` enough?

There are two primary issues with Panda3D's stock `Notify` class:

- It lacks flexibility; by default you can only control logging at the project and module level. This makes focusing on specific areas difficult.
- It doesn't support any in-game debugging.

## How does `NotifyMgr` address these issues?

`NotifyMgr` acts as a wrapper around `Notify` which adds more advanced control. Central to its functionality is the notion of "test suites," (defined by JSON objects) which allow the user to create (and easily switch between) groupings of messages about a particular aspect of the game's logic. This gives the user control at the project, module, method and individual message levels.

Here's an example test suite:


```json
{
    "default":
    {
        "files": [],
        "methods": []
    },
    "lure":
    {
        "files": ["BattleCalculatorAI"],
        "methods": ["__calcToonAtkHit", "__addLuredSuitInfo"]
    },
    "knockback":
    {
        "files": ["BattleCalculatorAI"],
        "methods": ["__addDmgToBonuses", "__processBonuses", "__postProcessToonAttacks", "__initRound"]
    },
    "cog-acc":
    {
        "files": ["BattleCalculatorAI", "SuitBattleGlobals"],
        "methods": ["__suitAtkHit", "pickSuitAttack", "__calcSuitAtkHp", "__calcSuitTarget"]
    }
}
```

`default` will display all debug messages, while the other suites will only display messages in their specified methods. To set the active suite, either of the following can de done:

- Add `suite <suite name>` to the config file.
- Say `~config suite <suite name>` in-game.

To configure the messages themselves, you first need to construct `NotifyMgr` with an instance of `Notify` inside the desired class `__init__` method:

```python
from toontown.debug import NotifyMgr

self.notifyMgr = NotifyMgr.NotifyMgr(self.notify)
```

From here, there are three use cases:

- Regular logging:

```python
self.notifyMgr.log("attack is Lure")
```

This is equivalent to `self.notify.debug`, which means all configuration settings work the same way (levels, external files, etc).

- Regular + in-game:

```python
self.notifyMgr.log("attack is Lure", whisper=True)
```

In addition to behaving like the previous option, this will also send the message to all toons via an in-game whisper.

- Suite-specific:

```python
self.notifyMgr.log("attack is Lure", suites=["lure"])
```

This will ensure that the above message is only logged when either the `lure` or `default` suites are active, even if another suite includes the message's encompassing method. This is particularly useful for organizing large, multipurpose methods.
