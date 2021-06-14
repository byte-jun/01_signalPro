# -*- coding: utf-8 -*-
import pyaudio
import wave

chunk = 1024

wf = wave.open(r"C:\Users\JUNJUN-HUANG\OneDrive\Matlab\matlab\三种数据格式ame asd wav\1106020025_0053064_6840_20210422153903_53081_8DT80MO_ROH_GE_GB_7_7_#3_#3.wav", 'rb')

p = pyaudio.PyAudio()

# 打开声音输出流
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# 写声音输出流进行播放
while True:
    data = wf.readframes(chunk)
    if data == "": break
    stream.write(data)

stream.close()
p.terminate()