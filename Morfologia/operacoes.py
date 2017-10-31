import numpy as np
import scipy.misc as scpm
from PIL import Image

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"

elemento1 = [(-1,0),(0,0),(1,0),(0,1),(0,-1)]
elemento2 = [(-2,0),(-1,0),(0,0),(1,0),(2,0)]
elemento3 = [(-2,0),(2,0),(0,2),(0,-2)]

def descricao( inimg):
	shape = inimg.shape
	conjunto = []
	for L in range(shape[0]):
		for C in range(shape[1]):
			if inimg[L][C] == 0:
				conjunto.append((C,L))
	return conjunto
	
def erode( conjunto, elemento):
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

def dilata( conjunto, elemento):
	result = []
	for val in conjunto:
		for elem in elemento:
			temp = ( val[0]+elem[0],val[1]+elem[1])
			if temp not in result:
				result.append(temp)
	return result	

def geraImgagem( conjunto, shape):
	outimg = np.ones(shape)*255
	for val in conjunto:
		outimg[val[1]][val[0]] = 0
	return outimg
	
def erosao( input, ext, elemento, hlp):
	inimg = np.array( Image.open(path+input+ext).convert('L'))
	conjunto = descricao( inimg)
	
	resultado = erode( conjunto, elemento)
	outimg = geraImgagem( resultado, inimg.shape)
	
	output = input + "_erosao" + hlp + ".png"
	scpm.imsave(pathnew + output, outimg)
	return output
	
def dilatacao( input, ext, elemento, hlp):
	inimg = np.array( Image.open(path+input+ext).convert('L'))
	conjunto = descricao( inimg)
	
	resultado = dilata( conjunto, elemento)
	outimg = geraImgagem( resultado, inimg.shape)
	
	output = input + "_dilatacao" + hlp + ".png"
	scpm.imsave(pathnew + output, outimg)
	return output
	
def abertura( input, ext, elemento, hlp):
	inimg = np.array( Image.open(path+input+ext).convert('L'))
	conjunto = descricao( inimg)
	
	resultado = erode( conjunto, elemento)
	outerode = geraImgagem( resultado, inimg.shape)
	conjunto = descricao( outerode)
	resultado = dilata( conjunto, elemento)
	
	outimg = geraImgagem( resultado, inimg.shape)
	
	output = input + "_abertura" + hlp + ".png"
	scpm.imsave(pathnew + output, outimg)
	return output
	
def fechamento( input, ext, elemento, hlp):
	inimg = np.array( Image.open(path+input+ext).convert('L'))
	conjunto = descricao( inimg)
	
	resultado = dilata( conjunto, elemento)
	outerode = geraImgagem( resultado, inimg.shape)
	conjunto = descricao( outerode)
	resultado = erode( conjunto, elemento)
	
	outimg = geraImgagem( resultado, inimg.shape)
	
	output = input + "_fechamento" + hlp + ".png"
	scpm.imsave(pathnew + output, outimg)
	return output

#main
input = 'base-erosao'
ext = '.png'
print erosao( input, ext, elemento1, "_v1")

input = 'base-dilatacao'
ext = '.png'
print dilatacao( input, ext, elemento1, "_v1")
	
input = 'base-erosao'
ext = '.png'
print abertura( input, ext, elemento1, "_v1")

input = 'base-dilatacao'
ext = '.png'
print fechamento( input, ext, elemento1, "_v1")

input = 'base-erosao'
ext = '.png'
print erosao( input, ext, elemento2, "_v2")

input = 'base-dilatacao'
ext = '.png'
print dilatacao( input, ext, elemento2, "_v2")
	
input = 'base-erosao'
ext = '.png'
print abertura( input, ext, elemento2, "_v2")

input = 'base-dilatacao'
ext = '.png'
print fechamento( input, ext, elemento2, "_v2")

input = 'base-erosao'
ext = '.png'
print erosao( input, ext, elemento3, "_v3")

input = 'base-dilatacao'
ext = '.png'
print dilatacao( input, ext, elemento3, "_v3")
	
input = 'base-erosao'
ext = '.png'
print abertura( input, ext, elemento3, "_v3")

input = 'base-dilatacao'
ext = '.png'
print fechamento( input, ext, elemento3, "_v3")
