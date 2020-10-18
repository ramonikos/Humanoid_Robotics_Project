import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 50  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print(type(myrecording))
sd.wait()  # Wait until recording is finished
write('baby_shark_50s.wav', fs, myrecording)  # Save as WAV file 