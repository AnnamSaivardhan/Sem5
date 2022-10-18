import matplotlib.pyplot as plt
from subprocess import call
import numpy as np
import os

q=[]
win_prob_optim=[]
win_prob_rand = []
nruns_str = str(10)
for i in range(15):
    i+=1
    if(i<10):
        nballs_str="0"+str(i)
    else:
        nballs_str=str(i)
    fname = "s"+nballs_str+nruns_str+".txt"
    f_states = open(fname,'w')
    call(["python3","cricket_states.py","--balls",nballs_str,"--runs",nruns_str],stdout=f_states)
    f_states.close()
    f1 = open("enc.txt",'w')
    f2 = open("mdp_res.txt",'w')
    f3 = open("decod_out.txt",'w')
    f4 = open("rand.txt",'w')
    f5 = open("data/cricket/rand_pol.txt",'r')
    f6 = open("updated_rand_pol.txt",'w')
    f7 = open(fname,'r')
    dict ={}
    lines = f5.readlines()
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
    f7.close()
    call(["python3","encoder.py","--parameters","data/cricket/sample-p1.txt","--q",str(0.25),"--states",fname ],stdout=f1)
    f1.close()
    call(["python3", "planner.py", "--mdp", "enc.txt", "--algorithm", "vi"],stdout=f2)
    f2.close()
    call(["python3", "decoder.py", "--value-policy", "mdp_res.txt", "--states", fname],stdout=f3)
    f3.close()
    call(["python3","planner.py","--mdp","enc.txt","--policy","updated_rand_pol.txt"],stdout=f4)
    f4.close()
    file = open("decod_out.txt", "r")
    file2 = open("rand.txt","r")
    q.append(i)
    win_prob_optim.append(float(file.readlines()[0].split(" ")[2]))
    win_prob_rand.append(float(file2.readlines()[0].split(" ")[0]))
    file.close()
    file2.close()
    os.remove("enc.txt")
    os.remove("mdp_res.txt")
    os.remove("decod_out.txt")
    os.remove("rand.txt")
    os.remove("updated_rand_pol.txt")
    os.remove(fname)
    os.remove("win_prob_optim.txt")



q = np.array(q)
win_prob_optim = np.array(win_prob_optim)
win_prob_rand = np.array(win_prob_rand)
plt.plot(q,win_prob_optim,label="OptimalPolicy")
plt.plot(q,win_prob_rand,label="RandomPolicy")
plt.xlabel("Number Of Balls")
plt.ylabel("Win Probability")
plt.title("Win Probability vs Number Of Balls(10 Runs)")
plt.legend()
plt.show()
plt.savefig("graph3.png")

            


