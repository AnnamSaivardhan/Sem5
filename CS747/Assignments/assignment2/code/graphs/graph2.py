import matplotlib.pyplot as plt
from subprocess import call
import numpy as np
import os

q = []
win_prob_optim = []
win_prob_rand = []

for i in range(20):
    i+=1
    
    if(i<10):
        z="0"+str(i)
    else:
        z=str(i)
    strii = "s"+"10"+z+".txt"
    f_stat = open(strii,'w')
    call(["python3","cricket_states.py","--balls","10","--runs",str(i)],stdout=f_stat)
    f_stat.close()
    f1 = open("enc.txt",'w')
    f2 = open("mdp_res.txt",'w')
    f3 = open("decod_out.txt",'w')
    f4 = open("rand.txt",'w')
    f5 = open("data/cricket/rand_pol.txt",'r')
    f6 = open("updated_rand_pol.txt",'w')
    lines = f5.readlines()
    dict={}
    q.append(i)
    for line in lines:
        arr = line.split()
        y = int(arr[0])
        z = int(arr[1])
        if z==4:
            z=3
        if z==6:
            z=4
        dict[y]=z
    f5.close()
    f7 = open(strii,'r')
    lines = f7.readlines()
    for line in lines:
        arr = line.split()
        y = int(arr[0])
        if y in dict:
            if int(y/1000)==0:
                a = "0"+str(y)
            else:
                a = str(y)
            f6.write(a+" "+str(dict[y])+"\n")
    f6.close()
    call(["python3","encoder.py","--parameters","data/cricket/sample-p1.txt","--q",str(0.25),"--states",strii ],stdout=f1)
    f1.close()
    call(["python3", "planner.py", "--mdp", "enc.txt", "--algorithm", "vi"],stdout=f2)
    f2.close()
    call(["python3", "decoder.py", "--value-policy", "mdp_res.txt", "--states", strii],stdout=f3)
    f3.close()
    call(["python3","planner.py","--mdp","enc.txt","--policy","updated_rand_pol.txt"],stdout=f4)
    f4.close()
    # call(["python3","planner.py","--mdp","enc.txt","--policy","updated_rand_pol.txt"],stdout=f4)
    file = open("decod_out.txt", "r")
    file2 = open("rand.txt","r")
    win_prob_optim.append(float(file.readlines()[0].split(" ")[2]))
    win_prob_rand.append(float(file2.readlines()[0].split(" ")[0]))
    file.close()
    os.remove("enc.txt")
    os.remove("mdp_res.txt")
    os.remove("decod_out.txt")
    os.remove("rand.txt")
    os.remove("updated_rand_pol.txt")
    os.remove(strii)
    os.remove("win_prob_optim.txt")
    
    
    
    file2.close()


q = np.array(q)
win_prob_optim = np.array(win_prob_optim)
win_prob_rand = np.array(win_prob_rand)
plt.plot(q,win_prob_optim,label="")
plt.plot(q,win_prob_rand,label="")
plt.xlabel("")
plt.ylabel("")
plt.legend()
plt.title("")
plt.show()
plt.savefig("graph2.png")


