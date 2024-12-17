# input: dest.mp4 30fps
# slice it to frames (bmp)
# 6*60*30*2400*512/1024/1024/1024 = 12.35 GiB

ffmpeg -i dest.mp4 -vf fps=30 frame%04d.bmp
python convert.py