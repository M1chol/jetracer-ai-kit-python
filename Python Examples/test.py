from nvidia_racecar import NvidiaRacecar
from time import sleep
car = NvidiaRacecar()

for i in range(10):
    car.steering += 0.1
    sleep(0.2)
for i in range(20):
    car.steering -= 0.1
    sleep(0.2)
for i in range(10):
    car.steering += 0.1
    sleep(0.2)

car.throttle = 1
sleep(5)
car.throttle = 0