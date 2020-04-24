import numpy as np

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
