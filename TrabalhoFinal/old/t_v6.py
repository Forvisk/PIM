import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt
import math
from random import randint

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
	##print inimg
	##print size
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

	print "Procura Borda : " + pat + input + ext
	inimg = scpm.imread( pat + input + ext)
	size = inimg.shape

	M = size[0]
	N = size[1]
	borda = np.zeros( [M, N] )

	if len(size) == 3:
		ok = True

		# Ja calculado
		output = input + "_p1_v6"
		return output

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

		#Ja calculado
		output = input + "_p1_v5"
		return output
		
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
		output = input + "_p1_v6"
		scpm.imsave(pathtemp + output + ".png", borda)
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

def pontoMedio( p1, p2):
	x = ( p1[0] + p2[0]) / 2
	y = ( p1[1] + p2[1]) / 2
	return [x,y]

def detectaBorda( pat, input, ext, original):
	print "Borda : " + pat + input + ext
	inimg = scpm.imread( pat + input + ext)
	size = inimg.shape

	M = size[0]
	N = size[1]
	MeioM = M/2
	MeioN = N/2
	ExtrN = 0
	ExtrS = M-1
	ExtrW = 0
	ExtrE = N-1

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

		#Ja calcualdo
		#output = original + "_p2_v6"+ ".png"
		#return output

		change = True
		it = 10
		turn = True
		while( change and it > 0):
			r1 = abs( ExtrS - ExtrN) / 2
			r2 = abs( ExtrW - ExtrE) / 2
			c1 = [ExtrN + r1, MeioN]
			c2 = [MeioM, ExtrW + r2]

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

		r1 = abs( ExtrS - ExtrN) / 2
		r2 = abs( ExtrW - ExtrE) / 2
		c1 = [ExtrN + r1, MeioN]
		c2 = [MeioM, ExtrW + r2]

		centro 	= pontoMedio(c1, c2)

		rangeBorda = 15*min(size[0], size[1]) / 700

		ray = min( M-centro[0], N-centro[1])
		thisray = ray
		lastcount = 0
		lastchange = 0
		while( lastchange < min(size[0],size[1])/700,10) and (ray > 0):
			count = 0
			for i in range(0,M):
				for j in range( 0,N):
					if( distanciaEucl( centro,[i,j]) == ray) and (inimg[i][j] == 255):
						count += 1
			if( lastcount <= count):
				#print [ray, count]
				thisray = ray
				lastcount = count
				lastchange = 0
			else:
				lastchange += 1
			ray -= 1

		#print ('Raio: ', thisray)
		#print ('Centro: ', centro)


		borda = np.zeros( [M, N] )
		for i in range( 0, M):
			for j in range( 0, N):
				dist = distanciaEucl( centro, [i,j])
				if( dist >= thisray):#-rangeBorda):
					borda[i,j] = 255



	if ok:
		output = original + "_p2_v6"+ ".png"
		scpm.imsave(pathtemp + output, borda)
		return [output, centro, thisray]
	if not ok:
		return '-1'

