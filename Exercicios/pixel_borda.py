import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"

def detectaBorda( input, output):

 	imagemIN = scipy.misc.imread( input)
	W, H, P = imagemIN.shape
	data = []
	for i in range(0, W):
		row = []
		for j in range(0,H):
			bS = 0
			bE = 0
			bD = 0
			bI = 0
			ok = 0
			pixel = imagemIN[i][j]
			if imagemIN[i][j][1] == 0:			
				ok = 0
				if (i - 1 < 0):
					bS = 1
				if (j - 1 < 0):
					bE = 1
				if (j + 1 >= H):
					bD = 1
				if (i + 1 >= W):
					bI = 1
				
				if not bS:
					if imagemIN[i-1][j][1] != 0:
						ok = 1
					#if not bE:
					#	if imagemIN[i-1][j-1][1] != 0:
					#		ok = 1
					#if not bD:
					#	if imagemIN[i-1][j+1][1] != 0:
					#		ok = 1
				else:
					ok = 1

				if not bI:
					if imagemIN[i+1][j][1] != 0:
						ok = 1
					#if not bE:
					#	if imagemIN[i+1][j-1][1] != 0:
					#		ok = 1
					#if not bD:
					#	if imagemIN[i+1][j+1][1] != 0:
					#		ok = 1
				else:
					ok = 1

				if not bE:
					if imagemIN[i][j-1][1] != 0:
						ok = 1
				else:
					ok = 1

				if not bD:
					if imagemIN[i][j+1][1] != 0:
						ok = 1
				else:
					ok = 1

				if ok == 1:
					row.append([0,0,0])
				else:	
					row.append([100, 100, 100])

			else:
				row.append([255,255,255])

		data.append(row)

	scipy.misc.imsave(output,data)
# =================

image = path + "Xadrez.png"
out = path+"xadrez_borda.png"
detectaBorda( image, out)

resultado = scipy.misc.imread(out)
plt.imshow(resultado)
plt.show()
	
