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