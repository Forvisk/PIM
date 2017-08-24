import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"

def DetectaPixel( input, output):
	imagemIN = scipy.misc.imread( input)
	W, H, P = imagemIN.shape
	bS = 0
	bE = 0
	bD = 0
	bI = 0
	ok = 0
	count = 0
	countIso = 0
	countGru = 0
	for i in range( 0, W):
		for j in range( 0, H):
			bS = 0
			bE = 0
			bD = 0
			bI = 0
			ok = 0
			if imagemIN[i][j][1] == 0:
				count += 1
				if (i - 1 < 0):
					bS = 1
				if (j-1 < 0):
					bE = 1
				if (j + 1 >= H):
					bD = 1
				if (i + 1 >= W):
					bI = 1
				
				if bS == 0:
					if imagemIN[i-1][j][1] == 0:
						#count += 1
						ok = 1
					if bE == 0:
						if imagemIN[i-1][j-1][1] == 0:
							#count += 1
							ok = 1
					if bD == 0:
						if imagemIN[i-1][j+1][1] == 0:
							#count += 1
							ok = 1
				if not bI:
					if imagemIN[i+1][j][1] == 0:
						#count += 1
						ok = 1
					if not bE:
						if imagemIN[i+1][j-1][1] == 0:
							#count += 1
							ok = 1
					if not bD:
						if imagemIN[i+1][j+1][1] == 0:
							#count += 1
							ok = 1
				if not bE:
					if imagemIN[i][j-1][1] == 1:
						#count += 1
						ok = 1
				if not bD:
					if imagemIN[i][j+1][1] == 1:
						#count += 1
						ok = 1
				if ok != 1:
					countIso += 1
					imagemIN[i][j] = [255, 0, 255]
				else:
					countGru += 1


#	print imagemIN
	scipy.misc.imsave( output,imagemIN)
	print "Pixels: " + str(count)
	print "Pixels isolados: " + str(countIso)
	print "Pixels com vizinhos: " + str(countGru)


# =================

image = path + "pixel_lost.png"

DetectaPixel( image, path+"pixel_found.png")