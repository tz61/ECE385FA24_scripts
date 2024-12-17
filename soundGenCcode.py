# read pcm file and generate sound (left channel and right channel)
# test file is touhou.pcm, extract left channel and generate c code
# it is a pcm u16le file generated with
# ffmpeg -i touhou.flac -f u16le -acodec pcm_u16le -ac 2 -ar 44100 touhou_u16le.pcm
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

def generate_sound():
    # read pcm file
    pcmfile = open("tamaonsen_u16le.pcm", "rb")
    pcmdata = pcmfile.read()
    pcmfile.close()

    # extract left channel
    data = np.frombuffer(pcmdata, dtype=np.uint32)
    magic_word_count = 16
    magic = "0x00110045" # magic number to stop song(append it to the end of song, total not exceeding 5 min)
    sample_points = data.shape[0]
    # show waveform in seperate subplots (upper is right channel(16bit unsigned), lower is left channel(16bit unsigned))
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.title('Right Channel')
    plt.subplot(2, 1, 2)
    # override to test
    sample_points = 44100*10
    f = open("music.c", "w")
    f.write("#include <stdint.h>\n")
    f.write("uint32_t touhou_wav[%d]= {\n"%(sample_points+magic_word_count))
    
    # store left channel in high 16 bits, right channel in low 16 bits
    for i in range(sample_points):# 2048 is burst byte size for AXI module
        f.write("0x%04x%04x,"%(data[i]&0xffff, (data[i]>>16)&0xffff))
    for i in range(magic_word_count-1):
        f.write(magic + ",")
    f.write(magic + "};\n")
    f.close()

if __name__ == "__main__":
    generate_sound()
    