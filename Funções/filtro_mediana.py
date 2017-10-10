import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

def mediana( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	outimg = []
	
	##Imagem Escala cinza
	if (len(size) == 2):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				#nelem = 0
				vetor = []
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								vetor.append(inimg[i + i2][j + j2])
								#nelem += 1
				#vetor.sort()
				#pixel = vetor[ nelem/2 +1]
				pixel = mediana( vetor)
				row.append( [ pixel, pixel, pixel])
			outimg.append(row)
		
	##Imagem RGB
	if(len(size) == 3):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				#nelem = 0
				vetorR = []
				vetorG = []
				vetorB = []
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								vetorR.append( inimg[i + i2][j + j2][0])
								vetorG.append( inimg[i + i2][j + j2][1])
								vetorB.append( inimg[i + i2][j + j2][2])
								#nelem += 1
				#vetorR.sort()
				#vetorG.sort()
				#vetorB.sort()
				#pixelR = vetorR[ nelem/2 +1]
				#pixelG = vetorG[ nelem/2 +1]
				#pixelB = vetorB[ nelem/2 +1]
				pixelR = mediana( vetorR)
				pixelG = mediana( vetorG)
				pixelB = mediana( vetorB)
				row.append( [ pixelR, pixelG, pixelB])
				#row.append(pixel)
			outimg.append(row)
	output = input + "_mediana" + ".png"
	scpm.imsave(pathnew + output, outimg)

def mediana( vetor):
	vetor.sort()
	return vetor[len(vetor)/2+1]
	
#input = "shapes"
#ext = ".png"
#mediana(input, ext)

#input = "python"
#ext = ".png"
#mediana(input, ext)

input = "lena"
ext = ".jpg"
mediana(input, ext)

