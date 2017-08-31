import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

path  = "imagens/"

def mult( input, val):
	im = scipy.misc.imread(input)
	imArr = np.array( im * val, dtype=np.uint8)
	plt.imshow(imArr)
	plt.show()


mult( path+"lena.jpg", 0.15)
#image1 = path + "mandril_b_w.jpg"
#image2 = path + "lena.jpg"
#im1 = scipy.misc.imread(image1)
#im2 = scipy.misc.imread(image2)
#print im1
#print im2
#imArr = np.add( im1, im2)
#plt.imshow(imArr)
#plt.show()
