# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 800)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Camera_Btn = QtWidgets.QPushButton(self.centralWidget)
        self.Camera_Btn.setGeometry(QtCore.QRect(310, 650, 140, 80))
        self.Camera_Btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/camera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Camera_Btn.setIcon(icon)
        self.Camera_Btn.setIconSize(QtCore.QSize(60, 60))
        self.Camera_Btn.setObjectName("Camera_Btn")
        self.Video_CheckBtn = QtWidgets.QPushButton(self.centralWidget)
        self.Video_CheckBtn.setGeometry(QtCore.QRect(30, 650, 140, 80))
        self.Video_CheckBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Assets/video-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Video_CheckBtn.setIcon(icon1)
        self.Video_CheckBtn.setIconSize(QtCore.QSize(60, 60))
        self.Video_CheckBtn.setCheckable(True)
        self.Video_CheckBtn.setObjectName("Video_CheckBtn")
        self.Picture_Display = QtWidgets.QLabel(self.centralWidget)
        self.Picture_Display.setGeometry(QtCore.QRect(60, 20, 360, 600))
        self.Picture_Display.setScaledContents(True)
        self.Picture_Display.setObjectName("Picture_Display")
        self.Listening_Led = QtWidgets.QLabel(self.centralWidget)
        self.Listening_Led.setGeometry(QtCore.QRect(210, 660, 60, 60))
        self.Listening_Led.setText("")
        self.Listening_Led.setScaledContents(True)
        self.Listening_Led.setObjectName("Listening_Led")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 480, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Education Robot Controller"))
        self.Picture_Display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">PICTURE GOES HERE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

