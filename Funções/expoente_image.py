import numpy as np
import scipy.misc as scpm
import math

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"

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
	
	output = input + "_gray" + ".png"
	scpm.imsave(pathtemp + output, outimg)
	return output

def expoente( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	if len(size) == 3:
		input = rgb_to_grey(input, ext)
		inimg = scpm.imread(pathtemp + input)
		size = inimg.shape
	
	outimg = np.zeros(size)
	for i in range( size[0]):
		for j in range( size[1]):
			outimg[i][j] = max(math.exp(inimg[i][j]) - 256, 0)
	output = input + "_exp" + ".png"
	scpm.imsave(pathnew + output, outimg)
	return output

input = "teste_11"
ext = ".jpg"
print expoente(input, ext)
