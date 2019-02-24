import os
import sys
from collections import OrderedDict

sys.path.append(r"D:")
print 'Initializing HUCMS'
import numpy as np
from HUCMS.mesh.Node import Node
from HUCMS.mesh.Element import Element
from HUCMS.mesh.Surface import Surface

class Mesh:

    def __init__(self, nodes=None, elements=None, nodeSets=None, elSets=None, notes=None):

        self.nodes = nodes
        self.elements = elements
        self.nodeSets = nodeSets
        self.elSets = elSets
        self.notes = notes

    def localNode(self, nNum):
        return ()
    
    def compareNodes(self, nodeOne, nodeTwo):

        # 0: Different nodes
        # 1: Matching ids, not matching coordinates
        # 2: Matching ids and coordinates. Same node
        # 4: Non-matching ids, same coordinate. Recommend merging.

        noneMatch = True
        coordMatch = False
        matchX = False
        matchY = False
        matchZ = False
        matchId = False

        if nodeOne.id == nodeTwo.id:
            matchId = True
            noneMatch = False
        if nodeOne.x == nodeTwo.x:
            matchX = True
            noneMatch = False
        if nodeOne.y == nodeTwo.y:
            matchY = True
            noneMatch = False
        if nodeOne.z == nodeTwo.z:
            matchZ = True
            noneMatch = False

        if matchX and matchY and matchZ:
            coordMatch = True
        if noneMatch:
            return 0
        if matchId==False and coordMatch==False:
            return 0
        if matchX and matchY and matchZ:
            if matchId:
                return 2
            else:
                return 4
        else:
            return 1

    @classmethod
    def fromOptistruct(self, path):
        self.partName = path.strip('mesh_').strip('.fem')
        self.inPath = path
        commentLines = []
        nodeDict = {}
        elementDict = {}
        surfDict = {}
        sets = {}
        with open(path) as mesh_file:
            meshFileLines = mesh_file.readlines()
            iterLines = iter(meshFileLines)
            for line in iterLines:
                if line.startswith('$$'):
                    commentLines.append(line)
                elif line.startswith('$HMSET'):
                    defineLine = line.split()
                    setType = defineLine[2]
                    setName = defineLine[3].strip('"')
                    if int(setType) == 1:
                        setType = 'Node'
                    elif int(setType) == 2:
                        setType = 'Element'

                    line = next(iterLines)
                    line = next(iterLines)
                    if line.startswith('SET'):
                        firstLine = line.split()
                        #print firstLine[3].split(',')
                        ids = [int(id) for id in firstLine[3].strip().split(',') if id != '']

                    line = next(iterLines)
                    while not line.startswith('$'):
                        #print line
                        for id in line.strip().split(','):
                            #print line.strip().split(',')
                            if id != '':
                                ids.append(int(id))
                        line = next(iterLines)

                    sets[setName] = Set(setType, setName, ids)


                elif line.startswith('GRID'):
                    #focus_line = [line[:4], int(line[4:24]), float(line[24:32]), float(line[32:40]), float(line[40:])]
                    focus_line = line.split(',')
                    nodeDict[int(focus_line[1])] = Node(focus_line[1], [focus_line[3], focus_line[4], focus_line[5]])
                elif line.startswith('CHEXA'):
                    focus_line = line.split(',')
                    next_line = next(iterLines)
                    elId = int(focus_line[1])
                    nIdList = focus_line[3:-1] + next_line.split(',')[1:-1]
                    
                    elNodes = OrderedDict()
                    for nId in nIdList:
                        elNodes[int(nId)] = nodeDict[int(nId)]
                    if len(elNodes) == 8:
                        elType = 'Hex'
                    else:
                        elType = None
                    elType='Hex'
                    #nodes_list = [nodeDict[int(nid)] for nid in nid_list]
                    elementDict[elId] = Element(elId, elNodes,type=elType)
                elif line.startswith('CQUAD4'):
                    focusLine = line.split(',')
                    elId = int(focusLine[1])
                    nIdList = focusLine[3:-1]

                    elNodes = OrderedDict()
                    for nId in nIdList:
                        elNodes[int(nId)] = nodeDict[int(nId)]
                    if len(elNodes)==8:
                        elType='Hex'
                    elif len(elNodes)==4:
                        elType='Tet'
                    else:
                        elType=None
                    elType='Quad'
                    elementDict[elId] = Element(elId, elNodes,type=elType)
                elif line.startswith('CPENTA'):
                    focusLine = line.split(',')
                    elId = int(focusLine[1])
                    nIdList = focusLine[3:-1]

                    elNodes = OrderedDict()
                    for nId in nIdList:
                        elNodes[int(nId)] = nodeDict[int(nId)]
                    if len(elNodes)==8:
                        elType='Hex'
                    elif len(elNodes)==4:
                        elType='Tet'
                    else:
                        elType=None
                    elType='Penta'
                    elementDict[elId] = Element(elId, elNodes,type=elType)
                elif line.startswith('CTRIA3'):
                    focusLine = line.split(',')
                    elId = int(focusLine[1])
                    nIdList = focusLine[3:-1]

                    elNodes = OrderedDict()
                    for nId in nIdList:
                        elNodes[int(nId)] = nodeDict[int(nId)]
                    if len(elNodes)==8:
                        elType='Hex'
                    elif len(elNodes)==4:
                        elType='Tet'
                    else:
                        elType=None
                    elType='Tria'
                    elementDict[elId] = Element(elId, elNodes,type=elType)
                elif line.startswith('CTETRA'):
                    focusLine = line.split(',')
                    elId = int(focusLine[1])
                    nIdList = focusLine[3:-1]

                    elNodes = OrderedDict()
                    for nId in nIdList:
                        elNodes[int(nId)] = nodeDict[int(nId)]
                    if len(elNodes)==8:
                        elType='Hex'
                    elif len(elNodes)==4:
                        elType='Tet'
                    else:
                        elType=None
                    elementDict[elId] = Element(elId, elNodes,type=elType)
                    elType='Tet'
                elif line.startswith('$HMNAME CSURF'):
                    surfElems = {}
                    
                    name = line.split('"')[1]
                    currLine = next(iterLines)
                    while not '+' in currLine:
                        currLine = next(iterLines)
                    splitLine = currLine.split(',')
                    elId = int(splitLine[1])
                    nIds = [int(splitLine[2]), int(splitLine[3])]
                    surfElems[elId] = nIds
                    currLine = next(iterLines)
                    while currLine.startswith('+'):
                        
                        splitLine = currLine.split(',')
                        
                        elId = int(splitLine[1])
                        nIds = [int(splitLine[2]), int(splitLine[3])]
                        surfElems[elId] = nIds
                        currLine = next(iterLines)
                        
                    surfDict[name] = Surface(name, surfElems)
                    
                else:
                    commentLines.append(line)

                self.sets = sets
                self.surfaces = surfDict

        return Mesh(nodeDict, elementDict)

    def toAbaqus(self):
        outName = os.path.splitext(self.inPath)[0] + '.inp'
        with open(outName, 'w') as out_mesh:
            out_mesh.write('*NODE, NSET=allnodes\n')

            for nId, node in self.nodes.iteritems():
                out_mesh.write('{}, {}, {}, {}\n'.format(node.id, node.x, node.y, node.z))

            out_mesh.write('*ELEMENT, ELSET={}, TYPE=C3D4\n'.format(self.partName))

            for elId, element in self.elements.iteritems():
                if element.type == 'Tet':
                    elLine = '{}'.format(element.id)

                    for nId, node in element.nodes.iteritems():
                        #print element.nodes
                        elLine += ', {}'.format(nId)
                    elLine += '\n'
                    out_mesh.write(elLine)
            
            out_mesh.write('*ELEMENT, ELSET={}, TYPE=C3D6\n'.format(self.partName))

            for elId, element in self.elements.iteritems():
                if element.type == 'Penta':
                    
                    elLine = '{}'.format(element.id)
                    
                    for nId, node in element.nodes.iteritems():
                        #print element.nodes
                        elLine += ', {}'.format(nId)
                    elLine += '\n'
                    out_mesh.write(elLine)
            
            out_mesh.write('*ELEMENT, ELSET={}, TYPE=C3D8\n'.format(self.partName))

            for elId, element in self.elements.iteritems():
                if element.type == 'Hex':
                    
                    elLine = '{}'.format(element.id)
                    
                    for nId, node in element.nodes.iteritems():
                        #print element.nodes
                        elLine += ', {}'.format(nId)
                    elLine += '\n'
                    out_mesh.write(elLine)
                
            out_mesh.write('*ELEMENT, ELSET={}, TYPE=S3\n'.format(self.partName))

            for elId, element in self.elements.iteritems():
                if element.type == 'Tria':
                    elLine = '{}'.format(element.id)

                    for nId, node in element.nodes.iteritems():
                        #print element.nodes
                        elLine += ', {}'.format(nId)
                    elLine += '\n'
                    out_mesh.write(elLine)
            
            out_mesh.write('*ELEMENT, ELSET={}, TYPE=S4\n'.format(self.partName))

            for elId, element in self.elements.iteritems():
                if element.type == 'Quad':
                    elLine = '{}'.format(element.id)

                    for nId, node in element.nodes.iteritems():
                        #print element.nodes
                        elLine += ', {}'.format(nId)
                    elLine += '\n'
                    out_mesh.write(elLine)

            for setName, set in self.sets.iteritems():

                if set.type == 'Node':
                    out_mesh.write('*NSET, NSET = {}\n'.format(setName))
                elif set.type == 'Element':
                    out_mesh.write('*ELSET, ELSET = {}\n'.format(setName))

                splitIds = [set.ids[ind:ind+16] for ind in range(0,len(set.ids),16)]

                for idLine in splitIds:
                    out_mesh.write(','.join([str(id) for id in idLine])+',\n')
            
            for surfaceName, surface in self.surfaces.iteritems():
                surface.generate(self.elements)
                out_mesh.write('*Surface, type=ELEMENT, name={}\n'.format(surfaceName))
                for elId, faceId in surface.faces.iteritems():
                    out_mesh.write('  {}, S{}\n'.format(elId, faceId))
                


class Set:

    def __init__(self, type, name, ids):

        self.type = type
        self.name = name
        self.ids = ids
"""
print __name__
if __name__ == '__main__':
    testMesh = Mesh.fromOptistruct(r"D:\Fly UC\FEA\Geometry\180829_ExtendedWidth\HM\Split_Mesh_Files\airfoil_4.fem")
    testMesh.toAbaqus()

"""



