from convert import imageToText
import os
import random
import string
import cv2
import time


def checkKey(key):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        raise Exception("Camera not accessible")

    time.sleep(1)
    text = ""

    try:
        while key not in text:
            valid, image = cam.read()
            if valid:
                tempFileName = ''.join(random.choices(string.ascii_letters, k=8))+'.png'
                cv2.imwrite(f'{tempFileName}', image)
                text = imageToText(f'{tempFileName}')
                os.remove(f'{tempFileName}')
                time.sleep(0.1)
    finally:
        cam.release()


    return f"\033[1;32mKey Accepted:\033[0m\n{text}"



print(checkKey("Hello"))
