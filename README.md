# Humanoid_Robotics_Project
Project work for Humanoid Robotics Course (TIF160, 2020) in Chalmers

## How to install dependencies
The dependency of the Python packages is listed in requirements.txt. If pip can't install certain packages, try to use winpip.

## How to run
live_audio_stream.py is the script to listen to audio input from microphone and to calculte the tempo of the music. The output is a float number of the music tempo in unit BPM, beats per minutes.
Simply run the script using python live_audio_stream.py and then play some music using mobilephone.

## Script for testing and debugging
record_sound.py is to record music from microphone and save as wav file.
beat_tracking.py is to calculate the tempo of a wav file, and mix click sound in the input music so you can check if the calcuation is correct.