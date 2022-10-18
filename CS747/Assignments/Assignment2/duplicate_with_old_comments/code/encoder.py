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
    p1_actions = np.zeros((5,7))
    #p1_actions[0] -> action == 0 
    #p1_actions[1] -> action == 1 
    #p1_actions[2] -> action == 2
    #p1_actions[3] -> action == 4
    #p1_actions[4] -> action == 6
    #p1_actions[0][0] -> out
    #p1_actions[0][1] -> zero runs
    #p1_actions[0][2] -> one run
    #p1_actions[0][3] -> two runs
    #p1_actions[0][4] -> three runs
    #p1_actions[0][5] -> four runs
    #p1_actions[0][6] -> six runs
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
    # 0 to numStates-1 is player1's turn
    # numStates to 2*numStates-1 is player2's turn
    # 2*numStates is the terminal state
    transition_matrix = np.zeros((2*num_states+2,2*num_states+2,5))
    reward_matrix = np.zeros((2*num_states+2,2*num_states+2))
    reward_matrix[:,2*num_states:2*num_states+1]=1
    cnt=0
    dict = {}
    difile = open('dict.txt','w')
    for line in lines:
        arr = line.split()
        dict[int(arr[0])] = cnt
        difile.write(str(cnt)+' '+arr[0]+'\n')
        cnt+=1
    difile.close()
    dict[11111] = 2*num_states #WIN
    dict[99999] = 2*num_states+1 #LOSE
    for line in lines:
        arr = line.split()
        num = int(arr[0])
        rr  = int(num%100)
        bb  = int((num//100)%100)
        init_state = int(dict[num])
        next_state = np.zeros(7)
        #next_state[0] -> zero runs
        #next_state[1] -> one run
        #next_state[2] -> two runs
        #next_state[3] -> three runs
        #next_state[4] -> four runs
        #next_state[5] -> six runs
        #next_state[6] -> out
        if bb>1:
            if rr>0:
                #FOR PLAYER1 STATES
                for i in range(6):
                    # if i==3:
                    #     continue
                    j = 6 if i==5 else i
                    if rr-j>0:
                        if ((j%2==0 and bb%6!=1) or (j%2==1 and bb%6==1)):
                            next_state[i]= dict[num-100 - j]
                        else:
                            next_state[i]=num_states+dict[num-100-j]
                        #next_state[i]= dict[num-100 - j] if ((j%2==0 and bb%6!=1) or (j%2==1 and bb%6==1)) else num_states+dict[num-100-j]
                        
                        transition_matrix[int(init_state),int(next_state[i]),:] += p1_actions[:,i+1]
                    else:
                        next_state[i]=dict[11111]
                        transition_matrix[int(init_state),int(next_state[i]),:] += p1_actions[:,i+1]
                transition_matrix[int(init_state),int(dict[99999]),:] = p1_actions[:,0]
                #FOR PLAYER2 STATES
                init_state2 = init_state + num_states
                # OUT
                transition_matrix[int(init_state2),dict[99999],:] += [p2,p2,p2,p2,p2] 
                if bb%6!=1:
                    # ZERO RUNS
                    nextstat = dict[num-100]+num_states
                    zz=(1-p2)/2
                    transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]
                    if rr>1:
                        # ONE RUN
                        nextstat = dict[num-101]
                        transition_matrix[int(init_state2),int(nextstat),:]+= [zz,zz,zz,zz,zz]
                    else:
                        # ONE RUN
                        nextstat = dict[11111]
                        transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]
                else:
                    zz=(1-p2)/2
                    #ZERO RUNS
                    nextstat = dict[num-100]
                    transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]
                    if rr>1:
                        #ONE RUN
                        nextstat = dict[num-101]+num_states
                        transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]
                    else:
                        #ONE RUN
                        nextstat = dict[11111]
                        transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz]
            
        else:
            #FOR PLAYER1 STATES
            for i in range(6):
                j = 6 if i==5 else i
                if rr-j>0:
                    next_state[i]= dict[99999] 
                    transition_matrix[int(init_state),int(next_state[i]),:] += p1_actions[:,i+1]
                else:
                    next_state[i]=dict[11111]
                    transition_matrix[int(init_state),int(next_state[i]),:] += p1_actions[:,i+1]
            transition_matrix[int(init_state),int(dict[99999]),:] += p1_actions[:,0]
            #FOR PLAYER2 STATES
            #ZERO RUNS
            nextstat = dict[99999]
            init_state2 = init_state + num_states
            zz = (1+p2)/2
            transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz] #zero runs+ out probability
            if rr>1:
                #ONE RUN
                zz = (1-p2)/2
                nextstat = dict[99999]
                transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz] 
            else:
                #ONE RUN
                zz=(1-p2)/2
                nextstat = dict[11111]
                transition_matrix[int(init_state2),int(nextstat),:] += [zz,zz,zz,zz,zz] 


    #WRITING THE TRANSITION MATRIX TO A FILE
    # outfile = open('output.txt','w')
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
    



                
                    

            
                
