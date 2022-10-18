import torch

"""simple Pytorch"""
def ques2_1():


    ## TODO
    A = None
    A=torch.rand(50,40,5)
    ## END TODO

    return A

def ques2_2():

    B = torch.FloatTensor([[1,2,3],[3,2,1]])
    B = B.to(torch.int32)

    ## TODO
    B = torch.FloatTensor([[1,2,3],[3,2,1]])
    B = B.to(torch.int32)
    ## END TODO

    return B

def ques2_3():
    C, D = None, None
    ## TODO
    C=torch.Tensor(3,100)
    x=torch.range(1,4,1)
    x[2]=0
    D=C[torch.tensor(x)]
    ## END TODO

    return C,D

def ques2_4():
    E, F = None, None
    ## TODO

    ## END TODO
    return E,F

def ques2_5():
    G1 = torch.zeros(10,10)
    G2 = torch.ones(10,10)
    G3 = torch.zeros(10,10)

    H = None

    ## TODO

    ## END TODO

    return H


"""Vectorization"""

def d(x,y):
    '''
    Given x and y where each is an np arrays of size (dim,1), compute L2 distance between them
    '''
    
    distance = 0
    
    ##TODO

    ##END TODO

    assert distance >= 0, "distance is npnnegative"
    return distance


print((ques2_2().dtype))