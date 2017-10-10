import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

def minima( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	outimg = []
	
	##Imagem Escala cinza
	if (len(size) == 2):
		for i in range(0, size[0]):
			row = []
			pixel = 255
			for j in range(0, size[1]):
				pixel = 255
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								pixel =min(pixel, inimg[i + i2][j + j2])
				row.append( [ pixel, pixel, pixel])
			outimg.append(row)
		
	##Imagem RGB
	if(len(size) == 3):
		for i in range(0, size[0]):
			row = []
			pixelR = 255
			pixelG = 255
			pixelB = 255
			for j in range(0, size[1]):
				#count = 0
				pixelR = 255
				pixelG = 255
				pixelB = 255
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								pixelR = min(pixelR, inimg[i + i2][j + j2][0])
								pixelG = min(pixelG, inimg[i + i2][j + j2][1])
								pixelB = min(pixelB, inimg[i + i2][j + j2][2])
				row.append( [ pixelR, pixelG, pixelB])
				#row.append(pixel)
			outimg.append(row)
	output = input + "_min" + ".png"
	scpm.imsave(pathnew + output, outimg)
	
#input = "shapes"
#ext = ".png"
#minima(input, ext)

#input = "python"
#ext = ".png"
#minima(input, ext)

input = "lena"
ext = ".jpg"
minima(input, ext)

