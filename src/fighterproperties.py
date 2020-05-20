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
    def shake_run(self, pos, flyspeed, turnspeed):
        """frontrunner tries to shake tailing fighter, moving sporadically"""
        randir = uniform(low=0,high=2,size=(2,))*turnspeed
        newpos, bhat = self.execute_move(pos, randir, flyspeed)
        return newpos, bhat
    def poor_dog_fighter(self, follow_pos, lead_pos, direction, turnspeed, flyspeed):
        """poor dogfighter; fighter doesn't see where the other object is going"""
        idealray = lead_pos - follow_pos
        direction = direction + (idealray-direction)*turnspeed
        newpos, bhat = self.execute_move(follow_pos, direction, flyspeed)
        return newpos, bhat
    def good_dog_fighter(self, follow_pos, lead_pos, follow_dir, lead_dir, fighterturnspeed, fighterflyspeed, targetflyspeed):
        """good dogfighter; figures out where the target will be and goes for that point"""
        npos2, dummy = self.flight_step(lead_pos, lead_dir, targetflyspeed)
        idealray = npos2 - follow_pos
        follow_dir = follow_dir + (idealray - follow_dir)*fighterturnspeed
        newpos, bhat = self.execute_move(follow_pos, follow_dir, fighterflyspeed)
        return newpos, bhat