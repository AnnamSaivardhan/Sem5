import numpy as np
import json
import torch

# create a neural network to predict the grade of the elective subject
class NeuralNet(torch.nn.Module):
    def _init_(self,input_size = 10,output_size = 1):
        super(NeuralNet,self)._init_()
        self.linear1 = torch.nn.Linear(9,8)
    
    def forward(self,x):
        y_pred = self.linear1(x)
        y_pred = torch.nn.functional.softmax(y_pred,dim = 1)
        return y_pred
    
    # use cross entropy loss and backpropagation to train the model
    def train(self,X_train,y_train,learning_rate = 0.01,epochs = 5):
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.SGD(self.parameters(),lr = learning_rate)
        tr_dataset = torch.utils.data.TensorDataset(X_train,y_train)
        train_loader = torch.utils.data.DataLoader(tr_dataset,batch_size = 1,shuffle = False)
        for epoch in range(epochs):
            for i,data in enumerate(train_loader,0):
                inputs,labels = data
                optimizer.zero_grad()
                array = torch.zeros(1,8)
                array[0][labels-1] = 1
                outputs = self.forward(inputs)
                loss = criterion(outputs,array)
                loss.backward()
                optimizer.step()
        print("Training completed")
    
    def predict(self,x_test):
        y_pred = self.forward(x_test)
        return y_pred

if __name__ == '_main_':
    file = open("trainingAndTest/training.json", "r")
    lines = file.readlines()
    file.close()
    n = int(lines[0])
    lines = lines[1:]
    data = np.zeros((n,10))
    dict = {"English":0, "Physics":1, "Chemistry":2, "Biology":3, "PhysicalEducation":4, "Accountancy":5, "BusinessStudies":6, "ComputerScience":7, "Economics":8, "Mathematics":9}
    for i in range(n):
        jsonline = json.loads(lines[i])
        for key in jsonline:
            if key in dict:
                data[i][dict[key]] = jsonline[key]
    X_train = torch.from_numpy(data[:,:9]).float()
    y_train = torch.from_numpy(data[:,9]).long()
    y_train = y_train[:,None]

    net = NeuralNet()
    # train_loader = torch.utils.data.DataLoader(dataset = torch.from_numpy(X_train).float(),batch_size = 1,shuffle = True)
    net.train(X_train,y_train)
    file = open("trainingAndTest/sample-test.in.json", "r")
    lines = file.readlines()
    file.close()
    k = int(lines[0])
    lines = lines[1:]
    data = np.zeros((k,10))
    for i in range(k):
        jsonline = json.loads(lines[i])
        for key in jsonline:
            if key in dict:
                data[i][dict[key]] = jsonline[key]
    X_test = data[:,0:9]
    y_test = net.predict(torch.from_numpy(X_test).float())

    C = 0
    W = 0
    for i in range(k):
        if abs(y_test[i][0] - data[i][9]) <= 1:
            C += 1
        else:
            W += 1
    
    print("Score = ",100*(C-W)/k)