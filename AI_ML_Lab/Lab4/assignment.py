from cmath import log
import numpy as np 
import torch
import matplotlib.pyplot as plt
import torch.utils.data as data_utils
import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
"""
    NO EDITS REQUIRED IN THIS FUNCTION. 
"""
def train(args, Xtrain, Ytrain, Xval, Yval, model ):
    """
      tr_dataset : Num training samples * feature_dimension
      Trains for fixed number of epochs
      Keeps track of training loss and validation accuracy
    """
    tr_dataset = data_utils.TensorDataset(Xtrain, Ytrain)
    loader = data_utils.DataLoader(tr_dataset, batch_size=args.batch_size, shuffle=True)
    eval_dataset = data_utils.TensorDataset(Xval, Yval)
    eval_loader = data_utils.DataLoader(eval_dataset, batch_size=args.batch_size, shuffle=False)
    # build model
    opt = torch.optim.Adam(filter(lambda p : p.requires_grad, model.parameters()),\
                           lr=args.lr, weight_decay=args.weight_decay)
    losses = []
    val_accs = []
    for epoch in range(args.epochs):
        n2=0
        total_loss = 0
        model.train()
        for batch in loader:
            opt.zero_grad()
            pred = model(batch[0])
            #n+=batch[0].shape[0]
            label = batch[1]
            loss = model.loss(pred, label)
            loss.backward()
            opt.step()
            total_loss += loss.item()
        losses.append(total_loss)
        val_acc,n = evaluate(eval_loader, model)
        if args.model_type=='svm' or args.model_type=='nll':
            val_acc = val_acc/n
        val_accs.append(val_acc)
        val_acc=val_acc.item()
        print("Epoch ", epoch, "Loss: ", total_loss, "Val Acc.: ", val_acc)
    return val_accs, losses

"""
    NO EDITS REQUIRED HERE.
"""
class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

"""
    NO EDITS REQUIRED IN THIS FUNCTION. 
"""
def set_seed(x=4):
    # Set random seeds
    seed = x
    random.seed(seed)
    np.random.seed(seed + 1)
    torch.manual_seed(seed + 2)

"""
    NO EDITS REQUIRED IN THIS FUNCTION. 
"""
def plot(val_accs, losses):
    """
        You can use this function to visualize progress of
        the training loss and validation accuracy  
    """
    plt.figure(figsize=(14,6))

    plt.subplot(1, 2, 1)
    plt.xlabel("Epoch", fontsize=18)
    plt.ylabel("Val Accuracy", fontsize=18)
    plt.plot(val_accs)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    plt.subplot(1, 2, 2)
    plt.xlabel("Epoch", fontsize=18)
    plt.ylabel("Train Loss", fontsize=18)
    plt.plot(losses)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    #plt.show()



class ModelClass(torch.nn.Module):
    def __init__(self, args,input_dim):
        super(ModelClass, self).__init__()
        """
            Initialize the linear layer and any hyper-parameters here 
            You can add optional layers like relu as per you discretion 
            Any model parameter should be hard-coded here, do not add it to args 
        """
        self.args  = args
        self.input_dm = input_dim
        ######### TODO: Your code starts here ###############
        self.lin = torch.nn.Linear(input_dim, 1)
        
        ######### Your code ends here  ################

    def forward(self, data):
        """
            Implement forard pass here
            Input: data is the batched data of shape (BATCH_SIZE * num_features)
            Output: Returns pred of shape BATCH_SIZE * 1 
            Note: pred will be autograd tensor
        """
        if self.args.model_type == "svm": 
            ##### TODO: Your code starts here###### 
            pred=self.lin(data)
           # print("pred-shape:",pred.shape)
            #pass       
            ######Your code ends here##########
        elif  self.args.model_type == "nll":
            ##### TODO: Your code starts here######  
            pred=torch.sigmoid(self.lin(data))
            pred=torch.reshape(pred,(data.shape[0],1))
            #pass       
            ######Your code ends here##########
        elif  self.args.model_type == "ranking":
            ##### TODO: our code starts here###### 
            pred=self.lin(data)
            #print(pred.shape) 
            #pass
            ######Your code ends here##########
        else: 
            raise NotImplementedError()
        return pred

    def loss(self, pred, label):
        """
          Input : pred  : tensor of shape BATCH_SIZE*1
                  label : tensor of shape BATCH_SIZE*1
          Output: returns single valued autograd tensor 
        """
        if self.args.model_type == "svm": 
            ##### TODO: Your code starts here#########
            label=torch.reshape(label,pred.shape)
            
            #label=2*label-1
            label[label==0]=-1
            #print(label.shape,pred.shape)
            loss=1-torch.mul(label,pred)
            loss[loss<=0]=0
            #print(loss.shape)
            loss=torch.sum(loss)

            #pass       
            ######Your code ends here##########
        elif  self.args.model_type == "nll":
            ##### TODO: Your code starts here######  
           # print("Hello")
            #print(label)
            x=torch.log(pred)
            label=torch.reshape(label,pred.shape)
            y=torch.log(1-pred)
            #print(x)
            #print((((label*torch.log(pred)))))
            loss = -1*torch.sum((torch.mul(label,x)+torch.mul(1-label,y)))/pred.shape[0]
            #pass       
            ######Your code ends here##########
        elif  self.args.model_type == "ranking":
            ##### TODO: Your code tarts here######  
            negs=pred[label==0]
            pos=pred[label==1]
            negs=torch.reshape(negs,(1,negs.shape[0]))
            arr=negs-pos
            arr[arr<0]=0
            loss=torch.sum(arr)
            #pass
            ######Your code ends here##########
        else: 
            raise NotImplementedError()
        
        return loss

