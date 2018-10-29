import numpy as np



class Element:

    def __init__(self, id, nodes, type=None):

        self.id = id
        self.nodes = nodes
        self.type = type
    
    def localNode(self, localId):
        #Returns node based on local id
        return self.nodes[self.nodes.keys()[localId-1]]
        
    def getLocalNode(self, globalID):
        return self.nodes.keys().index(globalID)+1
        
    def getFaceNumber(self, nIds):
        #nIds = [node.id for node in nodes]
        localNIds = [self.getLocalNode(nId) for nId in nIds]
        
        if self.type=='Hex':
            F1 = [1,2,3,4]
            F2 = [5,6,7,8]
            F3 = [1,2,5,6]
            F4 = [2,3,6,7]
            F5 = [3,4,7,8]
            F6 = [1,4,5,8]

            faceList = []
            for nId in localNIds:
                if nId in F1:
                    faceList.append(1)
                if nId in F2:
                    faceList.append(2)
                if nId in F3:
                    faceList.append(3)
                if nId in F4:
                    faceList.append(4)
                if nId in F5:
                    faceList.append(5)
                if nId in F6:
                    faceList.append(6)
                    
        elif self.type=='Tet':
            F1 = [1,2,3]
            F2 = [1,2,4]
            F3 = [2,3,4]
            F4 = [1,3,4]

            faceList1 = []
            faceList2 = []
        
            if localNIds[0] in F1:
                faceList1.append(1)
            if localNIds[0] in F2:
                faceList1.append(2)
            if localNIds[0] in F3:
                faceList1.append(3)
            if localNIds[0] in F4:
                faceList1.append(4)
            
            if localNIds[1] in F1:
                faceList2.append(1)
            if localNIds[1] in F2:
                faceList2.append(2)
            if localNIds[1] in F3:
                faceList2.append(3)
            if localNIds[1] in F4:
                faceList2.append(4)
            #print 'elem # {}'.format(self.id)
            #print 'globalNIds: {}'.format(nIds)
            #print 'localNIds: {}'.format(localNIds)
            for face in faceList1:
                if not face in faceList2:
                    #print face
                    return face
            
            return None
            
            
            #if checkEqual(faceList):
            #   return faceList[0]
                
def checkEqual(iterator):
    return len(set(iterator)) <= 1