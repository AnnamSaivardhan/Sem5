
import time
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import os
from sklearn import svm


############################ Q3 ################################

def q3(x, w, b, conv_param):
    """
    A naive implementation of convolution.
    The input consists of N data points, each with C channels, height H and
    width W. We convolve each input with F different filters, where each filter
    spans all C channels and has height HH and width WW.
    Input:
    - x: Input data of shape (N, C, H, W)
    - w: Filter weights of shape (F, C, HH, WW)
    - b: Biases, of shape (F,)
    - conv_param: A dictionary with the following keys:
      - 'stride': The number of pixels between adjacent receptive fields in the
        horizontal and vertical directions.
      - 'pad': The number of pixels that will be used to zero-pad the input.
    Returns a tuple of:
    - out: Output data, of shape (N, F, H', W') where H' and W' are given by
      H' = 1 + (H + 2 * pad - HH) / stride
      W' = 1 + (W + 2 * pad - WW) / stride
    - cache: (x, w, b, conv_param)
    """
    ###########################################################################
    # TODO: Implement the convolutional forward pass.                         #
    # Hint: you can use the function np.pad for padding.                      #
    ###########################################################################
   
    padding, stride = conv_param['pad'], conv_param['stride']
    ip = int(padding)
    iss = int(stride)
    z=0
    #print(z)
    x0=x.shape[0]
    x3=x.shape[3]
    x2=x.shape[2]
    w0=w.shape[0]
    w3=w.shape[3]
    w2=w.shape[2]
    var1=1+(x2+2*ip-w2)//iss
    z=z+1
    #print(z)
    var2=1+(x3+2*ip-w3)//iss
    z=z+1
    y=z
    y=0
    z=0
    #print(z)
    out=np.zeros((x0,w0,var1,var2))
    x_pad=np.pad(x,((0,0), (0,0), (padding,padding), (padding,padding)),'constant')
    for i in range(var1):
      for j in range(var2):
        y=y+1
        #print(y)
        x_m=x_pad[:,:,i*stride:i*stride+w.shape[2],j*stride:j*stride+w.shape[3]]
        for k in range(w.shape[0]):
          z=z+1
          #print(z)
          out[:,k,i,j]=np.sum(x_m*w[k,:,:,:],axis=(1,2,3))
    out+=(b)[None,:,None,None]

    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b, conv_param)
    return out, cache

def gram(x):
  ######START: TO CODE########
  #Returns the gram matrix
  y=x
  va=1
  #print(va)
  s2=y.shape[2]
  va+=1
  z = np.transpose(y, (2, 0, 1))
  #print(va)
  z=z.reshape(s2, -1)
  va+=1
  z2=np.tr
  x = np.matmul(z, z2)
  va+=1
  # assert gram.shape == (C, C)
  return x
  ######END: TO CODE########


def relative_error(x, y):
    """ returns relative error """
    return np.max(np.abs(x - y) / (np.maximum(1e-8, np.abs(x) + np.abs(y))))