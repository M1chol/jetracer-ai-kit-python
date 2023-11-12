import os
from math import cos, sin, pi, floor
from rplidar import RPLidar
import numpy as np
import cv2


class LidarJet():

    def __init__(self, port, show_output=True) -> None:
        self.SCREEN_W = 640
        self.SCREEN_H = 480
        self.show_output=show_output

        self.img = np.zeros((self.SCREEN_H, self.SCREEN_W, 1))
        self.img[:, :] = [255]

        # Setup the RPLidar
        self.lidar = RPLidar(port)
        self.lidar.clean_input()

        # used to scale data to fit on the screen
        self.max_distance = 0

        self.scan_data = [0]*360

    def process_data(self, data):
        self.img[:, :] = [255]
        for angle in range(360):
            distance = data[angle]
            if distance > 0:                    # ignore initially ungathered data points
                max_distance = 3000             #max([min([5000, distance]), max_distance])
                radians = angle * pi / 180.0 - pi/2
                x = distance * cos(radians)
                y = distance * sin(radians)
                point = (self.SCREEN_W//2 + int(x/max_distance*400), self.SCREEN_H//2 + int(y/max_distance*400))
                cv2.circle(self.img, point, 2, (0,0,0), 2)
        if self.show_output:
            cv2.imshow('Lidar', self.img)

    def read_frame_jpg(self):
        try:
            self.start_scan(oneScan=True)
            _, jpg_img = cv2.imencode('.jpg',self.img)
            return jpg_img.tobytes()
        except:
            pass

    def stop(self):
        print('Stoping...')
        self.lidar.stop()
        self.lidar.disconnect()
        quit()

    def start_scan(self, oneScan=False):
        self.lidar.clean_input()
        try:
            for scan in self.lidar.iter_scans():
                if cv2.waitKey(1) == 113:
                    self.stop()
                for (_, angle, distance) in scan:
                    self.scan_data[min([359, floor(angle)])] = distance
                self.process_data(self.scan_data)
                if oneScan:
                    break
        except KeyboardInterrupt:
            self.stop()

if __name__=="__main__":
    lidar = LidarJet('/dev/ttyACM1')
    lidar.start_scan()