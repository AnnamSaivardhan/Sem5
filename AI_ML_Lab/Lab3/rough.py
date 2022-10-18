import numpy as np
import time


A=np.ones((4,2,3))
B=np.ones((3,2))
print(B@A.transpose(0,2,1))


