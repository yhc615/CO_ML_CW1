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

def printStats(conMat):
	print("Confusion Matrix:\n")
	print(conMat)
	print(stats(conMat))

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
		#printStats(cM)
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
	printStats(confusionMatrix(y, predicts))


def main():
	raw_data = scipy.io.loadmat('Data/noisydata_students.mat')
	data = [raw_data['x'][:1000],raw_data['y'][:1000]]
	data[1] = [x[0] for x in data[1]]

	#q = crossValidation(10, data[0], data[1])
	#printStats(q)

	fullSetTrainTest(data[0], data[1])


if __name__ == "__main__":
	main()
