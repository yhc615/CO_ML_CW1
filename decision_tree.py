"""
Decision-tree Class Definition
"""

class Tree:
    def __init__(self,label, isLeaf=False):
        self.nodeLabel = None
        self.nodeKids = [None,None]
        self.isLeaf = isLeaf
        self.leafLabel = None
        if self.isLeaf:
            self.leafLabel = label
        else:
            self.nodeLabel = label

    def getNodeLabel(self):
        return self.nodeLabel

    def getIsLeaf(self):
        return self.isLeaf

    def getLeafLabel(self):
        return self.leafLabel

    def getKids(self):
        return self.nodeKids

    def setKid(self, i, node):
        if i in [0,1]:
            self.nodeKids[i] = node
        else:
            raise Exception("Out of range")
    def printTree(self):
        print("InnerNode: AU{}".format(self.nodeLabel+1))
        for k in self.nodeKids:
            if k.isLeaf:
                print("--Leaf: {}".format(k.leafLabel))
        for k in self.nodeKids:
            if not k.isLeaf:
                k.printTree()
        


def leaf(x):
    return Tree(x, True)

def tree(x):
    return Tree(x)