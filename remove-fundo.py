
from rembg import remove
from PIL import Image

#carrega a imagem
img = Image.open('t-img.jpg')

# remove o fundo
img_without_bg = remove(img)

#salva a imagem
img_without_bg.save('img_without_bg.png')

#mostra a imagem
img_without_bg.show()