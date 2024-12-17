# read pcm file and generate sound (left channel and right channel)
# test file is touhou.pcm, extract left channel and generate c code
# it is a pcm u16le file generated with
# ffmpeg -i touhou.flac -f u16le -acodec pcm_u16le -ac 2 -ar 44100 touhou_u16le.pcm
import numpy as np

def generate_sound(filename):
    # read pcm file
    pcmfile = open(filename, "rb")
    pcmdata = pcmfile.read()
    pcmfile.close()

    # extract left channel
    data = np.frombuffer(pcmdata, dtype=np.uint32)
    magic_word_count = 32 # 16 is enough but to prevent misread by sdcard, or maybe bigger e.g. 64
    magic = 0x00110045 # magic number to stop song(append it to the end of song, total not exceeding 5 min)
    sample_points = data.shape[0]
    # show waveform in seperate subplots (upper is right channel(16bit unsigned), lower is left channel(16bit unsigned))
    f = open(filename + ".img", "wb")
    # add 0.005s transition 220 samples
    # store left channel in high 16 bits, right channel in low 16 bits
    for i in range(sample_points):# 2048 is burst byte size for AXI module
        if ( i<220):
            factor = int(16*(1-i / 220))
        elif (i>sample_points-220):
            factor = int(16*(1-(sample_points-i) / 220))
        else:
            factor = 0
        f.write((int(int(data[i]>>16)&0xffff)>>factor).to_bytes(2, byteorder='little'))
        f.write((int(int(data[i])&0xffff)>>factor).to_bytes(2, byteorder='little'))
    for i in range(magic_word_count-1):
        f.write(magic.to_bytes(4, byteorder='little'))
    f.close()

if __name__ == "__main__":
    # get files with extension .pcm
    import glob
    files = glob.glob("*.pcm")
    for file in files:
        generate_sound(file)
    