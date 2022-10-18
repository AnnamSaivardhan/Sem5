import torch 
import numpy as np


a = torch.tensor([
                   [[1,1,1,1],
                    [2,2,2,2],
                    [3,3,3,3]],

                   [[4,4,4,4],
                    [5,5,5,5],
                    [6,6,6,6]],

                   [[7,7,7,7],
                    [8,8,8,8],
                    [9,9,9,9]], 
                                ])

b = torch.tensor([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
#print(a.size()[1])
print(torch.sum(a,dim=0).shape)
print(torch.sum(a,dim=1).shape)
print(torch.sum(a,dim=2).shape)
# https://towardsdatascience.com/understanding-dimensions-in-pytorch-6edf9972d3be link for sum visualisation
# c = a[:,:,3:]
# d = a[:,:,3]
# # now the dimension of d is 2 but c is 3.

c = a[2:,:,:]
print(c)
print(c.shape)