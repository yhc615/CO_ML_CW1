import random

def predictor(x, dtl):
	attrVal = x[dtl.getNodeLabel()]
	kids = dtl.getKids()
	if kids[attrVal].getIsLeaf():
		return kids[attrVal].getLeafLabel()
	else:
		return predictor(x, kids[attrVal])

def ambiguityStrat(arr, strat):
	if 1 in arr:
		positives = [i+1 for i, x in enumerate(arr) if x]
		if strat==0:
			return random.choice(positives)
		elif strat==1:
			return arr.index(1)+1
		elif strat==2:
			if len(positives)>1 and 6 in positives:
				positives.remove(6)
			if len(positives)>1 and 1 in positives:
				return 1
			return random.choice(positives)
	return random.choice(list(range(1,7)))

def testTrees(T, x2):
	predictions = []
	for x in x2:
		emotePredicts = [predictor(x, tree) for tree in T]
		predictions.append(ambiguityStrat(emotePredicts,0))
	return predictions