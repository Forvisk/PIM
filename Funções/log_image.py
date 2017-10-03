import numpy as np
import scipy.misc as scpm

path = "imagens/"

def log( input):
	original = scpm.imread("imagens/lena.jpg")
	a = 255.0/np.log( 256 ) #fmax+1=255+1
	transformada = np.log( original ) * a
	scpm.imsave("imagens/lena_log.jpg", transformada)



log("")
inp = "lena.jpg"
log( path+inp)
#quadrado(path+inp)

