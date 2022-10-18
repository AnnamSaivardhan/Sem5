from utils import *
import numpy as np


############ QUESTION 3 ##############
class KR:
	def __init__(self, x,y,b=1):
		self.x = x
		self.y = y
		self.b = 1
	
	def gaussian_kernel(self, z):
		'''
		Implement gaussian kernel
		'''

		N = self.x.shape[0]
		a = self.x[:,:,None]
		b = np.transpose(z,(1,0))
		# t = 15
		b = b[None,:,:]
		subtract = (a-b)/self.b
		# print(subtract[0])
		subtract = np.exp(-1*np.sum(np.square(subtract)/2,axis=1))/np.sqrt(2*np.pi)
		print(subtract[0])
		totalsums = np.sum(subtract,axis=0)
		totalsums = totalsums[None,:]
		subtract = np.divide(subtract,totalsums)
		subtract = np.transpose(subtract)
		return subtract*N
		
	def predict(self, x_test):
		'''
		returns predicted_y_test : numpy array of size (x_train, ) 
		'''
		N = self.x.shape[0]
		weights = self.gaussian_kernel(x_test)
		y = self.y
		y = y[:,None]
		val = np.matmul(weights,y)/N
		return val
		
		
def q3():
	#Kernel Regression
	x_train, x_test, y_train, y_test = get_dataset()
	
	obj = KR(x_train, y_train)
	
	y_predicted = obj.predict(x_test)
	
	print("Loss = " ,find_loss(y_test, y_predicted))

q3()