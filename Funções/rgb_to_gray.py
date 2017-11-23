import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"

#lvl = r*299/1000 + g*587/1000 + b*114/1000

def rgb_to_grey( input, ext):
	inimg = scpm.imread(path + input + ext)
	size = inimg.shape
	print size
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
	print outimg
	scpm.imsave(pathnew + output, outimg)
	return output
	
input = "mandril"
ext = ".jpg"
print rgb_to_grey(input, ext)



