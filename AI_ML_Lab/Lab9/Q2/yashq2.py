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
    if kernel == 'poly':
        d = 5
        K = (np.dot(X, X.T) + 1) ** d
    elif kernel == 'rbf':
        gamma = 15
        pairwise_D = np.linalg.norm(X[:,None,:] - X[None,:,:], axis = -1) ** 2
        K = np.exp(- gamma * pairwise_D)
    elif kernel == 'radial':
        dist = np.linalg.norm(X, axis=1)
        dist = np.outer(dist, dist)
        deg = np.arctan2(X[:,1], X[:,0])
        deg = np.outer(deg, deg)
        K = dist + deg
    pass
    # Center the kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N,N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + (one_n.dot(K)).dot(one_n)
    # Obtaining eigenpairs from the centered kernel matrix
    # scipy.linalg.eigh returns them in ascending order
    eigvals, eigvecs = np.linalg.eigh(K)
    eigvals, eigvecs = eigvals[::-1], eigvecs[:, ::-1]
    # Collect the top k eigenvectors (projected examples)
    X_pc = np.column_stack([eigvecs[:, i] for i in range(2)])
    return X_pc


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
