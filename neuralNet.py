import numpy as np


class neuralNet():
    
    def __init__(self,X,theta):
        self.X = X
        self.theta = theta
        self.N = len(theta)

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def actFunc(self,theta,X):
        A = self.sigmoid(np.dot(theta,X.T)).T
        print(A)
        return A

    def analysis(self):        
        A = self.getX()

        for i in range(self.getN()):
            A = self.appendOnes(A)
            A = self.actFunc(self.getTheta()[i], A)
            
        return A

    def appendOnes(self,X):
        self.X = np.hstack((X,np.ones((X.shape[0],1))))
        return self.X

    def getX(self):
        return self.X
    def getTheta(self):
        return self.theta
    def getN(self):
        return self.N



if __name__ == '__main__':
    
    X = np.array([[1,2,3,4],[4,5,6,4],[7,8,9,4],[7,8,9,4],[7,8,9,4],[7,8,9,4]])
    theta = [np.ones((X.shape[1],X.shape[1]+1)),np.ones((X.shape[1],X.shape[1]+1)),
            np.ones((1,X.shape[1]+1))]

    net = neuralNet(X=X,theta=theta)
    net.analysis()
