import matplotlib.pyplot as plt
import numpy as np

def kernel_pca(X: np.ndarray, kernel: str) -> np.ndarray:
    '''
    Returns projections of the the points along the top two PCA vectors in the high dimensional space.

        Parameters:
                X      : Dataset array of size (n,2)
                kernel : Kernel type. Can take values from ('poly', 'rbf', 'radial')

        Returns:
                X_pca : Projections of the the points along the top two PCA vectors in the high dimensional space of size (n,2)
    '''
    if (kernel == "rbf"):
        a = X
        b = X.T
        a = np.reshape(a,(a.shape[0],a.shape[1],1))
        b = np.reshape(b,(1,b.shape[0],b.shape[1]))
        sub = a-b
        ex = np.square(sub)
        ex = (-1)*(15)*(np.sum(ex,axis = 1))
        out = np.exp(ex)
    

    elif (kernel == 'poly'):
        a = X
        b = X.T
        add = np.matmul(a,b)+1
        out = np.power(add,5)
       

    elif (kernel == 'radial'):
        r = np.sqrt(np.sum(np.square(X),axis=1))
        r = r[:,None]
        mat1 = np.matmul(r,r.T)
       
        #theta  = np.arctan(X[:,1:]/X[:,0:1])
        theta = np.arctan(X[:,1]/X[:,0])
        theta = theta[:,None]
        
        mat2 = np.matmul(theta,theta.T)

        out = mat1+mat2
    mat = np.ones((out.shape[0],out.shape[0]))/out.shape[0]
    out = out - mat.dot(out) - out.dot(mat) + (mat.dot(out)).dot(mat)
    eigvals = np.linalg.eigh(out)[0]
    eigvals = eigvals[::-1]
    eigvecs = np.linalg.eigh(out)[1]
    eigvecs = eigvecs[:,::-1]
    X_pca = np.column_stack([eigvecs[:, i] for i in range(2)])
  
    
    return X_pca
 
if __name__ == "__main__":
    from sklearn.datasets import make_moons, make_circles
    from sklearn.linear_model import LogisticRegression
  
    X_c, y_c = make_circles(n_samples = 500, noise = 0.02, random_state = 517)
    X_m, y_m = make_moons(n_samples = 500, noise = 0.02, random_state = 517)
    X_c_pca = kernel_pca(X_c, 'radial')
  
    X_m_pca = kernel_pca(X_m, 'rbf')    
    plt.figure()
    plt.title("Data")
    plt.subplot(1,2,1)
    plt.scatter(X_c[:, 0], X_c[:, 1], c = y_c)
    plt.subplot(1,2,2)
    plt.scatter(X_m[:, 0], X_m[:, 1], c = y_m)
    plt.show()

    plt.figure()
    plt.title("Kernel PCA")
    plt.subplot(1,2,1)
    plt.scatter(X_c_pca[:, 0], X_c_pca[:, 1], c = y_c)
    plt.subplot(1,2,2)
    plt.scatter(X_m_pca[:, 0], X_m_pca[:, 1], c = y_m)
    plt.show()
