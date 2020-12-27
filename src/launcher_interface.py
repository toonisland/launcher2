# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt_dev\launcher_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LauncherWindow(object):
    def setupUi(self, LauncherWindow):
        LauncherWindow.setObjectName("LauncherWindow")
        LauncherWindow.setEnabled(True)
        LauncherWindow.resize(930, 635)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LauncherWindow.sizePolicy().hasHeightForWidth())
        LauncherWindow.setSizePolicy(sizePolicy)
        LauncherWindow.setMinimumSize(QtCore.QSize(930, 635))
        LauncherWindow.setMaximumSize(QtCore.QSize(930, 635))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        LauncherWindow.setFont(font)
        LauncherWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LauncherWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setGeometry(QtCore.QRect(20, 560, 891, 51))
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setStyleSheet("QProgressBar:horizontal {\n"
"background-color: rgba(249,249,249, 1);\n"
"border-radius: 8;\n"
"border: 2px solid #cacaca;\n"
"padding: 0px;\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk:horizontal {\n"
"background-color: #1c65a0;\n"
"border-radius: 6;\n"
"}")
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progress_bar.setObjectName("progress_bar")
        self.launcher_status = QtWidgets.QLabel(self.centralwidget)
        self.launcher_status.setGeometry(QtCore.QRect(30, 520, 871, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.launcher_status.setFont(font)
        self.launcher_status.setAutoFillBackground(False)
        self.launcher_status.setStyleSheet("QLabel {\n"
"background-color: rgba(249,249,249, 0);\n"
"border-radius: 0;\n"
"border: 0px solid #ffffff;\n"
"}")
        self.launcher_status.setAlignment(QtCore.Qt.AlignCenter)
        self.launcher_status.setObjectName("launcher_status")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(807, 287, 82, 49))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setStyleSheet("QPushButton { \n"
"    color: white;\n"
"    background: #cc3018;\n"
"    border-radius: 8;\n"
"    border: 4px solid #cacaca;\n"
"    padding: 0px;\n"
"    font: 12pt;}\n"
"QPushButton:hover { \n"
"    background: #dd3d23;\n"
"}")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(562, 313, 245, 37))
        self.pass_input.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pass_input.setStyleSheet("background: white;\n"
"border-radius: 8;\n"
"border: 2px solid #cacaca;\n"
"padding: 0px;\n"
"font: 12pt \"Arial\";")
        self.pass_input.setText("")
        self.pass_input.setFrame(False)
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(562, 271, 245, 37))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.user_input.setFont(font)
        self.user_input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.user_input.setStyleSheet("background: white;\n"
"border-radius: 8;\n"
"border: 2px solid #cacaca;\n"
"padding: 0px;\n"
"font: 12pt \"Arial\";")
        self.user_input.setText("")
        self.user_input.setFrame(False)
        self.user_input.setObjectName("user_input")
        self.launcher_state = QtWidgets.QLabel(self.centralwidget)
        self.launcher_state.setGeometry(QtCore.QRect(460, 240, 411, 31))
        self.launcher_state.setStyleSheet("background-color: rgba(249,249,249, 0);\n"
"border-radius: 5;\n"
"border: 0px solid #ffffff;\n"
"padding: 0px;\n"
"font: 14pt;")
        self.launcher_state.setAlignment(QtCore.Qt.AlignCenter)
        self.launcher_state.setObjectName("launcher_state")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 950, 655))
        self.frame.setStyleSheet("image: url(:/images/resources/images/Launcher.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(90, 120, 311, 361))
        self.textEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setLineWidth(0)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setObjectName("textEdit")
        self.frame.raise_()
        self.progress_bar.raise_()
        self.launcher_status.raise_()
        self.pushButton.raise_()
        self.pass_input.raise_()
        self.user_input.raise_()
        self.launcher_state.raise_()
        LauncherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LauncherWindow)
        QtCore.QMetaObject.connectSlotsByName(LauncherWindow)

    def retranslateUi(self, LauncherWindow):
        _translate = QtCore.QCoreApplication.translate
        LauncherWindow.setWindowTitle(_translate("LauncherWindow", "Toon Island Launcher"))
        self.progress_bar.setFormat(_translate("LauncherWindow", "%p%"))
        self.launcher_status.setText(_translate("LauncherWindow", "Status"))
        self.pushButton.setText(_translate("LauncherWindow", "Play!"))
        self.pass_input.setPlaceholderText(_translate("LauncherWindow", "password"))
        self.user_input.setPlaceholderText(_translate("LauncherWindow", "username"))
        self.launcher_state.setText(_translate("LauncherWindow", "State"))
        self.textEdit.setHtml(_translate("LauncherWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#5e9ca0;\">News!</span><span style=\" font-size:36pt;\"> </span></p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#2e6c80;\">1.0.0:</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Released Launcher</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\"> </span></p></body></html>"))
import resources_rc
