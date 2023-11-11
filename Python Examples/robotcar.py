from time import sleep
import pygame
from nvidia_racecar import NvidiaRacecar

class CarJet():
    def __init__(self) -> None:  
        self.car = NvidiaRacecar()
        pygame.init()
        if pygame.joystick.get_count() < 1:
            raise RuntimeError("No controller detected")
        self.js = pygame.joystick.Joystick(0)
        name = self.js.get_name()
        self.js.init()
        print(f"connected to {name}")
        self.skret, self.silnik = 0, 0

    def start_steering(self):
        steer = True
        while True:
            while steer:
                for event in pygame.event.get():
                    skret = round(self.js.get_axis(0),1)
                    silnik = round(self.js.get_axis(3),1)*-1
                    if self.js.get_button(1) == 1:
                        print('Disabling controll')
                        steer = False
                self.car.steering = skret
                self.car.throttle = silnik
            
            for event in pygame.event.get():
                if self.js.get_button(0) == 1:
                        print('Enabling controll')
                        steer = True

if __name__=="__main__":
    car = CarJet()
    car.start_steering()