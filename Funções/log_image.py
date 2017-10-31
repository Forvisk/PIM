import numpy as np
import scipy.misc as scpm

path = "imagens/"

def log( input):
	original = scpm.imread("imagens/teste_11.jpg")
	a = 255.0/np.log( 256 ) #fmax+1=255+1
	transformada = np.log( original ) * a
	scpm.imsave("imagens/teste_11_log.jpg", transformada)



log("")
inp = "teste_11.jpg"
log( path+inp)
#quadrado(path+inp)

