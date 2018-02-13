import random

def predictor(x, dtl, depth):
	attrVal = x[dtl.getNodeOp()]
	kids = dtl.getKids()
	if kids[attrVal].getIsLeaf():
		return kids[attrVal].getLeafClass(), depth
	else:
		return predictor(x, kids[attrVal], depth+1)

def ambiguityStrat(matches, depths, strat):
	if 1 in matches:
		positives = [i+1 for i, x in enumerate(matches) if x]
		depths = [depths[i] for i, x in enumerate(matches) if x]
		if strat==0:
			return random.choice(positives)
		elif strat==1:
			return matches.index(1)+1
		elif strat==2:
			if len(positives)>1 and 6 in positives:
				positives.remove(6)
			if len(positives)>1 and 5 in positives:
				positives.remove(5)
			return random.choice(positives)
		elif strat==3:
			return positives[depths.index(min(depths))]

	return random.choice(list(range(1,7)))

def testTrees(T, x2):
	predictions = []
	for x in x2:
		emotePredicts = [predictor(x, tree, 0) for tree in T]
		e,d = zip(*emotePredicts)
		predictions.append(ambiguityStrat(e,d,3))
	return predictions