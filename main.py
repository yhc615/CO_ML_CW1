import scipy.io
from Data import *
from decision_tree import *
from dtl import *
from predictor import *

def genTrees(dat):
	trees = []
	attr = list(range(0,45))
	for i in range(1,7):
		b_t = dat.getTargetsForVal(i)
		ex = dat.to_vector()[0]
		trees.append(DTL(ex, attr, b_t))
	return trees

raw_data = scipy.io.loadmat('Data/noisydata_students.mat')
data = Data(raw_data['x'][:],raw_data['y'][:])

treeSet = genTrees(data)

for i,x in enumerate(treeSet):
	print("Emotion: {}".format(i))
	x.printTree()