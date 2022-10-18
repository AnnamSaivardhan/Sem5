import argparse
import numpy as np
import pulp 
epsilon = 0.0000000000000001



#################################### AUXILIARY FUNCTIONS###########################################

#####FUNCTION TO EVALUATE VALUES OF V FROM A GIVEN POLICY#####
def policy_evaluation(policy,numStates,numActions,transition_matrix,reward_matrix,discount_factor):
    # Initialize Value_Function arbitrarily
    V1 = np.zeros(numStates)
    #Intialize the updated Value_Function arbitrarily
    V2 = np.zeros(numStates)
    while(True):
        for s in range(numStates):
            a=(int)(policy[s].item())
            V2[s] = np.sum(transition_matrix[s,a,:] * (reward_matrix[s,a,:] + discount_factor * V1))
        if np.all(np.abs(V1-V2)<0.00000000001):
            break
        for s in range(numStates):
            #Store V2 in V1 so V2 can be updated again
            V1[s] = V2[s]
    #If the difference between V1 and V2 is less than 0.000000000001, return V2
    return V2






########FUNCTION TO SOLVE THE MDP USING LINEAR PROGRAMMING FOR CONTINUOUS MDP#######
def linear_programming_cont(numStates,numActions,transition_matrix,reward_matrix,discount_factor):
    #Initializing the LP problem
    problem = pulp.LpProblem("MDP", pulp.LpMinimize)
    #Initializing the variables
    decision_variables = []
    for s in range(numStates):
        variable = str('v'+str(s))
        decision_variables.append(pulp.LpVariable(variable, lowBound=0))
    #Initializing the objective function
    problem+= (np.sum(decision_variables))
    #Initializing the constraints
    for s in range(numStates):
        for a in range(numActions):
            problem+= (decision_variables[s]>= np.sum(((transition_matrix[s,a,:]*discount_factor) * ((reward_matrix[s,a,:]/discount_factor) +  decision_variables))))
    #Solving the LP problem
    problem.solve(pulp.PULP_CBC_CMD(msg=False))
    #Extracting the V values
    V = np.zeros(numStates)
    for i in range(numStates):
        V[i]=np.float64(decision_variables[i].value())
    #Extracting the policy
    policy = np.zeros(numStates)
    for s in range(numStates):
            # Compute the value of each action
            action_values = np.zeros(numActions)
            for a in range(numActions): 
                action_values[a] = np.sum(transition_matrix[s,a,:] * (reward_matrix[s,a,:] + discount_factor * V))
            best_action = np.argmax(action_values)
            # Update the policy
            policy[s] = best_action
    return V, policy

    




########FUNCTION TO SOLVE THE MDP USING VALUE ITERATION FOR CONTINUOUS MDP#######
def value_iteration_cont(numStates,numActions,transition_matrix,reward_matrix,discount_factor,epsilon):
    # Initialize Value_Function arbitrarily
    V1 = np.zeros(numStates)
    V2 = np.zeros(numStates)
    # Initialize optimal_policy arbitrarily
    policy = np.zeros(numStates)
    # Initialize differences arbitrarily
    diff = np.zeros(numStates)
    # Repeat until convergence
    while True:
        # For each state s
        for s in range(numStates):
            # Compute the value of each action
            action_values = np.zeros(numActions)
            for a in range(numActions):
                # Compute the value of each action
                action_values[a] = np.sum(transition_matrix[s,a,:] * (reward_matrix[s,a,:] + discount_factor * V1))
            # Select the best action
            best_action = np.argmax(action_values)
            # Update the policy
            policy[s] = best_action
            # Update the value function
            V2[s] = action_values[best_action]
            diff[s] = np.abs(V1[s] - action_values[best_action])
        # Check for convergence
        if np.all(diff < epsilon ):
            break
        for s in range(numStates):
            # Update the value function
            V1[s] = V2[s]
    return V1, policy




