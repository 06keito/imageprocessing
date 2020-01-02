# -*- coding: utf-8 -*

import cv2
import numpy as np
from chainer import Chain, serializers
import chainer.functions  as F
import chainer.links as L

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

def preprocessing(img):
    img = img[190:290,270:370]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (28, 28))
    res, img = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY_INV)
    img = img.astype(np.float32) / 255
    img = np.array(img).reshape(1, 784)
    return img

def main():
    model = MyMLP()
    serializers.load_npz('mymodel.npz', model)

    capture = cv2.VideoCapture(0)
    if capture.isOpened() is False:
            raise("IO Error")

    while True:
        ret, image = capture.read()
        if ret == False:
            continue

        cv2.rectangle(image, (269,189), (371,291), (0,0,255), 1)
        cv2.imshow("Capture", image)
        k = cv2.waitKey(10)

        if k == ord('e'):
            img = preprocessing(image)
            num = model(img)
            print(num.data)
            print(np.argmax(num.data))

        if  k == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()