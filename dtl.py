def MAJORITY_VALUE(inp):
	return max(inp, key=inp.count)

def CHOOSE_BEST_DECISION_ATTR(ex,attr,b_targets):
	return 0
<<<<<<< HEAD

def leaf(x):
	node = Tree("")
	node.label_leaf(x)
	return node

def tree(x):
	return Tree(x)

def DTL(examples, attributes, binary_targets):
	if(binary_targets[1:] == binary_targets[:-1]):
		return leaf(binary_targets[0])
	elif not attributes:
		return leaf(MAJORITY_VALUE(binary_targets))
	else:
		best_attribute = CHOOSE_BEST_DECISION_ATTR(examples,attributes,binary_targets)
		tree = tree(best_attribute)
		for v in [0,1]:
			v_examples, v_binary_targets = [e for e in examples if e[best_attribute]==v],[binary_targets[i] for i,e in enumerate(examples) if e[best_attribute]==v]
			if not v_examples:
				tree.branch[v] = leaf(MAJORITY_VALUE(binary_targets))
			else:
				tree.branch[v] = DTL(v_examples,attributes-best_attribute,v_binary_targets)
		return tree
