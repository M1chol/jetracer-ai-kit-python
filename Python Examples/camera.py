# MIT License
# Copyright (c) 2019-2022 JetsonHacks
# Modified by Michal Kozlowski

# Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
# NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image

import cv2

""" 
gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
Flip the image by setting the flip_method (most common values: 0 and 2)
display_width and display_height determine the size of each camera pane in the window on the screen
Default 1920x1080 displayd in a 1/4 size window
"""

class CameraJet():
    
    def __init__(self, flip=0) -> None:
        self.wasInit = False
        self.video_capture = cv2.VideoCapture(self.gstreamer_pipeline(flip), cv2.CAP_GSTREAMER)
        try:
            ret_val, frame = self.video_capture.read()
            if not ret_val:
                raise RuntimeError('Camera image is empty')
        except: raise RuntimeError(
                'Could not initialize camera. Please see error trace. Perhaps there is a second session running? try launching $ sudo service nvargus-daemon restart')
        self.wasInit=True

    @staticmethod
    def gstreamer_pipeline(
        sensor_id=0,
        capture_width=1920,
        capture_height=1080,
        display_width=960,
        display_height=540,
        framerate=30,
        flip_method=0,
    ) -> str:
        return (
            "nvarguscamerasrc sensor-id=%d ! "
            "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (
                sensor_id,
                capture_width,
                capture_height,
                framerate,
                flip_method,
                display_width,
                display_height,
            )
        )

    def read_frame(self):
        if not self.wasInit:
            print(Warning('Camera was not initialized properly, running auto init'))
            self.cam_init()
        if self.video_capture.isOpened(): ret_val, frame = self.video_capture.read()
        else:
            raise RuntimeError("Unable to open camera, Perhaps there is a second session running? try launching $ sudo service nvargus-daemon restart')")
        return frame
    
    def read_frame_jpg(self):
        frame = self.read_frame()
        return cv2.imencode('.JPEG', frame)

    def show_stream(self):
        while True:
            image = self.read_frame()
            cv2.imshow("frame", image)
            if cv2.waitKey(1) == ord('q'):
                break

if __name__ == "__main__":
    cam = CameraJet()
    cam.show_stream()