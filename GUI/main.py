# always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import mainwindow
 
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    # access variables inside of the UI's file

    # functions for the buttons to call
    def pressedFwd(self):
        print("CHARGE!!!")
    def pressedRvr(self):
        print("Tatical retreat")
    def pressedTL(self):
        print("Turning Left")
    def pressedTR(self):
        print("Turning Right")
    def pressedStop(self):
        print("I'm out of juice")

    # xCamera is a toggleble pushbutton,
    # because .setCheckable(True) in mainwindow files
    def CameraToggle(self):
        # this is how you toggle bewteen bool states
        if self.xCamera.isChecked():
            print("GoPro Go!")
        else:
            print("GoPro Off!")

    # xSpdSld is a slider function
    def Speed(self):
        # defining the value
        value = self.xSpdSld.value()

        if value == 0:
            print("Speed is currently at 0!")
        elif value >= 0 and value <= 10:
            print("Now we're getting somewhere")
        elif value >=10 and value <= 20:
            print("We have achieve liftoff")
        else:
            print("Entering light speed!")

    # Display Speed
    def SpdDisplay(self):
        # value is rounded off to the nearest 10 to look nice
        value = self.xSpdSld.value()
        value = (value+9)//10*10
        self.ySpdDisplay.display(value)
        
        

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        #button functions
        self.xFwdBtn.clicked.connect(lambda: self.pressedFwd())
        self.xRvrBtn.clicked.connect(lambda: self.pressedRvr())
        self.xTLBtn.clicked.connect(lambda: self.pressedTL())
        self.xTRBtn.clicked.connect(lambda: self.pressedTR())
        self.xStopBtn.clicked.connect(lambda: self.pressedStop())
        self.xCamera.clicked[bool].connect(lambda: self.CameraToggle())
        self.xSpdSld.valueChanged[int].connect(lambda: self.Speed())
        self.xSpdSld.valueChanged[int].connect(lambda: self.SpdDisplay())
 
# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
     main()
