from lidar import LidarJet
lid = LidarJet('/dev/ttyACM1')
with open("zdjecie.jpg", "wb") as file:
    file.write(lid.read_frame_jpg())