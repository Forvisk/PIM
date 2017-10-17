import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

fatia_1 = [(20, [0,0,0]),(128,[255,0,0]),(230,[255,255,0]),(255,[0,255,0])]
fatia_2 = [(20, [0,0,0]),(40,[128,0,0]),(65,[128,128,0]),(90,[0,128,0]),(120, [0,0,128]),(160,[255,0,0]),(210,[255,255,0]),(255,[0,255,0])]
fatia_3 = [(10, [0,0,0]),(20,[128,0,0]),(40,[128,128,0]),(70,[0,128,0]),(110, [0,0,128]),(160,[255,0,0]),(220,[255,255,0]),(255,[0,255,0])]


def pseudocor( input, ext, fatia, cod):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	outimg = []
	##Imagem Escala cinza
	if (len(size) == 2):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				newpixel = [0,0,0]
				for fat in fatia:
					if( fat[0] <= inimg[i][j]):
						newpixel = fat[1]
				row.append( newpixel)
			outimg.append(row)
	##Imagem RGB
	if (len(size) == 3):
		for i in range(0, size[0]):
			row = []
			for j in range(0, size[1]):
				newpixel = [0,0,0]
				for fat in fatia:
					if( fat[0] <= inimg[i][j][0]):
						newpixel = fat[1]
				row.append( newpixel)
			outimg.append(row)
	output = input + "_psudocor" + cod + ".png"
	scpm.imsave(pathnew + output, outimg)
	
def getcor( pixel, fat):
	newpixel = []
	if len(pixel) == 1:
		if( fat[0] <= pixel):
			newpixel = fat[1]
	else:
		if( fat[0] <= pixel[0]):
			newpixel = fat[1]

	return newpixel
	
#input = "shapes"
#ext = ".png"
#pseudocor(input, fatia_1)

#input = "python"
#ext = ".png"
#pseudocor(input, fatia_1)

input = "lena"
ext = ".jpg"
pseudocor(input, ext, fatia_1, "1")

input = "r-x"
ext = ".jpg"
pseudocor(input, ext, fatia_1, "1")


input = "r-x"
ext = ".jpg"
pseudocor(input, ext, fatia_2, "2")


input = "r-x"
ext = ".jpg"
pseudocor(input, ext, fatia_3, "3")



