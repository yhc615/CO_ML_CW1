import scipy.io
from Data import *
from dtl import *
from decision_tree import *

raw_data = scipy.io.loadmat('Data/noisydata_students.mat')
data = Data(raw_data['x'][:10],raw_data['y'][:10])
data.set_binary_target("Happiness")
e, b_t = data.to_vector()
b_t = [x[0] for x in b_t]

attr = list(range(1,46))
#print(b_t)
dtl = DTL(e, attr, b_t)