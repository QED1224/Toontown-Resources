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

-Need to add logfile for Cog total damages
-Need to clarify variance on doodles in estate
-Need to actually add list of all toontask recovery rates
