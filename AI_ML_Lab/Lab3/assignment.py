import numpy as np
import time
import torch

def brute_dct(X: np.ndarray) -> np.ndarray:
    
    m, n = X.shape
    img_dct = np.empty((m,n))
    for k1 in range(m):
        for k2 in range(n):
            val = 0
            for n1 in range(m):
                for n2 in range(n):
                    val += 4*X[n1,n2]*np.cos((np.pi/m)*(n1+0.5)*k1)*np.cos((np.pi/n)*(n2+0.5)*k2)
            img_dct[k1, k2] = val

    return img_dct

def vectorized_dct(X: np.ndarray) -> np.ndarray:
    '''
    @params
        X : np.float64 array of size(m,n)
    return np.float64 array of size(m,n)
    '''
    # TODO
    N1=X.shape[0]
    N2=X.shape[1]
    Llt=np.fromfunction(lambda i,j:np.cos((np.pi/N1)*(j+0.5)*i),(N1,N1))
    Rlt=np.fromfunction(lambda i,j:np.cos((np.pi/N2)*(i+0.5)*j),(N2,N2))
    Y = 4*np.matmul(Llt,np.matmul(X,Rlt))
    

    return Y
    # END TODO

def get_document_ranking(D: np.ndarray, Q: np.ndarray) -> np.ndarray:
    '''
    @params
        D : n x w x k numpy float64 array 
            where each n x w slice represents a document
            with n vectors of length w 
        Q : m x w numpy float64 array
            which represents a query with m vectors of length w

    return np.ndarray of shape (k,) of docIDs sorted in descending order by relevance score
    '''
    # TODO
    Z=D.transpose(2,1,0)
    
    






    return None
    # END TODO

def compute_state_probability(M: np.ndarray,S_T: int, T: int, S_a: int) -> np.float64:
    '''
    @params
        M   : nxn numpy float64 array
        S_T : int
        T   : int
        S_a : int

    return np.float64
    '''
    # TODO
    return None
    # END TODO


def compute_state_probability_vec(M: np.ndarray,S_T: int, T: int, S_a: int) -> np.float64:
    '''
    @params
        M   : nxn numpy float64 array
        S_T : int
        T   : int
        S_a : int

    return np.float64
    '''
    # TODO
    return None
    # END TODO

if __name__=="__main__":

    np.random.seed(0)

    # Question 1
    X = np.random.randn(20,30)
    tic = time.time()
    brute_dct_X = brute_dct(X)
    print("Time for non vectorised DCT = ", time.time()-tic)

    tic = time.time()
    vectorized_dct_X = vectorized_dct(X)
    assert X.shape == vectorized_dct_X.shape, "Return matrix of the same shape as X"
    print("Time for vectorised DCT = ", time.time()-tic)
    print("Equality of both DCTs : ", np.all(np.abs(brute_dct_X - vectorized_dct_X) < 5e-4))

    np.savetxt('q1_output.txt', vectorized_dct_X, fmt="%s")
    
    
    # Question 2
    D = np.random.rand(30,6,100)
    Q = np.random.rand(5,6)

    doc_ranking = get_document_ranking(D,Q)
    np.savetxt('q2_output.txt', doc_ranking, fmt="%s")
    
   
    # Question 3
    N = 6
    S_T = 4
    S_a = 2
    T = 5000
    M = np.zeros(shape=(N,N),dtype=np.float64)
    M[1][0] = 0.09
    M[0][1] = 0.23
    M[5][1] = 0.62
    M[1][2] = 0.06
    M[0][3] = 0.77
    M[2][3] = 0.63
    M[3][4] = 0.65
    M[5][4] = 0.38
    M[1][5] = 0.85
    M[2][5] = 0.37
    M[3][5] = 0.35
    M[4][5] = 1.0

    tic = time.time()
    prob_non_vec = compute_state_probability(M,S_T,T,S_a)
    print("[Q3] Time for non vectorised = ", time.time()-tic)

    tic = time.time()
    prob_vec = compute_state_probability_vec(M,S_T,T,S_a)
    print("[Q2] Time for vectorised = ", time.time()-tic)
    print("Equality of both probs : ", abs(prob_non_vec - prob_vec) < 5e-4)
    with open('q3_output.txt','w') as f:
        f.write(str(prob_vec))