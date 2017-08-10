
import scipy.misc
import matplotlib.pyplot as plt
path = "imagens/"
image = scipy.misc.imread(path+'mandril.jpg')
print image.shape

image = scipy.misc.imread(path+'lena.jpg')
print image.shape

image = scipy.misc.imread(path+'python.png')
print image.shape

image = scipy.misc.imread(path+'mandril_b_w.jpg')
print image.shape
