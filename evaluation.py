#if actual == predicted ---> TP or TN
#if actual != predicted ---> FP or FN
import numpy

def confusionMatrix(actual, predicted):
	confusion = numpy.zeros(shape=(6,6)).astype(int)
	errorrate = 0
	for i in range(len(actual)):
		#emotion = actual result
		#result = predicted result
		confusion[actual[i]-1][predicted[i]-1] +=1
		errorrate += (1/len(predicted)) * (1-(predicted[i]==actual[i]))

	classificationrate = 1-errorrate

	return confusion
