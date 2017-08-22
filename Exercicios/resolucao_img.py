
import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"

def GeraNivel(input , T, output):
	imagemIN = scipy.misc.imread(input)
	W,H = imagemIN.shape
	data = []
	for i in range(0,H,T):
		row = []
		if i+T <= H:
			for j in range(0,W,T):
				lvl = 0
				c = 0
				for i1 in range(i, i+T):
					if j+T <= W:
						for j1 in range(j, j+T):
								lvl = lvl + imagemIN[i][j]
								c += 1
					else:
						for j1 in range(j, W):
								lvl = lvl + imagemIN[i][j]
								c += 1
				lvl = lvl // c
				row.append([ lvl , lvl , lvl ])
		else:
			for j in range(0,W,T):
				lvl = 0
				c = 0
				for i1 in range(i, i+T):
					if j+T <= W:
						for j1 in range(j, j+T):
								lvl = lvl + imagemIN[i][j]
								c += 1
					else:
						for j1 in range(j, W):	
								lvl = lvl + imagemIN[i][j]
								c += 1
				lvl = lvl // c
				row.append([ lvl , lvl , lvl ])
		data.append(row)

	scipy .misc.imsave(output,data)
# ================================================================================

input = path + "lena.jpg"
output = path + "piramide.png"

GeraNivel(input , 4, output)

resultado = scipy .misc.imread(output)
plt .imshow(resultado)
plt .show()