def evaluate(loader, model):
    """
        Testing module used for evaluation of validation data/ test data 
        Input:  loader : DataLoader object 
                model : model object
        Output: eval_score: the evaluation score for the model. 
                            Single valued torch tensor. 
                            "requires_grad=True" not necessary, since this is not used for backprop
        evaluation depends on model prediction and ground truth labels
        NOTE: In this function, you first need to use the model to predict the socres for each input (pred)
              Then as per the model_type, convert the (real values) pred to binary predictions
              Finally, use binary predictions, and binary labels to obtain evaluaiton score
    """
    model.eval() # This enables the evaluation mode for the model

    eval_score = 0
    n=0
    z=0
    for data in loader:
        with torch.no_grad():
            #NOTE: pred = model(data[0])
            #NOTE: label = data[1]
            if model.args.model_type == "svm": 
                ##### TODO: Your code starts here######  
                pred=model(data[0])
                label=data[1]
                label=2*label-1
                label=torch.reshape(label,pred.shape)  
                scre=pred
                scre[scre>0]=1
                scre[scre<=0]=-1
                n+=data[0].shape[0]
                eval_score+=torch.sum(scre==label)
                #print(eval_score)
                #eval_score=eval_score.item()



               
                ######Your code ends here##########
            elif  model.args.model_type == "nll":
                ##### TODO: Your code starts here######  
                pred=model(data[0])
                label=data[1]
                n+=data[0].shape[0]
                #print(data[0].shape[0])
                pred[pred<=0.5]=0
                pred[pred>0.5]=1
                label=torch.reshape(label,(pred.shape[0],1))
                eval_score=eval_score+data[0].shape[0]-torch.sum(torch.logical_xor(pred,label))
                
               # print(label.shape)
                #pass       
                ######Your code ends here##########
            elif  model.args.model_type == "ranking":
                ##### TODO: Your code starts here######  
                #print(data)
                pred=model(data[0])
                label=data[1]
                n+=data[0].shape[0]
                if z==0:
                    pos=pred[label==1]
                    print(pos.shape)
                    #print(pos.shape)
                    neg=pred[label==0]
                    z+=1
                else:
                    #print(pos.shape,z)
                    pos=torch.cat((pos,pred[label==1]),0)
                    #print(pos.shape)
                    neg=torch.cat((neg,pred[label==0]),0)
                # pos=torch.reshape(pos,(1,pos.shape[0]))
                # arr=pos-neg
                # arr[arr<=0]=0
                # arr[arr>0]=1
                # eval_score+=torch.sum(arr)
                ######Your code ends here##########
            else: 
                raise NotImplementedError()

        #TODO (optional) If you want to add common code here ####
        ######Your code ends here##########
    if(model.args.model_type)=="ranking":
        #print(pos.shape)
        pos=torch.reshape(pos,(1,pos.shape[0]))
        arr=pos-neg
        arr[arr<=0]=0
        arr[arr>0]=1
        eval_score=torch.sum(arr)
    return eval_score,n


if __name__ == '__main__':
    set_seed(4)
      
    df=pd.read_csv('dataset.csv') ############ give path of the csv file and it will return a pandas dataframe
    ########### then you will have to split the dataframe into training and validation set where Xtrain denotes input samples and
    ########Ytrain denotes ouptut lables in training set and similar notation is used for validation set. 
    df = df.drop(df.columns[0], axis=1)
    x = df[df.columns[0:80]].to_numpy()
    y = df["Output"].to_numpy()

 
    Xtrain, Xval, Ytrain, Yval = train_test_split(x, y, test_size=0.3, random_state=42)


    Xtrain = torch.from_numpy(Xtrain)
    Ytrain = torch.from_numpy(Ytrain)

    Xval = torch.from_numpy(Xval)
    Yval = torch.from_numpy(Yval)

    Xtrain = Xtrain.float()
    Ytrain = Ytrain.long()
    Xval = Xval.float()
    Yval = Yval.long()
    args = {'batch_size': 128,
            'epochs': 100, 
            'opt': 'adam',
            'weight_decay': 5e-3,
            'lr': 0.01,
            'model_type': 'nll'} 

    args = objectview(args)

    input_dim = Xtrain.shape[1]
    args.model_type = 'ranking'  # Can change the model type here
    my_model = ModelClass(args, input_dim)

    val_accs, losses =  train(args, Xtrain, Ytrain, Xval, Yval, my_model)
    plot(val_accs, losses)
