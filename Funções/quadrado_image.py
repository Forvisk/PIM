import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

def quadrado( input, ext):
	original = scpm.imread(path + input + ext)
	size = original.shape
	outimg = np.zeros(size)
	for i in range( size[0]):
		for j in range( size[1]):
			sqrt = original[i][j] ** 2
			outimg[i][j] = max(255, sqrt)
	output = input + "_quad" + ".png"
	scpm.imsave(pathnew + output, outimg)

input = "lena"
ext = ".jpg"
quadrado(input, ext)
