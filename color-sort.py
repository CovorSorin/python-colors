from PIL import Image
import random
from random import randint

#im = Image.open('img.jpg')
#pixels = list(im.getdata())

length = 1000
colors = []

for i in range(1, length):
    colors.append (
        (
    	    randint(0, 255),
            randint(0, 255),
            randint(0, 255)
    	)
    )

colors.sort()
im = Image.new("RGB", (length, 1))
im.putdata(colors)
size = (length, 20)
im = im.resize(size)
im.save('output.bmp')
