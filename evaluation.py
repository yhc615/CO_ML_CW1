#if actual == predicted ---> TP or TN
#if actual != predicted ---> FP or FN

def confusionMatrix(actual, predicted):
    confusion = [[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6]
    recallrate, precisionrate = [0]*6,[0]*6
    for i in range(len(actual)):
        #emotion = actual result
        #result = predicted result
        confusion[actual[i]-1][predicted[i]-1] +=1   
    TP,FP,TN,FN =[0]*6,[0]*6,[0]*6,[0]*6

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
