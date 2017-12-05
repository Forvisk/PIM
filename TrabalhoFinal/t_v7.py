import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt
import math
import sys
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

	print '(p1)'
	inimg = scpm.imread( pat + input + ext)
	size = inimg.shape

	M = size[0]
	N = size[1]
	borda = np.zeros( [M, N] )

	if len(size) == 3:
		ok = True

		# Ja calculado
		#output = input + "_p1_v7"
		#return output

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
		#output = input + "_p1_v7"
		#return output
		
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
		output = input + "_p1_v7"
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
	print '(p2)'
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
		#output = original + "_p2_v7"+ ".png"
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
		output = original + "_p2_v7"+ ".png"
		scpm.imsave(pathtemp + output, borda)
		return output
	if not ok:
		return '-1'

def findColonia( pat, input, ext, borda):
	print '(p3)'
	ok = True

	# Ja calculado
	#output = input + "_p3_v7.png"
	#return output

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
		output = input + "_p3_v7.png"
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

	output = original+"_pF_v7.png"
	scpm.imsave( pathtemp+output, outimg)
	return output

def areaConecta( pat, input, original):
	print '(p4) Wait...'
	inimg = scpm.imread( pat+input)
	size = inimg.shape
	M = size[0]
	N = size[1]

	#ja rodou
	#output = original + '_p4_v7.png'
	#return output

	outimg = pixelConecto( inimg)

	#print outimg
	for i in range(0,M):
		for j in range(0,N):
			if outimg[i][j] == 2:
				outimg[i][j] = 50
				#print [i,j]

	output = original + '_p4_v7.png'
	#print pathtemp + output
	scpm.imsave( pathtemp + output, outimg)
	return output

def pixelConecto( inimg):
	size = inimg.shape
	M = size[0]
	N = size[1]

	outimg = np.zeros([M,N])
	for i in range(0,M):
		for j in range(0,N):
			outimg[i][j] = inimg[i][j]

	pI = randint(0, M-1)
	pJ = randint(0, N-1)
	while( inimg[pI][pJ] != 0):
		pI = randint(0, M-1)
		pJ = randint(0,N-1)
	pontoOrig = [pI,pJ]

	outimg[pontoOrig[0]][pontoOrig[1]] = 1
	change = True
	ponto = [pontoOrig[0],pontoOrig[1]]


	pontosCon = []
	pontosCon.append(ponto)
	npontosCon = 1
	k = 0
	#while( change):
	while ( k < npontosCon):
		ponto = pontosCon[k]
		#print ( 'next', ponto)
		change = False
		if ponto[0]-1 in range(0,M):
			if outimg[ ponto[0]-1][ ponto[1]] == 0:
				outimg[ ponto[0]-1][ ponto[1]] = 1
				pontosCon.append( [ponto[0]-1, ponto[1]])
				npontosCon += 1
				#print [ponto[0]-1, ponto[1]]

		if ponto[0]+1 in range(0,M):
			if outimg[ ponto[0]+1][ ponto[1]] == 0:
				outimg[ ponto[0]+1][ ponto[1]] = 1
				pontosCon.append( [ponto[0]+1, ponto[1]])
				npontosCon += 1
				#print [ ponto[0]+1, ponto[1]]

		if ponto[1]-1 in range(0,N):
			if outimg[ ponto[0]][ ponto[1]-1] == 0:
				outimg[ ponto[0]][ ponto[1]-1] = 1
				pontosCon.append( [ponto[0], ponto[1]-1])
				npontosCon += 1
				#print [ ponto[0], ponto[1]-1]

		if ponto[1]+1 in range(0,N):
			if outimg[ ponto[0]][ ponto[1]+1] == 0:
				outimg[ ponto[0]][ ponto[1]+1] = 1
				pontosCon.append( [ponto[0], ponto[1]+1])
				npontosCon += 1
				#print [ ponto[0], ponto[1]+1]

		outimg[ ponto[0]][ ponto[1]] = 2
		k += 1
		#print ( 'ok', ponto)
		'''
		for i in range(0, M):
			for j in range( 0, N

				):
				if outimg[i][j] == 1:
					ponto = [i,j]
					change = True
		'''

	return outimg

def getAreasIguais( pat, input, original, ext):
	print '(p5) Wait...'
	inimg = scpm.imread( pat + input)
	oriimg = scpm.imread( path + original + ext)

	size = inimg.shape
	M = size[0]
	N = size[1]

	listaCor = []
	tam = 0
	add = True

	for i in range(0,M):
		for j in range(0,N):
			if inimg[i][j] == 50:
				add = True
				pixel = [ oriimg[i][j][0],oriimg[i][j][1],oriimg[i][j][2]]
				if tam > 0:
					for k in range(0,tam):
						if pixel[0] == listaCor[k][0] and pixel[1] == listaCor[k][1] and pixel[2] == listaCor[k][2]:
							add = False
							break
				else:
					add = True

				if add:
					#print pixel
					listaCor.append( pixel)
					tam += 1

	outimg = np.zeros([M,N])
	listaPontos = []
	for i in range(0,M):
		for j in range(0,N):
			if inimg[i][j] == 0:
				pixel = [ oriimg[i][j][0],oriimg[i][j][1],oriimg[i][j][2]]
				for k in range( 0, len(listaCor)):
						if pixel[0] == listaCor[k][0] and pixel[1] == listaCor[k][1] and pixel[2] == listaCor[k][2]:
							outimg[i][j] = 75
							#print( [i,j], pixel)
							listaPontos.append([i,j])
							#print [i,j]
			else:
				outimg[i][j] = inimg[i][j]
	
	output = original + "_p5.1_v7.png"
	scpm.imsave( pathtemp+output, outimg)

	outimg = np.zeros([M,N])
	for i in range(0,M):
		for j in range(0,N):
			outimg[i][j] = inimg[i][j]

	for k in range(0, len(listaPontos)):
		#print listaPontos[k]
		i = listaPontos[k][0]
		j = listaPontos[k][1]
		#print ([i,j], outimg[i][j])
		if outimg[i][j] == 0:
			print 'Busca Area Conexa'
			outimg = areaConexa( listaPontos[k], outimg)

	for i in range(0,M):
		for j in range(0,N):
			if outimg[i][j] == 2:
				outimg[i][j] = 50
	
	output = original + '_p5.2_v7.png'
	scpm.imsave( pathtemp+output, outimg)

	return output

