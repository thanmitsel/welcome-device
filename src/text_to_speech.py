#!~/Documents/welcome-device/venv/bin python3
import os

def label_to_speech(name):
    os.system('echo "Welcome {}"| festival --tts'.format(name))
