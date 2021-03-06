import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt
import math

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

def getAmostra( pat, input, ext):
	print "Amostra : " + pat + input + ext
	inimg = scpm.imread( pat + input + ext)
	size = inimg.shape

	arrayAmostra = getAmostraOutside( inimg, size[0], size[1])
	amostra = -1
	nAmostra = len(arrayAmostra)

	if len(size) == 3:
		pR = 0
		pG = 0
		pB = 0
		for i in range(0, nAmostra):
			pR += arrayAmostra[i][0]
			pG += arrayAmostra[i][1]
			pB += arrayAmostra[i][2]
		pR = pR / nAmostra
		pG = pG / nAmostra
		pB = pB / nAmostra
		amostra = [pR, pG, pB]

	if len(size) == 1:
		for i in range(0, nAmostra):
			pX = amostra[i]
		amostra = pX / nAmostra

	return amostra

def catchBorda( pat, inimg, ext, amostra):
	ok = False
	_C = 20
	_C2 = 5

	print "Procura Borda : " + pat + input + ext
	inimg = scpm.imread( pat + input + ext)
	size = inimg.shape

	M = size[0]
	N = size[1]

	#borda = np.zeros( [M, N, 3] )
	borda = np.zeros( [M, N] )

	if len(size) == 3:
		ok = True

		for i in range( 0, M):
			count = _C
			for j in range(0, N):
				if count > 0:
					for c in range(0,2):
						if( inimg[i][j][c] not in range(amostra[c]-10, amostra[c]+10)):
							count -= 1
							#borda[i][j] = [255,255,255]
							borda[i][j] = 255

			count = _C
			for j in range(N-1, -1, -1):
				if count > 0:
					for c in range(0,2):
						if( inimg[i][j][c] not in range(amostra[c]-10, amostra[c]+10)):
							count -= 1
							#borda[i][j][1] = 255
							borda[i][j] = 255
			

		for j in range(0, N):
			count = _C
			for i in range( 0, M):
				if count > 0:
					for c in range(0,2):
						if( inimg[i][j][c] not in range(amostra[c]-10, amostra[c]+10)):
							count -= 1
							#borda[i][j][2] = 255
							borda[i][j] = 255

			count = _C
			for i in range( M-1, -1, -1):
				if count > 0:
					for c in range(0,2):
						if( inimg[i][j][c] not in range(amostra[c]-10, amostra[c]+10)):
							count -= 1
							#borda[i][j][0] = 255
							borda[i][j] = 255

	if len(size) == 1:
		ok = True
		
		for i in range( 0, M):
			count = _C
			for j in range(0, N):
				if count > 0:
					if( inimg[i][j] not in range(amostra-10, amostra+10)):
						count -= 1
						borda[i][j] = 255

			count = _C
			for j in range(N-1, -1, -1):
				if count > 0:
					if( inimg[i][j] not in range(amostra-10, amostra+10)):
						count -= 1
						borda[i][j] = 255
			

		for j in range(0, N):
			count = _C
			for i in range( 0, M):
				if count > 0:
					if( inimg[i][j] not in range(amostra-10, amostra+10)):
						count -= 1
						borda[i][j] = 255

			count = _C
			for i in range( M-1, -1, -1):
				if count > 0:
					if( inimg[i][j] not in range(amostra-10, amostra+10)):
						count -= 1
						borda[i][j] = 255

	if ok:
		output = input + "_getBorda_v3" + ".png"
		scpm.imsave(pathtemp + output, borda)
		return output
	if not ok:
		return '-1'

def distanciaEucl( p1, p2):
	x1 = p1[0]
	x2 = p2[0]
	y1 = p1[1]
	y2 = p2[1]
	dist = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
	#print dist
	return dist

