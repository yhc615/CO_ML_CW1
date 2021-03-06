from math import log2
from decision_tree import *

def MAJORITY_VALUE(inp):
	return max(inp, key=inp.count)

def calcEntropy(p, n):
	if(not p or not n):
		return 0
	elif(p==n):
		return 1;
	return -(p/(p+n))*log2(p/(p+n))-(n/(p+n))*log2(n/(p+n))

def CHOOSE_BEST_DECISION_ATTR(ex,attr,b_targets):
	pEx, nEx = [e for i,e in enumerate(ex) if b_targets[i]], [e for i,e in enumerate(ex) if not b_targets[i]]
	p, n = len(pEx), len(nEx)
	entropy = calcEntropy(p,n)
	bestAttr = 0
	bestGain = 0
	for i,a in enumerate(attr):
		p0,n0 = len([e[i] for e in pEx if not e[i]]), len([e[i] for e in nEx if not e[i]])
		p1,n1 = len([e[i] for e in pEx if e[i]]), len([e[i] for e in nEx if e[i]])
		aRemainder = ((p0+n0)/(p+n))*calcEntropy(p0,n0) + ((p1+n1)/(p+n))*calcEntropy(p1,n1)
		aGain = entropy-aRemainder
		if aGain>bestGain or i==0:
			bestGain = aGain
			bestAttr = a
	return bestAttr

def DECISION_TREE_LEARNING(examples, attributes, binary_targets):
	if(binary_targets[1:] == binary_targets[:-1]):
		return leaf(binary_targets[0])
	elif not attributes:
		return leaf(MAJORITY_VALUE(binary_targets))
	else:
		best_attribute = CHOOSE_BEST_DECISION_ATTR(examples,attributes,binary_targets)
		attributes.remove(best_attribute)
		root = tree(best_attribute)
		for v in [0,1]:
			newAttr = attributes[:]
			v_examples, v_binary_targets = [e for e in examples if e[best_attribute]==v],[binary_targets[i] for i,e in enumerate(examples) if e[best_attribute]==v]
			if not v_examples:
				nodeToAdd = leaf(MAJORITY_VALUE(binary_targets))
			else:
				nodeToAdd = DECISION_TREE_LEARNING(v_examples, newAttr, v_binary_targets)
			root.setKid(v, nodeToAdd)
		return root