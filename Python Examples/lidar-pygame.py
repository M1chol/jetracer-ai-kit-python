import os
from math import cos, sin, pi, floor
import pygame
from rplidar import RPLidar
import camera

camera.init()
camera.show()

SCREEN_W = 640
SCREEN_H = 480

# Set up pygame and the display
#os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((SCREEN_W,SCREEN_H))
#pygame.mouse.set_visible(True)
lcd.fill((255,255,255))
pygame.display.update()

# Setup the RPLidar
PORT_NAME = '/dev/ttyACM1'
lidar = RPLidar(PORT_NAME)
lidar.clean_input()

# used to scale data to fit on the screen
max_distance = 0

#pylint: disable=redefined-outer-name,global-statement
def process_data(data):
    global max_distance
    lcd.fill((255,255,255))
    for angle in range(360):
        distance = data[angle]
        if distance > 0:                  # ignore initially ungathered data points
            max_distance = 3000 #max([min([5000, distance]), max_distance])
            radians = angle * pi / 180.0 - pi/2
            x = distance * cos(radians)
            y = distance * sin(radians)
            point = (SCREEN_W//2 + int(x/max_distance*400), SCREEN_H//2 + int(y/max_distance*400))
            pygame.draw.circle(lcd, (0,0,0), point, 3)
    pygame.display.update()


scan_data = [0]*360
def stop():
    print('Stoping...')
    lidar.stop_motor()
    #lidar.stop()
    #lidar.disconnect()
    quit()

for scan in lidar.iter_scans():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
    for (_, angle, distance) in scan:
        scan_data[min([359, floor(angle)])] = distance
    process_data(scan_data)

