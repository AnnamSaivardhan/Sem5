from platform import java_ver
import numpy as np
import torch
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(335)
torch.manual_seed(335) 

def train_test_split(dataframe):
    total_samples = dataframe.shape[0]
    train_ratio = .8
    random_indices = np.random.permutation(total_samples)
    train_set_size = int(train_ratio * total_samples)
    train_indices = random_indices[:train_set_size]
    test_indices = random_indices[train_set_size:]
    return dataframe.iloc[train_indices], dataframe.iloc[test_indices]


def w_closed_form(X, Y):
    '''
    @params
        X : 2D tensor of shape(n,d)
        n : no of samples for the X dataset
        d : dimension of each sample vector x(i)
        Y : 1D tensor of shape(n,1)
    calculates w_closed : 1D tensor of shape(d,1)
    writes the w_closed as a numpy array into the text file "w_closed.txt"
    returns w_closed
    '''

    # TODO TASK 1 : Write w_closed in form of X, Y matrices
    # Round w_closed upto 4 decimal places
    # w_closed = YOUR CODE HERE
    Xt=torch.t(X)
    a=torch.matmul(Xt,X)
    a=torch.inverse(a)
    b=torch.matmul(Xt,Y)
    w_closed=torch.matmul(a,b)
    #print(w_closed)

    # END TODO

    w_closed = w_closed.detach().squeeze().numpy()
    np.savetxt('w_closed.txt', w_closed, fmt="%f")
    torch.from_numpy(w_closed).unsqueeze(1)
    return w_closed


def l1_loss(X, Y, w):
    '''
    @params
        X : 2D tensor of shape(n,d)
        n : no of samples for the X dataset
        d : dimension of each sample vector x(i)
        y : 1D tensor of shape(n,1)
        w : 1D tensor of shape(d,1)
    return loss : float : scalar real value
    '''

    # TODO TASK 2 : Write l1-loss in form of X, Y, w matrices
    # Please take care of normalization factor 1/n

    # loss = YOUR CODE HERE
    #tr=torch.transpose(w)
    if type(w)==np.ndarray:
        w=torch.from_numpy(w)
    w=torch.reshape(w,(w.shape[0],1))
    loss= Y-torch.matmul(X,w)
    loss=torch.abs(loss)
    loss=torch.sum(loss)/X.shape[0]
    loss=loss.numpy()
    loss=loss.astype(np.float64)
    # END TODO

    return (loss)


def l2_loss(X, Y, w):
    '''
    @params
        X : 2D tensor of size(n,d)
        n : no of samples for the X dataset
        d : dimension of each sample vector x(i)
        Y : 1D tensor of size(n,1)
        w : 1D tensor of size(d,1)
    return loss : np.float64 : scalar real value
    '''

    # TODO TASK 3 : Write l2-loss in form of X, Y, w matrices
    # Please take care of normalization factor 1/n

    # loss = YOUR CODE HERE
    #tr=torch.transpose(w)
    if type(w)==np.ndarray:
        w=torch.from_numpy(w)
    #print(w.shape)
    w=torch.reshape(w,(w.shape[0],1))
    loss= Y-torch.matmul(X,w)
    #print(loss.shape)
    l2=torch.t(loss)
    #print(loss)
    loss=torch.matmul(l2,loss)
    
    loss=torch.sum(loss)/X.shape[0]
    loss=loss.numpy()
    loss=loss.astype(np.float64)

    # END TODO

    return (loss)


def l2_loss_derivative(X, Y, w):
    '''
    @params
        X : 2D tensor of size(n,d)
        n : no of samples for the X dataset
        d : dimension of each sample vector x(i)
        Y : 1D tensor of size(n,1)
        w : 1D tensor of size(d,1)
    return derivative : 1D tensor of size(d,1)
    '''

    # TODO TASK 4 : Write l2-loss-derivative in form of X, Y, w matrices
    # Please take care of normalization factor 1/n

    # derivative = YOUR CODE HERE
    if type(w)==np.ndarray:
        w=torch.from_numpy(w)
    w=torch.reshape(w,(w.shape[0],1))
    #print(w.shape,X.shape)
    b=torch.matmul(X,w)-Y
    b=torch.t(b)
    derivative=(2)*torch.matmul(b,X)/X.shape[0]
    derivative=torch.t(derivative)



    # END TODO

    return (derivative)


