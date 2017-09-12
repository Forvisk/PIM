import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"

def soma(imagem1, imagem2):
	im1 = scipy.misc.imread(imagem1)
	im2 = scipy.misc.imread(imagem2)
	im1Shape = im1.shape
	im2Shape = im2.shape
	print im1Shape
	print im2Shape
	if len(im1Shape) != len(im2Shape):
		print "Imagens binaria com rgb! Saindo"
		return
		
	
soma(path+"ex1.png", path+"python.png")
soma(path+"lena.jpg", path+"python.png")