#######FUNCTION TO SOLVE THE MDP USING HOWARD POLICY ITERATION FOR CONTINUOUS MDP######
def howard_policy_iteration_cont(numStates,numActions,transition_matrix,reward_matrix,discount_factor,epsilon):
    # Initialize Value_Function arbitrarily
    V = np.zeros(numStates)
    # Initialize optimal_policy arbitrarily
    policy = np.zeros(numStates)
    #Variable to store whether improvement is possible or not
    improve=True
    while (improve):
        improve = False
        # For each state s
        #Compute the policy evaluation for current policy
        V = policy_evaluation(policy,numStates,numActions,transition_matrix,reward_matrix,discount_factor)
        for s in range(numStates):
            # Compute the value of each action
            action_values = np.zeros(numActions)
            for a in range(numActions):
                action_values[a] = np.sum(transition_matrix[s,a,:] * (reward_matrix[s,a,:] + discount_factor * V))
            # Select the best action
            best_action = np.argmax(action_values)
            b = best_action
            # Check for improvement
            if policy[s]!=best_action and action_values[b]>action_values[(int)(policy[s].item())]:
                improve=True
            # Update the policy
            policy[s] = best_action  
    return V, policy 






#######FUNCTION TO SOLVE THE MDP USING VALUE ITERATION FOR EPISODIC MDP######
def value_iteration_episodic(numStates,numActions,transition_matrix,reward_matrix,discount_factor,epsilon):
    V = np.zeros(numStates)
    V2 = np.zeros(numStates)
    # Initialize optimal_policy arbitrarily
    policy = np.zeros(numStates)
    # Initialize differences arbitrarily
    diff = np.zeros(numStates)
    # Repeat until convergence
    c=0
    while True:
        # For each state s
        for s in range(numStates):
            # Compute the value of each action
            action_values = np.zeros(numActions)
            for a in range(numActions): 
                action_values[a] = np.sum(transition_matrix[s,a,:] * (reward_matrix[s,a,:] +  discount_factor*V))
            # Select the best action
            best_action = np.argmax(action_values)
            # Update the policy
            policy[s] = best_action
            # Update the value function
            V2[s] = action_values[best_action]
            diff[s] = np.abs(V[s] - action_values[best_action])
            
        # Check for convergence
        if np.all(diff < epsilon ):
            break
        #print(diff)
        for s in range(numStates):
            V[s] = V2[s]   
    return V, policy 





######FUNCTION TO SOLVE THE MDP USING LINEAR PROGRAMMING FOR EPISODIC MDP#####
def linear_programming_episodic(numStates,numActions,transition_matrix,reward_matrix,discount_factor):
    #Initializing the LP problem
    problem = pulp.LpProblem("MDP", pulp.LpMinimize)
    #Initializing the decision variables
    decision_variables = []
    for s in range(numStates):
        variable = str('v'+str(s))
        decision_variables.append(pulp.LpVariable(variable, lowBound=0))
    #Initializing the objective function
    problem+= (np.sum(decision_variables))
    #Initializing the constraints
    for s in range(numStates):
        for a in range(numActions):
            problem+= (decision_variables[s]>= np.sum(((transition_matrix[s,a,:]*discount_factor) * ((reward_matrix[s,a,:]/discount_factor) +  decision_variables))))
    #Solving the LP problem
    problem.solve(pulp.PULP_CBC_CMD(msg=False))
    #Extracting the V values
    V = np.zeros(numStates)
    for i in range(numStates):
        V[i]=np.float64(decision_variables[i].value())
    #Extracting the policy
    policy = np.zeros(numStates)
    for s in range(numStates):
            # Compute the value of each action
            action_values = np.zeros(numActions)
            for a in range(numActions): 
                action_values[a] = np.sum(transition_matrix[s,a,:] * (reward_matrix[s,a,:] + discount_factor * V))
            best_action = np.argmax(action_values)
            # Update the policy
            policy[s] = best_action
    return V, policy





