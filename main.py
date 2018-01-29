import scipy.io


class Data:
    
    def __init__(self, data_in):
        self.x = data_in['x']
        self.y = data_in['y']
    
    def __str__(self):
        example_no = 1
        output = "------------------------------------------------------\n"
        output +="Example_no ! \t  Emotion ! \t AUs \n"
        row = ""
        for x,y in zip(self.x,self.y):
            row = "{} \t\t".format(example_no)
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
            
            #gather Aus data
            row += "["
            for i in range(len(x)):
                if x[i]:
                    row += "{} ".format(i)
            row += "]"

            row += "\n -----------------------------------------------"
            example_no += 1
            output += row + "\n"
        return output

raw_data = scipy.io.loadmat('Data/cleandata_students.mat')
data = Data(raw_data)
print(data)
