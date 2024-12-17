# 00000000 in file font_rom.txt
# and 16 lines for one character
# read and generate to c file array

import os
f = open("font_rom.txt", "r")
f_c = open("font_rom.c", "w")
f_c.write("#include <stdint.h>\n")
f_c.write("uint8_t font_rom[128*16] = {")
# LSB is the left most bit
for i in range(128):
    for j in range(16):
        tmp = 0
        line = f.readline()
        for k in range(8):
            if line[k] == '1':
                tmp=tmp+1*2**(k)
        f_c.write("0x%02x" % tmp)
        if i != 127 or j != 15:
            f_c.write(", ")
f_c.write("};")
f.close()
f_c.close()
