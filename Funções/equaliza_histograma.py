# Pf(fn) = nPixelNivel / nPixelTotal = probabilidade do pixel daquela cor
# T(fk) = soma 0->k (Pf(fk))
# gk = round( T(fk) * maxNvlCinza )

import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt

path = "imagens/"
pathnew = "imagens/aut/"

def equal_histograma( input, extencao):
	imgin = scpm.imread( path + input + extencao)
	
	histg, interv = np.histogram( imgin, bins=np.arange(0,256))
	
	## Histograma da imagem
	## determina o valor do centro dos intervalos
	#center = ( interv[:-1] + interv[1:])/2
	##exibe histograma
	#plt.bar(center, histg, align='center')
	#plt.show()
	
	
	size = imgin.shape
	
	imgsize = size[0] * size[1] * 1.0
	prob = histg/imgsize
	
	FDP = np.zeros(256)
	#print prob
	# T(fk) = soma 0->k (Pf(fk))
	for i in range(0,256):
		for j in range(0, i):
			FDP[i] = FDP[i] + prob[j]
	
	for i in range(0, 256):
		FDP[i] = np.round( FDP[i] * 256)
	
	imgout = np.zeros( size)
	for i in range( size[0]):
		for j in range( size[1]):
			imgout[i][j] = int( FDP[ imgin[i][j]])
		
	output = input + "_equhistg" + ".png"
	scpm.imsave( pathnew+output, imgout)
	
	
	## Histograma da nova imagem
	#histg, interv = np.histogram( imgout, bins=np.arange(0,256))
	## determina o valor do centro dos intervalos
	#center = ( interv[:-1] + interv[1:])/2
	##exibe histograma
	#plt.bar(center, histg, align='center')
	#plt.show()
	
	return output


input = "lena"
ext = ".jpg"
equal_histograma( input, ext)

input = "car"
ext = ".png"
equal_histograma( input, ext)

input = "foto-escura"
ext = ".jpg"
equal_histograma( input, ext)
