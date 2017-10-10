import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

def mascara3x3( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	outimg = []
	
	##Imagem Escala cinza
	if (len(size) == 2):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				vetor = []
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								vetor.append(inimg[i + i2][j + j2])
				pixel = moda( vetor)
				row.append( [ pixel, pixel, pixel])
			outimg.append(row)
		
	##Imagem RGB
	if(len(size) == 3):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				vetorR = []
				vetorG = []
				vetorB = []
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								vetorR.append( inimg[i + i2][j + j2][0])
								vetorG.append( inimg[i + i2][j + j2][0])
								vetorB.append( inimg[i + i2][j + j2][0])
				pixelR = moda( vetorR)
				pixelG = moda( vetorG)
				pixelB = moda( vetorB)
				row.append( [ pixelR, pixelG, pixelB])
				#row.append(pixel)
			outimg.append(row)
	output = input + "_moda" + ".png"
	scpm.imsave(pathnew + output, outimg)


## retirado de https://gist.github.com/juanpabloaj/2832821
def moda(vetor):
	# moda
	repeticiones = 0
	for i in vetor:
		apariciones = vetor.count(i)
		if apariciones > repeticiones:
		    repeticiones = apariciones
	modas = []
	for i in vetor:
		apariciones = vetor.count(i)
		if apariciones == repeticiones and i not in modas:
			modas.append(i)
	#print "moda:", modas
	modas.sort()
	return modas[len(modas)/2]
	#return max(modas)

#input = "shapes"
#ext = ".png"
#mascara3x3(input, ext)

input = "python"
ext = ".png"
mascara3x3(input, ext)

input = "lena"
ext = ".jpg"
mascara3x3(input, ext)

