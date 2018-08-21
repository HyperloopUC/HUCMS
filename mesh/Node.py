import numpy as np

class Node(np.ndarray):

    def __new__(cls, id, coords, notes=''):

        holder = [coords[0], coords[1]]

        if len(coords)==2:
            holder.append(0.0)
        else:
            holder.append(float(coords[2]))
        array = np.asarray(holder, dtype=np.float64).view(cls)

        array.id = id
        array.notes = notes

        return array

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        return self[2]

    #@property
    #def id(self):
    #    return self.id

    @x.setter
    def x(self, x):
        self[0] = x

    @y.setter
    def y(self, y):
        self[1] = y

    @z.setter
    def z(self, z):
        self[2] = z

    #@id.setter
    #def id(self, id):
    #    self.id = id