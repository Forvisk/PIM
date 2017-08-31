import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
import math

path = "path/"

def distanciaEucl(x1, y1, x2, y2):
	dist = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
	print dist
	
def distanciaD4( ponto1, ponto2):
	if( len(ponto1) == len(ponto2)):
		dime = len(ponto1)
		ins = 0
		res = 0
		for i in range(0, dime):
			ins = max(ponto1[i] - ponto2[i], -(ponto1[i] - ponto2[i]))
			res += ins
		print res
		
def distanciaD8(ponto1, ponto2):
	if( len(ponto1) == len(ponto2)):
		dime = len(ponto1)
		res = 0
		for i in range(0, dime):
			res  =max( max(ponto1[i] - ponto2[i], -(ponto1[i] - ponto2[i])), res)
		print res


ponto1 = [1, 3]
ponto2 = [15, 19]
distanciaEucl(ponto1[0], ponto1[1], ponto2[0], ponto2[1])
distanciaD4(ponto1, ponto2)
distanciaD8(ponto1, ponto2)
