#IMPORTING THE LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm



#MAIN FUNCTION
if __name__ == '__main__':
    #OPENING THE FILE
    input_file = open('Testcases/input/input02.txt', 'r')
    lines = input_file.readlines()
    #CLOSING THE FILE
    input_file.close()
    cnt = 0
    train_inp = []
    test_inp =[]
    train_output = []
    #READING THE INPUT
    for line in lines:
        arr = line.split()
        if cnt == 0:
            n = int(arr[0])
            cnt += 1
        else:
            if cnt!=1:
                if arr[2][0]!='M':
                    dob = arr[0].split('/')
                    mon = int(dob[0])
                    day = int(dob[1])
                    year = int(dob[2])
                    tt = arr[1].split(':')
                    hour= int(tt[0])
                    min = int(tt[1])
                    #USING THE HOUR AS FEATURE
                    fet = hour+24*day+24*30*mon+24*30*12*year + min/60
                    fet = fet -base
                    train_inp.append([fet])
                    train_output.append([float(arr[2])])
                else:
                    dob=arr[0].split('/')
                    mon=int(dob[0])
                    day=int(dob[1])
                    year=int(dob[2])
                    tt=arr[1].split(':')
                    hour=int(tt[0])
                    min=int(tt[1])
                    #USING THE HOUR AS FEATURE
                    fet=hour+24*day+24*30*mon+24*30*12*year+min/60
                    fet = fet-base
                    test_inp.append(fet)
            else:
                if arr[2][0]!='M':
                    dob = arr[0].split('/')
                    mon = int(dob[0])
                    day = int(dob[1])
                    year = int(dob[2])
                    tt = arr[1].split(':')
                    hour= int(tt[0])
                    min = int(tt[1])
                    #USING THE HOUR AS FEATURE
                    fet = hour+24*day+24*30*mon+24*30*12*year+min/60
                    base = fet
                    fet = fet-base
                    train_inp.append([fet])
                    train_output.append([float(arr[2])])
                    cnt+=1
                else:
                    dob=arr[0].split('/')
                    mon=int(dob[0])
                    day=int(dob[1])
                    year=int(dob[2])
                    tt=arr[1].split(':')
                    hour=int(tt[0])
                    min=int(tt[1])
                    #USING THE HOUR AS FEATURE
                    fet=hour+24*day+24*30*mon+24*30*12*year+min/60
                    base = fet
                    fet = fet-base
                    test_inp.append(fet)
                    cnt+=1
    
    #CONVERTING THE INPUT TO NUMPY ARRAY
    train_inp = np.array(train_inp)
    #CONVERTING THE OUTPUT TO NUMPY ARRAY
    train_output = np.array(train_output)[:,0]
    #CONVERTING THE TEST INPUT TO NUMPY ARRAY
    test_inp = np.array(test_inp)[:,None]
    #CREATING A SVM REGRESSOR
    clf = svm.SVR(gamma = 0.00001,C = 10)
    clf.fit(train_inp,train_output)
    pred = clf.predict(test_inp)
    #PLOTTING THE OUTPUT
    plt.plot(train_inp,train_output,'ro',)
    plt.plot(test_inp,pred,'bo')
    plt.show()
    #WRITING THE OUTPUT TO THE FILE
    np.savetxt('Testcases/output/output02.txt',pred,fmt='%.2f')
    
    

            


