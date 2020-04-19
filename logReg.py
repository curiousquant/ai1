import numpy as np
from sklearn import datasets

class logReg():
    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.theta = np.zeros((self.X.shape[1],1))

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def cost(self):
        log_h = np.log(self.sigmoid(np.dot(self.getX(),self.getTheta())))
        print(log_h.shape)
        log_1_h = np.log(1-self.sigmoid(np.dot(self.getX() , self.getTheta())))

        return -(log_h.shape[0]*(self.getY()*log_h +(1-self.getY()*log_1_h))).mean()

    def gradientDescent(self):
        alpha = .01
        zbin = np.arange(0, 10000)
        for i in range(0,len(zbin)):
            # Theta_n = Theta_n-1 - alpha/m*X'T*[g(X*theta)-y]

            form1 = self.getX().T
            form2 = self.sigmoid(np.dot(self.getX(),self.getTheta()))-self.getY()
            update = self.getTheta()-alpha/self.getX().shape[0]*np.dot(form1,form2)
            #print(update)
            print(self.getTheta())
            self.setTheta(update)

    def getX(self):
        return self.X
    def getY(self):
        return self.y
    def getTheta(self):
        return self.theta
    def setTheta(self,theta):
        self.theta = theta

if __name__ == '__main__':
    iris = datasets.load_iris()
    X = iris.data[:,:2]
    y = (iris.target !=0)*1
    y=y.reshape(len(y),1)
    model = logReg(X,y)
    model.gradientDescent()

    print(np.mean([2,2]))