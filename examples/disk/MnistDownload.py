import os

from twister2deepnet.deepnet.datasets.MNIST import MNIST

__data_dir = '/tmp/twister2deepnet/mnist'

mnist_train = MNIST(source_dir=os.path.join(__data_dir, 'train'), train=True, transform=None)
mnist_train.download()

mnist_test = MNIST(source_dir=os.path.join(__data_dir, 'test'), train=False, transform=None)
mnist_test.download()