#!/bin/sh
#(int("814B0000",16)-int("81000000",16))/512=9600 sector
#(int("90000000",16)-int("81000000",16))/512=491520 sector= 240MiB
rm -f disk.img
touch disk.img
#491520+524288 audio(volume1)+volume2
dd if=/dev/zero of=disk.img bs=512 count=1015808 
# FB0
dd if=NotUsed/Zuofu.png.img of=disk.img bs=512 seek=0
# FB0_ALT
dd if=NotUsed/ncm.png.img of=disk.img bs=512 seek=4800
# Audio
dd if=Audio/audioImage.img of=disk.img bs=512 seek=9600
# 256MiB: volume2
dd if=/dev/urandom of=volume2.img bs=512 count=524288
dd if=volume2.img of=disk.img bs=512 seek=491520
# animation 26071200 sectors, 12.43GiB, 10863 frames, 10863*2400 sectors
# dd if=3D/animation.img of=disk.img bs=512 seek=1015808