def MAJORITY_VALUE(inp):
	return max(inp, key=inp.count)

def CHOOSE_BEST_DECISION_ATTR(ex,attr,b_targets):
	return 0
#Examples passed as [<yn>,<xn>]
def DTL(examples, attributes, binary_targets): #binary target will be the example index and its value
   #if all examples have the same value of binary_targets
   if all(e[binary_targets['i']] == binary_targets['val'] for e in examples):
       #return leaf node with this value
       return Tree(binary_targets['val'],'l')
   #else if attributes is empty
   elif not attributes:
        #return leaf node with this value
        return Tree(MAJORITY_VALUE(binary_targets),'l')
   else:
     best_attribute = CHOOSE_BEST_DECISION_ATTR(examples,attributes,binary_targets)
     root = Tree(best_attribute)
     #for each possible value of vi of best_attribute,
     for vi in [0,1]:
         #add a branch
         #declare examples_i, binary_targets_i
         if not examples_i:
             return Tree(MAJORITY_VALUE(binary_targets))
         else:
             subtree = DTL(examples_i, attributes-{best_attribute}, binary_targets_i )
     return root