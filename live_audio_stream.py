'''
https://blog.francoismaillet.com/epic-celebration/
'''
import pyaudio
import librosa
import numpy as np
import requests
from RingBuffer import RingBuffer
import sounddevice as sd
from time import sleep
import time
import serial
# ring buffer will keep the last 2 seconds worth of audio
ringBuffer = RingBuffer(5 * 22050)
arduinodata=serial.Serial('com4',9600,timeout=(1))
tempo=0
def callback(in_data, frame_count, time_info, flag):
    audio_data = np.frombuffer(in_data, dtype=np.float32)
    
    # we trained on audio with a sample rate of 22050 so we need to convert it
    audio_data = librosa.resample(audio_data, 44100, 22050)
    ringBuffer.extend(audio_data)
    # analysis beat
    #print(audio_data)
    onset_env = librosa.onset.onset_strength(ringBuffer.get(), sr=22050, aggregate=np.median)
    tempo, beat_times = librosa.beat.beat_track(onset_envelope=onset_env, sr=22050)
    #tempo = librosa.beat.tempo(ringBuffer.get(), sr=22050, start_bpm=60)
    print("tempo: ", tempo)
    arduinodata.reset_input_buffer()
    arduinodata.reset_output_buffer()
    if tempo<90:
        arduinodata.write(b'a')
    elif tempo<121:
        arduinodata.write(b'b')
    elif tempo<160:
        arduinodata.write(b'c')
    else:
        arduinodata.write(b'd')
    # arduinodata.write(int(tempo))
    time.sleep(3)
    return (in_data, pyaudio.paContinue)

# function that finds the index of the Soundflower
# input device and HDMI output device
#dev_indexes = findAudioDevices()

pa = pyaudio.PyAudio()
for i in range(0, pa.get_device_count()):
    print(i, pa.get_device_info_by_index(i)['name'])

stream = pa.open(format = pyaudio.paFloat32,
                 channels = 1,
                 rate = 44100,
                 output = False,
                 input = True,
                 frames_per_buffer=1024,
                 input_device_index = 1,
                 stream_callback = callback)

# start the stream
stream.start_stream()

while stream.is_active():
    sleep(0.25)
    arduinodata.write(int(tempo))

stream.close()
pa.terminate()
