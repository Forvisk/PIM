import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
from random import randint

def conut_area_conexa(image_name_in,image_name_out):
	imagem = scipy.misc.imread(image_name_in)
	Altura,Largura,asd = imagem.shape
	
	data_mirror = []
	data_mirror_aux = []
	data_line = []

	for i in range(0,Altura+2):
		data_line += [0]
	data_mirror = [data_line]
	for i in range(0,Altura):
		data_mirror_aux = [0]
		for j in range(0,Largura):
			if(imagem[i][j][0]==0):
				data_mirror_aux += [1]
			else:
				data_mirror_aux += [0]
		data_mirror_aux += [0]
		data_mirror += [data_mirror_aux]
	data_mirror += [data_line]

	count = 0;

	for i in range(1,Altura+1):
		for j in range(1,Largura+1):
			if(data_mirror[i][j]!=0):
				if(data_mirror[i-1][j]!=0): #cima
					data_mirror[i][j] = data_mirror[i-1][j]
				elif(data_mirror[i-1][j-1]!=0): #diagonal superior equerda
					data_mirror[i][j] = data_mirror[i-1][j-1]
				elif(data_mirror[i][j-1]!=0): #erqueda
					data_mirror[i][j] = data_mirror[i][j-1]
				else:
					count = count+1
					data_mirror[i][j] = count;

	troca = True
	while troca:
		troca = False
		for i in range(1,Altura+1):
			for j in range(1,Largura+1):
				if(data_mirror[i][j]!=0):
					if(data_mirror[i][j]!=data_mirror[i-1][j] and data_mirror[i-1][j]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i+1][j],Altura,Largura)
						troca = True
					if(data_mirror[i][j]!=data_mirror[i+1][j] and data_mirror[i+1][j]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i-1][j],Altura,Largura)
						troca = True
					if(data_mirror[i][j]!=data_mirror[i][j-1] and data_mirror[i][j-1]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i][j-1],Altura,Largura)
						troca = True
					if(data_mirror[i][j]!=data_mirror[i][j+1] and data_mirror[i][j+1]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i][j+1],Altura,Largura)
						troca = True
					if(data_mirror[i][j]!=data_mirror[i-1][j-1] and data_mirror[i-1][j-1]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i-1][j-1],Altura,Largura)
						troca = True
					if(data_mirror[i][j]!=data_mirror[i-1][j+1] and data_mirror[i-1][j+1]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i-1][j+1],Altura,Largura)
						troca = True
					if(data_mirror[i][j]!=data_mirror[i+1][j+1] and data_mirror[i+1][j+1]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i+1][j+1],Altura,Largura)
						troca = True
					if(data_mirror[i][j]!=data_mirror[i+1][j-1] and data_mirror[i+1][j-1]!=0):
						data_mirror = une(data_mirror,data_mirror[i][j],data_mirror[i+1][j-1],Altura,Largura)
						troca = True
	hash_aux = cont_distincts_number(data_mirror,Altura,Largura)

	data = []
	for i in range(1,Altura+1):
		data_aux = []
		for j in range(1,Largura+1):
			data_aux += [hash_aux[data_mirror[i][j]]]
		data += [data_aux]
	scipy.misc.imsave(image_name_out,data)

	return len(hash_aux)-1

def cont_distincts_number(data,alt,lar):
	ret = {}
	ret.update({0: [255,255,255,255] })
	for i in range(1,alt+1):
		for j in range(1,lar+1):
			if(ret.has_key(data[i][j])==False):
				ret.update({data[i][j]: [randint(0,255),randint(0,255),randint(0,255),255] })
	return ret

def une(data,pri,seg,alt,lar):
	for i in range(1,alt+1):
		for j in range(1,lar+1):
			if(data[i][j]==seg):
				data[i][j] = pri;
	return data;

def count_pixel_estancao_de_borda(image_name_in,image_name_out):
	imagem = scipy.misc.imread(image_name_in)
	Altura,Largura,asd = imagem.shape
	count = 0;
	data = []
	data_aux = []
	data_line = []
	for i in range(0,Altura+2):
		data_line += [[255,255,255,255]]
	data += [data_line]
	for i in range(0,Altura):
		data_aux = [[255,255,255,255]]
		for j in range(0,Largura):
			data_aux += [imagem[i][j]]
		data_aux += [[255,255,255,255]]
		data += [data_aux]
	data += [data_line]

	data_out = []
	data_out_aux = []
	for i in range(1,Altura+1):
		data_out_aux = []
		for j in range(1,Largura+1):
			isolado = False
			if(data[i][j][0]==0):
				isolado = True
				if(data[i-1][j][0]!=0 or data[i+1][j][0]!=0 or data[i][j-1][0]!=0 or data[i][j+1][0]!=0):
					isolado = False
			if(isolado):
				count += 1
				data_out_aux += [[255,0,0,255]]
			else:
				data_out_aux += [data[i][j]]
		data_out += [data_out_aux]
	scipy.misc.imsave(image_name_out,data_out)

# count_pixel_estancao_de_borda("entrada.png","saida_interpolacao.png")
print(conut_area_conexa("entrada.png","saida_conectividade.png"))
resultado = scipy.misc.imread("saida_conectividade.png")
plt.imshow(resultado)
plt.show()