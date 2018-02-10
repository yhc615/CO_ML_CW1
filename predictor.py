def predictor(x, dtl):
	attrVal = x[dtl.getNodeLabel()]
	kids = dtl.getKids()
	if kids[attrVal].getIsLeaf():
		return kids[attrVal].getLeafLabel()
	else:
		return predictor(x, kids[attrVal])

def ambiguityStrat(arr):
	if 1 in arr:
		return arr.index(1)+1
	return 0

def testTrees(T, x2):
	predictions = []
	for x in x2:
		emotePredicts = [predictor(x, tree) for tree in T]
		predictions.append(ambiguityStrat(emotePredicts))
	return predictions