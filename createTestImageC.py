# open file Start.png, and get its rgb 888 color tuple


from PIL import Image

im = Image.open("ZJU.png")
width = im.width #640
height = im.height #480
print("#include <stdint.h>")
print("uint32_t ZJU[480*640] = {")
for i in range(height):
    for j in range(width):
        r, g, b = im.getpixel((j, i))
        print("0x%02x%02x%02x00" % (r, g, b))
        if i != height - 1 or j != width - 1:
            print(", ", end="")
    
print("};")
        
