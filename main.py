import scipy.io
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

def main():
	raw_data = scipy.io.loadmat('Data/noisydata_students.mat')
	data = [raw_data['x'],raw_data['y']]
	data[1] = [x[0] for x in data[1]]

	treeSet = genTrees(data)
	predicts = testTrees(treeSet, data[0])
	cM = confusionMatrix(data[1], predicts)
	print("confusion matrix:")
	print("")
	for x in cM[0]:
		print(x)
	print("")
	print("TP, FP, TN, FN, recall rate, precision rate, F1")
	print("")
	for i in range(1,len(cM)):
		print(cM[i])
	# emotion_labels = {1:'Anger', 2:'Disgust', 3:'Fear', 4:'Happiness', 5:'Sadness', 6:'Surprise'}
	# for i,x in enumerate(treeSet):
	# 	print("Emotion: {}".format(emotion_labels[i+1]))
	# 	print(x)
	# 	print('-'*100)


if __name__ == "__main__":
	main()
