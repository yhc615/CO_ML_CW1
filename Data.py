import scipy.io

class Data:
    
    def __init__(self, x_in, y_out, target='None'): #data_in passed as [<x_n>,<y_n>]
        self.x = x_in
        self.y = y_out
        self.target_emotion = target #by default, specifies which emotion we are targetting
        
    def to_vector(self):
        return [self.x,self.y] 
    
    def set_binary_target(self, emotion):
        emotion_label = {'Anger':1, 'Disgust':2, 'Fear':3, 'Happiness':4, 'Sadness':5, 'Surprise':6}
        for i in range(len(self.y)):
            if self.y[i] == emotion_label[emotion]:
                self.y[i] = 1
            else:
                self.y[i] = 0
            self.target_emotion = emotion
    def sort(self, Au_label): #sort data on a particular Au label
        AU1_x=[] 
        AU1_y=[]
        AU0_x=[]
        AU0_y=[]
        for x,y in zip(self.x,self.y):
            if x[Au_label-1]:
                AU1_x.append(x), AU1_y.append(y)
            else:
                AU0_x.append(x), AU0_y.append(y)
                
        return [Data(AU0_x,AU0_y,self.target_emotion),Data(AU1_x,AU1_y,self.target_emotion)] # [<AuN=0>,<AuN=1>]
    
    #FOR PRINTING DATA
    def __str__(self):
        example_no = 1
        output = "------------------------------------------------------\n"
        output +="Example_no ! \t  Emotion ! \t AUs \n"
        row = ""
        for x,y in zip(self.x,self.y):
            row = "{} \t\t".format(example_no)
            if self.target_emotion == 'None':
                if y==1:
                    row += "Anger    \t"
                elif y==2:
                    row += "Disgust \t"
                elif y==3:
                    row += "Fear    \t" 
                elif y==4:
                    row += "Happiness \t"
                elif y==5:
                    row += "Sadness \t"
                else:
                    row += "Surprise \t"
            else:
                if y==1:
                    row += "{}   \t".format(self.target_emotion)
                else:
                    row += "-    \t\t"
            #gather X row(Au) data
            row += "["
            for i in range(len(x)):
                if x[i]:
                    row += "{} ".format(i+1)
            row += "]"

            row += "\n -----------------------------------------------"
            example_no += 1
            output += row + "\n"
        return output
    
    
raw_data = scipy.io.loadmat('Data/noisydata_students.mat')
data = Data(raw_data['x'][:10],raw_data['y'][:10])
print(data)
data.set_binary_target('Happiness')
print(data)
split_data = data.sort(41)
print(split_data[0])
print(split_data[1])
