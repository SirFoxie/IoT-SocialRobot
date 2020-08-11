import picamera
import time

with picamera.PiCamera() as camera:
    try:
        camera.start_preview()
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        camera.stop_preview()
        print('Video test stopped')
    