def findColonia( pat, input, ext, borda):
	print "Procura colonias: "+pat+input+ext
	ok = True

	# Ja calculado
	output = input + "_p3_v6.png"
	return output

	inborda = scpm.imread(pathtemp+borda)
	inimg = scpm.imread(pat + input + ext)
	size = inimg.shape
	M = size[0]
	N = size[1]

	Kirsch = [	[[ 5,-3,-3],[ 5, 0,-3],[ 5,-3,-3]],
				[[-3,-3,-3],[ 5, 0,-3],[ 5, 5,-3]],
				[[-3,-3,-3],[-3, 0,-3],[ 5, 5, 5]],
				[[-3,-3,-3],[-3, 0, 5],[-3, 5, 5]],
				[[-3,-3, 5],[-3, 0, 5],[-3,-3, 5]],
				[[-3, 5, 5],[-3, 0, 5],[-3,-3,-3]],
				[[ 5, 5, 5],[-3, 0,-3],[-3,-3,-3]],
				[[ 5, 5,-3],[ 5, 0,-3],[-3,-3,-3]]]

	outKirsch = np.zeros([M,N])

	for i in range(0,M):
		for j in range(0,N):
			if inborda[i][j] != 255:

				pixKirsch = [0,0,0,0,0,0,0,0]
				pixKirsch0 = [0,0,0,0,0,0,0,0]
				pixKirsch1 = [0,0,0,0,0,0,0,0]
				pixKirsch2 = [0,0,0,0,0,0,0,0]
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							if ( j+j2 in range(0, size[1])):

								for k in range(0,8):
									pixKirsch0[k] += inimg[i + i2][j + j2][0]*Kirsch[k][1+i2][1+j2]
									pixKirsch1[k] += inimg[i + i2][j + j2][1]*Kirsch[k][1+i2][1+j2]
									pixKirsch2[k] += inimg[i + i2][j + j2][2]*Kirsch[k][1+i2][1+j2]
									pixKirsch[k] = pixKirsch0[k] + pixKirsch1[k] + pixKirsch2[k]


				thold = 700
				if( (abs(pixKirsch[0]) > thold) or (abs(pixKirsch[1]) > thold) or (abs(pixKirsch[2]) > thold) or (abs(pixKirsch[3]) > thold) or 
					(abs(pixKirsch[4]) > thold) or (abs(pixKirsch[5]) > thold) or (abs(pixKirsch[6]) > thold) or (abs(pixKirsch[7]) > thold)):
					#outKirsch[i][j] = [100,255,0]
					outKirsch[i][j] = 100
				else:
					#outKirsch[i][j] = [0,0,0]
					outKirsch[i][j] = 0
			else:
				#outKirsch[i][j] = [255,255,255]
				outKirsch[i][j] = 255

	if ok:
		output = input + "_p3_v6.png"
		scpm.imsave( pathtemp+output, outKirsch)
		return output
	else:
		return '-1'

def unionBorda( pat, input, original, ext):
	inimg = scpm.imread( pat+input)
	outimg = scpm.imread( path + original + ext)

	size = inimg.shape
	M = size[0]
	N = size[1]

	for i in range( 0, M):
		for j in range( 0, N):
			if inimg[i][j] == 100:
				outimg[i][j] = [255,255,0]

	output = original+"_pF_v6.png"
	scpm.imsave( pathtemp+output, outimg)
	return output

def teste_interno(pat, input, original):
	inimg = scpm.imread( pat+input)
	output = original + '_p4_v6.png'

	outBorda = 255
	borda = 100

	listaInterna = []

	size = inimg.shape
	M = size[0]
	N = size[1]

	miolo = False
	lastMiolo = False

	for i in range(0,M):
		for j in range( 0, N):
			if inimg[i][j] == outBorda:
				pass
			'''
			if inimg[i][j] == borda:
				if inimg[i][j-1] == 0:
					miolo = False
				else:
					if inimg[i][j+1] == 0:
						miolo = True
			'''
			if inimg[i][j] == borda:
				if inimg[i][j+1] == 0:
					miolo = not(miolo)

			if (inimg[i][j] != outBorda and inimg[i][j] != borda) and miolo:
				listaInterna.append([i,j])

	outimg = inimg
	for k in range( len(listaInterna)):
		outimg[listaInterna[k][0]][listaInterna[k][1]] = 150

	

	scpm.imsave(pathtemp+output, outimg)
	return output

def conect( pat, inimg, original):
	inimg = scpm.imread( pat+inimg)
	size = inimg.shape

	M = size[0]
	N = size[1]


	xI = randint(0, M)
	xJ = randint(0,N)
	while( inimg[xI][xJ] != 0):
		xI = randint(0, M)
		xJ = randint(0,N)

	print "ponto inicial"
	print [xI, xJ]

	lista = rangeDistancia( inimg, xI,xJ)
	#print lista

	output = original + "_p5_1_v6.png"
	outimg = np.zeros([M,N])
	for i in range(0,M):
		for j in range(0,N):
			outimg[i][j] = inimg[i][j]
	outimg[xI][xJ] = 200
	for k in range( len(lista)):
		outimg[lista[k][0]][lista[k][1]] = 150

	scpm.imsave(pathtemp+output, outimg)

	xI = randint(0, M)
	xJ = randint(0,N)
	while( inimg[xI][xJ] != 0):
		xI = randint(0, M)
		xJ = randint(0,N)

	print "ponto inicial2"
	print [xI, xJ]

	lista = rangeDistancia( inimg, xI,xJ)
	#print lista

	output = original + "_p5_2_v6.png"
	outimg = np.zeros([M,N])
	for i in range(0,M):
		for j in range(0,N):
			outimg[i][j] = inimg[i][j]
	outimg[xI][xJ] = 200
	for k in range( len(lista)):
		outimg[lista[k][0]][lista[k][1]] = 150

	scpm.imsave(pathtemp+output, outimg)

	output = original + "_p5_v6.png"
	return output

