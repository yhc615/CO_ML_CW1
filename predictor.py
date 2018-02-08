def predictor(data, dtl):
	attrVal = data[dtl.getNodeLabel()]
	kids = dtl.getKids()
	if kids[attrVal].getIsLeaf():
		return kids[attrVal].getLeafLabel()
	else:
		return predictor(data, kids[attrVal])