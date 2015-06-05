# Contents <a name="contents"></a>
- [Introduction](#intro)
- [Core Knowledge](#core-knowledge)
    - [Toon Attack Accuracy](#atk-accuracy)
    - [Cog Attack Accuracy](#cog-atk-accuracy)
    - [Fishing](#fishing)
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
- [C.F.O.](#cfo)
    - [How was the C.F.O. reward chosen?](#cfo-1)
- [C.J.](#cj)
    - [How was the C.J. reward chosen?](#cj-1)
- [C.E.O.](#ceo)
- [Misc](#misc)
    - [Do some Shopkeepers sell more accurate gags?](#misc-1)
- [Credits](#credits)

# Introduction <a name="intro"></a>
[[back to top](#contents)]

**This guide is still a work-in-progress; some key information is missing from currently present sections.**

# Core Knowledge <a name="core-knowledge"></a>
[[back to top](#contents)]

## Toon Attack Accuracy <a name="atk-accuracy"></a>

`atkAcc` is a percentage which represents the likelihood of an attack performing to its highest degree. This is used in two ways:

1. For Lure SOS cards, it's used when calculating the odds that cogs "wake up early" each round.
2. It's used when calculating the value of `atkHit`, which is a boolean value that represents whether or not an attack hit.

### Special Cases

Fires, Trap and non-Drop/Lure SOS cards have 95%, 100% and 95% accuracy respectively. In addition, all three are always assigned an `atkHit` of 1, which means they are *guaranteed* to hit.

### Equation

A gag's overall accuracy is calculated using the following equation:

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

For all non-Lure gags, `propAcc` is simply the above pre-defined `AvPropAccuracy` value.

For Lure gags, `propAcc` is initially assigned its `AvPropAccuracy` value, then if the toon has Lure trees planted at a level greater than or equal to the gag level they're using **or** there's an active Lure interactive prop, `propAcc` is re-assigned a value from `AvLureBonusAccuracy`.

#### `trackExp`

`trackExp` is determined based on two factors: `toonExpLvl` and `exp`.

The following pseudocode outlines how `toonExpLvl` and `exp` are calculated:

<input type="text" id="name" name="name"/>

```python
AttackExpPerTrack = [0, 10, 20, 30, 40, 50, 60]

toonExpLvl = 0
for amount in Levels[track]: # Preset experience levels.
    if experience[track] >= amount: # The toon's experience level.
        toonExpLvl = Levels[track].index(amount) # A value between 0 and 6.

exp = AttackExpPerTrack[toonExpLvl]
if track == HEAL: # If the track is Toon-up, `exp` is halved.
    exp = exp * 0.5
trackExp = exp
```

Now, once the current attack's `trackExp` is calculated, every other slated attack is checked like so:

```python
for otherAtk in toonAtkOrder: # For each toon's ID...
    if otherAtk != attack[TOON_ID_COL]: # If `otherAtk` doesn't match the ID for the above attack...
        nextAttack = toonAttacks[currOtherAtk] 
        nextAtkTrack = getActualTrack(nextAttack) # The attack track (Lure, Drop, etc.)
        if atkTrack == nextAtkTrack and attack[TGT_COL] == nextAttack[TGT_COL]: # If the tracks and targets match...
            currTrackExp = toonTrackExp(nextAttack[TOON_ID_COL], atkTrack) # The `exp` for `nextAttack`.
            trackExp = max(currTrackExp, trackExp) # `trackExp` is assigned the largest `exp`.
```
So, if multiple toons use the same gag track on the same cog, the highest `trackExp` is used in the `atkAcc` calculations for all of them.

#### `tgtDef`

In Toon-up calculations, `tgtDef` is always 0. For the other tracks, it's assigned the defense value of the strongest cog among the attack's `targetList`. In other words, multi-cog attacks will always face the strongest `tgtDef` available since every active cog is in their `targetList`. For single-cog attacks it's based on the specific cog the attack has targeted.

Here's a summary of all possible defense values:

| Cog Level |  Defense |
|:---------:|:--------:|
|     1     |     2    |
|     2     |     5    |
|     3     |    10    |
|     4     | 12/15* |
|     5     | 15/20* |
|     6     |    25    |
|     7     |    30    |
|     8     |    35    |
|     9     |    40    |
|     10    |    45    |
|     11    |    50    |
|     12    |    55    |

*Tier 1 cogs (i.e., Cold Callers and Flunkies) have the lower value.

#### `bonus`

There are two possible sources of bonus: multiple hits on the same cog and the Lured Ratio. 

The former is simply 20 * [number of previous hits in the current round], given that the **previous attack hit**, **the previous was not the same track as the current** and one of the following is true:

- the *previous* attack affected the group; or
- the *current* attack affects the group; or
- the *current* and *previous* attacks affect the same target.

The latter is calculated like so:

```python
luredRatio = [number of cogs lured] / [total cogs]
accAdjust = 100 * luredRatio
atkAcc += accAdjust
```
So, for example, if there are 4 cogs in battle and two of them are lured, the bonus is:

```python
luredRatio = 2 / 4 = 0.5
100 * luredRatio = 50
atkAcc = atkAcc + 50
```
(Note: The Lured Ratio bonus does not apply to Lure, Toon-up or Drop gags.)

### Hit or Miss: the impact of `randChoice` <a name="hit-or-miss"></a>

Once we've calculated an attacks accuracy (`atkAcc`), we need to determine whether or not it will hit its intended target. This is decided by the value of `randChoice`, which is simply a pseudorandom integer between 0 and 99 (0 <= x < 99, to be exact).

If `randChoice` is less than `atkAcc`, the attack will hit. Otherwise, the attack will miss. It's important to note, however, that `atkAcc` is capped at 95 -- so, any gag which wasn't mentioned in the Special Cases section in [Attack Accuracy](#atk-accuracy) can miss.

#### Special Cases

For all SOS Cards, `randChoice` is assigned 0.

## Cog Attack Accuracy <a name="cog-atk-accuracy"></a>

The following three sections outline the calculations that are performed for each active cog in battle.

### Which attack will be used?

There are two variables used in the calculation of `atk` (the attack to be used): `theSuit` and `attacks`. The former represents the cog being used in the calculation, while the latter is a tuple containing the information for each of `theSuit`'s possible attacks.

Once `theSuit` and `attacks` are assigned, the `pickSuitAttack` function uses the following process to determine which attack will be used:

1. Generate a pseudorandom integer `randNum` such that 0 <= `randNum` < 99 and set a variable `attackNum` to `None`.
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

If the selected cog attack is a group attack, all active toons will be attacked. For single-toon attacks, 75% percent of the time the following algorithm is used to select a toon:

1. Store the total amount of damage done by the active toons in a variable `totalDamage`.
2. In a list, `dmgs`, store the relative contributions by each toon (contributed / `totalDamage` * 100).
3. Generate a pseudorandom integer `randNum` such that 0 <= `randNum` < 99.
4. Loop over `dmgs`, summing the relative contributions by each toon. This sum is stored in a variable `count`.
5. On each iteration, check if `randNum` is less than `count`
    - if it is, return an integer representing the number of iterations (that is, 0 for the first, 1 for the second, etc). In other words, a toon's damage contributions are directly proportional to its chance of being selected in this step.
    - if it's not, continue looping.
6. If no toon was found by the above, a toon is selected at random. This, for example, could happen when a large pseudorandom integer is generated, but the battle damage is evenly distributed.

In the other 25% of time, a toon is simply selected at random.

### Will the attack hit?

To determine this, a pseudorandom integer `randChoice` is generated such that 0 <= `randChoice` < 99. If `randChoice` is less than the cog attack's accuracy, the cog attack will hit. Otherwise it will miss.

(Attack accuracy/damage summary to be added.)

## Fishing <a name="fishing"></a>

# Toon-up <a name="toon-up"></a>
[[back to top](#contents)]

## Did using Toon-up have any impact on other gag's damage or accuracy? <a name="tu-1"></a>

### Hypothesis

Yes, Toon-up added a multi-hit-same-target bonus to `atkAcc` subject to the conditions outlined in the [bonus section](#bonus).

### Interpretation

Considering the conditions outlined in the [bonus section](#bonus), Toon-up would increase another gag's accuracy when one of the following was true:

- The Toon-up gag affected the group; or
- The attack gag affected the group; or
- Both gags affected the group.

For example, there would be no bonus applied if there were two toons in battle, and they used Pixie Dust and Fruit Pie Slice because neither is a group attack.

(Note: it appears that needing Laff was not a prerequisite for a Toon-up accuracy bonus.)


# Trap <a name="trap"></a>
[[back to top](#contents)]

## Did using Trap give Lure an accuracy boost? <a name="trap-1"></a>

Yes, Trap gags always count as a hit on the cog, regardless if the Trap is actually triggered or not. If one again considers the conditions in the [bonus section](#bonus), Trap meets the following conditions.

- It is not the same track as Lure;
- It always counts as a hit on the target

Now, one of the following must also be true:

- Both Lure and Trap are single-cog, and the target is the same.
- The Trap is multi-cog.
- The Lure is multi-cog.

So, the only scenario in which Trap will not give Lure an accuracy boost is if both Lure and Trap are single-cog, and the target is different.

Multiple Traps do give multiple boosts, with an accuracy boost of up to +60 to the Lure being possible. Of course, this requires multiple cogs in play for the Traps to be layed out.

### Battle Simulations

- [TNT & Big Magnet (single target)](http://pastebin.com/r2nq09PP)
- [2 Trapdoors & Small Magnet (2 targets)](http://pastebin.com/GaWL1GHT)
- [1 TNT, 2 Trapdoors & Small Magnet (3 targets)](http://pastebin.com/JSm1Nz9S)

## Did Trap provide an accuracy bonus to other gag tracks, even when not activated? <a name="trap-2"></a>

Yes, Trap did give an accuracy boost to other gag tracks as well. Even when not activated, Trap always counts as a hit on the cog. It would still meet the conditions given in the [bonus section](#bonus), thus a +20 accuracy boost to the next gag targeting the cog. 

### Battle Simulations

- [Trapdoor & Grand Piano](http://pastebin.com/KUmPsjuS)

## Did Trap's accuracy bonus and Organic Lure stack up? <a name="trap-3"></a>

Yes, Organic Lure and the accuracy boost Trap provides do stack up. As listed in the [`AvLureBonusAccuracy`](#AvLureBonusAccuracy) chart, each Organic Lure gag gains +10 propAcc points compared to its original values. In combination with the +20 a single Trap would provide, this would combine for a total of +30 overall accuracy points.

### Battle Simulations

- [Organic Small Magnet (single target)](http://pastebin.com/EEW7qXAn)
- [TNT & Organic Small Magnet (single target)](http://pastebin.com/s36873Qm)

# Lure <a name="lure"></a>
[[back to top](#contents)]

## What was the impact of using multiple Lure gags? <a name="lure-1"></a>

### Hypothesis

- When two lure gags were picked, the result of the weakest was calculated first.
- There were two different options for the second gag:
    + The first Lure's result was applied to the second. However, when calculating whether or not the first would hit, the `trackExp` of the strongest gag was used.
    + Each Lure gag was calculated independently; that is, it was possible for one to hit and the other to miss.

The first option was applied when these conditions were met:

- the gag tracks were the same and the target cog was the same; or
- the gag track was Lure and one of the following was true
    + the second Lure gag was single-cog and the first hit; or
    + the second Lure gag was multi-cog.

The second option would be applied when the second Lure gag was single-cog and the first missed.

### Interpretation

Using multiple Lure gags (of varying levels) was only beneficial in two situations:

- While training Lure, since the highest gag's `trackExp` would be applied to the weaker gag.
- If the weaker Lure was multi-cog and the stronger Lure was single-cog (i.e., Small Magnet and $10 Bill). In this case, there seemed to have been two options:
    + If the multi-cog Lure hit, the single-cog Lure did as well.
    + If the multi-cog Lure missed, the single-cog Lure was evaluated independently (so its accuracy wasn't lowered).

If multiple toons with the same experience level in Lure (i.e., maxed) used the same Lure gag, there was no impact on accuracy.

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

### Hypothesis

To determine whether or not a gag will hit, variables `randChoice` and `atkAcc` are compared as follows:

```python
if randChoice < acc:
    # HIT            
else:
    # MISS
```

(See Core Knowledge for definitions of `atkAcc` and `randChoice`.)

When a Lureless toon uses Lil' Oldman, Nancy Gas or Stinky Ned, `atkAcc` has a minimum value of 15 (this occurs against a level 12 cog):

```
atkAcc = propAcc + trackExp + tgtDef + [optional bonus] -> attackAcc = 70 + 0 + (-55) + 0 = 15
```

This means that `randChoice` would have to exceed 15 for the SOS to miss; however, as seen in Core Knowledge, `randChoice` is always assigned 0 when an SOS card is used.

### Interpretation

3 - 5 star Lure SOS cards were guaranteed to hit.

### Battle Simulations

## Did being Lureless impact the number of rounds Lure SOS cards would hold for? <a name="vp-2"></a>

### Hypothesis

Yes, cogs were more likely to "wake up" early if the caller was Lureless. The probability associated with this event is called a cogs `wakeupChance`, which is calculated as follows:

```python
wakeupChance = 100 - attackAcc * 2
```

`attackAcc` is calculated according the following formula (see Core Knowledge):

```python
attackAcc = propAcc + trackExp + tgtDef
```

This means that there are essentially two constants: `propAcc` (which is 70 for Lil' Oldman, Nancy Gas and Stinky Ned) and `trackExp` (which is 0 for a Lureless toon). With this in mind, we can calculate base probabilities by the value of `tgtDef`.

Cog levels 1 - 5 have a maximum `tgtDef` of 20, which means that they also have a maximum `wakeupChance` of 0. So, Lil' Oldman, Nancy Gas and Stinky Ned should always hold for 4 rounds when the highest cog is less than or equal to level 5.

For cog levels 6 - 12, we can establish base probabilities as follows,

```
6: attackAcc = 70 + 0 + (-25) = 45; wakeupChance = 100 - 45 * 2 = 10
7: attackAcc = 70 + 0 + (-30) = 40; wakeupChance = 100 - 40 * 2 = 20
8: attackAcc = 70 + 0 + (-35) = 35; wakeupChance = 100 - 35 * 2 = 30

...

12: attackAcc = 70 + 0 + (-55) = 15; wakeupChance = 100 - 15 * 2 = 70
```

Since 3 - 5 star Lure SOS cards are guaranteed to hit, the above probabilities represent the chance that the cogs will wake up after one round. Now, to calculate probabilities for the subsequent rounds, we may apply the Rule of Multiplication:

>The probability that Events A and B both occur is equal to the probability that Event A occurs times the probability that Event B occurs, given that A has occurred: P(A ∩ B) = P(A) P(B|A)

(Source: [Probability Rules](http://stattrek.com/probability/probability-rules.aspx).)

However, given that each round is calculated independent of any prior results, we note that P(B|A) = P(B). Thus, the probabilities can summarized as the following (note that the chance a cog stays lured is the *complement* of its `wakeupChance`):

|   | 1 - 5 | 6     | 7     | 8     | 9     | 10    | 11    | 12    |
|---|-------|-------|-------|-------|-------|-------|-------|-------|
| 1 |       |       |       |       |       |       |       | 100%  |
| 2 |       | 90.0% | 80.0% | 70.0% | 60.0% | 50.0% | 40.0% | 30.0% |
| 3 |       | 81.0% | 64.0% | 49.0% | 36.0% | 25.0% | 16.0% | 9.00% |
| 4 | 100%  | 72.9% | 51.2% | 34.3% | 21.6% | 12.5% | 6.40% | 2.70% |

(Only applicable to 3 - 5 star Lure SOS cards.)

### Interpretation

Being Lureless significantly devalues Lure SOS cards.

### TODO

- Verify the impact of any optional bonus on SOS cards
- Update section to include all SOS Lure cards (not just 3 - 5 star) 

### Battle Simulations

- [Maxed Lure; Lil' Oldman; Level 12 cog](http://pastebin.com/pr9LVZZ8)
- [Lureless; Lil' Oldman; Level 12 cog](http://pastebin.com/q8Q51Fm3)

# C.F.O. <a name="cfo"></a>

## How was the C.F.O. reward chosen? <a name="cfo-1"></a>

Both the overall type (i.e., Toon-up) and the subtype (i.e., +80) of the Unite were selected at random.

# C.J. <a name="cj"></a>

## How was the C.J. reward chosen? <a name="cj-1"></a>

The first step in choosing a Summon was to establish a `preferredSummonType`. This was done in two steps:

- The suit type was selected at random. This was known as the `preferredDept`.
- The Summon type was selected at random with the following odds: 70% chance for a cog, 27% chance for a building and 3% for an invasion.

The second step was to check for toons who already had the `preferredSummonType`. For those that did, the following algorithm was used to choose another Summon:

- Using the `preferredDept` and a cog level based on the battle difficulty, try to give the toon a cog, building or invasion (in that order).
- Using a cog level based on the battle difficulty, loop over every cog suit and try to give the toon a cog, building or invasion (in that order).
- Give the toon the weakest possible reward, checking suits in the following order: Boss, Law, Cash, Sell.
- If the toon has all possible Summons, give them nothing.


# C.E.O. <a name="ceo"></a>

# Misc <a name="misc"></a>
[[back to top](#contents)]

## Do some Shopkeepers sell more accurate gags? <a name="misc-1"></a>

### Hypothesis

No, there's no evidence that Shopkeepers had any impact on gag accuracy.

# Credits <a name="credits"></a>
[[back to top](#contents)]


