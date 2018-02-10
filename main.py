import scipy.io
import numpy as np
from math import floor
from decision_tree import *
from dtl import *
from predictor import *
from evaluation import *

def genTrees(data):# data = [<x_n>,<y_n>]	
	trees = []
	for i in range(1,7):
		attr = list(range(0,45))
		ex  = data[0]
		b_t = getBinaryTargets(data[1],i)
		trees.append(DTL(ex, attr, b_t))
	return trees

def getBinaryTargets(y_in, emotion_label): 
	b_targets = []
	for i in range(len(y_in)): 
		if y_in[i] == emotion_label:
			b_targets.append(1)
		else:
			b_targets.append(0)
	return b_targets

def ambStrat(arr):
	if 1 in arr:
		return arr.index(1)+1
	return 0

def testTrees(T, x2):
	predictions = []
	for x in x2:
		emotePredicts = [predictor(x, tree) for tree in T]
		predictions.append(ambStrat(emotePredicts))
	return predictions

def printStats(conMat, extra):
	print("Confusion Matrix:\n")
	print(conMat)
	if extra:
		stats = conMatStats(conMat)
		print("--TP:")
		for x in stats[0]: print(x)
		print("--FP:")
		for x in stats[1]: print(x)
		print("--TN:")
		for x in stats[2]: print(x)
		print("--FN:")
		for x in stats[3]: print(x)
		print("--Recall:")
		for x in stats[4]: print(x)
		print("--Precision:")
		for x in stats[5]: print(x)
		print("--F1:")
		for x in stats[6]: print(x)
		print("--Classification Rate:")
		print(stats[7])


def avgConMatSet(conMats):
	tmp = numpy.zeros(shape=(6,6)).astype(int)
	for mat in conMats:
		tmp += mat
	return tmp

def crossValidation(nFolds, x, y):
	xSplit, ySplit = [], []
	subSize = int(len(x)/nFolds)
	conMats = []
	ret = []
	for i in range(nFolds):
		xSplit.append(x[i*subSize:(i+1)*subSize])
		ySplit.append(y[i*subSize:(i+1)*subSize])
	for i in range(nFolds):
		xTrain, yTrain = [x for k,sublist in enumerate(xSplit) for x in sublist if k!=i], [y for k,sublist in enumerate(ySplit) for y in sublist if k!=i]
		xTest, yTest = xSplit[i], ySplit[i]
		treeSet = genTrees([xTrain,yTrain])
		predicts = testTrees(treeSet, xTest)
		cM = confusionMatrix(yTest, predicts)
		#print("--Fold {}:".format(i))
		#printStats(cM, 0)
		conMats.append(cM)
	return avgConMatSet(conMats)

def fullSetTrainTest(x, y):
	treeSet = genTrees([x,y])
	predicts = testTrees(treeSet, x)
	emotion_labels = {1:'Anger', 2:'Disgust', 3:'Fear', 4:'Happiness', 5:'Sadness', 6:'Surprise'}
	for i,x in enumerate(treeSet):
		print("Emotion: {}".format(emotion_labels[i+1]))
		print(x)
		print('-'*100)
	printStats(confusionMatrix(y, predicts), 0)


def main():
	raw_data = scipy.io.loadmat('Data/cleandata_students.mat')
	data = [raw_data['x'][:1000],raw_data['y'][:1000]]
	data[1] = [x[0] for x in data[1]]

	q = crossValidation(10, data[0], data[1])
	printStats(q, 1)

	#fullSetTrainTest(data[0], data[1])


if __name__ == "__main__":
	main()
