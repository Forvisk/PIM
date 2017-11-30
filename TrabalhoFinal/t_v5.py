import numpy as np
import scipy.misc as scpm
import matplotlib.pyplot as plt
import math
from PIL import Image

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
		output = input + "_p1_v5"
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

		#print ('Raio', thisray)



		borda = np.zeros( [M, N] )
		for i in range( 0, M):
			for j in range( 0, N):
				dist = distanciaEucl( centro, [i,j])
				if( dist >= thisray):#-rangeBorda):
					borda[i,j] = 255

	if ok:
		output = original + "_p2_v5"+ ".png"
		scpm.imsave(pathtemp + output, borda)
		return output
	if not ok:
		return '-1'

def findColonia( pat, input, ext, borda):
	print "Procura colonias: "+pat+input+ext
	ok = True

	inborda = scpm.imread(pathtemp+borda)
	inimg = scpm.imread(pat + input + ext)
	size = inimg.shape
	M = size[0]
	N = size[1]

	'''
	Sobel = [	[[-1,-2,-1],[ 0, 0, 0],[ 1, 2, 1]],
				[[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]]
	'''
	'''
	Prewitt = 	[	[[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]],
					[[-1,-1,-1],[ 0, 0, 0],[ 1, 1, 1]]]
	'''

	Kirsch = [	[[ 5,-3,-3],[ 5, 0,-3],[ 5,-3,-3]],
				[[-3,-3,-3],[ 5, 0,-3],[ 5, 5,-3]],
				[[-3,-3,-3],[-3, 0,-3],[ 5, 5, 5]],
				[[-3,-3,-3],[-3, 0, 5],[-3, 5, 5]],
				[[-3,-3, 5],[-3, 0, 5],[-3,-3, 5]],
				[[-3, 5, 5],[-3, 0, 5],[-3,-3,-3]],
				[[ 5, 5, 5],[-3, 0,-3],[-3,-3,-3]],
				[[ 5, 5,-3],[ 5, 0,-3],[-3,-3,-3]]]

	#outSobel = np.zeros([M,N,3])
	#outKirsch = np.zeros([M,N,3])
	outKirsch = np.zeros([M,N])
	#outPrewitt = np.zeros( [M,N,3])

	for i in range(0,M):
		for j in range(0,N):
			if inborda[i][j] != 255:
				'''
				pixSobel = [0,0]
				pixSobel0 = [0,0]
				pixSobel1 = [0,0]
				pixSobel2 = [0,0]
				'''
				'''
				pixprewitt = [0,0]
				pixprewitt0 = [0,0]
				pixprewitt1 = [0,0]
				pixprewitt2 = [0,0]
				'''
				pixKirsch = [0,0,0,0,0,0,0,0]
				pixKirsch0 = [0,0,0,0,0,0,0,0]
				pixKirsch1 = [0,0,0,0,0,0,0,0]
				pixKirsch2 = [0,0,0,0,0,0,0,0]
				for i2 in range(-1,2):
					if ( i+i2 in range(0,size[0])):
						for j2 in range(-1,2):
							if ( j+j2 in range(0, size[1])):
								'''
								for k in range(0,2):
									pixSobel0[k] += inimg[i + i2][j + j2][0]*Sobel[k][1+i2][1+j2]
									pixSobel1[k] += inimg[i + i2][j + j2][1]*Sobel[k][1+i2][1+j2]
									pixSobel2[k] += inimg[i + i2][j + j2][2]*Sobel[k][1+i2][1+j2]
									pixSobel[k] = pixSobel0[k] + pixSobel1[k] + pixSobel2[k]
								'''

								'''
								for k in range(0,2):
									pixprewitt0[k] += inimg[i + i2][j + j2][0]*Prewitt[k][1+i2][1+j2]
									pixprewitt1[k] += inimg[i + i2][j + j2][1]*Prewitt[k][1+i2][1+j2]
									pixprewitt2[k] += inimg[i + i2][j + j2][2]*Prewitt[k][1+i2][1+j2]
								'''
								for k in range(0,8):
									pixKirsch0[k] += inimg[i + i2][j + j2][0]*Kirsch[k][1+i2][1+j2]
									pixKirsch1[k] += inimg[i + i2][j + j2][1]*Kirsch[k][1+i2][1+j2]
									pixKirsch2[k] += inimg[i + i2][j + j2][2]*Kirsch[k][1+i2][1+j2]
									pixKirsch[k] = pixKirsch0[k] + pixKirsch1[k] + pixKirsch2[k]
									#print [k, i, j, pixKirsch0[k], pixKirsch1[k],pixKirsch2[k]]

				#for k in range(0,2):
				#	pixSobel[k] = pixSobel0[k] + pixSobel1[k] + pixSobel2[k]
				'''
				for k in range(0,2):
					pixprewitt[k] = pixprewitt0[k] + pixprewitt1[k] + pixprewitt2[k]
				'''
				'''
				thold = 400
				if( (abs(pixSobel[0]) > thold) or (abs(pixSobel[1]) > thold)):
					outSobel[i][j] = [100,100,0]
				else:
					outSobel[i][j] = [0,0,0]
				'''
				'''
				if( (abs(pixprewitt[0]) > 200) or (abs(pixprewitt[1]) > 200)):
					outPrewitt[i][j] = [100,100,0]
				else:
					outPrewitt[i][j] = [0,0,0]
				'''
				#for k in range(0,8):
				#	pixKirsch[k] = pixKirsch0[k] + pixKirsch1[k] + pixKirsch2[k]

				#print pixKirsch
				thold = 700
				if( (abs(pixKirsch[0]) > thold) or (abs(pixKirsch[1]) > thold) or (abs(pixKirsch[2]) > thold) or (abs(pixKirsch[3]) > thold) or 
					(abs(pixKirsch[4]) > thold) or (abs(pixKirsch[5]) > thold) or (abs(pixKirsch[6]) > thold) or (abs(pixKirsch[7]) > thold)):
					#outKirsch[i][j] = [100,255,0]
					outKirsch[i][j] = 100
				else:
					#outKirsch[i][j] = [0,0,0]
					outKirsch[i][j] = 0
			else:
				#outSobel[i][j] = [255,255,255]
				#outKirsch[i][j] = [255,255,255]
				outKirsch[i][j] = 255
				#outPrewitt[i][j] = [255,255,255]

	if ok:
		output = input + "_p3_v5.png"
		#scpm.imsave( pathtemp+output+"_sobel_.png", outSobel)
		#scpm.imsave( pathtemp+output+"_prewitt.png", outPrewitt)
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

	output = original+"_p4_v5.png"
	scpm.imsave( pathtemp+output, outimg)
	return output
	

