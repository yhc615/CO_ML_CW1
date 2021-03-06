#if actual == predicted ---> TP or TN
#if actual != predicted ---> FP or FN
import numpy

def confusionMatrix(actual, predicted):
	confusion = numpy.zeros(shape=(6,6)).astype(int)
	for i,a in enumerate(actual):
		confusion[actual[i]-1][predicted[i]-1] +=1

	return confusion

def conMatStats(confusion):
	recallrate, precisionrate,F1 = [0]*6,[0]*6,[0]*6
	
	TP,FP,TN,FN =[0]*6,[0]*6,[0]*6,[0]*6
	
	for i in range(6):
		for j in range(6):
			TP[i] = confusion[i][i]
			if j != i:
				FN[i] += confusion[i][j]
				
				FP[i] += confusion[j][i]
				for k in range(6):
					if k!=i:
						TN[i] += confusion[j][k]

	for i in range(6):
		if(TP[i] != 0 or FN[i] !=0):
			recallrate[i] = float(TP[i])/(TP[i]+FN[i])
		if(TP[i] != 0 or FP[i] !=0):
			precisionrate[i] = float(TP[i])/(TP[i]+FP[i])
		if(precisionrate[i] !=0 or recallrate[i] != 0):
			F1[i] = 2*(precisionrate[i]*recallrate[i])/(precisionrate[i]+recallrate[i])
		classificationrate = 1-(1/numpy.sum(confusion))*(numpy.sum(confusion)-numpy.trace(confusion))


	return TP, FP, TN, FN, recallrate, precisionrate, F1,classificationrate
