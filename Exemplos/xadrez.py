import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"


def GeraTabuleiro(W, H, T, filename):
	tabuleiro = []
	for i = 0 in range(0, H):
		linha = []
		for j = 0 in range(0, W):
			ponto = 0
			if ( j/T % 2 == 0):
				if( i/T % 2 == 0):
					ponto = 255
				else:
					ponto = 0
			else:
				if( i/T % 2 == 0):
					ponto = 0
				else:
					ponto = 255
			linha.append([ponto, ponto, ponto])
		tabuleiro.append(linha)		
	scipy.misc.imsave(path+filename,data)

#____________________

GeraTabuleiro(256, 256, 4, "Xadrez.png")

resultado = scipy.misc.imread(path+"Xadrez.png")
plt.imshow(resultado)
plt.show()
