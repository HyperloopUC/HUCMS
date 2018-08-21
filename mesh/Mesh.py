import sys
sys.path.append(r"D:\Projects\Hyperloop UC")

import numpy as np
from HUCMS.mesh.Node import Node
from HUCMS.mesh.Element import Element

class Mesh:

    def __init__(self, elements):

        allNodesList = [elements[0].nodes[0]]
        print 'umm'

        for element in elements:
            for node in element.nodes:
                for node_in in allNodesList:
                    compareResult = self.compareNodes(node, node_in)
                    if compareResult == 0:
                        allNodesList.append(node)
        self.elements = elements
        self.allNodes = allNodesList


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
        commentLines = []
        nodeDict = {}
        elementList = []
        with open(path) as mesh_file:
            meshFileLines = mesh_file.readlines()

            for ind, line in enumerate(meshFileLines):
                if line.startswith('$'):
                    commentLines.append(line)
                elif line.startswith('GRID'):
                    focus_line = [line[:4], int(line[4:24]), float(line[24:32]), float(line[32:40]), float(line[40:])]
                    nodeDict[focus_line[1]] = Node(focus_line[1], [focus_line[2], focus_line[3], focus_line[4]])
                elif line.startswith('CHEXA'):
                    focus_line = line.split()
                    next_line = meshFileLines[ind + 1]
                    id = int(focus_line[1])
                    nid_list = focus_line[3:] + next_line.split()[1:]
                    nodes_list = [nodeDict[int(nid)] for nid in nid_list]
                    elementList.append(Element(id, nodes_list))

        return Mesh(elementList)

    def toAbaqus(self):

        with open('output.inp', 'w') as out_mesh:
            out_mesh.write('*NODE\n')
            print len(self.allNodes)
            for node in self.allNodes:
                out_mesh.write('{}, {}, {}, {}\n'.format(node.id, node.x, node.y, node.z))

            out_mesh.write('*ELEMENT, TYPE=C3D8\n')

            for element in self.elements:

                out_mesh.write('{}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(element.id, element.nodes[0].id, element.nodes[1].id, element.nodes[2].id, element.nodes[3].id, element.nodes[4].id, element.nodes[5].id, element.nodes[6].id, element.nodes[7].id))


if __name__ == '__main__':
    testMesh = Mesh.fromOptistruct(r"D:\Projects\PyCharm Projects\mod_sim\test_mesh.fem")
    testMesh.toAbaqus()
    print testMesh
    print 'hello'