def areaConexa( pontoOrig, inimg):
	size = inimg.shape
	M = size[0]
	N = size[1]

	#print ( 'Orige: ', pontoOrig)

	outimg = np.zeros([M,N])
	for i in range(0,M):
		for j in range(0,N):
			outimg[i][j] = inimg[i][j]

	outimg[pontoOrig[0]][pontoOrig[1]] = 1
	change = True
	ponto = [pontoOrig[0],pontoOrig[1]]

	pontosCon = []
	pontosCon.append(ponto)
	npontosCon = 1
	k = 0
	#while( change):
	while ( k < npontosCon):
		ponto = pontosCon[k]
		#print ( 'next', ponto)
		change = False
		if ponto[0]-1 in range(0,M):
			if outimg[ ponto[0]-1][ ponto[1]] == 0:
				outimg[ ponto[0]-1][ ponto[1]] = 1
				pontosCon.append( [ponto[0]-1, ponto[1]])
				npontosCon += 1
				#print [ponto[0]-1, ponto[1]]

		if ponto[0]+1 in range(0,M):
			if outimg[ ponto[0]+1][ ponto[1]] == 0:
				outimg[ ponto[0]+1][ ponto[1]] = 1
				pontosCon.append( [ponto[0]+1, ponto[1]])
				npontosCon += 1
				#print [ ponto[0]+1, ponto[1]]

		if ponto[1]-1 in range(0,N):
			if outimg[ ponto[0]][ ponto[1]-1] == 0:
				outimg[ ponto[0]][ ponto[1]-1] = 1
				pontosCon.append( [ponto[0], ponto[1]-1])
				npontosCon += 1
				#print [ ponto[0], ponto[1]-1]

		if ponto[1]+1 in range(0,N):
			if outimg[ ponto[0]][ ponto[1]+1] == 0:
				outimg[ ponto[0]][ ponto[1]+1] = 1
				pontosCon.append( [ponto[0], ponto[1]+1])
				npontosCon += 1
				#print [ ponto[0], ponto[1]+1]

		outimg[ ponto[0]][ ponto[1]] = 2
		k += 1
		#print ( 'ok', ponto)
		'''
		for i in range(0, M):
			for j in range( 0, N

				):
				if outimg[i][j] == 1:
					ponto = [i,j]
					change = True
		'''

	return outimg

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
	colonias = findColonia( path, input, ext, borda)
	if colonias == '-1':
		return "ERRO"
	print colonias

	conecto = areaConecta( pathtemp, colonias, input)
	print conecto

	areas = getAreasIguais( pathtemp, conecto, input, ext)
	print areas

	uniao = unionBorda( pathtemp, colonias, input, ext)
	print uniao

	original = scpm.imread(path+input+ext)
	alt = scpm.imread(pathtemp+borda)
	size = alt.shape
	for i in range(size[0]):
		for j in range(size[1]):
			#if alt[i][j][0] != 0 and alt[i][j][1] != 0 and alt[i][j][2] != 0 :
			if alt[i][j] != 0 :
				original[i][j] = [alt[i][j],alt[i][j],alt[i][j]]
	output = input + "_r_v7.png"
	scpm.imsave(pathtemp+output, original)
	return output


'''
O que fazer agora

	conseguir colorir a parte interna das bordas para depois usar 
	a fonte interpolacao.py na pasta Funcoes para ler os compoentes conexos da imagem
	assim teremos o numero de colonias
'''
print 'Inicio programa' 

input = "placa_mancha"
ext = ".jpg"
print "\nInicio "+input+ext
print roda( input, ext)
print 'Fim '+input+ext+'\n'

'''
input = "placa_paint"
ext = ".jpg"
print roda( input, ext)
'''

input = "placa_listra"
ext = ".jpg"
print '\nInicio '+input+ext
print roda( input, ext)
print 'Fim '+input+ext+'\n'

#placa_pontos2.jpg nao funciona
'''
input = "placa_pontos2"
ext = ".jpg"
print roda( input, ext)
'''

input = "placa_ponto3"
ext = ".jpeg"
print '\nInicio '+input+ext
print roda( input, ext)
print 'Fim '+input+ext+'\n'

#placa_fungos.jpg nao funciona
'''
input = "placa_fungos"
ext = ".jpg"
print roda( input, ext)
'''