def ErosaoDescricao( inimg):
	size = inimg.shape
	conjunto = []

	for i in range(size[0]):
		for j in range( size[1]):
			if inimg[i][j] == 100:
				conjunto.append((j,i))
	return conjunto

def Erode( conjunto):
	elemento = [	(-1,-1),(-1, 0),(-1, 1),
					( 0,-1),( 0, 0),( 0, 1),
					( 1,-1),( 1,-1),( 1, 1)]

	etapas = []
	for elem in elemento:
		etapa = []
		for val in conjunto:
			temp = ( val[0] - elem[0], val[1] - elem[1])
			etapa.append(temp)
		etapas.append(etapa)
	
	result = []
	for val in etapas[0]:
		insere = True
		for index in range(len(etapas)):
			if val not in etapas[index]:
				insere = False
		if insere:
			result.append(val)
	
	return result

def geraImgagem( conjunto, inimg):
	size = inimg.shape
	outimg = np.zeros( size)
	for val in conjunto:
		outimg[val[1]][val[0]] = 0

	for i in range( size[0]):
		for j in range( size[1]):
			if inimg[i][j] == 255:
				outimg[i][j] = 255

	return outimg

def Erosao( pat, input):
	inimg = np.array( Image.open(pat+input).convert('L'))
	conjunto = ErosaoDescricao( inimg)
	
	resultado = Erode( conjunto)
	outimg = geraImgagem( resultado, inimg)
	
	output = input + "_p4_erosao.png"
	scpm.imsave(pathtemp + output, outimg)
	return output


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

	#erodido = Erosao( pathtemp, colonias)
	#print erodido
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
	output = input + "_r_v5.png"
	scpm.imsave(pathtemp+output, original)
	return output


'''
O que fazer agora

	conseguir colorir a parte interna das bordas para depois usar 
	a fonte interpolacao.py na pasta Funções para ler os compoentes conexos da imagem

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

input = "placa_listra"
ext = ".jpg"
print roda( input, ext)
print '\n'

#placa_pontos2.jpg nao funciona
'''
input = "placa_pontos2"
ext = ".jpg"
print roda( input, ext)
'''
input = "placa_ponto3"
ext = ".jpeg"
print roda( input, ext)
print '\n'
#placa_fungos.jpg nao funciona
'''
input = "placa_fungos"
ext = ".jpg"
print roda( input, ext)
'''
