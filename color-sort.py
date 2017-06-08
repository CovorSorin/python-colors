from PIL import Image
import colorsys    
import math
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

# simple sort
colors.sort()

# hsv sort	
colors.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))

# hsl sort
colours.sort(key=lambda rgb: colorsys.rgb_to_hls(*rgb))

# luminosity sorting
def lum (r,g,b):
	return math.sqrt( .241 * r + .691 * g + .068 * b )
colors.sort(key=lambda rgb: lum(*rgb))

im = Image.new("RGB", (length, 1))
im.putdata(colors)
size = (length, 20)
im = im.resize(size)
im.save('output2.bmp')
