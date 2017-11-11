import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"

def getAmostraOutside( inimg, M, N):
	amostra = []
	for i in range( 0, M/20):
		#row = []
		for j in range( 0, N/20):
			#row.append( inimg[i][j])
			amostra.append( inimg[i][j])
			#print inimg[i][j]
		#amostra.append(row)
	return amostra

def amostragemOutside( input, ext):
	print "\n" + path + input + ext + "\n"
	inimg = scpm.imread( path + input + ext)
	size = inimg.shape
	#return getAmostraOutside( inimg, size[0], size[1])

	output = input + "_amostra" + ".png"
	scpm.imsave(pathnew + output, getAmostraOutside( inimg, size[0], size[1]))
	return output

input = "placa_paint"
ext = ".png"
amostra = amostragemOutside( input, ext)

input = "placa_listra"
ext = ".jpg"
amostra = amostragemOutside( input, ext)

input = "placa_pontos"
ext = ".jpg"
amostra = amostragemOutside( input, ext)

input = "placa_paint_2"
ext = ".png"
amostra = amostragemOutside( input, ext)