# toontown.py

Simplifies common Toontown-related Panda3D tasks.

## Set-up

Put toontown.py in your working directory (or make sure it's on the module search path).

## Example Usage

```python
import direct.directbase.DirectStart
import toontown

# Creating a cog ...
cog = toontown.load_cog('Mr. Hollywoood')
cog.loop('walk')
cog.setPos(-14, -20, 1.6)
cog.setH(-180)

# Creating a skelecog ...
skelecog = toontown.load_cog('The Big Cheese', skelecog=True)
skelecog.loop('neutral')
skelecog.setPos(-7, -20, 1.6)
skelecog.setH(-180)

# Creating a toon ...
toon = toontown.Toon('horse', 'm', 'n', 'n', 'l', 'm')
toon.set_color('Blue')
toon.set_shirt('phase_4/maps/ContestFishtankShirt1.jpg')
toon.set_bottom('phase_3/maps/desat_shorts_10.jpg')
toon.loop('neutral')
toon.setPos(-2, -20, 1.6)
toon.setH(-180)

# Creating a boss ...
boss = toontown.load_cog('VP')
boss.loop('Ff_neutral')
boss.setPos(-10, 10, 1.6)

base.trackball.node().setPos(7, 55, -10)
run()
```

![Result](http://i.imgur.com/9OfmPws.png)
