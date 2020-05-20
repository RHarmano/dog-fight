import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from src.boundsprop import Boundsprop
from src.fighterproperties import FighterProperties

#Initialize the fighters and simulation properties
if __name__ == "__main__":
    dims = np.array([15,15])
    lead_pos = np.array([3,3])
    lead_dir = np.array([1,1])
    follow_pos = np.array([0,0])
    follow_dir = np.array([3,2])
    traits1 = np.array([1,1,1])
    traits2 = np.array([1,1,1])

    box = Boundsprop(dims)
    f1 = FighterProperties(lead_pos, lead_dir, traits1)
    f2 = FighterProperties(follow_pos, follow_dir, traits2)

    boundx = dims[0]
    boundy = dims[1]

    fig, ax = plt.subplots(1,1)
    ax.set_xlim([0,boundx])
    ax.set_ylim([0,boundy])
    #Quiver plot to show the vectors
    Q = plt.quiver([f1.pos[0], f2.pos[0]], [f1.pos[1], f2.pos[1]], [f1.direct[0], f2.direct[0]], [f1.direct[1], f2.direct[1]])
    
    def update_fig(num, Q, f1, f2):
        """ Updates fighter positions on the figure """
        f1.pos, f1.direct = f1.shake_run(boundx, boundy, f1.pos, f1.flyspeed, f1.turnspeed)
        if f2.goodfighter == 1:
            f2.pos, f2.direct = f2.good_dog_fighter(f2.pos, f1.pos, f2.direct, f1.direct, f2.turnspeed, f2.flyspeed, f1.flyspeed)
        elif f2.goodfighter == 0:
            f2.pos, f2.direct = f2.poor_dog_fighter(f2.pos, f1.pos, f2.direct, f2.turnspeed, f2.flyspeed)
        ax.clear()
        ax.set_xlim([0,15])
        ax.set_ylim([0,15])
        Q = ax.quiver([f1.pos[0], f2.pos[0]], [f1.pos[1], f2.pos[1]], [f1.direct[0], f2.direct[0]], [f1.direct[1], f2.direct[1]])
        return Q,

    anim = animation.FuncAnimation(fig, update_fig, fargs=(Q, f1, f2), interval=100, blit=False)
    plt.show()