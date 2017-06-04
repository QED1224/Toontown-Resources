## Disclaimer 

This is the testing branch of Toontown Resources. In this file, any findings, tests, or other relevant information that pertains to unanswered or incomplete questions in the master branch, may be found here. If you are looking for the guide itself, go to the master branch and look at README.md. At the time this file is created, the primary focus is on Doodle T&T 4.

What is known to be correct for Doodle 4 at the time of writing (May 8th 2017)

-The `setFatigue` equation given appears to be correct for when the Doodle is called into battle. In the Estate however, there appears to be variance in how much `setFatigue` will increase by, even if a Doodle performs a trick with max `aptitude`. This variance may be caused by the following function, although further testing is required.

```python
def doDrift(curValue, timeToMedian, dt = float(dt)):
    newValue = curValue + dt / (timeToMedian * 7200)
    return clampScalar(newValue, 0.0, 1.0)
```

-Credit to Yumeko for help with Doodle code and testing

May 21st 2017

-Need to clarify variance on doodles in estate

June 4th 2017

-Still need to clarify variance on Doodles in estate (unlikely to happen for awhile)

-Check how multiple Traps play out with Trap SOS (ex, Clerk Penny + TNT + Lure)

-Check out how mixing Sound SOS with normal Sound works

-Check if stuns "carry-over" for V2.0 Cogs. For example, suppose you use $10 Bill + Birthday Cake + Grand Piano on a Level 10 V2.0 Cog. Would the Grand Piano have a +40 stun boost?
