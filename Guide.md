# Contents <a name="contents"></a>
- [Introduction](#intro)
- [Core Knowledge](#core-knowledge)
    - [Toon Attack Accuracy](#atk-accuracy)
    - [Cog Attack Accuracy](#cog-atk-accuracy)
    - [Doodle Training and Tricks](#doodle-t&t)
    - [Fishing and Probability](#fish-prob)
- [Toon-up](#toon-up)
    - [Did using Toon-up have any impact on other gag's damage or accuracy?](#tu-1)
- [Trap](#trap)
    - [Did using Trap give Lure an accuracy boost?](#trap-1)
    - [Did Trap provide an accuracy bonus to other gag tracks, even when not activated?](#trap-2)
    - [Did Trap's accuracy bonus and Organic Lure stack up?](#trap-3)
- [Lure](#lure)
    - [What was the impact of using multiple Lure gags?](#lure-1)
- [Sound](#sound)
- [Throw](#throw)
- [Squirt](#squirt)
- [Drop](#drop)
- [V.P.](#vp)
    - [Did being Lureless impact the accuracy of Lure SOS cards?](#vp-1)
    - [Did being Lureless impact the number of rounds Lure SOS cards would hold for?](#vp-2)
    - [How did the V.P. choose which attack to use?](#vp-3)
    - [How did the V.P. choose which toon to attack?](#vp-4)
    - [Was there a way to predict when the undercarriage would open?](#vp-5)
- [C.F.O.](#cfo)
    - [How was the C.F.O. reward chosen?](#cfo-1)
    - [How did the C.F.O. choose which toon to attack?](#cfo-2)
- [C.J.](#cj)
    - [How was the C.J. reward chosen?](#cj-1)
    - [How did the C.J. decide when to jump?](#cj-2)
    - [How did the prosecution choose which toon to attack?](#cj-3)
    - [How is the scale related to the jury?](#cj-4)
- [C.E.O.](#ceo)
    - [How did the C.E.O. choose which attack to use?](#ceo-1)
    - [How did the C.E.O. choose which toon to attack?](#ceo-2)
- [Fishing](#fishing)
- [Misc](#misc)
    - [Did some Shopkeepers sell more accurate gags?](#misc-1)
    - [When multiple gags of the same track were used on the same cog, how was accuracy calculated?](#misc-2)
    - [Was it possible for two gags of the same track, aiming for the same cog, to have different hit/miss results?](#misc-3)
    - [Did doodle tricks count as a stun in battle?](#misc-4)
- [Credits](#credits)

# Introduction <a name="intro"></a>
[[back to top](#contents)]

**This guide is still a work-in-progress; some key information is missing from currently present sections.**

The information in this guide is primarily based on the source code of Toontown Online (timestamped 2013-07-02 T 6:22PM). It does not guarantee accuracy with regard to any Toontown private servers that have modified the battle system from Toontown Online.

# Core Knowledge <a name="core-knowledge"></a>
[[back to top](#contents)]

## Toon Attack Accuracy <a name="atk-accuracy"></a>

`atkAcc` is a percentage which represents the likelihood of an attack performing to its highest degree. This is used in two ways:

1. For Lure SOS cards, it was used when calculating the odds that cogs "wake up early" each round.
2. It was used when calculating the value of `atkHit`, which was a boolean value that represented whether or not an attack hit.

### Special Cases

Fires, Trap and non-Drop/Lure SOS cards have 95%, 100% and 95% accuracy respectively. In addition, all three are always assigned an `atkHit` of 1, which means they were *guaranteed* to hit.

### Equation

A gag's overall accuracy was calculated using the following equation:

```python
atkAcc = propAcc + trackExp + tgtDef + bonus
```

#### `propAcc`

**AvPropAccuracy (Gag track vs. Gag level):**

|         |  1 |  2 |  3 |  4 |  5 |  6 |  7  |
|:---------:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| Toon-up |  - |  - |  - |  - |  - | 70 | 100 |
| Trap    |  - | -  | -  | -  | -  | -  |  0  |
| Lure    | 50 | 50 | 60 | 60 | 70 | 70 | 100 |
| Sound   | -  | -  | -  | -  | -  | -  | 95  |
| Throw   | -  | -  | -  | -  | -  | -  | 75  |
| Squirt  | -  | -  | -  | -  | -  | -  | 95  |
| Drop    | -  | -  | -  | -  | -  | -  | 50  |

**AvLureBonusAccuracy:** <a name="AvLureBonusAccuracy"></a>

|      |  1 |  2 |  3 |  4 |  5 |  6 |  7  |
|------|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| Lure | 60 | 60 | 70 | 70 | 80 | 80 | 100 |

For all non-Lure gags, `propAcc` was simply the above pre-defined `AvPropAccuracy` value.

For Lure gags, `propAcc` was initially assigned its `AvPropAccuracy` value, then if the toon had Lure trees planted at a level greater than or equal to the gag level being used **or** there was an active Lure interactive prop, `propAcc` was re-assigned a value from `AvLureBonusAccuracy`.

#### `trackExp` <a name="trackExp"></a>

`trackExp` was calculated according to the following:

```
 trackExp = [highest gag level in track - 1] * 10
```

If the track was Toon-up, the above result was halved. 

This was repeated for every gag within a particular track. So, if multiple toons used the *same gag track* on the *same cog*, the highest `trackExp` was used in the `atkAcc` calculations for all of them. The latter requirement is particularly important: In order for weaker gags to inherit an increased `trackExp`, the target(s) of the weaker and stronger gags had to be the same. 

#### `tgtDef`

In Toon-up calculations, `tgtDef` was always 0. For the other tracks, it was assigned the defense value of the strongest cog among the attack's `targetList`. In other words, multi-cog attacks always faced the strongest `tgtDef` available since every active cog was in their `targetList`. For single-cog attacks it was based on the specific cog the attack had targeted.

Here's a summary of all possible defense values:

| Cog Level |  1 |  2 |  3  |    4    |    5    |  6  |  7  |  8  |  9  |  10 |  11 |  12 |
|:---------:|:--:|:--:|:---:|:-------:|:-------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **tgtDef** | -2 | -5 | -10 | -12/-15* | -15/-20* | -25 | -30 | -35 | -40 | -45 | -50 | -55 |

*Tier 1 cogs (i.e., Cold Callers and Flunkies) had the less negative value.

#### `bonus`

There were two possible sources of bonus: PrevHits and the Lured Ratio. 

In order for PrevHits to be applied, the followings conditions had to be met

- The previous attack hit; **and**
- The previous attack was not the same track as the current; **and**
- The previous attack affected the group; **or**
- The current attack affects the group; **or**
- The current and previous attacks affect the same target.

Assuming the above was met, PrevHits was calculated like so:

```
20 * [number of previous hits to a given cog in the current round] 
```

The Lured Ratio was calculated like so:

```
luredRatio = ([number of cogs lured] / [total cogs]) * 100
```
(Note: The Lured Ratio bonus does not apply to Lure, Toon-up or Drop gags.)

### Hit or Miss: the impact of `randChoice` <a name="hit-or-miss"></a>

Once we've calculated an attacks accuracy (`atkAcc`), we need to determine whether or not it will hit its intended target. This was decided by the value of `randChoice`, which was simply a pseudorandom integer between 0 and 99.

If `randChoice` was less than `atkAcc`, the attack hit. Otherwise, the attack missed. It's important to note, however, that `atkAcc` was capped at 95 -- so, any gag which wasn't mentioned in the Special Cases section in [Attack Accuracy](#atk-accuracy) could miss.

#### Special Cases

For all SOS Cards, `randChoice` was assigned 0.

## Cog Attack Accuracy <a name="cog-atk-accuracy"></a>

The following three sections outline the calculations that were performed for each active cog in battle.

### Which attack will be used?

There are two variables used in the calculation of `atk` (the attack to be used): `theSuit` and `attacks`. The former represented the cog being used in the calculation, while the latter was a tuple containing the information for each of `theSuit`'s possible attacks.

Once `theSuit` and `attacks` are assigned, the `pickSuitAttack` function used the following process to determine which attack would be used:

1. Generate a pseudorandom integer `randNum` such that 0 <= `randNum` <= 99 and set a variable `attackNum` to `None`.
2. Loop through each possible attack, summing the frequencies associated with `theSuit`'s level. This sum is stored in a variable `count`.
3. On each iteration, check if `randNum` is less than `count`.
    - if it is, set `attackNum` to an integer representing the number of iterations (that is, 0 for the first, 1 for the second, etc).
    - if it's not, continue looping.
4. Return `attackNum`

Considering the above, we may establish the following tables.

**Cog Level vs. Attack Usage Probability**

| Flunky  | Clip On Tie | Pound Key | Shred |
|:---:|:-------------:|:---------:|:-----:|
| 1 |     42%     |    30%    |  28%  |
| 2 |    32.5%    |    35%    | 32.5% |
| 3 |     24%     |    40%    |  36%  |
| 4 |    16.5%    |    45%    | 38.5% |
| 5 |     10%     |    50%    |  40%  |

(More tables to be added.)

#### Example calculations

- [Level 1 Flunky](http://pastebin.com/wANyHgsx)

### Which toon(s) will be attacked?

If the selected cog attack is a group attack, all active toons would be attacked. For single-toon attacks, 75% percent of the time the following algorithm was used to select a toon:

1. Store the total amount of damage done by the active toons in a variable `totalDamage`.
2. In a list, `dmgs`, store the relative contributions by each toon (contributed / `totalDamage` * 100).
3. Generate a pseudorandom integer `randNum` such that 0 <= `randNum` <= 99.
4. Loop over `dmgs`, summing the relative contributions by each toon. This sum is stored in a variable `count`.
5. On each iteration, check if `randNum` is less than `count`
    - if it is, return an integer representing the number of iterations (that is, 0 for the first, 1 for the second, etc). In other words, a toon's damage contributions are directly proportional to its chance of being selected in this step.
    - if it's not, continue looping.
6. If no toon was found by the above, a toon is selected at random. This, for example, could happen when a large pseudorandom integer is generated, but the battle damage is evenly distributed.

In the other 25% of time, a toon was simply selected at random.

### Will the attack hit?

To determine this, a pseudorandom integer `randChoice` was generated such that 0 <= `randChoice` <= 99. If `randChoice` was less than the cog attack's accuracy, the cog attack hit. Otherwise it missed.

(Attack accuracy/damage summary to be added.)

## Doodle Training and Tricks <a name="doodle-t&t"></a>

## Fishing and Probability <a name="fish-prob"></a>

# Toon-up <a name="toon-up"></a>
[[back to top](#contents)]

## Did using Toon-up have any impact on other gag's accuracy? <a name="tu-1"></a>

Yes, considering the conditions outlined in the [bonus section](#bonus), Toon-up would increase another gag's accuracy when one of the following was true:

- The Toon-up gag affected the group; or
- The attack gag affected the group; or
- Both gags affected the group.

(Note: it appears that needing Laff was not a prerequisite for a Toon-up accuracy bonus.)

# Trap <a name="trap"></a>
[[back to top](#contents)]

## Did using Trap give Lure an accuracy boost? <a name="trap-1"></a>

Yes, Trap gags always counted as a hit on the cog, regardless if the Trap was actually triggered or not. If one again considers the conditions in the [bonus section](#bonus), Trap met the following conditions.

- It is not the same track as Lure;
- It always counts as a hit on the target

Now, one of the following also needed to be true:

- Both Lure and Trap are single-cog, and the target is the same.
- The Trap is multi-cog.
- The Lure is multi-cog.

So, the only scenario in which Trap did not give Lure an accuracy boost was if both Lure and Trap were single-cog, and the target was different.

Multiple Traps did give multiple boosts, with an accuracy boost of up to +60 to the Lure being possible. Of course, this required multiple cogs to be in play for the Traps to be layed out.

### Battle Simulations

- [TNT & Big Magnet (single target)](http://pastebin.com/r2nq09PP)
- [2 Trapdoors & Small Magnet (2 targets)](http://pastebin.com/GaWL1GHT)
- [1 TNT, 2 Trapdoors & Small Magnet (3 targets)](http://pastebin.com/JSm1Nz9S)

## Did Trap provide an accuracy bonus to other gag tracks, even when not activated? <a name="trap-2"></a>

Yes, Trap did give an accuracy boost to other gag tracks as well. Even when not activated, Trap always counted as a hit on the cog. It would still meet the conditions given in the [bonus section](#bonus), thus a +20 accuracy boost to the next gag targeting the cog. 

### Battle Simulations

- [Trapdoor & Grand Piano](http://pastebin.com/KUmPsjuS)

## Did Trap's accuracy bonus and Organic Lure stack up? <a name="trap-3"></a>

Yes, Organic Lure and the accuracy boost Trap provides did stack up. As listed in the [`AvLureBonusAccuracy`](#AvLureBonusAccuracy) chart, each Organic Lure gag gains +10 propAcc points compared to its original values. In combination with the +20 a single Trap would provide, this would combine for a total of +30 overall accuracy points.

### Battle Simulations

- [Organic Small Magnet (single target)](http://pastebin.com/EEW7qXAn)
- [TNT & Organic Small Magnet (single target)](http://pastebin.com/s36873Qm)

# Lure <a name="lure"></a>
[[back to top](#contents)]

## What was the impact of using multiple Lure gags? <a name="lure-1"></a>

When two or more Lure gags were picked, the result of the weakest was calculated first using the highest possible value for `trackExp` according to the details outlined in [its section](#trackExp). From here, there were two options for all subsequent Lure gags:

1. If the current Lure gag was single-cog and the previous hit or the current Lure gag was multi-cog, the previous Lure's result was applied to the current.

2. If the current Lure gag was single-cog, the previous was multi-cog *and* the previous missed, the current was calculated independently. In other words, this was this only case in which sequential Lure gags could have different results.

In either case, rounds were stacked based on the Lure's target. So, multiple single-cog Lures only stacked rounds if they had the same target, while multiple multi-cog Lures always stacked across all cogs. If a combination of single- and multi-cog Lures were used, rounds only stacked on the target(s) which overlapped.

If multiple toons with the same experience level in Lure (i.e., maxed) used the same Lure gag, there was no impact on accuracy.

See the [section on multiple gag usage](#misc-2) for more general information.

### Battle Simulations

- [$1 Bill & $10 Bill (same target)](http://pastebin.com/rzUCvWPs)
- [$1 Bill & Hypno Goggles (single target)](http://pastebin.com/yNUrv0h7)
- [$1 Bill & Presentation (single target)](http://pastebin.com/qGZdyJUB)
- [Small Magnet & $10 Bill (single target)](http://pastebin.com/wagzTZfp)
- [Small Magnet & Big Magnet (single target)](http://pastebin.com/Saw5PygN)
- [Small Magnet & Hypno Goggles (single target)](http://pastebin.com/D9f7HZrn)

# Sound <a name="sound"></a>
[[back to top](#contents)]

# Throw <a name="throw"></a>
[[back to top](#contents)]

# Squirt <a name="squirt"></a>
[[back to top](#contents)]

# Drop <a name="drop"></a>
[[back to top](#contents)] 

# V.P. <a name="vp"></a>
[[back to top](#contents)]

## Did being Lureless impact the accuracy of Lure SOS cards? <a name="vp-1"></a>

Yes, a value of 0 was used for `trackExp` in all Lure SOS card accuracy calculations for Lureless toons (see [Toon Attack Accuracy](#atk-accuracy) for more information). In practice, this was only relevant for Des Traction and Dee Version, which *always* missed against level 11 and 12 cogs as seen below.

```
Level 11: atkAcc = 50 + 0 + (-50) = 0
Level 12: atkAcc = 50 + 0 + (-55) = -5
```

## Did being Lureless impact the number of rounds Lure SOS cards would hold for? <a name="vp-2"></a>

Yes, cogs were more likely to "wake up" early if the caller was Lureless. The probability associated with this event is called a cog's `wakeupChance`, which is calculated as follows:

```python
wakeupChance = 100 - atkAcc * 2
```
(See [Toon Attack Accuracy](#atk-accuracy) for information on `atkAcc`.)

With the above in mind, it can also be useful to think in terms of `wakeupChance`'s probabilistic complement: The probability that a given SOS card will hold for a specific number of rounds. In order to do so, we must apply the Rule of Multiplication:

>The probability that Events A and B both occur is equal to the probability that Event A occurs times the probability that Event B occurs, given that A has occurred: P(A ∩ B) = P(A) P(B|A)

(Source: [Probability Rules](http://stattrek.com/probability/probability-rules.aspx).)

However, given that each round is calculated independent of any prior results, we note that P(B|A) = P(B). Thus, the following equation can be used:

```python
Given (Max rounds - N) >= 0,

P(N rounds) = [1 - (wakeupChance / 100)] ^ (N - 1)
```

### Battle Simulations

- [Maxed Lure; Lil' Oldman; Level 12 cog](http://pastebin.com/pr9LVZZ8)
- [Lureless; Lil' Oldman; Level 12 cog](http://pastebin.com/q8Q51Fm3)

## How did the V.P. choose which attack to use? <a name="vp-3"></a>

Excluding the undercarriage which had different logic (see the following question), the V.P. had three attacks: Throw Gears, Gear Shower and Jump with usage odds of 4/6, 1/6 and 1/6 respectively. During normal mode, the V.P. would choose at random from these three.

Following dizziness, the V.P. would always use Gear Shower.

## How did the V.P. choose which toon to attack? <a name="vp-4"></a>

Throw Gears is the only attack which targeted a specific toon and the toon was selected at random.

## Was there a way to predict when the undercarriage would open? <a name="vp-5"></a>

Yes, the undercarriage would open every 9 seconds that the V.P. was not dizzy. The side it opened on and the direction of the gears were random.

# C.F.O. <a name="cfo"></a>
[[back to top](#contents)]

## How was the C.F.O. reward chosen? <a name="cfo-1"></a>

Both the overall type (i.e., Toon-up) and the subtype (i.e., +80) of the Unite were selected at random.

## How did the C.F.O. choose which toon to attack? <a name="cfo-2"></a>

At the start of the Crane Round, a list named `toonsToAttack` was created which contained the ID of every toon in the C.F.O. battle sorted randomly. Toons were then attacked according to this order: the toon at position 0 was attacked first and then its ID was appended to the end of the list. This cylcle repeated for the duration of the battle.

# C.J. <a name="cj"></a>
[[back to top](#contents)]

## How was the C.J. reward chosen? <a name="cj-1"></a>

The first step in choosing a Summon was to establish a `preferredSummonType`. This was done in two steps:

- The suit type was selected at random. This was known as the `preferredDept`.
- The Summon type was selected at random with the following odds: 70% chance for a cog, 27% chance for a building and 3% for an invasion.

The second step was to check for toons who already had the `preferredSummonType`. For those that did, the following algorithm was used to choose another Summon:

- Using the `preferredDept` and a cog level based on the battle difficulty, try to give the toon a cog, building or invasion (in that order).
- Using a cog level based on the battle difficulty, loop over every cog suit and try to give the toon a cog, building or invasion (in that order).
- Give the toon the weakest possible reward, checking suits in the following order: Boss, Law, Cash, Sell.
- If the toon has all possible Summons, give them nothing.

## How did the C.J. decide when to jump? <a name="cj-2"></a>

Every 15 seconds the C.J. had an 11% chance to jump. 

## How did the prosecution choose which toon to attack? <a name="cj-3"></a>

Every cycle, each prosecuting cog had a 50/50 chance to either (1) attack a toon or (2) hit the scale. If option 1 was selected, a toon was chosen at random from a list of all toons in the battle. 

## How is the scale related to the jury? <a name="cj-4"></a>

# C.E.O. <a name="ceo"></a>
[[back to top](#contents)]

## How did the C.E.O. choose which attack to use? <a name="ceo-1"></a>

## How did the C.E.O. choose which toon to attack? <a name="ceo-2"></a>

# Fishing <a name="fishing"></a>
[[back to top](#contents)]

# Misc <a name="misc"></a>
[[back to top](#contents)]

## Do some Shopkeepers sell more accurate gags? <a name="misc-1"></a>

No, there's no evidence that Shopkeepers had any impact on gag accuracy.

## When multiple gags of the same track were used on the same cog, how was accuracy calculated? <a name="misc-2"></a>

The first aspect that must be understood is how toon attacks were ordered, in which there were three steps:

1. The position of each toon in battle, from right to left, represents the initial attack order.
2. Order by track: Toon-up, Trap, Lure, Sound, Throw, Squirt and then Drop.
3. Order by gag level (lowest to highest) within each track.

From here, for all calculation purposes, attacks are considered in pairs (the previous attack and the current attack) within each track.

Now, we need to cover four more sub-cases:

1. Toon-up gags were always evaluated independently.
2. Lure gags were only evaluated independently when using a combination of multi- and single-cog Lures, and a multi-cog Lure was the lowest level ([see the multi-Lure section for details](#lure-1)). In all other cases, the result of the lowest Lure gag was applied to all subsequent Lures.
3. Sound gags always inherited the result of the lowest Sound gag used. 
4. For all other tracks, if the previous gag in the particular track had the same target as the current, the current inherited the result of the previous.

## Was it possible for two gags of the same track, aiming for the same cog, to have different hit/miss results? <a name="misc-3"></a>

Yes, considering the ordering process outlined in the previous section, if multiple gags of the same track and level were used, they were only ordered by toon ID within the particular track. This meant it was possible for "mismatches" to occur. For example, consider the following scenario with three toons (1 - 3) and two cogs (A and B):

- Toon 1 (ID = 1) uses a Safe on Cog A
- Toon 2 (ID = 2) uses a Safe on Cog B
- Toon 3 (ID = 3) uses a Safe on Cog A

Here, the attack order is 1, 2, 3 (by ID). This means that Toon 1's Safe is evaluated, then Toon 2's Safe is evaluated (but isn't assigned the result of 1 because it has a different target) and then Toon 3's Safe is evaluated (but isn't assigned the result of 2 because it has a different target). So, in this situation, it's possible for only one Safe to hit Cog A.

## Battle Simulations

- [3 Safes](http://pastebin.com/BhZ14ZL6)
- [3 Storm Clouds](http://pastebin.com/5fb8pbtA)

## Did doodle tricks count as a stun in battle? <a name="misc-4"></a>

# Credits <a name="credits"></a>
[[back to top](#contents)]

- Cell1234 (Patrick)
