import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"

def Histograma(input):
	## gera o histograma e seus intervalos
	imagem = scipy.misc.imread(input)
	histogramas, intervalos = np.histogram(imagem, bins=np.arange(0,256))
	
	## determina o valor do centro dos intervalos
	center = ( intervalos[:-1] + intervalos[1:])/2
	
	##exibe histograma
	plt.bar(center, histogramas, align='center')
	plt.show()

imagem = path + "lena.jpg"
Histograma(imagem)

imagem = path + "mandril.jpg"
Histograma(imagem)
