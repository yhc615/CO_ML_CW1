import scipy.io
import numpy as np
import pickle
from math import floor
from decision_tree import *
from dtl import *
from predictor import *
from evaluation import *
from data import *

emotion_labels = {1:'Anger', 2:'Disgust', 3:'Fear', 4:'Happiness', 5:'Sadness', 6:'Surprise'}

def printStats(conMat, extra):
	print("Confusion Matrix:\n")
	print(conMat)
	print("--Classification Rate:")
	stats = conMatStats(conMat)
	print(stats[7])
	if extra:
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

def genTrees(x2, y2):
	trees = []
	for i in range(1,7):
		attr = list(range(0,45))
		b_t = getBinaryTargets(y2,i)
		trees.append(DECISION_TREE_LEARNING(x2, attr, b_t))
	return trees

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
		treeSet = genTrees(xTrain, yTrain)
		predicts = testTrees(treeSet, xTest)
		cM = confusionMatrix(yTest, predicts)
		#print("--Fold {}:".format(i))
		#printStats(cM, 0)
		conMats.append(cM)
	tmp = numpy.zeros(shape=(6,6)).astype(int)
	for mat in conMats:
		tmp += mat
	return tmp

def fullSetTrainTest(x2, y2):
	treeSet = genTrees(x2,y2)
	predicts = testTrees(treeSet, x2)
	#for i,x in enumerate(treeSet):
		#print("Emotion: {}".format(emotion_labels[i+1]))
		#print(x)
		#print('-'*100)
	printStats(confusionMatrix(y2, predicts), 0)

def saveTrees(fNamePrefix, tSet):
	for i,t in enumerate(tSet):
		pickle.dump(t, open("trees/"+fNamePrefix+"_"+emotion_labels[i+1]+".p", "wb"))

def loadTrees(fNamePrefix):
	tSet = []
	for i,emote in emotion_labels.items():
		p = pickle.load(open("trees/"+fNamePrefix+"_"+emote+".p", "rb"))
		tSet.append(p)
	return tSet


def main():
	raw_data = scipy.io.loadmat('Data/cleandata_students.mat')
	data = [raw_data['x'][:],raw_data['y'][:]]
	data[1] = [x[0] for x in data[1]]

	#q = crossValidation(10, data[0], data[1])
	#print("\nTotal:")
	#printStats(q, 0)

	#fullSetTrainTest(data[0], data[1])
	#saveTrees("fullClean", genTrees(data[0],data[1]))
	trees = loadTrees("fullClean")
	predicts = testTrees(trees, data[0])
	printStats(confusionMatrix(data[1], predicts), 0)


if __name__ == "__main__":
	main()
