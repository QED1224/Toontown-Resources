# Contents <a name="contents"></a>
- [Introduction](#intro)
- [Core Knowledge](#core-knowledge)
    - [Toon Attack Accuracy](#toon-atk-acc)
    - [Cog Attack Accuracy](#cog-atk-acc)
    - [Doodle Training and Tricks](#doodle-t&t)
    - [Fishing and Probability](#fish-prob)
- [Toon-up](#toon-up)
    - [Did using Toon-up have any impact on other gag's damage or accuracy?](#toon-up-1)
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
- [Cogs](#cogs)
    - [Which cog was the most powerful?](#cogs-1)
- [V.P.](#vp)
    - [Did being Lureless impact the accuracy of Lure SOS cards?](#vp-1)
    - [Did being Lureless impact the number of rounds Lure SOS cards would hold for?](#vp-2)
    - [How did the V.P. choose which attack to use?](#vp-3)
    - [How did the V.P. choose which toon to attack?](#vp-4)
    - [Was there a way to predict when the undercarriage would open?](#vp-5)
    - [Were the gag-related decreases in SOS card performance intentional?](#vp-6)
- [C.F.O.](#cfo)
    - [How was the C.F.O. reward chosen?](#cfo-1)
    - [How did the C.F.O. choose which toon to attack?](#cfo-2)
- [C.J.](#cj)
    - [How was the C.J. reward chosen?](#cj-1)
    - [How did the C.J. decide when to jump?](#cj-2)
    - [How did the prosecution choose which toon to attack?](#cj-3)
    - [How was the scale related to the jury?](#cj-4)
    - [What was the optimal scalers-to-stunners ratio?](#cj-5)
- [C.E.O.](#ceo)
    - [How did the C.E.O. choose which attack to use?](#ceo-1)
    - [How did the C.E.O. choose which toon to attack?](#ceo-2)
- [Fishing](#fishing)
- [Racing](#racing)
    - [Wall-riding: A track-by-track breakdown](#racing-1)
- [Golfing](#golfing)
- [Misc](#misc)
    - [Did some Shopkeepers sell more accurate gags?](#misc-1)
    - [When multiple gags of the same track were used on the same cog, how was accuracy calculated?](#misc-2)
    - [Was it possible for two gags of the same track, aiming for the same cog, to have different hit/miss results?](#misc-3)
    - [Did doodle tricks count as a stun in battle?](#misc-4)
    - [Did Fires count as a stun?](#misc-5)
- [Credits](#credits)
- [Appendix A: Cog Attack Frequencies](#appendix-a)
- [Appendix B: Cog Attack Damages](#appendix-b)
- [Appendix C: Cog Attack Accuracy Values](#appendix-c)

# Introduction <a name="intro"></a>
[[back to top](#contents)]

**This guide is still a work-in-progress; some key information is missing from currently present sections.**

The information in this guide is primarily based on the source code of Toontown Online. It does not guarantee accuracy with regard to any Toontown private servers that have modified the battle system from Toontown Online.

# Core Knowledge <a name="core-knowledge"></a>
[[back to top](#contents)]

## Toon Attack Accuracy <a name="toon-atk-acc"></a>

`atkAcc` is a percentage which represents the likelihood of an attack performing to its highest degree. This is used in two ways:

1. For Lure SOS cards, it was used when calculating the odds that cogs "wake up early" each round.
2. It was used when calculating the value of `atkHit`, which was a boolean value that represented whether or not an attack hit.

### Special Cases <a name="toon-atk-acc-1"></a>

Fires and Trap have 95% and 100% accuracy respectively. In addition, both are always assigned an `atkHit` of 1, which means they were *guaranteed* to hit.

### Equation <a name="toon-atk-acc-2"></a>

A gag's overall accuracy was calculated using the following equation:

```python
atkAcc = propAcc + trackExp + tgtDef + bonus
```

#### `propAcc` <a name="toon-atk-acc-3"></a>

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

#### `trackExp` <a name="toon-atk-acc-4"></a>

`trackExp` was calculated according to the following:

```
 trackExp = [highest gag level in track - 1] * 10
```

If the track was Toon-up, the above result was halved. 

This was repeated for every gag within a particular track. So, if multiple toons used the *same gag track* on the *same cog*, the highest `trackExp` was used in the `atkAcc` calculations for all of them. The latter requirement is particularly important: In order for weaker gags to inherit an increased `trackExp`, the target(s) of the weaker and stronger gags had to be the same. 

#### `tgtDef` <a name="toon-atk-acc-5"></a>

In Toon-up calculations, `tgtDef` was always 0. For the other tracks, it was assigned the defense value of the strongest cog among the attack's `targetList`. In other words, multi-cog attacks always faced the strongest `tgtDef` available since every active cog was in their `targetList`. For single-cog attacks it was based on the specific cog the attack had targeted.

Here's a summary of all possible defense values:

| Cog Level |  1 |  2 |  3  |    4    |    5    |  6  |  7  |  8  |  9  |  10 |  11 |  12 |
|:---------:|:--:|:--:|:---:|:-------:|:-------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **tgtDef** | -2 | -5 | -10 | -12/-15* | -15/-20* | -25 | -30 | -35 | -40 | -45 | -50 | -55 |

*Tier 1 cogs (i.e., Cold Callers and Flunkies) had the less negative value.

#### `bonus` <a name="toon-atk-acc-6"></a>

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

### Hit or Miss: the impact of `randChoice` <a name="toon-atk-acc-7"></a>

Once we've calculated an attacks accuracy (`atkAcc`), we need to determine whether or not it will hit its intended target. This was decided by the value of `randChoice`, which was simply a pseudorandom integer between 0 and 99.

If `randChoice` was less than `atkAcc`, the attack hit. Otherwise, the attack missed. It's important to note, however, that `atkAcc` was capped at 95 -- so, any gag which wasn't mentioned in the [Special Cases section](#toon-atk-acc-1) could miss.

#### Special Cases <a name="toon-atk-acc-8"></a>

For all SOS Cards, `randChoice` was assigned 0.

## Cog Attack Accuracy <a name="cog-atk-acc"></a>

The following three sections outline the calculations that were performed for each active cog in battle.

### Which attack will be used? <a name="cog-atk-acc-1"></a>

There were two variables used in the calculation of `atk` (the attack to be used): `theSuit` and `attacks`. The former represented the cog being used in the calculation, while the latter was a tuple containing the information for each of `theSuit`'s possible attacks. Also note that a "relative" cog level was used for frequency calculation purposes. This was calculated as follows.
```
relative level = cog level - base level
```
Where "cog level" was the actual level and "base level" was the lowest possible level. From here, the `pickSuitAttack` function used the following process to determine which attack would be used:

1. A pseudorandom integer `randNum` was generated such that 0 <= `randNum` <= 99.
2. The attack frequencies associated with `theSuit`'s relative level were then iteratively summed. This sum was stored in a variable `count`.
3. On each iteration, `randNum` was compared to `count`.
    - if `randNum` was less than `count`, `attackNum` was assigned an integer representing the number of completed iterations (starting at 0).
    - if `randNum` was greater than or equal to `count`, the loop continued.
4. `attackNum` was returned.

Let's look at an example. Here's the output of a simulation of the above algorithm for a Level 3 Yesman:

```
:SuitBattleGlobals(debug): Entering pickSuitAttack...
:SuitBattleGlobals(debug): attacks:
(('RubberStamp', (2, 2, 3, 3, 4), (75, 75, 75, 75, 75), (35, 35, 35, 35, 35)),
('RazzleDazzle', (1, 1, 1, 1, 1), (50, 50, 50, 50, 50), (25, 20, 15, 10, 5)),
('Synergy', (4, 5, 6, 7, 8), (50, 60, 70, 80, 90), (5, 10, 15, 20, 25)),
('TeeOff', (3, 3, 4, 4, 5), (50, 60, 70, 80, 90), (35, 35, 35, 35, 35)))
:SuitBattleGlobals(debug): suitLevel = 0
:SuitBattleGlobals(debug):
        randNum = 44
        count = 0
        index = 0
:SuitBattleGlobals(debug): Looping through attacks...
:SuitBattleGlobals(debug):
            count = 35
            index = 0
:SuitBattleGlobals(debug): 44 < 35?
:SuitBattleGlobals(debug):
            count = 60
            index = 1
:SuitBattleGlobals(debug): 44 < 60?
:SuitBattleGlobals(debug): picking RazzleDazzle
```

As you can see above,

- `RubberStamp` had a 35% chance of being selected (0 <= `randNum` < 35)
- `RazzleDazzle` had a 25% chance of being selected (35 <= `randNum` < 60)
- `Synergy` had a 5% chance of being selected (60 <= `randNum` < 65)
- `TeeOff` had a 35% chance of being selected (65 <= `randNum` < 99)

In addition, since `randNum` had an equal chance to be any integer between 0 and 99, we would have expected to see (roughly) the above percentages as the number of trials got sufficiently large. Here are the results of simulating a Level 3 Yesman choosing an attack 5000000 times:

```
Cog: Yesman
Level: 3
Trials: 5000000
RubberStamp: 1750610 (35.0122%)
RazzleDazzle: 1250705 (25.0141%)
Synergy: 249389 (4.98778%)
TeeOff: 1749296 (34.98592%)
```

So, for any cog, the probability that a given attack will be chosen is equal to the attack's frequency value as listed in [Appendix A](#appendix-a).

### Which toon(s) will be attacked? <a name="cog-atk-acc-2"></a>

Each active cog uses to following process to determine its target(s).

- If the selected cog attack was a group attack, all active toons were attacked (see previous section).
- If the current cog hadn't taken any damage or `randNum` was greater than 75, a toon was selected at random.

If neither of the above were true, the following algorithm was used to select a toon:

1. The total amount of damage done to the current cog was stored in a variable `totalDamage`.
2. The relative contributions by each toon (contributed / `totalDamage`) * 100 were stored in a list `dmgs`.
3. A pseudorandom integer `randNum` was generated such that 0 <= `randNum` <= 99.
4. The values in `dmgs` were then iteratively summed. This sum was stored in a variable `count`.
5. On each iteration, `randNum` was compared to `count`.
    - if `randNum` was less than `count`, an integer representing the number of completed iterations was returned (starting at 0). 
    - if `randNum` was greater than or equal to `count`, the loop continued.
6. If no toon was found by the above, a toon was selected at random.

`totalDamage` and `dmgs` were reset every round.

### Will the attack hit? <a name="cog-atk-acc-3"></a>

For every targeted toon, a pseudorandom integer `randChoice` was generated such that 0 <= `randChoice` <= 99. If `randChoice` was less than the cog attack's accuracy, the cog attack hit. Otherwise it missed.

A list of attack accuracy values can be seen at [Appendix C](#appendix-c).

## Doodle Training and Tricks <a name="doodle-t&t"></a>
[[back to top](#contents)]

## How was Doodle trick experience calculated? <a name="doodle-t&t-1"></a>

Doodle tricks had similarities to how gags gained experience. Each time a successful trick was performed, that trick would gain +20 experience points. Each trick required 10000 experience points to fully max the trick. 10000 / 20 would require the Doodle to perform 500 successful tricks, in order to max that particular trick. To max all tricks, it would require an overall total of 3500 successful tricks.

In addition, performing a successful trick would increase the `aptitiude` value of that trick by 0.002. When a trick was fully maxed, `aptitude` capped out at 1.0. To determine the `aptitude` value a doodle has, the following equation could be used.

```python
aptitude = trick experience / 10000
```

## Did Doodle tricks have base accuracy values to them? <a name="doodle-t&t-2"></a>

Yes, Doodle tricks had individual accuracy values for each trick. These values were used in determining the final accuracy value of the trick, referred to as `cutoff`. Below is a list of the base accuracy values for each trick. 

| Trick  | Base accuracy value | 
|:------:|:-------------:|
| Jump | 1.0 | 
| Beg | 0.9 |
| Play Dead | 0.8 |
| Rollover | 0.7 |
| Backflip | 0.6 |
| Dance | 0.5 |
| Speak | 0.4 | 

## How did the game determine if the Doodle would successfully perform the trick? <a name="doodle-t&t-3"></a>

To determine if a trick would be successful or not, the following equation could be used.

```python
cutoff = trickAcc * (minApt + ((maxApt - minApt) * aptitude))
```

`cutoff` is the end result of the following variables being calculated. `trickAcc` referred to the base accuracy value of the trick being used (see previous question). `minApt` and `maxApt` were predetermined values set by the Doodle's mood. If the Doodle was neutral, excited, playful or affectionate, `minApt = 0.5` and `maxApt = 0.97`. However, if the Doodle was bored, restless, lonely, sad, tired, hungry or angry, `minApt = 0.1` and `maxApt = 0.6`. `aptitude` was the value determined by taking the trick's experience / 10000.  

If the Doodle was tired either at the Estate or the battle selection screen, `cutoff` was multiplied by 0.5. 

If the Doodle had a negative mood at the Estate, but had a positive mood on the battle selection screen, `minApt` and `maxApt` would still equal 0.5 and 0.97 respectively. 

If the Doodle had negative moods in both the Estate and the battle selection screen, `minApt = 0.1` and `maxApt = 0.6`. However, `cutoff` would not be multiplied by 0.5 unless one of the negative moods was tired.

Once the final value of `cutoff` was determined, an pseudo-RNG called `randVal` generated a value between 0.0 and 1.0. If `cutoff` was greater than `randVal`, the Doodle would successfully perform the trick. Otherwise, the Doodle would not perform the trick.

Below is a table that shows the final `cutoff` value for each trick, assuming the doodle was maxed in said trick, and had no negative emotions on both the battle selection screen and the Estate.

| Trick  | `cutoff` value | 
|:------:|:-------------:|
| Jump | 0.97 | 
| Beg | 0.873 |
| Play Dead | 0.776 |
| Rollover | 0.679 |
| Backflip | 0.582 |
| Dance | 0.485 |
| Speak | 0.388 |

Based on the above table, it's possible to quantitatively compare the effectiveness of each trick. Consider the following:

```
Expected Laff = cutoff * Laff Given

0.970 * 10 = 9.7000 Laff (Jump)
0.873 * 12 = 10.476 Laff (Beg)
0.776 * 14 = 10.864 Laff (Play Dead)
0.679 * 16 = 10.864 Laff (Rollover)
0.582 * 18 = 10.476 Laff (Backflip)
0.485 * 20 = 9.7000 Laff (Dance)
0.388 * 22 = 8.5360 Laff (Speak)
```
As you can see, maxed Play Dead and Rollover are the most efficient tricks. Therefore Play Dead is likely the only trick worth training.

## Fishing and Probability <a name="fish-prob"></a>
[[back to top](#contents)]

# Toon-up <a name="toon-up"></a>
[[back to top](#contents)]

## Did using Toon-up have any impact on other gag's accuracy? <a name="toon-up-1"></a>

Yes, considering the conditions outlined in the [bonus section](#toon-atk-acc-6), Toon-up would increase another gag's accuracy when one of the following was true:

- The Toon-up gag affected the group; or
- The attack gag affected the group; or
- Both gags affected the group.

(Note: it appears that needing Laff was not a prerequisite for a Toon-up accuracy bonus.)

# Trap <a name="trap"></a>
[[back to top](#contents)]

## Did using Trap give Lure an accuracy boost? <a name="trap-1"></a>

Yes, Trap gags always counted as a hit on the cog for the round it was used on, regardless if the Trap was actually triggered or not. If one again considers the conditions in the [bonus section](#toon-atk-acc-6), Trap met the following conditions.

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

Yes, Trap did give an accuracy boost to other gag tracks as well. Even when not activated, Trap always counted as a hit on the cog. It would still meet the conditions given in the [bonus section](#toon-atk-acc-6), thus a +20 accuracy boost to the next gag targeting the cog. 

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

When two or more Lure gags were picked, the result of the weakest was calculated first using the highest possible value for `trackExp` according to the details outlined in [its section](#toon-atk-acc-4). From here, there were two options for all subsequent Lure gags:

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

# Cogs <a name="cogs"></a>
[[back to top](#contents)]

## Which cog was the most powerful? <a name="cogs-1"></a>

# V.P. <a name="vp"></a>
[[back to top](#contents)]

## Did being Lureless impact the accuracy of Lure SOS cards? <a name="vp-1"></a>

Yes, a value of 0 was used for `trackExp` in all Lure SOS card accuracy calculations for Lureless toons (see [Toon Attack Accuracy](#toon-atk-acc) for more information). In practice, this was only relevant for Des Traction and Dee Version, which *always* missed against level 11 and 12 cogs as seen below.

```
Level 11: atkAcc = 50 + 0 + (-50) = 0
Level 12: atkAcc = 50 + 0 + (-55) = -5
```

## Did being Lureless impact the number of rounds Lure SOS cards would hold for? <a name="vp-2"></a>

Yes, cogs were more likely to "wake up" early if the caller was Lureless. The probability associated with this event is called a cog's `wakeupChance`, which is calculated as follows:

```python
wakeupChance = 100 - atkAcc * 2
```
(See [Toon Attack Accuracy](#toon-atk-acc) for information on `atkAcc`.)

With the above in mind, it can also be useful to think in terms of `wakeupChance`'s probabilistic complement: The probability that a given SOS card will hold for a specific number of rounds. In order to do so, we must apply the Rule of Multiplication:

>The probability that Events A and B both occur is equal to the probability that Event A occurs times the probability that Event B occurs, given that A has occurred: P(A ∩ B) = P(A) P(B|A)

(Source: [Probability Rules](http://stattrek.com/probability/probability-rules.aspx).)

However, given that each round is calculated independent of any prior results, we note that P(B|A) = P(B). Thus, the following equation can be used to determine the probability that a single cog will stay lured for N rounds:

```python
Given (Max rounds - N) >= 0,

P(N rounds) = [1 - (wakeupChance / 100)] ^ (N - 1)
```

Here are some example calculations:

```
Given: a Lureless toon using Lil' Oldman

Questions: 

a. what is the probability that a level 12 cog will stay lured for 3 rounds?
b. what is the probability that 4 level 12 cogs will stay lured for 3 rounds?

Answer: 

a.

1. atkAcc = 70 (propAcc) + 0 (trackExp) + (-55) (tgtDef) + 0 (bonus) = 15
2. wakeupChance = 100 - (15 * 2) = 70
3. P(3 rounds) = [1 - (70 / 100)] ^ (3 - 1) = 0.09 (Check: 4 - 3 >= 0? Yep.)

b.

1. The probability that a single level 12 cog will stay lured for 3 rounds is 9.0%. 
2. The probability that all 4 will stay lured for 3 rounds is (.09) ^ 4 = 0.00006561.
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

## Were the gag-related decreases in SOS card performance intentional? <a name="vp-6"></a>

While it's impossible to give a definitive answer without insider knowledge, here's what we know:

The primary point of disagreement is this simple section of code in `__calcToonAtkHit`:

```python
atkTrack, atkLevel = self.__getActualTrackLevel(attack)
if atkTrack == NPCSOS:
    return (1, 95)
```

Some will argue that the conditional expression shown above is a typo and that it should actually read `attack[TOON_TRACK_COL] == NPC_SOS`. This, on the surface, makes sense for a few reasons:

1. As currently written, the above conditional expression will never evaluate to True. Or, in other words, it's completely unused during normal cirumstances.
2. Simply changing `atkTrack` to `attack[TOON_TRACK_COL]`, alleviates all gag-related SOS card performance discrepancies (see [here](#vp-1) and [here](#vp-2) for examples).
3. Changing `atkTrack` to `attack[TOON_TRACK_COL]` introduces no apparent gag mechanic side effects.

However, regardless of whether the above is ultimately a net-positive for gameplay purposes, there is significant evidence to support the claim that the above conditional expression *does not contain a typo*.

The basis of this counterargument is that a "typo," by definition, implies a high-level oversight. And, as such, it should appear inconsistent with a considerable portion of the game's existing logic. Upon closer inspection, however, this doesn't seem to be the case. Here's why:

- It's written the same way in multiple places. These include the `__createToonTargetList` and `__applyToonAttackDamages` functions in addition to `__calcToonAtkHit`. In all three cases, the expression appears to be used as an "early-termination" or "guard" conditional. That is, it represents something that *shouldn't* evaluate to True -- but, if it ever did, there's a reasonble solution offered. 
    - In `__calcToonAtkHit`, the function returns immediately (with `(1, 95)` as its return value) if it evaluates to True.
    - In `__createToonTargetList`, the function returns immediately (with `[]` as its return value) if it evaluates to True.
    - In `__applyToonAttackDamages`, the function returns immediately (with 0 as its return value) if it evaluates to True.

    As you can see, not only is it written the same way in multiple places, but it also appears to be used the same way.

- There's evidence to support the notion that the developers were keenly and consistently aware of the differences between `atkTrack` and `attack[TOON_TRACK_COL]`.
    - There were multiple functions (`__getActualTrackLevelHp`, `__getActualTrackLevel` and `__getActualTrack`) which were disigned to explicitly convert from `NPC_SOS` to other values. Moreover, `__getActualTrackLevel` is called immediately prior to all the three instances of the expression `atkTrack == NPCSOS`. Evidently supporting the claim that `atkTrack == NPCSOS` is used as a means of error checking.

- There's evidence to support the notion that the developers intended execution of `__calcToonAtkHit` to extend beyond the condtional expression in question. 
    - In `__calcToonAtkHit`, there are two separate blocks of code dedicated to detecting when Drop is being used on lured cogs. Entry to the first is controlled by the expression ` elif atkTrack == DROP and attack[TOON_TRACK_COL] == NPCSOS`. Here, `atkTrack` and `attack[TOON_TRACK_COL] == NPCSOS` are explicitly distinguished from one another: The gag is Drop *and* it's an SOS.
    - In `__calcToonAtkHit`, `attack[TOON_TRACK_COL] == NPCSOS` is used to determine the value of `randChoice` long after the supposedly intended exit point.

- There's evidence to support the notion that the developers were not actively trying to avoid gag-related performance discrepancies.
    In `__addLuredSuitInfo`, the function which manages `wakeupChance`, there's a conditional expression dedicated to detecting NPC SOS cards for skill credit purposes. However, they make no effort to avoid assigning `wakeupChance` to NPC SOS cards.

To summarize, 

- If you believe `atkTrack == NPCSOS` *contains* a typo, the following is required of you:
    1. You need to assume that they made the same typo on 3 different occasions.
    2. You need to assume that they incorrectly used the `__getActualTrackLevel` on 3 different occasions.
    3. You need to assume that they intended on two core sections of `__calcToonAtkHit` never being used.
    4. You need to assume that they checked for the "Drop on lured cogs scenario" *twice* for no reason in `__calcToonAtkHit`. (Since making the intended "typo fix" forces the game to use an otherwise unused error-checking block in `__calcToonAtkHp` to determine when Drop SOS should miss.)
    

- If you believe `atkTrack == NPCSOS` *does not contain* a typo, the following is required of you:
    1. You need to assume that `atkTrack == NPCSOS` is used as an error-checking conditional, which should never evaluate to True during normal execution.

You're probably wondering which option is more likely, right? I believe that the `__getActualTrackLevel` function -- the same one called prior to *all* instances of our "mystery" expression -- holds the answer. If we can establish exactly what this was designed to do, we can also provide a conclusive answer to the first part of this question. Let's take a look at it.

```python
# The first question that needs to be answered here is what are the possible 
# values of toonAttack[TOON_TRACK_COL]? Given that we know what should constitute
# the toonAtkOrder, this is easy to answer: 
# 
# HEAL_TRACK = 0
# TRAP_TRACK = 1
# LURE_TRACK = 2
# SOUND_TRACK = 3
# THROW_TRACK = 4
# SQUIRT_TRACK = 5
# DROP_TRACK = 6
# PETSOS = 96
# NPCSOS = 97
# FIRE = 100

def __getActualTrackLevel(self, toonAttack):
    if toonAttack[TOON_TRACK_COL] == NPCSOS:
        # How do we get here? There's only one way: If toonAttack[TOON_TRACK_COL] == NPCSOS
        track, level, hp = NPCToons.getNPCTrackLevelHp(toonAttack[TOON_TGT_COL])
            if track != None:
                # How do we get here? Any case in which track != None
                # This is what *should* happen for attack SOS cards;
                # their "type" should converted from NPCSOS to track (atkTrack)
                return (track, level) # return point: we're gone!
            else:
                # But wait ... what's this block for? This should *never* happen!
                # How could we call an unknown SOS toon?! But ... what if it does?
                self.notify.warning('No NPC with id: %d' % toonAttack[TOON_TGT_COL])
    # How do we get here? There are two possible options:
    # 1. toonAttack[TOON_TRACK_COL] is 0 - 6, 96 or 100 (fail toonAttack[TOON_TRACK_COL] == NPCSOS)
    # 2. toonAttack[TOON_TRACK_COL] is 97! Yes, that's right, it's possible to return NPCSOS!
    # This occurs if we pass toonAttack[TOON_TRACK_COL] == NPCSOS, but fail track != None
    return (toonAttack[TOON_TRACK_COL], toonAttack[TOON_LVL_COL])
```

This means we know what the "mystery" conditional expression was designed to do! If `_getActualTrackLevel` ever returned `atkTrack == 97` (an error, essentially), it was supposed to catch it and terminate `__calcToonAtkHit` early. So, how can the "mystery" conditional contain a typo if it had a well-defined, consistenly used purpose?

Now, you're probably thinking that we still haven't answered the original question -- and you're right. We know that (a) it's highly unlikely the "mystery" conditional expression contains a typo and (b) there's clear intent on the developer's part to have attack SOS cards be evaluated in a similar fashion to their regular counterparts. But, were the *performance discrepancies intentional*? Here's what we know:

- `randChoice` was deliberately set to 0 whenever an attack SOS card was used. This serves as pretty clear evidence that the developers, at the very least, wanted accuracy to be improved for SOS cards.
- A user on a Toontown fansite reportedly received the following email in response to asking if SOS cards should be able to miss.
   
   > Thank you for your e-mail.

   > 1. SOS drop cards are supposed to work 100% of the time. If you should encounter one that doesn't work, please submit a   bug report with a screen report attached so we can look into this for you further.

   > 2. The stars at the bottom of the SOS cards are the potency. The more stars... The stronger the gag. The maximum number   of stars that you should be able to receive is five.

   ([Original post can be found here.](http://www.mmocentralforums.com/forums/showpost.php?p=95226&postcount=15))


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

## How was the scale related to the jury? <a name="cj-4"></a>

When determining how the amount of Toon jurors affected the scale, the following formula was used.

```python
jurorsOver = self.numToonJurorsSeated - ToontownGlobals.LawbotBossJurorsForBalancedScale
dmgAdjust = jurorsOver * ToontownGlobals.LawbotBossDamagePerJuror
```
`jurorsOver` was determined by taking the amount of Toon jurors seated and then subtracting it by the amount needed for a balanced scale (8 for non-modified servers). That amount was then multiplied by the damage amount each Toon juror done, which was set to 68 per toon juror. The result was then referred to as `dmgAdjust`. 

The initial damage of the scale was calculated at 1350. `dmgAdjust` was then added to the initial damage of the scale. Given how the formula is calculated, we can establish the following ratios for the initial amount of evidence in the prosecution and defense pans, based on the amount of Toon jurors seated.

| # Toon Jurors seated | Initial Toon Evidence | Initial Cog Evidence|
|:---------------------:|:--------------:|:-------------:|
| 0 | 806 | 1894 |
| 1 | 874 | 1826 |
| 2 | 942 | 1758 |
| 3 | 1010 | 1690 |
| 4 | 1078 | 1622 |
| 5 | 1146 | 1554 |
| 6 | 1214 | 1486 |
| 7 | 1282 | 1418 |
| 8 | 1350 | 1350 |
| 9 | 1418 | 1282 |
| 10 | 1486 | 1214 |
| 11 | 1554 | 1146 |
| 12 | 1622 | 1078 |

The above data can also be expressed through the following formulas:

```
Initial Cog Evidence = 1894 - 68 * (# toons seated)

Initial Toon Evidence = 2700 - Initial Cog Evidence
```

## What was the optimal scalers-to-stunners ratio? <a name="cj-5"></a>

# C.E.O. <a name="ceo"></a>
[[back to top](#contents)]

## How did the C.E.O. choose which attack to use? <a name="ceo-1"></a>

## How did the C.E.O. choose which toon to attack? <a name="ceo-2"></a>

# Fishing <a name="fishing"></a>
[[back to top](#contents)]

# Racing <a name="racing"></a>
[[back to top](#contents)]

## Wall-riding: A track-by-track breakdown <a name="racing-1"></a>

# Golfing <a name="golfing"></a>
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

Yes, if multiple gags of the same track and level were used, the attack order was simply based on the order in which toons joined the battle. This meant it was possible for "mismatches" to occur. For example, consider the following scenario with three toons (1 - 3) and two cogs (A and B):

- Toon 1 (rightmost) uses a Safe on Cog A
- Toon 2 (middle) uses a Safe on Cog B
- Toon 3 (leftmost) uses a Safe on Cog A

Here, the attack order is 1, 2, 3. This means that Toon 1's Safe is evaluated, then Toon 2's Safe is evaluated (but isn't assigned the result of 1 because it has a different target) and then Toon 3's Safe is evaluated (but isn't assigned the result of 2 because it has a different target). So, in this situation, it's possible for only one Safe to hit Cog A.

## Battle Simulations

- [3 Safes](http://pastebin.com/BhZ14ZL6)
- [3 Storm Clouds](http://pastebin.com/5fb8pbtA)

## Did doodle tricks count as a stun in battle? <a name="misc-4"></a>

Yes, Doodle tricks counted as a stun in battles, provided that the trick was successful. Tricks counted as their own individual track, meaning they would satisfy the conditions listed in the [bonus section](#toon-atk-acc-6).

## Did Fires count as a stun?<a name="misc-5"></a>

# Credits <a name="credits"></a>
[[back to top](#contents)]

- Cell1234 (Patrick)

# Appendix A: Cog Attack Frequencies <a name="appendix-a"></a>
[[back to top](#contents)]

<table>
		<tr>
			<th colspan="6">Bossbots</th>
		</tr>
		<tr>
			<th>Flunky</th>
			<th>Level 1</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
		</tr>
		<tr>
			<td align="center">Pound Key</td>
			<td align="center">30</td>
			<td align="center">35</td>
			<td align="center">40</td>
			<td align="center">45</td>
			<td align="center">50</td>
		</tr>
		<tr>
			<td align="center">Shred</td>
			<td align="center">10</td>
			<td align="center">15</td>
			<td align="center">20</td>
			<td align="center">25</td>
			<td align="center">30</td>
		</tr>
		<tr>
			<td align="center">Clip-on Tie</td>
			<td align="center">60</td>
			<td align="center">50</td>
			<td align="center">40</td>
			<td align="center">30</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
		</tr>
		<tr>
			<th>Pencil Pusher</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
		</tr>
		<tr>
			<td align="center">Fountain Pencil</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<td align="center">Rub-Out</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<td align="center">Finger Wag</td>
			<td align="center">35</td>
			<td align="center">30</td>
			<td align="center">25</td>
			<td align="center">20</td>
			<td align="center">15</td>
		</tr>
		<tr>
			<td align="center">Write Off</td>
			<td align="center">5</td>
			<td align="center">10</td>
			<td align="center">15</td>
			<td align="center">20</td>
			<td align="center">25</td>
		</tr>
		<tr>
			<td align="center">Fill With Lead</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<th>Yesman</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
		</tr>
		<tr>
			<td align="center">Rubber Stamp</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
		</tr>
		<tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">25</td>
			<td align="center">20</td>
			<td align="center">15</td>
			<td align="center">10</td>
			<td align="center">5</td>
		</tr>
		<tr>
			<td align="center">Synergy</td>
			<td align="center">5</td>
			<td align="center">10</td>
			<td align="center">15</td>
			<td align="center">20</td>
			<td align="center">25</td>
		</tr>
		<tr>
			<td align="center">Tee Off</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
		</tr>
		<tr>
			<th>Micromanager</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
		</tr>
		<tr>
			<td align="center">Demotion</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
		</tr>
		<tr>
			<td align="center">Finger Wag</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
		</tr>
		<tr>
			<td align="center">Fountain Pen</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
		</tr>
		<tr>
			<td align="center">Brain Storm</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
		</tr>
		<tr>
			<td align="center">Buzzword</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<th>Downsizer</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
		</tr>
		<tr>
			<td align="center">Canned</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
		</tr>
		<tr>
			<td align="center">Downsize</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
		</tr>
		<tr>
			<td align="center">Pinkslip</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
		</tr>
		<tr>
			<td align="center">Sacked</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
		</tr>
		<tr>
			<th>Head Hunter</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
		</tr>
		<tr>
			<td align="center">Fountain Pen</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
		</tr>
		<tr>
			<td align="center">Glower Power</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<td align="center">Half Windsor</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<td align="center">Head Shrink</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
		</tr>
		<tr>
			<td align="center">Rolodex</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
		</tr>
		<tr>
			<th>Corporate Raider</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
		</tr>
		<tr>
			<td align="center">Canned</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
		</tr>
		<tr>
			<td align="center">Evil Eye</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
		</tr>
		<tr>
			<td align="center">Play Hardball</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
		</tr>
		<tr>
			<td align="center">Rolodex</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
		</tr>
		<tr>
			<th>The Big Cheese</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
			<th>Level 12</th>
		</tr>
		<tr>
			<td align="center">Tee Off</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
		</tr>
		<tr>
			<td align="center">Glower Power</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
		</tr>
		</table>
		
		
		<table>
		<tr>
			<th colspan="6">Lawbots</th>
		</tr>
		<tr>
			<th>Bottomfeeder</th>
			<th>Level 1</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
	        </tr>
	        <tr>
			<td align="center">Rubber Stamp</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Shred</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Watercooler</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
	        </tr>
	        <tr>
			<td align="center">Pick Pocket</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<th>Bloodsucker</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
	        </tr>
	        <tr>
			<td align="center">Eviction Notice</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Red Tape</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Withdrawl</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
	        </tr>
	        <tr>
			<td align="center">Liquidate</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<th>Double Talker</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
	        </tr>
	        <tr>
			<td align="center">Rubber Stamp</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
	        </tr>
	        <tr>
			<td align="center">Bounce Check</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
	        </tr>
	        <tr>
			<td align="center">Buzzword</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Double Talk</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Jargon</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Mumbo Jumbo</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<th>Ambulance Chaser</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
	        </tr>
	        <tr>
			<td align="center">Shake</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Red Tape</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Rolodex</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Hang Up</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
	        </tr>
	        <tr>
			<th>Backstabber</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
	        </tr>
	        <tr>
			<td align="center">Guilt Trip</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
	        </tr>
	        <tr>
			<td align="center">Restraining Order</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Finger Wag</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
	        </tr>
	        <tr>
			<th>Spin Doctor</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
	        </tr>
	        <tr>
			<td align="center">Paradigm Shift</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Quake</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Spin</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
	        </tr>
	        <tr>
			<td align="center">Write Off</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<th>Legal Eagle</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
	        </tr>
	        <tr>
			<td align="center">Evil Eye</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Jargon</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Legalese</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
	        </tr>
	        <tr>
			<td align="center">Pecking Order</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<th>Big Wig</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
			<th>Level 12</th>
	        </tr>
	        <tr>
			<td align="center">Power Trip</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<td align="center">Finger Wag</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        </table>
	        
	        
	        <table>
	        <tr>
			<th colspan="6">Cashbots</th>
		</tr>
		<tr>
			<th>Short Change</th>
			<th>Level 1</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
	        </tr>
	        <tr>
			<td align="center">Watercooler</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Bounce Check</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Clip-On Tie</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Pick Pocket</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
	        </tr>
	        <tr>
			<th>Penny Pincher</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
	        </tr>
	        <tr>
			<td align="center">Bounce Check</td>
			<td align="center">45</td>
			<td align="center">45</td>
			<td align="center">45</td>
			<td align="center">45</td>
			<td align="center">45</td>
	        </tr>
	        <tr>
			<td align="center">Freeze Assets</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Finger Wag</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
	        </tr>
	        <tr>
			<th>Tightwad</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
	        </tr>
	        <tr>
			<td align="center">Fired</td>
			<td align="center">75</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
	        </tr>
	        <tr>
			<td align="center">Glower Power</td>
			<td align="center">10</td>
			<td align="center">15</td>
			<td align="center">20</td>
			<td align="center">25</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Finger Wag</td>
			<td align="center">5</td>
			<td align="center">70</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
	        </tr>
	        <tr>
			<td align="center">Freeze Assets</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">65</td>
			<td align="center">5</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Bounce Check</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">60</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<th>Bean Counter</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
	        </tr>
	        <tr>
			<td align="center">Audit</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Calculate</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Tabulate</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Audit</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<th>Number Cruncher</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
	        </tr>
	        <tr>
			<td align="center">Audit</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Calculate</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Crunch</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
	        </tr>
	        <tr>
			<td align="center">Tabulate</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<th>Money Bags</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
	        </tr>
	        <tr>
			<td align="center">Liquidate</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Market Crash</td>
			<td align="center">45</td>
			<td align="center">45</td>
			<td align="center">45</td>
			<td align="center">45</td>
			<td align="center">45</td>
	        </tr>
	        <tr>
			<td align="center">Power Tie</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<th>Loan Shark</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
	        </tr>
	        <tr>
			<td align="center">Bite</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Chomp</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
			<td align="center">35</td>
	        </tr>
	        <tr>
			<td align="center">Play Hardball</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Write-Off</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<th>Robber Baron</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
			<th>Level 12</th>
	        </tr>
	        <tr>
			<td align="center">Power Trip</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<td align="center">Tee-Off</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        </table>
	        
	        
	        <table>
	        <tr>
			<th colspan="6">Sellbots</th>
		</tr>
		<tr>
			<th>Cold Caller</th>
			<th>Level 1</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
	        </tr>
	        <tr>
			<td align="center">Freeze Assets</td>
			<td align="center">5</td>
			<td align="center">10</td>
			<td align="center">15</td>
			<td align="center">20</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Pound Key</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Double Talk</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Hot Air</td>
			<td align="center">45</td>
			<td align="center">40</td>
			<td align="center">35</td>
			<td align="center">30</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<th>Telemarketer</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
	        </tr>
	        <tr>
			<td align="center">Clip-on Tie</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Pick Pocket</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Rolodex</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Double Talk</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
	        </tr>
	        <tr>
			<th>Name Dropper</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
	        </tr>
	        <tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Rolodex</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
			<td align="center">40</td>
	        </tr>
	        <tr>
			<td align="center">Synergy</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Pick Pocket</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<th>Glad Hander</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
	        </tr>
	        <tr>
			<td align="center">Rubber Stamp</td>
			<td align="center">40</td>
			<td align="center">30</td>
			<td align="center">20</td>
			<td align="center">10</td>
			<td align="center">5</td>
	        </tr>
	        <tr>
			<td align="center">Fountain Pen</td>
			<td align="center">40</td>
			<td align="center">30</td>
			<td align="center">20</td>
			<td align="center">10</td>
			<td align="center">5</td>
	        </tr>
	        <tr>
			<td align="center">Filibuster</td>
			<td align="center">10</td>
			<td align="center">20</td>
			<td align="center">30</td>
			<td align="center">40</td>
			<td align="center">45</td>
	        </tr>
	        <tr>
			<td align="center">Schmooze</td>
			<td align="center">10</td>
			<td align="center">20</td>
			<td align="center">30</td>
			<td align="center">40</td>
			<td align="center">45</td>
	        </tr>
	        <tr>
			<th>Mover & Shaker</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
	        </tr>
	        <tr>
			<td align="center">Brain Storm</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Half Windsor</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Quake</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Shake</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Tremor</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<th>Two-Face</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
	        </tr>
	        <tr>
			<td align="center">Evil Eye</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Hang-up</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Red Tape</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<th>The Mingler</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
	        </tr>
	        <tr>
			<td align="center">Buzzword</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
			<td align="center">20</td>
	        </tr>
	        <tr>
			<td align="center">Paradigm Shift</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
			<td align="center">25</td>
	        </tr>
	        <tr>
			<td align="center">Power Trip</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
			<td align="center">15</td>
	        </tr>
	        <tr>
			<td align="center">Schmooze</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Tee Off</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
			<td align="center">10</td>
	        </tr>
	        <tr>
			<th>Mr. Hollywood</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
			<th>Level 12</th>
	        </tr>
	        <tr>
			<td align="center">Power Trip</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        
	        
</table>

# Appendix B: Cog Attack Damages <a name="appendix-b"></a>
[[back to top](#contents)]

<table>
		<tr>
			<th colspan="6">Bossbots</th>
		</tr>
		<tr>
			<th>Flunky</th>
			<th>Level 1</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
		</tr>
		<tr>
			<td align="center">Pound Key</td>
			<td align="center">2</td>
			<td align="center">2</td>
			<td align="center">3</td>
			<td align="center">4</td>
			<td align="center">6</td>
		</tr>
		<tr>
			<td align="center">Shred</td>
			<td align="center">3</td>
			<td align="center">4</td>
			<td align="center">5</td>
			<td align="center">6</td>
			<td align="center">7</td>
		</tr>
		<tr>
			<td align="center">Clip-on Tie</td>
			<td align="center">1</td>
			<td align="center">1</td>
			<td align="center">2</td>
			<td align="center">2</td>
			<td align="center">3</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
		</tr>
		<tr>
			<th>Pencil Pusher</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
		</tr>
		
</table>

# Appendix C: Cog Attack Accuracy Values <a name="appendix-c"></a>
[[back to top](#contents)]

<table>
		<tr>
			<th colspan="6">Bossbots</th>
		</tr>
		<tr>
			<th>Flunky</th>
			<th>Level 1</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
		</tr>
		<tr>
			<td align="center">Pound Key</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Shred</td>
			<td align="center">50</td>
			<td align="center">55</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
		</tr>
		<tr>
			<td align="center">Clip-on Tie</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
		</tr>
		<tr>
			<th>Pencil Pusher</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
		</tr>
		<tr>
			<td align="center">Fountain Pencil</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Rub-Out</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Finger Wag</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Write Off</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Fill With Lead</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<th>Yesman</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
		</tr>
		<tr>
			<td align="center">Rubber Stamp</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
		</tr>
		<tr>
			<td align="center">Synergy</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Tee Off</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<th>Micromanager</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
		</tr>
		<tr>
			<td align="center">Demotion</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Finger Wag</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Fountain Pen</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Brain Storm</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
			<td align="center">5</td>
		</tr>
		<tr>
			<td align="center">Buzzword</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<th>Downsizer</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
		</tr>
		<tr>
			<td align="center">Canned</td>
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Downsize</td>
			<td align="center">50</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
		</tr>
		<tr>
			<td align="center">Pinkslip</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
		</tr>
		<tr>
			<td align="center">Sacked</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
		</tr>
		<tr>
			<th>Head Hunter</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
		</tr>
		<tr>
			<td align="center">Fountain Pen</td>
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Glower Power</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Half Windsor</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
		</tr>
		<tr>
			<td align="center">Head Shrink</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<td align="center">Rolodex</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
		</tr>
		<tr>
			<th>Corporate Raider</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
		</tr>
		<tr>
			<td align="center">Canned</td>
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Evil Eye</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Play Hardball</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
		</tr>
		<tr>
			<td align="center">Rolodex</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<th>The Big Cheese</th>
			<th>Level 8</th>
			<th>Level 9</th>
			<th>Level 10</th>
			<th>Level 11</th>
			<th>Level 12</th>
		</tr>
		<tr>
			<td align="center">Tee Off</td>
			<td align="center">55</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
		</tr>
		<tr>
			<td align="center">Glower Power</td>
			<td align="center">55, 70, 60 *</td>
			<td align="center">65, 75, 65 *</td>
			<td align="center">75, 85, 70 *</td>
			<td align="center">85, 90, 75 *</td>
			<td align="center">95, 95, 80 *</td>
		</tr>
        </table>
		
		*Due to how The Big Cheese is coded, Glower Power has varying attack accuracies. 
		
		
