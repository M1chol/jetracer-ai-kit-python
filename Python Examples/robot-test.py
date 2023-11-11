from camera import CameraJet
from lidar import LidarJet
from robotcar import CarJet
from threading import Thread
from time import sleep

#cam = CameraJet()
lid = LidarJet('/dev/ttyACM1')
car = CarJet()


#t1 = Thread(target=cam.show_stream)
t2 = Thread(target=lid.start_scan)
t3 = Thread(target=car.start_steering)

#t1.start()
t2.start()
t3.start()

#print("Waiting 10 sec...")
#sleep(10)

#car.start_steering()