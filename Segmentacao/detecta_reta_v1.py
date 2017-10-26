import numpy as np
import scipy.misc as scpm

path = "imagens/"
pathnew = "imagens/aut/"
pathtemp = "imagens/temp/"


def detecta_reta( input, ext, hlp):
	inimg = scpm.imread(p + input + ext)
	size = inimg.shape

	outimg = []
	if len(size) == 2:
		outimg = unidim( inimg, size, mascara, Tresh, hlp)
	if len(size) == 3:
		outimg = rgbfim( inimg, size, mascara, Tresh, hlp)
		
	output = input + "_p1_retas" + hlp + ".png"
	scpm.imsave(pathtemp + output, outimg)
	return output
	
input = ""
ext = ""
print detecta_reta( input, ext, "00")
