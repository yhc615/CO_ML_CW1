"""
Decision-tree Class Definition
"""

class Tree:
	def __init__(self,label, isLeaf=False):
		self.nodeOp = None
		self.nodeKids = [None,None]
		self.isLeaf = isLeaf
		self.leafLabel = None
		if self.isLeaf:
			self.leafLabel = label
		else:
			self.nodeOp = label

	def getNodeLabel(self):
		return self.nodeOp

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

	def printTree(self): #DELETE LATER IF __STR__ works!
		print("InnerNode: AU{}".format(self.nodeOp+1))
		for k in self.nodeKids:
			if k:
				if k.isLeaf:
					print("--Leaf: {}".format(k.leafLabel))
		for k in self.nodeKids:
			if k:    
				if not k.isLeaf:
					k.printTree()

	def __str__(self,depth=0):
		output = ""
		#descent right branch
		if self.nodeKids[1] != None:
			output += self.nodeKids[1].__str__(depth+1)
		#print value of current node
		if not self.isLeaf:
			output += "\n" + ("|"*depth) + "AU{}".format(self.nodeOp+1)
		else:
			output += "\n" + ("|"*depth) + "Leaf: {}".format(self.leafLabel)
		#descend left branch
		if self.nodeKids[0] != None:
			output += self.nodeKids[0].__str__(depth+1)
		return output

def leaf(x):
	return Tree(x, True)

def tree(x):
	return Tree(x)