import argparse
import numpy as np
import pulp 

def lp_cont(numStates,numActions,transition_matrix,reward_matrix,discount_factor):
    

if __name__== '__main__':
    #Parser Initialisation
    parsr = argparse.ArgumentParser(description="step1 initialisation")

    #Adding arguments
    parsr.add_argument('--mdp',help="path to mds file")
    parsr.add_argument('--algorithm',help="algorithm to be implemented",default='lp')
    parsr.add_argument('--policy',help="policy to be implemented")

    #step3 Parse the arguments
    args = parsr.parse_args()

    file = open(args.mdp,'r')
    lines = file.readlines()
    cnt = 0
    for line in lines:
        cnt+=1
        arr = line.split()
        if arr[0]=="numStates":
            numStates = int(arr[1])
        elif arr[0]=="numActions":
            numActions = int(arr[1])
            transition_matrix = np.zeros((numStates,numActions,numStates))
            reward_matrix = np.zeros((numStates,numActions,numStates))
        elif arr[0]=="end":
            end_array = arr[1:]
        elif arr[0]=="transition":
            transition_matrix[int(arr[1]),int(arr[2]),int(arr[3])] = float(arr[5])
            reward_matrix[int(arr[1]),int(arr[2]),int(arr[3])] = float(arr[4])
        elif arr[0]=="discount":
            discount = float(arr[1])
        elif arr[0]=="mdptype":
            mdp_type=arr[1]

    if args.algorithm == 'lp':
        if mdp_type == 'continuing':
            lp_cont(np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,discount))  