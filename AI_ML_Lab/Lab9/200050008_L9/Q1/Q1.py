import numpy as np
from utils import *
############################ Q1 ################################
# Initialize global variable. DO NOT MAKE CHANGES HERE. 
# Change values of kernel parameters in function q1(), NOT HERE.
kernel_params = {'sigma_gauss':1,
                'gamma_rbf':1,
                'sigma_laplace':1}

########## SVM with Gaussian kernel ##########

def gauss_kernel(a,b):
    '''
    Define a Gaussian kernel for a SVM Regressor
    @params
        a: numpy.ndarray shape = (n,d)
        b: numpy.ndarray shape = (n,d)
    return: numpy.ndarray shape = ?
    '''
    sigma = kernel_params['sigma_gauss']
    ######START: TO CODE########
    # print("hi")
    n=a.shape[0]
    d=a.shape[1]
    a = np.reshape(a,(a.shape[0],a.shape[1],1))
    b=b.T
    b = np.reshape(b,(1,b.shape[0],b.shape[1]))
    # print("hello")
    sub = a-b
    ex = np.square(sub)
    # print(ex.shape)
    ex = (-1)*(np.sum(ex,axis = 1))/(2*(sigma**2))
    # print(ex.shape)
    out = np.exp(ex)
    # print(out.shape)
    return out
    ######END: TO CODE########

########## SVM with RBF kernel ##########

def rbf_kernel(a,b):
    '''
    Define a Gaussian RBF kernel for a SVM Regressor
    @params
        a: numpy.ndarray shape = (n,d)
        b: numpy.ndarray shape = (n,d)
    return: numpy.ndarray shape = ?
    '''
    gamma = kernel_params['gamma_rbf']
    ######START: TO CODE########
    
    n=a.shape[0]
    d=a.shape[1]
    a = np.reshape(a,(a.shape[0],a.shape[1],1))
    b=b.T
    b = np.reshape(b,(1,b.shape[0],b.shape[1]))
    sub = a-b
    ex = np.square(sub)
    ex = (-1)*(gamma)*(np.sum(ex,axis = 1))
    out = np.exp(ex)
    return out
    ######END: TO CODE########

 ########## SVM with Laplacian RBF kernel ##########

def laplace_kernel(a,b):
    '''
    Define a Laplacian RBF kernel for a SVM Regressor
    @params
        a: numpy.ndarray shape = (n,d)
        b: numpy.ndarray shape = (n,d)
    return: numpy.ndarray shape = ?
    '''
    sigma = kernel_params['sigma_laplace']
    ######START: TO CODE########
    
    n=a.shape[0]
    d=a.shape[1]
    a = np.reshape(a,(a.shape[0],a.shape[1],1))
    b=b.T
    b = np.reshape(b,(1,b.shape[0],b.shape[1]))
    ex = a-b
    #ex = np.square(sub)
    ex = np.abs(ex)
    ex = (-1)*(np.sum(ex,axis = 1))/(sigma)
    #ex = (-1)*np.sqrt(ex)
    out = np.exp(ex)
    return out
    ######END: TO CODE########
        
def q1():
    global kernel_params
    print("Dataset 1\n")
    X_train, X_test, y_train, y_test = get_dataset1()

    # The tunable hyperparmeters for the 3 kernels - all initialized to 1
    # Change values to the optimal values for dataset 1
    ######START: TO DO########
    kernel_params = {'sigma_gauss':2,
                    'gamma_rbf':0.125,
                    'sigma_laplace':15}
    ######END: TO DO########
    
    reg1 = SVM_Regression(kernel=gauss_kernel)
    reg1.train(X_train,y_train)
    print("Gaussian Kernel Score: ",reg1.get_score(X_test,y_test)) #Higher score = better fit
    reg1.plot(X_train,y_train)
    
    reg2 = SVM_Regression(kernel=rbf_kernel)
    reg2.train(X_train,y_train)
    print("RBF Kernel Score: ",reg2.get_score(X_test,y_test)) #Higher score = better fit
    reg2.plot(X_train,y_train)
    
    reg3 = SVM_Regression(kernel=laplace_kernel)
    reg3.train(X_train,y_train)
    print("Laplacian RBF Kernel Score: ",reg3.get_score(X_test,y_test)) #Higher score = better fit
    reg3.plot(X_train,y_train)
    
    print("Dataset 2\n")
    X_train, X_test, y_train, y_test = get_dataset2()

    # The tunable hyperparmeters for the 3 kernels - all initialized to 1
    # Change values to the optimal values for dataset 2
    ######START: TO DO########
    kernel_params = {'sigma_gauss':2,
                    'gamma_rbf':0.1,
                    'sigma_laplace':13}
    ######END: TO DO########
    
    reg1 = SVM_Regression(kernel=gauss_kernel)
    reg1.train(X_train,y_train)
    print("Gaussian Kernel Score: ",reg1.get_score(X_test,y_test)) #Higher score = better fit

    reg2 = SVM_Regression(kernel=rbf_kernel)
    reg2.train(X_train,y_train)
    print("RBF Kernel Score: ",reg2.get_score(X_test,y_test)) #Higher score = better fit

    reg3 = SVM_Regression(kernel=laplace_kernel)
    reg3.train(X_train,y_train)
    print("Laplacian RBF Kernel Score: ",reg3.get_score(X_test,y_test)) #Higher score = better fit


if __name__ == "__main__":
    print("#"*15, "Q1", "#"*15)
    try:
        q1()
    except:
        print("Error while solving Q1")
    # q1()
    