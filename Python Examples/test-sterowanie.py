from time import sleep
import pygame
from nvidia_racecar import NvidiaRacecar

car = NvidiaRacecar()
pygame.init()

while True:
    if pygame.joystick.get_count() > 0:
        break   
    print("No controller detected")
    sleep(0.5)

print(f"Found {pygame.joystick.get_count()} joystick")
js = pygame.joystick.Joystick(0)
name = js.get_name()
js.init()
print(f"connected to {name}")

car = NvidiaRacecar()
skret, silnik = 0, 0
loop = True
while loop:
    for event in pygame.event.get():
        skret = round(js.get_axis(0),1)
        silnik = round(js.get_axis(3),1)*-1
        if js.get_button(1) == 1:
            print('STOP')
            loop = False
    car.steering = skret
    car.throttle = silnik