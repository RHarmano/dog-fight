import numpy as np
from numpy.random import uniform

#every fighter is generated with a series of parameters. pos and direct are arrays in R2/R3, and traits is a tuple of the fighter's speed, turning capability and experience. These will be explained later
class FighterProperties:
    def __init__(self, pos, direct, traits):
        self.pos = pos
        self.direct = direct
        self.flyspeed = traits[0]
        self.turnspeed = traits[1]
        self.goodfighter = traits[2]
    def flight_step(self, pos, direction, flyspeed):
        """calculates what the next position will be for a fighter"""
        dirmag = 0
        for i in range(0,len(direction)):
            dirmag = dirmag + direction[i]**2
        dirmag = dirmag**0.5
        bhat = direction/dirmag
        nextpos = pos + bhat*flyspeed
        return nextpos, bhat
    def execute_move(self, pos, direction, flyspeed):
        """executes a movement towards the leading fighter"""
        futurepos, bhat = self.flight_step(pos, direction, flyspeed)
        return futurepos, bhat
    def shake_run(self, boundx, boundy, pos, flyspeed, turnspeed):
        """frontrunner tries to shake tailing fighter, moving sporadically"""
        futurepos, bhat = self.execute_move(pos, uniform(low=0,high=2,size=(2,))*turnspeed, flyspeed)
        if futurepos[0] > 0 and futurepos[0] < boundx and futurepos[1] > 0 and futurepos[1] < boundy:
            return futurepos, bhat
        else:
            return self.shake_run(boundx, boundy, pos, flyspeed, turnspeed)
    def poor_dog_fighter(self, follow_pos, lead_pos, direction, turnspeed, flyspeed):
        """poor dogfighter; fighter doesn't see where the other object is going"""
        newpos, bhat = self.execute_move(follow_pos, direction + (lead_pos - follow_pos - direction)*turnspeed, flyspeed)
        return newpos, bhat
    def good_dog_fighter(self, follow_pos, lead_pos, follow_dir, lead_dir, fighterturnspeed, fighterflyspeed, targetflyspeed):
        """good dogfighter; figures out where the target will be and goes for that point"""
        npos2, dummy = self.flight_step(lead_pos, lead_dir, targetflyspeed)
        newpos, bhat = self.execute_move(follow_pos, follow_dir + (npos2 - follow_pos - follow_dir)*fighterturnspeed, fighterflyspeed)
        return newpos, bhat