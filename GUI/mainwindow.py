# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 379)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.xStopBtn = QtWidgets.QPushButton(self.centralWidget)
        self.xStopBtn.setGeometry(QtCore.QRect(100, 140, 51, 23))
        self.xStopBtn.setObjectName("xStopBtn")
        self.xFwdBtn = QtWidgets.QPushButton(self.centralWidget)
        self.xFwdBtn.setGeometry(QtCore.QRect(90, 100, 71, 23))
        self.xFwdBtn.setObjectName("xFwdBtn")
        self.xTLBtn = QtWidgets.QPushButton(self.centralWidget)
        self.xTLBtn.setGeometry(QtCore.QRect(20, 140, 61, 23))
        self.xTLBtn.setObjectName("xTLBtn")
        self.xRvrBtn = QtWidgets.QPushButton(self.centralWidget)
        self.xRvrBtn.setGeometry(QtCore.QRect(90, 180, 75, 23))
        self.xRvrBtn.setObjectName("xRvrBtn")
        self.xTRBtn = QtWidgets.QPushButton(self.centralWidget)
        self.xTRBtn.setGeometry(QtCore.QRect(170, 140, 61, 23))
        self.xTRBtn.setObjectName("xTRBtn")
        self.xSpdSld = QtWidgets.QSlider(self.centralWidget)
        self.xSpdSld.setGeometry(QtCore.QRect(540, 70, 19, 160))
        self.xSpdSld.setMaximum(30)
        self.xSpdSld.setSingleStep(10)
        self.xSpdSld.setTracking(False)
        self.xSpdSld.setOrientation(QtCore.Qt.Vertical)
        self.xSpdSld.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.xSpdSld.setTickInterval(10)
        self.xSpdSld.setObjectName("xSpdSld")
        self.ySpdDisplay = QtWidgets.QLCDNumber(self.centralWidget)
        self.ySpdDisplay.setGeometry(QtCore.QRect(530, 280, 64, 23))
        self.ySpdDisplay.setObjectName("ySpdDisplay")
        self.xCamera = QtWidgets.QPushButton(self.centralWidget)
        self.xCamera.setGeometry(QtCore.QRect(90, 250, 75, 23))
        self.xCamera.setCheckable(True)
        self.xCamera.setObjectName("xCamera")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.xStopBtn.setText(_translate("MainWindow", "Stop"))
        self.xFwdBtn.setText(_translate("MainWindow", "Foward"))
        self.xTLBtn.setText(_translate("MainWindow", "Left"))
        self.xRvrBtn.setText(_translate("MainWindow", "Reverse"))
        self.xTRBtn.setText(_translate("MainWindow", "Right"))
        self.xCamera.setText(_translate("MainWindow", "Camera"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

