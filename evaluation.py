#if actual == predicted ---> TP or TN
#if actual != predicted ---> FP or FN
#vector of predicted outputs for the examples after all 6 trees are input as "predicted"

def confusion_matx(actual, predicted):
    #emotion_label = {'Anger':1, 'Disgust':2, 'Fear':3, 'Happiness':4, 'Sadness':5, 'Surprise':6}
    confusion = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    recallrate, precisionrate = [0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0]
    
    for i in range(len(actual)):
        confusion[actual[i]-1][predicted[i]-1] +=1   
    TP,FP,TN,FN =[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]

    for i in range(6):
        for j in range(6):
            TP[i] = confusion[i][i]
            if j != i:
                FN[i] += confusion[i][j]               
                FP[i] += confusion[j][i]
                TN[i] += confusion[j][j]
    for i in range(6):    
        if(TP[i] != 0 or FN[i] !=0):
            recallrate[i] = float(TP[i])/(TP[i]+FN[i])
        if(TP[i] != 0 or FP[i] !=0):
            precisionrate[i] = float(TP[i])/(TP[i]+FP[i])

    return confusion, TP, FP, TN, FN, recallrate, precisionrate

#example inputs:
actual = [1,1,3,6,6,6,1]
predicted = [2,1,3,6,6,6,6]

conf_matx = confusion_matx(actual, predicted)[0]
print("Confusion Matrix:")
for i in range(len(conf_matx)):    
    print(conf_matx[i])
print("TP")
print(confusion_matx(actual, predicted)[1])
print("FP")
print(confusion_matx(actual, predicted)[2])
print("TN")
print(confusion_matx(actual, predicted)[3])
print("FN")
print(confusion_matx(actual, predicted)[4])
print("RECALL RATES")
for element in confusion_matx(actual, predicted)[5]:
    print(element)
print("PRECISION RATES")
for element in confusion_matx(actual, predicted)[6]:
    print(element)
