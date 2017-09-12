import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
import math

path = "imagens/"
output = "imagens/resposta_ex4.png"
#violeta = [ 163, 73, 164]
preto = [ 0, 0, 0]
azul = [ 0, 0, 255]

def removeRuido( input):
	imagemIN = scipy.misc.imread( input)
	shape = imagemIN.shape
	print shape
	##pixel = np.copy(imagemIN[0][0])
	for i in range(0, shape[0]):
		for j in range( 0, shape[1]):
			pixelVizinhanca = []
			pixelVizinhanca.append(imagemIN[i][j])
			count = 0
			if i-1 < 0:
				if np.array_equal(imagemIN[i][j], imagemIN[i-1][j]):
					count += 1
				pixelVizinhanca.append(imagemIN[i-1][j])
			if i+1 < shape[0]:
				if np.array_equal(imagemIN[i][j], imagemIN[i+1][j]):
					count += 1
				pixelVizinhanca.append(imagemIN[i+1][j])
			if j-1 < 0:
				if np.array_equal(imagemIN[i][j], imagemIN[i][j-1]):
					count += 1
				pixelVizinhanca.append(imagemIN[i][j-1])
			if j+1 < shape[1]:
				if np.array_equal(imagemIN[i][j], imagemIN[i][j+1]):
					count += 1
				pixelVizinhanca.append(imagemIN[i][j+1])
			if count == 0:
				##print "Ruido em ("+str(i)+","+str(j)+")"
				if i-1 < 0:
					imagemIN[i][j] = np.copy( imagemIN[i-1][j])
				else:
					if i+1 < shape[0]:
						imagemIN[i][j] = np.copy( imagemIN[i+1][j])
					else:
						if j-1 < 0:
							imagemIN[i][j] = np.copy( imagemIN[i][j-1])
			
	scipy.misc.imsave(output,imagemIN)
	resultado = scipy.misc.imread(output)
	plt.imshow(resultado)
	plt.show()
			
				
				
			
	

imagem = path + "ex4.png"
entrada = scipy.misc.imread(imagem)
plt.imshow(entrada)
plt.show()
removeRuido( imagem)
