from .LossLayer import *

class SigmoidCrossEntropy(LossLayer):
    def __init__(self, model, *args, **kwargs):
        LossLayer.__init__(self, model, *args, **kwargs)
    def __str__(self):
        return "It is a CrossEntropy Layer"
    def reshape(self):
        self.Y = 0.0
    def forward(self):
        pass
    def reshape2(self):
        self.dX = np.zeros(self.X.shape) 
    def backward(self):
        self.dX = 1.0 / (1 + np.exp(-self.X)) - self.label
    @property
    def loss(self):
        e = np.clip(1.0 / (1 + np.exp(-self.X)), 1e-16, 1.0 - 1e-16)
        self.Y = np.mean(- np.multiply(self.label, np.log(e)) - \
               np.multiply(1.0 - self.label, np.log(1.0 - e)))
        return self.Y
