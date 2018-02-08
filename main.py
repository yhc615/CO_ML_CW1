import scipy.io
from Data import *
from decision_tree import *
from dtl import *
from predictor import *

raw_data = scipy.io.loadmat('Data/noisydata_students.mat')
data = Data(raw_data['x'][:],raw_data['y'][:])
data.set_binary_target("Happiness")
ex, b_t = data.to_vector()
b_t = [x[0] for x in b_t]

attr = list(range(0,45))
#print(b_t)
dtl = DTL(ex, attr, b_t)
predic = [predictor(d, dtl) for d in ex]
print(sum(predic))
print(sum(b_t))