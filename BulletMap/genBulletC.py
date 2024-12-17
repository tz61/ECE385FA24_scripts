# open file Start.png, and get its rgb 888 color tuple


from PIL import Image

im_content = Image.open("Bullets.bmp")
im_detect = Image.open("Bullets_det.bmp")
width = im_content.width  # 256
height = im_content.height  # 128
print("width: %d, height: %d" % (width, height))
f = open("Bullets.c", "w")
fb = open("Bullets.img", "wb")
f.write("#include <stdint.h>\n")
f.write("uint16_t Bullet_sprite[128*256] = {")
for i in range(height):
    for j in range(width):
        r, g, b = im_content.getpixel((j, i))
        r_d, g_d, b_d = im_detect.getpixel((j, i))
        # RGB 555+ 1 bit detect, if pixel in im_detect==0,0,0(black), then set the LSB to 1
        det = 0
        if r_d == 0 and g_d == 0 and b_d == 0:
            det = 1
        dest_col = (r >> 3) << 11 | (g >> 3) << 6 | (b >> 3) << 1 | det
        if(i == 8 and j == 8):
            print(hex(dest_col))
        f.write("0x%02x%02x" % ((dest_col >> 8)& 0xff, dest_col & 0xff))
        fb.write(dest_col.to_bytes(2, byteorder='little'))
        if i != height - 1 or j != width - 1:
            f.write(", ")

f.write("};")
f.close()
