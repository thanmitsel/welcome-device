#!~/Documents/welcome-device/venv/bin python3

from configparser import ConfigParser
from picamera import PiCamera
from time import sleep
import sys
import time

class Camera:
    def __init__(self):
        parser = ConfigParser()
        parser.read("config.txt")
        
        self.cam = PiCamera()
        self.cam.rotation = parser.getint('camera','rotation')
        self.cam.resolution = (parser.getint('camera', 'height'), parser.getint('camera', 'width'),) # min 64 X 64
        # self.camera.framerate = parser.getint('camera','framerate')
        self.path = parser.get('data paths','train')
        
    def start_preview(self):
        self.cam.start_preview(alpha=200)

    def end_preview(self):
        self.cam.stop_preview()
 
    def capture_store(self, apath):
        self.cam.capture(apath)

    def capture_memory(self, output_, format_='rgb'):
        self.cam.capture(output_, format = format_)

    def capture_set(self, apath, name):
        self.start_preview()
        for i in range(20):
            self.count_down(3)
            ts = str(time.time())+'.'+str(i)
            self.capture_store(apath+'{}_{}.jpg'.format(name, ts))
            print('Image captured..')
        self.end_preview()

    def count_down(self, sec):
        for i in range(sec, 0, -1):
            sys.stdout.write('\r{0}'.format(i))
            sys.stdout.flush()
            sleep(1)
