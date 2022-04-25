#!~/Documents/welcome-device/venv/bin python3

from capture_photos import Camera
from configparser import ConfigParser
from facerec_on_raspberry_pi import FaceRec

def main():
    print("In")
    type_in = input('Press 1 to add photo set or 2 run application\n')
    type_in = str(type_in)
    if type_in == '1':
        path_index = input('Options:\n1 to add to train\n2 add to test set\n3 add to prediction set\n')
        name_input = input('Define Suffix for image names\n')
        cm.capture_set(path_dic[path_index], name_input)
    elif type_in == '2':
        face_app = FaceRec()
        face_app.load_images()
        face_app.run_face_rec()
    else:
        print('You had one chance...')

if __name__ == "main":
    main()
else:
    print("Not main")
    main()



