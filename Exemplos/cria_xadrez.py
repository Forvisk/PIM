import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"


def GeraTabuleiro(W, H, T, filename):
	tabuleiro = []
	for i in range(0, H):
		linha = []
		for j in range(0, W):
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
	scipy.misc.imsave(path+filename,tabuleiro)

#____________________

def criarLinhas(W, H, T, filename):
	tabuleiro = []
	k = 0
	for i in range(0, H):
		linha = []
		for j in range(0, W):
			ponto = 0
			if( k == 0):
				ponto = 255
			else:
				ponto = 0
			linha.append([ponto, ponto, ponto])
		if k == 0:
			k = 1
		else:
			k = 0
		tabuleiro.append(linha)		
	scipy.misc.imsave(path+filename,tabuleiro)

#____________________


GeraTabuleiro(256, 256, 4, "Xadrez.png")

resultado = scipy.misc.imread(path+"Xadrez.png")
plt.imshow(resultado)
plt.show()

criarLinhas(512, 512, 4, "linhas_aa.png")
