import pandas as pd
import numpy as np
import torch
import matplotlib.pyplot as plt
np.random.seed(20)

def data_generate():
  '''
  Generates the data, returns X and Y in the appropriate shape.
  Return: A dictionary containing X_train, Y_train, X_test and Y_test
  '''
  data = pd.read_csv('generated_data.csv')
    
  total_samples = data.shape[0]
  train_ratio = .8
  random_indices = np.random.permutation(total_samples)
  train_set_size = int(train_ratio*total_samples)
    
  train_indices =  random_indices[:train_set_size]
  test_indices = random_indices[train_set_size:]
    
  data.iloc[train_indices], data.iloc[test_indices] 
  X_train = (data.iloc[train_indices].iloc[:,:-1]).to_numpy()     # Design matrix for train data 
  y_train = (data.iloc[train_indices].iloc[:,-1]).to_numpy()      # Labels for train data
  y_train = y_train.reshape((y_train.shape[0],1))

  X_test = (data.iloc[test_indices].iloc[:,:-1]).to_numpy()       # Design matrix for test data
  y_test = (data.iloc[test_indices].iloc[:,-1]).to_numpy()        # Labels for test data
  y_test = y_test.reshape((y_test.shape[0],1))

  return {'X_train': X_train, 'Y_train':y_train,
         'X_test': X_test, 'Y_test': y_test}


def create_weights(data_dictionary, lambda_val):
    '''
    Creates the weights matrix using the closed form solution of 
    ridge regression
    Input:
        data_dictionary: A dictionary containing X_train, Y_train, X_test and Y_test
        lambda_val: The hyperparameter value (of lambda) for the ridge regression
    Output: The weights matrix
    '''
    ####TO DO####
    ####You are free to add variables to help you in the calculation####
    X_train=data_dictionary["X_train"]
    Y_train=data_dictionary["Y_train"]
    X_test=data_dictionary["X_test"]
    Y_test=data_dictionary["Y_test"]
    Xt=np.transpose(X_train)
    #Xt=torch.t(X_train)
    iden=np.identity(Xt.shape[0])*lambda_val
    weights=np.matmul(np.linalg.inv((np.matmul(Xt,X_train)+iden)),np.matmul(Xt,Y_train))
    
    
    #####END TO DO########
    
    return weights
    
def generate_test_error(data_dictionary, weights):
    '''
    Generates the test error value for a particular weights matrix
    Input:
        data_dictionary: A dictionary containing X_train, Y_train, X_test and Y_test
        weights: The weights matrix generated through create_weights function
    Output: 
        The test error [float]
    '''
    ####TO DO####
    ####You are free to add variables to help you in the calculation####
    ####Add the code to find the test error value for a lambda value
    X_train=data_dictionary["X_train"]
    Y_train=data_dictionary["Y_train"]
    X_test=data_dictionary["X_test"]
    Y_test=data_dictionary["Y_test"]
    test_error=np.sum(np.square(np.matmul(X_test,weights)-Y_test))/X_test.shape[0]
    
    
    #####END TO DO########
    
    return test_error

def plot_it(error_array, lambda_array):
    '''
    Plots lambda vs test error and saves it to 'Q2.png'
    Input:
        error_array: Array of the found test errors
        lambda_array: Array of the lambda values used
    '''
    ####TO DO####
    ####You are free to add variables to help you in the calculation####
    ####Add the code to plot the errors vs lambda, also code for saving it###
    plt.plot(lambda_array, error_array)
    plt.xlabel("lambda_value")
    plt.ylabel("test_error")
    plt.savefig("Q2.png")
    
    
    
    #####END TO DO########
    #No return statement necessary here


if __name__=="__main__":
    
    data_dictionary = data_generate()
    error_array = []
    lambda_array = []
    ####TO DO####
    ####You are free to add variables to help you in the calculation####
    ####Add the code to generate weights, find weights and corresponding errors###
    ####HINT: You are expected to loop over different values of lambda and 
    lambda_array=np.arange(0,0.5,0.005)
    for lam in lambda_array:
        error_array.append(generate_test_error(data_dictionary,create_weights(data_dictionary,lam)))
    
    
    
    #####END TO DO########
    
    plot_it(error_array, lambda_array)
    