import torch
z= torch.tensor([[[1,1],[2,2]],[[1,1],[3,3]],[[1,2],[1,1]]])
k=torch.tensor([0,0])
z[z.sum(dim=2)==2]=k
print(z)