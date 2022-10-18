import torch 
import numpy as np



list1 = [1,2,3,4]
tensor_list1 = torch.tensor(list1)
tensor_list2 = torch.tensor([5,6,7,8])
tensor_2d = torch.tensor([[1,2,3],[4,5,6]])
tensor_3d = torch.ones((2,3,4))
scalar = torch.tensor(3)


#SIZE: 
print("tensor_list1 ",tensor_list1.size())
print("tensor_2d ",tensor_2d.size())
print("tensor_3d ",tensor_3d.size())
print("list1 ", len(list1))
#SHAPE: it does not have ()
print("tensor_list1 ",tensor_list1.shape)
print("tensor_2d ",tensor_2d.shape)
print("tensor_3d ",tensor_3d.shape)
print("scalar ",scalar.shape)
#ndim , dim gives nummber of dimensions
print("tensor_list1 ",tensor_list1.ndimension())
print("tensor_2d ",tensor_2d.ndimension())
print("tensor_3d ",tensor_3d.ndimension())
print("tensor_list1 ",tensor_list1.dim())
print("tensor_2d ",tensor_2d.dim())
print("tensor_3d ",tensor_3d.dim())

#OBSERVATIONS: USE SHAPE OR SIZE METHOD, SHAPE;
#Shape as (n,) is observed in numpy but not in pytorch
# [1,2,3,4] shape is (4,) in numpy and [4] in torch
# scalar shape is undefined in numpy but torch shows as []
