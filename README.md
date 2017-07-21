# Mobula

## What is it?
*Mobula* is a light deep learning framework on python.

It's **an efficent Python-DNN Implementation used numpy mainly**, and it's aimed to learn **how a neural network runs** :-)

## What can I do with it?
1. Digital Recognition

## Layers
*Mobula* has implemented these layers using numpy. It's efficient relatively on Python Implementation.
#### Layers with Learning
- FC
- Convolution
#### Layers without Learning
- Pooling
- Dropout
#### Activation Layer
- Sigmoid
- ReLU
- PReLU
- SELU
- Tanh
- Softmax
#### Cost Layer
- Mean Square Error
- CrossEntropy
- SigmoidCrossEntropy
- SoftmaxWithLoss 

## Benefit

- Easy to Configure

    Mobula needs less dependence. It is implemented by numpy mainly, so you can setup it easily.

## Quick Start

##### Notice: Recommend using Python in Anaconda, because of **Calculating Optimization numpy-mkl** in Anaconda.

The detail is in [Performance Analysis](docs/performance.md).

#### Digital Recognition
Let's construct a **Convolution Nerual Network** on *Mobula*! 

We use **LeNet-5** to solve *Digital Recognition* problem on Kaggle.

The score is above 0.99 in training for several minutes.

Firstly, you need to download the dataset train.csv and test.csv into **test/** folder. 

Secondly, constructing the **LeNet-5**.

The core code is that:

```python
from mobula import Net
import mobula.layers as L

data = L.Data(X, "Data", batch_size = 100, label = labels)

conv1 = L.Conv(data, "Conv1", dim_out = 20, kernel = 5)
pool1 = L.Pool(conv1, "pool1", pool = L.Pool.MAX, kernel = 2, stride = 2)
conv2 = L.Conv(pool1, "Conv2", dim_out = 50, kernel = 5)
pool2 = L.Pool(conv2, "pool2", pool = L.Pool.MAX, kernel = 2, stride = 2)
fc3   = L.FC(pool2, "fc3", dim_out = 500)
relu3 = L.ReLU(fc3, "relu3")
pred  = L.FC(relu3, "pred", dim_out = 10)
loss = L.SoftmaxWithLoss(pred, "loss", label_data = data)

net = Net()
net.setLoss(loss)

net.lr = 0.2
```

The training and predicting codes are in **test/** folders, namely **digit_recognizerKaggle2.py** and **digit_recognizerKaggle2predict.py**.

For training the network, 
```bash
python digit_recognizerKaggle2.py
```

When the number of iterations is 2000, the accuracy on training set is 0.99.

For predicting test.csv,  
```bash
python digit_recognizerKaggle2predict.py
```

At Line 50 in *digit_recognizerKaggle2predict.py*, `iter_num` is the iterations of the model which is used to predict test set. 

Enjoy it! :-)