def train_model(X_train, Y_train, X_test, Y_test):
    '''
    @params
        X_train : 2D tensor of size(n,d) over which model is trained
        n : no of samples for the X_train dataset
        d : dimension of each sample vector x(i)
        Y_train : 1D tensor of size(n,1) over which model is trained
        X_test : 1D tensor over which test error is calculated
        Y_test : 1D tensor over which test error is calculated
    @returns
        w : 1D tensor of size(d,1) ,  the final optimised w
        epochs : Total iterations it take for algorithm to converge
        test_err : python list containing the l2-loss at each epoch

    '''

    d = X_train.size(dim=1)  # No of features
    w = torch.randn(d, 1).double()  # initialize 
    epsilon = 1e-15  # Stopping precision
    eta = 1e-3  # learning rate
    old_loss = 0
    epochs = 0  # No of times w updates

    test_err = []  # Initially empty list

    while (abs(l2_loss(X_train, Y_train, w) - old_loss) > epsilon):
        old_loss = l2_loss(X_train, Y_train, w)  # compute loss
        dw = l2_loss_derivative(X_train, Y_train, w)  # compute derivate
        w = w - eta * dw  # move in the opposite direction of the derivate
        epochs += 1

        # TODO TASK 5 : Append the l2-error of test dataset to the list test_err
        tes_lss=l2_loss(X_test,Y_test,w)
        test_err.append(tes_lss)

        # YOUR CODE HERE

        # END TODO

    return w, epochs, test_err

if __name__ == '__main__':

    data = pd.read_csv('dataset.csv', index_col=0)
    data_train, data_test = train_test_split(data)

    X_train = (data_train.iloc[:,:-1].to_numpy())
    Y_train = (data_train.iloc[:,-1].to_numpy())
    X_train = torch.from_numpy(X_train)
    Y_train = torch.from_numpy(Y_train).unsqueeze(1)

    X_test = (data_test.iloc[:,:-1].to_numpy())
    Y_test = (data_test.iloc[:,-1].to_numpy())
    X_test = torch.from_numpy(X_test)
    Y_test = torch.from_numpy(Y_test).unsqueeze(1)

    ### UNCOMMENT & RUN THE CODE BELOW AFTER COMPLETING  function w_closed_form(X, Y)###
    
    w_closed = w_closed_form(X_train,Y_train)          # closed form solution for w


    #####


    ### UNCOMMENT & RUN THE CODE BELOW AFTER COMPLETING  function l1_loss(X, Y, w)
    
    l1_loss_train = l1_loss(X_train,Y_train, w_closed)
    l1_loss_train = np.array([l1_loss_train])
    np.savetxt('l1_loss.txt', l1_loss_train, fmt="%f")
    
    #####


    ### UNCOMMENT & RUN THE CODE BELOW AFTER COMPLETING  function l2_loss(X, Y, w)
    
    l2_loss_train = l2_loss(X_train,Y_train, w_closed)
    l2_loss_train = np.array([l2_loss_train])
    np.savetxt('l2_loss.txt', l2_loss_train, fmt="%f")
    
    #####


    ### UNCOMMENT & RUN THE CODE BELOW AFTER COMPLETING  functions l2_loss_derivative(X, Y, w) and train_model(X_train, Y_train, X_test, Y_test)
    
    w_trained, total_epochs, test_err = train_model(X_train, Y_train, X_test, Y_test)
    
    #####


    # TASK 6 : Plot the early stopping criterion
    ### UNCOMMENT & RUN THE CODE BELOW AFTER TRAINING THE ABOVE MODEL
    
    # Code to find e_star: the epoch after which test error starts increasing
    for e_star in range(len(test_err)-1):
        if test_err[e_star+1] > test_err[e_star]:
            break;

    #Code for plotting and saving the figure
    xvals = np.arange(0,len(test_err))
    plt.plot(xvals[e_star-500:e_star+500], test_err[e_star-500:e_star+500])
    plt.xlabel("epochs")
    plt.ylabel("test error")
    plt.savefig("q1.pdf") 

    
    #####





