#!/usr/bin/env python3

# NOTE: this test requires the picamera to be connected to the Pi

import os
import time
import picamera
import cognitive_face as CF

def do_recognition(self,image):
    """
    Request for recognition for the image for the detected face's
    age, gender and emotion, and sort the results for display.

    :image: image path

    Returns:
        Sorted facial attributes for one detected face.
    """
    res = CF.face.detect(image, False, False, 'age,gender,emotion')
    if any('faceAttributes' in x for x in res):
        face_att = res[0]['faceAttributes']
        if any ('gender' in x for x in face_att):
            gender = face_att['gender']
        if any ('age' in x for x in face_att):
            age = face_att['age']
        if any ('emotion' in x for x in face_att):
            emotion_list = face_att['emotion']
            emotion_level = (sorted(emotion_list ,key=emotion_list.get)[-1])
        return ('Gender: {}\nAge: {}\nEmotion:{}\n'.format(gender, age, emotion_level))
    else:
        return 'No Face Detected'
            
def main():
    try:
        with picamera.PiCamera() as camera:
            # starts streaming
            camera.start_preview()
            camera.resolution = (480, 800)
            while True:
                # starts real-time face recognition
                camera.capture('Video_Test.jpg', use_video_port=True)
                msg = do_recognition(video)
                print (msg)
                camera.annotate_foreground = picamera.Color('black')
                camera.annotate_text = msg
                # this is to prevent from exceeding API request limit
                time.sleep(1)
                
    except KeyboardInterrupt:            
        os.remove('Video_Test.jpg')
        print("Face recognition test stopped")

if __name__ == "__main__": main()
