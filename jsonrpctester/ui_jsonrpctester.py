# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jsonrpctester/jsonrpctester.ui'
#
# Created: Sun Jan  4 22:02:46 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 468)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 305, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelURL = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelURL.setObjectName("labelURL")
        self.gridLayout_2.addWidget(self.labelURL, 0, 0, 1, 1)
        self.labelMethod = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelMethod.setObjectName("labelMethod")
        self.gridLayout_2.addWidget(self.labelMethod, 1, 0, 1, 1)
        self.pushButtonSend = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.gridLayout_2.addWidget(self.pushButtonSend, 3, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 2)
        self.lineEditMethod = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMethod.setObjectName("lineEditMethod")
        self.gridLayout_2.addWidget(self.lineEditMethod, 1, 1, 1, 2)
        self.lineEditURL = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditURL.setObjectName("lineEditURL")
        self.gridLayout_2.addWidget(self.lineEditURL, 0, 1, 1, 2)
        self.groupBoxError = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxError.setObjectName("groupBoxError")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBoxError)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEditError = QtGui.QTextEdit(self.groupBoxError)
        self.textEditError.setObjectName("textEditError")
        self.horizontalLayout_3.addWidget(self.textEditError)
        self.gridLayout_2.addWidget(self.groupBoxError, 4, 0, 1, 3)
        self.groupBoxParameters = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxParameters.setObjectName("groupBoxParameters")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBoxParameters)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEditParameters = QtGui.QTextEdit(self.groupBoxParameters)
        self.textEditParameters.setObjectName("textEditParameters")
        self.horizontalLayout_2.addWidget(self.textEditParameters)
        self.gridLayout_2.addWidget(self.groupBoxParameters, 2, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.groupBoxResult = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxResult.setObjectName("groupBoxResult")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBoxResult)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEditResult = QtGui.QTextEdit(self.groupBoxResult)
        self.textEditResult.setEnabled(False)
        self.textEditResult.setObjectName("textEditResult")
        self.horizontalLayout_4.addWidget(self.textEditResult)
        self.horizontalLayout.addWidget(self.groupBoxResult)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "JsonRPCTester", None, QtGui.QApplication.UnicodeUTF8))
        self.labelURL.setText(QtGui.QApplication.translate("MainWindow", "URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMethod.setText(QtGui.QApplication.translate("MainWindow", "Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSend.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxError.setTitle(QtGui.QApplication.translate("MainWindow", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxParameters.setTitle(QtGui.QApplication.translate("MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxResult.setTitle(QtGui.QApplication.translate("MainWindow", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditResult.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Fill out form and press send...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

