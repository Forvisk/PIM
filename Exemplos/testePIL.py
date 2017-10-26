from PIL import Image
path = "imagens/"
image = Image.open(path+'python.png')
image.show()
x = 15
y = 14
r,g,b = image.getpixel( (x,y) )
print [r, g, b]
image.save(path+'saida.png')