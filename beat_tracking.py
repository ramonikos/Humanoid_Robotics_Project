# import modules
import librosa
from playsound import playsound
import soundfile as sf
import sounddevice as sd
import IPython.display as ipd
import numpy as np

# read audio file 
x, sr = librosa.load('baby_shark_50s.wav')
# stream audio from microphone

#ipd.Audio(x, rate=sr)
print("sr", sr)
onset_env = librosa.onset.onset_strength(x, sr=sr, aggregate=np.median)
tempo, beat_times = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
#tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=60, units='time')

print("tempo: ", tempo)

clicks = librosa.clicks(beat_times, sr=sr, length=len(x))
#ipd.Audio(x + clicks, rate=sr)
#sf.write("new_Wave.wav", x+clicks, sr)

#playsound("new_Wave.wav")