import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
import math

path = "imagens/"
output = "imagens/resposta_ex2.png"
violeta = [ 163, 73, 164]
preto = [ 0, 0, 0]

def bordaVioleta( input):
	imagemIN = scipy.misc.imread( input)
	shape = imagemIN.shape
	print shape
	data = []
	
	for i in range(0, shape[0]):
		row = []
		for j in range(0, shape[1]):
			bS = 0
			bE = 0
			bD = 0
			bI = 0
			ok = 0
			if np.array_equal( imagemIN[i][j], violeta):
				##print "achou"
				##row.append([0,0,0])
				if not bS:
					if not np.array_equal( imagemIN[i-1][j], violeta):
						ok = 1
					#if not bE:
					#	if imagemIN[i-1][j-1][1] != 0:
					#		ok = 1
					#if not bD:
					#	if imagemIN[i-1][j+1][1] != 0:
					#		ok = 1
				else:
					ok = 1

				if not bI:
					if not np.array_equal( imagemIN[i+1][j], violeta):
						ok = 1
					#if not bE:
					#	if np.array_equal( imagemIN[i+1][j-1], violeta):
					#		ok = 1
					#if not bD:
					#	if np.array_equal( imagemIN[i+1][j+1], violeta):
					#		ok = 1
				else:
					ok = 1

				if not bE:
					if not np.array_equal( imagemIN[i][j-1], violeta):
						ok = 1
				else:
					ok = 1

				if not bD:
					if not np.array_equal( imagemIN[i][j+1], violeta):
						ok = 1
				else:
					ok = 1

				if ok == 1:
					row.append([0,0,0])
				else:	
					row.append(imagemIN[i][j])
			else:
				##p = np.copy(imagemIN[i][j])
				##row.append(p)
				row.append(imagemIN[i][j])
			##	print "nop"
		data.append(row)
		
	scipy.misc.imsave(output,data)
	resultado = scipy.misc.imread(output)
	plt.imshow(resultado)
	plt.show()
				
				
imagem = path + "ex2_3.png"
entrada = scipy.misc.imread(imagem)
plt.imshow(entrada)
plt.show()
bordaVioleta( imagem)
	
