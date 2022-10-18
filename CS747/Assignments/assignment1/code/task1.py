"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the base Algorithm class that all algorithms should inherit
from. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)

We have implemented the epsilon-greedy algorithm for you. You can use it as a
reference for implementing your own algorithms.
"""

import numpy as np
import math
# Hint: math.log is much faster than np.log for scalars

class Algorithm:
    def __init__(self, num_arms, horizon):
        self.num_arms = num_arms
        self.horizon = horizon
    
    def give_pull(self):
        raise NotImplementedError
    
    def get_reward(self, arm_index, reward):
        raise NotImplementedError

# Example implementation of Epsilon Greedy algorithm
class Eps_Greedy(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # Extra member variables to keep track of the state
        self.eps = 0.1
        self.counts = np.zeros(num_arms)
        self.values = np.zeros(num_arms)
    
    def give_pull(self):
        if np.random.random() < self.eps:
            return np.random.randint(self.num_arms)
        else:
            return np.argmax(self.values)
    
    def get_reward(self, arm_index, reward):
        self.counts[arm_index] += 1
        n = self.counts[arm_index]
        value = self.values[arm_index]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.values[arm_index] = new_value


# START EDITING HERE



def kl(a,b):
    if a==0:
        return math.log(1/(1-b))
    elif a==1:
        return math.log(1/b)
    else:
        return (a*math.log(a/b)+(1-a)*math.log((1-a)/(1-b)))


def q_calc(pa,ua,rhs):
    if pa==1:
        return 1
    i=np.float64(pa)
    j=np.float64(0.999)
    rhs=rhs/ua
    while(j-i>=0.0001):
        z=(i+j)/2
        if(kl(pa,z)<rhs):
            i=z+0.0001
        else:
            j=z-0.0001
    return (i+j)/2



# def vec_fun(means,counts,rhs):
#     my_fun=np.vectorize(q_calc)
#     return my_fun(means,counts,rhs)



# You can use this space to define any helper functions that you need
# END EDITING HERE

class UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.counts=np.zeros(num_arms)  #to store the number of times each arm is pulled
        self.ucbs=np.zeros(num_arms)   #to store ucb of each arm
        self.rews=np.zeros(num_arms)   #to store total rewards of each arm
        self.means=np.zeros(num_arms)  #to store empirical means of each arms
        self.pulls=0
        self.zero_ind=0
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        if self.zero_ind<self.num_arms:
            return self.zero_ind
        else:
            return np.argmax(self.ucbs)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        if self.zero_ind<self.num_arms-1:
            self.rews[arm_index]+=reward
            self.counts[arm_index]+=1
            self.pulls+=1
            self.zero_ind+=1
        elif self.zero_ind==self.num_arms-1:
            self.rews[arm_index]+=reward
            self.counts[arm_index]+=1
            self.pulls+=1
            self.zero_ind+=1
            self.means=np.divide(self.rews,self.counts)
            x=np.sqrt(2*math.log(self.pulls)/self.counts)
            self.ucbs=self.means+x
        else:
            self.counts[arm_index]+=1
            self.rews[arm_index]+=reward
            self.pulls+=1
            self.means=np.divide(self.rews,self.counts)
            x=np.sqrt(2*math.log(self.pulls)/self.counts)
            self.ucbs=self.means+x
            
        # END EDITING HERE

class KL_UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        
        self.counts=np.zeros(num_arms)  #to store the number of times each arm is pulled
        self.klucbs=np.zeros(num_arms)   #to store ucb of each arm
        self.rews=np.zeros(num_arms)   #to store total rewards of each arm
        self.means=np.zeros(num_arms)  #to store empirical means of each arms
        self.pulls=0
        self.zero_ind=0


        
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        if self.zero_ind<self.num_arms:
            #print(self.zero_ind)
            return self.zero_ind
        else:
            #print(np.argmax(self.klucbs))
            return np.argmax(self.klucbs)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        if self.zero_ind<self.num_arms-1:
            self.rews[arm_index]+=reward
            self.counts[arm_index]+=1
            self.pulls+=1
            self.zero_ind+=1
        elif self.zero_ind==self.num_arms-1:
            self.rews[arm_index]+=reward
            self.counts[arm_index]+=1
            self.pulls+=1
            self.zero_ind+=1
            self.means=np.divide(self.rews,self.counts)
            rhs = math.log(self.pulls)+3*math.log(math.log(self.pulls))
            for i in range(self.num_arms):
                self.klucbs[i]=q_calc(self.means[i],self.counts[i],rhs)
            #self.klucbs=np.divide(vec_fun(self.means,rhs),self.counts,rhs)
        else:
            self.counts[arm_index]+=1
            self.rews[arm_index]+=reward
            self.pulls+=1
            self.means=np.divide(self.rews,self.counts)
            rhs = math.log(self.pulls)+3*math.log(math.log(self.pulls))
            for i in range(self.num_arms):
                self.klucbs[i]=q_calc(self.means[i],self.counts[i],rhs)

        
        # END EDITING HERE


class Thompson_Sampling(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.succs=np.ones(num_arms)
        self.fails=np.ones(num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        arr=np.zeros(self.num_arms)
        for i in range(self.num_arms):
            arr[i]=np.random.beta(self.succs[i],self.fails[i])
        return np.argmax(arr)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        if reward==1:
            self.succs[arm_index]+=1
        else:
            self.fails[arm_index]+=1
        # END EDITING HERE
