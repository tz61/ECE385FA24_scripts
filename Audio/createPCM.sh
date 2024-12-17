#!/bin/sh
for i in `ls *.flac`
do
    ffmpeg -i $i -f u16le -acodec pcm_u16le -ac 2 -ar 44100 $i.pcm -y
done
for i in `ls *.wav`
do
    ffmpeg -i $i -f u16le -acodec pcm_u16le -ac 2 -ar 44100 $i.pcm -y
done
python3 createSingleImage.py
# start at 0x814B0000 end at 0x8f2bfa80-1, so size 232848000 Bytes
# bgm size: 52920000 Bytes
# sfx size:  1764000 Bytes
rm -f audioImage.img
touch audioImage.img
# dd if=/dev/zero of=audioImage.img bs=1c count=232848000c
# dd if=BGM0_TITLE.flac.pcm.img of=audioImage.img bs=512 seek=0c 
dd if=BGM0_TITLE_WITHERED_LEAF.flac.pcm.img of=audioImage.img bs=512 seek=0c 
dd if=BGM1_Stage6_path.flac.pcm.img of=audioImage.img bs=64c seek=826875
dd if=BGM2_Stage6_boss_short.flac.pcm.img of=audioImage.img bs=64c seek=1653750
dd if=BGM3_PlayerScore.flac.pcm.img of=audioImage.img bs=64c seek=2480625
dd if=SFX0_MENU_CANCEL.wav.pcm.img of=audioImage.img bs=1c seek=211680000c
dd if=SFX1_MENU_PAUSE.wav.pcm.img of=audioImage.img bs=1c seek=213444000c
dd if=SFX2_MENU_OK.wav.pcm.img of=audioImage.img bs=1c seek=215208000c
dd if=SFX3_PL_DEAD.wav.pcm.img of=audioImage.img bs=1c seek=216972000c
dd if=SFX4_PL_SHOOT.wav.pcm.img of=audioImage.img bs=1c seek=218736000c
dd if=SFX5_PL_GRAZE.wav.pcm.img of=audioImage.img bs=1c seek=220500000c
dd if=SFX6_PL_EXTEND.wav.pcm.img of=audioImage.img bs=1c seek=222264000c
dd if=SFX7_PL_CARDGET.wav.pcm.img of=audioImage.img bs=1c seek=224028000c
dd if=SFX8_PL_POWERUP.wav.pcm.img of=audioImage.img bs=1c seek=225792000c
dd if=SFX9_PL_CH.wav.pcm.img of=audioImage.img bs=1c seek=227556000c
dd if=SFX10_ENEMY_LAZER.wav.pcm.img of=audioImage.img bs=1c seek=229320000c
dd if=SFX11_ENEMY_TAN.wav.pcm.img of=audioImage.img bs=1c seek=231084000c
dd if=SFX12_ENEMY_BIG.wav.pcm.img of=audioImage.img bs=1c seek=232848000c
dd if=SFX13_ENEMY_DEAD.wav.pcm.img of=audioImage.img bs=1c seek=234612000c
dd if=SFX14_ENEMY_TIMEOUT.wav.pcm.img of=audioImage.img bs=1c seek=236376000c
dd if=SFX15_CARD_ISSUE.wav.pcm.img of=audioImage.img bs=1c seek=238140000c
sync