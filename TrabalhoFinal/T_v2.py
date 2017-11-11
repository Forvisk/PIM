import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"


def getAmostraOutside( inimg, M, N):
	amostra = []
	for i in range( 0, M/10):
		for j in range( 0, N/10):
			amostra.append( inimg[i][j])
		for j in range( N-1, N-N/10, -1):
			amostra.append( inimg[i][j])

	for i in range( M-1, M-M/10, -1):
		for j in range( 0, N/10):
			amostra.append( inimg[i][j])
		for j in range( N-1, N-N/10, -1):
			amostra.append( inimg[i][j])

	return amostra

def amostragemOutside( input, ext):
	#print "\n" + path + input + ext + "\n"
	print "Amostra de: " + input + ext
	inimg = scpm.imread( path + input + ext)
	size = inimg.shape
	#print size
	amostra = getAmostraOutside( inimg, size[0], size[1])
	nAmostra = len(amostra)
	print nAmostra
	if len(size) == 3: #rgb
		pR = 0
		pG = 0
		pB = 0
		for i in range(0, nAmostra):
			pR += amostra[i][0]
			pG += amostra[i][1]
			pB += amostra[i][2]
		pR = pR / nAmostra
		pG = pG / nAmostra
		pB = pB / nAmostra
		mediaAmostra = [pR, pG, pB]
	else:
		if len(size) == 1: #gray scale
			for i in range(0, nAmostra):
				pX = amostra[i]
			mediaAmostra = pX / nAmostra
		else:
			mediaAmostra = -1
			print "ERRO!"
	mediaAmostra
	return mediaAmostra

	#output = input + "_amostra" + ".png"
	#scpm.imsave(pathnew + output, getAmostraOutside( inimg, size[0], size[1]))
	#return output

def findBorda( input, ext, amostra):
	inimg = scpm.imread( path + input + ext)
	size = inimg.shape

	borda = np.zeros(size)
	if len(size) == 3:	#RGB
		for i in range( 0, size[0]):
			found = False
			p = [0,0,0]
			j = 0
			#while( j in range( 0, size[1]) and not found):
			for j in range(  0, size[1]/2+1):
				for c in range(0, 2):
					if( inimg[i][j][c] not in range(amostra[c]-10, amostra[c]+10)):
						found = True
						borda[i][j] = [255, 255, 255]

			for j in range(  size[1]-1, size[1]/2, -1):
				for c in range(0, 2):
					if( inimg[i][j][c] not in range(amostra[c]-10, amostra[c]+10)):
						found = True
						borda[i][j] = [255, 255, 255]

			

	if len(size) == 1:
		for i in range( 0, size[0]):
			found = False
			j = 0
			for j in range( 0, size[1]/2+1):
				if( inimg[i][j] not in range(amostra-10, amostra+10)):
					found = True
					borda[i][j] = [255, 255, 255]

			found = False
			for j in range( size[1]-1, size[1]/2, -1):
				if( inimg[i][j] not in range(amostra-10, amostra+10)):
					found = True
					borda[i][j] = [255, 255, 255]
	
	output = input + "_borda_tv2" + ".png"
	scpm.imsave(pathnew + output, borda)
	return output


#input = "placa_paint"
#ext = ".png"
#amostra = amostragemOutside( input, ext)
#print amostra
#print findBorda( input, ext, amostra)

input = "placa_pontos"
ext = ".jpg"
amostra = amostragemOutside( input, ext)
print amostra
print findBorda( input, ext, amostra)

input = "placa_listra"
ext = ".jpg"
amostra = amostragemOutside( input, ext)
print amostra
print findBorda( input, ext, amostra)

#input = "placa_paint_2"
#ext = ".jpg"
#amostra = amostragemOutside( input, ext)
#print amostra
#print findBorda( input, ext, amostra)