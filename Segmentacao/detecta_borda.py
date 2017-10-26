import numpy as np
import scipy.misc as scpm


mascaraPrewitt = 	[
						[[ -1,  0,  1],
						 [ -1,  0,  1],
						 [ -1,  0,  1]],
						[[ -1, -1, -1]
						 [  0,  0,  0]
						 [  1,  1,  1]]
					]
					
mascaraSobel = 	[
						[[ -1,  0,  1],
						 [ -2,  0,  2],
						 [ -1,  0,  1]],
						[[ -1, -2, -1]
						 [  0,  0,  0]
						 [  1,  2,  1]]
					]

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"

def detectaBorda( input, ext, p, mascara, Tresh, hlp):
	inimg = scpm.imread(p + input + ext)
	size = inimg.shape

	outimg = []
	if len(size) == 2:
		outimg = unidim( inimg, mascara[0], Tresh, hlp)
	if len(size) == 3:
		outimg = rgbfim( inimg, mascara[0], Tresh, hlp)
		
	output = input + "_p1_retas" + hlp + ".png"
	scpm.imsave(pathtemp + output, outimg)
	return output


def unidim( inimg, mascara, Tresh, hlp):
	print "gray scale"
	outimg = []
	
	for i in range(0, size[0]):
		row = []
		
		for j in range(0, size[1]):
			pixel = 0
			for i2 in range(-1,2):
				if ( i+i2 in range(0,size[0])):
					for j2 in range(-1,2):
						if ( j+j2 in range(0, size[1])):
							pixel += inimg[i + i2][j + j2]*mascara[1+i2][1+j2]
			if( pixel > Tresh):
				pixel = 255
			else:
				pixel = 0
			row.append( [ pixel, pixel, pixel])
		outimg.append(row)
	
	return outimg

def rgbfim( inimg, mascara, Tresh, hlp)
	print "RGB"
	outimg = []
	
		for i in range(0, size[0]):
		row = []
		
		for j in range(0, size[1]):
			pixel = 0
			for i2 in range(-1,2):
				if ( i+i2 in range(0,size[0])):
					for j2 in range(-1,2):
						if ( j+j2 in range(0, size[1])):
							pixel += inimg[i + i2][j + j2][0]*mascara[1+i2][1+j2]
			if( pixel > Tresh):
				pixel = 255
			else:
				pixel = 0
			row.append( [ pixel, pixel, pixel])
		outimg.append(row)
	
	return outimg


input = "lena"
ext = ".png"
print detectaBorda( input, ext, path, mascaraPrewitt, 800, "00")
