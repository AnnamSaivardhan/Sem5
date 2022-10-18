
import time
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import os



############################ Q3 ################################

def GaussianFilter(x, w,stride):
    """
    A naive implementation of gradient filter convolution.
    The input consists of N data points,height H and
    width W. We convolve each input with F different filters and has height HH and width WW.
    Input:
    - x: Input data of shape (N, H, W)
    - w: Filter weights of shape (F, HH, WW)
    - stride: The number of pixels between adjacent receptive fields in the
        horizontal and vertical directions.
    Return:
   - out: Output data, of shape (N, F, H, W)
    """
    ##Note:if the mean value from a filter is float,perform ceil operation i.e.,29.2--->30
    #################### Enter Your Code Here
    N = x.shape[0]
    F = w.shape[0]
    HH = w.shape[1]
    H = x.shape[1]
    W = x.shape[2]
    WW = w.shape[2]
    dum1=0
    out = x.copy()
    out = np.reshape(out, (N, 1, H, W))
    a = (H-HH)/stride
    dum2=1
    b = (W-WW)/stride
    dum3=1
    for f in range(F): 
        dum1+=1
        for i in range(N):  
          dum2+=1
          for h1 in range(int(1+(a))):
              dum3+=1  
              for w1 in range(int(1+b)):
                hpos = w1*stride   
                vpos = h1*stride
                p = w[f,:,:]
                q = x[i,vpos:vpos+HH,hpos:hpos+WW]
                s = (q*p)
                out[i, f, h1+HH//2, w1+WW//2] = np.ceil(np.sum(s)/np.sum(w[f, :, :]))
    print(out)
    return out
x_shape = (1, 6,6)
w_shape = (1,3,3)
x = np.array([[15,20,25,25,15,10],[20,15,50,30,20,15],[20,50,55,60,30,20],[20,15,65,30,15,30],[15,20,30,20,25,30],[20,25,15,20,10,15]]).reshape(x_shape)
w = np.array([[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]]).reshape(w_shape)
stride=1
out = GaussianFilter(x, w, stride)
# correct out=array([[[[15, 20, 25, 25, 15, 10],
#          [20, 29, 38, 35, 24, 15],
#          [20, 36, 48, 43, 29, 20],
#          [20, 31, 42, 37, 27, 30],
#          [15, 24, 29, 25, 22, 30],
#          [20, 25, 15, 20, 10, 15]]]])