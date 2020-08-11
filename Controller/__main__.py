#!/usr/bin/env python3

import os
import sys
import time
import threading
import picamera
import cognitive_face as CF
import speech_recognition as sr

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, QObject, Qt, pyqtSignal

import Control_Panel
from Functions.Motor import *


video = 'Pictures/video.jpg'
image = ('Pictures/Image_{}.jpg'.format(time.strftime('%a %H:%M:%S')))

r = sr.Recognizer()
m = sr.Microphone(2, 44100, 1024)

key = '4627ffd84df84f9cbfb24fea12aabaa8'
CF.Key.set(key)

credentials_json = open('credentials.json').read()
preferred_phrases = ['hello, hi, start, green light, left, right, red light',
                     'wait','stop', 'bye']            
    
class Stream(QThread):
    picture_signal = pyqtSignal('QString')
    
    def __init__(self):
        QThread.__init__(self)
        self.capture = False

    def start_capture(self):
        self.capture = True
        
    def stop(self):
        self.running = False

    def capturing(self, camera):
        self.capture = False
        picture = image
        camera.capture(picture, use_video_port = True)
        self.picture_signal.emit(picture)
        

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
                
    def run(self):
        self.running = True
        with picamera.PiCamera() as camera:
            camera.start_preview()
            camera.resolution = (480, 800)
            while self.running:
                QApplication.processEvents()
                camera.capture(video, use_video_port=True)
                if self.capture:
                    t = threading.Thread(target=self.capturing, args=(camera,))
                    t.daemon = True
                    t.start()
                msg = self.do_recognition(video)
                camera.annotate_foreground = picamera.Color('black')
                camera.annotate_text = msg
                QApplication.processEvents()
                time.sleep(1)
            
        os.remove(video)
            
class MainWindow(QMainWindow, Control_Panel.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stream_thread = Stream()
        self.background_listening()
        self.Camera_Btn.setEnabled(False)
        self.signals()
        
    def callback(self, r, audio):
        # received audio data,
        # now we'll recognize it using Google Speech Recognition
        self.Listening_Led.setPixmap(QtGui.QPixmap("Assets/orange-circle.png"))
        try:
            AudioData = r.recognize_google_cloud(audio,
                            credentials_json, 'en-US', preferred_phrases)
            speech.command(AudioData)
        except sr.UnknownValueError:
            self.Listening_Led.setPixmap(QtGui.QPixmap("Assets/red-circle.gif"))    
        except sr.RequestError as e:
            self.Listening_Led.setPixmap(QtGui.QPixmap("Assets/red-circle.gif"))    
        
    
        r.adjust_for_ambient_noise(m)
        r.dynamic_energy_threshold = True
        print("Dynamic energy threshold is set to " + str(r.energy_threshold))
        self.Listening_Led.setPixmap(QtGui.QPixmap("Assets/green-circle.gif"))

        time.sleep(.5)        
        
    def background_listening(self):
        with m as source:
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = True
            print("Dynamic energy threshold is set to " + str(r.energy_threshold))
            self.Listening_Led.setPixmap(QtGui.QPixmap("Assets/green-circle.gif"))
            
        # start listening in the background
        # (note that we don't have to do this inside a `with` statement)
        self.stop_listening = r.listen_in_background(m, self.callback, 3)
           

    def signals(self):
        self.Video_CheckBtn.clicked.connect(lambda: self.start_streaming())
        self.Camera_Btn.clicked.connect(lambda: self.start_capture())
        self.stream_thread.picture_signal.connect(self.display)
        
    def start_capture(self):
        if self.stream_thread.isRunning():
            self.stream_thread.start_capture()
            self.Camera_Btn.setEnabled(False)
            
            
    def start_streaming(self):
        if self.Video_CheckBtn.isChecked():
            self.stream_thread.start()
            self.Camera_Btn.setEnabled(True)
        else:
            self.stream_thread.stop()
            self.Camera_Btn.setEnabled(False)
    
    def display(self, picture):
        self.Picture_Display.setPixmap(QtGui.QPixmap(picture))
        self.Camera_Btn.setEnabled(True)
            
    def keyPressEvent(self, e):
        """
        Function to detect key presses

        :param self: The GUI
        :param e: The event in which a key is pressed
        """
        
        key = e.key()
        

        # motor controls
        if key == Qt.Key_Q:
            motor.stop()
        elif key == Qt.Key_W:
            motor.foward()
        elif key == Qt.Key_A:
            motor.turn_left()
        elif key == Qt.Key_S:
            motor.reverse()
        elif key == Qt.Key_D:
            motor.turn_right()
            
        # for testing purposes
        if key == Qt.Key_Escape:
            # ends the whole programe
            motor.stop()
            self.stop_listening()
            self.stream_thread.stop()
            self.close()
        
        

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
