import numpy as np
import scipy.misc as scpm


mascaraPrewitt = 	[
						[[ -1,  0,  1],
						 [ -1,  0,  1],
						 [ -1,  0,  1]],
						[[ -1, -1, -1],
						 [  0,  0,  0],
						 [  1,  1,  1]]
					]
					
mascaraSobel = 	[
						[[ -1,  0,  1],
						 [ -2,  0,  2],
						 [ -1,  0,  1]],
						[[ -1, -2, -1],
						 [  0,  0,  0],
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
		outimg = unidim( inimg, size, mascara, Tresh, hlp)
	if len(size) == 3:
		outimg = rgbfim( inimg, size, mascara, Tresh, hlp)
		
	output = input + "_detecborda" + hlp + ".png"
	scpm.imsave(pathtemp + output, outimg)
	return output


def unidim( inimg, size, mascara, Tresh, hlp):
	print "gray scale"
	outimg = []
	
	for i in range(0, size[0]):
		row = []
		
		for j in range(0, size[1]):
			pixel = 0
			pixel0 = 0
			pixel1 = 0
			for i2 in range(-1,2):
				if ( i+i2 in range(0,size[0])):
					for j2 in range(-1,2):
						if ( j+j2 in range(0, size[1])):
							pixel0 += inimg[i + i2][j + j2]*mascara[0][1+i2][1+j2]
							pixel1 += inimg[i + i2][j + j2]*mascara[1][1+i2][1+j2]
			pixel = pixel0 + pixel1
			print pixel
			if( abs(pixel) > Tresh):
				pixel = 255
			else:
				pixel = 0
			row.append( [ pixel, pixel, pixel])
		outimg.append(row)
	
	return outimg

def rgbfim( inimg, size, mascara, Tresh, hlp):
	print "RGB"
	outimg = []
	
	for i in range(0, size[0]):
		row = []
		
		for j in range(0, size[1]):
			pixel = 0
			pixel0 = 0
			pixel1 = 0
			for i2 in range(-1,2):
				if ( i+i2 in range(0,size[0])):
					for j2 in range(-1,2):
						if ( j+j2 in range(0, size[1])):
							pixel0 += inimg[i + i2][j + j2][0]*mascara[0][1+i2][1+j2]
							pixel1 += inimg[i + i2][j + j2][1]*mascara[0][1+i2][1+j2]
			pixel = pixel0 + pixel1
			#print pixel
			if( abs(pixel) > Tresh):
				pixel = 255
			else:
				pixel = 0
			row.append( [ pixel, pixel, pixel])
		outimg.append(row)
	
	return outimg

'''
input = "linhas_aa"
ext = ".png"
print detectaBorda( input, ext, path, mascaraPrewitt, 160, "00")
'''
input = "placa_listra"
ext = '.jpg'
print detectaBorda( input, ext, path, mascaraSobel, 160, "01")
