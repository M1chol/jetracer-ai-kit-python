from camera import CameraJet
from time import sleep
from multiprocessing import Process
import cv2
import os

os.system("rm -r zdj")
os.system("mkdir zdj")

cam = CameraJet()

licznik = 0
while True:
    znak = cv2.waitKey(1)
    frame = cam.read_frame()
    cv2.imshow("podglad", frame)
    if znak == ord("q"):
        break
    if znak == ord("p"):
        with open(f"zdj/zdj{licznik}.jpg", "wb") as file:
            file.write(cam.read_frame_jpg())
        licznik += 1
        print(licznik)