def rangeDistancia( inimg, iniI, iniJ):
	lista = []

	size = inimg.shape
	M = size[0]
	N = size[1]

	conecto = np.zeros([M,N])
	conecto[iniI][iniJ] = 1

	maxDist = min(M, N)
	#print size

	#print ["ini", (iniI,iniJ)]

	for d in range(1,maxDist):
		#print d
		'''
		X o o
		v C o
		o o o
		'''
		for k in range(-d, d+1):
			if (iniJ-d in range(0,N)) and ( iniI+k in range(0,M)):
				if inimg[iniI+k][iniJ-d] == 0:
					if verificaVizinhanca( iniI+k, iniJ-d, conecto) == 1:
						conecto[iniI+k][iniJ-d] = 1
						#print [iniI+k, iniJ-d]

		'''
		o < x
		o C o
		o o o
		'''
		for k in range(-d, d+1):
			if (iniI-d in range(0,M))  and ( iniJ+k in range(0,N)):
				if inimg[iniI-d][iniJ+k] == 0:
					if verificaVizinhanca( iniI-d, iniJ+k, conecto) == 1:
						conecto[iniI-d][iniJ+k] = 1
						#print [iniI+k, iniJ-d]

		'''
		o o o
		o C ^
		o o x
		'''
		for k in range(-d, d+1):
			if (iniJ+d in range(0,N))  and ( iniI+k in range(0,M)):
				if inimg[iniI+k][iniJ+d] == 0:
					if verificaVizinhanca( iniI+k, iniJ+d, conecto) == 1:
						conecto[iniI+k][iniJ+d] = 1
						#print [iniI+k, iniJ-d]

		'''
		o o o
		o C o
		x > o
		'''
		for k in range(-d, d):
			if (iniI+d in range(0,M))  and ( iniJ+k in range(0,N)):
				if inimg[iniI+d][iniJ+k] == 0:
					if verificaVizinhanca( iniI+d, iniJ+k, conecto) == 1:
						conecto[iniI+d][iniJ+k] = 1
						#print [iniI+k, iniJ-d]


	for i in range(0,M):
		for j in range(0,N):
			if conecto[i][j] == 1:
				lista.append([i,j])

	return lista

def verificaVizinhanca( pCi, pCj, matriz):
	size = matriz.shape

	for ki in range(-1,2):
		if( pCi+ki in range(0,size[0])):
			for kj in range(-1,2):
				if(pCj+kj in range(0, size[1])):
					if (ki != 0 and kj != 0):
						if matriz[pCi+ki][pCj+kj] == 1:
							return 1

	return 0

def trataProximoBorda( pat, input, original, centro, raio):
	inimg = scpm.imread(pat+input)
	output = original + "_p6_v6.png"

	size = inimg.shape
	M = size[0]
	N = size[1]

	zona = min(M/25,N/25)

	outimg = np.zeros([M,N])
	for i in range(0,M):
		for j in range(0,N):
			outimg[i][j] = inimg[i][j]

	print ("Raio: ", raio)
	print ("Zona:", raio-zona, raio)
	print ("Centro", centro)

	outimg[centro[0]][centro[1]] = 200
	ponto = []
	print (min(M/25,N/25), min(M/10,N/10))
	for i in range(0,M):
		for j in range(0,N):
			dist = distanciaEucl(centro,[i,j]) 
			if dist > raio-zona and dist < raio:
				if inimg[i][j] == 100:
					if getFarsa( [i,j], centro, inimg) == 0:
						outimg[i][j] = 0

				outimg[i][j] += 20
			if dist == raio-zona:
				ponto = [i,j]

	print ponto
	thisang = math.atan2( ponto[1]-centro[1], ponto[0]-centro[0])
	print thisang

	thisang = math.degrees(thisang)
	print thisang


	for i in range(0,M):
		for j in range(0,N):
			ang = math.atan2( j-centro[1], i-centro[0])
			ang = math.degrees(ang)
			if ang > thisang-10 and ang < thisang + 10:
				outimg[i][j] += 30

	scpm.imsave( pathtemp+output, outimg)


	return output

