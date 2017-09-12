import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
import math

path = "imagens/"
output = "imagens/resposta_ex3.png"
#violeta = [ 163, 73, 164]
preto = [ 0, 0, 0]
azul = [ 0, 0, 255]


def distanciaPixel( input):
	imagemIN = scipy.misc.imread( input)
	shape = imagemIN.shape
	print shape
	for i in range(0, shape[0]):
		for j in range(0, shape[1]):
			if np.array_equal( imagemIN[i][j], azul):
				#print "achou " + str(i) + "," + str(j)
				i2 = i
				j2 = j+1
				while i2 < shape[0]:
				#for i2 = i in range( shape[0]):
					while j2 < shape[1]:
					#for j2 = j+1 in range( shape[1]):
						if np.array_equal( imagemIN[i2][j2], azul):
							#print "achou2 " + str(i) + "," + str(j)
							distanciaD4([i, j],[i2, j2])
						j2 += 1
					j2 = 0
					i2 += 1


def distanciaD4( ponto1, ponto2):
	if( len(ponto1) == len(ponto2)):
		dime = len(ponto1)
		ins = 0
		res = 0
		for i in range(0, dime):
			ins = max(ponto1[i] - ponto2[i], -(ponto1[i] - ponto2[i]))
			res += ins
		print res

imagem = path + "ex2_3.png"
entrada = scipy.misc.imread(imagem)
plt.imshow(entrada)
plt.show()
distanciaPixel( imagem)
