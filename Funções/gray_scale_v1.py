import numpy as np
import scipy.misc as spm
import matplotlib.pyplot as plt

path = "imagens/"

def gray_scale(input):
	imagem = spm.imread(input)
	threshold = 0
	shape = imagem.shape
	imagemBin = []
	for l in range(shape[0]):
		row = []
		for c in range( shape[1]):
			if( len(shape) == 2):
				if( imagem[l][c] <= threshold):
					row.append( [0,0,0])
				else:
					row.append( [255,255,255])
			else:
				media = imagem[l][c][0] + imagem[l][c][1] + imagem[l][c][2]
				#print imagem[l][c] 
				#print media
				media = media / 3
				#print media
				row.append( [media, media, media])
		imagemBin.append(row)
		
	return imagemBin


#imagem = path + 'lena.jpg'
#newimage = path + 'lena_bin.png'
#spm.imsave( newimage, binariza(imagem, 128))
#plt.imshow( spm.imread(newimage))
#plt.show()

imagem = path + 'mandril.jpg'
newimage = path + 'mandril_grayv1.png'
spm.imsave( newimage, gray_scale(imagem))
plt.imshow( spm.imread(newimage))
plt.show()

imagem = path + 'ex2_3.png'
newimage = path + 'ex2_3_grayv1.png'
spm.imsave( newimage, gray_scale(imagem))
plt.imshow( spm.imread(newimage))
plt.show()
	

