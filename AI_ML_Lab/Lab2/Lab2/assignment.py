import numpy as np
import torch
import time

""" LU Decomposition"""

def LU_decomposition(A: np.array):
    """
    A: A numpy array of size nxn

    Returns:
      L: A numpy asrray of size nxn
      U: A numpy array of size nxn
    """
    ## TODO
    A=A.astype(np.float64)
    n=A.shape[0]
    L = np.identity(n)
    L=L.astype(np.float64)
    U=A.copy()
    for i in range(n-1):
      L[i+1:,i:i+1]=(U[i+1:,i:i+1])/U[i][i]
      U[i+1:,:]=U[i+1:,:]- (U[i+1:,i:i+1]@U[i:i+1,:])/U[i][i]
    ## END TODO
    assert L.shape == A.shape and U.shape == A.shape, "Return matrices of the same shape as A"
    return L, U



"""simple Pytorch"""
def ques2_1():

    A = None

    ## TODO
    A=torch.rand(50,40,5)
    ## END TODO

    return A

def ques2_2():

    B = torch.FloatTensor([[1,2,3],[3,2,1]])

    ## TODO
    B = B.to(torch.int32)
    ## END TODO

    return B

def ques2_3():
    C, D = None, None
    ## TODO
    C=torch.rand(3,100)
    D=torch.roll(C,1,0)
    ## END TODO

    return C,D

def ques2_4():
    E, F = None, None
    ## TODO
    E=torch.rand(20,10)
    F=torch.sum(E,1)
    ## END TODO
    return E,F

def ques2_5():
    G1 = torch.zeros(10,10)
    G2 = torch.ones(10,10)
    G3 = torch.zeros(10,10)

    H = None
    
    H=torch.stack((G1,G2,G3),2)
    ## TODO

    ## END TODO

    return H


"""Vectorization"""

def pairwise_ranking_loss_looped(P,N):
    '''
    Given P an np array of size (n_1), 
          N an np array of size (n_2), 
    return L(P,N), an scalar (loss) according to the problem given
    '''
    
    loss = 0

    ## STEP 2 - Complete the for loop below

    for i in range(len(P)):
        for j in range (len(N)):
            ##TODO
            loss=loss+max(0,N[j]-P[i])
            ##END TODO
    print(loss)
    return loss 


def pairwise_ranking_loss_vec(P, N):
    '''
    Given P an np array of size (n_1), 
          N an np array of size (n_2), 
    return L(P,N), an scalar (loss) according to the problem given

    This problem can be simplified in the following way - 
   
    '''

    loss = 0
    ## TODO
    P=torch.tensor(P)
    P=torch.reshape(P,(P.shape[0],1))
    N=torch.tensor(N)
    #Z=N-torch.transpose(P,0,-1)
    Z=N-P
    #Z=torch.nn.functional.relu(Z)
    Z[Z<0]=0
    loss=torch.sum(Z)
    ## END TODO
    return loss

if __name__ == '__main__':

    np.random.seed(28963)

    # Problem 1
    A = np.array([
            [1, 1, -2],
            [1, 3, -1],
            [2, 1, -5]
        ])
    L, U = LU_decomposition(A)
    print(L, U)

    # Problem 2
    A = ques2_1()
    B = ques2_2()
    C, D = ques2_3()
    E, F = ques2_4()
    H = ques2_5()


    ## You can manipulate P, N to check correctness of your solution
    n1, n2 = 100, 200
    P, N = np.random.rand(n1), np.random.rand(n2)

    t1 = time.time()
    loss_loop = pairwise_ranking_loss_looped(P, N)
    t2 = time.time()
    loss_vec  = pairwise_ranking_loss_vec(P, N)
    t3 = time.time()

    assert abs(loss_vec - loss_loop) <= 1e-3  # Checking that the two computations match
    print("Vectorized time : {}, Loop time : {}".format(t3-t2,t2-t1))