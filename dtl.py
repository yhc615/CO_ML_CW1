def MAJORITY_VALUE(inp):
	return max(inp, key=inp.count)

def CHOOSE_BEST_DECISION_ATTR(ex,attr,b_targets):
	return 0

def DTL(examples, attributes, binary_targets):
	if(binary_targets[1:] == binary_targets[:-1]):
		return leaf(binary_targets[0])
	elif(attributes is empty):
		return leaf(MAJORITY_VALUE(binary_targets))
	else:
		best_attribute = CHOOSE_BEST_DECISION_ATTR(examples,attributes,binary_targets)
		tree = tree(best_attribute)
		for v in best_attribute:
			#todo: add branch to tree of v
			#v_examples, v_binary_targets = 
			if(not v_examples):
				return leaf(MAJORITY_VALUE(binary_targets))
			else:
				subtree = DTL(v_examples,attributes-best_attribute,v_binary_targets)
	return tree