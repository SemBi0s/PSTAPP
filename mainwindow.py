# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PST_APPkLLlyA.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import subprocess

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))


        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.StartBtn = QPushButton(self.centralwidget)
        self.StartBtn.setObjectName(u"StartBtn")
        self.StartBtn.setGeometry(QRect(210, 50, 381, 291))
        self.StartBtn.setLayoutDirection(Qt.LeftToRight)
        self.ConnectedText = QTextBrowser(self.centralwidget)
        self.ConnectedText.setObjectName(u"ConnectedText")
        self.ConnectedText.setEnabled(False)
        self.ConnectedText.setGeometry(QRect(540, 410, 241, 61))
        self.ConnectedText.setMouseTracking(False)
        self.ConnectedText.setLayoutDirection(Qt.LeftToRight)
        self.ConnectedText.setAutoFillBackground(True)
        self.DisconnectedText = QTextBrowser(self.centralwidget)
        self.DisconnectedText.setObjectName(u"DisconnectedText")
        self.DisconnectedText.setEnabled(False)
        self.DisconnectedText.setGeometry(QRect(10, 410, 321, 61))
        self.DisconnectedText.setMouseTracking(False)
        self.DisconnectedText.setLayoutDirection(Qt.LeftToRight)
        self.DisconnectedText.setAutoFillBackground(True)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(160, 370, 461, 21))
        self.progressBar.setMaximumSize(QSize(800, 480))
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setValue(0)
        self.CloseBtn = QPushButton(self.centralwidget)
        self.CloseBtn.setObjectName(u"CloseBtn")
        self.CloseBtn.setGeometry(QRect(760, 10, 31, 31))
        self.CloseBtn.setLayoutDirection(Qt.LeftToRight)
        self.RestartBtn = QPushButton(self.centralwidget)
        self.RestartBtn.setObjectName(u"RestartBtn")
        self.RestartBtn.setGeometry(QRect(10, 10, 31, 31))
        self.RestartBtn.setLayoutDirection(Qt.LeftToRight)
        self.RestartBtn.clicked.connect(self.checkConnected)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.CloseBtn.clicked.connect(MainWindow.close)
        self.checkConnected()
        self.showFullScreen()
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PST APP", None))
        self.StartBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ConnectedText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700; color:#57e389;\">CONNECTED</span></p></body></html>", None))
        self.DisconnectedText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700; color:#e01b24;\">DISCONNECTED</span></p></body></html>", None))
        self.CloseBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.RestartBtn.setText(QCoreApplication.translate("MainWindow", u"\u21ba", None))
    # retranslateUi

    def checkConnected(self):
                
        output = os.popen("nfc-list").read()
        print(output)
        if "No NFC device found." in output:
            self.DisconnectedText.show()
            self.ConnectedText.hide()
            self.StartBtn.setEnabled(False)
            
        else:
            self.DisconnectedText.hide()
            self.ConnectedText.show()
            self.StartBtn.setEnabled(True)
