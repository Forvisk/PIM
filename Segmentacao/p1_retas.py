import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"

mascaraHor = [		[-1,-1,-1],
				[ 2, 2, 2],
				[-1,-1,-1]
			]
mascaraVert = [	[-1, 2,-1],
				[-1, 2,-1],
				[-1, 2,-1]
			]
mascaraAng45 = [	[-1,-1, 2],
				[-1, 2,-1],
				[ 2,-1,-1]
			]
mascaraAng135 = [	[ 2,-1,-1],
				[-1, 2,-1],
				[-1,-1, 2]
			]

def mascara3x3( input, ext, p, mascara, Tresh, hlp):
	inimg = scpm.imread(p + input + ext)
	size = inimg.shape

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
				if( pixel > Tresh):
					pixel = 255
				else:
					pixel = 0
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
								#count += abs(mascara[1+i2][1+j2])
				#pixelR = pixelR / count
				#pixelG = pixelG / count
				#pixelB = pixelB / count
				
				if( pixelR > Tresh):
					pixelR = 255
				else:
					pixelR = 0
				if( pixelG > Tresh):
					pixelG = 255
				else:
					pixelG = 0
				if( pixelB > Tresh):
					pixelB = 255
				else:
					pixelB = 0
				#print count
				row.append( [ pixelR, pixelG, pixelB])
				#row.append(pixel)
			outimg.append(row)
	output = input + "_p1_retas" + hlp + ".png"
	scpm.imsave(pathtemp + output, outimg)
	return output
	
input = "linhas_aa"
ext = ".png"

out = mascara3x3( input, ext, path, mascaraHor, 800, "hor")
print out
out = mascara3x3( input, ext, path, mascaraVert, 800, "ver")
print out
out = mascara3x3( input, ext, path, mascaraAng45, 800, "45")
print out
out = mascara3x3( input, ext, path, mascaraAng135, 800, "135")
print out
