from testlib import *
import mobula.layers as L
from mobula import Net

X = np.zeros((2,2,5,5))
X[0,0,2,2] = 1.0
X[0,1,2,2] = 1.0
X[1,0,2,2] = 2.0

Y = np.zeros((2,1,3,3))
Y[0,0,2,2] = 10.0
Y[0,0,1,2] = 12.0
Y[1,0,0,0] = 23.0
Y[1,0,2,2] = 23.0
Y[1,0,1,1] = 33.0
Y[1,0,1,2] = 13.0

data = L.Data(X, "data", label = Y) 
conv = L.Conv(data, "Conv", pad = 0, kernel = 3, dim_out = 1)
conv.X = X
conv.reshape()
conv.W = np.zeros(conv.W.shape) 
conv.W = np.arange(conv.W.size).reshape(conv.W.shape)
conv.b = np.zeros(conv.b.shape)

conv.forward()
print (X)
print (conv.W)
print (conv.Y.shape)

data = L.Data(X, "data", label = Y) 
conv = L.Conv(data, "Conv", pad = 0, kernel = 3, dim_out = 1)
loss = L.MSE(conv, "Loss", label_data = data) 
net = Net()
net.setLoss(loss)


net.reshape()
net.reshape2()
net.lr = 0.01
for i in range(500000):
    net.forward()
    net.backward()
    print (loss.loss)
    if loss.loss < 0.0001:
        print ("end", i)
        break
print (Y, conv.Y)

'''
X = np.zeros((2,3,5,5))
X[0,0,:,:] = np.arange(25).reshape((5,5))
X[0,1,:,:] = np.arange(25, 50).reshape((5,5))
X[1,0,:,:] = np.arange(125, 150).reshape((5,5))

data = Data(X, "data") 
conv = Conv(data, "Conv", pad = 0, kernel_h = 2, kernel_w = 3, dim_out = 4)
data.reshape()
data.forward()
conv.reshape()
conv.reshape2()
conv.forward()
print "X", conv.X.shape
print conv.X_col.shape
conv.dY = conv.Y
print conv.W.T.shape, conv.dY.shape
conv.backward()
#print X
print "==="
#print conv.X_col
print conv.X_col.shape
print conv.dX
print X
print conv.X_col.shape
print conv.W.shape
#print conv.Y.shape
'''
