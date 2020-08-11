import time
import picamera

with picamera.PiCamera() as camera:
    try:
        camera.resolution = (480, 800)
        camera.framerate = 24
        camera.start_preview()
        time.sleep(5)
        camera.capture('image_test.jpg')
    except KeyboardInterrupt:
        print("Capture test stopped")
