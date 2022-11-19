
# pip install pillow

from PIL import Image

#carrega a imagem
img = Image.open(r".\img.jpg")

#converte para preto e branco
img  = img.convert("L")

#salva a imagem
img.save(r".\img2.jpg")

#mostra a imagem
img.show()

