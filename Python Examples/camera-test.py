import cv2

capture_device = 0
capture_fps = 30
capture_width = 640
capture_height = 480
width = 224
height = 224

#camera_id = 'nvarguscamerasrc sensor-id=%d ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 ! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! videoconvert ! appsink' % (
#                capture_device, capture_width, capture_height, capture_fps, width, height)

#print(camera_id)

# cap = cv2.VideoCapture(0)  
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# cam_running = True
# while cam_running:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

cap = cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)RG10, framerate=(fraction)10/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)
if not cap.isOpened:
    print("no camera")
else:
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Could not read image")
cv2.imshow("frame", frame)
cv2.waitKey(0)
