import argparse
import numpy as np


if __name__ == '__main__':
#PARSER INITIALIZATION
    parsr = argparse.ArgumentParser(description="step1 initialisation")

    #ADDING ARGUMENTS
    parsr.add_argument('--value-policy',help="value_and_policy file path")
    parsr.add_argument('--states',help="states_file_path")
    # parsr.add_argument('--q',help="player2 parameters")

    #PARSING THE ARGUMENTS
    args = parsr.parse_args()
    

    #OPENING THE STATES FILE
    stat_file = open(args.states,'r')
    states = stat_file.readlines()
    stat_list = []
    xx = 0
    for state in states:
        stat_list.append(state.split()[0])
        xx+=1
    
    



    #OPENING THE VALUE AND POLICY FILE
    val_pol_file = open(args.value_policy,'r')
    val_pol = val_pol_file.readlines()
    cnt = 0
    for line in val_pol:
        arr = line.split()
        a = int(float(arr[1]))
        z = a if a<3 else int(a+1)
        z = 6 if z==5 else z
        print(str(stat_list[cnt])+' '+str(z)+' '+str(arr[0]))
        cnt+=1
        if cnt>=xx: 
            break
    stat_file.close()
    val_pol_file.close()

    #Storing points in a file
    file_optim = open("win_prob_optim.txt",'w')


    