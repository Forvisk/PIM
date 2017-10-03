import numpy as np
import scipy.misc as scpm
import math

path = "imagens/"
pathnew = "imagens/aut/"

def expoente( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	outimg = np.zeros(size)
	for i in range( size[0]):
		for j in range( size[1]):
			outimg[i][j] = max(math.exp(inimg[i][j]) - 256, 0)
	output = input + "_exp" + ".png"
	scpm.imsave(pathnew + output, outimg)

input = "lena"
ext = ".jpg"
expoente(input, ext)
