import numpy as np
import matplotlib.pyplot as plt

class boundsprop:
    def __init__(self, dims):
        x = dims[0]
        y = dims[1]
        if len(dims) == 3:
            z = dims[2]

        x, y, z = np.meshgrid(x, y, z, indexing='ij')
        self.x = x
        self.y = y
        self.z = z

#every fighter is generated with a series of parameters. pos and direct are arrays in R2/R3, and traits is a tuple of the fighter's speed, turning capability and experience. These will be explained later
class fighterproperties:
    def __init__(self, pos, direct, traits):
        self.pos = pos
        self.direct = direct
        self.flyspeed = traits[0]
        self.turnspeed = traits[1]
        self.goodfighter = traits[2]

#calculates what the next position will be for a fighter
def flightstep(pos, direction, flyspeed):
    dirmag = 0
    for i in range(0,len(direction)):
        dirmag = dirmag + direction[i]**2
    dirmag = dirmag**0.5
    bhat = direction/dirmag
    nextpos = pos + bhat*flyspeed
    return nextpos

def executemove(pos, direction, flyspeed):
    futurepos = flightstep(pos, direction, flyspeed)
    return futurepos

#poor dogfighter; fighter doesn't see where the other object is going
def pdogfight(pos1, pos2, direction, turnspeed):
    idealray = pos2 - pos1
    direction = direction + (idealray-direction)*turnspeed
    return direction

#good dogfighter; figures out where the target will be and goes for that point
def gdogfight(pos1, pos2, dir1, dir2, fighterturnspeed, targetflyspeed):
    npos2 = flightstep(pos2, dir2, targetflyspeed)
    idealray = npos2 - pos1
    dir1 = dir1 + (idealray-dir1)*fighterturnspeed
    return dir1   

box = boundsprop([15,15,15])
f1 = fighterproperties([0,0], [1,1], [1,1,1])
f2 = fighterproperties([1,1], [3,2], [1,1,1])

fig = plt.figure(figsize=(15,15))
mapx = [f1.pos[0], f2.pos[0]]
xdir = [f1.direct[0], f2.direct[0]]
mapy = [f1.pos[1], f2.pos[1]]
ydir = [f1.direct[1], f2.direct[1]]
plt.quiver(mapx, mapy, xdir, ydir)
plt.show()