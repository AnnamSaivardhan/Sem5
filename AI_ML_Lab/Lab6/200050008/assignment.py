#!/usr/bin/env python
# coding: utf-8

# In[14]:
import pickle
from re import L
import torch
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
import random
import pandas as pd

def set_seed(seed:int=42):
    """Sets the seed for torch, numpy and random
    Args:
        seed (int): [description]
    """
    random.seed(seed)
    torch.manual_seed(seed)

class LogisticRegression:
    def __init__(self, xdim, ydim, args) -> None:
        """This is the model class for Logistic Regression

        Args:
            xdim - Dimension of input
            ydim - Number of output nodes. 1 for 2-class classification.
            args - dictionary containing hyper-parameters used in the model
        """
        self.xdim = xdim
        self.ydim = ydim
        self.args = args

        self.weights, self.bias = self.init_weights(xdim, ydim)
        assert self.weights.shape == (xdim, )


    def init_weights(self, xdim, ydim):
        """Initializes the weights of the logistic regression model.
        We have weights of shape (xdim,) and bias a scalar

        Returns:
            w, b
        """
        w, b = None, None

        ## TODO
        w = torch.zeros(xdim)
        b = torch.tensor(0)
        ## END TODO

        return w, b

    def forward(self, batch_x):
        """ Runs forward on a batch of features x and returns the predictions in yhat variable
        The code must be vectorized.

        Returns:
            The predictions in a tensor of shape  (batch_x.shape[0], )
        """
        assert (len(batch_x.size())==2)
        yhat = None

        ## TODO
        # fts=batch_x.shape[1]
        # nums=batch_x.shape[0]
        # wts = torch.reshape(self.weights,(fts,1))
        # bs = torch.reshape(self.bias,(1,1))
        # y = torch.matmul(batch_x,wts)+bs
        # y=self.args.temp*y
        # y=torch.sigmoid(y)
        # yhat = torch.reshape(y,(nums,))
        #print(type(self.bias))
        y = torch.matmul(batch_x,self.weights)+self.bias
        y=torch.sigmoid(self.args.temp*y)
        #yhat=y
        yhat=torch.reshape(y,(y.shape[0],))


        ## End TODO

        assert yhat.shape == (batch_x.shape[0], )
        return yhat

    def backward(self, batch_x, batch_y, batch_yhat):
        """Computes the gradients and updates the weights with the learning rate set to self.args.lr

            Returns the updated weights
        """
        assert (len(batch_x.size())==2)
        assert (len(batch_y.size())==1)
        assert (len(batch_yhat.size())==1)

        weights_new, bias_new = None, None

        ## TODO
        #old_wghts=torch.reshape(self.weights,(self.weights.shape[0],1))
        #old_bis=self.bias
        x=batch_x
        #x=x*self.args.temp
        #pred=torch.reshape(batch_yhat,(batch_yhat.shape[0],1))
        #label=torch.reshape(batch_y,(batch_y.shape[0],1))
        #mat1=(pred-label)
        x=torch.t(x)
        y=torch.reshape(batch_y-batch_yhat,(batch_y.shape[0],1))
        # Need to do reshape otherwise we may get an error
        #z=batch_y-batch_yhat
        mat2=torch.matmul(x,y)
        ww=torch.reshape(self.weights,(self.weights.shape[0],1))
        weights2=ww+self.args.temp*self.args.lr*(mat2)/batch_y.shape[0]
        weights_new=torch.reshape(weights2,(weights2.shape[0],))
        #print(weights_new[0])
        bis2=self.bias+self.args.temp*self.args.lr*(1/batch_y.shape[0])*torch.sum(batch_y-batch_yhat)
        bias_new=bis2
        ## End TODO

        self.weights = weights_new
        self.bias = bias_new
        return weights_new, bias_new

    def loss(self, y, y_hat):
        """Computes the loss and returns a scalar
        """
        assert (len(y.size())==1)
        assert (len(y_hat.size())==1)
        loss = 0

        ## TODO
        label=torch.reshape(y,(y.shape[0],1))
        pred=torch.reshape(y_hat,(y_hat.shape[0],1))
        #pred= (pred>torch.tensor(0.5)*torch.tensor(1))
        # pred[pred>0.5]=1
        # pred[pred<=0.5]=0
        l1=label
        l2=1-label
        p1 = torch.log(pred)
        p2= torch.log(1-pred)
        z1= torch.sum(torch.mul(l1,p1))
        z2=torch.sum(torch.mul(l2,p2))
        #print(z1,z2,len(y))
        loss = -1*(z1+z2)/len(y)
       # print(loss)

        ## End TODO

        assert len(loss.shape) == 0, "loss should be a torch scalar"
        return loss

    def score(self, yhat, y):
        """Computes the accuracy of the model
        """
        assert (len(y.size())==1)
        assert (len(yhat.size())==1)
        yhat = yhat > 0.5
        return torch.sum(yhat == y)/float(y.shape[0])


