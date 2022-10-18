import argparse
import numpy as np
epsilon = 0.0000000000000001



if __name__== '__main__':
    #PARSER INITIALIZATION
    parsr = argparse.ArgumentParser(description="step1 initialisation")

    #ADDING ARGUMENTS
    parsr.add_argument('--states',help="states_file_path")
    parsr.add_argument('--parameters',help="p1_parameters")
    parsr.add_argument('--q',help="player2 parameters")

    #PARSING THE ARGUMENTS
    args = parsr.parse_args()
    p2 = float(args.q)

    #OPENING THE PLAYER1 PARAMETER FILE
    P1_param = open(args.parameters,'r')
    # ARRAY TO STORE THE PROBABILITIES
    p1_actions = np.zeros((5,7))
    lines = P1_param.readlines()
    for line in lines:
        arr = line.split()
        if arr[0] == 'action':
            pass
        elif arr[0]=='0':
            for i in range(7):
                p1_actions[0][i] = float(arr[i+1])
        elif arr[0]=='1':
            for i in range(7):
                p1_actions[1][i] = float(arr[i+1])
        elif arr[0]=='2':
            for i in range(7):
                p1_actions[2][i] = float(arr[i+1])
        elif arr[0]=='4':
            for i in range(7):
                p1_actions[3][i] = float(arr[i+1])
        elif arr[0]=='6':
            for i in range(7):
                p1_actions[4][i] = float(arr[i+1])

    #OPENING THE STATES FILE
    states = open(args.states,'r')
    lines = states.readlines()
    num_states = len(lines)
    #TRANSITION PROBABILITIES MATRIX
    transition_matrix = np.zeros((2*num_states+2,2*num_states+2,5))
    #REWARD MATRIX
    reward_matrix = np.zeros((2*num_states+2,2*num_states+2))
    reward_matrix[:,2*num_states:2*num_states+1]=1
    #DICTIONARY TO STORE STATE NUMBERS TO ZERO INDEXING MAPPING
    dict = {}
    cnt=0
    for line in lines:
        arr = line.split()
        dict[int(arr[0])] = cnt
        cnt+=1
    #WIN KEY IS SET TO 11111
    dict[11111] = 2*num_states 
    #LOSS KEY IS SET TO 99999
    dict[99999] = 2*num_states+1 
    for line in lines:
        arr = line.split()
        num = int(arr[0])
        rr  = int(num%100)
        bb  = int((num//100)%100)
        init_state = int(dict[num])
        if bb>1:
            #FOR PLAYER1 STATES
            transition_matrix[int(init_state),int(dict[99999]),:] = p1_actions[:,0]
            for i in range(6):    
                j = 6 if i==5 else i
                if rr-j>0:
                    next_state_ = dict[num-100-j] if ((j%2==0 and bb%6!=1) or (j%2==1 and bb%6==1)) else num_states+dict[num-100-j]
                    transition_matrix[int(init_state),int(next_state_),:] += p1_actions[:,i+1]
                else:
                    next_state_=dict[11111]
                    transition_matrix[int(init_state),int(next_state_),:] += p1_actions[:,i+1]

            #FOR PLAYER2 STATES
            init_state2 = init_state + num_states
            # OUT
            transition_matrix[int(init_state2),dict[99999],:] += [p2,p2,p2,p2,p2] 
            if bb%6!=1:
                # ZERO RUNS
                nextstat = dict[num-100]+num_states
                zz=(1-p2)/2
                transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]
                nextstat = dict[num-101] if rr>1 else dict[11111]
                transition_matrix[int(init_state2),int(nextstat),:]+= [zz,zz,zz,zz,zz]
            else:
                zz=(1-p2)/2
                #ZERO RUNS
                nextstat = dict[num-100]
                transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]
                nextstat = dict[num-101]+num_states if rr>1 else dict[11111]
                transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]     
        else:
            #FOR PLAYER1 STATES
            transition_matrix[int(init_state),int(dict[99999]),:] += p1_actions[:,0]
            for i in range(6):
                j = 6 if i==5 else i
                next_state_ = dict[99999] if rr-j>0 else dict[11111]
                transition_matrix[int(init_state),int(next_state_),:] += p1_actions[:,i+1]
            #FOR PLAYER2 STATES
            #ZERO RUNS
            nextstat = dict[99999]
            init_state2 = init_state + num_states
            zz = (1+p2)/2
            transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz] #zero runs+ out probability
            zz=(1-p2)/2
            nextstat = dict[99999] if rr>1 else dict[11111]
            transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]

    #PRINTING THE OUTPUT
    print("numStates "+str(2*num_states+2))
    print("numActions "+str(5))
    print("end "+str(2*num_states)+" "+str(2*num_states+1))
    for i in range(2*num_states+2):
        for j in range(2*num_states+2):
            for k in range(5):
                if transition_matrix[i][j][k]>0:
                    print("transition "+str(i)+" "+str(k)+" "+str(j)+" "+str(reward_matrix[i][j])+" "+str(transition_matrix[i][j][k]))
    print("mdptype episodic")
    print("discount 1.0")
    



                
                    

            
                
