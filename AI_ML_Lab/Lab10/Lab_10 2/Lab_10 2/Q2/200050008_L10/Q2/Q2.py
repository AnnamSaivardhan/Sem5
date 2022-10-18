import numpy as np
from matplotlib import pyplot as plt
import sklearn as sk





file = open('trainingAndTest/training.txt', 'r')
lines = file.readlines()
file.close()
n = int(lines[0])
lines.pop(0)
x_total = np.random.rand(int(n),10)
x_total = 0*x_total
x_total = x_total - 1
y_total = np.random.rand(int(n))
y_total = 0*y_total
cnt=0
dict={}
dict["Physics"]=0
dict["Chemistry"]=1
dict["English"]=2
dict["Biology"]=3
dict["PhysicalEducation"]=4
dict["Accountancy"]=5
dict["ComputerScience"]=6
dict["Economics"]=7
dict["BusinessStudies"]=8
for i in range(0,int(n)):
    line = lines[i]
    line = line[1:-1]
    arr = line.split(',')
    lst = []
    x_total[cnt,dict[arr[0][1:-3]]]=float(arr[0][-1])
    x_total[cnt,dict[arr[1][1:-3]]]=float(arr[1][-1])
    x_total[cnt,dict[arr[2][1:-3]]]=float(arr[2][-1])
    x_total[cnt,dict[arr[3][1:-3]]]=float(arr[3][-1])    
    x_total[cnt,9]=float(arr[5][9:-1])
    y_total[cnt]=float(arr[4][-1])
    cnt+=1

x_train = np.array(x_total[:int(n)])
y_train = np.array(y_total[:int(n)])


file = open('Testcases/input/input00.txt', 'r')
lines = file.readlines()
n = int(lines[0])
lines.pop(0)
file.close()

x_test = np.random.rand(int(n),10)
x_total = 0*x_total
x_total = x_total - 1
cnt=0
for i in range(0,int(n)):
    line = lines[i]
    line = line[1:-1]
    arr = line.split(',')
    lst = []
    x_test[cnt,dict[arr[0][1:-3]]]=float(arr[0][-1])
    x_test[cnt,dict[arr[1][1:-3]]]=float(arr[1][-1])
    x_test[cnt,dict[arr[2][1:-3]]]=float(arr[2][-1])
    x_test[cnt,dict[arr[3][1:-3]]]=float(arr[3][-1])    
    x_test[cnt,9]=float(arr[4][9:-1])
    cnt+=1





from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
#Round off the predicted values
y_pred = np.round(y_pred)[:,None]
np.savetxt('Testcases/output/output00.txt', y_pred, fmt='%d')



# y_pred = y_pred - y_test
# #Calculate the accuracy
# y_pred[y_pred==0]=1
# y_pred[y_pred==-1]=1
# y_pred[y_pred!=1]=0
# a = np.sum(y_pred)
# b = len(y_pred)
# accuracy = 100*(2*a-b)/b
# print(accuracy)