def detectaBorda( pat, input):
	print "Borda : " + pat + input
	inimg = scpm.imread( pat + input)
	size = inimg.shape

	M = size[0]
	N = size[1]
	MeioM = M/2
	MeioN = N/2
	ExtrN = 0
	ExtrS = M-1
	ExtrW = 0
	ExtrE = N-1

	borda = np.zeros( [M, N, 3] )
	#borda = np.zeros( [M, N] )
	for i in range(0, M):
		for j in range(0,N):
			if inimg[i][j] == 255:
				borda[i][j] = [100,100,100]

	while( ExtrW < MeioN and inimg[MeioM][ExtrW] == 0):
		ExtrW += 1
	if( ExtrW != MeioN):
		ok = True

	while( ExtrE > MeioN and inimg[MeioM][ExtrE] == 0):
		ExtrE -= 1
	if( ExtrE != MeioN):
		ok = True

	while( ExtrN < MeioM and inimg[ExtrN][MeioN] == 0):
		ExtrN += 1
	if( ExtrN != MeioM):
		ok = True

	while( ExtrS > MeioM and inimg[ExtrS][MeioN] == 0):
		ExtrS -= 1
	if( ExtrS != MeioM):
		ok = True

	if ok:


		change = True
		it = 10
		turn = True
		while( change and it > 0):

			print [ ExtrN, ExtrS, ExtrW, ExtrE]

			for i in range( 0, abs( ExtrS - ExtrN)):
				borda[ExtrN + i][MeioN] = [255,255,255]

			for i in range( 0, abs( ExtrW - ExtrE)):
				borda[MeioM][ExtrW+i] = [255,255,255]

			for i in range(0, 7):
				borda[MeioM][ExtrW+i] = [255,0,0]	#Vermelho
				borda[MeioM][ExtrE-i] = [0,255,0]	#Verde
				borda[ExtrN+i][MeioN] = [0,0,255]	#Azul
				borda[ExtrS-i][MeioN] = [255,0,255]	#Magenta


			#	r**2 = x**2 + y**2	(circunferencia)
			r1 = abs( ExtrS - ExtrN) / 2
			r2 = abs( ExtrW - ExtrE) / 2
			c1 = [ExtrN + r1, MeioN]
			c2 = [MeioM, ExtrW + r2]
			print ( r1, r2)
			print (c1, c2)

			for i in range(-2, 3):
				borda[c1[0] +i][c1[1] +i][0] = 255
				borda[c1[0] -i][c1[1] +i][0] = 255
				borda[c2[0] +i][c2[1] +i][1] = 255
				borda[c2[0] -i][c2[1] +i][1] = 255


			if turn:
				turn = False
				NewMeioMrfN = c1[0]
				NewExtrW = 0
				while( ExtrW < MeioN and inimg[NewMeioMrfN][NewExtrW] == 0):
					NewExtrW += 1
				NewExtrE = N-1
				while( NewExtrE > MeioN and inimg[NewMeioMrfN][NewExtrE] == 0):
					NewExtrE -= 1

				if( NewExtrE >= ExtrE) and ( NewExtrW <= ExtrW):
					ExtrE = NewExtrE
					ExtrW = NewExtrW
					MeioM = NewMeioMrfN
				else:
					change = False

			else:
				turn = True
				NewMeioNrfM = c2[0]
				NewExtrN = 0
				while( NewExtrN < MeioM and inimg[NewMeioNrfM][NewExtrN] == 0):
					NewExtrN += 1
				NewExtrS = M-1
				while( NewExtrN > MeioM and inimg[NewMeioNrfM][NewExtrS] == 0):
					NewExtrN -= 1

				if ( NewExtrN >= ExtrN) and ( NewExtrS <= ExtrS):
					ExtrS = NewExtrS
					ExtrN = NewExtrN
					MeioN = NewMeioNrfM
				else:
					change = False

			it -= 1



	if ok:
		output = input + "_borda_v3" + ".png"
		scpm.imsave(pathtemp + output, borda)
		return output
	if not ok:
		return '-1'


def roda( input, ext):
	amostra = getAmostra( path, input, ext)
	if amostra == -1:
		return "ERRO"
	#else:	return amostra
	print amostra
	borda = catchBorda( path, input, ext, amostra)
	if borda == '-1':
		return "ERRO"
	#else: return borda
	print borda
	borda = detectaBorda( pathtemp, borda)
	if borda == '-1':
		return "ERRO"
	else: return borda



input = "placa_paint"
ext = ".png"
print roda( input, ext)

input = "placa_listra"
ext = ".jpg"
print roda( input, ext)

input = "placa_mancha"
ext = ".jpg"
print roda( input, ext)

# placa_fungos.jpg possiu marcas de agua o que impossibilita a  utilizacao
'''
input = "placa_fungos"
ext = ".jpg"
print roda( input, ext)
'''

#input = "placa_pontos"
#ext = ".jpg"
#print roda( input, ext)

#input = "placa_paint_2"
#ext = ".png"
#print roda( input, ext)