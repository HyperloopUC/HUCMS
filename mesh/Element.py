import numpy as np



class Element:

    def __init__(self, id, nodes, type=None):

        self.id = id
        self.nodes = nodes
        self.type = type
