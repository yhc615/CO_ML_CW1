import scipy.io
from decision_tree import *
from dtl import *
from predictor import *

def genTrees(data):# data = [<x_n>,<y_n>]	
	trees = []
	for i in range(1,7):
		attr = list(range(0,45))
		ex  = data[0]
		b_t = get_binary_targets(data[1],i)
		trees.append(DTL(ex, attr, b_t))
	return trees

def get_binary_targets(y_in, emotion_label): 
	b_targets = []
	for i in range(len(y_in)): 
		if y_in[i] == emotion_label:
			b_targets.append(1)
		else:
			b_targets.append(0)
	return b_targets

def main():
	raw_data = scipy.io.loadmat('Data/noisydata_students.mat')
	data = [raw_data['x'],raw_data['y']]

	treeSet = genTrees(data)

	emotion_labels = {1:'Anger', 2:'Disgust', 3:'Fear', 4:'Happiness', 5:'Sadness', 6:'Surprise'}
	for i,x in enumerate(treeSet):
		print("Emotion: {}".format(emotion_labels[i+1]))
		print(x)
		print('-'*100)


if __name__ == "__main__":
	main()