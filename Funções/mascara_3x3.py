import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

def mascara3x3( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	#mascara = [	[1,1,1],
	#			[1,1,1],
	#			[1,1,1]
	#			]
	mascara = [	[5,5,5],
				[-5,-5,-5],
				[-15,-15,-15]
				]
	#print mascara
	outimg = []
	
	##Imagem Escala cinza
	if (len(size) == 2):
		for i in range(0, size[0]):
			row = []
			pixel = 0
			for j in range(0, size[1]):
				count = 0
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								pixel += inimg[i + i2][j + j2]*mascara[1+i2][1+j2]
								count += abs(mascara[1+i2][1+j2])
				if (count == 0):
					count = 1
				pixel = pixel / count
				#print count
				row.append( [ pixel, pixel, pixel])
			outimg.append(row)
			
	##Imagem RGB
	if(len(size) == 3):
		for i in range(0, size[0]):
			row = []
			pixelR = 0
			pixelG = 0
			pixelB = 0
			for j in range(0, size[1]):
				count = 0
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							#print [i, j, i2, j2]
							if ( j+j2 in range(0, size[1])):
								pixelR += inimg[i + i2][j + j2][0]*mascara[1+i2][1+j2]
								pixelG += inimg[i + i2][j + j2][1]*mascara[1+i2][1+j2]
								pixelB += inimg[i + i2][j + j2][2]*mascara[1+i2][1+j2]
								count += mascara[1+i2][1+j2]
				pixelR = pixelR / count
				pixelG = pixelG / count
				pixelB = pixelB / count
				#print count
				row.append( [ pixelR, pixelG, pixelB])
				#row.append(pixel)
			outimg.append(row)
	output = input + "_media3x3" + ".png"
	scpm.imsave(pathnew + output, outimg)
	
#input = "shapes"
#ext = ".png"
#mascara3x3(input, ext)

input = "lena"
ext = ".png"
mascara3x3(input, ext)

#input = "mandril"
#ext = ".jpg"
#mascara3x3(input, ext)

