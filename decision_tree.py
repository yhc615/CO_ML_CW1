"""
Decision-tree Class Definition
"""

class Tree:
    def __init__(self,label, isLeaf=False):
        self.nodeLabel = None
        self.nodekids = []
        self.leafLabel = None
        if isLeaf:
            self.leafLabel = label
        else:
            self.nodeLabel = label

    def getKids(self):
        return self.kids

    def setKid(self, i, node):
        if k in [0,1]:
            self.kids[i] = node
        else:
            raise Exception("Out of range")
    def printTree(self):



def leaf(x):
    return Tree(x, True)

def tree(x):
    return Tree(x)