# -*- coding: utf-8 -*

import numpy as np
from chainer import Variable, optimizers, serializers
from chainer import Chain
import chainer.functions as F
import chainer.links as L
from sklearn.datasets import fetch_openml

class MyMLP(Chain):
    def __init__(self, n_in=784, n_units=100, n_out=10):
        super(MyMLP, self).__init__(
            l1=L.Linear(n_in, n_units),
            l2=L.Linear(n_units, n_units),
            l3=L.Linear(n_units, n_out),
        )
    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y

#プログラムが開始したことを示す(MNISTのダウンロードに時間を要するため).
print('Start')

mnist_X, mnist_y = fetch_openml('mnist_784', version=1, data_home=".", return_X_y=True)

x_all = mnist_X.astype(np.float32) / 255
y_all = mnist_y.astype(np.int32)

model = MyMLP()
optimizer = optimizers.SGD()
optimizer.setup(model)

BATCHSIZE = 100
DATASIZE = 70000

for epoch in range(20):
    print('epoch %d' % epoch)
    indexes = np.random.permutation(DATASIZE)
    for i in range(0, DATASIZE, BATCHSIZE):
        x = Variable(x_all[indexes[i : i + BATCHSIZE]])
        t = Variable(y_all[indexes[i : i + BATCHSIZE]])

        model.zerograds()

        y = model(x)

        loss = F.softmax_cross_entropy(y, t)

        loss.backward()

        optimizer.update()

serializers.save_npz("mymodel.npz", model)

#プログラムが終了したことを示す.
print('Finish')