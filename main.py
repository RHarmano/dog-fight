import numpy as np
import matplotlib.pyplot as plt
from src.boundsprop import Boundsprop
from src.fighterproperties import FighterProperties

#Initialize the fighters and simulation properties
box = Boundsprop([15,15,15])
f1 = FighterProperties([0,0], [1,1], [1,1,1])
f2 = FighterProperties([1,1], [3,2], [1,1,1])

fig = plt.figure(figsize=(15,15))
#Reorganize the fighters' coordinates so that the may be plotted
mapx = [f1.pos[0], f2.pos[0]]
xdir = [f1.direct[0], f2.direct[0]]
mapy = [f1.pos[1], f2.pos[1]]
ydir = [f1.direct[1], f2.direct[1]]
#Quiver plot to show the vectors
plt.quiver(mapx, mapy, xdir, ydir)
plt.show()