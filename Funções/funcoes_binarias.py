import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"

def uniao( input1, ext1, input2, ext2, hlp):
	input1 = binariza( input1, ext1, 100)
	inimg1 = scpm.imread(pathtemp + input1)	
	sizeIn1 = inimg1.shape
	
	input2 = binariza( input2, ext2, 100)
	inimg2 = scpm.imread(pathtemp + input2)	
	sizeIn2 = inimg2.shape
	
	print sizeIn1
	print sizeIn2
	
	output = input1 +"_union_" + input2 + hlp + ".png"
	#scpm.imsave(pathnew + output, outimg)
	return output


	
def binariza( input, ext, threshold):
	inimg = scpm.imread(path + input + ext)	
	shape = inimg.shape
	
	if( len(shape) == 3):
		#print input
		newimg = rgb_to_grey( input, ext)
		inimg = scpm.imread(pathtemp + newimg)
		shape = inimg.shape
	
	outimg = inimg
	outimg[inimg <= threshold] = 0
	outimg[inimg > threshold] = 255
		
	output = input + "_binar" + ".png"
	scpm.imsave( pathtemp + output, outimg)
	return output

	

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

input1 = "lena"
ext1 = ".png"
input2 = "mandril"
ext2 = ".jpg"
print uniao( input1, ext1, input2, ext2, "")