######FUNCTION TO SOLVE THE MDP USING HOWARD POLICY ITERATION FOR EPISODIC MDP######
def howard_policy_iteration_episodic(numStates,numActions,transition_matrix,reward_matrix,discount_factor,epsilon):
    # Initialize Value_Function arbitrarily
    V = np.zeros(numStates)
    # Initialize optimal_policy arbitrarily
    policy = np.zeros(numStates)
    #Variable to store whether improvement is possible or not
    improve=True
    while (improve):
        improve = False
        # For each state s
        #Compute the policy evaluation for current policy
        V = policy_evaluation(policy,numStates,numActions,transition_matrix,reward_matrix,discount_factor)
        for s in range(numStates):
            # Compute the value of each action
            action_values = np.zeros(numActions)
            for a in range(numActions):
                action_values[a] = np.sum(transition_matrix[s,a,:] * (reward_matrix[s,a,:] + discount_factor * V))
            # Select the best action
            best_action = np.argmax(action_values)
            b = best_action
            # Check for improvement
            if policy[s]!=best_action and action_values[b]>action_values[(int)(policy[s].item())]:
                improve=True
            # Update the policy
            policy[s] = best_action  
    return V, policy


####################################### MAIN_FUNCTION ##############################################
if __name__== '__main__':
    #PARSER INITIALIZATION
    parsr = argparse.ArgumentParser(description="step1 initialisation")

    #ADDING ARGUMENTS
    parsr.add_argument('--mdp',help="path to mds file")
    parsr.add_argument('--algorithm',help="algorithm to be implemented",default='vi')
    parsr.add_argument('--policy',help="policy to be implemented",default='None')

    #PARSING THE ARGUMENTS
    args = parsr.parse_args()


    #OPENING THE MDP FILE
    file = open(args.mdp,'r')
    lines = file.readlines()
    for line in lines:
        arr = line.split()
        if arr[0]=="numStates":
            numStates = int(arr[1])
        elif arr[0]=="numActions":
            numActions = int(arr[1])
            #Create the transition matrix
            transition_matrix = np.zeros((numStates,numActions,numStates))
            #Create the reward matrix
            reward_matrix = np.zeros((numStates,numActions,numStates))
        elif arr[0]=="end":
            end_array = arr[1:]
        elif arr[0]=="transition":
            reward_matrix[int(arr[1]),int(arr[2]),int(arr[3])] = float(arr[4])
            transition_matrix[int(arr[1]),int(arr[2]),int(arr[3])] = float(arr[5])
        elif arr[0]=="discount":
            discount = float(arr[1])
        elif arr[0]=="mdptype":
            # print("hdjfjkfjkfjfnff\n")
            mdp_type=arr[1]


    #RANDOM WORK
    #for i in range(numStates):
    #     if transition_matrix[6][3][i]!=0:
    #         print(i,transition_matrix[6][3][i])
    #         # print(np.sum(transition_matrix,axis=2)[i])


            
    #OPENING THE POLICY FILE IF PROVIDED
    if args.policy!='None':
        policy_file = open(args.policy,'r')
        policy_lines = policy_file.readlines()
        policy = np.zeros(numStates)
        cnt = 0
        for line in policy_lines:
            arr = line.split()
            policy[cnt] = int(arr[0])
            cnt+=1
    

    
########################################## SOLVING ####################################################   
    #SOLVING THE MDP USING ALGORITHM PROVIDED IN THE COMMAND LINE
    if args.algorithm=='vi' and args.policy=='None':
        if mdp_type=='continuing':
            res = value_iteration_cont(np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,discount,epsilon)
            for i in range(numStates):
                print(res[0][i],res[1][i])
        else:
            res=value_iteration_episodic(np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,discount,epsilon)
            for i in range(numStates):
                print(res[0][i],res[1][i])



    elif args.algorithm=='lp' and args.policy=='None':
        if mdp_type=='continuing':
            res = linear_programming_cont(np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,np.float64(discount))
            for i in range(numStates):
                print(res[0][i],res[1][i])
        else:
            res = linear_programming_episodic(np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,np.float64(discount))
            for i in range(numStates):
                print(res[0][i],res[1][i])



    elif args.algorithm=='hpi' and args.policy=='None':
        if mdp_type=='continuing':
            res = howard_policy_iteration_cont(np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,discount,epsilon)
            for i in range(numStates):
                print(res[0][i],res[1][i])
        else:
            res = howard_policy_iteration_episodic(np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,discount,epsilon)
            for i in range(numStates):
                print(res[0][i],res[1][i])


    else:
        res = policy_evaluation(policy,np.int64(numStates),np.int64(numActions),transition_matrix,reward_matrix,discount)
        for i in range(numStates):
            print(res[i],policy[i])
        
