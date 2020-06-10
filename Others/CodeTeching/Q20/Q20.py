# Carrey Wong
# 2020 05 27

from PIL import Image

im = Image.open("test.png")
rgb_im = im.convert('RGB')
rgb_im.save('test.jpg')