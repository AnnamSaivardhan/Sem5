import matplotlib.pyplot as plt
from subprocess import call
import numpy as np
import os

q = []
win_prob_optim = []
win_prob_rand = []
f5 = open("data/cricket/rand_pol.txt",'r')
f6 = open("updated_rand_pol.txt",'w')
lines = f5.readlines()
for line in lines:
    arr = line.split()
    z = int(arr[1])
    if z==4:
        z=3
    if z==6:
        z=4
    f6.write(str(arr[0])+" "+str(z)+"\n")
f5.close()
f6.close()

for i in range(51):
    f1 = open("enc.txt",'w')
    f2 = open("mdp_res.txt",'w')
    f3 = open("decod_out.txt",'w')
    f4 = open("rand.txt",'w')
    call(["python3","encoder.py","--parameters","data/cricket/sample-p1.txt","--q",str(i/50),"--states","s1530.txt" ],stdout=f1)
    call(["python3", "planner.py", "--mdp", "enc.txt", "--algorithm", "vi"],stdout=f2)
    call(["python3", "decoder.py", "--value-policy", "mdp_res.txt", "--states", "s1530.txt"],stdout=f3)
    call(["python3","planner.py","--mdp","enc.txt","--policy","updated_rand_pol.txt"],stdout=f4)
    file = open("decod_out.txt", "r")
    file2 = open("rand.txt","r")
    q.append(i/50)
    win_prob_optim.append(float(file.readlines()[0].split(" ")[2]))
    win_prob_rand.append(float(file2.readlines()[0].split(" ")[0]))
    file.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    file2.close()
    os.remove("enc.txt")
    os.remove("mdp_res.txt")
    os.remove("decod_out.txt")
    os.remove("rand.txt")

    os.remove("win_prob_optim.txt")
os.remove("updated_rand_pol.txt")

q = np.array(q)
win_prob = np.array(win_prob_optim)
win_prob_rand=np.array(win_prob_rand)
plt.plot(q,win_prob_optim,label="OptimalPolicy")
plt.plot(q,win_prob_rand,label="RandomPolicy")
plt.xlabel("q value")
plt.ylabel("Win Probability")
plt.title("Win Probability vs q value")
plt.legend()
plt.show()
plt.savefig("optim_graph.png")




