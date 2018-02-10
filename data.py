def getBinaryTargets(y, emote): 
	bTargets = []
	for i in range(len(y)): 
		bTargets.append(int(y[i] == emote))
	return bTargets