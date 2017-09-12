import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"

def trocaCor( imagem):
	imagemIN = scipy.misc.imread( imagem)
	W, H, P = imagemIN.shape
	
	for i in range(0, W):
		for j in range(0, H):
			if imagemIN[i][j][0] == 0:
				imagemIN[i][j][0] = 255
				imagemIN[i][j][1] = 0
				imagemIN[i][j][2] = 0
	
	out = path+"resp_ex1.png"
	scipy.misc.imsave( out, imagemIN)
	resultado = scipy.misc.imread(out)
	plt.imshow(resultado)
	plt.show()
	
imagem = path + "ex1.png"
trocaCor( imagem)