class LinearRegression:
    def __init__(self, xdim, args) -> None:
        """This is the model class for Linear Regression

        Args:
            xdim - Dimension of input
            args - dictionary containing hyper-parameters used in the model
        """
        self.xdim = xdim
        self.args = args

        self.weights, self.bias = self.init_weights(xdim)
        assert self.weights.shape == (xdim, )


    def init_weights(self, xdim):
        """Initializes the weights of the logistic regression model.
        We have weights of shape (xdim,) and bias a scalar

        Returns:
            w, b
        """
        w, b = None, None

        ## TODO
        w = torch.zeros(xdim)
        b = torch.tensor(0)
        ## END TODO

        return w, b

    def forward(self, batch_x):
        """ Runs forward on a batch of features x and returns the predictions in yhat variable
        The code must be vectorized.

        Returns:
            the predictions
        """
        assert (len(batch_x.size())==2)

        yhat = None

        ## TODO
        w_mat=torch.reshape(self.weights,(self.weights.shape[0],1))
        b_mat=torch.reshape(self.bias,(1,1))
        #w_mat=self.w
        #b_mat=self.b
        pred=torch.matmul(batch_x,w_mat)+b_mat
        yhat=torch.reshape(pred,(pred.shape[0],))
        ## End TODO

        assert yhat.shape == (batch_x.shape[0], )
        return yhat

    def backward(self, batch_x, batch_y, batch_yhat):
        """Computes the gradients and updates the weights with the self.args.lr

            Returns the updated weights
        """
        assert (len(batch_x.size())==2)
        assert (len(batch_y.size())==1)
        assert (len(batch_yhat.size())==1)

        weights_new, bias_new = None, None

        ## TODO
        d=self.weights.shape[0]
        n = batch_y.shape[0]
        #w_mat=self.weights
        w_mat=torch.reshape(self.weights,(d,1))
        #b_mat=torch.reshape(self.b,(1,1))
        y_mat=torch.reshape(batch_y,(n,1))
        yhat_mat=torch.reshape(batch_yhat,(n,1))
        w_mat= w_mat - 2*self.args.lr*(torch.matmul(torch.t(batch_x),yhat_mat-y_mat))/y_mat.shape[0]
        bias_new = self.bias - 2*self.args.lr*torch.mean(yhat_mat-y_mat)
        weights_new=torch.reshape(w_mat,(d,))
        ## End TODO

        self.weights = weights_new
        self.bias = bias_new
        return weights_new, bias_new

    def loss(self, y, y_hat):
        """Computes the loss and returns a scalar
        """
        assert (len(y.size())==1)
        assert (len(y_hat.size())==1)
        loss = 0

        ## TODO
        y_mat=torch.reshape(y,(y.shape[0],1))
        yhat_mat=torch.reshape(y_hat,(y_hat.shape[0],1))
        norm=torch.linalg.norm(yhat_mat-y_mat,ord=2)
        loss_ten=(y_hat-y)
        norm2=torch.linalg.norm(loss_ten,ord=2)
        loss2=torch.sum(torch.square(yhat_mat-y_mat))/y.shape[0]
        loss=norm*norm/y.shape[0]
        #print(loss_ten)
        #print(yhat_mat-y_mat)
        #print(norm-norm2)
        #assert norm==norm2 , "both norms should be same"
        #print(loss2-loss)
        #assert loss2 ==loss , "both losses ,ust be same"

        loss=loss2
        ## End TODO

        assert len(loss.shape) == 0, "loss should be a torch scalar"
        return loss

    def score(self, yhat, y):
        """Computes the negative opf mean squared error as score.

        Args:
            yhat (_type_): predictions
            y (_type_): _targets

        Returns:
            negative of mse
        """
        assert (len(y.size())==1)
        assert (len(yhat.size())==1)
        return - torch.mean(torch.square(y-yhat))



