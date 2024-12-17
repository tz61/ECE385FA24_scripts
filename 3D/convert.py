from math import *
from PIL import Image
def createTestImage(filename):
    # create a image containing 10 sectors
    # each sector with leading byte as their sector number (0-9)
    # and the rest of bytes within each sector are 0 to 510
    
    # create a file with 10 sectors
    f = open(filename+".img", "wb")
    im = Image.open(filename)
    width = 640
    height = 480
    for i in range(height):
        for j in range(width):
            r, g, b = im.getpixel((j, i))
            f.write((0).to_bytes(1, byteorder='big'))
            f.write((b).to_bytes(1, byteorder='big'))
            f.write((g).to_bytes(1, byteorder='big'))
            f.write((r).to_bytes(1, byteorder='big')) # red is MS byte in a single word
            # print("0x%02x%02x%02x00" % (r, g, b))
    f.close()
# 10863 frames
# 10863*2400 sectors= 12.43GiB= 26071200 sectors
# enumerate all bmp files in the current directory
import os
for filename in os.listdir("."):
    if filename.endswith(".bmp"):
        createTestImage(filename)