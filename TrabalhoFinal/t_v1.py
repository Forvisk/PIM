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

def detectaBorda( input, ext, p, mascara, Tresh, hlp, nameinput):
	inimg = scpm.imread(p + input + ext)
	size = inimg.shape

	outimg = []
	if len(size) == 2:
		outimg = unidim( inimg, size, mascara, Tresh, hlp)
	if len(size) == 3:
		outimg = rgbfim( inimg, size, mascara, Tresh, hlp)
		
	output = nameinput + "_t_v1" + hlp + ".png"
	scpm.imsave(pathnew + output, outimg)
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
			#print pixel
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

def rgb_to_grey( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	
	outimg = []
	
	##Imagem RGB
	if(len(size) == 3):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				resR = inimg[i][j][0]*299/1000
				resG = inimg[i][j][0]*587/1000
				resB = inimg[i][j][0]*114/1000
				pixelGray = resR + resG + resB
				
				#print count
				row.append( pixelGray)
				#row.append(pixel)
			outimg.append(row)
	else:
		print("Imagem ja em escala de cinza!")
	
	output = input + "_t_v1_p1"
	outext = ".png"
	scpm.imsave(pathtemp + output + outext, outimg)
	return output


input = "placa_paint"
ext = ".png"
temp =  rgb_to_grey(input, ext)
print detectaBorda( temp, ext, pathtemp, mascaraPrewitt, 160, "", input)

input = "placa_listra"
ext = ".jpg"
temp =  rgb_to_grey(input, ext)
ext = ".png"
print detectaBorda( temp, ext, pathtemp, mascaraPrewitt, 160, "", input)

input = "placa_pontos"
ext = ".jpg"
temp =  rgb_to_grey(input, ext)
ext = ".png"
print detectaBorda( temp, ext, pathtemp, mascaraPrewitt, 160, "", input)

input = "placa_paint_2"
ext = ".png"
temp =  rgb_to_grey(input, ext)
print detectaBorda( temp, ext, pathtemp, mascaraPrewitt, 160, "", input)