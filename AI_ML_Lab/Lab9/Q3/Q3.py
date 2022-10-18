from utils import *
import numpy as np


############ QUESTION 3 ##############
class KR:
	def __init__(self, x,y,b=1):
		self.x = x
		self.y = y
		self.b = b
	
	def gaussian_kernel(self, z):
		'''
		Implement gaussian kernel
		''' 
		
		a = (self.x).T
		a = np.reshape(a,(1,a.shape[0],a.shape[1]))
		b = np.reshape(z,(z.shape[0],z.shape[1],1))
		sub = (b-a)/self.b
		sub = np.exp(-1*np.sum(np.square(sub)/2,axis=1))/np.sqrt(2*np.pi)
		sum_arr = np.sum(sub,axis=1)		
		sum_arr = np.reshape(sum_arr,(sub.shape[0],1))
		return self.x.shape[0]*sub/sum_arr


		
	def predict(self, x_test):
		'''
		returns predicted_y_test : numpy array of size (x_train, ) 
		'''
		b = self.y
		b = np.reshape(b,(b.shape[0],1))
		out = self.gaussian_kernel(x_test)
		pred = np.matmul(out,b)/self.x.shape[0]
		return pred
		
def q3():
	#Kernel Regression
	x_train, x_test, y_train, y_test = get_dataset()
	
	obj = KR(x_train, y_train)
	
	y_predicted = obj.predict(x_test)
	
	print("Loss = " ,find_loss(y_test, y_predicted))


# q3()
	
