from PIL import Image
im = Image.open('img.png')

pixels = list(im.getdata())
print(pixels[0])
im2 = Image.new(im.mode, im.size)
pixels.sort()
im2.putdata(pixels)

im2.save('out.bmp')
