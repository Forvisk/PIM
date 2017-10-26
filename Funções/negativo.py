import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"

def negativo( input, ext, hlp):
	inimg = scpm.imread(path + input + ext)
		
	shape = inimg.shape
	#histogramas, intervalos = np.histogram(imagem, bins=np.arange(0,256))
	minPB = minR = minG = minB = 0
	
	
	outimg = []
	for l in range(shape[0]):
		row = []
		for c in range( shape[1]):
			#imagem[l][c]
			#row.append( [,,,])
			if( len(shape) == 2):
				color = abs(255 - inimg[l][c] + minPB)
				row.append( [ color, color, color])
			if( len(shape) == 3):
				r = abs(255 - inimg[l][c][0] + minR)
				g = abs(255 - inimg[l][c][1] + minG)
				b = abs(255 - inimg[l][c][2] + minB)
				row.append( [r, g, b])
		outimg.append(row)
	
	#outimg = abs(255 - imagem)	
	
	output = input + "_negativo" + hlp + ".png"
	scpm.imsave(pathnew + output, outimg)
	return output

input = "lena"
ext = ".png"
print negativo( input, ext, "")



	
