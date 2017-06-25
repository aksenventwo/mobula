from testlib import *
import csv
from mobula import Net
import mobula.layers as L
import matplotlib.pyplot as plt
import scipy.io as sio
import os

filename = "./ex4data1.mat"
load_data = sio.loadmat(filename)

X = load_data['X']
T = load_data['y']
X.shape = (5000,1,20,20)
T[T == 10] = 0
Y = np.zeros((5000, 10))
for i in range(5000):
    Y[i, T[i]] = 1.0

'''
for i in range(0,5000,100):
    x = X[i,0,:,:]
    plt.imshow(x, "gray")
    plt.show()
'''

data = L.Data(X, "Data", batch_size = 128, label = Y)

#conv1 = L.Conv(data, "Conv1", dim_out=10, kernel = 5)

#conv2 = L.Conv(conv1, "Conv2", dim_out=20, kernel = 5)

fc1 = L.FC(data, "fc1", dim_out = 15)
sig1 = L.Sigmoid(fc1, "sig1")
#sig1 = L.Tanh(fc1, "sig1")
#sig1 = L.PReLU(fc1, "sig1")
fc2 = L.FC(sig1, "fc2", dim_out = 10)
#sig2 = L.Sigmoid(fc2, "sig2")
#loss = L.CrossEntropy(sig2, "Loss", label_data = data)
loss = L.SigmoidCrossEntropy(fc2, "Loss", label_data = data) 

net = Net()
net.setLoss(loss)

net.lr = 0.2
filename = "./mnist.net"
if os.path.exists(filename): 
    print ("Finetuning...")
    net.load(filename)
for i in range(50000):
    net.forward()
    net.backward()

    if i % 2000 == 0:
        print ("Iter: %d, Cost: %f" % (i, loss.loss))
        net.time()
        old_batch_size = data.batch_size
        data.batch_size = None
        net.reshape()
        net.forward()
        pre = np.argmax(fc2.Y,1)
        pre.resize(pre.size)
        right = np.argmax(data.label, 1).reshape(pre.size)
        bs = (pre == right) 
        b = np.sum(bs)
        acc = (b * 1.0 / len(pre))
        print (pre[0:5000:50])
        print ("Accuracy: %f" % (acc))
        if b == len(pre):
            net.save(filename)
            import sys
            sys.exit()
        data.batch_size = old_batch_size
        net.reshape()

net.save(filename)