def getFarsa( ponto, centro, inimg):
	size = inimg.shape
	M = size[0]
	N = size[1]
	zonaMin = min(M/25,N/25)
	zonaMax = min(M/10,N/10)

	count = 0

	thisang = math.atan2( ponto[1]-centro[1], ponto[0]-centro[0])
	thisang = math.degrees(thisang)

	iMin = max(0, ponto[0]-M/7)
	iMax = min(M, ponto[0]+M/7)
	jMin = max(0, ponto[0]-N/7)
	jMax = min(N, ponto[0]+N/7)
	for i in range(iMin,iMax):
		for j in range(jMin,jMax):
			ang = math.atan2( j-centro[1], i-centro[0])
			ang = math.degrees(ang)
			if ang > thisang-2 and ang < thisang + 2:
				if inimg[i][j] == 100:
					dist = distanciaEucl([i,j], ponto)
					if dist in range(0, 100):
						#print dist
						#return 1
						count += 1
	print count

	return 0

def roda( input, ext):
	amostra = getAmostra( path, input, ext)
	if amostra == -1:
		return "ERRO"
	#else:	return amostra
	print ('Amostra recebida: ',amostra)
	borda = catchBorda( path, input, ext, amostra)
	if borda == '-1':
		return "ERRO"
	#else: return borda
	print borda
	ext2 = ".png"
	borda = detectaBorda( pathtemp, borda, ext2, input)
	if borda == '-1':
		return "ERRO"
	#else: return borda
	colonias = findColonia( path, input, ext, borda[0])
	if colonias == '-1':
		return "ERRO"
	print colonias
	#bordaInterna(pathtemp, colonias)
	#meio = teste_interno(pathtemp, colonias, input)
	#print meio

	#conecto = conect(pathtemp, colonias,input)
	#print conecto

	#tratadoBorda = trataProximoBorda( pathtemp, colonias, input, borda[1], borda[2])
	#print tratadoBorda

	uniao = unionBorda( pathtemp, colonias, input, ext)
	print uniao

	original = scpm.imread(path+input+ext)
	alt = scpm.imread(pathtemp+borda[0])
	size = alt.shape
	for i in range(size[0]):
		for j in range(size[1]):
			#if alt[i][j][0] != 0 and alt[i][j][1] != 0 and alt[i][j][2] != 0 :
			if alt[i][j] != 0 :
				original[i][j] = [alt[i][j],alt[i][j],alt[i][j]]
	output = input + "_r_v6.png"
	scpm.imsave(pathtemp+output, original)
	return output


'''
O que fazer agora

	conseguir colorir a parte interna das bordas para depois usar 
	a fonte interpolacao.py na pasta Funcoes para ler os compoentes conexos da imagem
	assim teremos o numero de colonias
'''


input = "placa_mancha"
ext = ".jpg"
print roda( input, ext)
print '\n'
'''
input = "placa_paint"
ext = ".jpg"
print roda( input, ext)
'''
'''
input = "placa_listra"
ext = ".jpg"
print roda( input, ext)
print '\n'
'''
#placa_pontos2.jpg nao funciona
'''
input = "placa_pontos2"
ext = ".jpg"
print roda( input, ext)
'''
'''
input = "placa_ponto3"
ext = ".jpeg"
print roda( input, ext)
print '\n'
'''
#placa_fungos.jpg nao funciona
'''
input = "placa_fungos"
ext = ".jpg"
print roda( input, ext)
'''
