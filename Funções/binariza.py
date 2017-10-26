import numpy as np
import scipy.misc as spm
import matplotlib.pyplot as plt

path = "imagens/"
pathnew = "imagens/aut/"

def binariza( input, ext, threshold):
	inimg = spm.imread(path + input + ext)
		
	shape = inimg.shape
	#imagemBin = []
	#for l in range(shape[0]):
	#	row = []
	#	for c in range( shape[1]):
	#		if( len(shape) == 2):
	#			if( imagem[l][c] <= threshold):
	#				row.append( [0,0,0])
	#			else:
	#				row.append( [255,255,255])
	#		else:
	#			media = imagem[l][c][0] + imagem[l][c][1] + imagem[l][c][2]
	#			#print imagem[l][c] 
	#			#print media
	#			media = media / 3
	#			#print media
	#			if( media <= threshold):
	#				row.append( [0,0,0])
	#			else:
	#				row.append( [255,255,255])
	#	imagemBin.append(row)
	
	outimg = inimg
	outimg[inimg <= threshold] = 0
	outimg[inimg  > threshold] = 255
	
	output = input + "_binar" + ".png"
	
	spm.imsave( pathnew + output, outimg)
	return output


input = "lena"
ext = ".png"
print binariza(input, ext, 100)
	

