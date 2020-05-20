#every fighter is generated with a series of parameters. pos and direct are arrays in R2/R3, and traits is a tuple of the fighter's speed, turning capability and experience. These will be explained later
class FighterProperties:
    def __init__(self, pos, direct, traits):
        self.pos = pos
        self.direct = direct
        self.flyspeed = traits[0]
        self.turnspeed = traits[1]
        self.goodfighter = traits[2]