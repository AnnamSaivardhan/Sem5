import torch 
import numpy as np
a = torch.tensor([[1,1,1,1],[2,2,2,2]])
b = torch.tensor([[1,1],[1,1]])
c = a+b
print(c.shape)
print(c)