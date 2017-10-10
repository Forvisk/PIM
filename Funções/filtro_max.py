import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

def mascara3x3( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	#print mascara
	outimg = []
	
	##Imagem Escala cinza
	if (len(size) == 2):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				pixel = 0
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								pixel = max(pixel, inimg[i + i2][j + j2])
				row.append( [ pixel, pixel, pixel])
			outimg.append(row)
		
	##Imagem RGB
	if(len(size) == 3):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				#count = 0
				pixelR = 0
				pixelG = 0
				pixelB = 0
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								pixelR = max(pixelR, inimg[i + i2][j + j2][0])
								pixelG = max(pixelG, inimg[i + i2][j + j2][0])
								pixelB = max(pixelB, inimg[i + i2][j + j2][0])
				row.append( [ pixelR, pixelG, pixelB])
				#row.append(pixel)
			outimg.append(row)
	output = input + "_max" + ".png"
	scpm.imsave(pathnew + output, outimg)
	
#input = "shapes"
#ext = ".png"
#mascara3x3(input, ext)

#input = "python"
#ext = ".png"
#mascara3x3(input, ext)

input = "lena"
ext = ".jpg"
mascara3x3(input, ext)

