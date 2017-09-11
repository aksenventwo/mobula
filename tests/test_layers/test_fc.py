import mobula
import mobula.layers as L
import numpy as np

def test_fc():
    X = np.zeros((4,2,1,1))
    X[0,:,0,0] = [0.,0.]
    X[1,:,0,0] = [0.,1.]
    X[2,:,0,0] = [1.,0.]
    X[3,:,0,0] = [1.,1.]

    Y = np.array([8.,10.,12.,14.]).reshape((-1, 1))

    data, label = L.Data([X, Y], "Data")()
    fc1 = L.FC(data, "fc1", dim_out = 1)
    loss = L.MSE(fc1, "MSE", label = label)

    fc1.reshape()

    fc1.W = np.array([1.0, 3.0]).reshape(fc1.W.shape)
    fc1.b = np.array([0.0]).reshape(fc1.b.shape)


    net = mobula.Net()
    net.set_loss(loss)

    net.lr = 0.5
    for i in range(30):
        net.forward()
        net.backward()
        print ("Iter: %d, Cost: %f" % (i, loss.Y))

    # forward one more time, because of the change of weights last backward
    net.forward()
    target = np.dot(X.reshape((4, 2)), fc1.W.T) + fc1.b.T
    assert np.allclose(fc1.Y, target)

def test_fc2():
    X = np.random.random((4,2,1,1))
    Y1 = np.random.random((4,10))
    Y2 = np.random.random((4,10))

    [x,y1,y2] = L.Data([X,Y1,Y2])()
    fc1 = L.FC(x, dim_out = 10)
    fc2 = L.FC(x, dim_out = 10)
    loss1 = L.MSE(fc1, label = Y1)
    loss2 = L.MSE(fc2, label = Y2)

    net = mobula.Net()
    loss = L.L1Loss(loss1 + loss2)
    net.set_loss(loss)
    L1Loss = mobula.get_layer("L1Loss")
    Add = mobula.get_layer(L1Loss.model.name)

    net.lr = 0.5
    for i in range(30):
        net.forward()
        net.backward()
        print ("Iter: %d, Cost: %f" % (i, loss.Y))
    # check backward 
    # [TODO]
    # check forward
    t1 = np.dot(X.reshape((4,2)), fc1.W.T) + fc1.b.T
    t2 = np.dot(X.reshape((4,2)), fc2.W.T) + fc2.b.T
    # forward one more time, because of the change of weights last backward
    net.forward()
    assert np.allclose(fc1.Y, t1)
    assert np.allclose(fc2.Y, t2)