class EarlyStoppingModule(object):
  """
    Module to keep track of validation score across epochs
    Stop training if score not imroving exceeds patience
  """
  def __init__(self, args):
    """
      input : args
      patience: number of epochs to wait for improvement in validation score
      delta: minimum difference between two validation scores that can be considered as an improvement
      best_score: keeps track of best validation score observed till now (while training)
      num_bad_epochs: keeps track of number of training epochs in which no improvement has been observed
      should_stop_now: boolean flag deciding whether training should early stop at this epoch
    """
    self.args = args
    self.patience = args.patience
    self.delta = args.delta
    self.best_score = None
    self.num_bad_epochs = 0
    self.should_stop_now = False

  def save_best_model(self, model, epoch):
    fname =f"./{self.args.model_type}_bestValModel.pkl"
    pickle.dump(model, open(fname,"wb"))
    print(f"INFO:: Saving best validation model at epoch {epoch}")


  def load_best_model(self):
    fname =f"./{self.args.model_type}_bestValModel.pkl"
    try:
      model = pickle.load(open(fname,"rb"))
      print(f"INFO:: Loading best validation model from {fname}")
    except Exception as e:
      print(f"INFO:: Cannot load best model due to exception: {e}")

    return model

  def check(self, curr_score, model, epoch) :
    """Checks whether the current model has the best validation accuracy and decides to stop or proceed.
    If the current score on validation dataset is the best so far, it saves the model weights and bias.

    Args:
        curr_score (_type_): Score of the current model
        model (_type_): Trained Logistic/Linear model
        epoch (_type_): current epoch

    Returns:
        self.stop_now: Whether or not to stop

    Task1: Check for stoppage as per the early stopping criteria
    Task2: Save best model as required
    """

    ## TODO
    if self.best_score==None:
        self.best_score=curr_score
        self.save_best_model(model,epoch)
        #print("hi")
    else:
        if curr_score -self.best_score < self.delta:
            self.num_bad_epochs+=1
            if self.num_bad_epochs>self.patience:
                self.should_stop_now=True
        else:
            self.best_score=curr_score
            self.num_bad_epochs=0
            self.save_best_model(model,epoch)

    ## END TODO

    return self.should_stop_now




def minibatch(trn_X, trn_y, batch_size):
    """
    Function that yields the next minibatch for your model training
    IMPORTANT: DO NOT RETURN
    """
    #TODO
    random_permutation = torch.randperm(trn_X.shape[0])
    trn_X=trn_X[random_permutation]
    trn_y=trn_y[random_permutation]
    i=0
    while(i<trn_X.shape[0]):
        yield (trn_X[i:i+batch_size],trn_y[i:i+batch_size])
        i+=batch_size
    #TODO
    pass

def split_data(X:torch.Tensor, y:torch.Tensor, split_per=0.6):
    """Splits the dataset into train and test.
    """
    shuffled_idxs = torch.randperm(X.shape[0])
    trn_idxs = shuffled_idxs[0:int(split_per * X.shape[0])]
    tst_idxs = shuffled_idxs[int(split_per * X.shape[0]):]
    return X[trn_idxs], y[trn_idxs], X[tst_idxs], y[tst_idxs]



