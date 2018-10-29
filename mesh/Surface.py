import numpy as np

class Surface:

    def __init__(self, name, elementNIds, type=None):
        self.elementNIds = elementNIds
        
    def generate(self, elements):
        self.faces = {}
        for elId, nIds in self.elementNIds.iteritems():
            self.faces[elId] = elements[elId].getFaceNumber(nIds)