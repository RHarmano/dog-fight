import numpy as np

class Boundsprop:
    def __init__(self, dims):
        x = dims[0]
        y = dims[1]
        if len(dims) == 3:
            z = dims[2]
            x, y, z = np.meshgrid(x, y, z, indexing='ij')
            self.x = x
            self.y = y
            self.z = z
        elif len(dims) == 2:
            x, y = np.meshgrid(x, y)
            self.x = x
            self.y = y