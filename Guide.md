# Contents <a name="contents"></a>
- [Introduction](#intro)
- [Core Knowledge](#core-knowledge)
    - [Toon Attack Accuracy](#toon-atk-acc)
    - [Toon Attack Damage](#toon-atk-dmg)
    - [Cog Attack Accuracy](#cog-atk-acc)
    - [Doodle Training and Tricks](#doodle-t&t)
    - [Fishing](#fishing-main)
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
- [V.P.](#vp)
    - [Did being Lureless impact the accuracy of Lure SOS cards?](#vp-1)
    - [Did being Lureless impact the number of rounds Lure SOS cards would hold for?](#vp-2)
    - [How did the V.P. choose which attack to use?](#vp-3)
    - [How did the V.P. choose which toon to attack?](#vp-4)
    - [Was there a way to predict when the undercarriage would open?](#vp-5)
    - [Were the gag-related decreases in SOS card performance intentional?](#vp-6)
    - [How were the SOS toons chosen?](#vp-7)
- [C.F.O.](#cfo)
    - [How was the C.F.O. reward chosen?](#cfo-1)
    - [How did the C.F.O. choose which toon to attack?](#cfo-2)
- [C.J.](#cj)
    - [How was the C.J. reward chosen?](#cj-1)
    - [How did the C.J. decide when to jump?](#cj-2)
    - [How did the prosecution choose which toon to attack?](#cj-3)
    - [How was the scale related to the jury?](#cj-4)
- [C.E.O.](#ceo)
    - [How did the C.E.O. choose which attack to use?](#ceo-1)
    - [How did the C.E.O. choose which toon to attack?](#ceo-2)
    - [How did the C.E.O. decide to continue moving or not?](#ceo-3)
- [Fishing](#fishing)
	- [Was using a Twig Rod more beneficial to catch light-weight Ultra Rares than a Gold Rod?](#fishing-1)
- [Racing](#racing)
- [Gardening](#gardening)
- [Golfing](#golfing)
- [Misc](#misc)
    - [Did some Shopkeepers sell more accurate gags?](#misc-1)
    - [When multiple gags of the same track were used on the same cog, how was accuracy calculated?](#misc-2)
    - [Was it possible for two gags of the same track, aiming for the same cog, to have different hit/miss results?](#misc-3)
    - [Did doodle tricks count as a stun in battle?](#misc-4)
    - [Did Fires count as a stun?](#misc-5)
- [Appendix A: Cog Attack Frequencies](#appendix-a)
	- [Sellbots](#atk-freq-sell)
	- [Cashbots](#atk-freq-cash)
	- [Lawbots](#atk-freq-law)
	- [Bossbots](#atk-freq-boss)
- [Appendix B: Cog Attack Damages](#appendix-b)
	- [Sellbots](#atk-dmg-sell)
	- [Cashbots](#atk-dmg-cash)
	- [Lawbots](#atk-dmg-law)
	- [Bossbots](#atk-dmg-boss)
- [Appendix C: Cog Attack Accuracies](#appendix-c)
	- [Sellbots](#atk-acc-sell)
	- [Cashbots](#atk-acc-cash)
	- [Lawbots](#atk-acc-law)
	- [Bossbots](#atk-acc-boss)

# Introduction <a name="intro"></a>

## Goals

This guide started out as an attempt to answer some long-standing questions about the battle system in Disney's Toontown Online. However, it has since grown far larger than anticipated; it has answered a total of 27 questions, many of which expand beyond the battle system itself. That said, the number one goal remains the same: to offer *accurate* information about Toontown's various mechanics. Suggestions or questions about the quality of our content are always welcome.

## Private Servers

The information used in this guide is primarily based on the source code of Toontown Online and, as such, it neither guarantees accuracy with regard to any private servers nor aims to keep up with any of their future changes.

## About the Authors

- Cell1234: I have been playing Toontown since 2003, just a bit before SBHQ came out. While I had some breaks, I always enjoyed the game and the people I met on it. I'm usually known as Patrick on forums, but I go by Cell1234 on Reddit.

- QED1224: I played Toontown from August of 2005 until its official close on September 19, 2013 (you may have known me as either Reign or Super Fireball Thunderroni). I'm still a huge fan of the game and its history, and you can find me on many of its online forums as QED.

# Core Knowledge <a name="core-knowledge"></a>
[[back to top](#contents)]

## Toon Attack Accuracy <a name="toon-atk-acc"></a>

`atkAcc` was a percentage which represented the likelihood of an attack performing to its highest degree. This was used in two ways:

1. For Lure SOS cards, it was used when calculating the odds that cogs "wake up" early each round.
2. It was used when calculating the value of `atkHit`, which was a boolean value that represented whether or not an attack hit.

### Special Cases <a name="toon-atk-acc-1"></a>

Fires and Trap had 95% and 100% accuracy respectively. In addition, both were always assigned an `atkHit` of 1, which meant they were *guaranteed* to hit.

### Equation <a name="toon-atk-acc-2"></a>

A gag's overall accuracy was calculated using the following equation:

```python
atkAcc = propAcc + trackExp + tgtDef + bonus
```

#### `propAcc` <a name="toon-atk-acc-3"></a>

<table>
  <tr>
    <th colspan="9">AvPropAccuracy</th>
  </tr>
  <tr>
    <th colspan="2">Track</th>
    <th>Level 1</th>
    <th>Level 2</th>
    <th>Level 3</th>
    <th>Level 4</th>
    <th>Level 5</th>
    <th>Level 6</th>
    <th>Level 7</th>
  </tr>
  <tr>
    <td colspan="2" align="center">Toon-up</td>
    <td align="center">70</td>
    <td align="center">70</td>
    <td align="center">70</td>
    <td align="center">70</td>
    <td align="center">70</td>
    <td align="center">70</td>
    <td align="center">100</td>
  </tr>
  <tr>
    <td colspan="2" align="center">Trap</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
  </tr>
  <tr>
    <td colspan="2" align="center">Lure</td>
    <td align="center">50</td>
    <td align="center">50</td>
    <td align="center">60</td>
    <td align="center">60</td>
    <td align="center">70</td>
    <td align="center">70</td>
    <td align="center">100</td>
  </tr>
  <tr>
    <td colspan="2" align="center">Sound</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
  </tr>
  <tr>
    <td colspan="2" align="center">Throw</td>
    <td align="center">75</td>
    <td align="center">75</td>
    <td align="center">75</td>
    <td align="center">75</td>
    <td align="center">75</td>
    <td align="center">75</td>
    <td align="center">75</td>
  </tr>
  <tr>
    <td colspan="2" align="center">Squirt</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
    <td align="center">95</td>
  </tr>
  <tr>
    <td colspan="2" align="center">Drop</td>
    <td align="center">50</td>
    <td align="center">50</td>
    <td align="center">50</td>
    <td align="center">50</td>
    <td align="center">50</td>
    <td align="center">50</td>
    <td align="center">50</td>
  </tr>
</table>

<table>
  <tr>
    <th colspan="9"><a name="AvLureBonusAccuracy">AvLureBonusAccuracy</a></th>
  </tr>
  <tr>
    <th colspan="2">Track</th>
    <th>Level 1</th>
    <th>Level 2</th>
    <th>Level 3</th>
    <th>Level 4</th>
    <th>Level 5</th>
    <th>Level 6</th>
    <th>Level 7</th>
  </tr>
  <tr>
    <td colspan="2" align="center">Lure</td>
    <td align="center">60</td>
    <td align="center">60</td>
    <td align="center">70</td>
    <td align="center">70</td>
    <td align="center">80</td>
    <td align="center">80</td>
    <td align="center">100</td>
  </tr>
</table>

For all non-Lure gags, `propAcc` was simply the above pre-defined `AvPropAccuracy` value.

For Lure gags, `propAcc` was initially assigned its `AvPropAccuracy` value, then if the toon had Lure trees planted at a level greater than or equal to the gag level being used **or** there was an active Lure interactive prop, `propAcc` was re-assigned a value from `AvLureBonusAccuracy`.

#### `trackExp` <a name="toon-atk-acc-4"></a>

`trackExp` was calculated according to the following:

```
 trackExp = [highest gag level in track - 1] * 10
```

If the track was Toon-up, the above result was halved. 

This was repeated for every gag within a particular track. So, if multiple toons used the *same gag track* (outside of Toon-up and Trap) on the *same target*, the highest `trackExp` was used in the `atkAcc` calculations for all of them. The latter requirement is particularly important: In order for weaker gags to inherit an increased `trackExp`, the target(s) of the weaker and stronger gags had to be the same. 

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

## Toon Attack Damage <a name="toon-atk-dmg"></a>
[[back to top](#contents)]

## Gag Damage

Gag damage was based on the amount of experience earned in a particular track. The following three steps outline the process that was used to convert from experience earned to damage.

- `expVal`:

```python
expVal = min(exp, maxE)
```
`exp` and `maxE` represented the amount of experience earned and the maximum amount of experience possible for the gag being used, respectively.

- `expPerHp`:

```python
expPerHp = float(maxE - minE + 1) / float(maxD - minD + 1)
```
`minE` was the minimum amount of experience necessary to gain access to the gag being used. `minD` and `maxD` were the minimum and maximum amount of damage for the gag being used, respectively.

- Finally, `damage`:

```python
damage = floor((expVal - minE) / expPerHp) + minD
```


## `hpBonus`

`hpBonus` applied in any case where multiple gags of the same track were used in the same round, on the same target. It was calculated as follows.

```python
hpBonus = ceil(totalDmgs * 0.20)
```
([See definition of `ceil` here](https://docs.python.org/2/library/math.html#math.ceil))

Where `totalDmgs` represented the total amount of damage done by the particular track, on the particular target.

`hpBonus` did not apply to Lure or Trap gags.

## `kbBonus`

`kbBonus` should have applied in any case in which a lured target was attacked with Throw or Squirt. It was calculated as follows.

```python
kbBonus = totalDmgs * 0.50
```
Where `totalDmgs` represented the total amount of damage done on the particular lured target.

However `kbBonus` was affected by a long-standing bug, which was essentially caused by the fact that `kbBonus` was assigned based on cog position instead of cog ID. This meant that `kbBonus` was dependent on consistent ordering. For example, consider the following situation:

```
D C B A

   1
```

Here, we have four *lured* cogs (D, C, B, and A) against 1 toon. This cog ordering was represented by a list named `activeSuits` (that is, `[A, B, C, D]`). There were, however, other representations including `suits`, `joiningSuits` and `pendingSuits` -- none of which were guaranteed to be ordered in the same way.

Now, consider that Toon 1 uses a Birthday Cake on cog C (index 2).

```
:BattleCalculatorAI(debug): activeSuits = [A, B, C, D]
:BattleCalculatorAI(debug): suits = [A, D, B, C]
```

In the above, `activeSuits` is ordered as expected and would result in cog C getting the bonus. However, the game actually used the ordering of `suits`!

```
:BattleCalculatorAI(debug): track = 4
:BattleCalculatorAI(debug): tgtPos = suits.index(C) = 3
:BattleCalculatorAI(debug): kbBonuses[tgtPos][track] = [0, 100.0]
:BattleCalculatorAI(debug): Applying kbBonus (100.0 * 0.5 dmg) to activeSuit at tgtPos 3
:BattleCalculatorAI(debug): activeSuit C takes 100.0 damage
```
As you can see, it used the index of cog C from `suits` on the cog at the same index in `activeSuits`, which was cog D.

## Carryover

"Carryover" damage only applied to version 2.0 cogs. Every time an instance of damage was done, the game checked to see if the cog was dead. Once the first layer was destroyed, any further instances of damage done would bleed through to the skelecog layer. For all calculation purposes, the game calculated the instances of damages in the order of gag damage (Red), `hpBonus` (Yellow) and then `kbBonus` (Orange). 

Suppose we have 3 toons use maxed Storm Clouds against a lured Level 12 The Big Cheese V2.0.

```
Toon 1 = 80 damage (Red). Is the cog destroyed? No, HP = 120.
Toon 2 = 80 damage (Red). Is the cog destroyed? No, HP = 40.
Toon 3 = 80 damage (Red). Is the cog destroyed? Yes, but it is a version 2.0, so revive it with max HP.
hpBonus is calculated (240 * 0.20 = 48). Is the skelecog destroyed? No, HP = 152.
kbBonus is calculated (240 * 0.5 = 120). Is the skelecog destroyed? No, HP = 32.
```

## Cog Attack Accuracy <a name="cog-atk-acc"></a>
[[back to top](#contents)]

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
:SuitBattleGlobals(LP): Entering pickSuitAttack...
:SuitBattleGlobals(LP): Attacks ...
:SuitBattleGlobals(LP): RubberStamp with freq = 35
:SuitBattleGlobals(LP): RazzleDazzle with freq = 25
:SuitBattleGlobals(LP): Synergy with freq = 5
:SuitBattleGlobals(LP): TeeOff with freq = 35
:SuitBattleGlobals(LP): 
	randNum = 60
	count = 0
	index = 0
:SuitBattleGlobals(LP): Looping through attacks...
:SuitBattleGlobals(LP): 
	count = 35 (RubberStamp)
	index = 0
:SuitBattleGlobals(LP): 60 < 35? => False
:SuitBattleGlobals(LP): 
	count = 60 (RubberStamp + RazzleDazzle)
	index = 1
:SuitBattleGlobals(LP): 60 < 60? => False
:SuitBattleGlobals(LP): 
	count = 65 (RubberStamp + RazzleDazzle + Synergy)
	index = 2
:SuitBattleGlobals(LP): 60 < 65? => True
:SuitBattleGlobals(LP): Picking Synergy...
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
2. The relative contributions by each toon, (contributed / `totalDamage`) * 100, were stored in a list `dmgs`.
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

### How was Doodle trick experience calculated? <a name="doodle-t&t-1"></a>

Doodle tricks had similarities to how gags gained experience. Each time a successful trick was performed, that trick would gain +20 experience points. Each trick required 10000 experience points to fully max the trick. 10000 / 20 would require the Doodle to perform 500 successful tricks, in order to max that particular trick. To max all tricks, it would require an overall total of 3500 successful tricks.

In addition, performing a successful trick would increase the `aptitiude` value of that trick by 0.002. When a trick was fully maxed, `aptitude` capped out at 1.0. To determine the `aptitude` value a doodle has, the following equation could be used.

```python
aptitude = trick experience / 10000
```

### Did Doodle tricks have base accuracy values to them? <a name="doodle-t&t-2"></a>

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

### How did the game determine if the Doodle would successfully perform the trick? <a name="doodle-t&t-3"></a>

To determine if a trick would be successful or not, the following equation could be used.

```python
cutoff = trickAcc * (minApt + ((maxApt - minApt) * aptitude))
```

`cutoff` is the end result of the following variables being calculated. `trickAcc` referred to the base accuracy value of the trick being used (see previous question). `minApt` and `maxApt` were predetermined values set by the Doodle's mood. If the Doodle was neutral, excited, playful or affectionate, `minApt = 0.5` and `maxApt = 0.97`. However, if the Doodle was bored, restless, lonely, sad, tired, hungry or angry, `minApt = 0.1` and `maxApt = 0.6`. `aptitude` was the value determined by taking the trick's experience / 10000.  

If the Doodle was tired either at the Estate or the battle selection screen, `cutoff` was multiplied by 0.5. 

If the Doodle had a negative mood at the Estate, but had a positive mood on the battle selection screen, `minApt` and `maxApt` would still equal 0.5 and 0.97 respectively. 

If the Doodle had negative moods in both the Estate and the battle selection screen, `minApt = 0.1` and `maxApt = 0.6`. However, `cutoff` would not be multiplied by 0.5 unless one of the negative moods was tired.

Once the final value of `cutoff` was determined, a pseudorandom number, `randVal`, was generated such that 0.0 <= `randVal` < 1.0. If `cutoff` was greater than `randVal`, the Doodle would successfully perform the trick. Otherwise, the Doodle would not perform the trick.

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
As you can see, maxed Play Dead and Rollover were the most efficient tricks. Therefore Play Dead was likely the only trick worth training, since it maximized the work-reward ratio.

## Fishing <a name="fishing-main"></a>
[[back to top](#contents)]

### `itemType`

`itemType` was the primary factor in determining the result of a successful cast. The possible types were `JellybeanItem` (1%), `FishItem` (2%), `BootItem` (5%) and `QuestItem` (92%).

### `QuestItem`

`QuestItem` served two purposes:

- If there was an active Fishing quest, the following calculation was done to determine if the quest item would be found:

    ```python
   questItemFound = False
   minChance = questClass.getPercentChance() # Quest rarity %
   chance = random.randint(minChance - 40, 100)
   if chance <= minChance:
       questItemFound = True
    ```
- If there was not an active Fishing quest or the quest item was not found,  `QuestItem` used the same process as `FishItem` (see next section).

### `FishItem`

Every fish had three components: genus, species and weight. Genus and species were randomly selected from a list, `fishList`, which was formed as follows.

- `rarity`:

```python
rarity = int(ceil(10 * (1 - pow(diceRoll, RodRarityFactor))))
if rarity <= 0:
    rarity = 1
```
Where `diceRoll` was a pseudorandom real number such that 0.0 <= `diceRoll` < 1.0 and `RodRarityFactor` was given by the following table.

|   Rod    | `RodRarityFactor` | 
|:--------:|:-----------------:|
| Twig     | 1 / 4.3           | 
| Bamboo   | 1 / (4.3 * 0.975) |
| Hardwood | 1 / (4.3 * 0.95)  |
| Steel    | 1 / (4.3 * 0.90)  |
| Gold     | 1 / (4.3 * 0.85)  |

- `fishList`: 

After the calculation of `rarity`, the possible fish were narrowed by pond location and rod used. Then, the possible fish were further subdivided into multiple `fishList`s, each associated with a particular `rarity` value. All possible combinations can be [seen here](http://pastebin.com/as4BKA3E). 

After selecting a genus and species, the fish's weight was calculated according to the following process:

```python
minWeight = max(minFishWeight, minRodWeight)
maxWeight = min(maxFishWeight, maxRodWeight)
randNumA = random.random() # A real number between 0.0 and 1.0
randNumB = random.random() # A real number between 0.0 and 1.0
randNum = (randNumA + randNumB) / 2.0
randWeight = minWeight + (maxWeight - minWeight) * randNum
randWeight = int(round(randWeight * 16))
```

If no `fishList` was associated with the calculated `rarity` value, a Balloon Fish weighing 0lbs was caught.

### `JellybeanItem`

In this case, Jellybeans were awarded according to the following table.
 
|   Rod    | Jellybeans | 
|:--------:|:----------:|
| Twig     | 10         | 
| Bamboo   | 20         |
| Hardwood | 30         |
| Steel    | 75         |
| Gold     | 150        |

### `BootItem`

In this case, a boot was caught.

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

- Both Lure and Trap were single-cog, and the target was the same.
- The Trap was multi-cog.
- The Lure was multi-cog.

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

> If events A and B come from the same sample space, the probability that both A and B occur is equal to the probability the event A occurs times the probability that B occurs, given that A has occurred.
> 
> P(A ∩ B) = P(A) P(B|A)

   (Source: [Probability Rules](http://stattrek.com/statistics/dictionary.aspx?definition=Multiplication_rule).)

However, given that each round is calculated independent of any prior results, we note that P(B|A) = P(B). Thus, the following equation can be used to determine the probability that a single cog will stay lured for N rounds:

```
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

- `randChoice` was deliberately set to 0 whenever an attack SOS card was used. This serves as pretty clear evidence that the developers, at the very least, wanted accuracy to be improved for SOS cards.
- A user on a Toontown fansite reportedly received the following email in response to asking if SOS cards should be able to miss.
   
   > Thank you for your e-mail.

   > 1. SOS drop cards are supposed to work 100% of the time. If you should encounter one that doesn't work, please submit a   bug report with a screen report attached so we can look into this for you further.

   > 2. The stars at the bottom of the SOS cards are the potency. The more stars... The stronger the gag. The maximum number   of stars that you should be able to receive is five.

   ([Original post can be found here.](https://gyazo.com/38a8efa05345441c711e95420f59cb40))
   
- The Toontown Player's Guide stated that Drop SOS cards had *near* perfect accuracy.

  > ... Some of these Toons, like Professor Pete, will restock your gag supply, while others, like Clumsy Ned, will lend a hand by dropping pianos with near perfect accuracy ...

## How were the SOS toons chosen?  <a name="vp-7"></a>

Upon entering the elevator, the game would return a list of all VP SOS toons via the .keys() method. The game would then use `random.choice` to pick an SOS from that list. In other words, the stars on the SOS card would not affect the chances of it being selected.

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
jurorsOver = numToonJurorsSeated - LawbotBossJurorsForBalancedScale
dmgAdjust = jurorsOver * LawbotBossDamagePerJuror
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

# C.E.O. <a name="ceo"></a>
[[back to top](#contents)]

## How did the C.E.O. choose which attack to use? <a name="ceo-1"></a>

Every 5 seconds, the C.E.O. had a 20% chance to use its Fore! attack and an 80% chance to use a directed attack.

## How did the C.E.O. choose which toon(s) to attack? <a name="ceo-2"></a>

Every time a toon recorded a hit on the C.E.O., its ID and associated damage were added to `threatDict`, a Python dictionary which tracked the amount damage done by each toon. A golf ball hit was worth 0.1 and a Seltzer Bottle hit was worth the damage indicated in-game.

Each time a directed attack was chosen, assuming there were unflattened toons, the C.E.O. had a 10% chance to attack a toon at random. In the other 90% of time, the toon who had inflicted the most damage was chosen. In the case of a tie, a toon was selected at random from a list of toons who had dealt the same amount of damage.

Once a toon was picked, an attack was chosen based on the state of the toon:

- If the toon was roaming, the directed golf attack was used.
- If the toon was on a table, there was a 25% chance that Throw Gears was used and a 75% chance that the C.E.O. would roll over the occupied table.

After the attack was completed, the toon's damage total in `threatDict` was reduced by 25%.

## How did the C.E.O. decide to continue moving or not? <a name="ceo-3"></a>

If the C.E.O. was moving towards a toon on a table, and that particular toon hopped off the table, `random.random()` generated a number between 0.0 and 1.0. If `random.random()` was less than 0.5, the C.E.O. would stop moving towards that table and use his directed golf attack. Otherwise, the C.E.O. would run over that table and stop on top of it.

# Fishing <a name="fishing"></a>
[[back to top](#contents)]

## Was using a Twig Rod more beneficial to catch light-weight Ultra Rares than a Gold Rod? <a name="fishing-1"></a>

No, infact using a Twig Rod was less beneficial to catch light-weight Ultra Rares than a Gold Rod. In order for any rod to obtain an Ultra Rare Fish, the `rarity` value had to equal 10. Given how `rarity` was calculated ([see Fishing for more details](#fishing-main)), we can figure out the bare minimum `diceRoll` number for Twig Rod and Gold Rod to have a `rarity` value of 10. Assume `diceRoll` = X.

```
Twig Rod
rarity = int(ceil(10 * (1 - pow(X, 1 / 4.3)))) = 9 => X = 0.000050119

Gold Rod
rarity = int(ceil(10 * (1 - pow(X, 1 / (4.3 * 0.85))))) = 9 => X = 0.0002213
```
In order for a Twig Rod to have `rarity = 10`, `diceRoll` needed to be less than 0.000050119. But for a Gold Rod to have `rarity = 10`, `diceRoll` needed to be less than 0.0002213. 

Since `rarity` was determined before picking a fish (and the fish being picked from that `fishList` was done randomly), a Twig Rod had a much lower chance to hit a `rarity` value of 10 than a Gold Rod. 

# Racing <a name="racing"></a>
[[back to top](#contents)]

# Gardening <a name="gardening"></a>
[[back to top](#contents)]

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

From here, for all calculation purposes, attacks were considered in pairs (the previous attack and the current attack) within each track.

Now, we need to cover four more sub-cases:

1. Toon-up gags were always evaluated independently.
2. Lure gags were only evaluated independently when using a combination of multi- and single-cog Lures, and a multi-cog Lure was the lowest level ([see the multi-Lure section for details](#lure-1)). In all other cases, the result of the lowest Lure gag was applied to all subsequent Lures.
3. Sound gags always inherited the result of the lowest Sound gag used. 
4. For all other tracks, if the previous gag in the particular track had the same target as the current, the current inherited the result of the previous.

## Was it possible for two gags of the same track, aiming for the same cog, to have different hit/miss results? <a name="misc-3"></a>

Yes, do to how toon attacks were ordered (see previous question), it was possible for "mismatches" to occur. Essentially, this was caused by the fact that attacks were only considered in pairs. For example, consider the following scenario with three Trapless toons with maxed gags (1 - 3) and two level 12 cogs (A and B):

```
 B A
3 2 1
```

- Toon 1 uses a Safe on Cog A
- Toon 2 uses a Safe on Cog B
- Toon 3 uses a Safe on Cog A

Here, the attack order is 1, 2, 3 which means:

1. Toon 1's Safe was evaluated.
2. Toon 2's Safe was evaluated, but wasn't assigned the result of 1 because it had a different target.
3. Toon 3's Safe was evaluated, but wasn't assigned the result of 2 because it had a different target. 

So, in this situation, it was possible for only one Safe to hit Cog A.

At first glance this may appear to be rather undesirable, however it's important to fully understand the impact of independent calculations. There are two key areas to consider: expected damage and battle duration.

Let's first look at the expected damage on cog A *without an attack mismatch*.

```
 B A
3 2 1

- Toon 1 uses Safe on cog A
- Toon 2 uses Safe on cog A
- Toon 3 uses Safe on cog B

atkAcc = 50 + 60 + (-55) + 0 = 55

P(Toon 1 and Toon 2 hit) = atkAcc / 100 = 0.55
P(only Toon 1 hit or only Toon 2 hit) = 0 (shared calculation)
P(Toon 1 and Toon 2 miss) = 1 - P(Toon 1 and Toon 2 hit) = 0.45
P(at least Toon 1 or Toon 2 hit) = P(Toon 1 and Toon 2 hit) = 0.55
```

In this case, there was a 55% chance (both Safes hit) that damage was done to cog A and a 45% chance (both Safes miss) that no damage was done

Now, let's look at the expected damage on cog A *with an attack mismatch*.

```
 B A
3 2 1

- Toon 1 uses Safe on cog A
- Toon 2 uses Safe on cog B
- Toon 3 uses Safe on cog A

atkAcc = 50 + 60 + (-55) + 0 = 55

P(Toon 1 and Toon 3 hit) = (atkAcc / 100) ^ 2 = 0.3025
P(only Toon 1 hit or only Toon 3 hit) = (0.45 * 0.55) * 2 = 0.495
P(Toon 1 and Toon 3 miss) = (1 - P(Toon 1 and Toon 3 hit))^2 = 0.2025
P(at least Toon 1 or Toon 3 hit) = 0.3025 + 0.495 = 0.7975
```

You'll note that there was a 24.75% decrease (0.3025 vs. 0.55) to the odds that two Safes hit cog A compared to without an attack mismatch. However, this decrease didn't actually constitute an overall loss in expected damage: it was simply more evenly distributed. This is evident in the probability that at least one Safe hit, which was 79.75% vs. 55% *in favor of attack mismatches*. To further clarify the difference, let's take a closer look at the possible outcomes. 
```
HH = Both hit
HM = First hit, second miss
MH = First miss, second hit
MM = Both miss
```
As you can see, there were three outcomes which resulted in damage to a cog: HH, HM and MH. However, without attack mismatches, accuracy inheritance eliminated both HM and MH. This loss of opportunity could only be offset by a large increase in the probability of HH. For instance, in the above example there's a difference of 24.75%, which was just enough to make up for the loss (see [Level 12 Big Wig; Safe + Safe](http://pastebin.com/bzugMzEs)). Thus, the key factor was the fact that as the probability of HH increased, the difference between the probability of HH with and without attack mismatches decreased. Take, for example, maxed Storm Cloud:

```
 B A
3 2 1

atkAcc = 95 + 60 + (-55) + 0 = 100 (capped to 95).

a) No mismatches

- Toon 1 uses Storm Cloud on cog A
- Toon 2 uses Storm Cloud on cog A
- Toon 3 uses Storm Cloud on cog B

P(Toon 1 and Toon 2 hit) = atkAcc / 100 = 0.95
P(only Toon 1 hit or only Toon 2 hit) = 0 (shared calculation)
P(Toon 1 and Toon 2 miss) = 1 - P(Toon 1 and Toon 2 hit) = 0.05
P(at least Toon 1 or Toon 2 hit) = P(Toon 1 and Toon 2 hit) = 0.95

b) Mismatches

- Toon 1 uses Storm Cloud on cog A
- Toon 2 uses Storm Cloud on cog B
- Toon 3 uses Storm Cloud on cog A

P(Toon 1 and Toon 3 hit) = (atkAcc / 100) ^ 2 = 0.9025
P(only Toon 1 hit or only Toon 3 hit) = (0.05 * 0.95) * 2 = 0.095
P(Toon 1 and Toon 3 miss) = (1 - P(Toon 1 and Toon 3 hit)) ^ 2 = 0.0025
P(at least Toon 1 or Toon 3 hit) = P(Toon 1 and Toon 3 hit) = 0.9025 + 0.095 = 0.9975
```

As shown above, in this case there was only a 4.75% difference in the probability of HH. You might be tempted to point out that we also only saw a 4.75% increase in P(at least Toon 1 or Toon 2 hit), which is true, but there's another factor: one hit was significantly better than no hits. Think about it in terms of the number of possible ways to defeat a cog:

```
Cog HP = 200

a) No mismatches

1. HH + 32 = (80 + 80) + 32 = 192 (P = 0.95)
2. 192 + (HH + 32) = 384 (P = 0.9025).

b) Mismatches

1. HH + 32 = (80 + 80) + 32 = 192 (P = 0.9025).
2. 192 + (HH + 32) = 384 (P = 0.8145)

OR

1. HH + 32 = (80 + 80) + 32 = 192 (P = 0.9025).
2. 192 + HM = 192 + 80 = 272 (P = 0.042869).

OR

1. HH + 32 = 192 (P = 0.9025).
2. 192 + MH = 192 + 80 = 272 (P = 0.042869).

OR

1. MH = 80 (P = 0.0475).
2. 80 + (HH + 32) = 272 (P = 0.042869).

OR

1. HM = 80 (P = 0.0475).
2. 80 + (HH + 32) = 272 (P = 0.042869).
```
As you can see, attack mismatches gave us 5 ways to win vs. only 1 without them. With the above in mind, we can conclude that attack mismatches should have been preferred in any of the following scenarios.

- If either gag was capable of defeating the given cog in one round.
- Assuming maxed gags, when any combination of Throw and Squirt was used.

### Battle Simulations

- [Level 12 Big Wig; Whole Cream Pie + Birthday Cake](http://pastebin.com/gLBF00qr)
- [Level 12 Big Wig; Safe + Safe](http://pastebin.com/bzugMzEs)
- [Level 12 Big Wig; Storm Cloud + Storm Cloud](http://pastebin.com/9H3u0B4H)
- [Level 5 Bottom Feeder; Safe + Safe](http://pastebin.com/DM3tf9eg)

## Did doodle tricks count as a stun in battle? <a name="misc-4"></a>

Yes, Doodle tricks counted as a stun in battles, provided that the trick was successful. Tricks counted as their own individual track, meaning they would satisfy the conditions listed in the [bonus section](#toon-atk-acc-6).

### Battle Simulations

- [Jump & Grand Piano](http://pastebin.com/x4g9dZuZ)

## Did Fires count as a stun?<a name="misc-5"></a>

Yes, Fires counted as a stun, so long as the gag(s) used aftewards were multi-target gags. Fires would not count as a stun for single target gags.

### Battle Simulations

- [1 Fire & Hypno Goggles](http://pastebin.com/yqU1WxdX)

# Appendix A: Cog Attack Frequencies <a name="appendix-a"></a>

## Sellbots <a name="atk-freq-sell"></a>
[[back to top](#contents)]

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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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

## Cashbots <a name="atk-freq-cash"></a>
[[back to top](#contents)]

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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<td align="center">Write-Off</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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

## Lawbots <a name="atk-freq-law"></a>
[[back to top](#contents)]

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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
	        
## Bossbots <a name="atk-freq-boss"></a>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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

# Appendix B: Cog Attack Damages <a name="appendix-b"></a>

## Sellbots <a name="atk-dmg-sell"></a>
[[back to top](#contents)]

## Cashbots <a name="atk-dmg-cash"></a>
[[back to top](#contents)]

## Lawbots <a name="atk-dmg-law"></a>
[[back to top](#contents)]

<table>
		<tr>
    			<th colspan="7">Lawbots</th>
  		</tr>
  		<tr>
    			<th colspan="2">Bottom Feeder</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 1</th>
    			<th>Level 2</th>
    			<th>Level 3</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
  		</tr>
		<tr>
    			<td align="center">Rubber Stamp</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
  		</tr>
  		<tr>
    			<td align="center">Shred</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
  		</tr>
  		<tr>
    			<td align="center">Watercooler</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
  		</tr>
  		<tr>
    			<td align="center">Pick Pocket</td>
    			<td align="center">Single</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">2</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Bloodsucker</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 2</th>
    			<th>Level 3</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
  		</tr>
		<tr>
    			<td align="center">Eviction Notice</td>
    			<td align="center">Single</td>
    			<td align="center">1</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
  		</tr>
  		<tr>
    			<td align="center">Red Tape</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
  		</tr>
  		<tr>
    			<td align="center">Withdrawal</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
    			<td align="center">14</td>
  		</tr>
  		<tr>
    			<td align="center">Liquidate</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Double Talker</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 3</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
  		</tr>
		<tr>
    			<td align="center">Rubber Stamp</td>
    			<td align="center">Single</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
  		</tr>
  		<tr>
    			<td align="center">Bounce Check</td>
    			<td align="center">Single</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
  		</tr>
  		<tr>
    			<td align="center">Buzz Word</td>
    			<td align="center">Group</td>
    			<td align="center">1</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
  		</tr>
  		<tr>
    			<td align="center">Double Talk</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
    			<td align="center">13</td>
    			<td align="center">18</td>
  		</tr>
  		<tr>
    			<td align="center">Jargon</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
    			<td align="center">12</td>
  		</tr>
  		<tr>
    			<td align="center">Mumbo Jumbo</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
    			<td align="center">12</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Ambulance Chaser</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
  		</tr>
		<tr>
    			<td align="center">Shake</td>
    			<td align="center">Group</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
  		</tr>
  		<tr>
    			<td align="center">Red Tape</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
    			<td align="center">19</td>
  		</tr>
  		<tr>
    			<td align="center">Rolodex</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
  		</tr>
  		<tr>
    			<td align="center">Hang Up</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Back Stabber</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
  		</tr>
		<tr>
    			<td align="center">Guilt Trip</td>
    			<td align="center">Group</td>
    			<td align="center">8</td>
    			<td align="center">11</td>
    			<td align="center">13</td>
    			<td align="center">15</td>
    			<td align="center">18</td>
  		</tr>
  		<tr>
    			<td align="center">Restraining Order</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">9</td>
    			<td align="center">11</td>
    			<td align="center">13</td>
  		</tr>
  		<tr>
    			<td align="center">Finger Wag</td>
    			<td align="center">Single</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
    			<td align="center">9</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Spin Doctor</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
    			<th>Level 10</th>
  		</tr>
		<tr>
    			<td align="center">Paradigm Shift</td>
    			<td align="center">Group</td>
    			<td align="center">9</td>
    			<td align="center">10</td>
    			<td align="center">13</td>
    			<td align="center">16</td>
    			<td align="center">17</td>
  		</tr>
  		<tr>
    			<td align="center">Quake</td>
    			<td align="center">Group</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
    			<td align="center">14</td>
    			<td align="center">16</td>
  		</tr>
  		<tr>
    			<td align="center">Spin</td>
    			<td align="center">Single</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
    			<td align="center">18</td>
    			<td align="center">20</td>
  		</tr>
  		<tr>
    			<td align="center">Write Off</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
    			<td align="center">9</td>
    			<td align="center">10</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Legal Eagle</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
    			<th>Level 10</th>
    			<th>Level 11</th>
  		</tr>
		<tr>
    			<td align="center">Evil Eye</td>
    			<td align="center">Single</td>
    			<td align="center">10</td>
    			<td align="center">11</td>
    			<td align="center">13</td>
    			<td align="center">15</td>
    			<td align="center">16</td>
  		</tr>
  		<tr>
    			<td align="center">Jargon</td>
    			<td align="center">Single</td>
    			<td align="center">7</td>
    			<td align="center">9</td>
    			<td align="center">11</td>
    			<td align="center">13</td>
    			<td align="center">15</td>
  		</tr>
  		<tr>
    			<td align="center">Legalese</td>
    			<td align="center">Single</td>
    			<td align="center">11</td>
    			<td align="center">13</td>
    			<td align="center">16</td>
    			<td align="center">19</td>
    			<td align="center">21</td>
  		</tr>
  		<tr>
    			<td align="center">Pecking Order</td>
    			<td align="center">Single</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
    			<td align="center">17</td>
    			<td align="center">19</td>
    			<td align="center">22</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Big Wig</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
    			<th>Level 10</th>
    			<th>Level 11</th>
    			<th>Level 12</th>
  		</tr>
		<tr>
    			<td align="center">Power Trip</td>
    			<td align="center">Group</td>
    			<td align="center">10</td>
    			<td align="center">11</td>
    			<td align="center">13</td>
    			<td align="center">15</td>
    			<td align="center">16</td>
  		</tr>
  		<tr>
    			<td align="center">Finger Wag</td>
    			<td align="center">Single</td>
    			<td align="center">13</td>
    			<td align="center">15</td>
    			<td align="center">17</td>
    			<td align="center">19</td>
    			<td align="center">21</td>
  		</tr>
</table>

## Bossbots <a name="atk-dmg-boss"></a>
[[back to top](#contents)]

<table>
		<tr>
    			<th colspan="7">Bossbots</th>
  		</tr>
  		<tr>
    			<th colspan="2">Flunky</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 1</th>
    			<th>Level 2</th>
    			<th>Level 3</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
  		</tr>
		<tr>
    			<td align="center">Pound Key</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
  		</tr>
  		<tr>
    			<td align="center">Shred</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
  		</tr>
  		<tr>
    			<td align="center">Clip-on Tie</td>
    			<td align="center">Single</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">2</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Pencil Pusher</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 2</th>
    			<th>Level 3</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
  		</tr>
		<tr>
    			<td align="center">Fountain Pen</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
  		</tr>
  		<tr>
    			<td align="center">Rub-Out</td>
    			<td align="center">Single</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">12</td>
  		</tr>
  		<tr>
    			<td align="center">Finger Wag</td>
    			<td align="center">Single</td>
    			<td align="center">1</td>
    			<td align="center">2</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
  		</tr>
  		<tr>
    			<td align="center">Write-Off</td>
    			<td align="center">Single</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
  		</tr>
  		<tr>
    			<td align="center">Fill With Lead</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Yesman</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 3</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
  		</tr>
		<tr>
    			<td align="center">Rubber Stamp</td>
    			<td align="center">Single</td>
    			<td align="center">2</td>
    			<td align="center">2</td>
    			<td align="center">3</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
  		</tr>
  		<tr>
    			<td align="center">Razzle Dazzle</td>
    			<td align="center">Single</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
    			<td align="center">1</td>
  		</tr>
  		<tr>
    			<td align="center">Synergy</td>
    			<td align="center">Group</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
  		</tr>
  		<tr>
    			<td align="center">Tee-Off</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Micromanager</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 4</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
  		</tr>
		<tr>
    			<td align="center">Demotion</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
    			<td align="center">18</td>
  		</tr>
  		<tr>
    			<td align="center">Finger Wag</td>
    			<td align="center">Single</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
  		</tr>
  		<tr>
    			<td align="center">Fountain Pen</td>
    			<td align="center">Single</td>
    			<td align="center">3</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
  		</tr>
  		<tr>
    			<td align="center">Brain Storm</td>
    			<td align="center">Single</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
  		</tr>
  		<tr>
    			<td align="center">Buzz Word</td>
    			<td align="center">Single</td>
    			<td align="center">4</td>
    			<td align="center">6</td>
    			<td align="center">9</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Downsizer</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 5</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
  		</tr>
		<tr>
    			<td align="center">Canned</td>
    			<td align="center">Single</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
  		</tr>
  		<tr>
    			<td align="center">Downsize</td>
    			<td align="center">Single</td>
    			<td align="center">8</td>
    			<td align="center">9</td>
    			<td align="center">11</td>
    			<td align="center">13</td>
    			<td align="center">15</td>
  		</tr>
  		<tr>
    			<td align="center">Pink Slip</td>
    			<td align="center">Single</td>
    			<td align="center">4</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
  		</tr>
  		<tr>
    			<td align="center">Sacked</td>
    			<td align="center">Single</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
    			<td align="center">9</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Head Hunter</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 6</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
    			<th>Level 10</th>
  		</tr>
		<tr>
    			<td align="center">Fountain Pen</td>
    			<td align="center">Single</td>
    			<td align="center">5</td>
    			<td align="center">6</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
  		</tr>
  		<tr>
    			<td align="center">Glower Power</td>
    			<td align="center">Single</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
    			<td align="center">13</td>
  		</tr>
  		<tr>
    			<td align="center">Half Windsor</td>
    			<td align="center">Single</td>
    			<td align="center">8</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
    			<td align="center">14</td>
    			<td align="center">16</td>
  		</tr>
  		<tr>
    			<td align="center">Head Shrink</td>
    			<td align="center">Single</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
    			<td align="center">18</td>
    			<td align="center">21</td>
  		</tr>
  		<tr>
    			<td align="center">Rolodex</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
    			<td align="center">9</td>
    			<td align="center">10</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">Corporate Raider</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 7</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
    			<th>Level 10</th>
    			<th>Level 11</th>
  		</tr>
		<tr>
    			<td align="center">Canned</td>
    			<td align="center">Single</td>
    			<td align="center">6</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
    			<td align="center">9</td>
    			<td align="center">10</td>
  		</tr>
  		<tr>
    			<td align="center">Evil Eye</td>
    			<td align="center">Single</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
    			<td align="center">18</td>
    			<td align="center">21</td>
    			<td align="center">24</td>
  		</tr>
  		<tr>
    			<td align="center">Play Hardball</td>
    			<td align="center">Single</td>
    			<td align="center">7</td>
    			<td align="center">8</td>
    			<td align="center">12</td>
    			<td align="center">15</td>
    			<td align="center">16</td>
  		</tr>
  		<tr>
    			<td align="center">Power Tie</td>
    			<td align="center">Single</td>
    			<td align="center">10</td>
    			<td align="center">12</td>
    			<td align="center">14</td>
    			<td align="center">16</td>
    			<td align="center">18</td>
  		</tr>
		<tr>
			<th colspan="7"> </th>
		</tr>
		<tr>
    			<th colspan="2">The Big Cheese</th>
    			<th colspan="5">Damage</th>
  		</tr>
		<tr>
    			<th>Attack</th>
    			<th>Type</th>
    			<th>Level 8</th>
    			<th>Level 9</th>
    			<th>Level 10</th>
    			<th>Level 11</th>
    			<th>Level 12</th>
  		</tr>
		<tr>
    			<td align="center">Glower Power</td>
    			<td align="center">Single</td>
    			<td align="center">10, 14, 14</td>
    			<td align="center">12, 16, 15,</td>
    			<td align="center">15, 18, 17</td>
    			<td align="center">18, 20, 19</td>
    			<td align="center">20, 22, 20</td>
  		</tr>
  		<tr>
    			<td align="center">Tee-Off</td>
    			<td align="center">Single</td>
    			<td align="center">8</td>
    			<td align="center">11</td>
    			<td align="center">14</td>
    			<td align="center">17</td>
    			<td align="center">20</td>
  		</tr>
</table>

# Appendix C: Cog Attack Accuracies <a name="appendix-c"></a>

## Sellbots <a name="atk-acc-sell"></a>
[[back to top](#contents)]

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
			<td align="center">90</td>
			<td align="center">90</td>
			<td align="center">90</td>
			<td align="center">90</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Pound Key</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Double Talk</td>
			<td align="center">50</td>
			<td align="center">55</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
	        </tr>
	        <tr>
			<td align="center">Hot Air</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<th colspan="6"> </th>
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
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Pick Pocket</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Rolodex</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<td align="center">Double Talk</td>
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
			<th>Name Dropper</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
	        </tr>
	        <tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Rolodex</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Synergy</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<td align="center">Pick Pocket</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<th colspan="6"> </th>
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
			<td align="center">90</td>
			<td align="center">70</td>
			<td align="center">50</td>
			<td align="center">30</td>
			<td align="center">10</td>
	        </tr>
	        <tr>
			<td align="center">Fountain Pen</td>
			<td align="center">70</td>
			<td align="center">60</td>
			<td align="center">50</td>
			<td align="center">40</td>
			<td align="center">30</td>
	        </tr>
	        <tr>
			<td align="center">Filibuster</td>
			<td align="center">30</td>
			<td align="center">40</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
	        </tr>
	        <tr>
			<td align="center">Schmooze</td>
			<td align="center">55</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Half Windsor</td>
			<td align="center">50</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
	        </tr>
	        <tr>
			<td align="center">Quake</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
	        </tr>
	        <tr>
			<td align="center">Shake</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Tremor</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Hang-up</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
	        </tr>
	        <tr>
			<td align="center">Red Tape</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Paradigm Shift</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Power Trip</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
	        </tr>
	        <tr>
			<td align="center">Schmooze</td>
			<td align="center">55</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Tee Off</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<th colspan="6"> </th>
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
			<td align="center">55</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Razzle Dazzle</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">90</td>
			<td align="center">95</td>
	        </tr>
</table>

## Cashbots <a name="atk-acc-cash"></a>
[[back to top](#contents)]

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
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<td align="center">Bounce Check</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Clip-On Tie</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
	        <tr>
			<td align="center">Pick Pocket</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
	        </tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Freeze Assets</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Finger Wag</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Glower Power</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
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
			<td align="center">Freeze Assets</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Bounce Check</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Calculate</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Tabulate</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
	        </tr>
	        <tr>
			<td align="center">Write-Off</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
	        </tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Calculate</td>
			<td align="center">50</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
	        </tr>
	        <tr>
			<td align="center">Crunch</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
	        </tr>
	        <tr>
			<td align="center">Tabulate</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
			<td align="center">50</td>
	        </tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Market Crash</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
	        </tr>
	        <tr>
			<td align="center">Power Tie</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Chomp</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">90</td>
	        </tr>
	        <tr>
			<td align="center">Play Hardball</td>
			<td align="center">55</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">95</td>
	        </tr>
	        <tr>
			<td align="center">Write-Off</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">95</td>
	        </tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
	        </tr>
	        <tr>
			<td align="center">Tee-Off</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">90</td>
	        </tr>
</table>

## Lawbots <a name="atk-acc-law"></a>
[[back to top](#contents)]

<table>
		<tr>
			<th colspan="6">Lawbots</th>
		</tr>
		<tr>
			<th>Bottom Feeder</th>
			<th>Level 1</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
		</tr>
		<tr>
			<td align="center">Rubber Stamp</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
			<td align="center">95</td>
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
			<td align="center">Watercooler</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<td align="center">Pick Pocket</td>
			<td align="center">25</td>
			<td align="center">30</td>
			<td align="center">35</td>
			<td align="center">40</td>
			<td align="center">45</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
		</tr>
		<tr>
			<th>Blood Sucker</th>
			<th>Level 2</th>
			<th>Level 3</th>
			<th>Level 4</th>
			<th>Level 5</th>
			<th>Level 6</th>
		</tr>
		<tr>
			<td align="center">Eviction Notice</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Red Tape</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Withdrawal</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<td align="center">Liquidate</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Bounce Check</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Buzz Word</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Double Talk</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Jargon</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Mumbo Jumbo</td>
			<td align="center">50</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Red Tape</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Rolodex</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<td align="center">Hang Up</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
			<td align="center">75</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
		</tr>
		<tr>
			<th>Back Stabber</th>
			<th>Level 5</th>
			<th>Level 6</th>
			<th>Level 7</th>
			<th>Level 8</th>
			<th>Level 9</th>
		</tr>
		<tr>
			<td align="center">Guilt Trip</td>
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Restraining Order</td>
			<td align="center">50</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Finger Wag</td>
			<td align="center">50</td>
			<td align="center">55</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">80</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Quake</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
		</tr>
		<tr>
			<td align="center">Spin</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Write Off</td>
			<td align="center">60</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">90</td>
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
			<th colspan="6"> </th>
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
			<td align="center">60</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Jargon</td>
			<td align="center">60</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">90</td>
		</tr>
		<tr>
			<td align="center">Legalese</td>
			<td align="center">55</td>
			<td align="center">65</td>
			<td align="center">75</td>
			<td align="center">85</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<td align="center">Pecking Order</td>
			<td align="center">70</td>
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<th colspan="6"> </th>
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
			<td align="center">75</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">90</td>
			<td align="center">95</td>
		</tr>
		<tr>
			<td align="center">Finger Wag</td>
			<td align="center">80</td>
			<td align="center">85</td>
			<td align="center">85</td>
			<td align="center">85</td>
			<td align="center">90</td>
		</tr>
</table>

## Bossbots <a name="atk-acc-boss"></a>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
			<th colspan="6"> </th>
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
		
\* The Big Cheese was coded with three unused attacks. They were CigarSmoke, FloodTheMarket and SongAnd Dance. However, when the game selected one of these attacks, The Big Cheese would instead use his programmed default attack, which was Glower Power. Despite this, the game would still use the accuracy and damage values of the move that was internally selected (see [Cog Attack Accuracy](#cog-atk-acc) for more information), thus allowing Glower Power to have varying damage and accuracy values for the same level.
		
