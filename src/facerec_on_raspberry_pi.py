#!~/Documents/welcome-device/venv/bin python3
import face_recognition
from os import listdir
from configparser import ConfigParser
from numpy import (uint8, empty)
from PIL import Image
from time import sleep
from text_to_speech import label_to_speech 
from capture_photos import Camera

class FaceRec:
    def __init__(self):
        parser = ConfigParser()
        parser.read("config.txt")
        self.cam = Camera()
        self.output = empty((parser.getint('camera', 'width'), parser.getint('camera', 'height'), 3), dtype=uint8)
        self.data_path = parser.get('data paths', 'train')
        self.encoding_list = []
        self.face_locations = []
        self.face_encodings = []
        self.train_filenames = [] #loaded images to be matched

    def load_images(self):
        # Load a sample picture and learn how to recognize it.
        print("Loading known face image(s)")
        self.train_filenames = listdir(self.data_path)
        for file_num, file_ in enumerate(self.train_filenames):
            print("Loading {} of {} images".format(file_num +1, len(self.train_filenames)))
            reference_image = face_recognition.load_image_file(self.data_path+file_)
            reference_encoding = face_recognition.face_encodings(reference_image)[0]
            self.encoding_list.append(reference_encoding)

    def run_face_rec(self):
        while True:
            print("Capturing image.")
            # Grab a single frame of video from the RPi camera as a numpy array
            self.cam.capture_memory(self.output, 'rgb')
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(self.output)
            print("Found {} faces in image.".format(len(self.face_locations)))
            self.face_encodings = face_recognition.face_encodings(self.output, self.face_locations)
            
            if len(self.face_locations)>0:
                # Loop over each face found in the frame to see if it's someone we know.
                for face_encoding in self.face_encodings:
	            # See if the face is a match for the known face(s)
                    name = "<Unknown Person>"
                    match = face_recognition.compare_faces(self.encoding_list, face_encoding)
                    if sum(match)>0:
                        name = self.train_filenames[match.index(True)].split('.')[0]
                print("I see someone named {}!".format(name))
                label_to_speech(name)
            else:
                print("No face identified")
            sleep(2)
