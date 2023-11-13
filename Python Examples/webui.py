from flask import Flask, render_template, Response
from camera import CameraJet
from lidar import LidarJet
from multiprocessing import Process
from steering import CarJet

def steerCar():
    car = CarJet()
    car.start_steering()

steering = Process(target=steerCar)
steering.start()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def gen_c(camera):
    while True:
        frame = camera.read_frame_jpg()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def gen_l(lidar):
    while True:
        frame = lidar.read_frame_jpg()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    cam = CameraJet()
    return Response(gen_c(cam),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/lidar')
def lidar_feed():
    lid = LidarJet('/dev/ttyACM1')
    return Response(gen_l(lid),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':  
    app.run(host='0.0.0.0', debug=True)