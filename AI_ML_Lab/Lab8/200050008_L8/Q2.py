
import time
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import os
from sklearn import svm

############################ Q2 ################################

def Q2_kernel_1(a,b):
    '''
    Look at the diagram from the question part 1 & 
    write an appropriate kernel which returns a scalar value 
    determining the relation of input in higher dimension space
    Input to everyone will be common
    Output will be graded based on accuracy of the classfier learnt with the help of the kernel
    Try to find generalized solutions rather than overfitting the test cases
    ALSO COMMENT THE KERNEL WHICH YOU HAVE IMPLEMENTED
    @params
        a: numpy.ndarray shape = (n,d)
        b: numpy.ndarray shape = (n,d)
    return: numpy.ndarray shape = ?
    '''
    ######START: TO CODE########
    out = np.ndarray(0)
    out=np.power(1+(a@b.T),1)
    return out
    ######END: TO CODE########

def Q2_kernel_2(a,b):
    '''
    Look at the diagram from the question part 2 & 
    write an appropriate kernel which returns a scalar value 
    determining the relation of input in higher dimension space
    Input to everyone will be common
    Output will be graded based on accuracy of the classfier learnt with the help of the kernel
    Try to find generalized solutions rather than overfitting the test cases
    Hint: This kernel has an important hyperparameter which controls 
        upto what dimension non linearity should be mapped
    @params
        a: numpy.ndarray shape = (n,d)
        b: numpy.ndarray shape = (n,d)
    return: numpy.ndarray shape = ?
    ALSO COMMENT THE KERNEL WHICH YOU HAVE IMPLEMENTED
    '''
    ######START: TO CODE########
    out = np.ndarray(0)
    out=np.power(1+(a@b.T),2)
    return out
    ######END: TO CODE########


def Q2_kernel_3(a,b):
    '''
    For this question assume that the data is linearly separable in very high dimensional space
    Hint: This kernel is theoretically capable of learning infinite dimension transformations. 
    Input to everyone will be common
    Output will be graded based on accuracy of the classfier learnt with the help of the kernel
    Try to find generalized solutions rather than overfitting the test cases
    @params
        a: numpy.ndarray shape = (n,d)
        b: numpy.ndarray shape = (n,d)
    return: numpy.ndarray shape = ?
    ALSO COMMENT THE KERNEL WHICH YOU HAVE IMPLEMENTED
    '''
    ######START: TO CODE########
    out = np.ndarray(0)
    out=np.power(1+(a@b.T),3)
    return out
    ######END: TO CODE########