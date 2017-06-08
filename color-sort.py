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
colors.sort(key=lambda rgb: colorsys.rgb_to_hls(*rgb))

# luminosity sort
def lum (r,g,b):
    return math.sqrt(.241 * r + .691 * g + .068 * b)
colors.sort(key=lambda rgb: lum(*rgb))

# step sort 1
def step (rgb, repetitions=1):
    r,g,b = rgb
    lum = math.sqrt(.241 * r + .691 * g + .068 * b)

    h, s, v = colorsys.rgb_to_hsv(r,g,b)
    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)

    return (h2, lum, v2)
colors.sort(key=lambda rgb: step(rgb,8))

# step sort 2
def step (rgb, repetitions=1):
    r,g,b = rgb
    lum = math.sqrt(.241 * r + .691 * g + .068 * b)

    h, s, v = colorsys.rgb_to_hsv(r,g,b)

    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)

    if h2 % 2 == 1:
            v2 = repetitions - v2
            lum = repetitions - lum

    return (h2, lum, v2)
colors.sort(key=lambda rgb: step(rgb,8))

im = Image.new("RGB", (length, 1))
im.putdata(colors)
size = (length, 20)
im = im.resize(size)
im.save('output2.bmp')
