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
    #L, U = np.zeros(A.shape), np.zeros(A.shape)
    ## TODO
    n=A.shape[0]
    print(n)
    L = np.identity(n)
    U=A.copy()
    for i in range(n-1):
      U[i+1:,:]=U[i+1:,:]-((np.tile(U[i,:],1,n-i-1))/U[i,i])*
    print(U)
    ## END TODO
    #assert L.shape == A.shape and U.shape == A.shape, "Return matrices of the same shape as A"
    return U


LU_decomposition(np.array([[1.,1.,0.],[2.,1.,-1.],[3.,-1.,-1.]]))