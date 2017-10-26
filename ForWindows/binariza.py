from PIL import Image as pimag
import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt

path = "imagens/"
pathnew = "imagens/aut/"

def binariza( input, ext, threshold):
	inimg = pimag.open(path + input + ext).convert('L')
	#inimg = scpm.imread(path + input + ext)
		
	#shape = inimg.shape
	shape = inimg.size
	outimg = []
	for i in range( 0, shape[0]):
		row = []
		for j in range(0, shape[1]):
			if inimg[i][j] <= threshold:
				row.append(0)
			else:
				row.append(255)
	#outimg = inimg.convert('L')
	#outimg[inimg <= threshold] = 0
	#outimg[inimg  > threshold] = 255
	
	output = input + "_binar" + ".png"
	
	#scpm.imsave( pathnew + output, outimg)
	outimg.save(pathnew + output)
	return output


input = "lena"
ext = ".png"
print binariza(input, ext, 100)