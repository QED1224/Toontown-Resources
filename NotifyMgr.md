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
        "methods": [],
    },
    "cog-acc":
    {
        "files": ["BattleCalculatorAI", "SuitBattleGlobals"],
        "methods": ["__suitAtkHit", "pickSuitAttack", "__calcSuitAtkHp", "__calcSuitTarget"]
    }
}
```

`default` will display all debug messages, while `cog-acc` will only display those in the specified methods. To set the active suite, either of the following can de done:

- Manually edit the config file.
- Say `config suite <name>` in-game.

