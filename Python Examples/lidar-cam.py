import os
from math import cos, sin, pi, floor
from rplidar import RPLidar
import camera
import numpy as np
import cv2
import threading

# Create camera thread
camera.init()
t1 = threading.Thread(target=camera.show)
t1.start()

SCREEN_W = 640
SCREEN_H = 480

frame = np.zeros((SCREEN_H, SCREEN_W, 1))
frame[:, :] = [255]

# Setup the RPLidar
PORT_NAME = '/dev/ttyACM1'
lidar = RPLidar(PORT_NAME)
lidar.clean_input()

# used to scale data to fit on the screen
max_distance = 0

#pylint: disable=redefined-outer-name,global-statement
def process_data(data):
    global max_distance
    frame[:, :] = [255]
    for angle in range(360):
        distance = data[angle]
        if distance > 0:                  # ignore initially ungathered data points
            max_distance = 3000 #max([min([5000, distance]), max_distance])
            radians = angle * pi / 180.0 - pi/2
            x = distance * cos(radians)
            y = distance * sin(radians)
            point = (SCREEN_W//2 + int(x/max_distance*400), SCREEN_H//2 + int(y/max_distance*400))
            cv2.circle(frame, point, 2, (0,0,0), 2)
    cv2.imshow('Lidar', frame)


scan_data = [0]*360
def stop():
    print('Stoping...')
    lidar.stop()
    lidar.disconnect()
    t1.join()
    quit()

try:
    for scan in lidar.iter_scans():
        if cv2.waitKey(1) == 113:
            stop()
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
        process_data(scan_data)
except KeyboardInterrupt:
    stop()