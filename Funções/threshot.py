import numpy as np
import scipy.misc as spm
import matplotlib.pyplot as plt

path = "imagens/"

def binariza(input, threshold):
	imagem = spm.imread(input)
		
	shape = imagem.shape
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
	
	imagemBin = imagem
	imagemBin[imagem <= threshold] = 0
	imagemBin[imagem > threshold]	= 255
	return imagemBin


imagem = path + 'lena.jpg'
newimage = path + 'lena_bin.jpg'
spm.imsave( newimage, binariza(imagem, 128))
plt.imshow( spm.imread(newimage))
plt.show()

imagem = path + 'mandril.jpg'
newimage = path + 'mandril_b2in.png'
spm.imsave( newimage, binariza(imagem, 128))
plt.imshow( spm.imread(newimage))
plt.show()
	

