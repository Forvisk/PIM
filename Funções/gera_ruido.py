import numpy as np
import scipy.misc as scpm

path = "imagens/"
#pathnew = "imagens/aut/"

def ruido( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	outimg = []
	
	##Imagem Escala cinza
	if (len(size) == 2):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				pixel = inimg[i][j]
				if random(15) < 3:
					if random(2) == 1:
						pixel = 255
					else:
						pixel = 0
				row.append( [ pixel, pixel, pixel])
			outimg.append(row)
		
	##Imagem RGB
	if(len(size) == 3):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				pixelR = inimg[i][j][0]
				pixelG = inimg[i][j][1]
				pixelB = inimg[i][j][2]
				if random(15) < 3:
					if random(2) == 1:
						pixelR = 255
						pixelG = 255
						pixelB = 255
					else:
						pixelR = 0
						pixelG = 0
						pixelB = 0
				row.append( [ pixelR, pixelG, pixelB])
				#row.append(pixel)
			outimg.append(row)
	output = input + "_ruido" + ".png"
	scpm.imsave(path + output, outimg)


#input = "shapes"
#ext = ".png"
#ruido(input, ext)

input = "python"
ext = ".png"
ruido(input, ext)

input = "lena"
ext = ".jpg"
ruido(input, ext)

