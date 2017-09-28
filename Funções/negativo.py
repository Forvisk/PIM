import numpy as np
import scipy.misc as spm
import matplotlib.pyplot as plt

path = "imagens/"

def negativo(input):
	imagem = spm.imread(input)
		
	shape = imagem.shape
	#histogramas, intervalos = np.histogram(imagem, bins=np.arange(0,256))
	minPB = minR = minG = minB = 0
	
	#
	#imagemRet = []
	#for l in range(shape[0]):
	#	row = []
	#	for c in range( shape[1]):
	#		#imagem[l][c]
	#		#row.append( [,,,])
	#		if( len(shape) == 2):
	#			color = 255 - imagem[l][c] + minPB
	#			row.append( [ color, color, color])
	#		else:
	#			r = 255 - imagem[l][c][0] + minR
	#			g = 255 - imagem[l][c][1] + minG
	#			b = 255 - imagem[l][c][2] + minB
	#			row.append( [r, g, b])
	#	imagemRet.append(row)
	
	imagemRet = 255 - imagem	
	return imagemRet


imagem = path + 'lena.jpg'
newimage = path + 'lena_neg.jpg'
spm.imsave( newimage, negativo(imagem))
plt.imshow( spm.imread(newimage))
plt.show()

imagem = path + 'mandril.jpg'
newimage = path + 'mandril_neg.png'
spm.imsave( newimage, negativo(imagem))
plt.imshow( spm.imread(newimage))
plt.show()

imagem = path + 'ex2_3.png'
newimage = path + 'ex2_3_neg.png'
spm.imsave( newimage, negativo(imagem))
plt.imshow( spm.imread(newimage))
plt.show()
	