def train(args, X_tr, y_tr, X_val, y_val, model):
    es = EarlyStoppingModule(args)
    losses = []
    val_acc = []
    epoch_num = 0
    while (epoch_num<=args.max_epochs):
        for idx, (batch_x, batch_y) in enumerate(minibatch(X_tr, y_tr, args.batch_size)):
            if idx == 0:
                assert batch_x.shape[0] == args.batch_size
            batch_yhat = model.forward(batch_x)
            losses.append(model.loss(batch_y, batch_yhat).item())
            updated_wts = model.backward(batch_x, batch_y, batch_yhat)

        val_score = model.score(model.forward(torch.Tensor(X_val)), torch.Tensor(y_val))
        print(f"INFO:: Validation score at epoch {epoch_num}: {val_score}")
        val_acc.append(val_score)
        if es.check(val_score,model,epoch_num):
          break
        epoch_num +=1
    return losses, val_acc


class objectview(object):
    def __init__(self, d):
        self.__dict__ = d


if __name__ == '__main__':

    set_seed(0)

    """
    Logistic Regression
    """
    print("LOGISTIC REGRESSION")
    args = {'batch_size': 16,
        'max_epochs': 500,
        'lr': 0.01,
        'patience' : 10,
        'delta' : 1e-4,
        'temp' : 8,
        'model_type': 'logistic-moons'}

    args = objectview(args)

    """This is on synthetic 2 moons dataset"""
    print("MODEL:: Logistic Regression on 2-moons")
    datasets = make_moons(n_samples=1000, noise=0.05, random_state=0)
    X, y = datasets
    X, y = torch.Tensor(X), torch.Tensor(y)

    X_train, y_train, X_val, y_val = split_data(X, y,)

    LogR = LogisticRegression(X_train.shape[1], 1, args)
    losses, val_acc = train(args, X_train, y_train,X_val, y_val, model=LogR)

    es = EarlyStoppingModule(args)
    best_model = es.load_best_model()

    print(LogR.score(best_model.forward(torch.Tensor(X_val)), torch.Tensor(y_val)))

    """This is on Real-world titanic dataset. We have done all the data pre-processing."""
    print("MODEL:: Logistic Regression on Titanic")
    set_seed(0)

    args = {'batch_size': 16,
        'max_epochs': 500,
        'lr': 0.1,
        'patience' : 10,
        'delta' : 1e-4,
        'temp' : 8,
        'model_type': 'logistic-titanic'}

    args = objectview(args)

    with open("titanic_trn.pkl", "rb") as file:
        X, y = pickle.load(file)
    X, y = torch.Tensor(X), torch.Tensor(y)

    X_train, y_train, X_val, y_val = split_data(X, y,)

    LogR = LogisticRegression(X_train.shape[1], 1, args)
    losses, val_acc = train(args, X_train, y_train,X_val, y_val, model=LogR)

    es = EarlyStoppingModule(args)
    best_model = es.load_best_model()

    print(LogR.score(best_model.forward(torch.Tensor(X_val)), torch.Tensor(y_val)))


    # """
    # Linear Regression
    # """
    set_seed(0)
    print("MODEL:: LINEAR REGRESSION")
    args = {'batch_size': 8,
        'max_epochs': 500,
        'lr': 0.01,
        'patience' : 10,
        'delta' : 1e-4,
        'model_type': 'linear'}

    args = objectview(args)

    data = pd.read_csv('dataset.csv', index_col=0)
    X = (data.iloc[:,:-1].to_numpy())
    y = (data.iloc[:,-1].to_numpy())
    X, y = torch.Tensor(X), torch.Tensor(y)

    X_train, y_train, X_val, y_val = split_data(X, y,)

    LinR = LinearRegression(X_train.shape[1], args)
    losses, val_acc = train(args, X_train, y_train,X_val, y_val,  model=LinR)

    es = EarlyStoppingModule(args)
    best_model = es.load_best_model()

    print(LinR.score(best_model.forward(torch.Tensor(X_val)), torch.Tensor(y_val)))
