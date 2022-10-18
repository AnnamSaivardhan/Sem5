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
    for state in states:
        stat_list.append(state.split()[0])
    
    
    # final_file = open('final.txt','w')


    #OPENING THE VALUE AND POLICY FILE
    val_pol_file = open(args.value_policy,'r')
    val_pol = val_pol_file.readlines()
    cnt = 0
    for line in val_pol:
        arr = line.split()
        # print(arr[1])
        a = int(float(arr[1]))
        z = int(float(arr[1])) if int(float(arr[1]))<3 else (int(float(arr[1]))+1)
        z = 6 if z==5 else z
        print(str(stat_list[cnt])+' '+str(z)+' '+str(arr[0]))
        cnt+=1
        if cnt>=150:
            stat_file.close()
            val_pol_file.close()
            exit()
    # final_file.close()
    