from camera import CameraJet
from lidar import LidarJet
from robotcar import CarJet
from multiprocessing import Process
from time import sleep

def lid_proc():
    lid = LidarJet('/dev/ttyACM1')
    lid.start_scan()

def cam_proc():
    cam = CameraJet()
    cam.show_stream()

def car_proc():
    car = CarJet()
    car = car.start_steering()

if __name__ == "__main__":
    lid_proc = Process(target=lid_proc)
    cam_proc = Process(target=cam_proc)
    car_proc = Process(target=car_proc)

    lid_proc.start()
    cam_proc.start()
    car_proc.start()